#import flask module
from flask import Flask, render_template

#creating an app using flask
app = Flask(__name__)

#defining the basic route / and its
#corresponding request handler
@app.route("/")
def main():
	return render_template('index.html')

#check if the executed file is the main program
#run the app
if __name__ == "__main__":
	app.run()



