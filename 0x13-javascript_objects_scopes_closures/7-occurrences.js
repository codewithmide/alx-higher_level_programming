#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0; // counter for each value in a list
  for (let i = 0; i < list.length; i++) { // list counter
    if (searchElement === list[i]) { // if each value is the same as the first for loop
      nOccurrences++;// increment the counter
    }
  }
  return nOccurrences;
};
