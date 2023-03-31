# sensmore
Sensmore project
-----------------------------------

sensmore project is project of performance monetoring in companys, factories, etc.. 
here all project Back-End files (servers)

this rebo contain 4 main codes file 
> - [generate random data.py](#Lgenerate-random-data)
> - api_reciever.py 
> - main server with RTDB.py
> - simulate 7 users devices.py

---------------------
### generate random data:
in this code file we generated company data and upload it to google firebase <br>
the company in our demo shown in code file contain 4 rooms, 2 pathrooms, office, kitchen and manager office
the company also have 5 department HR, IT, Marketing, Sales and Finance
we generat 10 employees in this company withrandom department

-----------------------
### api_reciever:
in code a flask server to recieve employee id and room id to be stored in firebase to be analyzed later

-----------------------
### main server with RTDB:
this is the same previus code with feature Real time tracking (teste for only 7 employees) for real time dashboard

--------------------------
### simulate 7 users devices:
this code simulate 7 employees device, run each employee in one thread, and generates 
