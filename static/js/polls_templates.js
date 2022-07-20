'use strict';
(function () {
  const pollTemplate = document.querySelector(`#reminderTemplate`).content.querySelector(`tr`);
  const createStroke = (poll) => {
    console.log('i am here')
    let stroke = pollTemplate.cloneNode(true);
    let title = stroke.querySelector(`.title`);
    let date = stroke.querySelector(`.date`);
    let gain = stroke.querySelector(`.gain`);
    let showMoreBtn = stroke.querySelector(`.show-more`);

    title.textContent = poll.title;
    gain.textContent = poll.gain;
    date.textContent = poll.created_at;
    showMoreBtn.href = poll.url;

    stroke.style.backgroundColor = poll.has_gain ? '#98ff98' : '#DCDCDC'

    return stroke;
  };

  window.blogTemplates = {
    createStroke,
  };
})();