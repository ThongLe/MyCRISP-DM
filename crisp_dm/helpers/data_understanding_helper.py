from crisp_dm.helpers.data_processing_helper import DataProcessingHelper
from utils.exception import MyException

class DataPreparationHelper(DataProcessingHelper):
    def __init__(self):
        pass

    def validate_data(self, *args):
        data    = args[0] if len(args) >= 1 else None
        parse_X = args[1] if len(args) >= 2 else None
        parse_y = args[2] if len(args) >= 3 else None

        if data is None:
            raise MyException("Missing data!")

        if parse_X is None:
            raise MyException("Missing data parser to X!")

        if parse_y is None:
            raise MyException("Missing data parser to Y!")

    def run(self, *args):
        data, parse_X, parse_y = args

        X = parse_X(data)
        y = parse_y(data)

        return X, y