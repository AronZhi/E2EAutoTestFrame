import json
import requests

class RequestProxy:
    def ConstrutBody(self, cls, func_name, *args, **kwargs):
        json_body = {}
        json_body['module'] = cls.__module__
        json_body['class'] = cls.__name__
        json_body['func'] = func_name
        arg_list = []
        for _, item in enumerate(args):
            arg_list.append(item)
        json_body['args'] = arg_list
        json_body['kwargs'] = kwargs
        body = json.dumps(json_body, ensure_ascii=False)
        return body
    
    """
    def Proxy(self, cls, func_name, remote, **kwargs):
        body = self.ConstrutBody(cls, func_name, **kwargs)
        response = requests.post(url=remote, data=body, headers={'Content-Type': 'application/json'})
        try:
            response_data = json.loads(response)
        except Exception as e:
            pass
        return response_data
    """