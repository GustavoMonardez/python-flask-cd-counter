from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'pass'

@app.route("/", methods=["GET","POST"])
def index():
    if 'count' in session:
        session["count"] +=1
    else:
        session["count"] = 1
   
    print("session count:",session["count"])

    return render_template("index.html", count=session["count"])

@app.route("/destroy_session", methods=["GET", "POST"])
def clear():
    session.clear()
    return redirect("/")

@app.route("/count_by_twos", methods=["GET","POST"])
def count_by_twos():
    session["count"]+=1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)