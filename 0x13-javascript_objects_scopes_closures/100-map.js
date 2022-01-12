#!/usr/bin/node
const dataFile = require('./100-data.js');
console.log(dataFile.list);
console.log(dataFile.list.map((elem, index) => elem * index));
