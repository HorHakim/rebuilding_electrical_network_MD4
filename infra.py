from config import *

class Infra:
	def __init__(self, infra_id, infra_state, infra_length, infra_type, nb_houses):
		self.infra_id = infra_id
		self.infra_state = infra_state
		self.infra_length = infra_length
		self.infra_type = infra_type
		self.nb_houses = nb_houses
		
		if infra_type == "aerien":
			self.infra_cost = infra_length * AERIAL_COST_PER_METER
			self.infra_duration = infra_length * AERIAL_DURATION_PER_METER / 4
			self.infra_reparation_cost = infra_length * AERIAL_COST_PER_METER
		
		elif infra_type == "semi-aerien":
			self.infra_cost = infra_length * SEMI_AERIAL_COST_PER_METER
			self.infra_duration = infra_length * SEMI_AERIAL_DURATION_PER_METER / 4
			self.infra_reparation_cost = infra_length * SEMI_AERIAL_COST_PER_METER
		
		elif infra_type == "fourreau":
			self.infra_cost = infra_length * DUCT_COST_PER_METER
			self.infra_duration = infra_length * DUCT_DURATION_PER_METER / 4
			self.infra_reparation_cost = infra_length * DUCT_COST_PER_METER


	def repair_infra(self):
		self.infra_state = "infra_intacte"


	def get_reparation_cost(self):
		if self.infra_state == "infra_intacte":
			return 0
		elif self.infra_state == "a_remplacer":
			return self.infra_reparation_cost



	def __radd__(self, other_object):
		if self.infra_state == "infra_intacte":
			return 0 + other_object
		
		elif self.infra_state == "a_remplacer":
			return (self.infra_reparation_cost * self.infra_duration / self.nb_houses) + other_object


	def __repr__(self):
		return f"infra_object : {self.infra_id}"