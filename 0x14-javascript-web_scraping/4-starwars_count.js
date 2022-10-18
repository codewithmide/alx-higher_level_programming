#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, function (error, results, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const movieData = JSON.parse(body).results;

    for (let i = 0; i < movieData.length; i++) {
      const chart = (movieData[i].characters);
      for (let j = 0; j < chart.length; j++) {
        if (chart[j].includes('https://swapi-api.hbtn.io/api/people/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
