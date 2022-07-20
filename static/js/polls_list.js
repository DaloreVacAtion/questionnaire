(function() {
 const GET_POLLS_URL = `/api/polls/`;
 const tablePolls = document.querySelector(`.custom-table`);
 const tablePollsBody = tablePolls.querySelector(`tbody`);
 const strokesFragment = document.createDocumentFragment();
 let copyData = [];
 const renderStrokes = (data) => {
    for (let i = 0; i < data.length; i++) {
      strokesFragment.appendChild(window.blogTemplates.createStroke(data[i]));
    }

    tablePollsBody.appendChild(strokesFragment);
  };

   const successHandler = (data) => {
       console.log('i am here')
       console.log(data)
    if (data.data.length > 0) {
      document.querySelector('div.polls').classList.remove('d-none');
      copyData = data.data.slice();
      renderStrokes(copyData);
    } else {
      document.querySelector(`h2`).insertAdjacentHTML(`afterEnd`, `<p class="h3">Здесь будет список пользователей!<p>`);
    }

  };

  const errorHandler = (errorMessage) => {
    console.log(errorMessage);
  };

  const createStrokesFragment = () => {
    window.backend.get(GET_POLLS_URL, successHandler, errorHandler);
  };

  createStrokesFragment();

})();