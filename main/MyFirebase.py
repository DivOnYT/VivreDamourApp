import pyrebase
import time

config = {
}

class MyFirebase():
	def __init__(self):
		self.firebase = pyrebase.initialize_app(config)
		self.auth = self.firebase.auth()
		self.db = self.firebase.database()

	def return_msg(self, number):
		user = self.db.child("Messages").child(number).get()
		general = user.val()
		msg = general.get("Message : ")
		return msg

	def sign_in_email_pass(self, email, password):
		try:
			if (email or password) == "":
				return False
			else:
				self.auth.sign_in_with_email_and_password(email, password)
				print("User connected %s %s" % (email, password))
				return True
		except:
			return False

	def signin_db(self, email, password):
		if (email or password) == "":
			return False
		else:
			try:
				eml = email.split("@")
				user = self.db.child("Users").child(eml[0]).get()
				general = user.val()
				print(general)
				emal = general.get("Email : ")
				pas = general.get("Mot de Passe : ")
				self.nom = general.get("Prénom : ")
				if (email == emal) & (password == pas):
					return True
				else:
					return False
			except:
				return False


	def auth_with_email_pass(self, email, password):
		try:
			if (email or password) == "":
				return False
			else:
				createin = self.auth.create_user_with_email_and_password(email, password) 
				self.auth.refresh(createin['refreshToken'])
				print("User created %s %s" % (email, password))
				return True
		except:
			return False

	def db_signin(self, name, email, password, tel, sexe):
		data = {
                        "Prénom : ": name,
                        "Email : ": email,
                        "Teléphone : ": tel,
                        "Sexe :": sexe,
                        "Mot de Passe : ": password
                        }

		dat = email.split("@")
		try:
			self.db.child("Users").child(dat[0]).set(data)
			return True
		except:
			return False

	def write_ID(self, ID):
		self.files = open("jours.txt", "w", encoding="Utf-8")
		self.files.write(ID)

	def write_jour(self, jour):
		self.files = open("jours.txt", "w", encoding="Utf-8")
		self.files.write(jour)

	def check_ID(self):
		self.file = open("jours.txt", "r+", encoding="Utf-8")
		self.ID = int(self.file.readline())
		return ID

	def timed_days(self):
		self.t = time.localtime()
		self.file = open("jours.txt", "r+", encoding="Utf-8")
		self.jour = int(self.file.readline())
		self.ID = int(self.file.readline())
		print(self.jour)
		print(self.ID)
		if self.jour == self.t[2]:
			self.ID = self.ID
			self.jour = self.jour
		else:
			self.ID += 1
			self.jour = self.t[2]
		print(self.ID)
		print(self.jour)

	def check_jour(self):
		self.jour = int(self.file.readline())
		return jour

	def return_msg(self, ID):
		try:
			msg = self.db.child("Messages").child(ID).get().val().get("Message : ")
			return msg
		except:
			return "Aucun Parcours Trouve\n ..."

	def verify_parcours(self):
		try:
			parcours = self.db.child("Parcours").get().val().get("Parcours : ")
			return parcours
		except:
			return "Aucun Parcours Trouve\n ..."
			
if __name__ == "__main__":
        msg = MyFirebase().timed_days()
        parc = MyFirebase().verify_parc
