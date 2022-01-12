#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // prints squre with variable c
  charPrint (c) {
    super.print(c);
  }
}
module.exports = Square;
