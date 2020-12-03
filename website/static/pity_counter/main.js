$(document).ready(function(){
    $('.btn').click(function(){
        var but = $(this)[0];
        var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

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
                } else {
                    var element = document.getElementById('stan');
                }
                if (but.value == 'reset') {
                    element.innerHTML = 0;
                } else {
                    element.innerHTML = parseInt(element.innerHTML) + parseInt(but.value);
                }
                if (but.id == 'Stan'){
                    if (element.innerHTML >= 80){
                        element.innerHTML = 0
                    }
                } else {
                    if (element.innerHTML >= 90) {
                        element.innerHTML = 0;
                    }
                }
            }
        })
    });
});
