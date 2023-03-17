import dcs
from pydcs_extensions.hercules.hercules import Hercules
from pydcs_extensions.a4ec.a4ec import A_4E_C
from pydcs_extensions.bronco.bronco import Bronco_OV_10A
import calvinball

class CyprusInvasion(calvinball.mission.Mission):
    def __init__(self) -> None:
        t = dcs.terrain.Syria()
        miz_name = "CyprusInvasion"
        ctld = CyprusInvasionCtld()
        clients = CyprusInvasionClients()
        red_airwings = CyprusInvasionRedAirwings()
        blue_airwings = CyprusInvasionBlueAirwings()

        super().__init__(t, miz_name, ctld, clients, red_airwings, blue_airwings)

class CyprusInvasionCtld(calvinball.ctld.Ctld):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

class CyprusInvasionClients(calvinball.clients.Clients):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission, edit: bool):
        m.groundControl.blue_game_masters = 1
        m.groundControl.blue_tactical_commander = 1
        m.groundControl.blue_jtac = 2
        m.groundControl.red_game_masters = 1

        m.coalition["blue"].set_bullseye({"x": -32691, "y": -270357})

        airport_set = [
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Akrotiri"],
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    { "airframe": dcs.helicopters.Mi_24P, "count": 4, "parking": [42, 43, 44, 45], "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation" },
                    { "airframe": dcs.helicopters.Mi_8MT, "count": 4, "parking": [2, 3, 4, 5], "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN" },
                    { "airframe": dcs.helicopters.UH_1H, "count": 4, "parking": [33, 34, 35, 36], "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972" },
                    { "airframe": dcs.helicopters.AH_64D_BLK_II, "count": 4, "parking": [10, 11, 12, 13], "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit" },
                    { "airframe": dcs.helicopters.SA342L, "count": 1, "parking": [20], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2" },
                    { "airframe": dcs.helicopters.SA342M, "count": 1, "parking": [21], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet" },
                    { "airframe": dcs.helicopters.Ka_50, "count": 2, "parking": [38, 39], "fuel": 0.6, "loadout": "Empty", "livery": "Russia New Year" },
                    { "airframe": dcs.planes.AV8BNA, "count": 2, "parking": [32, 37], "fuel": 1, "loadout": "Empty", "livery": "vma-214" },
                    { "airframe": dcs.planes.A_10C_2, "count": 1, "parking": [30], "fuel": 1, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                    { "airframe": dcs.planes.A_10A, "count": 1, "parking": [31], "fuel": 1, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                    { "airframe": dcs.planes.P_51D_30_NA, "count": 1, "parking": [46], "fuel": 1, "loadout": "Empty", "livery": "Ukraine Modern" },
                    { "airframe": dcs.planes.AJS37, "count": 1, "parking": [28], "fuel": 1, "loadout": "Empty", "livery": "SF-37 Akktu Stakki - F21" },
                    { "airframe": dcs.planes.C_101CC, "count": 1, "parking": [27], "fuel": 1, "loadout": "Empty", "livery": "usaf agressor fictional" },
                    { "airframe": dcs.planes.L_39ZA, "count": 1, "parking": [26], "fuel": 1, "loadout": "Empty", "livery": "algerian af tiger nl-36" },
                    { "airframe": dcs.planes.F_5E_3, "count": 2, "parking": [18, 19], "fuel": 1, "loadout": "Empty", "livery": "BR FAB 4846" },
                    { "airframe": dcs.planes.Su_25, "count": 2, "parking": [22, 23], "fuel": 1, "loadout": "Empty", "livery": "petal camo scheme #1 (native). 299th brigade" },
                    { "airframe": dcs.planes.Su_25T, "count": 2, "parking": [8, 9], "fuel": 1, "loadout": "Empty", "livery": "Algerian AF Desert KU-03" },
                    { "airframe": dcs.planes.M_2000C, "count": 1, "parking": [14], "fuel": 1, "loadout": "Empty", "livery": "2003 Tigermeet" },
                    { "airframe": dcs.planes.MiG_21Bis, "count": 2, "parking": [29, 7], "fuel": 1, "loadout": "Empty", "livery": "HuAF 31st AB (Turul Sqn)" },
                    { "airframe": dcs.planes.MiG_19P, "count": 1, "parking": [16], "fuel": 1, "loadout": "Empty", "livery": "DDR - Fictional" },
                    { "airframe": dcs.planes.Mirage_F1CE, "count": 1, "parking": [17], "fuel": 1, "loadout": "Empty", "livery": "USA AGGRESSOR Colour (CE)" },
                    { "airframe": dcs.planes.F_86F_Sabre, "count": 1, "parking": [6], "fuel": 1, "loadout": "Empty", "livery": "Royal Saudi Air Force" },
                    { "airframe": dcs.planes.MB_339A, "count": 2, "parking": [40, 41], "fuel": 1, "loadout": "Empty", "livery": "MB339AN 'NIGERIA'" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Paphos"],
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    { "airframe": dcs.helicopters.Mi_24P, "count": 4, "parking": [41, 42, 43, 44], "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation" },
                    { "airframe": dcs.helicopters.Mi_8MT, "count": 4, "parking": [37, 38, 39, 40], "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN" },
                    { "airframe": dcs.helicopters.UH_1H, "count": 4, "parking": [20, 21, 22, 23], "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972" },
                    { "airframe": dcs.helicopters.AH_64D_BLK_II, "count": 4, "parking": [10, 11, 12, 13], "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit" },
                    { "airframe": dcs.helicopters.SA342L, "count": 1, "parking": [2], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2" },
                    { "airframe": dcs.helicopters.SA342M, "count": 1, "parking": [4], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet" },
                    { "airframe": dcs.helicopters.Ka_50, "count": 2, "parking": [8, 9], "fuel": 0.6, "loadout": "Empty", "livery": "Russia New Year" },
                    { "airframe": dcs.planes.AV8BNA, "count": 2, "parking": [6, 7], "fuel": 1, "loadout": "Empty", "livery": "vma-214" },
                    { "airframe": dcs.planes.A_10C_2, "count": 1, "parking": [34], "fuel": 1, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                    { "airframe": dcs.planes.A_10A, "count": 1, "parking": [36], "fuel": 1, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                    { "airframe": dcs.planes.P_51D_30_NA, "count": 1, "parking": [32], "fuel": 1, "loadout": "Empty", "livery": "Ukraine Modern" },
                    { "airframe": dcs.planes.AJS37, "count": 1, "parking": [31], "fuel": 1, "loadout": "Empty", "livery": "SF-37 Akktu Stakki - F21" },
                    { "airframe": dcs.planes.C_101CC, "count": 1, "parking": [30], "fuel": 1, "loadout": "Empty", "livery": "usaf agressor fictional" },
                    { "airframe": dcs.planes.L_39ZA, "count": 1, "parking": [29], "fuel": 1, "loadout": "Empty", "livery": "algerian af tiger nl-36" },
                    { "airframe": dcs.planes.F_5E_3, "count": 2, "parking": [18, 19], "fuel": 1, "loadout": "Empty", "livery": "BR FAB 4846" },
                    { "airframe": dcs.planes.Su_25, "count": 2, "parking": [16, 17], "fuel": 1, "loadout": "Empty", "livery": "petal camo scheme #1 (native). 299th brigade" },
                    { "airframe": dcs.planes.Su_25T, "count": 2, "parking": [14, 15], "fuel": 1, "loadout": "Empty", "livery": "Algerian AF Desert KU-03" },
                    { "airframe": dcs.planes.M_2000C, "count": 1, "parking": [33], "fuel": 1, "loadout": "Empty", "livery": "2003 Tigermeet" },
                    { "airframe": dcs.planes.MiG_21Bis, "count": 1, "parking": [24], "fuel": 1, "loadout": "Empty", "livery": "HuAF 31st AB (Turul Sqn)" },
                    { "airframe": dcs.planes.MiG_19P, "count": 1, "parking": [26], "fuel": 1, "loadout": "Empty", "livery": "DDR - Fictional" },
                    { "airframe": dcs.planes.Mirage_F1CE, "count": 1, "parking": [27], "fuel": 1, "loadout": "Empty", "livery": "USA AGGRESSOR Colour (CE)" },
                    { "airframe": dcs.planes.F_86F_Sabre, "count": 1, "parking": [28], "fuel": 1, "loadout": "Empty", "livery": "Royal Saudi Air Force" },
                    { "airframe": dcs.planes.MB_339A, "count": 1, "parking": [35], "fuel": 1, "loadout": "Empty", "livery": "MB339AN 'NIGERIA'" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Larnaca"],
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    { "airframe": dcs.helicopters.Mi_24P, "count": 4, "parking": [8, 9, 10, 11], "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation" },
                    { "airframe": dcs.helicopters.Mi_8MT, "count": 4, "parking": [12, 13, 14, 15], "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN" },
                    { "airframe": dcs.helicopters.UH_1H, "count": 4, "parking": [16, 17, 18, 19], "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972" },
                    { "airframe": dcs.helicopters.AH_64D_BLK_II, "count": 4, "parking": [35, 7, 34, 6], "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit" },
                    { "airframe": dcs.helicopters.SA342L, "count": 1, "parking": [36], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2" },
                    { "airframe": dcs.helicopters.SA342M, "count": 1, "parking": [37], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet" },
                    { "airframe": dcs.helicopters.Ka_50, "count": 2, "parking": [4, 5], "fuel": 0.6, "loadout": "Empty", "livery": "Russia New Year" },
                    { "airframe": dcs.planes.AV8BNA, "count": 2, "parking": [23, 24], "fuel": 1, "loadout": "Empty", "livery": "vma-214" },
                    { "airframe": dcs.planes.A_10C_2, "count": 1, "parking": [25], "fuel": 1, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                    { "airframe": dcs.planes.A_10A, "count": 2, "parking": [22], "fuel": 1, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                    { "airframe": dcs.planes.P_51D_30_NA, "count": 1, "parking": [21], "fuel": 1, "loadout": "Empty", "livery": "Ukraine Modern" },
                    { "airframe": dcs.planes.AJS37, "count": 1, "parking": [20], "fuel": 1, "loadout": "Empty", "livery": "SF-37 Akktu Stakki - F21" },
                    { "airframe": dcs.planes.C_101CC, "count": 1, "parking": [43], "fuel": 1, "loadout": "Empty", "livery": "usaf agressor fictional" },
                    { "airframe": dcs.planes.L_39ZA, "count": 1, "parking": [44], "fuel": 1, "loadout": "Empty", "livery": "algerian af tiger nl-36" },
                    { "airframe": dcs.planes.F_5E_3, "count": 2, "parking": [45, 46], "fuel": 1, "loadout": "Empty", "livery": "BR FAB 4846" },
                    { "airframe": dcs.planes.Su_25, "count": 2, "parking": [41, 42], "fuel": 1, "loadout": "Empty", "livery": "petal camo scheme #1 (native). 299th brigade" },
                    { "airframe": dcs.planes.Su_25T, "count": 2, "parking": [33, 40], "fuel": 1, "loadout": "Empty", "livery": "Algerian AF Desert KU-03" },
                    { "airframe": dcs.planes.M_2000C, "count": 1, "parking": [30], "fuel": 1, "loadout": "Empty", "livery": "2003 Tigermeet" },
                    { "airframe": dcs.planes.MiG_21Bis, "count": 2, "parking": [38, 29], "fuel": 1, "loadout": "Empty", "livery": "HuAF 31st AB (Turul Sqn)" },
                    { "airframe": dcs.planes.MiG_19P, "count": 2, "parking": [31, 32], "fuel": 1, "loadout": "Empty", "livery": "DDR - Fictional" },
                    { "airframe": dcs.planes.Mirage_F1CE, "count": 1, "parking": [39], "fuel": 1, "loadout": "Empty", "livery": "USA AGGRESSOR Colour (CE)" },
                    { "airframe": dcs.planes.F_86F_Sabre, "count": 1, "parking": [27], "fuel": 1, "loadout": "Empty", "livery": "Royal Saudi Air Force" },
                    { "airframe": dcs.planes.MB_339A, "count": 2, "parking": [2, 3], "fuel": 1, "loadout": "Empty", "livery": "MB339AN 'NIGERIA'" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Pissouri",
                "farp_zone": "FARP-1",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading":135,"x":-25647.644121734,"y":-292288.6812443}, {"heading":141,"x":-25630.586474933,"y":-292263.78100127}, {"heading":162,"x":-25620.195034927,"y":-292230.8420971}, {"heading":182,"x":-25618.626515681,"y":-292202.02055595} ]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading":116,"x":-25670.332684407,"y":-292305.81681553},{"heading":119,"x":-25699.525772331,"y":-292316.29793918},{"heading":106,"x":-25730.009206237,"y":-292323.52732528},{"heading":72,"x":-25764.409685157,"y":-292321.03195375}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading": 247, "x": -25691.324009923, "y": -292091.02223221}, {"heading": 255, "x": -25707.30130795, "y": -292084.98356839}, {"heading": 251, "x": -25724.788271932, "y": -292083.34809694}, {"heading": 257, "x": -25744.829904119, "y": -292083.59970793}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading":63,"x":-25792.124350791,"y":-292313.07171858},{"heading":45,"x":-25816.436192186,"y":-292297.26113392},{"heading":40,"x":-25839.572057985,"y":-292276.1919098},{"heading":30,"x":-25854.884727125,"y":-292247.93895688}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [ {"heading":225,"x":-25640.585785127,"y":-292128.6922812} ]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading":234,"x":-25656.663107399,"y":-292113.39921855}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50, "fuel": 0.6, "loadout": "Empty", "livery": "Russia New Year",
                        "positions": [{"heading":208,"x":-25619.60684021,"y":-292171.04230084},{"heading":212,"x":-25628.625825875,"y":-292148.49483668}]
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Pyrgos",
                "farp_zone": "FARP-2",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading":162,"x":-23079.808341465,"y":-249876.79543257},{"heading":182,"x":-23078.239822219,"y":-249847.97389142},{"heading":135,"x":-23107.257428272,"y":-249934.63457977},{"heading":141,"x":-23090.199781471,"y":-249909.73433674}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading":106,"x":-23189.622512775,"y":-249969.48066075},{"heading":72,"x":-23224.022991695,"y":-249966.98528922},{"heading":116,"x":-23129.945990945,"y":-249951.770151},{"heading":119,"x":-23159.139078869,"y":-249962.25127465}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading":251,"x":-23184.40157847,"y":-249729.30143241},{"heading":257,"x":-23204.443210657,"y":-249729.5530434},{"heading":247,"x":-23150.937316461,"y":-249736.97556768},{"heading":255,"x":-23166.914614488,"y":-249730.93690386}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading":45,"x":-23276.049498724,"y":-249943.21446939},{"heading":40,"x":-23299.185364523,"y":-249922.14524527},{"heading":30,"x":-23314.498033663,"y":-249893.89229235},{"heading":63,"x":-23251.737657329,"y":-249959.02505405}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading":225,"x":-23100.199091665,"y":-249774.64561667}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading":234,"x":-23116.276413937,"y":-249759.35255402}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50, "fuel": 0.6, "loadout": "Empty", "livery": "Russia New Year",
                        "positions": [{"heading":208,"x":-23079.220146748,"y":-249816.99563631},{"heading":212,"x":-23088.239132413,"y":-249794.44817215}]
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Stavrovouni",
                "farp_zone": "FARP-3",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading":162,"x":-3217.0771259095,"y":-224878.51487261},{"heading":182,"x":-3215.5086066635,"y":-224849.69333146},{"heading":135,"x":-3244.5262127165,"y":-224936.35401981},{"heading":141,"x":-3227.4685659155,"y":-224911.45377678}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading":116,"x":-3267.2147753895,"y":-224953.48959104},{"heading":106,"x":-3326.8912972195,"y":-224971.20010079},{"heading":119,"x":-3296.4078633135,"y":-224963.97071469},{"heading":72,"x":-3361.2917761395,"y":-224968.70472926}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading":247,"x":-3288.2061009055,"y":-224738.69500772},{"heading":255,"x":-3304.1833989325,"y":-224732.6563439},{"heading":251,"x":-3321.6703629145,"y":-224731.02087245},{"heading":257,"x":-3341.7119951015,"y":-224731.27248344}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading":40,"x":-3436.4541489675,"y":-224923.86468531},{"heading":30,"x":-3451.7668181075,"y":-224895.61173239},{"heading":63,"x":-3389.0064417735,"y":-224960.74449409},{"heading":45,"x":-3413.3182831685,"y":-224944.93390943}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading":225,"x":-3237.4678761095,"y":-224776.36505671}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading":234,"x":-3253.5451983815,"y":-224761.07199406}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50, "fuel": 0.6, "loadout": "Empty", "livery": "Russia New Year",
                        "positions": [{"heading":212,"x":-3225.5079168575,"y":-224796.16761219},{"heading":208,"x":-3216.4889311925,"y":-224818.71507635}]
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Xylofagou",
                "farp_zone": "FARP-4",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading":162,"x":-254.91884470955,"y":-185855.39919956},{"heading":135,"x":-282.36793151655,"y":-185913.23834676},{"heading":182,"x":-253.35032546355,"y":-185826.57765841},{"heading":141,"x":-265.31028471555,"y":-185888.33810373}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading":72,"x":-399.13349493955,"y":-185945.58905621},{"heading":116,"x":-305.05649418955,"y":-185930.37391799},{"heading":119,"x":-334.24958211355,"y":-185940.85504164},{"heading":106,"x":-364.73301601955,"y":-185948.08442774}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading":255,"x":-342.02511773255,"y":-185709.54067085},{"heading":257,"x":-379.55371390155,"y":-185708.15681039},{"heading":247,"x":-326.04781970555,"y":-185715.57933467},{"heading":251,"x":-359.51208171455,"y":-185707.9051994}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading":30,"x":-489.60853690755,"y":-185872.49605934},{"heading":45,"x":-451.16000196855,"y":-185921.81823638},{"heading":40,"x":-474.29586776755,"y":-185900.74901226},{"heading":63,"x":-426.84816057355,"y":-185937.62882104}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading":225,"x":-275.30959490955,"y":-185753.24938366}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading":234,"x":-291.38691718155,"y":-185737.95632101}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50, "fuel": 0.6, "loadout": "Empty", "livery": "Russia New Year",
                        "positions": [{"heading":212,"x":-263.34963565755,"y":-185773.05193914},{"heading":208,"x":-254.33064999255,"y":-185795.5994033}]
                    },
                ]
            },
        ]

        if not edit:
            airport_set[0]["airframes"].append({ "airframe": A_4E_C, "count": 2, "parking": [15, 25], "fuel": 1, "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            airport_set[1]["airframes"].append({ "airframe": A_4E_C, "count": 1, "parking": [25], "fuel": 1, "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            airport_set[2]["airframes"].append({ "airframe": A_4E_C, "count": 2, "parking": [26, 28], "fuel": 1, "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            # airport_set[0]["airframes"].append({ "airframe": Bronco_OV_10A, "count": 2, "parking": [6, 7], "fuel": 1, "loadout": "Empty", "livery": "colombian 2221" })
            # airport_set[0]["airframes"].append({ "airframe": Hercules, "count": 2, "parking": [40, 41], "fuel": 0.6, "loadout": "Empty" })

        return airport_set

class CyprusInvasionRedAirwings(calvinball.redairwing.RedAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_airwings = {
            "1st Goon Wing - Larnaca": {
                "airbase": "Larnaca",
                "warehouse": "Larnaca Airwing Warehouse#00001",
                "squadrons": {
                    "1GW-Larnaca-1": {
                        "airframe": dcs.planes.C_101CC,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Royal jordanian Air Force",
                        "loadouts": {
                            "2*AIM-9M, 2*LAU 68, 2*MK-82, DEFA 553 CANNON": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "2*AIM-9P, 2*BELOUGA, DEFA 553 CANNON": "{ AUFTRAG.Type.BOMBCARPET }",
                            "2*R550 Magic, DEFA 553 CANNON (I)": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "1GW-Larnaca-2": {
                        "airframe": dcs.planes.F_86F_Sabre,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Royal Saudi Air Force",
                        "loadouts": {
                            "HVAR*16": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "M117*2": "{ AUFTRAG.Type.BOMBCARPET }",
                            "GAR-8*2": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "1GW-Larnaca-3": {
                        "airframe": dcs.planes.L_39ZA,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Splinter camo desert",
                        "loadouts": {
                            "S-5KOx64": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "OFAB-100 Jupiter x8": "{ AUFTRAG.Type.BOMBCARPET }",
                            "R-60Mx2, PK-3x2": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "1GW-Larnaca-4": {
                        "airframe": dcs.helicopters.Mi_24P,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Russian Air Force",
                        "loadouts": {
                            # this is a custom one to strip the agtms off 
                            "GoonsSuck": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                        }
                    },
                    "1GW-Larnaca-5": {
                        "airframe": dcs.helicopters.Mi_8MT,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "4 x B8 + 2GUV_AP-30 (GrL 30mm)": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "6 x FAB-100": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50
                        }
                    },
                    "1GW-Larnaca-6": {
                        "airframe": dcs.planes.MiG_15bis,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "USSR_Red",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "1GW-Larnaca-7": {
                        "airframe": dcs.planes.MiG_19P,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "IAP",
                        "loadouts": {
                            "FAB-250 x 2, ORO-57K x 2": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET }",
                            "K-13A x 2": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "1GW-Larnaca-8": {
                        "airframe": dcs.planes.MB_339A,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "MB339AN 'NIGERIA'",
                        "loadouts": {
                            "A - 2*500L TipTanks + 4*Mk.82HD + 2*LR-25 (API Rockets)": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "Anti - Light Armoured Vehicle (36*BAT-120 ABL)": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50
                        }
                    }
                }
            },
            "2nd Goon Wing - Paphos": {
                "airbase": "Paphos",
                "warehouse": "Paphos Airwing Warehouse#00001",
                "squadrons": {
                    "2GW-Paphos-1": {
                        "airframe": dcs.planes.C_101CC,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Royal jordanian Air Force",
                        "loadouts": {
                            "2*AIM-9M, 2*LAU 68, 2*MK-82, DEFA 553 CANNON": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "2*AIM-9P, 2*BELOUGA, DEFA 553 CANNON": "{ AUFTRAG.Type.BOMBCARPET }",
                            "2*R550 Magic, DEFA 553 CANNON (I)": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "2GW-Paphos-2": {
                        "airframe": dcs.planes.F_86F_Sabre,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Royal Saudi Air Force",
                        "loadouts": {
                            "HVAR*16": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "M117*2": "{ AUFTRAG.Type.BOMBCARPET }",
                            "GAR-8*2": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "2GW-Paphos-3": {
                        "airframe": dcs.planes.L_39ZA,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Splinter camo desert",
                        "loadouts": {
                            "S-5KOx64": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "OFAB-100 Jupiter x8": "{ AUFTRAG.Type.BOMBCARPET }",
                            "R-60Mx2, PK-3x2": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "2GW-Paphos-4": {
                        "airframe": dcs.helicopters.Mi_24P,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Russian Air Force",
                        "loadouts": {
                            # this is a custom one to strip the agtms off 
                            "GoonsSuck": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50
                        }
                    },
                    "2GW-Paphos-5": {
                        "airframe": dcs.helicopters.Mi_8MT,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "4 x B8 + 2GUV_AP-30 (GrL 30mm)": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "6 x FAB-100": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50
                        }
                    },
                    "2GW-Paphos-6": {
                        "airframe": dcs.planes.MiG_15bis,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "USSR_Red",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "2GW-Paphos-7": {
                        "airframe": dcs.planes.MiG_19P,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "IAP",
                        "loadouts": {
                            "FAB-250 x 2, ORO-57K x 2": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET }",
                            "K-13A x 2": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "2GW-Paphos-8": {
                        "airframe": dcs.planes.MB_339A,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "MB339AN 'NIGERIA'",
                        "loadouts": {
                            "A - 2*500L TipTanks + 4*Mk.82HD + 2*LR-25 (API Rockets)": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "Anti - Light Armoured Vehicle (36*BAT-120 ABL)": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50
                        }
                    }
                }
            },
            "3rd Goon Wing - Gecitkale": {
                "airbase": "Gecitkale",
                "warehouse": "Gecitkale Airwing Warehouse#00001",
                "squadrons": {
                    "3GW-Gecitkale-1": {
                        "airframe": dcs.planes.Tu_22M3,
                        "groupSize": 1,
                        "initialInventory": 0,
                        "livery": "af standard",
                        "loadouts": {
                            "FAB-250*33": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.BOMBCARPET": 100
                        }
                    }
                }
            },
            "4th Goon Wing - Ercan": {
                "airbase": "Ercan",
                "warehouse": "Ercan Airwing Warehouse#00001",
                "squadrons": {
                    "4GW-Ercan-1": {
                        "airframe": dcs.planes.C_101CC,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Royal jordanian Air Force",
                        "loadouts": {
                            "2*AIM-9M, 2*LAU 68, 2*MK-82, DEFA 553 CANNON": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "2*AIM-9P, 2*BELOUGA, DEFA 553 CANNON": "{ AUFTRAG.Type.BOMBCARPET }",
                            "2*R550 Magic, DEFA 553 CANNON (I)": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "4GW-Ercan-2": {
                        "airframe": dcs.planes.F_86F_Sabre,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Royal Saudi Air Force",
                        "loadouts": {
                            "HVAR*16": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "M117*2": "{ AUFTRAG.Type.BOMBCARPET }",
                            "GAR-8*2": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "4GW-Ercan-3": {
                        "airframe": dcs.planes.L_39ZA,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Splinter camo desert",
                        "loadouts": {
                            "S-5KOx64": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "OFAB-100 Jupiter x8": "{ AUFTRAG.Type.BOMBCARPET }",
                            "R-60Mx2, PK-3x2": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "4GW-Ercan-4": {
                        "airframe": dcs.helicopters.Mi_24P,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Russian Air Force",
                        "loadouts": {
                            # this is a custom one to strip the agtms off 
                            "GoonsSuck": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50
                        }
                    },
                    "4GW-Ercan-5": {
                        "airframe": dcs.helicopters.Mi_8MT,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "4 x B8 + 2GUV_AP-30 (GrL 30mm)": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "6 x FAB-100": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50
                        }
                    },
                    "4GW-Ercan-6": {
                        "airframe": dcs.planes.MiG_15bis,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "USSR_Red",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "4GW-Ercan-7": {
                        "airframe": dcs.planes.MiG_19P,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "IAP",
                        "loadouts": {
                            "FAB-250 x 2, ORO-57K x 2": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET }",
                            "K-13A x 2": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "4GW-Ercan-8": {
                        "airframe": dcs.planes.MB_339A,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "MB339AN 'NIGERIA'",
                        "loadouts": {
                            "A - 2*500L TipTanks + 4*Mk.82HD + 2*LR-25 (API Rockets)": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS }",
                            "Anti - Light Armoured Vehicle (36*BAT-120 ABL)": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50
                        }
                    }
                }
            },
        }
        return red_airwings

class CyprusInvasionBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_airwings = {
            "1st - Akrotiri": {
                "airbase": "Akrotiri",
                "warehouse": "Akrotiri Airwing Warehouse#00001",
                "squadrons": {
                    "GGD-01": {
                        "airframe": dcs.planes.E_2C,
                        "groupSize": 1,
                        "initialInventory": 1,
                        "livery": "VAW-125 Tigertails",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.AWACS }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.AWACS": 50
                        }
                    }
                }
            }
        }
            "2nd - Akrotiri": {
                "airbase": "Akrotiri",
                "warehouse": "Akrotiri Airwing Warehouse#00001",
                "squadrons": {
                    "GGD-02": {
                        "airframe": dcs.planes.MQ_9_Reaper,
                        "groupSize": 1,
                        "initialInventory": 1,
                        "livery": "MQ-9 REAPER",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.FACA }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.FACA": 50
                        }
                    }
                }
            }
        }
        return blue_airwings