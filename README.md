# TaleSmith - Story Generator

TaleSmith is a Python-based AI story generator that creates engaging narratives based on user prompts.

## Features
- Generate stories of different genres
- Configurable via `.env` file
- Easy to set up and run

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/preetkanan/talesmith.git
   ```
2. Navigate to the project folder:
   ```bash
   cd talesmith
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   ```bash
   # Windows
   .\.venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Add your Hugging Face token to `.env`:
   ```text
    HF_TOKEN=your_huggingface_token_here
    NGROK_AUTH_TOKEN=your_ngrok_token_here
   ```

## Usage
```bash
python app.py
```

## Contributing
Feel free to open issues or submit pull requests. Ensure that no secrets are committed to the repository.

## License
MIT License