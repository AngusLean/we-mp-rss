import unittest
from pathlib import Path
import subprocess
import re


ROOT = Path(__file__).resolve().parents[1]


class ForkUiCleanupTest(unittest.TestCase):
    def test_app_vue_has_no_promo_or_sponsor_modal(self):
        app_vue = (ROOT / "web_ui/src/App.vue").read_text(encoding="utf-8")

        self.assertNotIn("ClawCloud", app_vue)
        self.assertNotIn("云部署", app_vue)
        self.assertNotIn("感谢支持", app_vue)
        self.assertNotIn("showSponsorModal", app_vue)
        self.assertNotIn("uiConfig", app_vue)

    def test_backend_has_no_ui_feature_toggle_hook(self):
        sys_info = (ROOT / "apis/sys_info.py").read_text(encoding="utf-8")

        self.assertNotIn("get_ui_config", sys_info)
        self.assertNotIn("config.ui.yaml", sys_info)

    def test_extra_ui_config_file_is_removed(self):
        self.assertFalse((ROOT / "config.ui.yaml").exists())

    def test_web_ui_dependency_tree_has_no_invalid_peer_deps(self):
        result = subprocess.run(
            ["npm", "ls", "vite", "@vitejs/plugin-vue", "--json"],
            cwd=ROOT / "web_ui",
            capture_output=True,
            text=True,
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=(
                "web_ui 的 Vite / plugin-vue 依赖存在无效 peer dependency，"
                "这会让 dev 启动时容易出现白屏。\n"
                f"stdout:\n{result.stdout}\n\nstderr:\n{result.stderr}"
            ),
        )

    def test_dev_frontend_port_is_consistent(self):
        vite_config = (ROOT / "web_ui/vite.config.ts").read_text(encoding="utf-8")
        dockerfile_dev = (ROOT / "web_ui/Dockerfile.dev").read_text(encoding="utf-8")
        compose_dev = (ROOT / "compose/docker-compose.dev.yaml").read_text(encoding="utf-8")

        self.assertIn('port: 5173', vite_config)
        self.assertIn('--port", "5173"', dockerfile_dev)
        self.assertIn('- "5173:5173"', compose_dev)

    def test_dev_frontend_node_version_matches_vite_requirement(self):
        dockerfile_dev = (ROOT / "web_ui/Dockerfile.dev").read_text(encoding="utf-8")

        self.assertIn("FROM node:22-bookworm-slim", dockerfile_dev)

    def test_static_bundle_is_synced_from_web_ui_dist(self):
        dist_index = (ROOT / "web_ui/dist/index.html").read_text(encoding="utf-8")
        static_index = (ROOT / "static/index.html").read_text(encoding="utf-8")

        self.assertEqual(
            static_index,
            dist_index,
            msg="后端实际提供的是 static/index.html，必须与 web_ui/dist/index.html 保持同步。",
        )

        asset_paths = re.findall(r'/(assets/[^"\']+)', dist_index)
        missing_assets = [asset for asset in asset_paths if not (ROOT / "static" / asset).exists()]
        self.assertFalse(
            missing_assets,
            msg=f"static 目录缺少前端构建产物: {missing_assets}",
        )


if __name__ == "__main__":
    unittest.main()
