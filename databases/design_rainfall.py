import rlma_saws_database as rlma
import tr102_database as tr102
import numpy as numpy
from stationinfo import Stations as si
import pandas as pd

# --- GLOBAL VARIABLES ---
path = "~\OneDrive\Documents\VSCode\MEng\methods\Params_20210731.V2.xlsx"
sheetName = "rainfall_stations"
userMAP = 0
gridMAP = 0
designrainfallgrid = numpy.zeros((23,8))

# --- ESTIMATION RESULTS BOOLEANS ---
rlma_saws_database = False
tr102_database = False
aritmetic_mean_method = False
thiessen_polygon_method = False

def arithmeticmean_rlma_saws():
    temp = 0

def thiessenpolygon_rlma_saws():
    temp = 0

def arithmeticmean_tr102():
    temp = 0

def thiessenpolygon_tr102():
    temp = 0

def readfile():
    dataframe1 = pd.read_excel(path, sheet_name=sheetName, index_col=False, header=None)
    input_array = dataframe1.to_numpy()
    print(input_array)
    objs = list()

    for i in range(200):
        temp_array = list()

        for j in range(2):
            temp_array.append(input_array[i, j])
        obj = si(temp_array)
        objs.append(obj)
    return objs


if __name__ == "__main__":
    rlma.readfile()
    tr102.readfile()

    stations = readfile()
    print(stations[0].stationnumb)

    

    