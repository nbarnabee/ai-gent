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

Also note that YOU SHOULD PROBABLY NOT RANDOMLY DOWNLOAD AND USE THIS


## Migrating to uv  

New package management, oooh.  (I hardly use Python and this is... what.. the third package manager I've tried?)

1. Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`

2. Initialize it in your project: `uv init` (This will create the files pyproject.toml, .python-version, a blank README.md, and git if it wasn't already)
    
3. Create a new virtual environment: `uv venv` (This will create a hidden directory: .venv. It will not conflict with your current venv directory)

4. Initialize the correct virtual environment: `source .venv/bin/activate`
    
5. Add dependencies: `uv add -r requirements.txt` (This installs deps and creates a uv.lock file)
    
6. Now it is safe to remove the old virtual environment (venv) and the requirements.txt file: `rm -rf venv && rm requirements.txt`


For more information, see [the UV documentation](https://docs.astral.sh/uv/guides/projects/#pyprojecttoml)