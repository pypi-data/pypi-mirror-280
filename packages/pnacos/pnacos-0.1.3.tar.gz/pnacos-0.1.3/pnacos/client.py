import requests
import logging
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout
from urllib3.util import Retry

from pnacos import NACOS_URL


class HttpClient:
    def __init__(self, max_retries=3, backoff_factor=0.3, timeout=10, pool_maxsize=10):
        """
        初始化HTTP客户端

        :param max_retries: 最大重试次数
        :param backoff_factor: 重试间隔时间因子
        :param timeout: 请求超时时间（秒）
        :param pool_maxsize: 连接池的最大连接数
        """
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.timeout = timeout

        # 初始化Session和连接池
        self.session = requests.Session()
        retries = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retries, pool_maxsize=pool_maxsize)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def request(self, method, url, **kwargs):
        """
        发送HTTP请求，失败时重试

        :param method: 请求方法（GET, POST, DELETE等）
        :param url: 请求的URL
        :param kwargs: 其他参数，如headers, params, data, json等
        :return: 响应对象
        """
        method = method.upper()
        if method not in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD']:
            raise ValueError("Unsupported HTTP method")
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()  # 如果响应状态码不是200，抛出HTTPError
        except (HTTPError, ConnectionError, Timeout) as e:
            logging.error(f"Request failed: {e}. No more retries left.")
        except RequestException as e:
            logging.error(f"Request failed with an unexpected error: {e}")
        return response


# 客户端初始化
client = HttpClient()


class NacosClient:
    def __init__(self, server_addresses, username=None, password=None):
        """

        :param server_addresses: 172.26.22.201:30002
        :param namespace_id:
        :param username:
        :param password:
        """
        self.server_addresses = server_addresses
        self.username = username
        self.password = password
        self.client = client
        self.baseurl = 'http://' + self.server_addresses
        if self.username and self.password:
            self.token = self.login()

    def login(self) -> str:
        url = self.baseurl + NACOS_URL.get("LOGIN")
        response = self.client.request('POST', url, data={"username": self.username, "password": self.password})
        if response.status_code != 200:
            raise ConnectionError(f"Login failed: {response.text}")
        return response.json()['accessToken']

    def request(self, method, url, **kwargs):
        if hasattr(self, 'token'):
            if "?" in url:
                url += "&accessToken=" + self.token
            else:
                url += "?accessToken=" + self.token
        return self.client.request(method, url, **kwargs)
