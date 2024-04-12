#!/usr/bin/node
// A script that prints x times that 'C is Fun'.

const args = process.argv.slice(2);
const x = parseInt(args[0]); // Converting to Integer

if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
