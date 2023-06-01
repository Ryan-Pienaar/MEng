import databases.lrh_rainfall_distr as lrh_database
import numpy as np
import grid_rainfall as gr
import rational as rational

# ------ GLOBAL VARIABLES ------
area = 6331
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

user_arf = 0

def design_rainfall_information():
    arr = np.zeros((7, 7))

def rainfall_distr_over_time():
    arr = np.zeros((21, 2))

def muskingum_routing():
    arr = np.zeros((21, 7))

def excecute():
    print("METHOD NOT IMPLEMENTED")