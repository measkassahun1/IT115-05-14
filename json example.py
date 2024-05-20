#Impoting the json library
import json

data = {

    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Golf','Running','Football','Traveling'],
    'is_student': False
}

#Creating a json object and writing the python object contents to the json
with open('data.json','w') as json_file:
#Dumps to the json file 
    json.dump(data,json_file,indent=4)

print("Data has been written to data.json")

#Reading the json object and printing the output to the terminal
with open('data.json','r') as json_file:

    #Creating a variable to hold the json file contents
    loaded_data = json.load(json_file)

    #loading data to file
print("Successfully able to read data.json")
print(loaded_data)

#Adding to the json object
loaded_data['age'] = 34
loaded_data['interests'].append('History')

#write the changes to the json file

with open('data.json','w') as json_file:

    json.dump(loaded_data,json_file,indent=4)

print("Data has been re-written to data.json")
