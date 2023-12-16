// netlify/functions/fetchData.js
const fetch = require('node-fetch');

exports.handler = async function (event, context) {
  try {
    // フロントエンドから送信されたURLを取得
    const { url } = JSON.parse(event.body);

    // 外部のURLからデータをフェッチ
    const response = await fetch(url);
    const data = await response.json();

    // データを返す
    return {
      statusCode: 200,
      body: JSON.stringify(data),
    };
  } catch (error) {
    // エラーが発生した場合はエラーレスポンスを返す
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Internal Server Error' }),
    };
  }
};
