import os
import csv
import unittest
import join


class TestCsv(unittest.TestCase):

    def setUp(self):
        self.test_file_left = 'test_file_left.csv'
        self.test_file_right = 'test_file_right.csv'
        self.test_file_inner = 'test_file_inner.csv'
        self.test_data_left = csv.reader(self.test_file_left)
        self.test_data_right = csv.reader(self.test_file_right)
        self.test_data_inner = csv.reader(self.test_file_inner)
        self.file1 = 'csv1.csv'
        self.file2 = 'csv2.csv'
        self.left_join_result = ''

    def left_join_test(self):
        left_join_object = join.join_with_pandas.csv_joiner(
            self.file1, self.file2, "CustomerID", "left")
        left_join_object.join()
        self.left_join_result = csv.reader("final.csv")
        for correct_line, tested_line in zip(self.test_data_left, self.left_join_result):
            self.assertEqual(correct_line, tested_line)

    def right_join_test(self):
        pass

    def inner_join_test(self):
        pass

    def main(self):
        self.left_join_test()
        self.right_join_test()
        self.inner_join_test()
    #self.assertEqual(self.test_data, self.left_join_result)

    # def setUp(self):
    #     with open(self.test_file, 'w', newline='') as csv_file:
    #         writer = csv.writer(csv_file, dialect='excel')
    #         writer.writerows(rows)

        # def tearDown(self):
        #     os.remove(test_file)

    # def test_read_line(self):
    #     with open(test_file, 'r') as csv_file:
    #         reader = csv.reader(csv_file, dialect='excel')
    #         self.assertEqual(next(reader), rows[0])
    #         self.assertEqual(next(reader), rows[1])


if __name__ == "__main__":
    unittest.main()
