#!/usr/bin/node

const result = Number(process.argv[2]);
if (isNaN(result)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < result; i++) {
    console.log(('X').repeat(result));
  }
}
