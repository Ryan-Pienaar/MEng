class Information:

    def __init__(self, infolist):
        # LOCATION
        self.Station = infolist[0]
        self.PDRN = infolist[1]
        self.SDRN = infolist[2]
        self.TDRN = infolist[3]
        self.QDRN = infolist[4]

        # GENERAL CATCHMENT INFO (SRTM 30m Derived)
        self.Area = infolist[12]
        self.ShapeLen = infolist[13]
        self.ShapeArea = infolist[14]
        self.Perim = infolist[15]
        self.LC = infolist[16]
        self.LCkm = infolist[17]
        self.Length = infolist[18]

        # CATCHMENT CLASSIFICATION
        self.SummerRain = infolist[19]
        self.WinterRain = infolist[20]
        self.FlatPerm = infolist[21]
        self.SteepImperm = infolist[22]

        # AREA DISTRIBUTION FACTORS
        self.RurualPerc = infolist[23]
        self.UrbanPerc = infolist[24]
        self.LakesPerc = infolist[25]
        self.DolomitePerc = infolist[26]
        
        # NATURAL FLOW PATHS
        self.LO = infolist[28]
        self.H = infolist[29]
        self.OSFDesc = infolist[30]
        self.LC = infolist[31]
        self.LCH = infolist[32]
        self.SCH = infolist[33]

        # ARTIFICIAL FLOW PATHS
        # STREET FLOW (URBAN)
        self.UrbanFPL = infolist[34]
        self.UrbanSlope = infolist[35]
        self.UrbanManning = infolist[36]
        self.UrbanSActualVelocity = infolist[37]

        # CANAL FLOW (URBAN)
        self.UrbanCanalLen = infolist[38]
        self.UrbanCActualVelocity = infolist[39]
        self.CanalLining = infolist[40]
        self.UrbanCMaxVelocity = infolist[41]

        #CALCULATED VALUES
        self.ElevS = infolist[42]
        self.ElevE = infolist[43]
        self.Elev10 = infolist[44]
        self.Elev85 = infolist[45]
        self.SEqArea = infolist[46]
        self.SAvg = infolist[47]
        self.SCatchAvg = infolist[48]
        self.S1085 = infolist[49]
        self.CoastD_DD = infolist[50]
        self.ARF = infolist[51]

        #DESIGN RAINFALL
        self.MAP = infolist[53]

        #OVERLAND SURFACE FLOW
        self.OSFManning = infolist[58]

        #TIME OF CONCENTRATION
        #self.L = infolist[59]
        #self.TC = infolist[61]

        #VELD TYPES AND REGIONS
        #self.VTRPerc1 = infolist[64]
        #self.VTRNum1 = infolist[65]
        #self.VTRPerc2 = infolist[66]
        #self.VTRNum2 = infolist[67]
        #self.VTRPerc3 = infolist[68]
        #self.VTRNum3 = infolist[69]
        self.AvgOverlandSlope = infolist[99]
        self.OFS = infolist[30]

        #RURAL RUNOFF COEFFICIENTS (C1)
        self.VleisAndPans = infolist[75]
        self.FlatAreas = infolist[76]
        self.Hilly = infolist[77]
        self.SteepAreas = infolist[78]

        #self.HydroSoilGroup = infolist[99]
        self.ThickBushPerc = infolist[80]
        self.LightBushPerc = infolist[81]
        self.GrasslandPerc = infolist[82]
        self.CultivLandContPerc = infolist[83]
        self.CultivLandPerc = infolist[84]
        self.NoVegPerc = infolist[85]
        self.SandyFlatPerc = infolist[86]
        self.SandySteepPerc = infolist[87]
        self.HeavySoilFlatPerc = infolist[88]
        self.HeavySoilSteepPerc = infolist[89]

        #URBAN RUNOFF
        self.HousesPerc = infolist[90]
        self.FlatsPerc = infolist[91]

        #C2 Industry
        self.LightIndustryPerc = infolist[92]
        self.AverageIndustryPerc = infolist[93]
        self.HeavyIndustryPerc = infolist[94]
        #C2 Business
        self.CityCentrePerc = infolist[95]
        self.SuburbanPerc = infolist[96]
        self.StreetsPerc = infolist[97]
        self.MaxFlood = infolist[98]

        #JP CALITZ SCS DATA
        #self.SCSMax = infolist[122]
        #self.SCSMin = infolist[123]
        #self.SCSMean = infolist[124]
        #self.SCSMed = infolist[125]
        #self.SCSMode = infolist[126]

        self.A = infolist[54]
        self.AB = infolist[55]
        self.B = infolist[56]
        self.BC = infolist[57]
        self.C = infolist[58]
        self.CD = infolist[59]
        self.D = infolist[60]


    def test(self):
        print(self.Area)
        print(self.ShapeLen)
        print(self.ShapeArea)
        print(self.Perim)
        print(self.LC)
        print(self.LCkm)
        print(self.Length)
