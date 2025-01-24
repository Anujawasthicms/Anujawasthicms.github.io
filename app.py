from flask import Flask, render_template, request

app = Flask(__name__)

# Define the questions for the survey
questions = [
    "How often do you use sustainable transportation?",
    "How often do you reduce meat and eat sustainably?",
    "How often do you use reusable materials?",
    "How often do you adopt sustainable consumption habits?",
    "How often do you conserve water?",
    "How often do you practice proper waste management?",
    "How often do you use energy-efficient practices?"
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the selected scores from the form
        scores = [int(request.form.get(f"q{i}", 0)) for i in range(len(questions))]
        total_score = sum(scores)

        # Calculate the result level
        if total_score <= 10:
            level = "Beginner - Start building sustainable habits."
        elif total_score <= 20:
            level = "Emerging - You're making progress!"
        elif total_score <= 30:
            level = "Proficient - Great adoption of sustainable practices!"
        else:
            level = "Champion - You're a sustainability role model!"

        # Render the results page with the calculated score and level
        return render_template("result.html", total_score=total_score, level=level)

    # Render the main form page
    return render_template("index.html", questions=questions)


if __name__ == "__main__":
    app.run(debug=True)
