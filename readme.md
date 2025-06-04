# 🧘‍♀️ Fitness Class Booking API

A backend service for a fitness studio to allow users to:
- View upcoming classes like Yoga, Zumba, and HIIT
- Book a class using name and email
- Retrieve their bookings
- Track availability for each class

---

## Project Structure

```
booking_software/
├── scripts/
│   ├── handlers/
│   │   └── db.py
│   ├── models/
│   │   └── models.py
│   ├── routers/
│   │   ├── bookings.py
│   │   └── classes.py
│   └── services/
│       ├── bookings.py
│       └── classes.py
├── tests/
│   ├── test_bookings.py
│   └── test_classes.py
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

###  1. Clone the Project

```bash
git clone https://github.com/yourusername/booking_software.git
cd booking_software
```

###  2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

###  3. Install Dependencies

```bash
pip install -r requirements.txt
```

###  4. Create .env File

```bash
echo DATABASE_URL=sqlite:///./test.db > .env
```

### 🚀 Running the App

```bash
uvicorn main:app --reload
```

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

##  Available Endpoints

### `GET /classes`

Get list of all upcoming classes (in IST, readable format).

**Example Request:**
```http
GET /classes HTTP/1.1
Host: localhost:8000
```

**Example Response:**
```json
[
    {
        "id": 1,
        "name": "Yoga",
        "date": "2025-06-05",
        "time": "07:30 AM",
        "instructor": "Alice",
        "available_slots": 10
    }
]
```

---

### `POST /bookings`

Book a fitness class.

**Request Body:**
```json
{
    "class_id": 1,
    "client_name": "John Doe",
    "client_email": "john@example.com"
}
```

**Response:**
```json
{
    "id": 12,
    "class_id": 1,
    "client_name": "John Doe",
    "client_email": "john@example.com"
}
```

Handles edge cases:
- Overbooking returns 400
- Non-existent class returns 404

---

### `GET /bookings?client_email=...`

Fetch all bookings for a specific user.

**Example Request:**
```http
GET /bookings?client_email=john@example.com
```

**Example Response:**
```json
[
    {
        "id": 12,
        "class_id": 1,
        "client_name": "John Doe",
        "client_email": "john@example.com"
    }
]
```

---

##  Running Unit Tests

```bash
pytest
```

**Expected Output:**
```
==================== test session starts ====================
collected 4 items

tests/test_classes.py ..                                [50%]
tests/test_bookings.py ..                               [100%]

===================== 4 passed in 0.42s =====================
```

---

## Requirements

`requirements.txt`:
```
fastapi==0.111.0
uvicorn==0.29.0
SQLAlchemy==2.0.30
pydantic==2.7.1
pytz==2024.1
email-validator==2.1.1
pytest==8.2.1
httpx==0.27.0
```

Install them via:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

Shriram Narayana Bhat - Software Developer
Have questions? Feel free to connect!