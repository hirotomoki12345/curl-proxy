const fetch = require('node-fetch');

exports.handler = async function(event, context) {
    const { url } = event.queryStringParameters;
    try {
        const response = await fetch(url);
        if (response.ok) {
            const content = await response.text();
            return {
                statusCode: 200,
                body: content
            };
        } else {
            return {
                statusCode: response.status,
                body: `Failed to fetch the URL. Status code: ${response.status}`
            };
        }
    } catch (error) {
        return {
            statusCode: 500,
            body: `An error occurred: ${error.message}`
        };
    }
};
