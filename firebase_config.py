import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyAAsPz3zvzjJTPojRWLjf-Nm-_7YHLYFTQ",
  "authDomain": "student-report-generation.firebaseapp.com",
  "projectId": "student-report-generation",
  "storageBucket": "student-report-generation.appspot.com",
  "messagingSenderId": "308670169513",
  "appId": "1:308670169513:web:d34db6927a7305d433c4b8",
  'measurementId': "G-T7NT7C1J56",
  "databaseURL" : "https://student-report-generation-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)