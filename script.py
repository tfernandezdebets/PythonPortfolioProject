import csv

#functions
def store_parameter(dataset, name, variable_type = str): #takes a dictionary and a string as parameters
 parameter = []
 for row in dataset:
  if variable_type == int:
   parameter.append(int(row[name]))
  elif variable_type == float:
   parameter.append(float(row[name]))
  else:
   parameter.append(row[name])
 return parameter

def calculate_average(lst):
 total = 0
 for item in lst:
  if not isinstance(item, int) and not isinstance(item, float):
   print("There are non-integer/non-float values in this list. The function was interrupted and nothing has been returned")
   return
  total += item
 return total / len(lst)

def proportion_of_regions(lst):
 regions_dictionary = {}
 for item in lst:
  if item in regions_dictionary:
   regions_dictionary[item] += 1
  else:
   regions_dictionary[item] = 1
 print("\nThere are {number} regions in this dataset.".format(number = len(regions_dictionary)))
 for region, number in regions_dictionary.items():
  print("There are {number} individuals from {region}, which represents {percentage:.2f}%.".format(number = number, region = region, percentage = 100 * number/len(lst)))
 return regions_dictionary

def average_cost_smoker(smoker_lst, cost_lst):
 total_cost_smokers = 0
 total_number_smokers = 0
 total_cost_non_smokers = 0
 total_number_non_smokers = 0

 for smoker, charge in list(zip(smoker_lst, cost_lst)):
  if smoker == 'yes':
   total_cost_smokers += charge
   total_number_smokers += 1
  elif smoker == 'no':
   total_cost_non_smokers += charge
   total_number_non_smokers += 1
  else:
   print("An input other than \"yes\" or \"no\" was entered")

 print('\n')
 print("""There are {x} smokers and {y} non-smokers in this dataset.\nThe average insurance cost\
 for smokers is ${cost_smokers:.2f} and that of non-smokers is ${cost_non_smokers:.2f}.""".format(x = total_number_smokers, y = total_number_non_smokers, cost_smokers = total_cost_smokers / total_number_smokers, cost_non_smokers = total_cost_non_smokers / total_number_non_smokers))
 print("On average, smokers pay {percentage:.2f}% more than non-smokers in this dataset.".format(percentage = 100* total_cost_smokers * total_number_non_smokers / total_number_smokers / total_cost_non_smokers))

 return total_cost_smokers / total_number_smokers, total_cost_non_smokers / total_number_non_smokers

def average_age_parents(list_age, list_children):
 total_age_parents = 0
 total_number_parents = 0
 for children, age in list(zip(list_children, list_age)):
  if children > 0:
   total_age_parents += age
   total_number_parents += 1
 return total_number_parents, total_age_parents / total_number_parents

def average_cost_bmi(list_bmi, list_cost): #underweight, healthy and overweight categories are defined according to WHO guidance
 total_cost_obese = 0
 number_obese = 0
 total_cost_overweight = 0
 number_overweight = 0
 total_cost_healthy = 0
 number_healthy = 0
 total_cost_underweight = 0
 number_underweight = 0

 for bmi, insurance in list(zip(list_bmi, list_cost)):
  if bmi >= 30:
   total_cost_obese += insurance
   number_obese += 1
  elif bmi >= 25.0:
   total_cost_overweight += insurance
   number_overweight += 1
  elif bmi >= 18.5:
   total_cost_healthy += insurance
   number_healthy += 1
  else:
   total_cost_underweight += insurance
   number_underweight += 1

 print("""\nAccording to the WHO, individuals are:
 - \'underweight\' if their bmi is less than 18.5
 - \'healthy\' if their bmi is between 18.5 and 25.0
 - \'overweight\' if their bmi is greater than 25.0
 - \'obese\' if their bmi is greater than 30.0

In this dataset, {num1} individuals are underweight, {num2} healthy, {num3} overweight and {num4} are obese.
Here is the average insurance cost for each of these:
 - underweight: ${average1:.2f}
 - healthy: ${average2:.2f}
 - overweight: ${average3:.2f}
 - obese: ${average4:.2f}

On average, overweight individuals pay {percentage1:.2f}% more than healthy individuals.
On average, obese individuals pay {percentage2:.2f}% more than healthy individuals.""".format(num1 = number_underweight, num2 = number_healthy, num3 = number_overweight, num4 = number_obese, average1 = total_cost_underweight / number_underweight, average2 = total_cost_healthy / number_healthy, average3 = total_cost_overweight / number_overweight, average4 = total_cost_obese / number_obese, percentage1 = 100 * total_cost_overweight * number_healthy / total_cost_healthy / number_overweight, percentage2 = 100 * total_cost_obese * number_healthy / total_cost_healthy / number_obese))
 return number_underweight, total_cost_underweight, number_healthy, total_cost_healthy, number_overweight, total_cost_overweight, number_obese, total_cost_obese


#main body of script
insurance_dataset = []

with open('insurance.csv', newline='') as insurance_csv:
 insurance_file = csv.DictReader(insurance_csv)
 for row in insurance_file:
  insurance_dataset.append(row)

parameters_evaluated = [key for key, value in insurance_dataset[0].items()]

##let's store each parameter in its own list
age = store_parameter(insurance_dataset, 'age', int)
sex = store_parameter(insurance_dataset, 'sex')
bmi = store_parameter(insurance_dataset, 'bmi', float)
children = store_parameter(insurance_dataset, 'children', int)
smoker = store_parameter(insurance_dataset, 'smoker')
region = store_parameter(insurance_dataset, 'region')
charges = store_parameter(insurance_dataset, 'charges', float)

print("""There are {} individuals in this dataset. Their {}, {}, {}, number of {}, whether they are\
 {}s or not, {} of origin and incurred insurance {} are collected.""".format(len(age), parameters_evaluated[0], parameters_evaluated[1], parameters_evaluated[2], parameters_evaluated[3], parameters_evaluated[4], parameters_evaluated[5], parameters_evaluated[6]))
if len(parameters_evaluated) > 7: #this currently needs to be updated manually, as does the sentence above
 print("More parameters have been evaluated in this dataset since you last checked!")

print("\nThe average {parameter} is {value:.2f} years old.".format(parameter = 'age', value = calculate_average(age)))
print("The average {parameter} is {value:.2f}.".format(parameter = 'bmi', value = calculate_average(bmi)))
print("Average insurance {parameter} amount to ${value:.2f}.".format(parameter = 'charges', value = calculate_average(charges)))
proportion_of_regions(region)
average_cost_smoker(smoker, charges)

print("\nThere are {number} parents in this dataset. On average, they are {age:.1f} years old.".format(number = average_age_parents(age, children)[0], age = average_age_parents(age, children)[1]))
average_cost_bmi(bmi, charges)
