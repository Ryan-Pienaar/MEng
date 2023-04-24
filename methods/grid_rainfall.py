import pandas as pd

FilePath = "Params_20210731.V2.xlsx"
SheetName = "grid_rainfall"

def readfile():
    dataframe1 = pd.read_excel(FilePath, sheet_name=SheetName, index_col=False, header=None)
    rainfall = dataframe1.to_numpy()

    return rainfall



def lookup(lookup_value, time_period, rainfall_grid):
    i = 0

    while True:
        if rainfall_grid[i][0] == lookup_value:
            return rainfall_grid[i][time_period]
        i += 1
    
    
            
    
    