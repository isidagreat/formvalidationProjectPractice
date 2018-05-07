from flask import Flask, render_template, sessions, request, flash, redirect
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ohyeaa"



@app.route("/")
def index():
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def validate():
	print ("Received POST")
	print (request.form)
	if len(request.form["email"]) < 1:
		flash("Email cannot be empty")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash ("invalid Email")
	if request.form["fname"].isalpha() != True:
		flash("Name cannot contain numbers")
		return redirect ("/")
	if len(request.form["fname"]) < 1:
		flash("First Name cannot be empty")
		return redirect("/")
	if len(request.form["lname"]) < 1:
		flash("last Name cannot be empty")
		return redirect("/")
	if request.form["lname"].isalpha() != True:
		flash("Last Name cannot contain numbers")
		return redirect ("/")
	if len(request.form["pword"]) < 8:
		flash("Password should be more than 8 characters")
		return redirect("/")
	if request.form["cword"] != request.form["pword"]:
		flash("passwords do not match")
		return redirect("/")

	flash("Submitted Successfully")
	return redirect("/")	

if __name__ == "__main__":
	app.run(debug=True)