// script that fetches the character name from give URL

let url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (data, stat) {
  $('div#character').text(data.name);
});