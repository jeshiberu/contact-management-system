from flask import Flask
app = Flask(__name__)

@app.route('/')
def Contact_Management_System():
  return "<p>Contact Management System</p>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  