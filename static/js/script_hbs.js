$(document).ready(function(){
    $('.clickeff').mousedown(function(){
        $(this).css({
        'opacity':'0.80',
        });
    });
});
$(document).ready(function(){
    $('.clickeff').mouseup(function(){
        $(this).css({
        'opacity':'1',
        });
    });
});
$(document).ready(function(){
    $('.img_jumb').mouseenter(function(){
        $('img').css({
        'box-shadow': '0px 3px 3px 3px black;',
        });
    });
});

// $(document).ready(function(){
//     $('.fw_transition1').mouseenter(function(){
//         $(this).css({})
//     })
// })
