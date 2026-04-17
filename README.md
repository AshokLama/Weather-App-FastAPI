#Weather App API (FastAPI)

A simple Weather API built using FastAPI that allows users to:

* Get current weather by location
* Store weather queries in a database
* Perform full CRUD operations
* Export stored data

---

##Features

##Core Features

* Get weather using location (city, zip, etc.)
* Store results in database (SQLite)
* Input validation (date range + location)

##CRUD Operations

* **CREATE** → Add weather request with date range
* **READ** → View all stored weather data
* **UPDATE** → Update stored weather info
* **DELETE** → Remove records

##API Integration

* Weather data from OpenWeather API
* Optional:

  * Google Maps link
  * YouTube search for location

##Data Export

* Export data to CSV file

---

#Project Structure

```
weather_app/
│── main.py              # Main FastAPI app
│── database.py          # Database connection
│── models.py            # Database models
│── schemas.py           # Request/response validation
│── crud.py              # CRUD logic
│── weather_service.py   # External API call
│── export.py            # Export functionality
│── requirements.txt     # Dependencies
```

---

#Installation

##1. Clone project

```
git clone https://github.com/AshokLama/Weather-App-FastAPI.git
```

##2. Install dependencies

```
 pip3 install fastapi uvicorn sqlalchemy requests pydantic python-multipart
```

##3. Add API Key

Get free API key from OpenWeather and update:

```
weather_service.py
```

```
API_KEY = "your_api_key_here"
```

---

#Run Application

```
python3 -m uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

#API Endpoints

##Create Weather Record

**POST** `/weather/`

```
{
  "location": "Denver",
  "start_date": "2026-01-01",
  "end_date": "2026-01-05"
}
```

---

##Get All Records

**GET** `/weather/`

---

##Update Record

**PUT** `/weather/{id}?temp=30`

---

##Delete Record

**DELETE** `/weather/{id}`

---

##Export Data

**GET** `/export/csv`

---

#Validation Rules

* Start date must be before end date
* Location must be valid
* ID must exist for update/delete

---

#Technologies Used

* FastAPI
* SQLite
* SQLAlchemy
* Requests

---



