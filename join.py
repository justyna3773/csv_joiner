from multiprocessing.sharedctypes import Value
import join_with_pandas
import sys

if __name__ == "__main__":
    try:
        join_class = join_with_pandas.csv_joiner(sys.argv[1], sys.argv[2],sys.argv[3], type=sys.argv[4] )
    except ValueError:
        raise("Value Error")
    if len(sys.argv) < 4:
        raise ValueError("Too few arguments\n")
        sys.exit()
