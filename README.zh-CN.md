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

## 阿里云 ACR / ACK 私有镜像流程

- 如果你已在阿里云平台完成 GitHub 代码源绑定，后续只需要把代码推到 GitHub，阿里云会自动构建并推送私有镜像
- 私有镜像地址格式：`registry.cn-<地域>.aliyuncs.com/<命名空间>/we-mp-rss:latest`
- NAS 上可直接把上面的地址替换进 `WE_MP_RSS_IMAGE`

```bash
PASSWORD='请改成你的强密码' WE_MP_RSS_IMAGE=registry.cn-<地域>.aliyuncs.com/<命名空间>/we-mp-rss:latest docker compose -f <(curl -fsSL https://raw.githubusercontent.com/AngusLean/we-mp-rss/main/compose/docker-compose-sqlite.yaml) up -d
```

- ACK 拉取私有镜像前，先创建镜像仓库登录密钥：

```bash
kubectl create secret docker-registry regsecret \
  --docker-server=registry.cn-<地域>.aliyuncs.com \
  --docker-username='<阿里云镜像仓库登录名>' \
  --docker-password='<阿里云镜像仓库密码>' \
  -n default
```

- 然后把 `compose/ack-private-image.yaml` 里的镜像地址、密码、命名空间按你的实际值替换后执行：

```bash
kubectl apply -f compose/ack-private-image.yaml
```

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
