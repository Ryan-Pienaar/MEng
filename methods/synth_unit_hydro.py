import numpy as np
import math as math
import methods.grid_rainfall as gr
import pandas as pd

path = "Params_20210731.V2.xlsx"

# ----- GLOBAL VARIABLES -----
#TODO: Correct how certain variables are obtained
area = 6331
MAP = 518
veldtype1_nr = 4
veldtype2_nr = 7
veldtype3_nr = 5
veldtype1_perc = 97.29
veldtype2_perc = 2.71
veldtype3_perc = 0
LC = 113.05
KU = 0.384
L = 186.696
SCH = 0.00131
S = 0.04186
TL = 37.666
TC = 47.875
IC = 582856.728
QP = 64.557
return_period1 = 100
return_period2 = 200
returnp_ratio1 = 1.6
returnp_ratio2 = 1.8
single_rainfall_station = False
multiple_rainfall_station = True
inland_summer = True
coastal_winter = False
ARF = 0
incr_vars = [12, 14, 16, 18, 20]
adjust_peak_flow = [239, 397, 578, 812, 1236, 1713, 2074]
TSD = 1

dataframe1 = pd.read_excel(path, sheet_name="flood_runoff_f1", index_col=False, header=None)
input_arr_2 = dataframe1.to_numpy()

dataframe2 = pd.read_excel(path, sheet_name="flood_runoff_f2", index_col=False, header=None)
input_arr_4_5_6_7 = dataframe2.to_numpy()

dataframe3 = pd.read_excel(path, sheet_name="flood_runoff_f3", index_col=False, header=None)
input_arr_1_3_8_9 = dataframe3.to_numpy()

def max_value(input_arr, column):
    arr = np.zeros(len(input_arr))

    for i in range(len(input_arr)):
        arr[i] = input_arr[i][column]
    
    val = arr.max()
    return val

def lookup(arr, lookup_value, column):
    i = 0

    while True:
        if arr[i][0] == lookup_value:
            return arr[i][column]
        i += 1

def FloodRunoffFactorArays(main_arr):
    arr1 = np.zeros((4, 5))
    arr2 = np.zeros((4, 5))
    arr3 = np.zeros((4, 5))
    arr4 = np.zeros((4, 5))
    arr5 = np.zeros((4, 5))

    for i in range(5):
        
        if veldtype1_nr == 1 or veldtype1_nr == 3 or veldtype1_nr == 8 or veldtype1_nr == 9:
            arr1[0][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 1)
            arr2[0][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 2)
            arr3[0][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 3)
            arr4[0][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 4)
            arr4[0][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 5)
        elif veldtype1_nr == 4 or veldtype1_nr == 5 or veldtype1_nr == 6 or veldtype1_nr == 7:
            arr1[0][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 1)
            arr2[0][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 2)
            arr3[0][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 3)
            arr4[0][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 4)
            arr5[0][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 5)
        elif veldtype1_nr == 2:
            arr1[0][i] = lookup(input_arr_2, main_arr[4][i], 1)
            arr2[0][i] = lookup(input_arr_2, main_arr[4][i], 2)
            arr3[0][i] = lookup(input_arr_2, main_arr[4][i], 3)
            arr4[0][i] = lookup(input_arr_2, main_arr[4][i], 4)
            arr5[0][i] = lookup(input_arr_2, main_arr[4][i], 5)

        if veldtype2_nr == 1 or veldtype2_nr == 3 or veldtype2_nr == 8 or veldtype2_nr == 9:
            arr1[1][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 1)
            arr2[1][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 2)
            arr3[1][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 3)
            arr4[1][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 4)
            arr5[1][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 5)
        elif veldtype2_nr == 4 or veldtype2_nr == 5 or veldtype2_nr == 6 or veldtype2_nr == 7:
            arr1[1][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 1)
            arr2[1][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 2)
            arr3[1][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 3)
            arr4[1][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 4)
            arr5[1][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 5)
        elif veldtype2_nr == 2:
            arr1[1][i] = lookup(input_arr_2, main_arr[4][i], 1)
            arr2[1][i] = lookup(input_arr_2, main_arr[4][i], 2)
            arr3[1][i] = lookup(input_arr_2, main_arr[4][i], 3)
            arr4[1][i] = lookup(input_arr_2, main_arr[4][i], 4)
            arr5[1][i] = lookup(input_arr_2, main_arr[4][i], 5)

        if veldtype3_nr == 1 or veldtype3_nr == 3 or veldtype3_nr == 8 or veldtype3_nr == 9:
            arr1[2][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 1)
            arr2[2][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 2)
            arr3[2][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 3)
            arr4[2][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 4)
            arr5[2][i] = lookup(input_arr_1_3_8_9, main_arr[4][i], 5)
        elif veldtype3_nr == 4 or veldtype3_nr == 5 or veldtype3_nr == 6 or veldtype3_nr == 7:
            arr1[2][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 1)
            arr2[2][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 2)
            arr3[2][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 3)
            arr4[2][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 4)
            arr5[2][i] = lookup(input_arr_4_5_6_7, main_arr[4][i], 5)
        elif veldtype3_nr == 2:
            arr1[2][i] = lookup(input_arr_2, main_arr[4][i], 1)
            arr2[2][i] = lookup(input_arr_2, main_arr[4][i], 2)
            arr3[2][i] = lookup(input_arr_2, main_arr[4][i], 3)
            arr4[2][i] = lookup(input_arr_2, main_arr[4][i], 4)
            arr5[2][i] = lookup(input_arr_2, main_arr[4][i], 5)

        arr1[3][i] = (arr1[0][i] * (veldtype1_perc / 100)) + (arr1[1][i] * (veldtype2_perc / 100)) + (arr1[2][i] * (veldtype3_perc / 100))
        arr2[3][i] = (arr2[0][i] * (veldtype1_perc / 100)) + (arr2[1][i] * (veldtype2_perc / 100)) + (arr2[2][i] * (veldtype3_perc / 100))
        arr3[3][i] = (arr3[0][i] * (veldtype1_perc / 100)) + (arr3[1][i] * (veldtype2_perc / 100)) + (arr3[2][i] * (veldtype3_perc / 100))
        arr4[3][i] = (arr4[0][i] * (veldtype1_perc / 100)) + (arr4[1][i] * (veldtype2_perc / 100)) + (arr4[2][i] * (veldtype3_perc / 100))
        arr5[3][i] = (arr5[0][i] * (veldtype1_perc / 100)) + (arr5[1][i] * (veldtype2_perc / 100)) + (arr5[2][i] * (veldtype3_perc / 100))

        
        if area > 1000 and area <= 3000:
            main_arr[6][i] = arr1[3][i] - ((arr1[3][i] - arr2[3][i]) / 2000 * (area - 1000))
        elif area > 3000 and area <= 10000:
            main_arr[6][i] = arr2[3][i] - ((arr2[3][i] - arr3[3][i]) / 7000 * (area - 3000))
        elif area > 10000 and area <= 30000:
            main_arr[6][i] = arr3[3][i] - ((arr3[3][i] - arr4[3][i]) / 20000 * (area - 10000))
        elif area > 30000 and area <= 100000:
            main_arr[6][i] = arr4[3][i] - ((arr4[3][i] - arr5[3][i]) / 70000 * (area - 30000))


    return main_arr

def design_rainfall_info():
    rainfall_grid = gr.readfile()
    main_arr = np.zeros((8, 10))
    arr1 = np.zeros((8, 5))
    arr2 = np.zeros((8, 5))
    

    for i in range(5):
        if single_rainfall_station or multiple_rainfall_station:
            if incr_vars[i] == 0:
                arr1[0][i] = 0
                arr2[0][i] = 0
            elif inland_summer:
                arr1[0][i] = incr_vars[i] * (217.8/math.pow(1+4.164*incr_vars[i], 0.8832)) * returnp_ratio1 * ((18.79+0.17*MAP)/100)
                arr2[0][i] = incr_vars[i] * (217.8/math.pow(1+4.164*incr_vars[i], 0.8832)) * returnp_ratio2 * ((18.79+0.17*MAP)/100)
            arr1[1][i] = 0
            arr2[1][i] = 0
        else:
            if return_period1 == 2:
                arr1[1][i] = gr.lookup(incr_vars[i], 1, rainfall_grid)
            elif return_period1 == 5:
                arr1[1][i] = gr.lookup(incr_vars[i], 2, rainfall_grid)
            elif return_period1 == 10:
                arr1[1][i] = gr.lookup(incr_vars[i], 3, rainfall_grid)
            elif return_period1 == 20:
                arr1[1][i] = gr.lookup(incr_vars[i], 4, rainfall_grid)
            elif return_period1 == 50:
                arr1[1][i] = gr.lookup(incr_vars[i], 5, rainfall_grid)
            elif return_period1 == 100:
                arr1[1][i] = gr.lookup(incr_vars[i], 6, rainfall_grid)
            elif return_period1 == 200:
                arr1[1][i] = gr.lookup(incr_vars[i], 7, rainfall_grid)

            if return_period2 == 2:
                arr2[1][i] = gr.lookup(incr_vars[i], 1, rainfall_grid)
            elif return_period2 == 5:
                arr2[1][i] = gr.lookup(incr_vars[i], 2, rainfall_grid)
            elif return_period2 == 10:
                arr2[1][i] = gr.lookup(incr_vars[i], 3, rainfall_grid)
            elif return_period2 == 20:
                arr2[1][i] = gr.lookup(incr_vars[i], 4, rainfall_grid)
            elif return_period2 == 50:
                arr2[1][i] = gr.lookup(incr_vars[i], 5, rainfall_grid)
            elif return_period2 == 100:
                arr2[1][i] = gr.lookup(incr_vars[i], 6, rainfall_grid)
            elif return_period2 == 200:
                arr2[1][i] = gr.lookup(incr_vars[i], 7, rainfall_grid)
        
        if incr_vars[i] == 0:
            arr1[2][i] = 0
            arr2[2][i] = 0
        else:
            if arr1[1][i] == 0:
                arr1[2][i] = arr1[0][i] / incr_vars[i]
            else:
                arr1[2][i] = arr1[1][i] / incr_vars[i]

            if arr2[1][i] == 0:
                arr2[2][i] = arr2[0][i] / incr_vars[i]
            else:
                arr2[2][i] = arr2[1][i] / incr_vars[i]

        if area == 0:
            arr1[3][i] = 0
            arr2[3][i] = 0
            arr1[4][i] = 0
            arr2[4][i] = 0
        elif area <= 10 and incr_vars[i] > 1:
            arr1[3][i] = 100
            arr2[3][i] = 100
        else:
            arr1[3][i] = math.pow(90000 - 12800 * math.log(area) + 9830 * math.log(incr_vars[i] * 60), 0.4)
            arr2[3][i] = math.pow(90000 - 12800 * math.log(area) + 9830 * math.log(incr_vars[i] * 60), 0.4)

        if arr1[1][i] == 0:
            arr1[4][i] = round(arr1[3][i]/100 * arr1[0][i], 1)
        else:
            arr1[4][i] = round(ARF / 100 * arr1[1][i], 1)

        if arr2[1][i] == 0:
            arr2[4][i] = round(arr2[3][i]/100 * arr2[0][i], 1)
        else:
            arr2[4][i] = round(ARF / 100 * arr2[1][i], 1)

        if area <= 1000:
            arr1[5][i] = 0
            arr2[5][i] = 0

    arr1 = FloodRunoffFactorArays(arr1)
    arr2 = FloodRunoffFactorArays(arr2)

    for i in range(5):
        if incr_vars[i] == 0:
            arr1[7][i] = 0
            arr2[7][i] = 0
        else:
            if arr1[5][i] == 0:
                arr1[7][i] = arr1[6][i] / 100 * arr1[4][i]
            else:
                arr1[7][i] = arr1[5][i] / 100 * arr1[4][i]

            if arr2[5][i] == 0:
                arr2[7][i] = arr2[6][i] / 100 * arr2[4][i]
            else:
                arr2[7][i] = arr2[5][i] / 100 * arr2[4][i]



    #print(arr1) 
    #print(arr2) 

    return arr1, arr2


def peak_flow_adjust(s_curve_lag_arr, dsri_arr1, dsri_arr2):
    arr1 = np.zeros((3, 5))
    arr2 = np.zeros((3, 5))

    for i in range(5):
        if incr_vars[i] == 0:
            arr1[0][i] = 0
            arr2[0][i] = 0
            arr1[1][i] = 0
            arr2[1][i] = 0
        else:
            arr1[0][i] = max_value(s_curve_lag_arr, i+4) * QP
            arr2[0][i] = max_value(s_curve_lag_arr, i+4) * QP
            arr1[1][i] = arr1[0][i] * dsri_arr1[7][i]
            arr2[1][i] = arr2[0][i] * dsri_arr2[7][i]

        if max_value(s_curve_lag_arr, 2) < 1:
            arr1[2][i] = max_value(s_curve_lag_arr, 2)
            arr2[2][i] = max_value(s_curve_lag_arr, 2)
        else:
            arr1[2][i] = 1
            arr2[2][i] = 1

    #print(arr1)
    #print(arr2)

    return arr1, arr2


def s_curve_lagging(TSD):

    if TSD == 1:
        dataframe1 = pd.read_excel(path, sheet_name="suh_curve_lag_1", index_col=False, header=None)
        arr = dataframe1.to_numpy()
        return arr

    elif TSD == 0.5:
        dataframe2 = pd.read_excel(path, sheet_name="suh_curve_lag_2", index_col=False, header=None)
        arr = dataframe2.to_numpy()
        return arr
        
    elif TSD == 0.25:
        dataframe3 = pd.read_excel(path, sheet_name="suh_curve_lag_3", index_col=False, header=None)
        arr = dataframe3.to_numpy()
        return arr
    
    else:
        raise ValueError("Invalid TSD Value: Must be 1, 0.5 or 0.25")

if __name__ == "__main__":
    np.set_printoptions(suppress = True)
    dsri_arr1, dsri_arr2 = design_rainfall_info()
    s_curve_lagging = s_curve_lagging(TSD)
    pfa_arr1, pfa_arr2 = peak_flow_adjust(s_curve_lagging, dsri_arr1, dsri_arr2)
    print(pfa_arr1)



def excecute():
    print("METHOD NOT IMPLEMENTED")