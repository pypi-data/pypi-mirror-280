import requests
from fake_useragent import UserAgent as ua


class Http:
    """
    A simple HTTP client class to handle various HTTP requests using the `requests` library.
    For a detailed list of available keyword arguments, refer to:
    https://docs.python-requests.org/en/latest/api/#requests.request
    """

    def __init__(self):
        """Initialize a new HTTP client session."""
        self.session = requests.Session()

    def get(self, url, user_agent=None, timeout=30, proxy=None,
            proxy_username=None, proxy_password=None, **kwargs):
        """
        Send a GET request to the specified URL.

        :param url: The URL to request.
        :param user_agent: Optional user agent string. Defaults to a popular browser's user agent.
        :param timeout: default connection timeout to 30 seconds
        :param proxy: Optional proxy URL.
        :param proxy_username: Optional proxy authentication username.
        :param proxy_password: Optional proxy authentication password.
        :param kwargs: Other optional keyword arguments supported by `requests.get()`.
        :return: Response object.
        """
        return self._request("GET", url, user_agent, proxy, proxy_username, proxy_password, timeout, **kwargs)

    def post(self, url, user_agent=None, proxy=None, proxy_username=None, proxy_password=None, timeout=30,  **kwargs):
        """
        Send a POST request to the specified URL.

        :param url: The URL to request.
        :param user_agent: Optional user agent string. Defaults to a popular browser's user agent.
        :param timeout: default connection timeout to 30 seconds
        :param proxy: Optional proxy URL.
        :param proxy_username: Optional proxy authentication username.
        :param proxy_password: Optional proxy authentication password.
        :param kwargs: Other optional keyword arguments supported by `requests.post()`.
        :return: Response object.
        """
        return self._request("POST", url, user_agent, proxy, proxy_username, proxy_password, timeout, **kwargs)

    def put(self, url, user_agent=None, proxy=None, proxy_username=None, proxy_password=None, **kwargs):
        """
        Send a PUT request to the specified URL.

        :param url: The URL to request.
        :param user_agent: Optional user agent string. Defaults to a popular browser's user agent.
        :param proxy: Optional proxy URL.
        :param proxy_username: Optional proxy authentication username.
        :param proxy_password: Optional proxy authentication password.
        :param kwargs: Other optional keyword arguments supported by `requests.put()`.
        :return: Response object.
        """
        return self._request("PUT", url, user_agent, proxy, proxy_username, proxy_password, **kwargs)

    def patch(self, url, user_agent=None, proxy=None, proxy_username=None, proxy_password=None, **kwargs):
        """
        Send a PATCH request to the specified URL.

        :param url: The URL to request.
        :param user_agent: Optional user agent string. Defaults to a popular browser's user agent.
        :param proxy: Optional proxy URL.
        :param proxy_username: Optional proxy authentication username.
        :param proxy_password: Optional proxy authentication password.
        :param kwargs: Other optional keyword arguments supported by `requests.patch()`.
        :return: Response object.
        """
        return self._request("PATCH", url, user_agent, proxy, proxy_username, proxy_password, **kwargs)

    def delete(self, url, user_agent=None, proxy=None, proxy_username=None, proxy_password=None, **kwargs):
        """
        Send a DELETE request to the specified URL.

        :param url: The URL to request.
        :param user_agent: Optional user agent string. Defaults to a popular browser's user agent.
        :param proxy: Optional proxy URL.
        :param proxy_username: Optional proxy authentication username.
        :param proxy_password: Optional proxy authentication password.
        :param kwargs: Other optional keyword arguments supported by `requests.delete()`.
        :return: Response object.
        """
        return self._request("DELETE", url, user_agent, proxy, proxy_username, proxy_password, **kwargs)

    def head(self, url, user_agent=None, proxy=None, proxy_username=None, proxy_password=None, **kwargs):
        """
        Send a HEAD request to the specified URL.

        :param url: The URL to request.
        :param user_agent: Optional user agent string. Defaults to a popular browser's user agent.
        :param proxy: Optional proxy URL.
        :param proxy_username: Optional proxy authentication username.
        :param proxy_password: Optional proxy authentication password.
        :param kwargs: Other optional keyword arguments supported by `requests.head()`.
        :return: Response object.
        """
        return self._request("HEAD", url, user_agent, proxy, proxy_username, proxy_password, **kwargs)

    def options(self, url, user_agent=None, proxy=None, proxy_username=None, proxy_password=None, **kwargs):
        """
        Send an OPTIONS request to the specified URL.

        :param url: The URL to request.
        :param user_agent: Optional user agent string. Defaults to a popular browser's user agent.
        :param proxy: Optional proxy URL.
        :param proxy_username: Optional proxy authentication username.
        :param proxy_password: Optional proxy authentication password.
        :param kwargs: Other optional keyword arguments supported by `requests.options()`.
        :return: Response object.
        """
        return self._request("OPTIONS", url, user_agent, proxy, proxy_username, proxy_password, **kwargs)

    def _request(self, method, url, user_agent=None, proxy=None, proxy_username=None,
                 proxy_password=None, timeout=None, **kwargs):
        random_ua = ua().random
        DEFAULT_USER_AGENT = random_ua
        HEADERS = {
            "User-Agent": user_agent if user_agent else DEFAULT_USER_AGENT
        }

        if 'headers' in kwargs:
            HEADERS.update(kwargs['headers'])
            del kwargs['headers']

        PROXIES = None
        if proxy:
            if proxy.count(':') >= 2:  # Check if it looks like "host:port" or more complex
                PROXIES = {
                    "http": f"http://{proxy}",
                    "https": f"https://{proxy}"
                }
            else:
                print("Invalid proxy format. Proxy must be in the format 'host:port' or 'username:password@host:port'.")
                return None

        print(f"Making {method} request to {url} with headers: {HEADERS}, proxies: {PROXIES}, timeout: {timeout}")

        try:
            response = self.session.request(method, url, headers=HEADERS, proxies=PROXIES, timeout=timeout, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as err:
            print(f"Error making {method} request to {url}: {err}")
            return None
        except Exception as err:
            print(f"Unexpected error: {err}")
            return None

    def download_file(self, file_name_path, url, user_agent=None, proxy=None,
                      proxy_username=None, proxy_password=None, **kwargs):
        """
        Download a file from the specified URL.

        :param file_name_path: Path to save the downloaded file.
        :param url: The URL of the file to download.
        :param user_agent: Optional user agent string. Defaults to a popular browser's user agent.
        :param proxy: Optional proxy URL.
        :param proxy_username: Optional proxy authentication username.
        :param proxy_password: Optional proxy authentication password.
        :param kwargs: Other optional keyword arguments supported by `requests.get()`.
        """
        response = self.get(url, user_agent=user_agent, proxy=proxy,
                            proxy_username=proxy_username, proxy_password=proxy_password, stream=True, **kwargs)
        if response:
            with open(file_name_path, 'wb') as handle:
                for block in response.iter_content(1024):
                    handle.write(block)

    def start_session(self):
        """Start a new persistent session."""
        self.session = requests.Session()

    def close_session(self):
        """Close the current session."""
        self.session.close()

