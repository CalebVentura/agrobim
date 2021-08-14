from firebase import firebase
fb_app = firebase.FirebaseApplication('https://agrobim-2ec0d-default-rtdb.firebaseio.com', None)
result = fb_app.get('/user', None)
print(result)
