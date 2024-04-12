from flask import Flask, render_template
from database import load_Contacts_from_db

app = Flask(__name__)

 
@app.route('/')
def Contact_Management_System():
  Contact = load_Contacts_from_db()
  return render_template('home.html', Contacts=Contacts)

@app.route("/api/contacts")
def list_contacts():
  return jsonify(CONTACTS)

if __name__ == "__maicn__":
  app.run(host='0.0.0.0', port=8080, debug=True)
  