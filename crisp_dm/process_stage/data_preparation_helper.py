from crisp_dm.process_stage.data_processing_helper import DataProcessingHelper
from utils.exception import MyException

class DataPrepairationHelper(DataProcessingHelper):
    def __init__(self):
        pass

    def validate_data(self, *args):
        data = args[0] if len(args) >= 1 else None

        if data is None:
            raise MyException("Missing data!")

    def run(self, *args):
        data = args[0]
        return data