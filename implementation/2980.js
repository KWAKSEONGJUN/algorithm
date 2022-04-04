const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = fs.readFileSync('../text.txt').toString().split('\n');

const L = input[0].split(' ')[1];
let trafficLightStatus = input
  .slice(1)
  .map((v) => v.split(' '))
  .reduce(
    (acc, v) => ({
      ...acc,
      [v[0]]: {
        Rtime: parseInt(v[1]),
        Gtime: parseInt(v[2]),
        waitingTime: 0,
        currentLight: 'R',
      },
    }),
    {}
  );

const runTrafficLight = (trafficLightStatus) =>
  Object.entries(trafficLightStatus).reduce((acc, [key, value]) => {
    const { Rtime, Gtime, waitingTime, currentLight } = value;
    if (currentLight === 'R' && waitingTime >= Rtime) {
      return {
        ...acc,
        [key]: {
          ...value,
          waitingTime: 1,
          currentLight: 'G',
        },
      };
    } else if (currentLight === 'G' && waitingTime >= Gtime) {
      return {
        ...acc,
        [key]: {
          ...value,
          waitingTime: 1,
          currentLight: 'R',
        },
      };
    } else {
      return {
        ...acc,
        [key]: {
          ...value,
          waitingTime: waitingTime + 1,
        },
      };
    }
  }, {});

let time = 0;
let distance = 0;

while (distance < L) {
  trafficLightStatus = runTrafficLight(trafficLightStatus);

  if (trafficLightStatus[distance] === undefined || trafficLightStatus[distance].currentLight === 'G') {
    delete trafficLightStatus[distance];
    distance++;
  }
  time++;
}

console.log(time);
