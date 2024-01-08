#!/usr/bin/node

function incrementAndCall(number, theFunction) {
    const incrementAndCall = number + 1;
    theFunction(incrementAndCall);
}
module.exports = incrementAndCall;