# ai-gent
A helpful (toy) AI agent


Setup:    
1. create a simple virtual environment with `python3 -m venv venv`
2. initialize said venv with `source venv/bin/activate`
3. install requirements with `pip install -r requirements.txt`
4. generate an API key to use with Google Gemini and enter it into an .env file as GEMINI_API_KEY

Usage:  

`python3 main.py <PROMPT>`
  
Also accepts the `--verbose` flag, which will print the initial prompt and token information.
