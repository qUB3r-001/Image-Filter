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

function reveal(){
    let value = $(".img-comp-slider").val();
    let width = $(".img-comp-slider").width();
    let shift = Math.round(value*width/100)+'px';
    $(".img-final img").css('transform', 'translateX(-'+shift+')');
    $(".img-final").css('marginLeft', shift);
}

$(function(){
      var startingSlide = 0;

      $(".rgb-channel").hide();
      $(".rgb-channel input").prop('disabled', true);
      $(".single-channel input").prop('disabled', false);
      if($("#result-img").attr('src')){
        startingSlide = 2;
        $(".myCarousel").hide();
        $(".reset-btn").show();
        let req_width = $(".img-org img").width();
        $(".img-comp-slider").css('width', req_width+'px');
        $(".img-comp-slider").val(0);
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
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
          renderBullet: function (index, className) {
            return '<span class="' + className + '">' + (index + 1) + "</span>";
          },
        },
        simulateTouch: false,
        initialSlide: startingSlide,
      });



    $("#img_file").change(function(){
        preview(this);
        $(".before-img-load").hide();
        $(".loader-bar").show();
        $(".loader-bar").delay(3000).hide(0);
        $(".after-img-load").delay(3000).show(0);
        $("#show_img").show();
        //$("#img_file").hide();
    });

    $("#filter_form").submit(function(){
        $(".loading-square").show();
        $("#result-div").show();
        swiper1.slideNext();
    });

    $(".after-img-load").click(function(){
        $(".before-img-load").show();
        $(".loader-bar").hide();
        $(".after-img-load").hide();
        $("#img_file").val('');
    });


});
