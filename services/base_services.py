import sys
import logging
import requests

from logging import StreamHandler, Formatter, FileHandler


class BaseService:
    response = None
    response_json = None
    logger = None

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = StreamHandler(stream=sys.stdout)
        handler.setFormatter(Formatter(fmt='%(asctime)s %(levelname)s %(message)s'))
        file_handler = FileHandler(r'C:\Users\Admin\PycharmProjects\Qa16-autoTesti-\services\store1\store1.log')
        file_handler.setFormatter(Formatter(fmt='%(asctime)s %(levelname)s %(message)s'))
        self.logger.addHandler(handler)
        self.logger.addHandler(file_handler)

    def get(self, url):
        self.response = requests.get(url)
        if self.response.status_code == 200:
            self.logger.info("Cod 200 for get request")
            return self.response.json()
        else:
            self.logger.info("Fail cod 200 for get request")
            assert False

    def post(self, url, some_dict):
        self.response = requests.post(url, json=some_dict)
        if self.response.status_code == 200:
            self.logger.info("Received cod 200 for post request")
            return self.response.json()
        else:
            self.logger.info("Fail cod 200 for post request")
            assert False

    def delete(self, url):
        self.response = requests.delete(url)
        if self.response.status_code == 200:
            self.logger.info("Cod 200 for delete request")
            return self.response.json()
        else:
            self.logger.info("Fail cod 200 for delete request")
            assert False

    def put(self, url, some_dict: dict):
        self.response = requests.put(url, json=some_dict)
        if self.response.status_code == 200:
            self.logger.info("Cod 200 for put request")
            return self.response.json()
        else:
            self.logger.info("Fail cod 200 for put request")
            assert False

    def check_id(self, obj_id: int):
        try:
            self.logger.info("Try received id")
            assert self.response_json['id'] == obj_id, "we have got other id"
        except AssertionError as e:
            self.logger.error(f"Check for id: {obj_id} failed", str(e), exc_info=True)
