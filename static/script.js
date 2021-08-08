$(function(){
      var swiper = new Swiper(".mySwiper", {
        effect: "cube",
        grabCursor: true,
        cubeEffect: {
          shadow: true,
          slideShadows: false,
          shadowOffset: 20,
          shadowScale: 0.94,
        },
        pagination: {
          el: ".swiper-pagination",
        },
      });

       var swiper = new Swiper(".myCarousel", {
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      });


    function preview(input){
        if(input.files && input.files[0]){
            let reader = new FileReader();
            reader.onload = function(e){
                $("#show_img").attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#img_file").change(function(){
        preview(this);
        $("#show_img").show();
    });

    $("#filter_form").submit(function(){
        $(".loading-square").show();
        $("#result-div").show();
    });


});