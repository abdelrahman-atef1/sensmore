from datetime import datetime
import random
import requests
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import threading

def update_rt(data):
    response = requests.post('http://127.0.0.1:5678/update', json = data)
    print(response.ok)

cred = credentials.Certificate("D:/work/python/beacon files/sensemore.json")

default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':"https://sensemore-6c16d-default-rtdb.firebaseio.com"
	})

# Get a database reference to our blog.
ref = db.reference("/")


url = 'http://127.0.0.1:5678/data'

jops = """Marketing Department
IT Department
Out Range
Cafeteria
Manager Office
Main Hall
General Management
Finance Department
Sales Department"""
jops = jops.split("\n")



base = {
  "Employees": {
    "00001": {
      "Name": "Amed",
      "Department": "Marketing Department",
      "RoomID": 1
    },
    "00002": {
      "Name": "Yousf",
      "Department": "IT",
      "RoomID": 1
    },
    "00003": {
      "Name": "Xiave",
      "Department": "IT",
      "RoomID": 2
    },
    "00004": {
      "Name": "warda",
      "Department": "Sales Department",
      "RoomID": 2
    },
    "00005": {
      "Name": "Amed",
      "Department": "IT Department",
      "RoomID": 3
    },
    "00006": {
      "Name": "Khaled",
      "Department": "Finance Department",
      "RoomID": 3
    },
    "00007": {
      "Name": "Ashraf",
      "Department": "Manager Office",
      "RoomID": 4
    }
  },
  "Rooms": {
    "1": {
      "RoomName": "IT Department"
    },
    "2": {
      "RoomName": "General Managemnt"
    },
    "3": {
      "RoomName": "Finance Department"
    },
    "4": {
      "RoomName": "Manager Office"
    },
    "5": {
      "RoomName": "Sales Department"
    }
  },


  "Departments": {
    "1": {
      "DepartmentName": "Marketing Department",
      "Color": "blue"
    },
    "2": {
      "DepartmentName": "IT Department",
      "Color": "green"
    },
    "3": {
      "DepartmentName": "Manager Office",
      "Color": "red"
    },
    "4": {
      "DepartmentName": "Finance Department",
      "Color": "orange"
    },
    "5": {
      "DepartmentName": "Sales Department",
      "Color": "orange"
    },
    "6": {
      "DepartmentName": "General Management",
      "Color": "orange"
    },
    "7": {
      "DepartmentName": "Cafeteria",
      "Color": "orange"
    }

  }
}


## add employee to firebase
def add_new_employee(ref, id, data):

    users_data = ref.child("company_data").child(id)
    users_data.set(data)


# base["Employees"]
# for i in base["Employees"]:
#     add_new_employee(ref, i, base["Employees"][i])



def  (ref, _id, weight):
    t_step = 15
    times = 0
    movement_data = []

    while times < 60*5:
        # Choose a random room from the available rooms
        room = random.choices([1, 2, 3, 4], weights = weight)

        # Create a dictionary with the data for this movement
        movement = {
            'employee_id': _id,
            'room': room[0],
        'timestamp': str(datetime.now()).split(".")[0]
        }

        # Append the movement data to the list
        threading.Thread(target = update_rt, args = [movement]).start()

        movement_data.append(movement)

        if len(movement_data) == 12: # assuming one movement every 30 seconds
            dat = {"data": movement_data}
            response = requests.post(url, json=dat)
            movement_data = []
            print(response.json())
            print(f"uploaded data for id: {id}")


        # Wait for 30 seconds before returning
        times += t_step
        print("sleep once")
        time.sleep(t_step)


keys = list(base["Employees"].keys())

emp1 = threading.Thread(target = collect_movement, args = [ref,keys[0], [10, 2, 1 ,0]])

emp2 = threading.Thread(target = collect_movement, args = [ref,keys[1], [10, 2, 1 ,0]])

emp3 = threading.Thread(target = collect_movement, args = [ref,keys[2], [5, 8, 1 ,1]])

emp4 = threading.Thread(target = collect_movement, args = [ref,keys[3], [1,1,1,1]])

emp5 = threading.Thread(target = collect_movement, args = [ref,keys[4], [3, 2, 9 ,0]])

emp6 = threading.Thread(target = collect_movement, args = [ref,keys[5], [10, 2, 11 ,0]])

emp7 = threading.Thread(target = collect_movement, args = [ref,keys[6], [4, 2, 1 ,8]])


emp1.start()
emp2.start()
emp3.start()
emp4.start()
emp5.start()
emp6.start()
emp7.start()
