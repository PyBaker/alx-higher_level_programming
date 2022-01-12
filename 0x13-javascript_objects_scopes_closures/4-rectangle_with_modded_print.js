#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w && h) > 0) {
      this.width = Number(w);
      this.height = Number(h);
    }
  }

  // prints shape using 'X' string
  print (letter) {
    if (letter == undefined) letter = 'X' 
    const count = [...Array(this.height).keys()];
    // for (let i in count)
    for (let i = 0; i < count.length; i++) {
      console.log(letter.repeat(this.width));
    }
  }

  // rotates shape switching height and width
  rotate () {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // multiplies width and height of rectangle by 2
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
