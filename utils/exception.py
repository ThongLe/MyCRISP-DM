class MyException(Exception):
    def __init__(self, value):
        self.msg = value

    def __str__(self):
        return repr(self.msg)