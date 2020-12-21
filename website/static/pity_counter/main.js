$(document).ready(function(){
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    $('.btn').click(function(){
        var but = $(this)[0];
        if (but.id == 'reporter') {
            var primogems = $('input[id="primogems"]').val();
            $.ajax({
                url: 'report/',
                data: {
                    csrfmiddlewaretoken: csrfToken,
                    primogems: primogems,
                    banner: but.value
                },
                type: 'post',
                success: function(response) {
                    $('#report').remove();
                    var report = '' +
                        '<h3 id="report"><b>Time</b>: ' +
                        response.days +
                        ' days <br><b>Date</b>: ' +
                        response.date +
                        '<br><b>Cost</b>: ' +
                        response.primo +
                        ' primogems<br><b>Price</b>: $' +
                        response.price +
                        '</h3>';
                    if (but.value == 'Char') {
                        $('#CharBan').append(report);
                    } else if (but.value == 'Weap') {
                        $('#WeapBan').append(report);
                    } else {
                        $('#StanBan').append(report);
                    }
                }
            })
        } else {
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
                    } else if (but.id != 'report') {
                        element.innerHTML = parseInt(element.innerHTML) + parseInt(but.value);
                    }
                    if (but.id == 'Weap'){
                        if (element.innerHTML >= 80) {
                            element.innerHTML = 0
                        }
                    } else if (but.id != 'report') {
                        if (element.innerHTML >= 90) {
                            element.innerHTML = 0;
                        }
                    }
                }
            })
        }
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
});
