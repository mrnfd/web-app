# VLN2_Group47
**Castle Apartments**
_Castle Apartments_ is a real estate platform developed as part of the course T-220-VLN2. 
The site is designed to serve both buyers and property sellers through an elegant, responsive web application built using Django, PostgreSQL, and Python.

We successfully implemented all the core requirements outlined in the project description.
As well as these **extra requirements**:
1.     User registration for both Buyers and Sellers
2.     Login system with role-based access
3.     Editable user profiles, tailored to each user type
4.     Enhanced buyer profiles, including details such as email, phone number, street name, house number, city, and ZIP code
5.     The home page features a search bar that allows buyers to search for properties by address, city, ZIP code, or neighborhood. Matching properties are dynamically displayed based on the input.
6.     Search functionality is also integrated across multiple sections of the site, including the catalogue page, sellers page, My Offers page (for buyers), as well as the Listings and Offers pages (for sellers).    
7.     A seller directory page listing all registered sellers on the platform
8.     Home page, displays seller's offers and listings
9.     Listings page, allows sellers to view all of their property listings and add new ones
10.     Offers page, displays all purchase offers made by buyers on the seller's properties, with options to accept or decline each offer


**Usage**
To run the website you must
Set up a virtual environment:

python -m venv env

source env/bin/activate 

Install the necessary dependencies:

pip install -r requirements.txt

Start the server:

python manage.py runserver

Then the website should be running on http://localhost:8000/

_For the demonstration several test users were created._
Their credentials are listed below:
Buyers
Username: TestBuyerOne
Password: ABC12345ABC

Sellers
Username: TestSellerOne
Password: ABC12345ABC

Username: TestSellerTwo
Password: KALLI24680
