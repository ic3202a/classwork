class delivery_personnel:
	#constructor
	def __init__(self, years_of_services, company, is_drone, zip_codes_covered, name = None):
		self.years_of_services = years_of_services
		self.company = company
		self.is_drone = is_drone
		self.zip_codes_covered = zip_codes_covered
		self.name = name

	#getters and setters
	def get_years_of_services (self):
		return(self.years_of_services)

	def set_years_of_services (self, y):
		self.years_of_services = y

	def get_company (self):
		return(self.company)

	def set_company (self, c):
		self.company = c

	def get_zip_codes_covered (self):
		return(self.zip_codes_covered)

	def set_zip_codes_covered(self, z):
		self.zip_codes_covered = z

	#deliver method
	def deliver (self, years_of_services, input_list):
		zip_codes_left = [i for i in input_list if i != zip_codes_covered]
		return[zip_codes_left]

def main():

	delivery_1 = delivery_personnel(years_of_services = 4, company = "FedEx", is_drone = False, zip_codes_covered = 90210, name = "Tom")

	# print(delivery_1.get_years_of_services())
	# print(delivery_1.get_company())
	# print(delivery_1.get_zip_codes_covered())
	zip_code_1 = [42039, 61729, 90210]
	print(deliver(zip_code_1))



if __name__ == '__main__':
	main()