from flask import Blueprint, request, jsonify, abort
import json
from services.generative_ai import create_chat_session
from config import Config

bp = Blueprint('routes', __name__)

# Middleware for API authentication based on Authorization header
@bp.before_request
def require_authorization():
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != Config.API_SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401

@bp.route('/grader', methods=['POST'])
def chat():
    user_message = request.json.get('data')
    if not user_message:
        return jsonify({"error": "Data not provided"}), 400

    # Convert user_message from JSON to plain text
    user_message = json.dumps(user_message)

    # Create a chat session using the generative AI service
    chat_session = create_chat_session()
    response = chat_session.send_message(user_message)

    try:
        # Try parsing the response text as JSON
        response_text = json.loads(response.text)
    except json.JSONDecodeError:
        # If parsing fails, return an error
        return jsonify({"error": "Invalid response format from AI service"}), 500

    # Return the parsed JSON response
    final_response = jsonify({"response": response_text})
    return final_response
