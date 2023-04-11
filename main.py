import pandas as pd
import databases.catchment as catchment

dataframe1 = pd.read_excel("Params_20210731.V2.xlsx", sheet_name="python_read", index_col=False)
inputarray = dataframe1.to_numpy()

CatchmentList = []

for i in range (0,410):
    CatchmentObj = catchment.Information
    CatchmentObj.Station = inputarray[i][0]
    CatchmentObj.PDRN = inputarray[i][1]
    CatchmentObj.SDRN = inputarray[i][2]
    CatchmentObj.TDRN = inputarray[i][3]
    CatchmentObj.QDRN = inputarray[i][4]
    CatchmentObj.CatchmentDescr = None
    CatchmentList.append(CatchmentObj)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(dataframe1)
    print(CatchmentList.pop().QDRN)


