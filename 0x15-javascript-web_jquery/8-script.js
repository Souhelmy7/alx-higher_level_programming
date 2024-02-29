$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      data.results.forEach(function (movies) {
        $('#list_movies').append('<li>' + movies.title + '</li>');
      });
    }
  });
});
