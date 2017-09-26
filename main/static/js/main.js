$(function(){

    var valueMax = $('.progress-bar-success').attr('aria-valuemax');
    var valueProgressNow = $('.progress-bar-success').attr('aria-valuenow');

    $('.button-up').on('click', function() {
        var btn = $(this);
        var input = $('.number-holder');
        if (input.attr('max') == undefined || parseInt(input.val())  < parseInt(input.attr('max'))) {
            input.val(parseInt(input.val(), 10) + 1);

            var currentCoin = $('.current_coin').text();
            var newCurVal = parseInt($('.progress-bar-danger').attr('aria-valuenow'));
            $('.progress-bar-danger').attr('aria-valuenow', newCurVal+1);
            $('.current_coin').text(parseInt(currentCoin)+1);
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

            var currentCoin = $('.current_coin').text();
            var newCurVal = parseInt($('.progress-bar-danger').attr('aria-valuenow'));
            $('.progress-bar-danger').attr('aria-valuenow', newCurVal-1);
            $('.current_coin').text(parseInt(currentCoin)-1);

        } else {
            btn.prev("disabled", true);
        }
    });

    $('.add-button').click(function () {
        var currentVal = $( ".number-holder" ).val();
        var currentProcentage = (currentVal * 100)/valueMax;

        $('#progressAdd').css('width', currentProcentage+'%');
        console.log(currentProcentage);
    });

    $( ".number-holder").on('keyup input', function() {
        var currentVal = $( ".number-holder" ).val();
        var currentProcentage = (currentVal * 100)/valueMax;
        var currentCoin = $('.current_coin').text();

        if(parseInt(currentCoin)) {
            $('#progressAdd').css('width', currentProcentage + '%');
            $('.current_coin').text(0);
            $('.current_coin').text(parseInt(valueProgressNow) + parseInt(currentVal));
        }else{
            $('.current_coin').text(parseInt(valueProgressNow));
        }
    });



});