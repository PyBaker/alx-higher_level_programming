#!/usr/bin/node
let counter = 0;
const functionForLogging = function (argument) {
  // or more simply console.log("%d: %s", counter, argument);
  console.log(`${counter}: ${argument}`);
  counter++;
};
module.exports.logMe = functionForLogging;
