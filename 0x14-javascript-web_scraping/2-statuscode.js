#!/usr/bin/node
const axios = require('axios');
async function makeHeadRequest () {
  try {
    const res = await axios.head(process.argv[2]);
    console.log(`code: ${res.status}`);
  } catch (err) {
    console.log('code:', err.response.status);
  }
}
makeHeadRequest();
