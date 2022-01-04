from .Hello import Hello

class Hello3(Hello):
    def __init__(self, msg):
        super().__init__()
        print(msg)