import sys
import traceback
from Loger import g_main_log

class Container:
    def __init__(self) -> None:
        self.module_inst = {}
        self.class_inst = {}
        self.last_error = ''
    
    def _HandleError(self, err_msg):
        etype, evalue, tb = sys.exc_info()
        str_list = traceback.format_exception(etype, evalue, tb)
        trace_back = ''
        for str in str_list:
            trace_back += str
        trace_back += err_msg
        g_main_log.error(trace_back)
    
    def GetLastError(self):
        error = self.last_error
        self.last_error = ''
        return error
        

    def GetModelObj(self, module_name):
        if module_name:
            module = self.module_inst.get(module_name, None)
            if module:
                return module
            try:
                if '' != module_name:
                    _from_list = []
                    _sub_modules = module_name.split('.')
                    if len(_sub_modules) > 0:
                        _from_list.append(_sub_modules[-1])
                    module = __import__(module_name, fromlist=_from_list)
                else:
                    module = sys.modules[self.__class__.__module__]
                self.module_inst[module_name] = module
                return module
            except:
                pass
        self._HandleError(f'Get module ("{module_name}") failed.')
        return None
    
    def GetClassObj(self, module_name, class_name, init_args):
        try:
            key = module_name + '.' + class_name
            _class_instance = self.class_inst.get(key, None)
            if _class_instance:
                return _class_instance
            _module = self.GetModelObj(module_name)
            if _module is None:
                return None
            if not hasattr(_module, class_name):
                g_main_log.error('Can not find class \'%s\' in module \'%s\'' % (class_name, module_name))
                return None
            _class = getattr(_module, class_name)
            if hasattr(_class, '__init__'):
                """
                _init_method = getattr(_class, '__init__')
                if hasattr(_init_method, '__code__'):
                    _real_vars = len(_init_method.__code__.co_varnames)
                else:
                    _real_vars = 0
                """
                _class_instance, call_result = self._CallFunc(_class, init_args, {})
                if not call_result:
                    pass
            else:  # not override __init__
                _class_instance = _class()
            self.class_inst[key] = _class_instance
            return _class_instance
        except Exception as e:           
            self._HandleError(f'Create class("{class_name}") instance failed.')
        return None
    
    def _CallFunc(self, func, params, kwparams):
        result = None
        if type(params) not in (tuple, dict, list) or type(kwparams) not in (dict,):
            g_main_log.error('Invalid parameter type (not dict and tuple type)')
            return None, False
        try:
            if type(params) is dict:
                params.update(kwparams)
                result = func(**params)
            else:
                if kwparams is None or len(kwparams) == 0:
                    result = func(*params)
                else:
                    result = func(*params, **kwparams)             
        except Exception as e:
            self._HandleError(str(e))
            return None, False
        return result, True
    
    def CallFunc(self, data):
        module_name = data.get('module', '')
        class_name = data.get('class', '')
        func_name = data.get('func', '')
        args = data.get('args', [])
        kwargs = data.get('kwargs', None)
        if '' != class_name:
            if func_name == '__init__':
                return not (self.GetClassObj(module_name, class_name, args) is None)
            else:
                cls_inst = self.GetClassObj(module_name, class_name, [])
                if cls_inst:
                    func = getattr(cls_inst, func_name)
                    """
                    if func.__code__.co_argcount > 0:
                        if func.__code__.co_varnames[0] == 'self':
                            return self._CallFunc(func, args, kwargs)
                    """
                    return self._CallFunc(func, args, kwargs)
        else:
            module_inst = self.GetModelObj(module_name)
            if module_inst:
                func = getattr(module_inst, func_name)
                return self._CallFunc(func, args, kwargs)
        return None
