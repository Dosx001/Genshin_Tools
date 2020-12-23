$(document).ready(function() {
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    $('select').change(function() {
        var selection = $(this)[0].value;
        if (selection == 'Domain of Mastery') {
            $('#5').remove();
            $('#extra').remove();
        } else if ($('#5')[0] == null) {
            $('#Materials').append('<div class="input-group-prepend" id="extra">' +
                '<span class="input-group-text">5&nbsp;' +
                '<img src="/media/resource_converter/star.png"></span></div>' +
                '<input type="number" class="form-control" id="5" value="0">');
        }
    });

    $('button').click(function() {
        var selection = $('#ControlSelect')[0].value;
        request_data = {
            activity: selection,
            materials: {
                star2: $('input[id=2]')[0].value,
                star3: $('input[id=3]')[0].value,
                star4: $('input[id=4]')[0].value
            }
        }
        if (selection != 'Domain of Mastery') {
            request_data.materials.star5 = $('input[id=5]')[0].value;
        }
        $.ajax({
            url: '',
            type: 'post',
            data: {
                csrfmiddlewaretoken: csrfToken,
                data: JSON.stringify(request_data)
            }
        })
    });
});
