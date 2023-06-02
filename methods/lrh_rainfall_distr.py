import pandas as pd

path = "~\OneDrive\Documents\VSCode\MEng\methods\Params_20210731.V2.xlsx"
sheetName = "lrh_rainfall_distr"

def readfile():
    dataframe1 = pd.read_excel(path, sheet_name=sheetName, index_col=False, header=None)
    input_array = dataframe1.to_numpy()

    return input_array

if __name__ == "__main__":
    print(readfile())