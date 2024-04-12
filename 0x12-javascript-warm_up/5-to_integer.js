#!/usr/bin/node
// A script that prints an arguement converted into an integer.

const args = process.argv.slice(2);

if (isNaN(args[0])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(args)}`);
}
