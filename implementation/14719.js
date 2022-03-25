const fs = require('fs');
const input = fs.readFileSync('../text.txt').toString().split('\n');

const [h, w] = input[0].split(' ').map((v) => parseInt(v));
const blocks = input[1].split(' ').map((v) => parseInt(v));

let max = 0;
let answer = 0;
let stack = [];

for (let i = 0; i < w; i++) {
  if (blocks[i] >= max) {
    stack.forEach((v) => (answer += max - v));
    stack = [];
    max = blocks[i];
    continue;
  }

  if (stack.length && stack[stack.length - 1] < blocks[i]) {
    stack = stack.map((v) => {
      const diff = blocks[i] - v > 0 ? blocks[i] - v : 0;
      answer += diff;
      return v + diff;
    });
  }

  stack.push(blocks[i]);
}

console.log(answer);
