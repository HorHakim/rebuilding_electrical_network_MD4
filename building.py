class Building:
	def __init__(self, building_id, nb_houses, list_infras):
		self.building_id = building_id
		self.nb_houses = nb_houses
		self.list_infras = list_infras


	def get_building_metric(self):
		return sum(self.list_infras)


	def get_building_cost(self):
		building_cost = 0
		for infra_object in self.list_infras:
			building_cost += infra_object.get_reparation_cost()

		return building_cost


	def repair_all_infras(self):
		for infra in self.list_infras:
			infra.repair_infra()


	def __lt__(self, other_building):
		return self.get_building_metric() < other_building.get_building_metric()