-- First, insert the Listings with all the new attributes
INSERT INTO "Listings_listing" (
    seller_id_id, 
    street, 
    number, 
    zip, 
    city, 
    description, 
    type, 
    price, 
    listing_date, 
    numb_of_rooms, 
    bath_rooms, 
    bed_rooms, 
    size_sqm, 
    status,
    thumbnail
)
VALUES 
(4, 'Maple Street', 123, 10001, 'New York', 'Charming family home with garden.', 'HOUSE', 350000, '2024-05-01', 4, 2, 3, 120, 'ACTIVE','property_images\property1_thumb.jpg'),

(5, 'Elm Avenue', 56, 90210, 'Los Angeles', 'Modern condo near downtown.', 'CONDO', 275000, '2024-04-15', 3, 2, 2, 85, 'PENDING','property_images\property2_thumb.jpeg'),

(6, 'Oak Drive', 89, 60007, 'Chicago', 'Townhome with garage and balcony.', 'TOWNHOME', 310000, '2024-03-22', 3, 2, 2, 95, 'ACTIVE','property_images\property1_thumb.jpg'),

(5, 'Pine Road', 12, 33101, 'Miami', 'Multifamily building with 4 units.', 'MULTIFAMILY', 800000, '2024-01-10', 8, 4, 5, 300, 'ACTIVE','property_images\property2_thumb.jpeg'),

(6, 'Willow Lane', 7, 78701, 'Austin', 'Mobile home in quiet community.', 'MOBILE', 95000, '2024-02-05', 2, 1, 1, 60, 'PENDING','property_images\property1_thumb.jpg'),

(5, 'Sunset Farm', 1, 97302, 'Salem', 'Beautiful farm with open fields.', 'FARM', 500000, '2023-11-01', 5, 3, 4, 250, 'SOLD','property_images\property2_thumb.jpeg'),

(6, 'Hilltop', NULL, 80014, 'Denver', 'Large plot of undeveloped land.', 'LAND', 150000, '2024-05-05', NULL, NULL, NULL, 1000, 'ACTIVE','property_images\property1_thumb.jpg'),

(5, 'Commerce Blvd', 200, 19103, 'Philadelphia', 'Commercial property with warehouse.', 'COMMERCIAL', 1200000, '2023-12-12', NULL, NULL, NULL, 500, 'ACTIVE','property_images\property2_thumb.jpeg');


INSERT INTO "Listings_listingimage" (
    listing_id_id,
    image_url,
    thumbnail
)
VALUES

(1, 'images\propertys_photos\test_property1\property1_img1.jpg', FALSE),
(1, 'images\propertys_photos\test_property1\property1_img2.jpg', FALSE),
(1, 'images\propertys_photos\test_property1\property1_img3.jpg', FALSE),
(1, 'images\propertys_photos\test_property1\property1_img4.jpg', FALSE),
(1, 'images\propertys_photos\test_property1\property1_thumb.jpg', TRUE),

(3, 'images\propertys_photos\test_property1\property1_img1.jpg', FALSE),
(3, 'images\propertys_photos\test_property1\property1_img2.jpg', FALSE),
(3, 'images\propertys_photos\test_property1\property1_img3.jpg', FALSE),
(3, 'images\propertys_photos\test_property1\property1_thumb.jpg', TRUE),

(5, 'images\propertys_photos\test_property1\property1_img1.jpg', FALSE),
(5, 'images\propertys_photos\test_property1\property1_img2.jpg', FALSE),
(5, 'images\propertys_photos\test_property1\property1_thumb.jpg', TRUE),

(7, 'images\propertys_photos\test_property1\property1_img1.jpg', FALSE),
(7, 'images\propertys_photos\test_property1\property1_thumb.jpg', TRUE),

(2, 'images\propertys_photos\test_property2\property2_img1.jpg', FALSE),
(2, 'images\propertys_photos\test_property2\property2_img2.jpg', FALSE),
(2, 'images\propertys_photos\test_property2\property2_img3.jpg', FALSE),
(2, 'images\propertys_photos\test_property2\property2_thumb.jpeg', TRUE),

(4, 'images\propertys_photos\test_property2\property2_img1.jpg', FALSE),
(4, 'images\propertys_photos\test_property2\property2_img2.jpg', FALSE),
(4, 'images\propertys_photos\test_property2\property2_thumb.jpeg', TRUE),

(6, 'images\propertys_photos\test_property2\property2_img1.jpg', FALSE),
(6, 'images\propertys_photos\test_property2\property2_img3.jpg', FALSE),
(6, 'images\propertys_photos\test_property2\property2_thumb.jpeg', TRUE),

(8, 'images\propertys_photos\test_property2\property2_img2.jpg', FALSE),
(8, 'images\propertys_photos\test_property2\property2_thumb.jpeg', TRUE);