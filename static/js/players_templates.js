'use strict';
(function () {
  const playersTemplate = document.querySelector(`#reminderTemplate`).content.querySelector(`tr`);
  const createStroke = (player) => {
    console.log('i am here')
    let stroke = playersTemplate.cloneNode(true);
    let username = stroke.querySelector(`.username`);
    let polls_count = stroke.querySelector(`.polls`);

    username.textContent = player.username;
    username.style.color = player.username_color
    stroke.style.border = "4px solid " + player.username_color
    stroke.style.backgroundColor = '#d1c2f0'
    polls_count.textContent = player.passed_polls;

    return stroke;
  };

  window.blogTemplates = {
    createStroke,
  };
})();