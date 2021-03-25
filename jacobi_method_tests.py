import unittest
from jacobi_method import *
import psutil
import os
import time
import csv


def write_to_file(num, memory_usage_, speed_, logic='FAILED'):
    myFile = 'Results.csv'
    with open(myFile, "r") as f:
        reader = csv.reader(f)
        for header in reader:
            break

    with open(myFile, "a", newline='\n') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writerow({header[0]: num, header[1]: memory_usage_, header[2]: speed_, header[3]: logic})


class JMCase(unittest.TestCase):
    def test_1(self):
        A_ = np.array([[2, 1], [5, 7]])
        b_ = np.array([[11], [13]])

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = round((py.memory_info()[0] / 2. ** 30), 8)  # memory use in GB

        start = time.time()
        solution, _ = JM(A_, b_)
        end = time.time()
        speed = round(end - start, 6)  # operating time

        write_to_file(num=1, memory_usage_=memory_usage, speed_=speed, logic='PASSED')
        for pair in zip(solution, [7.111, -3.222]):  # [7.111, -3.222] is exact solution
            self.assertEqual(round(pair[0], 3), pair[1])

    def test_2(self):
        A_ = np.array([[10, -2, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]])
        b_ = np.array([[6], [25], [-11], [15]])

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = round((py.memory_info()[0] / 2. ** 30), 8)  # memory use in GB

        start = time.time()
        solution, _ = JM(A_, b_)
        end = time.time()
        speed = round(end - start, 6)  # operating time

        write_to_file(num=2, memory_usage_=memory_usage, speed_=speed, logic='FAILED')
        for pair in zip(solution, [1, 2, -1, 1]):  # [1, 2, -1, 1] is exact solution
            self.assertEqual(round(pair[0], 2), round(pair[1], 2))

    def test_3(self):
        A_ = np.array([[8, 4, 1], [2, 10, 3], [1, 4, 10]])
        b_ = np.array([[15], [2], [5]])

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = round((py.memory_info()[0] / 2. ** 30), 8)  # memory use in GB

        start = time.time()
        solution, _ = JM(A_, b_)
        end = time.time()
        speed = round(end - start, 6)  # operating time

        write_to_file(num=3, memory_usage_=memory_usage, speed_=speed, logic='PASSED')
        for pair in zip(solution, [629/317, -207/634, 137/317]):  # [629/317, -207/634, 137/317] is exact solution
            self.assertEqual(round(pair[0], 2), round(pair[1], 2))

    def test_4(self):
        A_ = np.array([[1, 4, 8, 16], [2, 2, 3, 3], [1, 4, 4, 4], [2, 2, 6, 6]])
        b_ = np.array([[15], [2], [5], [6]])

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = round((py.memory_info()[0] / 2. ** 30), 8)  # memory use in GB

        start = time.time()
        solution, _ = JM(A_, b_)
        end = time.time()
        speed = round(end - start, 6)  # operating time

        write_to_file(num=4, memory_usage_=memory_usage, speed_=speed)
        for pair in zip(solution, [-11 / 9, 2 / 9, 3 / 4, 7 / 12]):  # [-11/9, 2/9, 3/4, 7/12] is exact solution
            self.assertEqual(round(pair[0], 2), round(pair[1], 2))


if __name__ == '__main__':
    unittest.main()
