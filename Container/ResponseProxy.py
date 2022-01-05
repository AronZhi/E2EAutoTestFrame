import json

class ResponseProxy:
    def GetValueType(self, value):
        if type(value) is dict:
            return 'dict'
        elif type(value) is list:
            return 'list'
        elif type(value) is tuple:
            return 'tuple'
        elif type(value) is str:
            return 'str'
        elif type(value) is bool:
            return 'bool'
        elif type(value) is float:
            return 'float'
        else:
            return 'int'

    def ConstrutBody(self, ret_value, error_msg):
        data_type = self.GetValueType(ret_value)
        data = {'ret_value': ret_value, 'type': data_type, 'error_msg': str(error_msg)}
        body = json.dumps(data, ensure_ascii=False)
        return body
    
    def FormatResponse(self, response:str):
        data = json.loads(response)
        if data['type'] == 'tuple':
            data['ret_value'] = tuple(data['ret_value'])
        return data