#!/usr/bin/node

/* You could write the code as seen below

if (process.argv[2]) {
  console.log(process.argv[2]);
} else { console.log('No argument'); }

*/

console.log(process.argv[2] ? process.argv[2] : 'No argument');
