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
                    var report = '<table id="report" class="table table-hover"><tbody>';
                    for (var itr in response) {
                        report += '<tr><th scope="row">' + itr + '</th><td>';
                        if (itr == 'Price') {
                            report += '$'
                        }
                        report += response[itr] + '</td>';
                    }
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
                    } else {
                        element.innerHTML = parseInt(element.innerHTML) + parseInt(but.value);
                    }
                    if (but.id == 'Weap' && element.innerHTML >= 80){
                        element.innerHTML = 0
                    } else if (element.innerHTML >= 90) {
                        element.innerHTML = 0;
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
