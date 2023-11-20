from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "secretsanta2023"

# List of names
names = ["Marta", "Julia", "Nena", "Gocha", "Kacha", "Ala", "Michał", "Karola", "Jan", "Asia", "Kuba T.", "Kuba P.", "Marca", "Werka"]

# Secret Santa assignments
assignments = {}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the selected name
        selected_name = request.form["name"]

        # Choose a random recipient
        remaining_names = [name for name in names if name != selected_name]
        recipient = random.choice(remaining_names)

        # Save the assignment
        assignments[selected_name] = recipient

        # Remove the assigned recipient from the pool
        names.remove(recipient)

        return render_template("result.html", selected_name=selected_name, recipient=recipient)

    return render_template("index.html", names=names, reset_link="/reset")

@app.route("/reset")
def reset():
    global names, assignments
    names = ["Marta", "Julia", "Nena", "Gocha", "Kacha", "Ala", "Michał", "Karola", "Jan", "Asia", "Kuba T.", "Kuba P.", "Marca", "Werka"]
    assignments = {}
    return render_template("result.html", reset_message="Data has been reset. You can now run the Secret Santa process again.")


if __name__ == "__main__":
    app.run(debug=True)