from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# init google firebase credentials.
# read cred.json file and init database
cred = credentials.Certificate("D:/work/python/beacon files/sensemore.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL':"https://sensemore-6c16d-default-rtdb.firebaseio.com"
})


# Get a database reference to our blog.
ref = db.reference("/")


app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    res = request.get_json()
    data = res.get('data')
    for item in data:
        add_record(ref, item)

    # do something with the data, such as storing it in a database
    response_data = {"result":"sucess"}
    return jsonify(response_data)


def add_record(ref,  data):

    users_record = ref.child("employee_location").child(f"{data['employee_id']}").child(data["timestamp"].split(".")[0])
    users_record.set(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)
