#!/usr/bin/node

const parsedNumber = parseInt(process.argv[2]);
console.log(parsedNumber ? 'My number: ' + process.argv[2] : 'Not a number');
