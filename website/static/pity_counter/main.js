$(document).ready(function(){
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    $('.btn').click(function(){
        var but = $(this)[0];

        $.ajax({
            url: '',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: but.id,
                value: but.value
            },
            type: 'post',
            success: function(response) {
                if (but.id == 'Char') {
                    var element = document.getElementById('char');
                } else if (but.id == 'Weap') {
                    var element = document.getElementById('weap');
                } else if (but.id == 'Stan') {
                    var element = document.getElementById('stan');
                }
                if (but.value == 'reset') {
                    element.innerHTML = 0;
                } else if (but.id != 'test') {
                    element.innerHTML = parseInt(element.innerHTML) + parseInt(but.value);
                }
                if (but.id == 'Weap'){
                    if (element.innerHTML >= 80) {
                        element.innerHTML = 0
                    }
                } else if (but.id != 'test') {
                    if (element.innerHTML >= 90) {
                        element.innerHTML = 0;
                    }
                }
            }
        })
    });

    $('#blessing').on('change', function() {

        $.ajax({
            url: 'blessing/',
            data: {
                csrfmiddlewaretoken: csrfToken,
            },
            type: 'post',
        })
    });

    $('#test').click(function() {
        var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        var primogems = $('#primogems')[0];
        var blessing = $('#blessing')[0];
        console.log(blessing.checked);

    });
});
