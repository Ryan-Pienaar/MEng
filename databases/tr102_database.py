import pandas as pd

# --- GLOBAL VARIABLES ---

path = "~\OneDrive\Documents\VSCode\MEng\methods\Params_20210731.V2.xlsx"
sheetName = "tr102_database"

def readfile(path, sheet):
    dataframe1 = pd.read_excel(path, sheet_name=sheet, index_col=False, header=None)
    input_array = dataframe1.to_numpy()

    return input_array

if __name__ == "__main__":
    print(readfile(path, sheetName))