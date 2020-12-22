$(document).ready(function() {
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    $('select').change(function() {
        var selection = $(this)[0].value;
        if (selection == 'Domain of Mastery') {
            $('#5').remove();
            $('#extra').remove();
        } else if ($('#5')[0] == null) {
            $('.input-group').append('<div class="input-group-prepend" id="extra">' +
                '<span class="input-group-text">5&nbsp;' +
                '<img src="/media/resource_converter/star.png"></span></div>' +
                '<input type="number" class="form-control" id="5" value="0">');
        }
    });

    $('button').click(function() {
        var test = $('#ControlSelect')[0];
        console.log(test.value);
    });
});
