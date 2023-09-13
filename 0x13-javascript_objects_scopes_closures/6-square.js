#!/usr/bin/node

const BaseSquare = require('./5-square');

class square extends BaseSquare {
    charPrint (c) {
        if (c === undefined) {
            c = 'X';
        }
        for (let index = 0; index < this.height; index++) {
            let row = '';
            for (let j = 0; j < this.width; j++) {
                row += 'x';            
            }
            console.log(row);
        
    }
    }
}

module.exports = Square;