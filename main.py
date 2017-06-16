from crisp_dm.crisp_dm_processor import CRISPDMProcessor
from sklearn import linear_model

evaluation_func = lambda c: c > 1

# Test 1
print 'Processor 1:'
processor_1 = CRISPDMProcessor(2, evaluation_func)

processor_1.draw_data = [[0, 0], [1, 1], [0, 1]]
processor_1.parse_X = lambda dt: dt[0:-1]
processor_1.parse_y = lambda dt: dt[-1]
processor_1.model = linear_model.Lasso(alpha=0.1)

processor_1.process()

# Test 2
print '============================================'
print '============================================'
print 'Processor 2:'
processor_2 = CRISPDMProcessor(2, evaluation_func)

processor_2.prepaired_data = [[0, 0], [1, 1], [0, 1]]
processor_2.parse_X = lambda dt: dt[0:-1]
processor_2.parse_y = lambda dt: dt[-1]
processor_2.model = linear_model.Lasso(alpha=0.1)

processor_2.process()

# Test 2
print '============================================'
print '============================================'
print 'Processor 3:'
processor_3 = CRISPDMProcessor(2, evaluation_func)

processor_3.X = [[0, 0], [1, 1]]
processor_3.y = [0, 1]
processor_3.model = linear_model.Lasso(alpha=0.1)

processor_3.process()