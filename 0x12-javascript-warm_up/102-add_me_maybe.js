#!/usr/bin/node

exports.addMeMaybe = (number, theFunction) => {
  number++;
  console.log(number);
  theFunction(number);
};
