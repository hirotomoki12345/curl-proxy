// netlify_functions/answerQuestion.js

const axios = require('axios');

exports.handler = async function (event, context) {
  try {
    const question = event.queryStringParameters.question;
    const token = 'cQi2uJoenm91t7F3tZO7qet54AK-zydIxB6FufuGH3UDZbwSPdf3n5ZTvMcUC65zHZZrRA.'; // Bard APIのトークンを設定
    const response = await axios.get(`https://api.bardapi.com/ask?q=${encodeURIComponent(question)}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const answer = response.data.content;

    return {
      statusCode: 200,
      body: JSON.stringify({ answer }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Internal Server Error' }),
    };
  }
};
