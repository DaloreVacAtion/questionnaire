'use strict';
(function () {

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

  const csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  };

  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  $('div.username_settings').find('option').each(function() {
            if ($(this).val() === $('input#username').val()) {
                $(this).attr('selected', true);
            }
        });

  $('div.background_settings').find('option').each(function() {
            if ($(this).val() === $('input#background').val()) {
                $(this).attr('selected', true);
            }
        });

  const successHandler = (data) => {
    window.location.reload()
  };

  const errorHandler = (data) => {
    console.log('Упал в ошибку')
      if (data.status == 402) {
          alert('У вас слишком мало денег!')
      }
  };

  $('.btn-success').on(`click`, function () {

  let username_color = $("#username_color :selected").val()
  let background_color = $("#background_color :selected").val()
  if ((username_color === $('input#username').val()) && (background_color === $('input#background').val())) {
      alert('Выбранные Вами цвета не отличаются от уже имеющихся. Валюта не будет списана.')
      return
  }
    let newData = {
        'username_color': username_color,
        'background_color': background_color
      }
      window.backend.post(`/api/colors/`, successHandler, errorHandler, newData);
    });
})();