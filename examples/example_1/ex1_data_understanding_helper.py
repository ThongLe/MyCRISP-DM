from crisp_dm.helpers.data_understanding_helper import DataUnderstandingHelper

class Ex1DataUnderstandingHelper(DataUnderstandingHelper):
    def __init__(self):
        pass

    def run(self, *args):
        data = args[0]

        # define your code here ====================

        for field in ['sales', 'salary']:
            for value in data[field].unique():
                new_field = '_'.join([field, str(value)])
                data[new_field] = 0
                data[new_field][data[field] == value] = 1


        data = data[[field for field in data.columns if field not in ['sales', 'salary']]]

        # ==========================================

        return data