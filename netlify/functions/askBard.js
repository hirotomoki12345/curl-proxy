// netlify/functions/askBard.js
const { BardAPI } = require('bard-api-node');

exports.handler = async function (event, context) {
  try {
    const assistant = new BardAPI();

    // Set session information for authentication
    assistant.setSession(process.env.BARD_SESSION_NAME, process.env.BARD_SESSION_TOKEN);

    // Get the question from the request body
    const requestBody = JSON.parse(event.body);
    const question = requestBody.question;

    // Send a query to Bard
    const response = await assistant.getBardResponse(question);

    // Return the Bard response
    return {
      statusCode: 200,
      body: JSON.stringify({ response: response.content }),
    };
  } catch (error) {
    // Handle errors
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};
