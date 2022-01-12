#!/usr/bin/node
const esrever = (list) => {
  const newList = [];
  for (let i = list.length; i > 0; i--) {
    newList.push(list[i - 1]);
  }
  return newList;
};
module.exports.esrever = esrever;
