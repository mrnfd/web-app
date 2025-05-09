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
    status
)
VALUES 
(2, 'Maple Street', 123, 10001, 'New York', 'Charming family home with garden.', 'HOUSE', 350000, '2024-05-01', 4, 2, 3, 120, 'ACTIVE'),

(3, 'Elm Avenue', 56, 90210, 'Los Angeles', 'Modern condo near downtown.', 'CONDO', 275000, '2024-04-15', 3, 2, 2, 85, 'PENDING'),

(2, 'Oak Drive', 89, 60007, 'Chicago', 'Townhome with garage and balcony.', 'TOWNHOME', 310000, '2024-03-22', 3, 2, 2, 95, 'ACTIVE'),

(3, 'Pine Road', 12, 33101, 'Miami', 'Multifamily building with 4 units.', 'MULTIFAMILY', 800000, '2024-01-10', 8, 4, 5, 300, 'ACTIVE'),

(2, 'Willow Lane', 7, 78701, 'Austin', 'Mobile home in quiet community.', 'MOBILE', 95000, '2024-02-05', 2, 1, 1, 60, 'PENDING'),

(3, 'Sunset Farm', 1, 97302, 'Salem', 'Beautiful farm with open fields.', 'FARM', 500000, '2023-11-01', 5, 3, 4, 250, 'SOLD'),

(2, 'Hilltop', NULL, 80014, 'Denver', 'Large plot of undeveloped land.', 'LAND', 150000, '2024-05-05', NULL, NULL, NULL, 1000, 'ACTIVE'),

(3, 'Commerce Blvd', 200, 19103, 'Philadelphia', 'Commercial property with warehouse.', 'COMMERCIAL', 1200000, '2023-12-12', NULL, NULL, NULL, 500, 'ACTIVE');

-- Now, insert the ListingImages 
-- First, let's get the listing IDs by assuming the auto-increment started at 1
-- Property 1 images for listings 1, 3, 5, 7
INSERT INTO "Listings_listingimage" (
    listing_id_id,
    image_url,
    thumbnail
)
VALUES
-- Listing 1 (Maple Street) - Property 1 images
(1, 'static\images\propertys_photos\test_property1\property1_img1.jpg', FALSE),
(1, 'static\images\propertys_photos\test_property1\property1_img2.jpg', FALSE),
(1, 'static\images\propertys_photos\test_property1\property1_img3.jpg', FALSE),
(1, 'static\images\propertys_photos\test_property1\property1_img4.jpg', FALSE),
(1, 'static\images\propertys_photos\test_property1\property1_thumb.jpg', TRUE),

-- Listing 3 (Oak Drive) - Property 1 images
(3, 'static\images\propertys_photos\test_property1\property1_img1.jpg', FALSE),
(3, 'static\images\propertys_photos\test_property1\property1_img2.jpg', FALSE),
(3, 'static\images\propertys_photos\test_property1\property1_img3.jpg', FALSE),
(3, 'static\images\propertys_photos\test_property1\property1_thumb.jpg', TRUE),

-- Listing 5 (Willow Lane) - Property 1 images
(5, 'static\images\propertys_photos\test_property1\property1_img1.jpg', FALSE),
(5, 'static\images\propertys_photos\test_property1\property1_img2.jpg', FALSE),
(5, 'static\images\propertys_photos\test_property1\property1_thumb.jpg', TRUE),

-- Listing 7 (Hilltop) - Property 1 images
(7, 'static\images\propertys_photos\test_property1\property1_img1.jpg', FALSE),
(7, 'static\images\propertys_photos\test_property1\property1_thumb.jpg', TRUE),

-- Property 2 images for listings 2, 4, 6, 8
-- Listing 2 (Elm Avenue) - Property 2 images
(2, 'static\images\propertys_photos\test_property2\property2_img1.jpg', FALSE),
(2, 'static\images\propertys_photos\test_property2\property2_img2.jpg', FALSE),
(2, 'static\images\propertys_photos\test_property2\property2_img3.jpg', FALSE),
(2, 'static\images\propertys_photos\test_property2\property2_thumb.jpeg', TRUE),

-- Listing 4 (Pine Road) - Property 2 images
(4, 'static\images\propertys_photos\test_property2\property2_img1.jpg', FALSE),
(4, 'static\images\propertys_photos\test_property2\property2_img2.jpg', FALSE),
(4, 'static\images\propertys_photos\test_property2\property2_thumb.jpeg', TRUE),

-- Listing 6 (Sunset Farm) - Property 2 images
(6, 'static\images\propertys_photos\test_property2\property2_img1.jpg', FALSE),
(6, 'static\images\propertys_photos\test_property2\property2_img3.jpg', FALSE),
(6, 'static\images\propertys_photos\test_property2\property2_thumb.jpeg', TRUE),

-- Listing 8 (Commerce Blvd) - Property 2 images
(8, 'static\images\propertys_photos\test_property2\property2_img2.jpg', FALSE),
(8, 'static\images\propertys_photos\test_property2\property2_thumb.jpeg', TRUE);