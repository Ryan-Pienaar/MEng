import pandas as pd
import databases.catchment as catchment

# GLOBAL VARIABLES
FilePath = "Params_20210731.V2.xlsx"
SheetName = "python_read"

# LISTS
CatchmentList = []

# FUNCTIONS
def readFile(path, sheet):
    dataframe1 = pd.read_excel(path, sheet_name=sheet, index_col=False)
    inputarray = dataframe1.to_numpy()
    List = []
    for i in range (0,410): #TODO: Finish setting variables
        CatchmentObj = catchment.Information
        CatchmentObj.Station = inputarray[i][0]
        CatchmentObj.PDRN = inputarray[i][1]
        CatchmentObj.SDRN = inputarray[i][2]
        CatchmentObj.TDRN = inputarray[i][3]
        CatchmentObj.QDRN = inputarray[i][4]
        CatchmentObj.CatchmentDescr = None #None for now. Will update when catxhment descriptions are added.
        CatchmentObj.Area = inputarray[i][5]
        List.append(CatchmentObj)

    return List

# MAIN FUNCTION
if __name__ == '__main__':
    CatchmentList = readFile(FilePath, SheetName)
    print(CatchmentList.pop().Area)


