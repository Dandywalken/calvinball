import dcs
import pydcs_extensions

class Ctld:
    def build(self, m: dcs.Mission):
        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD Inf M4 8", [
            dcs.vehicles.Infantry.CH_USInfantry_M4,
            dcs.vehicles.Infantry.CH_USInfantry_M4,
            dcs.vehicles.Infantry.CH_USInfantry_M4,
            dcs.vehicles.Infantry.CH_USInfantry_M4,
            dcs.vehicles.Infantry.CH_USInfantry_FIM92,
            dcs.vehicles.Infantry.CH_USInfantry_M240,
            dcs.vehicles.Infantry.CH_USInfantry_FGM148,
            dcs.vehicles.Infantry.CH_USInfantry_M136
        ], dcs.mapping.Point(180657, -39472, m.terrain)).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD Infantry AA", [
            dcs.vehicles.Infantry.CH_USInfantry_FIM92,
            dcs.vehicles.Infantry.CH_USInfantry_FIM92,
            dcs.vehicles.Infantry.CH_USInfantry_FIM92,
            dcs.vehicles.Infantry.CH_USInfantry_M4,
            dcs.vehicles.Infantry.CH_USInfantry_M4
        ], dcs.mapping.Point(180657, -39472, m.terrain)).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD Infantry AT", [
            dcs.vehicles.Infantry.CH_USInfantry_M136,
            dcs.vehicles.Infantry.CH_USInfantry_M136,
            dcs.vehicles.Infantry.CH_USInfantry_M136,
            dcs.vehicles.Infantry.CH_USInfantry_M136,
            dcs.vehicles.Infantry.CH_USInfantry_FGM148,
            dcs.vehicles.Infantry.CH_USInfantry_M4,
            dcs.vehicles.Infantry.CH_USInfantry_M4
        ], dcs.mapping.Point(180657, -39472, m.terrain)).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD AT SK Special 2", [
            dcs.vehicles.Infantry.CH_USInfantry_FGM148,
            dcs.vehicles.Infantry.CH_USInfantry_FGM148
        ], dcs.mapping.Point(180657, -39472, m.terrain)).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD AA SK Special 2", [
            dcs.vehicles.Infantry.CH_USInfantry_FIM92,,
            dcs.vehicles.Infantry.CH_USInfantry_FIM92
        ], dcs.mapping.Point(180657, -39472, m.terrain)).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD MORTAR", [
            dcs.vehicles.Artillery.x_2B11_mortar,
        ], dcs.mapping.Point(180657, -39472, m.terrain)).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD HAWK", [
            dcs.vehicles.AirDefence.Hawk_sr,
            dcs.vehicles.AirDefence.Hawk_tr,
            dcs.vehicles.AirDefence.Hawk_pcp,
            dcs.vehicles.AirDefence.Hawk_cwar,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
        ], dcs.mapping.Point(180657, -39472, m.terrain), formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD NASAM", [
            dcs.vehicles.AirDefence.NASAMS_Command_Post,
            dcs.vehicles.AirDefence.NASAMS_Radar_MPQ64F1,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
        ], dcs.mapping.Point(180657, -39472, m.terrain), formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD BLUE RECCE JTAC", dcs.vehicles.Infantry.Soldier_M4, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD BLUE RECCE JTAC HMMWV", dcs.vehicles.Unarmed.Hummer, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD HMMWV MG", dcs.vehicles.Armor.M1043_HMMWV_Armament, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD HMMWV TOW", dcs.vehicles.Armor.M1045_HMMWV_TOW, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD AVENGER", dcs.vehicles.AirDefence.M1097_Avenger, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD M818", dcs.vehicles.Unarmed.M_818, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD M60", dcs.vehicles.Armor.M_60, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD STRYKER MGS", dcs.vehicles.Armor.M1128_Stryker_MGS, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD STRYKER ICV", dcs.vehicles.Armor.M1126_Stryker_ICV, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD MLRS", dcs.vehicles.Artillery.MLRS, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "CTLD M-109", dcs.vehicles.Artillery.M_109, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation = True

        # CSAR required group
        m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Downed Pilot", dcs.vehicles.Infantry.Soldier_M4, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1).late_activation = True

        # Herc required groups/names
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "2S6 Tunguska", dcs.vehicles.AirDefence.x_2S6_Tunguska, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BMD-1", dcs.vehicles.Armor.BMD_1, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BMP-1", dcs.vehicles.Armor.BMP_1, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BMP-2", dcs.vehicles.Armor.BMP_2, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BMP-3", dcs.vehicles.Armor.BMP_3, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BRDM-2", dcs.vehicles.Armor.BRDM_2, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BTR_D", dcs.vehicles.Armor.BTR_D, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BTR-80", dcs.vehicles.Armor.BTR_80, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BTR-80", dcs.vehicles.Armor.BTR_80, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BTR-82A", dcs.vehicles.Armor.BTR_82A, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Cobra", dcs.vehicles.Armor.Cobra, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Dog Ear radar", dcs.vehicles.AirDefence.Dog_Ear_radar, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Gepard", dcs.vehicles.AirDefence.Gepard, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "HEMTT TFFT", dcs.vehicles.Unarmed.HEMTT_TFFT, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Hummer", dcs.vehicles.Unarmed.Hummer, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Infantry", dcs.vehicles.Infantry.Soldier_M4, dcs.mapping.Point(180657, -39472, m.terrain), group_size=4)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "LAV-25", dcs.vehicles.Armor.LAV_25, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M 818", dcs.vehicles.Unarmed.M_818, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M-113", dcs.vehicles.Armor.M_113, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M-2 Bradley", dcs.vehicles.Armor.M_2_Bradley, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M1043 HMMWV Armament", dcs.vehicles.Armor.M1043_HMMWV_Armament, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M1045 HMMWV TOW", dcs.vehicles.Armor.M1045_HMMWV_TOW, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M1097 Avenger", dcs.vehicles.AirDefence.M1097_Avenger, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M1126 Stryker ICV", dcs.vehicles.Armor.M1126_Stryker_ICV, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M1128 Stryker MGS", dcs.vehicles.Armor.M1128_Stryker_MGS, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M1134 Stryker ATGM", dcs.vehicles.Armor.M1134_Stryker_ATGM, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M48 Chaparral", dcs.vehicles.AirDefence.M48_Chaparral, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M6 Linebacker", dcs.vehicles.AirDefence.M6_Linebacker, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "M978 HEMTT Tanker", dcs.vehicles.Unarmed.M978_HEMTT_Tanker, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Marder", dcs.vehicles.Armor.Marder, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "MCV-80", dcs.vehicles.Armor.MCV_80, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "MTLB", dcs.vehicles.Armor.MTLB, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Roland ADS", dcs.vehicles.AirDefence.Roland_ADS, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Roland Radar", dcs.vehicles.AirDefence.Roland_Radar, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "SAU 2-C9", dcs.vehicles.Artillery.SAU_2_C9, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "SAU Gvozdika", dcs.vehicles.Artillery.SAU_Gvozdika, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Strela-10M3", dcs.vehicles.AirDefence.Strela_10M3, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Tigr_233036", dcs.vehicles.Unarmed.Tigr_233036, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "TPZ", dcs.vehicles.Armor.TPZ, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "UAZ-469", dcs.vehicles.Unarmed.UAZ_469, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Ural-375", dcs.vehicles.Unarmed.Ural_375, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Vulcan", dcs.vehicles.AirDefence.Vulcan, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True
        self.__drive(m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "ZSU-23-4 Shilka", dcs.vehicles.AirDefence.ZSU_23_4_Shilka, dcs.mapping.Point(180657, -39472, m.terrain), group_size=1)).late_activation=True

    def __drive(self, vg: dcs.unitgroup.VehicleGroup):
        for u in vg.units:
            u.player_can_drive = True
        return vg