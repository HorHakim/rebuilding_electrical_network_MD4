class Building:
	def __init__(self, id_building, nb_houses, list_infras):
		self.id_building = id_building
		self.nb_houses = nb_houses
		self.list_infras = list_infras


	def get_building_metric(self):
		return sum(self.list_infras)


	def repair_all_infras(self):
		for infra in self.list_infras:
			infra.repair()


	def __lt__(self, other_building):
		return self.get_building_metric() < other_building.get_building_metric()




'''
PSEUDO ALGO:

list_buildings = [building_1, building_2, ........, building_n]
sorted_list_buildings = []

WHILE list_buildings:
	prioritary_building = min(list_buildings) # reccup le building le plus prio
	
	prioritary_building.repaire_all_infra() # considère que toutes ses infras sont réparée
	
	sorted_list_buildings.append(prioritary_building) # rajoute dans la liste trié

	list_buildings.pop(list_buildings.index(prioritary_building)) # ça l'enlève de la liste de référence.

'''