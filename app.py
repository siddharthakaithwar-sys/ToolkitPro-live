from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Taaki frontend se block na ho

# Tumhara naya Nvidia client setup
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_prompt = data.get("prompt", "").strip()
        
        # Agar prompt khali ho toh default bhejenge taaki 400 bad request error na aaye
        if not user_prompt:
            user_prompt = "Hello, check system connection."
            
        # Nvidia OpenAI client call
        completion = client.chat.completions.create(
          model="meta/llama-3.2-3b-instruct",
          messages=[{"role": "user", "content": user_prompt}],
          temperature=0.2,
          top_p=0.7,
          max_tokens=1024,
          stream=False
        )
        
        # AI ka text reply nikalna
        ai_reply = completion.choices[0].message.content
        return jsonify({"response": ai_reply})

    except Exception as e:
        return jsonify({"response": f"Backend Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
