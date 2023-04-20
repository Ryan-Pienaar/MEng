import pandas as pd
from databases.catchment import Information as catchment

# GLOBAL VARIABLES
FilePath = "Params_20210731.V2.xlsx"
SheetName = "python_read"

# LISTS
CatchmentList = []


# FUNCTIONS
def readfile(path, sheet):
    dataframe1 = pd.read_excel(path, sheet_name=sheet, index_col=False, header=None)
    input_array = dataframe1.to_numpy()
    objs = list()

    for i in range(411):
        temp_array = list()
        for j in range(102):
            temp_array.append(input_array[i][j])
        obj = catchment(temp_array)
        objs.append(obj)

    return objs


# MAIN FUNCTION
if __name__ == '__main__':
    CatchmentList = readfile(FilePath, SheetName)
    CatchmentList[0].test()
