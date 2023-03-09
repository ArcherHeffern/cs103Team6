from flask import request,redirect,url_for,Flask, render_template
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('API_KEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    return render_template("index.html")

# TODO:  
# a) an about page which explains what your program does
# b) a "team" page which has a short bio of each member of the team and what their role was
# c) an index page with links to each of the team-members pages

# d) a form page for each team member which ask the user for some input, then calls the appropriate GPT method to get the response, which it sends back to the browser.

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)