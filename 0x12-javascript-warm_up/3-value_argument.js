#!/usr/bin/node
/* process.argv.length < 3 // ternary operator to check number of arguments
  ? console.log('No argument')
: process.argv.length === 3 ? console.log('Argument found') : console.log('Arguments found');
*/

if (process.argv[2]) {
  console.log(process.argv[2]);
} else { console.log('No argument'); }
