import pandas as pd
from databases.catchment import Information as catchment
from tkinter import *
from os.path import exists
import methods.rational as rational
import methods.alt_rational as alt_rational
import methods.probabilistic_ams as probabilistic_ams
import methods.probabilistic_pds as probabilistic_pds
import methods.scs as scs
import methods.sdf as sdf
import methods.synth_unit_hydro as suh
import methods.empirical as empirical
import methods.lag_routed_hydrograph as lrh

# GLOBAL VARIABLES
#FilePath = "Params_20210731.V2.xlsx"
#SheetName = "python_read"

# LISTS
CatchmentList = []

# C:\Users\ryanp\OneDrive\Documents\VSCode\MEng\methods\230703-Catchment Information Data Sheet.xlsx
# GENERAL CATCHMENT INFORMATION
# FUNCTIONS
def readfile(path, sheet):
    dataframe1 = pd.read_excel(path, sheet_name=sheet, index_col=False, header=None)
    
    #for i in range(3):
    #    dataframe1.drop(index=dataframe1.index[0], axis=0, inplace=True)

    input_array = dataframe1.to_numpy()
    objs = list()

    for i in range(411):
        temp_array = list()
        for j in range(152):
            temp_array.append(input_array[i][j])
        obj = catchment(temp_array)
        objs.append(obj)

    return objs

def show_methods():
    print(center_m_title)
    print("List of methods:")
    print("(1) Rational Method")
    print("(2) Alternative Rational Method -- NOT IMPLEMENTED --")
    print("(3) SCS Method -- NOT IMPLEMENTED --")
    print("(4) SDF Method -- NOT IMPLEMENTED --")
    print("(5) Empirical Methods -- NOT IMPLEMENTED --")
    print("(6) Synthetic Unit Hydrograph Method -- NOT IMPLEMENTED --")
    print("(7) Lag-Routed Hydrograph Method -- NOT IMPLEMENTED --")
    print("(8) Probabilisti Methods (AMS) -- NOT IMPLEMENTED --")
    print("(9) Probabilisti Methods (PDS) -- NOT IMPLEMENTED --")


# MAIN FUNCTION
if __name__ == '__main__':
    
    title = "DFET Python (Version 0.1)"
    c_title = title.center(204, "-")
    print(c_title)

    #FilePath = input("Please enter data file location: ")
    FilePath = "Params_20210731.V2.xlsx"

    #while not exists(FilePath):
     #   FilePath = input("File not found. Please enter correct file name or file path: ")
    
    xlsx_file = pd.ExcelFile(FilePath)

    print("Current sheets in xlsx file: ", xlsx_file.sheet_names)

    SheetName = "python_read"

    while SheetName not in xlsx_file.sheet_names:
        SheetName = input("Sheet does not exist. Please enter valid sheet name: ")

    CatchmentList = readfile(FilePath, SheetName)

    print("DATA READ SUCCESSFUL")

    methods_title = "METHODS"
    center_m_title = methods_title.center(204, "-")
    
    show_methods()
    
    method = int(input("Please choose the number of which method is to be used: "))

    while method <= 0 or method >= 10:
        method = input("ERR: INVALID METHOD NUMBER. Please choose a valid method number: ")
    
    if method == 1:
        rational.excecute(CatchmentList)

    elif method == 2:
        alt_rational.excecute()

    elif method == 3:
        scs.execute()
    
    elif method == 4:
        sdf.excecute()
    
    elif method == 5:
        empirical.excecute()
    
    elif method == 6:
        suh.excecute()
    
    elif method == 7:
        lrh.excecute(CatchmentList)
    
    elif method == 8:
        probabilistic_ams.excecute()
    
    elif method == 9:
        probabilistic_pds.excecute()