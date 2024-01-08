#!/usr/bin/node

const arg1 = process.argv[2];

const size = parseInt(arg1);

if(!isNaN(size)) {
    for (let i = 0; i < size; i++) {
        let row = '';
        for (let j = 0; j < size; j++) {
            row += 'X';
        }
        console.log(row);
    }
}
else {
    console.log('Missing size')
}