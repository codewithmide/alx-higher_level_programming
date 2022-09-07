#!/usr/bin/node
let counter = 0;

exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
