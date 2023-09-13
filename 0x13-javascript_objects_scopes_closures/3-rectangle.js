#!/usr/bin/node

class Rectangle {
    constructor(w, h){
        if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            return {};
            
         }
        this.width = w;
        this.height = h;
    }
}

print() {
    for (let index = 0; index < this.height; index++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
            row += 'x';            
        }
        console.log(row);
        
    }
}

module.exports = Rectangle;