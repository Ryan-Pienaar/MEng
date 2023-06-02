import lrh_rainfall_distr as lrh_database
import numpy as np
import grid_rainfall as gr
import rational as rational
import math as math

# ------ GLOBAL VARIABLES ------
SingleRainfallStation = False
MultipleRainfallStations = True
InlandSummer = True
OutlandWinter = False

Area = 6331
MAP = 518

veldtype1_nr = 0
veldtype2_nr = 0
veldtype3_nr = 0

veldtype1_perc = 0
veldtype2_perc = 0
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
    
        if Area <= 1000:
            arr[4][i] = 0
        elif Area > 1000 and Area <= 3000:
            arr[5][i] = 

    return arr

def rainfall_distr_over_time():
    arr = np.zeros((21, 2))

def muskingum_routing():
    arr = np.zeros((21, 7))

def excecute():
    print("METHOD NOT IMPLEMENTED")

if __name__ == "__main__":
    print(DesignRainfallInformation())
