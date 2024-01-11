#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the constructor of the base class (Rectangle) with the size argument for both width and height
  }
}

module.exports = Square;
