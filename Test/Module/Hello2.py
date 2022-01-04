from .Hello import Hello

class Hello2(Hello):
    def __init__(self):
        super().__init__()
        print('init Hello 2')
    
    def Hi_1(self):
        return 'Hello world ex 1'
    
    def Hi_2(self, msg: str):
        return msg