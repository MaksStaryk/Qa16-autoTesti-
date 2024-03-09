class BaseService:
    response = None
    response_json = None

    # url = 'https://petstore.swagger.io/v2/pet'

    def check_cod_200(self, ):
        assert self.response.status_code == 200, f'not 200'

    def status_404(self):
        assert self.response.status_code == 404, 'dont take 404'

    def check_id(self, obj_id: int):
        assert self.response_json['id'] == obj_id, "we have got other id"