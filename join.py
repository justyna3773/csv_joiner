
import join_with_pandas
import sys

if __name__ == "__main__":
    try:
        join_class = join_with_pandas.csv_joiner(
            sys.argv[1], sys.argv[2], sys.argv[3], type=sys.argv[4])
        join_class.join()
    except ValueError:
        raise("Value Error")
    except FileNotFoundError:
        raise("File not found\n")
    except IndexError:
        raise("Wrong number of arguments")
    if len(sys.argv) < 4:
        raise ValueError("Too few arguments\n")
    if sys.argv[4] not in ['left', 'right', 'inner']:
        raise ValueError("Choose either left, right or inner join\n")
