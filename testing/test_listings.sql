INSERT INTO "Listings_listing" (
    seller_id_id, street, number, description, type, price, listing_date, numb_of_rooms, size_sqm, status
)
VALUES 
(2, 'Maple Street', 123, 'Charming family home with garden.', 'HOUSE', 350000, '2024-05-01', 4, 120, 'ACTIVE'),

(3, 'Elm Avenue', 56, 'Modern condo near downtown.', 'CONDO', 275000, '2024-04-15', 3, 85, 'PENDING'),

(2, 'Oak Drive', 89, 'Townhome with garage and balcony.', 'TOWNHOME', 310000, '2024-03-22', 3, 95, 'ACTIVE'),

(3, 'Pine Road', 12, 'Multifamily building with 4 units.', 'MULTIFAMILY', 800000, '2024-01-10', 8, 300, 'ACTIVE'),

(2, 'Willow Lane', 7, 'Mobile home in quiet community.', 'MOBILE', 95000, '2024-02-05', 2, 60, 'PENDING'),

(3, 'Sunset Farm', 1, 'Beautiful farm with open fields.', 'FARM', 500000, '2023-11-01', 5, 250, 'SOLD'),

(2, 'Hilltop', NULL, 'Large plot of undeveloped land.', 'LAND', 150000, '2024-05-05', NULL, 1000, 'ACTIVE'),

(3, 'Commerce Blvd', 200, 'Commercial property with warehouse.', 'COMMERCIAL', 1200000, '2023-12-12', NULL, 500, 'ACTIVE');
