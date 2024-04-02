from flask import Flask, request, jsonify
from flask_cors import CORS
from logic import Logic
import google.generativeai as genai

app = Flask(__name__)
processor = Logic()
CORS(app)

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    
    try:
        response = processor.generate_prompt(prompt)
        return jsonify({'response': response})
    except genai.types.generation_types.BlockedPromptException as e:
        error_message = f"Sorry, an error occurred. This prompt is identifed as a blocked prompt due to safety concerns. Please try another prompt."
        return jsonify({'error': error_message}), 500

@app.route('/train_model', methods=['POST'])
def train_model():
    try:
        prompt = request.json.get('prompt')
        attribute = request.json.get('attribute')

        print(prompt, attribute)
        processor.train_model(prompt, attribute)

        return jsonify({'message': 'Model retrained successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)