from flask import Flask, request, jsonify, render_template
from huggingface_hub import InferenceClient
from pyngrok import ngrok
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configuration
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

# Initialize Flask app
app = Flask(__name__)

# Initialize Hugging Face client
client = InferenceClient(model=MODEL_ID, token=HUGGINGFACE_API_KEY)


@app.route("/")
def index():
    """Render the homepage."""
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    """Generate a story from the given user prompt."""
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt.strip():
        return jsonify({"error": "Prompt cannot be empty"}), 400

    try:
        response = client.chat_completion(
            model=MODEL_ID,
            messages=[
                {
                    "role": "system",
                    "content": (
                        """
                        You are a creative story generator.
                        Write engaging, imaginative stories with a clear beginning, middle, and end.
                        If the token budget is low, summarize and close the story gracefully.
                        """
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=800,
            temperature=0.8,
            top_p=0.9,
        )

        story = response.choices[0].message["content"]
        return jsonify({"generated_text": story})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Start ngrok tunnel
    if NGROK_AUTH_TOKEN:
        ngrok.set_auth_token(NGROK_AUTH_TOKEN)
        public_url = ngrok.connect(5000)
        print("Public URL:", public_url)

    # Run Flask app
    app.run(host="0.0.0.0", port=5000)
