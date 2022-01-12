#!/usr/bin/node
const nbOccurences = (list, searchElement) => {
  return list.filter(x => x === searchElement).length;
};
module.exports.nbOccurences = nbOccurences;
