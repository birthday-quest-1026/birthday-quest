from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Questions (like your JS list)
questions = [
    {"q": "What has to be broken before you can use it?", "a": "egg"},
    {"q": "I’m tall when I’m young, and short when I’m old. What am I?", "a": "candle"}
]

@app.route("/", methods=["GET", "POST"])
def game():
    # Track which question we're on using ?id=0, ?id=1 in the URL
    qid = int(request.args.get("id", 0))

    if qid >= len(questions):
        return render_template("end.html")

    question = questions[qid]
    message = ""

    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        if user_answer == question["a"]:
            return redirect(url_for("game", id=qid + 1))
        else:
            message = "❌ Wrong answer, try again!"

    return render_template("question.html", question=question["q"], message=message)

if __name__ == "__main__":
    app.run(debug=True)
