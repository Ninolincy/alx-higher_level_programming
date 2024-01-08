#!/usr/bin/node

const process = require('process');
const arg = process.argv;

if (arg.length < 4) {
    console.log(0);
}
else {
    console.log(arg.sort().reverse()[1]);
}