import math
import numpy
from array import *
import pandas as pd
import methods.grid_rainfall as gr
from databases.catchment import Information
import openpyxl
    

# OUTPUT VARIABLES
C1 = 0.00
C2 = 0.00
TC = 0.00
#TC1 = 0.00
#TC2 = 0.00
#TC3 = 0.00
CT2 = 0.00
CT5 = 0.00
CT10 = 0.00
CT20 = 0.00
CT50 = 0.00
CT100 = 0.00
CT200  = 0.00
PT_MP = 0.00
PT_RLMA_SI = 0.00
IT = 0.00
ARF = 0.00
LT_AVG = 0.00

#GLOBAL VARIABLES
# INFORMATION VARIABLES
global SDRN
global TDRN
global QDRN
global CatchmentDesc
global FlatPermiable
global SteepImpermiable
global SingleRainfallStation
global MultipleRainfallStations
global InlandSummer
global CoastalWinter

# PHYSICAL CATCHMENT CHARACTERISTICS
global RainfallRegion
global MAP
global Area
global OFD # Lo
global OFHD # H
global AOS # So
global OFS # r-value
global LMW # Lch
global ACS # Sch
# -- AREA DISTRIBUTION FACTORS --
global RuralPerc
global UrbanPerc
global LakesPerc
global DolomitePerc
# -- ARTIFICIAL FLOW --
global UseArtifical
# -- STREET FLOW --
global FlowPathLength
global Slope
global ActualVelocityS
# -- CANAL FLOW --
global CanalLength
global ActualVelocityC
global MaxVelocity

# -- RURAL RUNOFF VARIABLES --
#AVERAGE CATCHMENT SLOPE VARIABLE
global VleisAndPans
global FlatAreas
global Hilly
global SteepAreas

# PERMEABILITY VARIABLES
global A
global AB
global B
global BC
global C
global CD
global D

# LAND USE/VEGETATION
global ThickBush_Plantations
global LightBush_Farmlands
global Grasslands
global Cultivatedland_Contoured
global Cultivatedland
global NoVegetation

# -- URBAN RUNOFF VARIABLES --
# LAWNS
global SandyFlat
global SandySteep
global HeavySoilFlat
global HeavySoilSteep

# RESIDENTIAL AREAS
global Houses
global Flats

# INDUSTRY
global LightIndustry
global AverageIndustry
global HeavyIndustry

# BUSINESSES
global CityCentre
global Suburban
global Streets
global MaximumFlood

# --- INPUT VARIABLE ARRAY ---
def ImportCatchmentData(catch):
    #GLOBAL VARIABLES
    # INFORMATION VARIABLES
    global SDRN
    global TDRN
    global QDRN
    global CatchmentDesc
    global FlatPermiable
    global SteepImpermiable
    global SingleRainfallStation
    global MultipleRainfallStations
    global InlandSummer
    global CoastalWinter

    # PHYSICAL CATCHMENT CHARACTERISTICS
    global RainfallRegion
    global MAP
    global Area
    global OFD # Lo
    global OFHD # H
    global AOS # So
    global OFS # r-value
    global LMW # Lch
    global ACS # Sch
    # -- AREA DISTRIBUTION FACTORS --
    global RuralPerc
    global UrbanPerc
    global LakesPerc
    global DolomitePerc
    # -- ARTIFICIAL FLOW --
    global UseArtifical
    # -- STREET FLOW --
    global FlowPathLength
    global Slope
    global ActualVelocityS
    # -- CANAL FLOW --
    global CanalLength
    global ActualVelocityC
    global MaxVelocity

    # -- RURAL RUNOFF VARIABLES --
    #AVERAGE CATCHMENT SLOPE VARIABLE
    global VleisAndPans
    global FlatAreas
    global Hilly
    global SteepAreas

    # PERMEABILITY VARIABLES
    global A
    global AB
    global B
    global BC
    global C
    global CD
    global D

    # LAND USE/VEGETATION
    global ThickBush_Plantations
    global LightBush_Farmlands
    global Grasslands
    global Cultivatedland_Contoured
    global Cultivatedland
    global NoVegetation

    # -- URBAN RUNOFF VARIABLES --
    # LAWNS
    global SandyFlat
    global SandySteep
    global HeavySoilFlat
    global HeavySoilSteep

    # RESIDENTIAL AREAS
    global Houses
    global Flats

    # INDUSTRY
    global LightIndustry
    global AverageIndustry
    global HeavyIndustry

    # BUSINESSES
    global CityCentre
    global Suburban
    global Streets
    global MaximumFlood

    # INFORMATION VARIABLES
    SDRN = catch.SDRN
    TDRN = catch.TDRN
    QDRN = catch.QDRN
    CatchmentDesc = None
    FlatPermiable = catch.FlatPerm
    SteepImpermiable = catch.SteepImperm
    SingleRainfallStation = False
    MultipleRainfallStations = True
    if catch.SummerRain == 1:
        InlandSummer = True
    elif catch.SummerRain == 0:
        InlandSummer = False
    if catch.WinterRain == 1:
        CostalWinter = True
    elif catch.WinterRain == 0:
        CoastalWinter = False

    # PHYSICAL CATCHMENT CHARACTERISTICS
    RainfallRegion = None
    MAP = catch.MAP
    Area = catch.Area
    OFD = catch.LO # Lo
    OFHD = catch.H # H
    AOS = catch.AvgOverlandSlope # So
    OFS = catch.OFS # r-value
    LMW = catch.LCH # Lch
    ACS = catch.SCH # Sch
    # -- AREA DISTRIBUTION FACTORS --
    RuralPerc = catch.RurualPerc
    UrbanPerc = catch.UrbanPerc
    LakesPerc = catch.LakesPerc
    DolomitePerc = catch.DolomitePerc
    # -- ARTIFICIAL FLOW --
    UseArtifical = False
    # -- STREET FLOW --
    FlowPathLength = catch.UrbanFPL
    Slope = catch.UrbanSlope
    ActualVelocityS = catch.UrbanSActualVelocity
    # -- CANAL FLOW --
    CanalLength = catch.UrbanCanalLen
    ActualVelocityC = catch.UrbanCActualVelocity
    MaxVelocity = catch.UrbanCMaxVelocity

    # -- RURAL RUNOFF VARIABLES --
    #AVERAGE CATCHMENT SLOPE VARIABLE
    VleisAndPans = catch.VleisAndPans
    FlatAreas = catch.FlatAreas
    Hilly = catch.Hilly
    SteepAreas = catch.SteepAreas

    # PERMEABILITY VARIABLES
    A = catch.A
    AB = catch.AB
    B = catch.B
    BC = catch.BC
    C = catch.C
    CD = catch.CD
    D = catch.D

    # LAND USE/VEGETATION
    ThickBush_Plantations =catch.ThickBushPerc
    LightBush_Farmlands = catch.LightBushPerc
    Grasslands = catch.GrasslandPerc
    Cultivatedland_Contoured = catch.CultivLandContPerc
    Cultivatedland = catch.CultivLandPerc
    NoVegetation = catch.NoVegPerc

    # -- URBAN RUNOFF VARIABLES --
    # LAWNS
    SandyFlat = catch.SandyFlatPerc
    SandySteep = catch.SandySteepPerc
    HeavySoilFlat = catch.HeavySoilFlatPerc
    HeavySoilSteep = catch.HeavySoilSteepPerc

    # RESIDENTIAL AREAS
    Houses = catch.HousesPerc
    Flats = catch.FlatsPerc

    # INDUSTRY
    LightIndustry = catch.LightIndustryPerc
    AverageIndustry = catch.AverageIndustryPerc
    HeavyIndustry = catch.HeavyIndustryPerc

    # BUSINESSES
    CityCentre = catch.CityCentrePerc
    Suburban = catch.SuburbanPerc
    Streets = catch.StreetsPerc
    MaximumFlood = catch.MaxFlood
    
def RuralRunoffCoefficient():

    # MAIN COEFFICIENTS
    CS = 0.00
    CP = 0.00
    CY = 0.00

    #AVERAGE CATCHMENT SLOPE VARIABLE
    FactorVP = 0.00
    FactorFA = 0.00
    FactorH = 0.00
    FactorSA = 0.00

    # PERMEABILITY VARIABLES
    A_Factor = 0.00
    AB_Factor = 0.00
    B_Factor = 0.00
    BC_Factor = 0.00
    C_Factor = 0.00
    CD_Factor = 0.00
    D_Factor = 0.00

    # LAND USE/VEGETATION
    ThickBush_Plantations_Factor = 0.00
    LightBush_Farmlands_Factor = 0.00
    Grasslands_Factor = 0.00
    Cultivatedland_Contoured_Factor = 0.00
    Cultivatedland_Factor = 0.00
    NoVegetation_Factor = 0.00

    # FACTOR CALCULATIONS
    # --- AVERAGE CATCHMENT SLOPE ---
    # ----- FactorVP -----
    if MAP == 0.00:
        FactorVP = 0.00
        FactorFA = 0.00
        FactorH = 0.00
        FactorSA = 0.00
        A_Factor = 0.00
        AB_Factor = 0.00
        B_Factor = 0.00
        BC_Factor = 0.00
        C_Factor = 0.00
        CD_Factor = 0.00
        D_Factor = 0.00
        ThickBush_Plantations_Factor = 0.00
        LightBush_Farmlands_Factor = 0.00
        Grasslands_Factor = 0.00
        Cultivatedland_Contoured_Factor = 0.00
        Cultivatedland_Factor = 0.00
        NoVegetation_Factor = 0.00

    elif MAP < 600.00:
        FactorVP = 0.01
        FactorFA = 0.06
        FactorH = 0.12
        FactorSA = 0.22
        A_Factor = 0.03
        AB_Factor = 0.04
        B_Factor = 0.06
        BC_Factor = 0.08
        C_Factor = 0.12
        CD_Factor = 0.16
        D_Factor = 0.21
        ThickBush_Plantations_Factor = 0.03
        LightBush_Farmlands_Factor = 0.07
        Grasslands_Factor = 0.17
        Cultivatedland_Contoured_Factor = 0.07
        Cultivatedland_Factor = 0.17
        NoVegetation_Factor = 0.26
    elif MAP >= 600 and MAP < 900:
        FactorVP = 0.03
        FactorFA = 0.08
        FactorH = 0.16
        FactorSA = 0.26
        A_Factor = 0.04
        AB_Factor = 0.06
        B_Factor = 0.08
        BC_Factor = 0.12
        C_Factor = 0.16
        CD_Factor = 0.21
        D_Factor = 0.26
        ThickBush_Plantations_Factor = 0.04
        LightBush_Farmlands_Factor = 0.11
        Grasslands_Factor = 0.21
        Cultivatedland_Contoured_Factor = 0.11
        Cultivatedland_Factor = 0.21
        NoVegetation_Factor = 0.28
    elif MAP > 900:
        FactorVP = 0.05
        FactorFA = 0.11
        FactorH = 0.2
        FactorSA = 0.3
        A_Factor = 0.05
        AB_Factor = 0.07
        B_Factor = 0.1
        BC_Factor = 0.15
        C_Factor = 0.2
        CD_Factor = 0.25
        D_Factor = 0.3
        ThickBush_Plantations_Factor = 0.05
        LightBush_Farmlands_Factor = 0.15
        Grasslands_Factor = 0.25
        Cultivatedland_Contoured_Factor = 0.15
        Cultivatedland_Factor = 0.25
        NoVegetation_Factor = 0.3

    # ----- CS CALCULATION -----
    CS1 = 0.00
    CS2 = 0.00
    CS3 = 0.00
    CS4 = 0.00

    if VleisAndPans == 0:
        CS1 = 0.00
    else:
        CS1 = VleisAndPans / 100 * FactorVP

    if FlatAreas == 0:
        CS2 = 0.00
    else:
        CS2 = FlatAreas / 100 * FactorFA

    if Hilly == 0:
        CS3 = 0.00
    else:
        CS3 = Hilly / 100 * FactorH

    if SteepAreas == 0:
        CS4 = 0.00
    else:
        CS4 = SteepAreas / 100 * FactorSA

    CS = CS1 + CS2 + CS3 + CS4


    # ----- CP CALCULATIONS -----
    CP1 = 0.00
    CP2 = 0.00
    CP3 = 0.00
    CP4 = 0.00
    CP5 = 0.00
    CP6 = 0.00
    CP7 = 0.00

    if A == 0:
        CP1 = 0.00
    else:
        CP1 = A / 100 * A_Factor

    if AB == 0:
        CP2 = 0.00
    else:
        CP2 = AB / 100 * AB_Factor

    if B == 0:
        CP3 = 0.00
    else:
        CP3 = B / 100 * B_Factor

    if BC == 0:
        CP4 = 0.00
    else:
        CP4 = BC / 100 * BC_Factor

    if C == 0:
        CP5 = 0.00
    else:
        CP5 = C / 100 * C_Factor

    if CD == 0:
        CP6 = 0.00
    else:
        CP6 = CD / 100 * CD_Factor

    if D == 0:
        CP7 = 0.00
    else:
        CP7 = D / 100 * D_Factor

    CP = CP1 + CP2 + CP3 + CP4 + CP5 + CP6 + CP7


    # ----- CV CALCULATIONS -----
    CV1 = 0.00
    CV2 = 0.00
    CV3 = 0.00
    CV4 = 0.00
    CV5 = 0.00
    CV6 = 0.00

    if ThickBush_Plantations == 0.00:
        CV1 = 0.00
    else:
        CV1 = (ThickBush_Plantations / 100) * ThickBush_Plantations_Factor

    if LightBush_Farmlands == 0.00:
        CV2 = 0.00
    else:
        CV2 = (LightBush_Farmlands / 100) * LightBush_Farmlands_Factor

    if Grasslands == 0.00:
        CV3 = 0.00
    else:
        CV3 = (Grasslands / 100) * Grasslands_Factor

    if Cultivatedland_Contoured == 0.00:
        CV4 = 0.00
    else:
        CV4 = (Cultivatedland_Contoured / 100) * Cultivatedland_Contoured_Factor

    if Cultivatedland == 0.00:
        CV5 = 0.00
    else:
        CV5 = (Cultivatedland / 100) * Cultivatedland_Factor

    if NoVegetation == 0.00:
        CV6 = 0.00
    else:
        CV6 = (NoVegetation / 100) * NoVegetation_Factor

    CV = CV1 + CV2 + CV3 + CV4 + CV5 + CV6

    return (CP + CS + CV)

def UrbanRunoffCoefficients():

    # OUTPUT VARIABLES
    CL = 0.00
    CR = 0.00
    CI = 0.00
    CB = 0.00

    # LAWNS
    FactorSF = 0.1
    FactorSS = 0.2
    FactorHSF = 0.17
    FactorHSS = 0.35

    # RESIDENTIAL AREAS
    Houses_Factor = 0.5
    Flats_Factor = 0.7

    # INDUSTRY
    FactorLI = 0.8
    FactorAI = 0.85
    FactorHI = 0.9

    # BUSINESSES
    FactorCC = 0.95
    FactorSurb = 0.7
    FactorStreets = 0.95
    FactorMF = 1

    # ----- CL CALCULATION -----
    CL1 = 0.00
    CL2 = 0.00
    CL3 = 0.00
    CL4 = 0.00

    if SandyFlat == 0.00:
        CL1 = 0.00
    else:
        CL1 = (SandyFlat / 100) * FactorSF

    if SandySteep == 0.00:
        CL2 = 0.00
    else:
        CL2 = (SandySteep / 100) * FactorSS

    if HeavySoilFlat == 0.00:
        CL3 = 0.00
    else:
        CL3 = (HeavySoilFlat / 100) * FactorHSF

    if HeavySoilSteep == 0.00:
        CL4 = 0.00
    else:
        CL4 = (HeavySoilSteep / 100) * FactorHSS

    CL = CL1 + CL2 + CL3 + CL4

    # ----- CR CALCULATIONS -----
    CR1 = 0.00
    CR2 = 0.00

    if Houses == 0.00:
        CR1 = 0.00
    else:
        CR1 = (Houses / 100) * Houses_Factor

    if Flats == 0.00:
        CR2 = 0.00
    else:
        CR2 = (Flats / 100) * Flats_Factor

    CR = CR1 + CR2

    # ----- CI CALCULATIONS -----
    CI1 = 0.00
    CI2 = 0.00
    CI3 = 0.00

    if LightIndustry == 0.00:
        CI1 = 0.00
    else:
        CI1 = (LightIndustry / 100) * FactorLI

    if AverageIndustry == 0.00:
        CI2 = 0.00
    else:
        CI2 = (AverageIndustry / 100) * FactorAI

    if HeavyIndustry == 0.00:
        CI3 = 0.00
    else:
        CI3 = (HeavyIndustry / 100) * FactorHI

    CI = CI1 + CI2 + CI3

    # ----- CB CCALCULATIONS -----
    CB1 = 0.00
    CB2 = 0.00
    CB3 = 0.00
    CB4 = 0.00

    if CityCentre == 0.00:
        CB1 = 0.00
    else:
        CB1 = (CityCentre / 100) * FactorCC

    if Suburban == 0.00:
        CB2 = 0.00
    else:
        CB2 = (Suburban / 100) * FactorSurb

    if Streets == 0.00:
        CB3 = 0.00
    else:
        CB3 = (Streets / 100) * FactorStreets

    if MaximumFlood == 0.00:
        CB4 = 0.00
    else:
        CB4 = (MaximumFlood / 100) * FactorMF

    CB = CB1 + CB2 + CB3 + CB4

    return (CL + CR + CI + CB)

def TimeOfConcentration():
    r_val_table = [0.02, 0.02, 0.025, 0.035, 0.06, 0.1, 0.1, 0.15, 0.25, 0.3, 0.3, 0.4, 0.4, 0.8]

    tau = 0.00
    UseCorrectionFactor = False
    TC1 = 0.00
    TC2 = 0.00
    TC3 = 0.00

    # ----- CORRECTION FACTOR CALCULATION -----
    if Area < 1:
        tau = 2
    elif Area >= 1 and Area <= 100:
        tau = 2 - (0.5 * numpy.log10(Area))
    elif Area >= 100 and Area <= 5000:
        tau = 1
    elif Area >= 5000 and Area <= 100000:
        tau = 2.42 - (0.385 * numpy.log10(Area))
    elif Area > 100000:
        tau = 0.5
    else:
        tau = 0.00

    # ----- TC1 CALCULATION -----
    if OFD == 0:
        TC1 = 0
    else:
        TC1 = 0.604 * (math.pow((r_val_table[OFS-1] * OFD) / (math.pow(AOS, 0.5)), 0.467))

    # ----- TC2 CALCULATION -----
    if ACS == 0:
        TC2 = 0
    elif UseCorrectionFactor:
        TC2 = tau * math.pow(((0.87 * math.pow(LMW, 2)) / (1000 * ACS)), 0.385)
    elif not UseCorrectionFactor:
        TC2 = math.pow(((0.87 * math.pow(LMW, 2)) / (1000 * ACS)), 0.385)

    # ----- TC3 CALCULATIONS -----
    if not UseArtifical:
        TC3 = 0
    elif FlowPathLength == 0:
        TC3 = (CanalLength / ActualVelocityC) / 3.6
    elif CanalLength == 0:
        TC3 = (FlowPathLength / ActualVelocityS) / 3.6
    else:
        TC3 = ((CanalLength / ActualVelocityC) / 3.6) + ((FlowPathLength / ActualVelocityS) / 3.6)

    #print(TC1)
    #print(TC2)
    #print(TC3)

    return (TC1 + TC2 + TC3)


    #print(tau)

def WheightedRunoffCoefficients(C1, C2):
    T2 = 0
    T5 = 1
    T10 = 2
    T20 = 3
    T50 = 4
    T100 = 5
    T200 = 6
    RRC = 0
    DRRC = 1
    AdjustmentFactor = 2
    AdjustedRRC = 3
    WRC = 4

    arr = numpy.zeros((5,7))

    if FlatPermiable:
        arr[2][0] = 0.5
        arr[2][1] = 0.55
        arr[2][2] = 0.6
        arr[2][3] = 0.67
        arr[2][4] = 0.83
        arr[2][5] = 1
        arr[2][6] = 1.2
    elif SteepImpermiable:
        arr[2][0] = 0.75
        arr[2][1] = 0.8
        arr[2][2] = 0.85
        arr[2][3] = 0.9
        arr[2][4] = 0.95
        arr[2][5] = 1
        arr[2][6] = 1.2
    
    for i in range(7):
        arr[0][i] = C1
        arr[1][i] = (C1 * (1 - DolomitePerc/100) + (C1 * DolomitePerc / 100) * ((VleisAndPans/100*0.1) + (FlatAreas/100*0.2) + (Hilly/100*0.35) + (SteepAreas/100*0.5)))
        arr[3][i] = arr[1][i] * arr[2][i]
        arr[4][i] = RuralPerc/100*arr[3][i] + UrbanPerc/100*C2 + LakesPerc/100*0

    return arr

def DesignRainfallInformation(TC, wrc_arr):
    arr = numpy.zeros((5,7))
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
        
        if UseArtifical:
            arr[1][i] = gr.lookup(47.875, i+1, rainfall_grid)
        else:
            arr[1][i] = 0

        if TC == 0:
            arr[2][i] = 0
        elif arr[1][i] == 0:
            arr[2][i] = arr[0][i] / TC
        elif arr[1][i] != 0:
            arr[2][i] = arr[1][i] / TC
        
        if Area == 0:
            arr[3][i] = 0
        elif Area <= 10 and TC > 1:
            arr[3][i] = 100
        else:
            arr[3][i] = math.pow((90000 - 12800 * math.log(Area) + 9830 * math.log(TC * 60)), 0.4)

        if arr[2][i] == 0:
            arr[4][i] == 0
        elif Area <= 10 and TC > 10:
            arr[4][i] = arr[2][i]
        elif ARF == 0:
            arr[4][i] = (arr[3][i] / 100) * arr[2][i]
        else:
            arr[4][i] = (ARF / 100) * arr[2][i]

    return arr
    
def PeakFlow(wrc_arr, dri_arr):
    arr = numpy.zeros(7)

    for i in range(7):
        if dri_arr[4][i] == 0:
            arr[i] = 0
        else:
            arr[i] = wrc_arr[4][i] * dri_arr[4][i] * Area / 3.6

    return arr

def print_array(arr):
    arr_length = len(arr)
    arr_width = int(numpy.size(arr) / arr_length)
    
    print("-------------------------------------------------------------------------------------")
    print("|     2     |     5     |    10     |    20     |    50     |    100    |    200    |")
    print("-------------------------------------------------------------------------------------")
    for i in range (arr_length):
        temp = 1
        print("|  ", end="")
        for j in range (arr_width):
            print(f'{round(arr[i][j], 6):.6f}' + " |  ", end="")
        print()
    print("-------------------------------------------------------------------------------------")

def excecute(CatchList):
    # Create a new Excel workbook
    wb = openpyxl.Workbook()

    # Select the active worksheet
    ws = wb.active

    # Define the precision you want for the floating point numbers
    precision = 3

    # Write data to Excel file
    for i in range(411):
        print(str(i/411*100)+"%")
        ImportCatchmentData(CatchList[i])
        C1 = RuralRunoffCoefficient()
        C2 = UrbanRunoffCoefficients()
        TC = TimeOfConcentration()
        WRC_ARR = WheightedRunoffCoefficients(C1, C2)
        DRI_ARR = DesignRainfallInformation(TC, WRC_ARR)
        PF_ARR = PeakFlow(WRC_ARR, DRI_ARR)
        combined_data = [str(CatchList[i].Station)] + [round(val, precision) for val in PF_ARR]
        ws.append(combined_data)

    # Save the Excel workbook
    wb.save("rational.xlsx")

if __name__ == '__main__':
    #excecute()
    #read_variables()
    temp = 0











