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
        self.df1 = pd.read_csv(self.file1, index_col=False)
        self.df2 = pd.read_csv(self.file2, index_col=False)
        self.type = type

    def join(self):
        dataTypeObj1 = self.df1.dtypes
        dataTypeObj2 = self.df2.dtypes
        if dataTypeObj1[self.col_name] != dataTypeObj2[self.col_name]:
            self.df2[self.col_name] = self.df2[self.col_name].astype(
                dataTypeObj1[self.col_name])
        if self.type == "inner":
            self.inner_join()
        elif self.type == "left":
            self.left_join()
        elif self.type == "right":
            self.right_join()

    def left_join(self):
        # assume that left is the first argument
        df3 = self.df1.merge(self.df2, on=[self.col_name], how='left')
        print(df3)
        df3.to_csv("final.csv", index=False)

    def right_join(self):
        df4 = pd.merge(self.df1, self.df2, on=[self.col_name], how='right')
        print(df4)
        df4.to_csv("final.csv", index=False)

    def inner_join(self):
        df5 = pd.merge(self.df1, self.df2, on=[self.col_name], how='inner')
        print(df5)
        df5.to_csv("final.csv", index=False)
