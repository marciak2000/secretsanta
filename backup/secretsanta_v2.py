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
        selected_name = request.form["name"]

        # Check if the person has already generated a recipient in this round
        if selected_name in assignments:
            recipient = assignments[selected_name]
        else:
            # Generate a recipient, making sure it's not the same person
            remaining_names = set(names) - set(assignments.values())
            remaining_names.remove(selected_name)  # Remove the current person from potential recipients
            recipient = random.choice(list(remaining_names))

            # Update assignments
            assignments[selected_name] = recipient

        return render_template("result.html", selected_name=selected_name, recipient=recipient)

    return render_template("index.html", names=names, reset_link="/reset", result_link="/result")

@app.route("/reset")
def reset():
    global names, assignments
    names = ["Marta", "Julia", "Nena", "Gocha", "Kacha", "Ala", "Michał", "Karola", "Jan", "Asia", "Kuba T.", "Kuba P.", "Marca", "Werka"]
    assignments = {}
    return render_template("result.html", reset_message="Data has been reset. You can now run the Secret Santa process again.")


if __name__ == "__main__":
    app.run(debug=True)