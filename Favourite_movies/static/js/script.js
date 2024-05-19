
document.addEventListener('DOMContentLoaded', ()=> {
    const currentUrl = window.location.href;
    console.log('vvvvvvvvvvvvvvvvvvvvvvvvv', currentUrl)
    document.querySelectorAll('.nav-bottom a').forEach((a)=> {
        if (currentUrl.endsWith('movies')) return
        if (currentUrl.includes((a.innerText.toLowerCase())) ) {
            a.classList.add('nav-selected')
        }
    })
    const prevButton = document.querySelector('.movies-carousel-prev');
    const nextButton = document.querySelector('.movies-carousel-next');
    const carouselItems = document.querySelectorAll('.movies-carousel-movie');
    
    let currentIndex = 0;
    
    console.log('vvvvvvvvvvvvvvvvvvvvvvvvv', prevButton)
    slideCarousel();
    
    prevButton.addEventListener('click', function() {
        if (currentIndex > 0) {
        currentIndex--;
        slideCarousel();
        }
    });
    
    nextButton.addEventListener('click', function() {
        if (currentIndex < carouselItems.length - 1) {
        currentIndex++;
        slideCarousel();
        }
    });
    
    function slideCarousel() {
        console.log(carouselItems)
        console.log(currentIndex)
        carouselItems.forEach(node => node.classList.remove('selected'))
        carouselItems[currentIndex].classList.add('selected')
        const offset = carouselItems[currentIndex].offsetLeft;
        document.querySelector('.carousel-inner').scrollLeft = offset;
    }

    // const carouselItemsImgs = document.querySelectorAll('.movies-carousel-movie img');
    // carouselItemsImgs.forEach((item, i) => {
    //     item.addEventListener('click', (e)=> {
    //         e.preventDefault()
    //         currentIndex=i
    //         slideCarousel()
    //     })
    // })
      
})

