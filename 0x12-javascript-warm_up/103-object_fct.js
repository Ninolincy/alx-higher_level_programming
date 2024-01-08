#!/usr/bin/node

function incr (number) {
    return number + 1;
  }
  
  function incrementAndCall(number, theFunction) {
    const incrementedNumber = incr(number);
    theFunction(incrementedNumber);
}
module.exports = {
    incr,
    incrementAndCall,
};
