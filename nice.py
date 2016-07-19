from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

JANKS = ["Yo momma so fat, she beeps when she backs up.", "Yo momma so old, she babysat Grace Hopper.",
         "Yo momma so ugly, when she tried to join an ugly contest, they said, 'Sorry, no professionals.'"]

@app.route('/')
def start_here():
    """Home page."""

    return """Hi! This is the home page. <a href="/hello">Click here!</a>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br>
          <label>
          Select a compliment:
            <select name="compliment-type">
              <label><option value="smart">Smart</option></label>
              <label><option value="awesome">Awesome</option></label>
            </select></label>
          <input type="submit">
        </form>

        <form action="/diss">
        <input type="submit" value="Click here for the harshest insult of your life.">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment-type")

    #new_string = "Thank you for using flask."

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, %s, I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def insult_person():

    diss = choice(JANKS)

    return """
    <!doctype html>
    <html>
      <head>
      </head>
      <body>

      <span style="font-size:72pt;font-family:sans-serif;">%s</span>

      </body>
      </html>""" % diss

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
