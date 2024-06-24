## 创作背景

> 适配nacos2.0API，官网API地址： https://nacos.io/zh-cn/docs/v2/guide/user/open-api.html

## 安装

`pip3 install pnacos`

## 使用

```python
from pnacos.client import NacosClient
from pnacos.config import NacosConfig

client = NacosClient("172.26.22.201:300002", username="nacos", password="nacos123456")
cfg = NacosConfig(client)
```