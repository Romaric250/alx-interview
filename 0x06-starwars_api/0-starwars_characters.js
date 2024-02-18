#!/usr/bin/node
const request = require('request');

function getCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body).name);
    });
  });
}

function getMovieCharacters(movieId) {
  request(`https://swapi.dev/api/films/${movieId}/`, async (error, response, body) => {
    if (error) console.error(error);
    else {
      const characters = JSON.parse(body).characters;
      for (const characterUrl of characters) {
        const name = await getCharacterName(characterUrl);
        console.log(name);
      }
    }
  });
}

const movieId = process.argv[2];
getMovieCharacters(movieId);