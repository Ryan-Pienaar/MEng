import numpy as np
import math as math

# ----- GLOBAL VARIABLES -----
#TODO: Correct how certain variables are obtained
area = 6331
MAP = 518
veldtype_nr1 = 4
veldtype_nr2 = 7
veldtype_nr3 = 5
veldtype_perc1 = 97.29
veldtype_perc2 = 2.71
veldtype_perc3 = 0
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

def design_rainfall_info():
    main_arr = np.zeros((8, 10))
    arr1 = np.zeros((8, 5))
    arr2 = np.zeros((8, 5))
    incr_vars = [12, 14, 16, 18, 20]

    for i in range(5):
        if single_rainfall_station or multiple_rainfall_station:
            if incr_vars[i] == 0:
                arr1[0][i] = 0
                arr2[0][i] = 0
            elif inland_summer:
                arr1[0][i] = incr_vars[i] * (217.8/math.pow(1+4.164*incr_vars[i], 0.8832)) * returnp_ratio1 * ((18.79+0.17*MAP)/100)
                arr2[0][i] = incr_vars[i] * (217.8/math.pow(1+4.164*incr_vars[i], 0.8832)) * returnp_ratio2 * ((18.79+0.17*MAP)/100)

    print(arr1)
    print(arr2)


def peak_flow_adjust():
    temp = 0

def s_curve_lagging():
    temp = 0

if __name__ == "__main__":
    design_rainfall_info()



def excecute():
    print("METHOD NOT IMPLEMENTED")