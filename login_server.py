from flask import Flask, request, render_template, redirect, url_for
app =Flask(__name__)


users_database = {
    "Ransford" : "August52003.",
    "Randy" : "Qiitoboykingjr"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users_database and users_database[username] == password:
            return render_template("homepage.html")
        else:
            return render_template("errorpage.html")


    return render_template("login.html")

#@app.route("/success")
#def success():
 #   return "Login successful!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4443)