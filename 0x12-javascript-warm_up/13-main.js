#!/usr/bin/node
const add = require('./13-add').add;
console.log('this is the first:  ' + require('./13-main.js') + "          require('./13-main.js')");
console.log('this is the second:  ' + add + "         add")
console.log('this is the third:  ' + add() + "         add()")
console.log('this is the fourth:  ' + add(3, 5) + "                        add(3,5)");
//console.log('this is the fifth:  ' + require() + "          require()");
console.log('this is the sixth:  ' + require + "          require");
