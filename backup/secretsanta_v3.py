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
        remaining_recipients = set(names) - set(assignments.values())
        remaining_recipients.discard(selected_name)

        if remaining_recipients:
            recipient = random.choice(list(remaining_recipients))
            # Save the assignment
            assignments[selected_name] = recipient
            # Remove the assigned recipient from the pool
            names.remove(recipient)
        else:
            # Handle the case where there are no available recipients
            if selected_name in assignments:
                return render_template("result.html", selected_name=selected_name, recipient=assignments[selected_name])
            else:
                return render_template("result.html", selected_name=selected_name, recipient="No available recipients")

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