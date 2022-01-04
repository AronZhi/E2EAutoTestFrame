import json

class ResponseProxy:
    def ConstrutBody(self, ret_value, error_msg):
        data = {'ret_value': ret_value, 'error_msg': str(error_msg)}
        body = json.dumps(data, ensure_ascii=False)
        return body
