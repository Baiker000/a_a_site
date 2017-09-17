$(function(){

    $('.button-up').on('click', function() {
        var btn = $(this);
        var input = $('.number-holder');
        if (input.attr('max') == undefined || parseInt(input.val())  < parseInt(input.attr('max'))) {
            input.val(parseInt(input.val(), 10) + 1);
        }
        else if(!input.val()){
            input.val(1);
        } else {
            btn.next("disabled", true);
        }
    });

    $('.button-down').on('click', function() {
        var btn = $(this);
        var input = $('.number-holder');
        if (input.attr('min') == undefined || parseInt(input.val()) > parseInt(input.attr('min'))) {
            input.val(parseInt(input.val(), 10) - 1);
        } else {
            btn.prev("disabled", true);
        }
    });

    $('.add-button').click(function () {
        var currentVal = $( ".number-holder" ).val();
        $('#progressAdd').css('width', currentVal+'%');
    });

    $( ".number-holder" ).on('keyup', function() {
        var currentVal = $(this).val();
        $('#progressAdd').css('width', currentVal+'%');
    });
    $( ".number-holder" ).on('input', function() {
        var currentVal = $(this).val();
        $('#progressAdd').css('width', currentVal+'%');
    });
});