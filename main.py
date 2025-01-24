from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def sustainability_score():
    if request.method == "POST":
        # Collect scores from the form
        scores = [int(request.form.get(f"q{i}", 0)) for i in range(1, 8)]
        total_score = sum(scores)

        # Determine the result based on the score
        if total_score <= 10:
            result = "Beginner - Start building sustainable habits."
        elif total_score <= 20:
            result = "Emerging - You're making progress!"
        elif total_score <= 30:
            result = "Proficient - Great adoption of sustainable practices!"
        else:
            result = "Champion - You're a sustainability role model!"

        return render_template("result.html", total_score=total_score, result=result)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
