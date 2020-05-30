from flask import Flask, render_template, request,session
from flask_session import Session

app = Flask(__name__)
app.debug = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)

@app.route('/' ,methods = ["GET","POST"])
def start():
	if session.get("texts") is None:
		session["texts"] = []
	if request.method == 'POST':
		text = request.form.get("name")
		session["texts"].append(text)

	return render_template("login_page.html",texts = session["texts"]

if __name__ == "__main__":
	app.run()
