class Infra:
	def __init__(self, infra_id, infra_state, infra_length, infra_type, nb_houses):
		self.infra_id = infra_id
		self.infra_state = infra_state
		self.infra_length = infra_length
		self.infra_type = infra_type
		self.nb_houses = nb_houses
		
		if infra_type == "aerien":
			self.infra_cost += infra_length * AERIAL_COST_PER_METER
			self.infra_duration = ??
		
		elif row["type_infra"] == "semi-aerien":
			self.infra_cost += infra_length * SEMI_AERIAL_COST_PER_METER
			self.infra_duration = ??
		
		elif row["type_infra"] == "fourreau":
			self.infra_cost += infra_length * DUCT_COST_PER_METER
			self.infra_duration= ??