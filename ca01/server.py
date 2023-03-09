from flask import request,redirect,url_for,Flask, render_template, abort
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

@app.route('/api/archer', methods=["GET", "POST"])
def archer():
    if request.method == 'GET':
        return render_template("form.html", name="Archer", prompt="Write a story about a superhero whose power is to turn into a __ whenever they sneeze.", route="/api/archer")
    elif request.method == "POST":
        return gptAPI.archers_prompt(request.form['prompt'])
    else:
        abort(405)
# TODO:  
# a) an about page which explains what your program does

@app.route('/about')
def about():



# b) a "team" page which has a short bio of each member of the team and what their role was
@app.route('/team')
def team():
    

# c) an index page with links to each of the team-members pages
@app.route('/index')
def index():
    

# d) a form page for each team member which ask the user for some input, then calls the appropriate GPT method to get the response, which it sends back to the browser.

@app.route('/api/efren', methods=['GET', 'POST'])
def efren():
    if method == 'GET':
        return render_template("index.html", )
    elif method == 'POST':
        prompt = request.form[inp]
        gptAPI.efren_prompt(prompt)
        return render_template("index.html",)
    else:
        return 'unknown HTTP method: '+str(request.method)


if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
