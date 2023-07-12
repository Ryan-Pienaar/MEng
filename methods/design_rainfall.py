import methods.rlma_saws_database as rlma_data
import methods.tr102_database as tr102_data
import numpy as numpy
from methods.stationinfo import Stations as si
import pandas as pd

# --- GLOBAL VARIABLES ---
path = "/Users/ryanpienaar/VSCode/MEng/methods/Params_20210731.V2.xlsx"
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
    temp = numpy.zeros((199, 31))
    adjusted_index = 0
    missing_entries = 0
    

    for i in range(len(station_list)):
        not_skip = True
        copy_index = 0
        curr_station_numb = station_list[i].stationnumb
        index = 0

        if curr_station_numb != 0:
            while (curr_station_numb != rlma_saws_database[index][0]):
                index += 1
                if index > 3945:
                    missing_entries += 1
                    not_skip = False
                    break
            
            if not_skip:
                temp[adjusted_index][copy_index] = station_list[i].area
                copy_index += 1
                temp[adjusted_index][copy_index] = rlma_saws_database[index][6]
                copy_index += 1
                for j in range(8, 28):
                    temp[adjusted_index][copy_index] = rlma_saws_database[index][j]
                    copy_index += 1
                for j in range(49, 58):
                    temp[adjusted_index][copy_index] = rlma_saws_database[index][j]
                    copy_index += 1
                adjusted_index += 1

    rlma_saws_mean_map_avg = col_average(temp, 1)
    #print(rlma_saws_mean_map_avg)  
    rlma_saws_mean_r_avg = col_average(temp, 30)
    #print(rlma_saws_mean_r_avg)
    #print(missing_entries)

    for i in range(7):
        arr[0][i] = col_average(temp, i + 2)
        arr[1][i] = col_average(temp, i + 9)
        arr[2][i] = col_average(temp, i + 16)
        arr[3][i] = col_average(temp, i + 23)

    return arr

def thiessenpolygon_rlma_saws(station_list, rlma_saws_database):
    arr = numpy.zeros((4,7))
    temp = numpy.zeros((199, 61))
    adjusted_index = 0
    missing_entries = 0
    

    for i in range(len(station_list)):
        not_skip = True
        copy_index = 0
        curr_station_numb = station_list[i].stationnumb
        index = 0

        if curr_station_numb != 0:
            while (curr_station_numb != rlma_saws_database[index][0]):
                index += 1
                if index > 3945:
                    missing_entries += 1
                    not_skip = False
                    break
            
            if not_skip:
                temp[adjusted_index][copy_index] = station_list[i].area
                copy_index += 1
                temp[adjusted_index][copy_index] = rlma_saws_database[index][6]
                copy_index += 1
                temp[adjusted_index][copy_index] = temp[adjusted_index][copy_index - 1] * temp[adjusted_index][0]
                copy_index += 1
                for j in range(8, 28):
                    temp[adjusted_index][copy_index] = rlma_saws_database[index][j]
                    copy_index += 1
                    temp[adjusted_index][copy_index] = temp[adjusted_index][copy_index - 1] * temp[adjusted_index][0]
                    copy_index += 1
                    
                for j in range(49, 58):
                    temp[adjusted_index][copy_index] = rlma_saws_database[index][j]
                    copy_index += 1
                    temp[adjusted_index][copy_index] = temp[adjusted_index][copy_index - 1] * temp[adjusted_index][0]
                    copy_index += 1
                    
                    
                adjusted_index += 1

    rlma_saws_thiessen_map_avg = tcol_average(temp, 1)
    #print(rlma_saws_mean_map_avg)  
    rlma_saws_thiessen_r_avg = tcol_average(temp, 59)
    #print(rlma_saws_mean_r_avg)
    #print(missing_entries)
    incr = 0
    for i in range(7):
        arr[0][i] = tcol_average(temp, i + 3 + incr)
        arr[1][i] = tcol_average(temp, i + 18 + incr)
        arr[2][i] = tcol_average(temp, i + 29 + incr)
        arr[3][i] = tcol_average(temp, i + 43 + incr)
        incr += 1

    return arr

def arithmeticmean_tr102(station_list, tr102_database):
    arr = numpy.zeros((4,7))
    temp = numpy.zeros((199, 31))
    adjusted_index = 0
    missing_entries = 0
    

    for i in range(len(station_list)):
        not_skip = True
        copy_index = 0
        curr_station_numb = station_list[i].stationnumb
        index = 0

        if curr_station_numb != 0:
            while (curr_station_numb != tr102_database[index][0]):
                index += 1
                if index > 1945:
                    missing_entries += 1
                    not_skip = False
                    break
            
            if not_skip:
                temp[adjusted_index][copy_index] = station_list[i].area
                copy_index += 1
                temp[adjusted_index][copy_index] = tr102_database[index][6]
                copy_index += 1
                for j in range(8, 28):
                    temp[adjusted_index][copy_index] = tr102_database[index][j]
                    copy_index += 1
                for j in range(28, 37):
                    temp[adjusted_index][copy_index] = tr102_database[index][j]
                    copy_index += 1
                adjusted_index += 1

    tr102_mean_map_avg = col_average(temp, 1)
    tr102_mean_r_avg = col_average(temp, 30)

    for i in range(7):
        arr[0][i] = col_average(temp, i + 2)
        arr[1][i] = col_average(temp, i + 9)
        arr[2][i] = col_average(temp, i + 16)
        arr[3][i] = col_average(temp, i + 23)

    return arr

def thiessenpolygon_tr102(station_list, tr102_database):
    arr = numpy.zeros((4,7))
    temp = numpy.zeros((199, 61))
    adjusted_index = 0
    missing_entries = 0
    

    for i in range(len(station_list)):
        not_skip = True
        copy_index = 0
        curr_station_numb = station_list[i].stationnumb
        index = 0

        if curr_station_numb != 0:
            while (curr_station_numb != tr102_database[index][0]):
                index += 1
                if index > 1945:
                    missing_entries += 1
                    not_skip = False
                    break
            
            if not_skip:
                temp[adjusted_index][copy_index] = station_list[i].area
                copy_index += 1
                temp[adjusted_index][copy_index] = tr102_database[index][6]
                copy_index += 1
                temp[adjusted_index][copy_index] = temp[adjusted_index][copy_index - 1] * temp[adjusted_index][0]
                copy_index += 1
                for j in range(8, 28):
                    temp[adjusted_index][copy_index] = tr102_database[index][j]
                    copy_index += 1
                    temp[adjusted_index][copy_index] = temp[adjusted_index][copy_index - 1] * temp[adjusted_index][0]
                    copy_index += 1
                    
                for j in range(28, 37):
                    temp[adjusted_index][copy_index] = tr102_database[index][j]
                    copy_index += 1
                    temp[adjusted_index][copy_index] = temp[adjusted_index][copy_index - 1] * temp[adjusted_index][0]
                    copy_index += 1
                    
                    
                adjusted_index += 1

    tr102_thiessen_map_avg = tcol_average(temp, 1)
    #print(rlma_saws_mean_map_avg)  
    tr102_thiessen_r_avg = tcol_average(temp, 59)
    #print(rlma_saws_mean_r_avg)
    #print("Missing Entries: " + str(missing_entries))
    incr = 0
    for i in range(7):
        arr[0][i] = tcol_average(temp, i + 3 + incr)
        arr[1][i] = tcol_average(temp, i + 17 + incr)
        arr[2][i] = tcol_average(temp, i + 31 + incr)
        arr[3][i] = tcol_average(temp, i + 45 + incr)
        incr += 1

    return arr

def readfile():
    dataframe1 = pd.read_excel(path, sheet_name=sheetName, index_col=False, header=None)
    input_array = dataframe1.to_numpy()
    #print(input_array)
    objs = list()

    for i in range(200):
        temp_array = list()

        for j in range(2):
            temp_array.append(input_array[i, j])
        obj = si(temp_array)
        objs.append(obj)
    return objs

def col_average(in_array, col_index):
    sum = 0
    dfact = 0
    for i in range(len(in_array)):
        if in_array[i][col_index] != 0:
            sum += in_array[i][col_index]
            dfact += 1
    
    average = sum / dfact

    return average

def tcol_average(in_array, col_index):
    area_sum = 0
    sum = 0
    
    
    for i in range(len(in_array)):
        if in_array[i][col_index + 1] != 0:
            area_sum += in_array[i][0]
            sum += in_array[i][col_index + 1]
    
    average = sum / area_sum

    return average

def excecute(method_nr):
    rdata = rlma_data.readfile()
    tdata = tr102_data.readfile()
    stations = readfile()

    if method_nr == 1:
        return arithmeticmean_rlma_saws(stations, rdata)
    elif method_nr == 2:
        return thiessenpolygon_rlma_saws(stations, rdata)
    elif method_nr == 3:
        return arithmeticmean_tr102(stations, tdata)
    elif method_nr == 4:
        return thiessenpolygon_tr102(stations, tdata)

    #print("RLMA/SAWS Arithmetic Mean MAP Average: " + str(rlma_saws_mean_map_avg))
    #print("RLMA/SAWS Arithmetic Mean R Average: " + str(rlma_saws_mean_r_avg))
    #print("RLMA/SAWS Thiessen Polygon Mean MAP Average: " + str(rlma_saws_thiessen_map_avg))
    #print("RLMA/SAWS Thiessen Polygon R Average: " + str(rlma_saws_thiessen_r_avg))
    #print("TR102 Arithmetic Mean MAP Average: " + str(tr102_mean_map_avg))
    #print("TR102 Arithmetic Mean R Average: " + str(tr102_thiessen_map_avg))
    #print("TR102 Thiessen Polygon MAP Average: " + str(tr102_mean_r_avg))
    #print("TR102 Thiessen Polygon R Average: " + str(tr102_thiessen_r_avg))


    
if __name__ == "__main__":
    excecute()
    