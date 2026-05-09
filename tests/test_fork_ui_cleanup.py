import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
