$(document).ready(function() {
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    $('#createButton').click(function() {
        var serializedData = $('#createTaskForm').serialize();

        $.ajax({
            url: $('createTaskForm').data('url'),
            data: serializedData,
            type: 'post',
            success: function(response) {
                $('#task_list').append(
                    '<div class="card mb-1 id="taskCard" data-id="'
                    + response.task.id +
                    '"><div class="card-body">'
                    + response.task.title +
                    '<button type="button" class="close float-right"><span aria-hidden="true">&times;</span></button></div></div>'
                    )
            }
        })
        $('#createTaskForm')[0].reset();
    });

    $('#task_list').on('click', '.card', function() {
        var dataId = $(this).data('id');
        $.ajax({
            url: dataId + '/completed/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id : dataId
            },
            type: 'post',
            success: function() {
                var cardItem = $('#taskCard[data-id="' + dataId + '"]');
                cardItem.css('text-decoration', 'line-through').hide().slideDown();
                $('#task_list').append(cardItem);
            }
        })
    });
});
