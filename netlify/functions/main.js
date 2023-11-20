// functions/main.js
exports.handler = async function (event, context) {
  try {
    const { question } = JSON.parse(event.body);
    const answer = `You asked: ${question}. This is a placeholder answer.`;

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
