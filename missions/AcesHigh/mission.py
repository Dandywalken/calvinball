import dcs
import pydcs_extensions
import calvinball

class AcesHigh(calvinball.mission.Mission):
    def __init__(self) -> None:
        t = dcs.terrain.Normandy()
        miz_name = "AcesHigh"
        ctld = AcesHighCtld()
        clients = AcesHighClients()
        red_airwings = AcesHighRedAirwings()
        blue_airwings = AcesHighBlueAirwings()
        carriers = AcesHighCarriers()
        qrf = AcesHighQrf()
        reinforcement = AcesHighReinforcement()
        red_brigades = AcesHighRedBrigades()
        blue_brigades = AcesHighBlueBrigades()

        super().__init__(t, miz_name, ctld, clients, red_airwings, blue_airwings, carriers, qrf, reinforcement, red_brigades, blue_brigades)

        self.m.coalition["blue"].set_bullseye({"x": 57597, "y": -72593})
        self.m.coalition["red"].set_bullseye({"x": 57597, "y": -72593})

class AcesHighCtld(calvinball.ctld.Ctld):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

class AcesHighQrf(calvinball.qrf.Qrf):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

        p = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 1", [
            dcs.vehicles.Unarmed.Kubelwagen_82,
            dcs.vehicles.Unarmed.Kubelwagen_82,
            dcs.vehicles.Unarmed.Blitz_36_6700A,
            dcs.vehicles.Unarmed.Blitz_36_6700A,
            dcs.vehicles.Unarmed.Horch_901_typ_40_kfz_21,
            dcs.vehicles.Unarmed.Horch_901_typ_40_kfz_21,
            dcs.vehicles.Unarmed.Sd_Kfz_2,
            dcs.vehicles.Unarmed.Sd_Kfz_2,
            dcs.vehicles.Unarmed.Sd_Kfz_2,
            dcs.vehicles.Unarmed.Sd_Kfz_7,
            dcs.vehicles.Unarmed.Sd_Kfz_7,
            dcs.vehicles.Unarmed.Sd_Kfz_7
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 2", [
            dcs.vehicles.Armor.Pz_V_Panther_G,
            dcs.vehicles.Armor.Pz_V_Panther_G,
            dcs.vehicles.Armor.Pz_V_Panther_G,
            dcs.vehicles.Armor.Pz_V_Panther_G,
            dcs.vehicles.Unarmed.Sd_Kfz_2,
            dcs.vehicles.Unarmed.Sd_Kfz_2
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True
        

class AcesHighReinforcement(calvinball.reinforcement.Reinforcement):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

        p = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BLUE REINFORCEMENT 1", [
            dcs.vehicles.Armor.M4_Sherman,
            dcs.vehicles.Armor.M4_Sherman,
            dcs.vehicles.Armor.M4_Sherman,
            dcs.vehicles.Armor.M4_Sherman,
            dcs.vehicles.Unarmed.M30_CC,
            dcs.vehicles.Unarmed.M30_CC,
            dcs.vehicles.Unarmed.M30_CC

        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

class AcesHighCarriers(calvinball.carriers.Carriers):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.mission):
        return {}
    
class AcesHighClients(calvinball.clients.Clients):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission, edit: bool):
        m.groundControl.blue_game_masters = 1
        m.groundControl.blue_tactical_commander = 1
        m.groundControl.blue_jtac = 2
        m.groundControl.red_game_masters = 1

        airport_set = [
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Lymington"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.P_51D_30_NA, "count": 4, "parking": [55, 56, 50, 48], "fuel": 1, "loadout": "Empty", "livery": "USAF 363rd FS, 357th FG DESERT RAT" },
                    { "airframe": dcs.planes.P_47D_30, "count": 4, "parking": [49, 52, 51, 53], "fuel": 1, "loadout": "Empty", "livery": "Maj_Howard_Park_1945"},
                    { "airframe": dcs.planes.FW_190D9, "count": 4, "parking": [4, 5, 6, 7], "fuel": 1, "loadout": "Empty", "livery": "FW-190D9_GB" },
                    { "airframe": dcs.planes.FW_190A8, "count": 4, "parking": [8, 9, 12, 10], "fuel": 1, "loadout": "Empty", "livery": "FW-190A8_RAF" },
                    { "airframe": dcs.planes.Bf_109K_4, "count": 4, "parking": [11, 13, 14, 15], "fuel": 1, "loadout": "Empty", "livery": "Bf-109 K4 Irmgard" },
                    { "airframe": dcs.planes.SpitfireLFMkIXCW, "count": 4, "parking": [16, 17, 19, 18], "fuel": 1, "loadout": "Empty", "livery": "RAF, No. 145 Squadron" },
                    { "airframe": dcs.planes.I_16, "count": 4, "parking": [20, 23, 21, 22], "fuel": 1, "loadout": "Empty", "livery": "Red Army Standard" },
                    { "airframe": dcs.planes.MosquitoFBMkVI, "count": 4, "parking": [36, 37, 38, 39], "fuel": 1, "loadout": "Empty", "livery": "605 Sqn" },
                ]
            },
        ]

        comms_plan = {
            "uhf": { 1: 250, 2: 251, 3: 252, 4: 253, 5: 254 },
            "vhf_am": { 1: 135, 2: 136, 3: 137, 4: 138, 5: 139 },
            "vhf_fm": { 1: 31, 2: 32, 3: 33, 4: 34, 5: 35 },
            "vhf_am_de": { 1: 39, 2: 40, 3: 41, 4: 42 }
        }

        radio_override = {
            dcs.helicopters.Ka_50_3: { "radio": 2, "frequency": 250 },
            dcs.helicopters.SA342L: { "radio": 1, "frequency": 135 },
            dcs.helicopters.SA342M: { "radio": 1, "frequency": 135 },
        }

        radios = {
            dcs.helicopters.AH_64D_BLK_II: ["vhf_am", "uhf", "vhf_fm", "vhf_fm"],
            dcs.helicopters.Ka_50_3: ["vhf_fm"],
            dcs.helicopters.Mi_24P: ["uhf", "vhf_fm"],
            dcs.helicopters.Mi_8MT: ["uhf", "vhf_fm"],
            dcs.helicopters.SA342L: ["vhf_fm"],
            dcs.helicopters.SA342M: ["vhf_fm"],
            dcs.helicopters.UH_1H: ["uhf"],
            dcs.planes.A_10A: ["vhf_am"],
            dcs.planes.A_10C_2: ["vhf_am", "uhf", "vhf_fm"],
            dcs.planes.AJS37: ["uhf"],
            dcs.planes.AV8BNA: ["vhf_am", "uhf", "vhf_fm"],
            dcs.planes.C_101CC: ["uhf"],
            dcs.planes.F_5E_3: ["uhf"],
            dcs.planes.F_86F_Sabre: ["uhf"],
            dcs.planes.L_39ZA: ["uhf"],
            dcs.planes.M_2000C: ["uhf", "vhf_am"],
            dcs.planes.MB_339A: ["uhf"],
            dcs.planes.MiG_19P: ["vhf_am"],
            dcs.planes.MiG_21Bis: ["uhf"],
            dcs.planes.Mirage_F1EE: ["vhf_am", "uhf"],

            dcs.planes.P_51D_30_NA: ["vhf_am"],
            dcs.planes.P_47D_30: ["vhf_am"],
            dcs.planes.FW_190D9: ["vhf_am_de"],
            dcs.planes.FW_190A8: ["vhf_am_de"],
            dcs.planes.Bf_109K_4: ["vhf_am_de"],
            dcs.planes.SpitfireLFMkIX: ["vhf_am"],
            dcs.planes.SpitfireLFMkIXCW: ["vhf_am"],
            dcs.planes.I_16: ["vhf_am"],
            dcs.planes.MosquitoFBMkVI: ["vhf_am"],

            dcs.planes.Su_25: ["vhf_am"],
            dcs.planes.Su_25T: ["vhf_am"],
            dcs.planes.F_14B: ["uhf", "vhf_am"],
            dcs.planes.FA_18C_hornet: ["vhf_am", "uhf"],
            dcs.planes.F_15ESE: ["uhf", "vhf_am"],
            dcs.planes.F_16C_50: ["uhf", "vhf_am"],
            dcs.planes.JF_17: ["uhf"],
            dcs.planes.F_15C: ["uhf"],
        }

        if not edit:
            radios[pydcs_extensions.A_4E_C] = ["uhf"]

        for airport in airport_set:
            for airframe in airport["airframes"]:
                airframe["radios"] = {}
                if airframe["airframe"] in radio_override:
                    airframe["radio_override"] = radio_override[airframe["airframe"]]
                for i, template in enumerate(radios[airframe["airframe"]]):
                    airframe["radios"][i+1] = comms_plan[template]

        return airport_set

class AcesHighRedAirwings(calvinball.redairwing.RedAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_airwings = {
            "Funtington": {
                "airbase": "Funtington",
                "warehouse": "Funtington Airwing Warehouse#00001",
                "squadrons": {
                    "Funtington 1": {
                        "airframe": dcs.planes.Bf_109K_4,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Bf-109 K4 Jagdgeschwader 53",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50
                        }
                    }
                }
            },
        }
        return red_airwings

class AcesHighBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_airwings = {
            "Lymington": {
                "airbase": "Lymington",
                "warehouse": "Lymington Airwing Warehouse#00001",
                "squadrons": {
                    "G-01": {
                        "airframe": dcs.planes.SpitfireLFMkIXCW,
                        "groupSize": 2,
                        "initialInventory": 99,
                        "livery": "RAF, No. 145 Squadron",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.CAP }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50
                        }
                    }
                }
            },
        }
        return blue_airwings

class AcesHighRedBrigades(calvinball.redbrigade.RedBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_brigades = {}
        return red_brigades

class AcesHighBlueBrigades(calvinball.bluebrigade.BlueBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_brigades = {}
        return blue_brigades