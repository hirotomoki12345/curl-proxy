// netlify/functions/proxy.js
const fetch = require('node-fetch');

exports.handler = async function (event, context) {
  const targetUrl = 'http://localhost:9000';  // あなたのターゲットURLに置き換えてください
  const requestUrl = event.queryStringParameters.url;

  try {
    const response = await fetch(`${targetUrl}?url=${requestUrl}`, {
      method: 'GET',
      headers: event.headers,
    });

    const data = await response.text();

    return {
      statusCode: response.status,
      body: JSON.stringify({ data }),
      headers: {
        'Content-Type': 'application/json',
      },
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
      headers: {
        'Content-Type': 'application/json',
      },
    };
  }
};
