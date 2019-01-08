jQuery(document).ready(function(){
    
    jQuery('.megamenu_toggle').click(function(e){
        e.preventDefault(); 
        jQuery(this).toggleClass('active');
        jQuery('.menu_section_full').slideDown();    
        jQuery('.active_page').slideUp();
    });    
 
    jQuery('.megamenu_toggle2').click(function(e){
        e.preventDefault(); 
        jQuery('.menu_section_full').slideUp();    
    });   

    jQuery('.navhide a').click(function(e){  
        jQuery('.menu_section_full').slideUp();   
        jQuery('.active_page').slideUp();
        jQuery('section').removeClass('active_page');
    });    

    jQuery('.custom_onclicknav').click(function(){
       
        var secname = jQuery(this).data('show');
        console.log(secname); 
        
        // About Us
        if(secname==='aboutus') { 
            jQuery('.about_us_page').addClass('active_page');  
        }
        
        // Training Section
        if(secname==='training') {
            jQuery('.training_page').addClass('active_page');  
        }
       
        // Careers
        if(secname==='careers') {
            jQuery('.careers_page').addClass('active_page');  
        }
        
        jQuery('.active_page').slideDown(); 
        
    });
    
    // ApplyNow
    jQuery('.apply_now_btn').click(function(){
       
        var devtype = jQuery(this).data('dtype');
        var cantype = jQuery(this).data('ctype');
        jQuery('.career_full_page').addClass('active_page');
        jQuery('.active_page').slideDown();  
//        console.log(devtype+cantype);  
        
    });

    // ApplyNow
    jQuery('.view_service_details').click(function(){
       
        jQuery('.wwcd_inner').addClass('active_page');
        jQuery('.active_page').slideDown();   
        
    });

    // Home Slider Script
    jQuery('.main_slider').slick({
        dots: true,
        speed: 300,
        slidesToShow: 1,
        prevArrow: false,
        nextArrow: false,
        autoplay: false,
        centerMode: true
    });  


var windowwidth = jQuery(window).width();
    if(windowwidth>768) { 
        jQuery('#fullpage').pagepiling({ 
            direction: 'horizontal',
            anchors: ['slider', 'whatwecado', 'howweareworking', 'contactus'],
            navigation: {
                'position': 'right',
                'tooltips': ['Slider', 'What We Can Do', 'How We Are Working', 'Contact Us']
            },
            onLeave: function(index, nextIndex, direction){ 
                $('.section:nth-child('+index+') .text-translate').removeClass('active');
                $('.section:nth-child('+nextIndex+') .text-translate').addClass('active');

                if(direction == 'up') {
                  // alert(nextIndex);
                  $('.section:nth-child('+index+') .translate').addClass('active');
                  $('.section:nth-child('+nextIndex+') .translate').addClass('in');
                  setTimeout(function() { 
                    $('.section:nth-child('+nextIndex+') .translate').removeClass('in'); 
                    $('.section:nth-child('+nextIndex+') .translate').addClass('active'); 
                    $('.section:nth-child('+index+') .translate').removeClass('active'); 
                    $('.section:nth-child('+index+') .translate').addClass('out'); 
                  }, 500);
                }
                if(direction == 'down') {
                  // alert(nextIndex);
                  $('.section:nth-child('+index+') .translate').addClass('active');
                  $('.section:nth-child('+nextIndex+') .translate').addClass('out');
                  setTimeout(function() { 
                    $('.section:nth-child('+nextIndex+') .translate').removeClass('out'); 
                    $('.section:nth-child('+nextIndex+') .translate').addClass('active'); 
                    $('.section:nth-child('+index+') .translate').removeClass('active'); 
                    $('.section:nth-child('+index+') .translate').addClass('in'); 
                  }, 500);
                }
            },
            afterLoad: function(anchorLink, index){

                if(index==1) {
                     // Home Slider Script
                    jQuery('.main_slider').slick({
                        dots: true,
                        speed: 300,
                        slidesToShow: 1,
                        centerMode: true
                    });  
                }   

                if(index==3)  {
                    // Horizontal Scrolling
                    jQuery('.hr_scrolling').mousewheel(function(event, delta) {
                        this.scrollLeft -= (delta * 100);
                        event.preventDefault();  
                        console.log('left:'+this.scrollLeft);
                        if((this.scrollLeft<4130) && (this.scrollLeft>0)){ 
                            return false; 
                        }
                    }); 
                }
            }    
          });
    }
 
});

jQuery(window).scroll(function() {    
    var scroll = jQuery(window).scrollTop();

    if (scroll >= 100) {
        jQuery("body").addClass("scrolled");
    } else {
        jQuery("body").removeClass("scrolled");
    }
});   


// slider animations
var slide_btn = [
                    'slick-slide-control00',
                    'slick-slide-control01',
                    'slick-slide-control02',
                    'slick-slide-control03'
                ];
var slide_img = [
                    'h_img_1',
                    'h_img_2',
                    'h_img_3',
                    'h_img_4'
                ];
    
$(document).ready(()=>{
    $('#slick-slide-control00').on('click', (event)=> {slider_anim('slick-slide-control00')});
    $('#slick-slide-control01').on('click', (event)=> {slider_anim('slick-slide-control01')});
    $('#slick-slide-control02').on('click', (event)=> {slider_anim('slick-slide-control02')});
    $('#slick-slide-control03').on('click', (event)=> {slider_anim('slick-slide-control03')});
})

function slider_anim(btn) {
    for (var i = 0; i < slide_btn.length; i++) {
        if (btn == slide_btn[i]) {
            $("#"+slide_img[i]).addClass('animated zoomIn');
        }else{
            $("#"+slide_img[i]).removeClass('animated zoomIn');
        }
    }
}

$('[data-toggle="datepicker"]').datepicker();
