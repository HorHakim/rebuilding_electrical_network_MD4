import pandas
from config import *


def prepare_data(network_df, building_df, infra_df):

	network_to_repair_df = network_df[network_df["infra_type"] == "a_remplacer"]
	network_to_repair_df  = pandas.merge(network_to_repair_df, infra_df, left_on="infra_id", right_on="id_infra")
	network_to_repair_df.drop(columns=["nb_maisons", "id_infra", "infra_type"], inplace=True)
	network_to_repair_df  = pandas.merge(network_to_repair_df, building_df, on="id_batiment")

	return network_to_repair_df



def compute_rebuilding_costs(network_to_repair_df):
	infra_to_repair_df = network_to_repair_df[["infra_id", "longueur", "type_infra"]]
	infra_to_repair_df = infra_to_repair_df.drop_duplicates("infra_id")

	total_cost = 0

	for _, row in infra_to_repair_df.iterrows():
		if row["type_infra"] == "aerien":
			total_cost += row["longueur"] * AERIAL_COST_PER_METER
		
		elif row["type_infra"] == "semi-aerien":
			total_cost += row["longueur"] * SEMI_AERIAL_COST_PER_METER
		
		elif row["type_infra"] == "fourreau":
			total_cost += row["longueur"] * DUCT_COST_PER_METER

		else:
			print(f"Warning this row isn't manage by the program : \n{row}")

	return total_cost



if __name__ == "__main__":
	network_df = pandas.read_excel("./data/reseau_en_arbre.xlsx")
	building_df = pandas.read_csv("./data/batiments.csv")
	infra_df = pandas.read_csv("./data/infra.csv")

	network_to_repair_df = prepare_data(network_df, building_df, infra_df)

	print("Le réseau que l'on doit réparer :")
	print(network_to_repair_df)

	total_cost = compute_rebuilding_costs(network_to_repair_df)
	print(f"Le coût total des réparations est de : {total_cost}")
