#!/usr/bin/node

exports.addMyMaybe = (number, theFunction) => {
  number++;
  theFunction(number);
};
