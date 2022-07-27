from flask import *
app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<h1>hello world ji</h1>"

if __name__ == "__main__":
   app.run(host="0.0.0.0",port=5000,debug=True)