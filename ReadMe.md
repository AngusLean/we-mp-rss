<div align="center">
<img src="static/logo.svg" alt="We-MP-RSS Logo" width="20%">
<h1>WeRSS - WeChat Official Account RSS Subscription Assistant</h1>

[![Python Version](https://img.shields.io/badge/python-3.13.1+-red.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

[中文](README.zh-CN.md)|[English](ReadMe.md)
</div>

## One-line Compose Deploy From Your GitHub Fork

```bash
mkdir -p we-mp-rss && cd we-mp-rss && PASSWORD='change-this-password' WE_MP_RSS_IMAGE=ghcr.io/AngusLean/we-mp-rss:latest docker compose -f <(curl -fsSL https://raw.githubusercontent.com/AngusLean/we-mp-rss/main/compose/docker-compose-sqlite.yaml) up -d
```

Push your fork to `main`, wait for GitHub Actions to publish `ghcr.io/AngusLean/we-mp-rss:latest`, then run the command above.

- Default port mapping is `8002:8001`
- Default database is `SQLite`, with data stored in `./data`
- Proxy is disabled by default and timezone defaults to `Asia/Shanghai`
- If your NAS shell is only `/bin/sh`, start `bash` first and then run the command above

Visit `http://<your-ip>:8002/`

## Alibaba Cloud ACR / ACK Private Image Flow

- If you have already bound your GitHub repository in Alibaba Cloud, pushing code to GitHub will trigger the platform to build and publish the private image automatically
- Private image format: `registry.cn-<region>.aliyuncs.com/<namespace>/we-mp-rss:latest`
- On NAS, replace `WE_MP_RSS_IMAGE` with that ACR image address

```bash
PASSWORD='change-this-password' WE_MP_RSS_IMAGE=registry.cn-<region>.aliyuncs.com/<namespace>/we-mp-rss:latest docker compose -f <(curl -fsSL https://raw.githubusercontent.com/AngusLean/we-mp-rss/main/compose/docker-compose-sqlite.yaml) up -d
```

- Before ACK pulls the private image, create an image pull secret:

```bash
kubectl create secret docker-registry regsecret \
  --docker-server=registry.cn-<region>.aliyuncs.com \
  --docker-username='<acr-login-name>' \
  --docker-password='<acr-password>' \
  -n default
```

- Then replace the image, password, and namespace values in `compose/ack-private-image.yaml` and apply it:

```bash
kubectl apply -f compose/ack-private-image.yaml
```

## Quick Start

```bash
docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data ghcr.io/rachelos/we-mp-rss:latest
```

Visit `http://<your-ip>:8001/` to get started.

## Quick Upgrade

```bash
docker stop we-mp-rss
docker rm we-mp-rss
docker pull ghcr.io/rachelos/we-mp-rss:latest
# If you added other parameters, please modify accordingly
docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data ghcr.io/rachelos/we-mp-rss:latest
```

## Official Image

```bash
docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data rachelos/we-mp-rss:latest
```

## Proxy Mirror For Faster Access

```bash
docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data docker.1ms.run/rachelos/we-mp-rss:latest
```

## Special Thanks

cyChaos, 子健MeLift, 晨阳, 童总, 胜宇, 军亮, 余光, 一路向北, 水煮土豆丝, 人可, 须臾, 澄明, 五梭, Jarvis, 三三, 哈基米, 苹果
