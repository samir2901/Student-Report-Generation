from firebase_config import *
from student import * 
from PyPDF2 import PdfReader, PdfWriter
import os 

def login(username, password):
  #email: samir2000@gmail.com
  #password: admin123  
  auth = firebase.auth()  
  try:
    auth.sign_in_with_email_and_password(username, password)
    return True 
  except:
    return False

def putintoDatabase(data):
  database = firebase.database()
  database.child("student").child(data[0]).child(data[1]).push(data[2])

def getData(clss,section):
  database = firebase.database()
  data = database.child('student').child(clss).child(section).get()
  d = dict(data.val())
  #key = list(d.keys())[0]
  l = []
  for key in d.keys():
    l.append(d[key])
  return l

def getStudent(clss,section,data):
  id = data["id"]  
  name = data['name']  
  dob = data['dob']
  eng = data['obEnglishMarks']
  math = data['obMathMarks']
  evs = data['obEvsMarks']
  stud = ClassPrepStudent(id,name,dob,section)
  stud.putMarks(eng,math,evs)
  return stud 


def generateReport(student : ClassPrepStudent):
  total = student.calculateTotal()
  prcnt = student.percentage()
  prmt_clss = student.clss + 1
  if prcnt < 33:
    remark = "Not promoted"
  else:
    remark = "Promoted to class " + str(prmt_clss) + " with a percentage of " + str(prcnt) + "%."
  
  
  reader = PdfReader("PrepPrimaryReportCard Format.pdf")
  writer = PdfWriter()
  page = reader.pages[0]
  fields = reader.get_fields()
  writer.add_page(page)
  writer.update_page_form_field_values(
    writer.pages[0],
    {
        "id" : student.id,
        "name" : student.name,
        "class" : student.clss,
        "section" : student.section,
        "dob" : student.dob,
        "engMark" : student.obEnglishMarks,
        "mathMark" : student.obMathMarks,
        "evsMark" : student.obEvsMarks,
        "totalMark" : total,
        "remarks" : remark
    }
  )  
  if not os.path.exists(f"reports/{student.clss}"):
    os.mkdir(f"reports/{student.clss}")
  path = f"reports/{student.clss}/{student.section}"
  if not os.path.exists(path):  
    os.mkdir(path)  
  output_file = os.path.join(path, student.id + ".pdf")
  
  with open(output_file, "wb") as ostream:
    writer.write(ostream)



  