// netlify/functions/requestAndCurl.js

const axios = require('axios');

exports.handler = async function (event, context) {
  try {
    const { url } = JSON.parse(event.body);

    if (!url) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'URLを指定してください' }),
      };
    }

    // Google.comへのリクエスト
    const response = await axios.get(url);

    return {
      statusCode: 200,
      body: JSON.stringify({
        command: `curl -X GET ${url}`,
        result: response.data,
      }),
    };
  } catch (error) {
    console.error(error.message);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Internal Server Error' }),
    };
  }
};
