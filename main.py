from SearchAlgorithm import *
from TestCases import *
from utils import *


if __name__ == '__main__':
    testCases = TestCases()
    testCases.setUp()
    testCases.test_Expand()
    testCases.test_RemoveCycles()
    testCases.test_depth_first_search()
    testCases.test_breadth_first_search()
    testCases.test_coord2station()



