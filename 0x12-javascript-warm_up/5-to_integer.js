#!/usr/bin/node

const arg1 = process.argv[2];

if (!isNotNum(arg1) && Number.isInteger(parseFloat(arg1))) {
  console.log(`My number: ${parseInt(arg1)}`);
} else {
  console.log('Not a number');
}