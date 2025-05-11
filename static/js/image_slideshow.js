let currentSlide = 0;

function moveSlide(direction) {
    const slides = document.querySelectorAll('.carousel-item');
    const totalSlides = slides.length;
    currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
    updateSlidePosition();
}

function updateSlidePosition() {
    const slides = document.querySelector('.carousel-images');
    const slideWidth = document.querySelector('.carousel-item').clientWidth;
    slides.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}