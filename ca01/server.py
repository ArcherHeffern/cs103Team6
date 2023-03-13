from flask import request,redirect,url_for,Flask, render_template, abort
from gpt import GPT
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
gptAPI = GPT(os.environ.get('API_KEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to all querys '''
    return render_template("index.html")

@app.route('/about')
def about():
    """An about page describing the project"""
    return render_template('about.html')

@app.route('/team')
def team():
    """a "team" page which has a short bio of each member of the team and what their role was"""
    return render_template('team.html')

"""Form page for each team member which ask the user for some input, then calls the appropriate GPT method to get the response, which it sends back to the browser."""

@app.route('/archer', methods=["GET", "POST"])
def archer():
    if request.method == 'GET':
        return render_template("form.html", name="Archer", prompt="Write a story about a superhero whose power is to turn into a __ whenever they sneeze.", route="/archer")
    elif request.method == "POST":
        return gptAPI.archers_prompt(request.form['prompt'])
    else:
        abort(405)


@app.route('/efren', methods=['GET', 'POST'])
def efren():
    if request.method == 'GET':
        return render_template("form.html", name='Efren', prompt="what is your prompt efren?", route='/efren')
    elif request.method == 'POST':
        return gptAPI.efren_prompt(request.form['prompt'])
    else:
        abort(405)

# @app.route('/paras', methods=["GET", "POST"])
# def paras():
#     pass

# @app.route('/samir', methods=["GET", "POST"])
# def paras():
#     pass

# @app.route('/kelden', methods=["GET", "POST"])
# def paras():
#     pass

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
