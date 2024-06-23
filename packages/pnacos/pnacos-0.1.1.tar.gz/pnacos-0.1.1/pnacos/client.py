import json
import logging
from urllib.parse import urlencode
import requests

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

NACOS_URL = {
    "CONFIG": "/nacos/v2/cs/config",
}


class NacosClient:
    def __init__(self, server_addresses, namespace_id=None, username=None, password=None, proxies=None):
        self.server_list = self._parse_server_addresses(server_addresses)
        self.current_server = self.server_list[0]
        self.namespace_id = namespace_id
        self.username = username
        self.password = password
        self.proxies = proxies

    def parse_nacos_server_addr(self, server_addr):
        """
        解析Nacos地址
        :param server_addr:
        :return:
        """
        sp = server_addr.split(":")
        port = int(sp[1]) if len(sp) > 1 else 8848
        return sp[0], port

    def _parse_server_addresses(self, server_addresses):
        """
        解析多个Nacos服务地址
        :param server_addresses:
        :return:
        """
        server_list = []
        for server_addr in server_addresses.split(","):
            try:
                server_list.append(self.parse_nacos_server_addr(server_addr.strip()))
            except Exception as e:
                logger.exception(f"[init] Invalid server address: {server_addr}")
                raise ValueError(f"Invalid server address: {server_addr}") from e
        return server_list

    def get_server(self):
        """
        获取当前Nacos服务器
        :return:
        """
        logger.info(f"[get-server] Using server: {self.current_server}")
        return self.current_server

    @staticmethod
    def _get_common_headers():
        return {}

    def _request(self, path, headers, params, data=None, method="GET", timeout=None):
        if self.username and self.password:
            params = params or {}
            params.update({"username": self.username, "password": self.password})

        url = f"{path}?{urlencode(params)}"
        all_headers = self._get_common_headers()
        if headers:
            all_headers.update(headers)

        for tries in range(3):  # 尝试三次
            try:
                address, port = self.get_server()
                server_url = f"http://{address}:{port}"
                response = requests.request(
                    url=server_url + url,
                    data=urlencode(data).encode() if data else None,
                    headers=all_headers,
                    method=method,
                    timeout=timeout,
                    proxies=self.proxies
                )
                response.raise_for_status()  # 检查HTTP错误
                return response
            except requests.RequestException as e:
                logger.error(f"[_request] Try {tries + 1} failed: {e}")
                if tries == 2:  # 最后一次尝试失败后抛出异常
                    raise

    def get_config(self, data_id, group):
        params = {
            "dataId": data_id,
            "group": group,
            "namespaceId": self.namespace_id
        }
        resp = self._request(NACOS_URL["CONFIG"], None, params)
        try:
            data = resp.json().get("data", {})
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON response: {e}")
            data = '{}'
        return data


if __name__ == "__main__":
    SERVER_ADDRESSES = "172.26.22.201:30002"
    NAMESPACE = "90910445-f94b-4581-bb29-4ee46c9f356f"
    USERNAME = "nacos"
    PASSWORD = "nacos123456"

    client = NacosClient(SERVER_ADDRESSES, namespace_id=NAMESPACE, username=USERNAME, password=PASSWORD)

    data_id = "user-web"
    group = "dev"
    try:
        content = client.get_config(data_id, group)
        print("获取的配置内容: ", content)
    except Exception as e:
        logger.error(f"Failed to get config: {e}")
