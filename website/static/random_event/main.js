$(document).ready(function() {
    $('.btn').click(function() {
        var serializedData = $('#EventForm').serialize();

        $.ajax({
            url: '',
            data: serializedData,
            type: 'post',
            success: function(response) {
                var element = document.getElementById('num');
                element.innerHTML = --element.innerHTML;
            }
        })
    });
});
