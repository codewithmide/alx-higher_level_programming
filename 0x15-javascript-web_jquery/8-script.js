#!/usr/bin/node
// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (const result of data.results) {
    $('UL#list_movies').append('<li>' + result.title + '</li>');
  }
});