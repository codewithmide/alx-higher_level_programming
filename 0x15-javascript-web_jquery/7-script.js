// Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

$(function () {
    
    var character = $('#character');

    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
        success: function(names) {
            $(character).append(names.name);
        }
    })
})