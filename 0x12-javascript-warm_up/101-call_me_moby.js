#!/usr/bin/node

function executeXtimes(x, theFunction) {
    let i = 0;
    while (i < x) {
        theFunction();
    }i++;
}
module.exports = executeXtimes;