import lrh_rainfall_distr as lrh_database
import numpy as np
import pandas as pd
import grid_rainfall as gr
import rational as rational
import math as math

# ------ GLOBAL VARIABLES ------
path = "Params_20210731.V2.xlsx"

SingleRainfallStation = False
MultipleRainfallStations = True
InlandSummer = True
OutlandWinter = False

Area = 6331
MAP = 518

veldtype1_nr = 4
veldtype2_nr = 7
veldtype3_nr = 6

veldtype1_perc = 97.29
veldtype2_perc = 2.71
veldtype3_perc = 0

TC = 47.875
TSD = 48
delta_T = 2.4
L = 186.696
SCH = 0.00131
LC = 113.0115
musk_routing_factor_k1 = 0
musk_routing_factor_k2 = 0
musk_C0 = 0
musk_C1 = 0
musk_C2 = 0


veldtype_based = False
tc_based = True

ARF = 0

dataframe1 = pd.read_excel(path, sheet_name="flood_runoff_f1", index_col=False, header=None)
input_arr_2 = dataframe1.to_numpy()

dataframe2 = pd.read_excel(path, sheet_name="flood_runoff_f2", index_col=False, header=None)
input_arr_4_5_6_7 = dataframe2.to_numpy()

dataframe3 = pd.read_excel(path, sheet_name="flood_runoff_f3", index_col=False, header=None)
input_arr_1_3_8_9 = dataframe3.to_numpy()

def lookup(arr, lookup_value, column):
    i = 0

    while True:
        if arr[i][0] == lookup_value:
            return arr[i][column]
        i += 1


def FloodRunoffFactorArays(main_arr):
    arr1 = np.zeros((4, 7))
    arr2 = np.zeros((4, 7))
    arr3 = np.zeros((4, 7))
    arr4 = np.zeros((4, 7))
    arr5 = np.zeros((4, 7))

    for i in range(7):
        
        if veldtype1_nr == 1 or veldtype1_nr == 3 or veldtype1_nr == 8 or veldtype1_nr == 9:
            arr1[0][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 1)
            arr2[0][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 2)
            arr3[0][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 3)
            arr4[0][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 4)
            arr4[0][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 5)
        elif veldtype1_nr == 4 or veldtype1_nr == 5 or veldtype1_nr == 6 or veldtype1_nr == 7:
            arr1[0][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 1)
            arr2[0][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 2)
            arr3[0][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 3)
            arr4[0][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 4)
            arr4[0][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 5)
        elif veldtype1_nr == 2:
            arr1[0][i] = lookup(input_arr_2, main_arr[3][i], 1)
            arr2[0][i] = lookup(input_arr_2, main_arr[3][i], 2)
            arr3[0][i] = lookup(input_arr_2, main_arr[3][i], 3)
            arr4[0][i] = lookup(input_arr_2, main_arr[3][i], 4)
            arr4[2][i] = lookup(input_arr_2, main_arr[3][i], 5)

        if veldtype2_nr == 1 or veldtype2_nr == 3 or veldtype2_nr == 8 or veldtype2_nr == 9:
            arr1[1][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 1)
            arr2[1][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 2)
            arr3[1][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 3)
            arr4[1][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 4)
            arr4[0][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 5)
        elif veldtype2_nr == 4 or veldtype2_nr == 5 or veldtype2_nr == 6 or veldtype2_nr == 7:
            arr1[1][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 1)
            arr2[1][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 2)
            arr3[1][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 3)
            arr4[1][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 4)
            arr4[0][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 5)
        elif veldtype2_nr == 2:
            arr1[1][i] = lookup(input_arr_2, main_arr[3][i], 1)
            arr2[1][i] = lookup(input_arr_2, main_arr[3][i], 2)
            arr3[1][i] = lookup(input_arr_2, main_arr[3][i], 3)
            arr4[1][i] = lookup(input_arr_2, main_arr[3][i], 4)
            arr4[2][i] = lookup(input_arr_2, main_arr[3][i], 5)

        if veldtype3_nr == 1 or veldtype3_nr == 3 or veldtype3_nr == 8 or veldtype3_nr == 9:
            arr1[2][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 1)
            arr2[2][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 2)
            arr3[2][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 3)
            arr4[2][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 4)
            arr4[0][i] = lookup(input_arr_1_3_8_9, main_arr[3][i], 5)
        elif veldtype3_nr == 4 or veldtype3_nr == 5 or veldtype3_nr == 6 or veldtype3_nr == 7:
            arr1[2][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 1)
            arr2[2][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 2)
            arr3[2][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 3)
            arr4[2][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 4)
            arr4[0][i] = lookup(input_arr_4_5_6_7, main_arr[3][i], 5)
        elif veldtype3_nr == 2:
            arr1[2][i] = lookup(input_arr_2, main_arr[3][i], 1)
            arr2[2][i] = lookup(input_arr_2, main_arr[3][i], 2)
            arr3[2][i] = lookup(input_arr_2, main_arr[3][i], 3)
            arr4[2][i] = lookup(input_arr_2, main_arr[3][i], 4)
            arr4[2][i] = lookup(input_arr_2, main_arr[3][i], 5)

        arr1[3][i] = (arr1[0][i] * (veldtype1_perc / 100)) + (arr1[1][i] * (veldtype2_perc / 100)) + (arr1[2][i] * (veldtype3_perc / 100))
        arr2[3][i] = (arr2[0][i] * (veldtype1_perc / 100)) + (arr2[1][i] * (veldtype2_perc / 100)) + (arr2[2][i] * (veldtype3_perc / 100))
        arr3[3][i] = (arr3[0][i] * (veldtype1_perc / 100)) + (arr3[1][i] * (veldtype2_perc / 100)) + (arr3[2][i] * (veldtype3_perc / 100))
        arr4[3][i] = (arr4[0][i] * (veldtype1_perc / 100)) + (arr4[1][i] * (veldtype2_perc / 100)) + (arr4[2][i] * (veldtype3_perc / 100))
        arr5[3][i] = (arr5[0][i] * (veldtype1_perc / 100)) + (arr5[1][i] * (veldtype2_perc / 100)) + (arr5[2][i] * (veldtype3_perc / 100))

        
        if Area > 1000 and Area <= 3000:
            main_arr[5][i] = arr1[3][i] - ((arr1[3][i] - arr2[3][i]) / 2000 * (Area - 1000))
        elif Area > 3000 and Area <= 10000:
            main_arr[5][i] = arr2[3][i] - ((arr2[3][i] - arr3[3][i]) / 7000 * (Area - 3000))
        elif Area > 10000 and Area <= 30000:
            main_arr[5][i] = arr3[3][i] - ((arr3[3][i] - arr4[3][i]) / 20000 * (Area - 10000))
        elif Area > 30000 and Area <= 100000:
            main_arr[5][i] = arr4[3][i] - ((arr4[3][i] - arr5[3][i]) / 70000 * (Area - 30000))

        if main_arr[3][i] == 0:
            main_arr[6][i] = 0
        elif main_arr[4][i] == 0:
            main_arr[6][i] = main_arr[5][i] / 100 * main_arr[3][i]
        else:
            main_arr[6][i] = main_arr[4][i] / 100 * main_arr[3][i]


    #print(arr1)
    #print(arr2)
    #print(arr3)
    #print(arr4)
    return main_arr

def DesignRainfallInformation():
    arr = np.zeros((7,7))
    var = [0.47, 0.64, 0.81, 1, 1.3, 1.6, 1.8]
    QT = 0
    rounded_tc = round(TC * 8) / 8
    rainfall_grid = gr.readfile()

    for i in range(7):
        if SingleRainfallStation or MultipleRainfallStations:
            if TC == 0:
                arr[0][i] = 0
            elif InlandSummer:
                arr[0][i] = TC * (217.8/math.pow((1 + 4.164 * TC), 0.8832)) * var[i] * ((18.79 + 0.17*MAP)/100)
            else:
                arr[0][i] = TC * (122.8/math.pow((1 + 4.779 * TC), 0.7372)) * var[i] * ((18.79 + 0.17*MAP)/100)
        else:
            arr[0][i] = 0
        
        if SingleRainfallStation or MultipleRainfallStations:
            arr[1][i] = 0
        else:
            arr[1][i] = gr.lookup(47.875, i+1, rainfall_grid)
        
        if Area == 0:
            arr[2][i] = 0
        elif Area <= 10 and TC > 1:
            arr[2][i] = 100
        else:
            arr[2][i] = math.pow((90000 - 12800 * math.log(Area) + 9830 * math.log(TC * 60)), 0.4)

        if Area == 0:
            arr[3][i] = 0
        elif arr[1][i] == 0:
            arr[3][i] = round(arr[2][i] / 100 * arr[0][i], 1)
        else:
            arr[3][i] = round(ARF / 100 * arr[1][i], 1)

    return arr

def rainfall_distr_over_time():
    arr = np.zeros((21, 2))

def muskingum_routing():
    arr = np.zeros((21, 7))

def excecute():
    print("METHOD NOT IMPLEMENTED")

if __name__ == "__main__":
    #print(DesignRainfallInformation())
    print(FloodRunoffFactorArays(DesignRainfallInformation()))
