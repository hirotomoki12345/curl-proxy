const { get_bard_answer } = require('./get_answer.py');

exports.handler = async function (event, context) {
  try {
    const question = event.queryStringParameters.question;
    const answer = await get_bard_answer(question);

    return {
      statusCode: 200,
      body: JSON.stringify({ answer }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};
