#!/usr/bin/node
const args = process.argv.slice(2); // All arguements

if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
