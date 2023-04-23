import pandas as pd

FilePath = "Params_20210731.V2.xlsx"
SheetName = "grid_rainfall"

def readfile(path, sheet):
    dataframe1 = pd.read_excel(path, sheet_name=sheet, index_col=False, header=None)
    input_array = dataframe1.to_numpy()

