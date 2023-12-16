// netlify/functions/proxy.js
const fetch = require('node-fetch');

exports.handler = async function (event, context, callback) {
  const targetUrl = 'http://localhost:9000';  // あなたのターゲットURLに置き換えてください
  const requestUrl = event.queryStringParameters.url;

  try {
    const response = await fetch(`${targetUrl}?url=${requestUrl}`, {
      method: 'GET',
      headers: event.headers,
    });

    const data = await response.text();

    callback(null, {
      statusCode: response.status,
      body: data,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  } catch (error) {
    callback(error);
  }
};
