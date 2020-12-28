$(document).ready(function() {
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    $('#ControlSelect').change(function() {
        var selection = $(this)[0].value;
        var element = document.getElementById('label');
        $('#usr_info').remove();
        if (selection == 'Domain of Mastery') {
            $('#5').remove();
            $('#extra').remove();
            $('#5star').remove();
            element.innerHTML = 'Adventure Rank'
            $('#Activity').append('<select class="form-control" id="usr_info">' +
                '<option>27</option><option>28 to 35</option>' +
                '<option>36 to 44</option><option>+45</option>'
            )
        }
        else if (selection == 'World Boss') {
            element.innerHTML = 'World Level';
            var section = '<select class="form-control" id="usr_info">';
            for (i = 0; i < 9; i++) {
                section += '<option>' + i + '</option>';
            }
            $('#Activity').append(section);
        }
        else {
            element.innerHTML = 'Adventure Rank';
            $('#Activity').append('<select class="form-control" id="usr_info">' +
                '<option>16 to 20</option><option>21 to 29</option>' +
                '<option>30 to 39</option><option>+40</option>'
            )
        }
        if (selection != 'Domain of Mastery' && $('#5')[0] == null) {
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
                usr_info: $('#usr_info')[0].value,
                data: JSON.stringify(request_data)
            },
            success: function(response) {
                $('#report').remove();
                if (response == true) {
                    var report = '<div id="report" align="center"><h1>' +
                        'Congratulations Traveler! You\'re done.</h1>' +
                        '<img align="center" src="/media/resource_converter/done.png">';
                } else {
                    var report = '<table id="report" class="table table-hover">' +
                        '<thead><tr><th sscpoe="col">Drops</th><th sscpoe="col">Runs</th>' +
                        '<th sscpoe="col">Resin</th><th sscpoe="col">Days</th></thead><tbody>';
                    for (var object in response) {
                        report += '<tr>';
                        for (var item in response[object]) {
                            report += '<td>' + response[object][item] + '</td>';
                        }
                        report += '</tr>';
                    }
                }
                $('form').append(report);
            }
        })
    });
});
