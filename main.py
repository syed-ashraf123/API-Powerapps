from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/<variable>')
def profile(variable):
	return variable
@app.route('/')
def profile1():
	return "OK Request coming"

app.route("https://requestingapps.herokuapp.com/<variable>")
def profile2(variable):
	return variable


if __name__ == "__main__":
    app.run(debug=True)
