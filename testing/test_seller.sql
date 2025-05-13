INSERT INTO "Sellers_seller" (
    name, email, contact_number, profile_image_url, seller_type,
    street, house_numb, city, zip_code, logo, cover_image, bio
)
VALUES
    (
        'test_seller1', 'test_seller1@example.com', '123-456-7890',
        'images/seller_photos/test_seller1/profile_seller1.png',
        'Individual',
        NULL, NULL, '', '', NULL, NULL, 'Test individual seller profile.'
    ),
    (
        'test_seller2', 'test_seller2@example.com', '987-654-3210',
        'images/seller_photos/test_seller2/profile_seller2.png',
        'Agency',
        '123 Main St', '500', 'Metropolis', '12345', 
        'images/seller_photos/test_seller2/logo_seller2.png', 
        'images/seller_photos/test_seller2/cover_seller2.png',
         'Test agency seller profile with office location.'
    ),
    (
        'test_seller3', 'test_seller3@example.com', '222-333-4444',
        'images/seller_photos/test_seller3/profile_seller3.png',
        'Agency',
        '456 Elm St', 'Suite 12', 'Gotham', '67890',
        'images/seller_photos/test_seller3/logo_seller3.png',
        'images/seller_photos/test_seller3/cover_seller3.png',
        'Another test agency seller profile.'
    );