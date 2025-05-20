#!/usr/bin/env python
"""
Django database reset and test data population script.
Run with: python manage.py shell < reset_db.py
"""

from django.db import connection
from django.conf import settings

from Buyers.models import Buyer
from Listings.models import Listing, ListingImage
from Sellers.models import Seller
from django.contrib.auth.models import User

from datetime import date
import sys

def reset_database():
    """Clear all data from the database while handling foreign key constraints"""
    print("Starting database reset...")
    
    # Get cursor
    cursor = connection.cursor()
    
    # Turn off foreign key constraints temporarily
    if 'postgresql' in settings.DATABASES['default']['ENGINE']:
        cursor.execute('SET CONSTRAINTS ALL DEFERRED;')
    elif 'sqlite' in settings.DATABASES['default']['ENGINE']:
        cursor.execute('PRAGMA foreign_keys = OFF;')
    
    try:
        # Clear tables in order to avoid foreign key conflicts
        print("Clearing database tables...")
        ListingImage.objects.all().delete()
        Listing.objects.all().delete()
        Buyer.objects.all().delete()
        Seller.objects.all().delete()
        
        # Turn foreign key constraints back on
        if 'postgresql' in settings.DATABASES['default']['ENGINE']:
            cursor.execute('SET CONSTRAINTS ALL IMMEDIATE;')
        elif 'sqlite' in settings.DATABASES['default']['ENGINE']:
            cursor.execute('PRAGMA foreign_keys = ON;')
            
        print("Database cleared successfully.")
        return True
    except Exception as e:
        print(f"Error during database reset: {e}")
        return False

def create_test_data():
    """Create test data for the application"""
    print("Creating test data...")
    
    # Create test sellers
    print("Creating test sellers...")
    test_sellers = [
        Seller(
            name='test_seller1',
            email='test_seller1@example.com',
            contact_number='123-456-7890',
            seller_type='Individual',
            bio='Test individual seller profile.'
        ),
        Seller(
            name='test_seller2',
            email='test_seller2@example.com',
            contact_number='987-654-3210',
            seller_type='Agency',
            street='Main St, Suite 500',
            house_numb='123',
            city='Metropolis',
            postal_code='12345',
            bio='Test agency seller profile with office location.'
        ),
        Seller(
            name='test_seller3',
            email='test_seller3@example.com',
            contact_number='555-123-4567',
            seller_type='Individual',
            street='Beach Rd',
            house_numb='789',
            city='Coast City',
            postal_code='67890',
            bio='Experienced coastal property specialist.'
        )
    ]
    Seller.objects.bulk_create(test_sellers)
    print("Test sellers created successfully.")
    
    # Create test buyers
    print("Creating test buyers...")
    test_buyers = [
        Buyer(
            name='test_buyer1',
            email='test_buyer1@example.com',
            contact_number='5551234567',
            profile_image_url='https://randomuser.me/api/portraits/men/1.jpg',
            street='Maple Avenue',
            house_numb='123',
            zip_code=10001,
            country='United States'
        ),
        Buyer(
            name='test_buyer2',
            email='test_buyer2@example.com',
            contact_number='5552345678',
            profile_image_url='https://randomuser.me/api/portraits/women/2.jpg',
            street='Oak Street',
            house_numb='456',
            zip_code=20002,
            country='Canada'
        ),
        Buyer(
            name='test_buyer3',
            email='test_buyer3@example.com',
            contact_number='5553456789',
            profile_image_url='https://randomuser.me/api/portraits/men/3.jpg',
            street='Pine Road',
            house_numb='789',
            zip_code=30003,
            country='United Kingdom'
        ),
        Buyer(
            name='test_buyer4',
            email='test_buyer4@example.com',
            contact_number='5554567890',
            profile_image_url='https://randomuser.me/api/portraits/women/4.jpg',
            street='Cedar Lane',
            house_numb='101',
            zip_code=40004,
            country='Australia'
        )
    ]
    Buyer.objects.bulk_create(test_buyers)
    print("Test buyers created successfully.")

    # Get seller references
    seller1 = Seller.objects.get(name='test_seller1')
    seller2 = Seller.objects.get(name='test_seller2')
    seller3 = Seller.objects.get(name='test_seller3')
    
    # Create test listings
    print("Creating test listings...")
    test_listings = [
        # Seller 2 listings
        Listing(
            seller_id=seller1,
            street='Maple Street',
            number=123,
            zip=10001,
            city='New York',
            description='Charming family home with garden.',
            type='HOUSE',
            price=350000,
            listing_date=date(2024, 5, 1),
            numb_of_rooms=4,
            bath_rooms=2,
            bed_rooms=3,
            size_sqm=120,
            status='ACTIVE',
            thumbnail='images/propertys_photos/test_property1/property1_thumb.jpg'
        ),
        Listing(
            seller_id=seller2,
            street='Oak Drive',
            number=89,
            zip=60007,
            city='Chicago',
            description='Townhome with garage and balcony.',
            type='TOWNHOME',
            price=310000,
            listing_date=date(2024, 3, 22),
            numb_of_rooms=3,
            bath_rooms=2,
            bed_rooms=2,
            size_sqm=95,
            status='ACTIVE',
            thumbnail='images/propertys_photos/test_property1/property1_thumb.jpg'
        ),
        Listing(
            seller_id=seller2,
            street='Willow Lane',
            number=7,
            zip=78701,
            city='Austin',
            description='Mobile home in quiet community.',
            type='MOBILE',
            price=95000,
            listing_date=date(2024, 2, 5),
            numb_of_rooms=2,
            bath_rooms=1,
            bed_rooms=1,
            size_sqm=60,
            status='PENDING',
            thumbnail='images/propertys_photos/test_property1/property1_thumb.jpg'
        ),
        Listing(
            seller_id=seller2,
            street='Hilltop',
            number=None,
            zip=80014,
            city='Denver',
            description='Large plot of undeveloped land.',
            type='LAND',
            price=150000,
            listing_date=date(2024, 5, 5),
            numb_of_rooms=None,
            bath_rooms=None,
            bed_rooms=None,
            size_sqm=1000,
            status='ACTIVE',
            thumbnail='images/propertys_photos/test_property1/property1_thumb.jpg'
        ),
        
        # Seller 3 listings
        Listing(
            seller_id=seller3,
            street='Elm Avenue',
            number=56,
            zip=90210,
            city='Los Angeles',
            description='Modern condo near downtown.',
            type='CONDO',
            price=275000,
            listing_date=date(2024, 4, 15),
            numb_of_rooms=3,
            bath_rooms=2,
            bed_rooms=2,
            size_sqm=85,
            status='PENDING',
            thumbnail='images/propertys_photos/test_property2/property2_thumb.jpeg'
        ),
        Listing(
            seller_id=seller3,
            street='Pine Road',
            number=12,
            zip=33101,
            city='Miami',
            description='Multifamily building with 4 units.',
            type='MULTIFAMILY',
            price=800000,
            listing_date=date(2024, 1, 10),
            numb_of_rooms=8,
            bath_rooms=4,
            bed_rooms=5,
            size_sqm=300,
            status='ACTIVE',
            thumbnail='images/propertys_photos/test_property2/property2_thumb.jpeg'
        ),
        Listing(
            seller_id=seller3,
            street='Sunset Farm',
            number=1,
            zip=97302,
            city='Salem',
            description='Beautiful farm with open fields.',
            type='FARM',
            price=500000,
            listing_date=date(2023, 11, 1),
            numb_of_rooms=5,
            bath_rooms=3,
            bed_rooms=4,
            size_sqm=250,
            status='SOLD',
            thumbnail='images/propertys_photos/test_property2/property2_thumb.jpeg'
        ),
        Listing(
            seller_id=seller3,
            street='Commerce Blvd',
            number=200,
            zip=19103,
            city='Philadelphia', 
            description='Commercial property with warehouse.',
            type='COMMERCIAL',
            price=1200000,
            listing_date=date(2023, 12, 12),
            numb_of_rooms=None,
            bath_rooms=None,
            bed_rooms=None,
            size_sqm=500,
            status='ACTIVE',
            thumbnail='images/propertys_photos/test_property2/property2_thumb.jpeg'
        )
    ]
    Listing.objects.bulk_create(test_listings)
    print("Test listings created successfully.")
    
    # Get all listings to associate images
    listings = list(Listing.objects.all())
    
    # Create listing images
    print("Creating listing images...")
    listing_images = []
    
    # Images for listing 1
    listing_images.extend([
        ListingImage(listing_id=listings[0], image_url='images/propertys_photos/test_property1/property1_img1.jpg', thumbnail=False),
        ListingImage(listing_id=listings[0], image_url='images/propertys_photos/test_property1/property1_img2.jpg', thumbnail=False),
        ListingImage(listing_id=listings[0], image_url='images/propertys_photos/test_property1/property1_img3.jpg', thumbnail=False),
        ListingImage(listing_id=listings[0], image_url='images/propertys_photos/test_property1/property1_img4.jpg', thumbnail=False),
        ListingImage(listing_id=listings[0], image_url='images/propertys_photos/test_property1/property1_thumb.jpg', thumbnail=True)
    ])
    
    # Images for listing 2
    listing_images.extend([
        ListingImage(listing_id=listings[1], image_url='images/propertys_photos/test_property2/property2_img1.jpg', thumbnail=False),
        ListingImage(listing_id=listings[1], image_url='images/propertys_photos/test_property2/property2_img2.jpg', thumbnail=False),
        ListingImage(listing_id=listings[1], image_url='images/propertys_photos/test_property2/property2_img3.jpg', thumbnail=False),
        ListingImage(listing_id=listings[1], image_url='images/propertys_photos/test_property2/property2_thumb.jpeg', thumbnail=True)
    ])
    
    # Images for listing 3
    listing_images.extend([
        ListingImage(listing_id=listings[2], image_url='images/propertys_photos/test_property1/property1_img1.jpg', thumbnail=False),
        ListingImage(listing_id=listings[2], image_url='images/propertys_photos/test_property1/property1_img2.jpg', thumbnail=False),
        ListingImage(listing_id=listings[2], image_url='images/propertys_photos/test_property1/property1_img3.jpg', thumbnail=False),
        ListingImage(listing_id=listings[2], image_url='images/propertys_photos/test_property1/property1_thumb.jpg', thumbnail=True)
    ])
    
    # Images for listing 4
    listing_images.extend([
        ListingImage(listing_id=listings[3], image_url='images/propertys_photos/test_property2/property2_img1.jpg', thumbnail=False),
        ListingImage(listing_id=listings[3], image_url='images/propertys_photos/test_property2/property2_img2.jpg', thumbnail=False),
        ListingImage(listing_id=listings[3], image_url='images/propertys_photos/test_property2/property2_thumb.jpeg', thumbnail=True)
    ])
    
    # Images for listing 5
    listing_images.extend([
        ListingImage(listing_id=listings[4], image_url='images/propertys_photos/test_property2/property2_img1.jpg', thumbnail=False),
        ListingImage(listing_id=listings[4], image_url='images/propertys_photos/test_property2/property2_img3.jpg', thumbnail=False),
        ListingImage(listing_id=listings[4], image_url='images/propertys_photos/test_property2/property2_thumb.jpeg', thumbnail=True)
    ])
    
    # Images for listing 6
    listing_images.extend([
        ListingImage(listing_id=listings[5], image_url='images/propertys_photos/test_property1/property1_img1.jpg', thumbnail=False),
        ListingImage(listing_id=listings[5], image_url='images/propertys_photos/test_property1/property1_img2.jpg', thumbnail=False),
        ListingImage(listing_id=listings[5], image_url='images/propertys_photos/test_property1/property1_thumb.jpg', thumbnail=True)
    ])
    
    # Images for listing 7
    listing_images.extend([
        ListingImage(listing_id=listings[6], image_url='images/propertys_photos/test_property1/property1_img1.jpg', thumbnail=False),
        ListingImage(listing_id=listings[6], image_url='images/propertys_photos/test_property1/property1_thumb.jpg', thumbnail=True)
    ])
    
    # Images for listing 8
    listing_images.extend([
        ListingImage(listing_id=listings[7], image_url='images/propertys_photos/test_property2/property2_img2.jpg', thumbnail=False),
        ListingImage(listing_id=listings[7], image_url='images/propertys_photos/test_property2/property2_thumb.jpeg', thumbnail=True)
    ])
    
    ListingImage.objects.bulk_create(listing_images)
    print("Test listing images created successfully.")

def main():
    print("Database reset and repopulation script started")
    
    # Reset the database
    if not reset_database():
        print("Database reset failed. Exiting.")
        return False
    
    # Create test data
    try:
        create_test_data()
        print("Database successfully repopulated with test data!")
        return True
    except Exception as e:
        print(f"Error creating test data: {e}")
        return False

if __name__ == "__main__":
    # This allows the script to be run directly with:
    # python manage.py shell < reset_db.py
    success = main()
    if not success:
        sys.exit(1)