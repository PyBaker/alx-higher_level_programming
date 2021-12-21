exports.callMeMoby = (x, theFunction) => {
  let count = 0;
  while (count < x) {
    theFunction();
    count++;
  }
};
