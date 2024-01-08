#!/usr/bin/node

const arg1 = process.argv[2];
const x = parseInt(arg1);

if (!isNaN(x)) {
    let i = 0;
    while (i < x)
    {
        console.log('C is fun');
    }
    i++;
}

else {
    console.log('Missing number of occurences');
}