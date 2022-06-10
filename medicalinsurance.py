names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

#Additional data
names.append("Priscilla")
insurance_costs.append(8320.0)

#Creating one list with itens from both variables names and insurance_costs
medical_records = zip(insurance_costs, names)
medical_records_list=list(medical_records)
print(medical_records_list)

#Checking how many itens on the list
num_medical_records = len(medical_records_list)
print('There are '+str(num_medical_records) + '  medical records.')

#Checking the first medical record on the list
first_medical_record = medical_records_list[0]
print('Here is the first medical record: ' + str(first_medical_record))

#Sortind by insurance cost
medical_records_list.sort()
print('Here are the medical records sorted by insurance cost: ' + str(medical_records_list))

cheapest_three = medical_records_list[0:3]
print('Here are the three cheapest insurance costs in our medical records: ' + str(cheapest_three))

priciest_three = medical_records_list[-3:]
print('Here are the three most expensive insurance costs in our medical records' + str(priciest_three))

#Checking how many Paul there are in the records
ocurrences_paul= names.count("Paul")
print('There are ' + str(ocurrences_paul) + ' individuals with the name Paul in our medical records')

#Sorting medical records alphabetically ny name
medical_records = zip(names, insurance_costs)
medical_records_list_alpha=list(medical_records)
print(medical_records_list_alpha)
medical_records_list_alpha.sort()
print('Here are the medical records sorted by name ' + str(medical_records_list_alpha))
print('B')
