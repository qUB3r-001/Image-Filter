$(function(){



      var startingSlide = 0;

      $(".rgb-channel").hide();
      $(".rgb-channel input").prop('disabled', true);
      $(".single-channel input").prop('disabled', false);
      if($("#result-img").attr('src')){
        startingSlide = 2;
      }

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

       var swiper1 = new Swiper(".myCarousel", {
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
        initialSlide: startingSlide,
        simulateTouch: false,
      });



    $("#img_file").change(function(){
        preview(this);
        $("#show_img").show();
        //$("#img_file").hide();
    });

    $("#filter_form").submit(function(){
        $(".loading-square").show();
        $("#result-div").show();
        swiper1.slideNext();
    });



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

function modeSelect(){
    if($("#single-channel-radio-btn").is(':checked')){
        $(".single-channel").show();
        $(".rgb-channel").hide();
        $(".rgb-channel input").prop('disabled', true);
        $(".single-channel input").prop('disabled', false);
    }
    else{
        $(".single-channel").hide();
        $(".rgb-channel").show();
        $(".rgb-channel input").prop('disabled', false);
        $(".single-channel input").prop('disabled', true);
    }
}