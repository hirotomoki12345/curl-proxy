// Netlify Functions
exports.handler = async function (event, context) {
  const { url } = JSON.parse(event.body);

  try {
    // fetchを使用して指定されたURLからデータを取得
    const response = await fetch(url);
    const data = await response.text();
    
    return {
      statusCode: 200,
      body: JSON.stringify({ data }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: `Error fetching data: ${error.message}` }),
    };
  }
};
