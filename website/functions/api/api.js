// Netlify Function for API
exports.handler = async function(event, context) {
  return {
    statusCode: 200,
    body: JSON.stringify({ message: "MasterQuiz Bot API endpoint" })
  };
};