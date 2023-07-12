class Information:

    def __init__(self, infolist):
        # LOCATION
        self.Station = infolist[0]
        self.PDRN = infolist[1]
        self.SDRN = infolist[2]
        self.TDRN = infolist[3]
        self.QDRN = infolist[4]

        # AREA DISTRIBUTION FACTORS
        self.Area = infolist[12]
        self.RuralPerc = infolist[23]
        self.UrbanPerc = infolist[24]
        self.LakePerc = infolist[25]
        self.DolomitePerc = infolist[26]

        # DESIGN RAINFALL INFORMATION
        self.SRT = infolist[55]
        self.MRT = infolist[56]
        self.RLM_SI_DR = infolist[54]
        self.MAP = infolist[57]

        # CATCHMENT CLASSIFICATION
        self.InlandSummerRain = infolist[19]
        self.CoastalWinterRain = infolist[20]
        self.FlatPermeable = infolist[21]
        self.SteepImpermeable = infolist[22]

        # FLOW PATHS: NATURAL
        self.OF = infolist[28]
        self.OFHD = infolist[29]
        self.OFSD = infolist[30]
        self.DTCC = infolist[31]
        self.LMW =infolist[32]
        self.AMWS = infolist[33]

        # FLOW PATHS: ARTIFICIAL
        # -- STREET FLOW --
        self.FPL = infolist[34]
        self.Slope = infolist[35]
        self.ManningValue = infolist[36]
        self.SActualVelocity = infolist[37]
        # -- CANAL FLOW --
        self.CanalLength = infolist[38]
        self.CActualVelocity = infolist[39]
        self.MaxVelocity = infolist[41]

        # -- EXTRA VARIABLES --
        self.ARF = infolist[51]

    def test(self):
        print(self.Station)
