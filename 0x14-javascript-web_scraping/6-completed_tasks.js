#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');
const myArgs = process.argv.slice(2);
const result = {};
request(myArgs[0], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const JSONbody = JSON.parse(body);
    let i = 0;
    for (i = 0; i < JSONbody.length; i++) {
      if (!(JSONbody[i].userId in result)) {
        result[JSONbody[i].userId] = 0;
      }
      if (JSONbody[i].completed) {
        result[JSONbody[i].userId] += 1;
      }
      if (result[JSONbody[i].userId] === 0) {
        delete result[JSONbody[i].userId];
      }
    }
    console.log(result);
  }
});
