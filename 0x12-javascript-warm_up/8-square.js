#!/usr/bin/node
const result = Number(process.argv[2]);
if (isNaN(result)) {
  console.log('Missing size');
} else {
  // let [i,j] = [0,0] // initialising counters

  for (let i = 0; i < result; i++) {
    console.log(('X').repeat(result));
  }
}
//  for(let i = 0;i < result;i++)
