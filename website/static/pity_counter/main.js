function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function(){
  $('.btn').click(function(){
    let btn = $(this);
    $.ajax({
      url: '',
      type: 'post',
      data: {
        buttum_text: btn.text(),
        csrfmiddlewaretoken: getCookie('csrftoken');
      }
      success: function(response) {
        btn.text(response.seconds)
      }
    });
  });
});
