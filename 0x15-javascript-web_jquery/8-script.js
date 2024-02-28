#!/usr/bin/node

$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    var movies = data.results;
    var list = $('<ul id="list_movies"></ul>');
    
    movies.forEach(function(movie) {
      var title = $('<li></li>').text(movie.title);
      list.append(title);
    });
    
    $('body').append(list);
  });
});
