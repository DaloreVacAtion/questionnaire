'use strict';
(function () {

  var ids = window.location.pathname.match(/\/(\d+)+[\/]?/g).map(id => id.replace(/\//g, ''));;

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

  const successHandler = (data) => {
    window.location.href = '/polls/'
  };

  const errorHandler = (data) => {
    console.log('Упал в ошибку')
    console.log(data);
  };

  $('.btn-success').on(`click`, function () {

    let divs = document.querySelectorAll('div.question')
    for (var i = 0; i < divs.length; i++) {
      if (divs[i].querySelectorAll("input:checked").length === 0) {
        alert('Вы не ответили на один из вопросов')
        return
      }
     }

    var questions_ids = [];
    $("input:hidden.question").each(function() {
        questions_ids.push({'question': parseInt($(this).val())});
    });

    var answers_ids = [];
    $("input:checked").each(function() {
        answers_ids.push({'answer_for_question': parseInt($(this).val())});
    });
    let question_data = questions_ids.map((a, i) => Object.assign({}, a, answers_ids[i]))
    let newData = {
        'poll': parseInt(ids[0]),
        'answers': question_data
      }
      window.backend.post(`/api/answers/`, successHandler, errorHandler, newData);
    });
})();