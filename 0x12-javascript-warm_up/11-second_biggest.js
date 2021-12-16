#!/usr/bin/node

if (process.argv.length < 3) {
  console.log(0);
} else {
  /*
   * the sort() method used with Numbers is tricky to understand but i think this link will help :)
   *
   * From freecodecamp :
   *   https://forum.freecodecamp.org/t/arr-sort-a-b-a-b-explanation/167677/3
   *
   * From the docs :
   *   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
   *
   * Let me know if you found this useful buddy :) ... Happy Coding :)
   */
  const sortedArray = process.argv.map(Number).sort((a, b) => a - b)
  console.log(sortedArray[sortedArray.length - 2]);
}
