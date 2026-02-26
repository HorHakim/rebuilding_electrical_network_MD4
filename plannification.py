import pandas
from infra import Infra
from building import Building

from config import COST_PER_PHASE


def generate_building_to_repair_list(network_to_repair_df):

	infra_dict = {}
	for infra_id, infra_df in network_to_repair_df.groupby("infra_id"):

		infra_state = "a_remplacer"
		infra_length = infra_df["longueur"].values[0]
		infra_type = infra_df["type_infra"].values[0]
		nb_houses = infra_df["nb_maisons"].sum()

		infra_dict[infra_id] = Infra(infra_id, infra_state, infra_length, infra_type, nb_houses)

	building_to_repair_list = []
	for building_id, building_df in network_to_repair_df.groupby("id_batiment"):

		nb_houses = building_df["nb_maisons"].values[0]
		list_infras = [infra_dict[infra_id] for infra_id in building_df["infra_id"].values]
		
		bulding_object = Building(building_id, nb_houses, list_infras)
		
		building_to_repair_list.append(bulding_object)

	return building_to_repair_list


def classify_buildings(building_to_repair_list, total_cost):

	buildings_per_phase = {
		1 : [],
		2 : [],
		3 : [],
		4 : []
	}

	current_phase = 1
	cost_of_current_phase = 0

	while building_to_repair_list:
		current_building = min(building_to_repair_list) 

		cost_of_current_phase += current_building.get_building_cost()

		current_building.repair_all_infras()

		buildings_per_phase[current_phase].append(current_building) 

		if cost_of_current_phase > COST_PER_PHASE[current_phase] * total_cost:
			current_phase += 1
			cost_of_current_phase = 0
		
		building_to_repair_list.pop(building_to_repair_list.index(current_building))

	return buildings_per_phase



def export_plannification_results(buildings_per_phase):

	list_of_buildings_ids = []
	list_of_phases = []

	for phase, list_of_buildings_objects in buildings_per_phase.items():
		nb_houses = 0
		for building_object in list_of_buildings_objects:
			list_of_buildings_ids.append(building_object.building_id)
			list_of_phases.append(phase)
			nb_houses += building_object.nb_houses
		print(f"le nombre de batiment de la phase {phase} : {nb_houses}")

	pandas.DataFrame({"building_id" : list_of_buildings_ids, "phase": list_of_phases}).to_excel("buildings_phases.xlsx", index=False)


def run_plannification_algo(network_to_repair_df, total_cost):

	building_to_repair_list = generate_building_to_repair_list(network_to_repair_df)
	buildings_per_phase = classify_buildings(building_to_repair_list, total_cost)
	export_plannification_results(buildings_per_phase)