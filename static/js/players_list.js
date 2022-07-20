(function() {
 const GET_PLAYERS_URL = `/api/players/`;
 const tablePlayers = document.querySelector(`.custom-table`);
 const tablePlayersBody = tablePlayers.querySelector(`tbody`);
 const strokesFragment = document.createDocumentFragment();
 let copyData = [];
 const renderStrokes = (data) => {
    for (let i = 0; i < data.length; i++) {
      strokesFragment.appendChild(window.blogTemplates.createStroke(data[i]));
    }

    tablePlayersBody.appendChild(strokesFragment);
  };

   const successHandler = (data) => {
       console.log('i am here')
       console.log(data)
    if (data.data.length > 0) {
      document.querySelector('div.players').classList.remove('d-none');
      copyData = data.data.slice();
      renderStrokes(copyData);
    } else {
      document.querySelector(`h2`).insertAdjacentHTML(`afterEnd`, `<p class="h3">Здесь будут отображаться опросы. Если страница пустая, не переживайте. Скорее всего, не было создано ни одного опроса. Посетите эту страницу позже!<p>`);
    }

  };

  const errorHandler = (errorMessage) => {
    console.log(errorMessage);
  };

  const createStrokesFragment = () => {
    window.backend.get(GET_PLAYERS_URL, successHandler, errorHandler);
  };

  createStrokesFragment();

})();