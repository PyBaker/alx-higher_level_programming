#!/usr/bin/node

exports.callMeMoby = (x, theFunction) => {
  //just for control
  let count = 0;
  while (count < x) {
    theFunction();
    count++;
  }
};

