import rlma_saws_database as rlma_data
import tr102_database as tr102_data
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

# --- Averages ---
rlma_saws_mean_map_avg = 0
rlma_saws_thiessen_map_avg = 0
rlma_saws_mean_r_avg = 0
rlma_saws_thiessen_r_avg = 0
tr102_mean_map_avg = 0
tr102_thiessen_map_avg = 0
tr102_mean_r_avg = 0
tr102_thiessen_r_avg = 0


def arithmeticmean_rlma_saws(station_list, rlma_saws_database):
    arr = numpy.zeros((4,7))
    temp = numpy.zeros((199, 33))

    for i in range(len(station_list)):
        copy_index = 0
        curr_station_numb = station_list[i].stationnumb
        index = 0
        while (curr_station_numb != rlma_saws_database[index][0]):
            print(rlma_saws_database[index][0] + " -- " + curr_station_numb)
            index += 1
        
        
        temp[i][3] = station_list[i].area
        copy_index += 1
        temp[i][4] = rlma_saws_database[index][6]
        for j in range(8, 28):
            temp[i][copy_index] = rlma_saws_database[index][j]
            copy_index += 1
        for j in range(49, 57):
            temp[i][copy_index] = rlma_saws_database[index][j]
            copy_index += 1
        
    return temp
        



def thiessenpolygon_rlma_saws(station_list, rlma_saws_database):
    arr = numpy.zeros((4,7))
    temp = numpy.zeros((201, 33))

def arithmeticmean_tr102(station_list, tr102_database):
    arr = numpy.zeros((4,7))
    temp = numpy.zeros((201, 33))

def thiessenpolygon_tr102(station_list, tr102_database):
    arr = numpy.zeros((4,7))
    temp = numpy.zeros((201, 33))

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
    rdata = rlma_data.readfile()
    tr102_data.readfile()

    stations = readfile()
    ars = arithmeticmean_rlma_saws(stations, rdata)
    print(ars)

    

    