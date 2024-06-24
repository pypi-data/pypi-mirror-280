import json

from pnacos import NACOS_URL
from pnacos.client import NacosClient


class NacosConfig:
    def __init__(self, client: NacosClient):
        self.client = client
        self.path = NACOS_URL.get("CONFIG")

    def get_config(self, namespaceId, group, dataId, tag) -> (bool, dict):
        """
        获取配置
        :return:
        """
        params = {
            "namespaceId": namespaceId,
            "group": group,
            "dataId": dataId,
            "tag": tag
        }

        rsp = self.client.request("GET", self.client.baseurl + self.path, params=params)
        context = rsp.json()
        if context.get("code") != 0:
            return False, {}
        return True, json.loads(context.get("data", {}))


if __name__ == "__main__":
    SERVER_ADDRESSES = "172.26.22.201:30002"
    USERNAME = "nacos"
    PASSWORD = "nacos123456"

    client = NacosClient(SERVER_ADDRESSES, username=USERNAME, password=PASSWORD)
    cfg = NacosConfig(client)
    print(cfg.get_config("90910445-f94b-4581-bb29-4ee46c9f356f", "dev", "user-web", None))
