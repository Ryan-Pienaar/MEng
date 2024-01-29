import numpy as np
import math as math
import methods.design_rainfall as dr
import methods.rational as rm


# ----- GLOBAL VARIABLES -----
#TODO: Calculations for global variables from other methods

rlma_saws = True
tr102 = False
arith_mean = True
polygon = False
single_rainfall = False
multiple_rainfall = True
grid_rainfall = False

area = 6331
LO = 0
SO = 0
r_value = 0
LCH = 186,696
SCH = 0.00131
S = 0.04186
FPL = 0
slope = 0
av1 = 0
canal_length = 0
av2 = 0
TC1 = 0
TC2 = 0
TC3 = 0
TC = 0
TL1 = 0.6 * TC
TL2 = 0
TL3 = 21.749
use_TL1 = False
use_TL2 = True
use_TL3 = False

R = 62
y2d1_max = 48
MAP = 518

def sum(arr, col_nr):
    total = 0
    
    for i in range(len(arr)):
        total += arr[i][col_nr]
    
    return total

def design_rainfall():
    arr = np.zeros((2, 7))
    temp_arr1 = dr.excecute(1)
    temp_arr2 = dr.excecute(2)
    temp_arr3 = dr.excecute(3)
    temp_arr4 = dr.excecute(4)

    for i in range(7):
        if grid_rainfall:
            arr[0][i] = 0
        elif rlma_saws and arith_mean:
            arr[0][i] = round(temp_arr1[0][i])
        elif rlma_saws and polygon:
            arr[0][i] = temp_arr2[0][i]
        elif tr102 and arith_mean:
            arr[0][i] = temp_arr3[0][i]
        elif tr102 and polygon:
            arr[0][i] = temp_arr4[0][i]

    print(arr)

            
        

def initial_weighted_cn():
    sec1_cn_sum = 0
    sec2_cn_sum = 0
    sec1_area_sum = 0
    sec2_area_sum = 0
    


    # ---- SECTION 1 ----
    #Generalised CN numbers
    arr1 = np.zeros((7, 3))

    #Garden crops
    arr2 = np.zeros((2, 3))

    #Small grain
    arr3 = np.zeros((13, 3))

    #Sugar cane
    arr4 = np.zeros((8, 3))

    #Woods and scrub
    arr5 = np.zeros((4, 3))

    #Urban/suburban land uses
    arr6 = np.zeros((7, 3))

    # ---- SECTION 2 ----

    #Seeded legumes/rotational meadow
    arr7 = np.zeros((6, 3))

    #Fallow
    arr8 = np.zeros((3, 3))

    #Row crops
    arr9 = np.zeros((12, 3))

    #Pasture or veld
    arr10 = np.zeros((8 , 3))

    #Forests/Plantations/Orchids
    arr11 = np.zeros((4, 3))

    #Urban/suburban land uses
    arr12 = np.zeros((7, 3))

def runoff_volume(sec1_sum, sec2_sum):
    temp = 0


if __name__ == "__main__":
    design_rainfall()

def execute():
    print("Working on this method")


