from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the pipeline with the correct model identifier
chatbot = pipeline("text-generation", model="gpt2")

@app.route('/get_advice', methods=['POST'])
def get_advice():
    question = request.json['question']
    response = chatbot(question, max_length=50, num_return_sequences=1)
    return jsonify({"response": response[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
