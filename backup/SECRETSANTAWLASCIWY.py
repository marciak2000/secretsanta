from flask import Flask, render_template, request

import random

app = Flask(__name__)
app.secret_key = "secretsanta2023"

# Lists of names for gift givers and recipients
gift_givers = ["Marta", "Julia", "Nena", "Gocha", "Kacha", "Ala", "Michał", "Karola", "Jan", "Asia", "Kuba T.", "Kuba P.", "Marca", "Werka"]
recipients = ["Marta", "Julia", "Nena", "Gocha", "Kacha", "Ala", "Michał", "Karola", "Jan", "Asia", "Kuba T.", "Kuba P.", "Marca", "Werka"]

# Secret Santa assignments
assignments = {}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the selected name
        selected_name = request.form["name"]

        # Check if the person has already been assigned a recipient
        if selected_name in assignments:
            recipient = assignments[selected_name]
        else:
            # Choose a random recipient
            remaining_recipients = set(recipients) - set(assignments.values())
            remaining_recipients.discard(selected_name)

            if remaining_recipients:
                recipient = random.choice(list(remaining_recipients))
                # Save the assignment
                assignments[selected_name] = recipient
                # Remove the assigned recipient from the pool
                recipients.remove(recipient)
            else:
                # Handle the case where there are no available recipients
                return render_template("result.html", selected_name=selected_name, recipient="No available recipients")

        return render_template("result.html", selected_name=selected_name, recipient=recipient)

    return render_template("index.html", names=gift_givers, reset_link="/reset")

@app.route("/reset")
def reset():
    global recipients, assignments
    recipients = ["Marta", "Julia", "Nena", "Gocha", "Kacha", "Ala", "Michał", "Karola", "Jan", "Asia", "Kuba T.", "Kuba P.", "Marca", "Werka"]
    assignments = {}
    return render_template("result.html", reset_message="Data has been reset. You can now run the Secret Santa process again.")

if __name__ == "__main__":
    app.run(debug=True)