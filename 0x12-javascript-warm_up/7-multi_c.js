#!/usr/bin/node
// A script that prints x times that 'C is Fun'.

const firstArg = process.argv[2];

if (isNaN(Number(firstArg))) {
  console.log("Missing number of occurrences");
} else {
  const numOccurrences = parseInt(firstArg);
  for (let i = 0; i < numOccurrences; i++) {
    console.log("C is fun");
  }
}