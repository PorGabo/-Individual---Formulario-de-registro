from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/profile_data", methods=["POST"])
def login():
	a = request.form.get("nombre")
	b = request.form.get("apellido")
	age = request.form.get("edad")
	country = request.form.get ("nacionalidad")
	occupation = request.form.get("ocupacion")
	phone = request.form.get("celular")
	email = request.form.get("correo")
	return render_template(
		"session.html",
		name=a,
		lastname=b,
		age=age,
		country=country,
		occupation=occupation,
		phone=phone,
		email=email,
		)

@app.route("/<string:name>")
def session(name):
	return render_template(
		"session.html",
		name=name,
		)


@app.route("/users")
def names():
	# Query a DB for users.
	name_list = ["Jose", "Pedro", "Maria", "Luis"]
	return render_template(
		"list.html",
		nombres=name_list,
	)
