#!/usr/bin/node
const args = process.argv.slice(2); // No Script name

if (args.length === 0) {
  console.log('No arguement');
} else if (args.length === 1) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
