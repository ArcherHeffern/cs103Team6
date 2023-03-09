Steps to get server running: 

1. Create a bash shell
2. cd to ca01
3. Activate virtual env

When first running: 

    If Windows: 
    python -m venv .venv && . .venv/Scripts/activate && pip install -r requirements.txt

    If macos: 
    python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

All subsequent times: 

    If Windows: 
    . .venv/Scripts/activate

    If macos: 
    . .venv/bin/activate

4. Get api key

    visit openai.com and get an APIkey
    create file in ca01 called .env and paste in API_KEY="<yourAPIKey>"
    
Running the app: 

    python server.py