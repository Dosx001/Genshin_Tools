$(document).ready(function() {
    $('#createButton').click(function() {
        var serializedData = $('#createTaskForm').serialize();
        console.log(serializedData)

        $.ajax({
            url: $('createTaskForm').data('url'),
            data: serializedData,
            type: 'post',
            success: function(response) {
                $('#task_list').append(
                    '<div class="card mb-1"><div class="card-body">'
                    + response.event.title +
                    '<button type="button" class="close float-right"><span aria-hidden="true">&times;</span></button></div></div>'
                    )
            }
        })
        $('#createTaskForm')[0].reset();
    });
});
