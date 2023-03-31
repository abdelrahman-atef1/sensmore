import random 
company_rooms = ["office", "kitchen", "manager office",
                 "room 1", "room 2", "room 3", "room 4",
                 "bathroom 1", "pathroom 2"]

company_employees = {}



import requests
import json

url = 'https://neat-windows-float-102-185-45-85.loca.lt/data'
data = json.dumps({'employee_id': '12345', 'room_id': '67890'})
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=data, headers=headers)

if response.status_code == 200:
    print('Data sent successfully')
else:
    print('Error sending data:', response.text)
    
    
import random

# Define the list of possible departments
departments = ["HR", "IT", "Marketing", "Sales", "Finance"]

# Define the list of possible room numbers
room_numbers = [100, 200, 300, 400, 500]

# Define a function to generate a unique ID for each employee
def generate_employee_id(employee_num):
    return f"EMP{employee_num:02d}"

# Define a function to generate a random department ID
def generate_department_id():
    return random.choice(departments)

# Define a function to generate a random room ID
def generate_room_id():
    return f"R{random.choice(room_numbers):03d}"

# Generate 10 random employees with unique IDs, main room IDs, and department IDs
employees = []
for i in range(1, 11):
    employee_id = generate_employee_id(i)
    department_id = generate_department_id()
    room_id = generate_room_id()
    employees.append({
        "employee_id": employee_id,
        "main_room_id": room_id,
        "department_id": department_id
    })

# Print the list of employees
print(employees)