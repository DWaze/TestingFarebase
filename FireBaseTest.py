import pyrebase

config = {
  "apiKey": "AIzaSyBxVvXDopI89U3EdD_uldHvFYS1wGKLhTo",
  "authDomain": "homotics-914a5.firebaseapp.com",
  "databaseURL": "https://homotics-914a5.firebaseio.com",
  "storageBucket": "homotics-914a5.appspot.com",
}

firebase = pyrebase.initialize_app(config)


auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("smarthomeotics@gmail.com", "fc5a5xG9k3fi")

print(user["idToken"])

db = firebase.database()

data = {
  "name": "Mortimer 'Morty' zed"
}

results = db.child("users").push(data, user['idToken'])

print(results)