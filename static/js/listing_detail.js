let currentSlide = 0;

function moveSlide(direction) {
    // Get all carousel items and total number of slides
    const slides = document.querySelectorAll('.carousel-item');
    const totalSlides = slides.length;

    // Update current slide index, wrapping around properly
    currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
    updateSlidePosition();
}

function updateSlidePosition() {
    // Shift the carousel container to show the current slide
    const slides = document.querySelector('.carousel-images');
    const slideWidth = document.querySelector('.carousel-item').clientWidth;
    slides.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}

document.addEventListener('DOMContentLoaded', function (){
    // Toggle visibility of additional info on clicking label
    const label = document.getElementById('toggle-info');
    const info = document.getElementById('additional-info');

    if (label && info) {
        label.addEventListener('click', function () {
            info.classList.toggle('additional-info');
        });
    }

    // Navigate to create offer page when button clicked
    const createOfferBtn = document.querySelector('.create-offer-button');
    if (createOfferBtn) {
        createOfferBtn.addEventListener('click', function() {
            const listingId = this.getAttribute('data-id');
            window.location.href = `/offers/${listingId}/create_offer`;
        });
    }

    // Navigate to update offer page when button clicked
    const updateoffer = document.querySelector('.update-offer-button');
    if (updateoffer) {
        updateoffer.addEventListener('click', function () {
            const offerId = this.getAttribute('data-id');
            window.location.href = `/offers/update_offer/${offerId}`;
        });
    }
});