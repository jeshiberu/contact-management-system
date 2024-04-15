from flask import Flask, jsonify, render_template
from database import load_Contacts_from_db, load_Contact_from_db

app = Flask(__name__)

 
@app.route('/')
def Contact_Management_System():
  Contacts = load_Contacts_from_db()
  return render_template('home.html', 
                         Contacts=Contacts,
                         Contact_Management_System='Contact Management System')

@app.route("/api/contacts")
def list_contacts():
  return jsonify(CONTACTS)


@app.route("/contact/<id>")
def show_contact(id):
  contact = load_Contacts_from_db(id)
  return jsonify(contact)



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
  