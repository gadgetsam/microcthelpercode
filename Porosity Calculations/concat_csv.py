import pandas as pd
import glob

# use your path
def concat_csv(path):
    all_files = glob.glob(path + "/*.csv")

    li = pd.read_csv(all_files[0], index_col=None, header=None)
    all_files.pop(0)

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=None)
        li = li.append(df, sort=False)
    return li
