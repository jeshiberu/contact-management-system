#import sqlalchemy
# The error may be in the SQL query or connection setup
from sqlalchemy import create_engine, text
import os

#Hide DB CONNECTION DETAILS
db_connection_string = os.environ['DB_CONNECTION_STRING']

#print(sqlalchemy.__version__)

engine = create_engine(db_connection_string)

def load_Contacts_from_db():
  #sql connection
  with engine.connect() as conn:
    result = conn.execute(text("select * from Contacts"))
  print(result.all())

  
  #row
  Contacts = []
  for row in result.all():
    Contacts.append(row._asdict())
    return Contacts


def load_Contact_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(
      "SELECT * FROM Contacts WHERE id = :val"), val=id
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
      

  # print("type(result):", type(result))
  # print("\n")
  # result_all = result.all()
  # print(result_all)
  # print("\n")
  # print("type(result.all())", type(result_all)) 
  # print("\n")
  # first_result = result_all[0]
  # print("type(first_result):", type(first_result)) 
  # print("\n")
  # first_result_dict = result_all[0]._asdict()
  # print("type(first_result_dict):", type(first_result_dict))
  # print(first_result_dict)

