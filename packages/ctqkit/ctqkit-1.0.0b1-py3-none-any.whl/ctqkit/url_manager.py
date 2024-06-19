class URLManager:
    def __init__(self, client):
        """
        Initializes an instance of URLManager.

        Args:
            client (str): The client type, must be one of 'gd', 'zky', or 'zdx'.

        Raises:
            ValueError: If the client parameter is not a valid value.
        """
        if client not in ["gd", "zky", "zdx"]:
            raise ValueError(
                "client参数只能填写gd(国盾量子计算云平台), zky(中科院量子计算云平台), zdx(中电信天衍量子计算云平台)中的一个"
            )
        self.all_urls = {
            "gd": {
                "laboratory_url": "http://172.16.30.201:9900/experiment/",
                "login_url": "http://172.16.30.201:9900/api-uaa/oauth/token",
            },
            "zdx": {},
            "zky": {},
        }
        self.urls = self.all_urls.get(client)

    def get_url(self, key):
        """
        Fetches a specific URL.

        Args:
            key (str): The key for the URL.

        Returns:
            str or None: The corresponding URL if the key exists; otherwise, None.
        """
        return self.urls.get(key, None)
