import sys
import logging

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
        file_handler = FileHandler('store1.log')
        file_handler.setFormatter(Formatter(fmt='%(asctime)s %(levelname)s %(message)s'))
        self.logger.addHandler(handler)
        self.logger.addHandler(file_handler)

    def check_cod_200(self, ):
        try:
            assert self.response.status_code == 200, f'not 200'
        except AssertionError as asert:
            self.logger.error("Check for code 200 failed", exc_info=True)

    def status_404(self):
        try:
            assert self.response.status_code == 404, 'dont take 404'
        except AssertionError as e:
            self.logger.error("Check for code 404 failed", str(e), exc_info=True)

    def check_id(self, obj_id: int):
        try:
            assert self.response_json['id'] == obj_id, "we have got other id"
        except AssertionError as e:
            self.logger.error(f"Check for {obj_id} failed", str(e), exc_info=True)
