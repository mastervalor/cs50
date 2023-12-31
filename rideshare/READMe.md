# Ride Share App

Ride Share App is a web application that allows users to request, offer, and book shared rides. 

## Demo

A video demo of the app can be found here: https://www.youtube.com/watch?v=D4mlDl9Baok

## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)  
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [File Structure](#file-structure)
  - [Key Files](#key-files)
- [Features](#features)
- [Future Enhancements](#future-enhancements)
- [Contact](#contact)

## About The Project 

Ride Share App allows users to request a ride, offer a ride, and connect to coordinate ride details. Drivers can claim open ride requests and riders can track the status of their ride request.

Some key features:

- User authentication
- Post, view, and manage ride requests  
- Accept ride requests as a driver
- Messaging between drivers and riders
- View details and status of pending/upcoming rides

### Built With

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Python](https://www.python.org/)
- [MySQL](https://www.mysql.com/)
- [Bootstrap](https://getbootstrap.com/)

## Getting Started

To get a local copy up and running, follow these steps. 

### Prerequisites

- Python 3.x
- Pip  
- MySQL

### Installation

1. Clone the repository
 git clone https://github.com/your_username/ride-share.git
2. Navigate to project directory
cd ride-share
3. Create and activate a virtual environment
 python3 -m venv env
 source env/bin/activate
4. Install dependencies
 pip install -r requirements.txt
5. Configure environment variables for database credentials in a `.env` file  

6. Initialize the database 
 ```
 python manage.py db init
 python manage.py db migrate
 python manage.py db upgrade
7.Run the development server
 python server.py

 The app should now be running at http://localhost:5000!

Usage
Register an account

Users can register a new account by providing their name, email, and password.

Request a ride

Log in and navigate to the New Ride page to create a ride request by entering your origin, destination, and other details. Your request will appear on the dashboard for drivers to claim.

Offer a ride

Drivers can view open ride requests on the dashboard and claim a ride by clicking "I can drive". Claimed rides will appear under "Booked Rides".

Messaging

Once a ride is claimed, drivers and riders can message each other through the Details page to coordinate pickup times, locations, etc.

View and manage rides

Users can view status and details of pending, claimed, and past rides on their dashboard. Ride requests can also be edited or deleted.

Code Overview
File Structure
ride-share/
├── server.py
├── flask_app/
│   ├── __init__.py
│   ├── config/
│   │   └── mysqlconnection.py
│   ├── controllers/
│   │   ├── rides_controller.py
│   │   └── users_controller.py   
│   ├── models/
│   │   ├── message_model.py
│   │   ├── ride_model.py
│   │   └── user_model.py
│   └── templates/
│       ├── dashboard.html
│       ├── details.html
│       ├── edit.html
│       ├── login.html
│       └── new.html

Key Files
server.py

Runs the Flask app
init.py

Initializes Flask app
mysqlconnection.py

Initializes connection to MySQL database
rides_controller.py

Contains route handlers and logic for ride requests
users_controller.py

Contains route handlers and logic for user authentication
message_model.py

Database model for ride messages
ride_model.py

Database model for ride requests
user_model.py

Database model for user accounts
Templates

HTML templates for site pages
Features
Core Features:

User registration and authentication
Create, view, edit ride requests
Claim ride requests as a driver
Messaging between users
Dashboard to view past, pending, and upcoming rides
Additional Features:

Input validation and error messages
Database relationships between users, rides, and messages
Password hashing for security
Future Enhancements
Possible future enhancements:

Payment integration
Driver/rider ratings
Push notifications
Advanced search and filters
Direct messaging outside of ride context