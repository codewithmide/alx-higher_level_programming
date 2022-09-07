#!/usr/bin/node
const { dict } = require('./101-data');

const myValue = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = acc[value] ? [...acc[value], key] : [key];
  return acc;
}, {});
console.log(myValue);
