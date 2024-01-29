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
        self.MAP = infolist[57]

        #OVERLAND SURFACE FLOW
        self.OSFManning = infolist[58]

        #TIME OF CONCENTRATION
        self.L = infolist[59]
        self.TC = infolist[61]

        #VELD TYPES AND REGIONS
        self.VTRPerc1 = infolist[64]
        self.VTRNum1 = infolist[65]
        self.VTRPerc2 = infolist[66]
        self.VTRNum2 = infolist[67]
        self.VTRPerc3 = infolist[68]
        self.VTRNum3 = infolist[69]
        self.AvgOverlandSlope = infolist[79]
        self.OFS = infolist[80]

        #RURAL RUNOFF COEFFICIENTS (C1)
        self.VleisAndPans = infolist[95]
        self.FlatAreas = infolist[96]
        self.Hilly = infolist[97]
        self.SteepAreas = infolist[98]

        self.HydroSoilGroup = infolist[99]
        self.ThickBushPerc = infolist[100]
        self.LightBushPerc = infolist[101]
        self.GrasslandPerc = infolist[102]
        self.CultivLandContPerc = infolist[103]
        self.CultivLandPerc = infolist[104]
        self.NoVegPerc = infolist[105]
        self.SandyFlatPerc = infolist[106]
        self.SandySteepPerc = infolist[107]
        self.HeavySoilFlatPerc = infolist[108]
        self.HeavySoilSteepPerc = infolist[109]

        #URBAN RUNOFF
        self.HousesPerc = infolist[110]
        self.FlatsPerc = infolist[111]

        #C2 Industry
        self.LightIndustryPerc = infolist[112]
        self.AverageIndustryPerc = infolist[113]
        self.HeavyIndustryPerc = infolist[114]
        #C2 Business
        self.CityCentrePerc = infolist[115]
        self.SuburbanPerc = infolist[116]
        self.StreetsPerc = infolist[117]
        self.MaxFlood = infolist[118]

        #JP CALITZ SCS DATA
        self.SCSMax = infolist[122]
        self.SCSMin = infolist[123]
        self.SCSMean = infolist[124]
        self.SCSMed = infolist[125]
        self.SCSMode = infolist[126]


    def test(self):
        print(self.Area)
        print(self.ShapeLen)
        print(self.ShapeArea)
        print(self.Perim)
        print(self.LC)
        print(self.LCkm)
        print(self.Length)
