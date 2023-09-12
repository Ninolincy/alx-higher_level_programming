#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let nOccurences = 0;
    for (let index = 0; index < list.length; index++) {
        if (searchElement === list[index]) {
            nOccurences++;
        }
    }
    return (nOccurences);
}