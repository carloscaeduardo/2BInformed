if (window.matchMedia("(max-width: 992px)").matches) {
  /* The viewport is less than, or equal to, 992 pixels wide */
      $('.post-slick').slick({
          infinite: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          autoplay: true,
          autoplaySpeed: 2000,
        });
} else {
    $('.post-slick').slick({
      infinite: true,
      slidesToShow: 2,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 2000,
        });
  /* The viewport is greater than 700 pixels wide */
}



