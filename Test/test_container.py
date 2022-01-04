import pytest
import sys
import os
test_path = os.path.dirname(__file__)
sys.path.insert(0,os.path.dirname(test_path))
from Container.Container import Container
from Container.RequestProxy import RequestProxy

def test_proxy(): 
    from Api.Hello import Hello
    reqProxy = RequestProxy()
    body = reqProxy.ConstrutBody(Hello, 'Test', '0.0.0.0:9001')
    print(body)

def test_container_1():
    container = Container()
    body = {"module": "Test.Module.Hello", "class": "Hello", "func": "Hi_1", "args": [], "kwargs": {}}
    res = container.CallFunc(body)
    assert res[0] == 'hello world 1'

def test_container_2():
    container = Container()
    body = {"module": "Test.Module.Hello", "class": "Hello", "func": "Hi_2", "args": ['test'], "kwargs": {}}
    res = container.CallFunc(body)
    assert res[0] == 'hello world 2'

def test_container_3():
    container = Container()
    body = {"module": "Test.Module.Hello2", "class": "Hello2", "func": "Hi_2", "args": ['test'], "kwargs": {}}
    res = container.CallFunc(body)
    assert res[0] == 'test'

def test_container_4():
    container = Container()
    body = {"module": "Test.Module.Hello3", "class": "Hello3", "func": "__init__", "args": ['test'], "kwargs": {}}
    res = container.CallFunc(body)
    assert res

def test_container_5():
    container = Container()
    body = {"module": "Test.Module.Hello4", "class": "", "func": "Hi_2", "args": ['test'], "kwargs": {}}
    res = container.CallFunc(body)
    print(res)
    assert res[0] == 'hello world 4_2'

if __name__ == '__main__':
    pytest.main(['-s', '-v', '--junit-xml', f'{test_path}/Proxy_Test_Report.xml', __file__]) 
