#!/usr/bin/node
// const dataFile = require('./101-data.js');j

npm install lodash --save
// console.log(dataFile.dict)
const _ = require("lodash");
let myDict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
};

const grouped = _.groupBy(myDict, Array(myDict).keys());
console.log(grouped);
