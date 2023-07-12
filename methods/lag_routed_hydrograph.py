import methods.lrh_rainfall_distr as lrh_database
import numpy as np
import pandas as pd
import methods.grid_rainfall as gr
import methods.rational as rational
import math as math

np.set_printoptions(suppress=True)

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
musk_routing_factor_k1 = 0.6 * TC
musk_routing_factor_k2 = 0

musk_C0 = 0.041
musk_C1 = 0.04
musk_C2 = 0.920

musk_temp1= 0
musk_temp2 = 0
musk_temp3 = 0

veldtype_based = False
tc_based = True

if veldtype1_nr == 1:
    musk_temp1 = 1.83 * math.pow(Area, 0.318)
elif veldtype1_nr == 2:
    musk_temp1 = 1.3 * math.pow(Area, 0.318)
elif veldtype1_nr == 3:
    musk_temp1 = 1.1 * math.pow(Area, 0.318)
elif veldtype1_nr == 4:
    musk_temp1 = 0.97 * math.pow(Area, 0.318)
elif veldtype1_nr == 5:
    musk_temp1 = 0.79 * math.pow(Area, 0.318)
elif veldtype1_nr == 6:
    musk_temp1 = 0.86 * math.pow(Area, 0.318)
elif veldtype1_nr == 7:
    musk_temp1 = 0.48 * math.pow(Area, 0.318)
elif veldtype1_nr == 8:
    musk_temp1 = 0.45 * math.pow(Area, 0.318)
elif veldtype1_nr == 9:
    musk_temp1 = 0.55 * math.pow(Area, 0.318)

if veldtype2_nr == 1:
    musk_temp2 = 1.83 * math.pow(Area, 0.318)
elif veldtype2_nr == 2:
    musk_temp2 = 1.3 * math.pow(Area, 0.318)
elif veldtype2_nr == 3:
    musk_temp2 = 1.1 * math.pow(Area, 0.318)
elif veldtype2_nr == 4:
    musk_temp2 = 0.97 * math.pow(Area, 0.318)
elif veldtype2_nr == 5:
    musk_temp2 = 0.79 * math.pow(Area, 0.318)
elif veldtype2_nr == 6:
    musk_temp2 = 0.86 * math.pow(Area, 0.318)
elif veldtype2_nr == 7:
    musk_temp2 = 0.48 * math.pow(Area, 0.318)
elif veldtype2_nr == 8:
    musk_temp2 = 0.45 * math.pow(Area, 0.318)
elif veldtype2_nr == 9:
    musk_temp2 = 0.55 * math.pow(Area, 0.318)

if veldtype3_nr == 1:
    musk_temp3 = 1.83 * math.pow(Area, 0.318)
elif veldtype3_nr == 2:
    musk_temp3 = 1.3 * math.pow(Area, 0.318)
elif veldtype3_nr == 3:
    musk_temp3 = 1.1 * math.pow(Area, 0.318)
elif veldtype3_nr == 4:
    musk_temp3 = 0.97 * math.pow(Area, 0.318)
elif veldtype3_nr == 5:
    musk_temp3 = 0.79 * math.pow(Area, 0.318)
elif veldtype3_nr == 6:
    musk_temp3 = 0.86 * math.pow(Area, 0.318)
elif veldtype3_nr == 7:
    musk_temp3 = 0.48 * math.pow(Area, 0.318)
elif veldtype3_nr == 8:
    musk_temp3 = 0.45 * math.pow(Area, 0.318)
elif veldtype3_nr == 9:
    musk_temp3 = 0.55 * math.pow(Area, 0.318)

musk_routing_factor_k2 = (musk_temp1 * (veldtype1_perc/100)) + (musk_temp2 * (veldtype2_perc/100)) + (musk_temp3 * (veldtype3_perc/100))   
print(musk_routing_factor_k2)

if tc_based:
    musk_C2 = math.exp((-1 * delta_T)/musk_routing_factor_k1)
    musk_C1 = musk_routing_factor_k1/delta_T*(1-musk_C2)-musk_C2
    musk_C0 = (-1*musk_routing_factor_k1)/delta_T*(1-musk_C2)+1
elif veldtype_based:
    musk_C2 = math.exp((-1 * delta_T)/musk_routing_factor_k2)
    musk_C1 = (-1*musk_routing_factor_k2)/delta_T*(1-musk_C2)+1

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
    rain_distr_arr = lrh_database.readfile()

    for i in range(21):
        arr[i][0] = i * 5
        if arr[i][0] == 0:
            arr[i][1] = 0
        else:
            arr[i][1] = round(lookup(rain_distr_arr, TSD, i + 1), 4)
    
    return arr

def muskingum_routing(rdot_arr, dri_arr):
    arr = np.zeros((21, 7))
    temp1_arr = np.zeros((21, 6))
    temp2_arr = np.zeros((21, 6))
    temp3_arr = np.zeros((21, 6))
    temp4_arr = np.zeros((21, 6))
    temp5_arr = np.zeros((21, 6))
    temp6_arr = np.zeros((21, 6))
    temp7_arr = np.zeros((21, 6))
    
    temp_arr = np.zeros(21)
    peakflow_arr = np.zeros(7)

    for i in range(1, 21):
        temp1_arr[i][0] = dri_arr[6][0] * (rdot_arr[i][1]/100)
        temp1_arr[i][1] = temp1_arr[i][0] - temp1_arr[i - 1][0]
        temp1_arr[i][2] = TSD * rdot_arr[i][0] / 100
        temp1_arr[i][3] = temp1_arr[i][1] / delta_T
        temp1_arr[i][4] = 0.278 * temp1_arr[i][3] * Area
        temp1_arr[i][5] = musk_C0 * temp1_arr[i][4] + musk_C1 * temp1_arr[i - 1][4] + musk_C2 * temp1_arr[i - 1][5]

        temp2_arr[i][0] = dri_arr[6][1] * (rdot_arr[i][1]/100)
        temp2_arr[i][1] = temp2_arr[i][0] - temp2_arr[i - 1][0]
        temp2_arr[i][2] = TSD * rdot_arr[i][0] / 100
        temp2_arr[i][3] = temp2_arr[i][1] / delta_T
        temp2_arr[i][4] = 0.278 * temp2_arr[i][3] * Area
        temp2_arr[i][5] = musk_C0 * temp2_arr[i][4] + musk_C1 * temp2_arr[i - 1][4] + musk_C2 * temp2_arr[i - 1][5]

        temp3_arr[i][0] = dri_arr[6][2] * (rdot_arr[i][1]/100)
        temp3_arr[i][1] = temp3_arr[i][0] - temp3_arr[i - 1][0]
        temp3_arr[i][2] = TSD * rdot_arr[i][0] / 100
        temp3_arr[i][3] = temp3_arr[i][1] / delta_T
        temp3_arr[i][4] = 0.278 * temp3_arr[i][3] * Area
        temp3_arr[i][5] = musk_C0 * temp3_arr[i][4] + musk_C1 * temp3_arr[i - 1][4] + musk_C2 * temp3_arr[i - 1][5]

        temp4_arr[i][0] = dri_arr[6][3] * (rdot_arr[i][1]/100)
        temp4_arr[i][1] = temp4_arr[i][0] - temp4_arr[i - 1][0]
        temp4_arr[i][2] = TSD * rdot_arr[i][0] / 100
        temp4_arr[i][3] = temp4_arr[i][1] / delta_T
        temp4_arr[i][4] = 0.278 * temp4_arr[i][3] * Area
        temp4_arr[i][5] = musk_C0 * temp4_arr[i][4] + musk_C1 * temp4_arr[i - 1][4] + musk_C2 * temp4_arr[i - 1][5]

        temp5_arr[i][0] = dri_arr[6][4] * (rdot_arr[i][1]/100)
        temp5_arr[i][1] = temp5_arr[i][0] - temp5_arr[i - 1][0]
        temp5_arr[i][2] = TSD * rdot_arr[i][0] / 100
        temp5_arr[i][3] = temp5_arr[i][1] / delta_T
        temp5_arr[i][4] = 0.278 * temp5_arr[i][3] * Area
        temp5_arr[i][5] = musk_C0 * temp5_arr[i][4] + musk_C1 * temp5_arr[i - 1][4] + musk_C2 * temp5_arr[i - 1][5]

        temp6_arr[i][0] = dri_arr[6][5] * (rdot_arr[i][1]/100)
        temp6_arr[i][1] = temp6_arr[i][0] - temp6_arr[i - 1][0]
        temp6_arr[i][2] = TSD * rdot_arr[i][0] / 100
        temp6_arr[i][3] = temp6_arr[i][1] / delta_T
        temp6_arr[i][4] = 0.278 * temp6_arr[i][3] * Area
        temp6_arr[i][5] = musk_C0 * temp6_arr[i][4] + musk_C1 * temp6_arr[i - 1][4] + musk_C2 * temp6_arr[i - 1][5]

        temp7_arr[i][0] = dri_arr[6][6] * (rdot_arr[i][1]/100)
        temp7_arr[i][1] = temp7_arr[i][0] - temp7_arr[i - 1][0]
        temp7_arr[i][2] = TSD * rdot_arr[i][0] / 100
        temp7_arr[i][3] = temp7_arr[i][1] / delta_T
        temp7_arr[i][4] = 0.278 * temp7_arr[i][3] * Area
        temp7_arr[i][5] = musk_C0 * temp7_arr[i][4] + musk_C1 * temp7_arr[i - 1][4] + musk_C2 * temp7_arr[i - 1][5]

    for i in range(21):
        arr[i][0] = temp1_arr[i][5]
        arr[i][1] = temp2_arr[i][5]
        arr[i][2] = temp3_arr[i][5]
        arr[i][3] = temp4_arr[i][5]
        arr[i][4] = temp5_arr[i][5]
        arr[i][5] = temp6_arr[i][5]
        arr[i][6] = temp7_arr[i][5]

    for i in range(7):
        for j in range(21):
            temp_arr[j] = arr[j][i]
        peakflow_arr[i] = max(temp_arr)
    
    print(peakflow_arr)
    #print(dri_arr[6][0])
    return arr, peakflow_arr

def excecute():
    print("METHOD NOT IMPLEMENTED")

if __name__ == "__main__":
    #print(DesignRainfallInformation())
    #print(FloodRunoffFactorArays(DesignRainfallInformation()))
    dri_arr = FloodRunoffFactorArays(DesignRainfallInformation())
    rdot_arr = rainfall_distr_over_time()
    muskingum_routing(rdot_arr, dri_arr)
