from utils.exception import MyException

class DataProcessingHelper(object):
    def __init__(self):
        pass

    def validate_data(self, *args):
        pass

    def process(self, *args):
        try:
            self.validate_data(*args)
            return self.run(*args)
        except MyException, (exception):
            print exception.msg

    def run(self, *args):
        pass