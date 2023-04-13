
# OUTPUT VARIABLES
C1 = 0.00
C2 = 0.00
TC = 0.00
TC1 = 0.00
TC2 = 0.00
TC3 = 0.00
C1D = 0.00
FT = 0.00
C1T = 0.00
CT = 0.00
PT_MP = 0.00
PT_RLMA_SI = 0.00
IT = 0.00
ARF = 0.00
LT_AVG = 0.00

# INFORMATION VARIABLES
SDRN = None
TDRN = None
QSDRN = None
CatchmentDesc = None

# PHYSICAL CATCHMENT CHARACTERISTICS
RainfallRegion = None
MAP = 518
Area = 0.00
OFD = 0.00 # Lo
OFHD = 0.00 # H
AOS = 0.00 # So
OFS = 0.00 # r-value
LMW = 0.00 # Lch
ACS = 0.00 # Sch
# -- AREA DISTRIBUTION FACTORS --
RuralPerc = 0.00
UrbanPerc = 0.00
LakesPerc = 0.00
DolomitePerc = 0.00
# -- ARTIFICIAL FLOW --
# -- STREET FLOW --
FlowPathLength = 0.00
Slope = 0.00
ActualVelocityS = 0.00
# -- CANAL FLOW --
CanalLength = 0.00
ActualVelocityC = 0.00
MaxVelocity = 0.00

def RuralRunoffCoefficient():

    # MAIN COEFFICIENTS
    CS = 0.00
    CP = 0.00
    CY = 0.00

    #AVERAGE CATCHMENT SLOPE VARIABLE
    VleisAndPans = 57.6
    FlatAreas = 34.3
    Hilly = 6.7
    SteepAreas = 1.4

    FactorVP = 0.00
    FactorFA = 0.00
    FactorH = 0.00
    FactorSA = 0.00

    # PERMEABILITY VARIABLES
    A = 0.00
    AB = 23.15
    B = 27.31
    BC = 2.82
    C = 0.00
    CD = 15.69
    D = 31.03
    A_Factor = 0.00
    AB_Factor = 0.00
    B_Factor = 0.00
    BC_Factor = 0.00
    C_Factor = 0.00
    CD_Factor = 0.00
    D_Factor = 0.00

    # LAND USE/VEGETATION
    ThickBush_Plantations = 4.34
    LightBush_Farmlands = 0.73
    Grasslands = 80.18
    Cultivatedland_Contoured = 0.00
    Cultivatedland = 14.29
    NoVegetation = 0.46
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

    elif MAP < 600:
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

    # ----- TOTAL C1 CALCULATION -----
    print("CP: " + str(CP))
    print("CD: " + str(CS))
    print("CV: " + str(CV))
    print("C1: " + str(C1))

    return (CP + CS + CV)


def UrbanRunoffCoefficients(self):

    # OUTPUT VARIABLES
    CL = 0.00
    CR = 0.00
    CI = 0.00
    CB = 0.00

    # LAWNS
    SandyFlat = 0.00
    SandySteep = 0.00
    HeavySoilFlat = 0.00
    HeavySoilSteep = 0.00

    # RESIDENTIAL AREAS
    Houses = 0.00
    Flats = 0.00

    # INDUSTRY
    LightIndustry = 0.00
    AverageIndustry = 0.00
    HeavyIndustry = 0.00

    # BUSINESSES
    CityCentre = 0.00
    Suburban = 0.00
    Streets = 0.00
    MaximumFlood = 0.00

def WheightedRunoffCoefficients(self):
    temp = 1

def DesignRainfallInformation(self):
    temp = 1

if __name__ == '__main__':
    print(RuralRunoffCoefficient())











