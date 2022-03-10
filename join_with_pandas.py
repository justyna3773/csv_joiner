import csv
import pandas as pd


class csv_joiner:
    def __init__(self, file1, file2, col_name, type='inner'):
        self.file1 = file1
        # maybe I should assign file contents there
        self.file2 = file2
        self.rows1 = []
        self.headers1 = []
        self.rows2 = []
        self.headers2 = []
        self.col_name = col_name
        self.df1 = pd.read_csv(self.file1)
        self.df2 = pd.read_csv(self.file2)
        self.type = type

    def left_join(self):
        # assume that left is the first argument
        df3 = self.df1.merge(self.df2, on=[self.col_name], how='left')
        df3.to_csv("final.csv", index=False)

    def right_join(self):
        df4 = self.df1.merge(self.df2, on=[self.col_name], how='right')
        df4.to_csv("final.csv", index=False)

    def inner_join(self):
        df5 = self.df1.merge(self.df2, on=[self.col_name], how='inner')
        df5.to_csv("final.csv", index=False)
