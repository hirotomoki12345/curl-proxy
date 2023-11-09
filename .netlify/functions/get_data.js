// functions/get_data.js
const fetch = require('node-fetch');

exports.handler = async function (event, context) {
  try {
    const data = JSON.parse(event.body);
    const url = data.url;

    // 外部ドメインへのリクエスト
    const response = await fetch(url);
    const result = await response.text();

    return {
      statusCode: 200,
      body: JSON.stringify({ data: result }),
      headers: {
        'Access-Control-Allow-Origin': '*', // これをフロントエンドのオリジンに設定してください
        'Content-Type': 'application/json',
      },
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
      headers: {
        'Access-Control-Allow-Origin': '*', // これをフロントエンドのオリジンに設定してください
        'Content-Type': 'application/json',
      },
    };
  }
};
