# World Needs More Food Trucks!
This application uses the [django](https://www.djangoproject.com/) framework to find a food truck no matter where in the city. **Based on the IP Address**.

    The application takes IP from the get request and gets the latitude and longitude using that IP address and then gets the distances of all trucks according to that IP and sorts them to get the nearest ones then returns them with JSON API representation.

## How to set up and run the application.

### 1. Install the requirements.
    pip install -r requirements.txt

### 2. migrate the database.
    python manage.py migrate

### 3. run the application.
    python manage.py runserver

## How to use tha application on localhost.
### 1. To get the 5 nearest trucks:  
#### Request this API link:  
    http://127.0.0.1:8000/api/

### 2. To get the the number of nearest trucks you want:  
#### Request this API link following with the number of trucks:  
    http://127.0.0.1:8000/api/<number_of_trucks>

