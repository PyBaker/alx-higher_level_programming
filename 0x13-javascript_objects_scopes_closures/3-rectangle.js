#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w && h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const count = [...Array(this.height).keys()];
    // for (let i in count)
    for (let i = 0; i < count.length; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
