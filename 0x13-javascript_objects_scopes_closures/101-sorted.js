#!/usr/bin/node
const data = require('./101-data');

const originalDict = data.dict;
const reversedDict = {};

for (const key in originalDict) {
  const occurrences = originalDict[key];

  if (!reversedDict[occurrences]) {
    reversedDict[occurrences] = [];
  }

  reversedDict[occurrences].push(key);
}

console.log(reversedDict);
