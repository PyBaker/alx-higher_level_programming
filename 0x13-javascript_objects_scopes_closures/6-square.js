#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // prints squre with variable c
  charPrint (c) {
    if (c === undefined) c = 'X';
    const count = [...Array(this.height).keys()];
    // for (let i in count)
    for (let i = 0; i < count.length; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
