import pytest
import sys
import os
test_path = os.path.dirname(__file__)
sys.path.insert(0,os.path.dirname(test_path))
from Worker.Worker import Worker

def test_worker():
    worker = Worker()
    print(worker.GetIdentity())
    res = worker.Handle('{"module": "Test.Module.Hello4", "class": "", "func": "Hi_2", "args": ["test"], "kwargs": {}}')
    print(res)
    worker.Stop()

if __name__ == '__main__':
    #pytest.main(['-s', '-v', '--junit-xml', f'{test_path}/Worker_Test_Report.xml', __file__])
    print(str(({'test': 1}, True)))
