# bloodsupport

1. clone it and open terminal and cd to this folder

2. run command:
        source newenv/bin/activate
  This activates a virtual environment for the project which contains all dependencies like python, pip, django,etc.
 3. python manage.py makemigrations
 4. python manage.py migrate
5. python manage.py runserver

root url is 127.0.0.1:8000/

for getting json data go to http://127.0.0.1:8000/api/?lat=31.398636&long=75.531594&radius=10

This is a get request it has three fields lat(latitude of current location), long(longitude) and radius(radius in which to find blood banks)

It returns JSON data in the below format:
  
  [
    {
        "id": 1,
        "hosp_name": "ABC Hospital",
        "hosp_add": "G.T. Road, Jalandhar",
        "hosp_contact": "12344567",
        "latitude": 31.398636,
        "longitude": 75.531594,
        "a_pos": 12,
        "b_pos": 13,
        "ab_pos": 5,
        "o_pos": 20,
        "a_neg": 1,
        "ab_neg": 0,
        "b_neg": 0,
        "o_neg": 2
    }
]

If u want to add more data go to  http://127.0.0.1:8000/admin
Log in using the below credentials:
  username: parth
  password: demo1234
  
and then go do bloodbank and then add
  
  If login fails:
    1. Go to terminal(the one in which server is running)
    2. Stop server by Ctrl+C
    3. Run command:
        python manage.py createsuperuser
    4. Put in username and password u want to keep
    
    
    
Blood group not to be sent to backend when json response comes in just check if the given blood bank has the blood group requested by user in the form
and if qty available > qty requested show Available else show only x qty available nd if qty == 0 then dont show it


