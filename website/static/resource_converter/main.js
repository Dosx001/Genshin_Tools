$(document).ready(function() {
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    $('#ControlSelect').change(function() {
        var selection = $(this)[0].value;
        if (selection == 'Domain of Mastery') {
            $('#5').remove();
            $('#extra').remove();
            $('#5star').remove();
        } else if ($('#5')[0] == null) {
            $('#Materials').append('<div class="input-group-prepend" id="extra">' +
                '<span class="input-group-text">5&nbsp;' +
                '<img src="/media/resource_converter/star.png"></span></div>' +
                '<input type="number" class="form-control" id="5" value="0">');
            $('#rarity').append('<option id="5star">5</option>');
        }
    });

    $('button').click(function() {
        var selection = $('#ControlSelect')[0].value;
        request_data = {
            rarity: parseInt($('#rarity')[0].value),
            goal: parseInt($('#goal')[0].value),
            materials: {
                star2: parseInt($('input[id=2]')[0].value),
                star3: parseInt($('input[id=3]')[0].value),
                star4: parseInt($('input[id=4]')[0].value)
            }
        }
        if (selection != 'Domain of Mastery') {
            request_data.materials.star5 = parseInt($('input[id=5]')[0].value);
        }
        $.ajax({
            url: '',
            type: 'post',
            data: {
                csrfmiddlewaretoken: csrfToken,
                activity: selection,
                adv_rank: $('#adv_rank')[0].value,
                data: JSON.stringify(request_data)
            },
            success: function(response) {
                $('#report').remove;
                for (var object in response) {
                    for (var item in response[object]) {
                        console.log(item, response[object][item]);
                    }
                }
            }
        })
    });
});
