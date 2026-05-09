<div align="center">
<img src="static/logo.svg" alt="We-MP-RSS Logo" width="20%">
<h1>WeRSS - 微信公众号订阅助手</h1>

[![Python Version](https://img.shields.io/badge/python-3.13.1+-red.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

[中文](README.zh-CN.md)|[English](ReadMe.md)
</div>

## NAS 一行 Compose 拉起自己的 GitHub Fork

```bash
mkdir -p we-mp-rss && cd we-mp-rss && PASSWORD='请改成你的强密码' WE_MP_RSS_IMAGE=ghcr.io/AngusLean/we-mp-rss:latest docker compose -f <(curl -fsSL https://raw.githubusercontent.com/AngusLean/we-mp-rss/main/compose/docker-compose-sqlite.yaml) up -d
```

先把你的 fork 推到 `main`，等待 GitHub Actions 自动发布镜像到 `ghcr.io/AngusLean/we-mp-rss:latest`，再执行上面的命令。

- 默认端口是 `8002:8001`
- 默认使用 `SQLite`，数据目录是当前目录下的 `./data`
- 默认关闭代理，时区为 `Asia/Shanghai`
- 如果 NAS 只有 `/bin/sh`，先进入 `bash` 再执行这条命令

访问 `http://<您的ip>:8002/`

## 快速运行

```bash
docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data ghcr.io/rachelos/we-mp-rss:latest
```

访问 `http://<您的ip>:8001/` 即可开启。

## 快速升级

```bash
docker stop we-mp-rss
docker rm we-mp-rss
docker pull ghcr.io/rachelos/we-mp-rss:latest
# 如果添加了其它参数，请自行修改
docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data ghcr.io/rachelos/we-mp-rss:latest
```

## 官方镜像

```bash
docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data rachelos/we-mp-rss:latest
```

## 代理镜像加速访问

```bash
docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data docker.1ms.run/rachelos/we-mp-rss:latest
```

## 感谢伙伴

cyChaos、子健MeLift、晨阳、童总、胜宇、军亮、余光、一路向北、水煮土豆丝、人可、须臾、澄明、五梭
