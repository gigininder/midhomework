from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    X = "資管二A 黃俊翔<br>"
    X += "<a href=/about>我的個人簡介</a><br>"
    X += "<a href=/account>MIS工作內容</a><br>"
    X += "<a href=/welcome>職涯測驗結果</a><br>"
    X += "<a href=/today>求職履歷自傳</a><br>"
    return X

@app.route("/about")
def course():
	return render_template("about.html")

@app.route("/account")
def today():
    return render_template("account.html")

@app.route("/welcome")
def about():
    return render_template("welcome.html")

@app.route("/today")
def welcome():
    return render_template("today.html")

#if __name__ == "__main__":
	#app.run()