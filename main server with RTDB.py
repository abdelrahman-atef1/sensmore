from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
"""
code cotain Realtime database for internal dashboard/monetoring
in admon/manager device
just send request to get any employee data
the data stored here is not the full or read data as _this is just a demo code_

"""

## the database here is Dictionary for simple
## it contains 7 different users, the room he currently at,
## their time in each room from the available 4 room in the demo
dataBase = {"00001":{
                "times":[0, 0, 0, 0],
                "room":"1"
                        },
"00002":{
                "times":[0, 0, 0, 0],
                "room":"1"
                        },
"00003":{
                "times":[0, 0, 0, 0],
                "room":"3"
                        },
"00004":{
                "times":[0, 0, 0, 0],
                "room":"4"
                        },
"00005":{
                "times":[0, 0, 0, 0],
                "room":"1"
                        },
"00006":{
                "times":[0, 0, 0, 0],
                "room":"2"
                        },
"00007":{
                "times":[0, 0, 0, 0],
                "room":"4"
                        }
}

## init firebase credentials
cred = credentials.Certificate("D:/work/python/beacon files/sensemore.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL':"https://sensemore-6c16d-default-rtdb.firebaseio.com"
})

# Get a database reference dir.
ref = db.reference("/")


"""
the flask emo app contain 3 main methods

2 for RTDP dashboard
and one for firebase

update_data:
        this method update the data recieved form each employee beacon
        the data updated every sample time 'T' and i depend on company
        in dashboard will map the time samples into real time by mul the_
        _samples with the step period

get_employee_data:
        this method return specific employee data [his current room, time unit_
        _ in each room]

receive_data:
        this method recieve chunk data for each employee and upload it into_
        _ firebase
"""
app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_data():
    res = request.get_json()
    id_ = res.get('employee_id')
    dataBase[id_]["room"] = res.get('room')
    dataBase[id_]["times"][int(res.get('room'))-1] +=1

    # do something with the data, such as storing it in a database
    response_data = {"result":"sucess"}
    return jsonify(response_data)

@app.route('/employee/<string:employee_id>', methods=['GET'])
def get_employee_data(employee_id):
    if employee_id not in dataBase:
        return jsonify({"error": f"Employee with ID {employee_id} not found."}), 404

    employee_data = dataBase[employee_id]
    return jsonify(employee_data)


@app.route('/data', methods=['POST'])
def receive_data():
    res = request.get_json()
    data = res.get('data')
    for item in data:
        add_record(ref, item)


    # do something with the data, such as storing it in a database
    response_data = {"result":"sucess"}
    return jsonify(response_data)

# add record to firebase RTDB
def add_record(ref,  data):

    users_record = ref.child("employee_location").child(f"{data['employee_id']}").child(data["timestamp"].split(".")[0])
    users_record.set(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)
