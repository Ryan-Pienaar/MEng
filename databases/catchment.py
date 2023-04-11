class Information:
    # LOCATION
    Station = None
    PDRN = None
    SDRN = None
    TDRN = None
    QDRN = None
    CatchmentDescr = None

    # AREA DISTRIBUTION FACOTRS
    Size = 0.00
    RuralPerc = 0.00
    UrbanPerc = 0.00
    LakePerc = 0.00
    DolomitePerc = 0.00

    # DESIGN RAINFALL INFORMATION
    SRT = False
    MRT = False
    RLM_SI_DR = 0.00

    # CATCHMENT CLASSIFICATION
    SummerRain = False
    WinterRain = False
    FlatPermeable = False
    SteepImpermeable = False

    # FLOW PATHS: NATURAL
    OF = 0.00
    OFHD = 0.00
    OFSD = None
    OFCC = 0.00
    LMW = 0.00
    AMWS = 0.00

    # FLOW PATHS: ARTIFICIAL
    # -- STREET FLOW --
    FPL = 0.00
    Slope = 0.00
    ManningValue = 0.00
    SActualVelocity = 0.00
    # -- CANAL FLOW --
    CanalLength = 0.00
    CActualVelocity = 0.00
    MaxVelocity = 0.00
