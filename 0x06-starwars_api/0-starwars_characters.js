#!/usr/bin/node

const request = require('request');
const Id = process.argv[2];
const Endpoint = `https://swapi.dev/api/films/${Id}/`;

function makeRequest (charactList, index) {
  if (charactList.length === index) {
    return;
  }

  request(charactList[index], (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log(JSON.parse(body).name);
      makeRequest(charactList, index + 1);
    }
  });
}

request(Endpoint, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const characters = JSON.parse(body).characters;

    makeRequest(characters, 0);
  }
});
