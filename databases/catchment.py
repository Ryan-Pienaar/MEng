class Information:

    def __init__(self, infolist):
        # LOCATION
        self.Station = infolist[0]
        self.PDRN = infolist[1]
        self.SDRN = infolist[2]
        self.TDRN = infolist[3]
        self.QDRN = infolist[4]
        self.CatchmentDescr = None

        # AREA DISTRIBUTION FACTORS
        self.Area = 0.00
        self.RuralPerc = 0.00
        self.UrbanPerc = 0.00
        self.LakePerc = 0.00
        self.DolomitePerc = 0.00

        # DESIGN RAINFALL INFORMATION
        self.SRT = False
        self.MRT = False
        self.RLM_SI_DR = False
        self.MAP = 0.00

        # CATCHMENT CLASSIFICATION
        self.InlandSummerRain = False
        self.CoastalWinterRain = False
        self.FlatPermeable = False
        self.SteepImpermeable = False

        # FLOW PATHS: NATURAL
        self.OF = 0.00
        self.OFHD = 0.00
        self.OFSD = None
        self.OFCC = 0.00
        self.LMW = 0.00
        self.AMWS = 0.00

        # FLOW PATHS: ARTIFICIAL
        # -- STREET FLOW --
        self.FPL = 0.00
        self.Slope = 0.00
        self.ManningValue = 0.00
        self.SActualVelocity = 0.00
        # -- CANAL FLOW --
        self.CanalLength = 0.00
        self.CActualVelocity = 0.00
        self.MaxVelocity = 0.00

        # -- EXTRA VARIABLES --
        ARF = 0.00

    def test(self):
        print(self.Station)
