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
      var resultArr = [77, 40, 58, 66, 50, 82, 69, 87, 49, 78, 56, 47, 61, 60, 55, 83, 62, 53, 49, 64, 41, 42, 68, 57, 58];
      var demoImgArr = [...Array(7)].map(el => Array(7).fill(96));
      var shift = 0;
    for(let i=0; i<7; i++){
        for(let j=0; j<7; j++){
            if(i==0 || j==0 || i==6 || j==6);
            else{
                demoImgArr[i][j] = 51-j-5*(i-1);
            };
        }
    }

    /*console.log(demoImgArr.slice(0,3).map(el => el.slice(0,3)).flat());*/

    var showDemoImgArr = [...Array(25)];
    /*console.log(showDemoImgArr);*/

    for(let i=0; i<5; i++){
        for(let j=0; j<5; j++){
            showDemoImgArr[j+5*i] = demoImgArr.slice(i,3+i).map(el => el.slice(j,j+3)).flat()
        }
    }

    /*console.log(showDemoImgArr);*/

      $(".rgb-channel").hide();
      $(".rgb-channel input").prop('disabled', true);
      $(".single-channel input").prop('disabled', false);
      $("#submit_form").prop('disabled', true);

      if($("#result-img").attr('src')){
        startingSlide = 2;
        $(".hide-after-result").hide();
        $(".reset-btn").show();
        let req_width = $(".img-org img").width();
        $(".img-comp-slider").css('width', req_width+'px');
        $(".img-comp-slider").val(0);
        $(".img-mix-wrapper").css('width', req_width+'px');
        /*$(".slider-btn")[0].click();*/
      }

      var swiper = new Swiper(".mySwiper", {
        effect: "cube",
        cubeEffect: {
          shadow: false,
          slideShadows: false,
          shadowOffset: 20,
          shadowScale: 0.94,
        },
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
      });

      const swiper_final = new Swiper(".Swiper-Main",{
        navigation: {
            nextEl: '.swiper-button-custom-next',
            prevEl: '.swiper-button-custom-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
            renderBullet: function (index, className) {
                return '<span class="' + className + '">' + (index + 1) + "</span>";
            },
        },
        spaceBetween: 100,

      });

      swiper_final.on('slideChange', function () {
        for (let i=0; i<3; i++){
            if(i < swiper_final.activeIndex) $(`.steps-apply-filter p:nth-of-type(${i+1})`).addClass("text-decoration-line-through").removeClass("bg-white text-dark");
            if(i === swiper_final.activeIndex) $(`.steps-apply-filter p:nth-of-type(${i+1})`).addClass("bg-white text-dark").removeClass("text-decoration-line-through");
            if(i > swiper_final.activeIndex) $(`.steps-apply-filter p:nth-of-type(${i+1})`).removeClass("bg-white text-dark text-decoration-line-through");
        }
      });

//    swiper_final.on('beforeInit', function () {
//      $(`.steps-apply-filter p:nth-of-type(${+swiper_final.activeIndex + 1}`).css('background-color', 'red');
//    });

    $("#img_file").change(function(){
        preview(this);
        $(".before-img-load").hide();
        $(".loader-bar").show();
        $(".loader-bar").delay(3000).hide(0);
        $(".after-img-load").delay(3000).show(0);
        $("#show_img").show();
        $("#submit_form").prop('disabled', false);
        //$("#img_file").hide();
    });

    $("#flexSwitchCheckDefault").change(function(){
           if($(this).is(':checked')){
           $(".single-channel").hide();
            $(".rgb-channel").show();
            $(".rgb-channel input").prop('disabled', false);
            $(".single-channel input").prop('disabled', true);
            $(".form-check-label").text("RGB Channel");
        }
        else{
          $(".single-channel").show();
            $(".rgb-channel").hide();
            $(".rgb-channel input").prop('disabled', true);
            $(".single-channel input").prop('disabled', false);
            $(".form-check-label").text("Single Channel");
        }
    });


    $("#filter_form").submit(function(){
        $("#submit_form").hide();
        $(`.steps-apply-filter p:nth-of-type(${swiper_final.activeIndex + 1})`).addClass("text-decoration-line-through");
        $(".loading-square").show();
        $("#result-div").show();
/*        swiper1.slideNext();*/
//        $(".myCarousel .swiper-pagination-bullet-active").html('<i class="fas fa-check"></i>');
    });

    $(".after-img-load").click(function(){
        $(".before-img-load").show();
        $(".loader-bar").hide();
        $(".after-img-load").hide();
        $("#img_file").val('');
        $("#submit_form").prop('disabled', true);
    });

//    $(".myCarousel .swiper-button-next").click(function(){
//        let num = $(".myCarousel .swiper-pagination-bullet-active").text();
//
//        $(".myCarousel .swiper-pagination span").each(function(i){
//            if(i+1<num) $(this).html('<i class="fas fa-check"></i>');
//            else $(this).html(i+1);
//        });
//    });

/*     $(".myCarousel .swiper-button-prev").click(function(){
        let num = $(".myCarousel .swiper-pagination-bullet-active").text();

        $(".myCarousel .swiper-pagination span").each(function(i){
            if(i+1<num) $(this).html('<i class="fas fa-check"></i>');
            else $(this).html(i+1);
        });
    });*/

    /*console.log($(".demo-img-pixel"));*/
//    setInterval(function(){
//        if(shift>24) shift = 0;
//        $(".demo-img-pixel").each(function(i){
//            $(this).css('background-color', 'hsl(0,0%,'+showDemoImgArr[shift][i]+'%)');
//        });
//        $(".result-pixel-2").css('background-color', 'hsl(0,0%,'+resultArr[shift]+'%)');
//        shift++;
//
//
//  /*      let focusCoor = $(".focus-image").offset();
//        let {top, left} = $(".demo-image-div-2").offset();
//        let height = top - focusCoor.top;
//        let width = left - focusCoor.left;
//        let realHeight = Math.sqrt(Math.pow(height, 2) + Math.pow(width, 2));
//        let angle = Math.round(Math.atan(width/height)*57.296);
//        $(".top-left-point").css({
//            'top':`${focusCoor.top}px`,
//            'left': `${focusCoor.left}px`,
//            'height': realHeight,
//            'transform': 'rotate(-'+angle+'deg)',
//        });
//        $(".bottom-left-point").css({
//            'top':`${focusCoor.top+72}px`,
//            'left': `${focusCoor.left}px`,
//            'height': realHeight,
//            'transform': 'rotate(-'+angle+'deg)',
//        });*/
//    }, 1000);


});

