from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, CardTransition
from MyFirebase import MyFirebase
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from plyer import notification
import time

class Inscription(Screen):
        pass
        
class Connexion(Screen):
        pass

class HomeScreen(Screen):
        pass

class MainApp(App):
        theme_cls = ThemeManager()
        Firebase = MyFirebase()
        
        def homescreen(self):
            jour = self.Firebase.check_jour()
            ID = self.Firebase.check_ID()
            t = time.localtime()

            if ID == 41:
                ID = 1
                self.Firebase.write_ID(ID)
            else:
                self.Firebase.write_ID(ID)

            msg = self.Firebase.return_msg(ID)
            parcours = self.Firebase.verify_parcours()
            self.root.ids.homescreen.Message.text = msg
            self.root.ids.homescreen.Parcours.text = parcours

        def connexion(self):
                self.root.ids.inscription_screen.ids.on_error.text = ""
                self.root.ids.connexion_screen.ids.error.text = ""
                email = self.root.ids.connexion_screen.ids.email.text
                password = self.root.ids.connexion_screen.ids.password.text
                db_verify = self.Firebase.signin_db(email, password)
                authen = self.Firebase.sign_in_email_pass(email, password)
                if (authen & db_verify) == True:
                        self.Firebase.timed_days()
                        self.change_screen("homescreen", direction="left", mode="push")
                        self.homescreen()
                else:
                        if self.Firebase.signin_db(email, password) == False:
                                self.root.ids.connexion_screen.ids.error.text = "Erreur L'Email ou Le Mot de Passe ne correspont pas!\nOu l'utilisateur n'existe pas"
                        elif self.Firebase.sign_in_email_pass(email, password) == False:
                                self.root.ids.connexion_screen.ids.error.text = "Erreur L'Email ou Le Mot de Passe ne correspont pas!\nOu l'utilisateur n'existe pas"
                                
        def inscription(self):
                self.root.ids.connexion_screen.ids.error.text = ""
                self.root.ids.inscription_screen.ids.on_error.text = ""
                email = self.root.ids.inscription_screen.ids.email.text
                password = self.root.ids.inscription_screen.ids.password.text
                tel = self.root.ids.inscription_screen.ids.phone.text
                name = self.root.ids.inscription_screen.ids.prenom.text
                femme = self.root.ids.inscription_screen.ids.Femme.active
                homme = self.root.ids.inscription_screen.ids.Homme.active
                sexe = ""
                
                if homme == True:
                        sexe = "Homme"
                elif femme == True:
                        sexe = "Femme"
                db_verify = self.Firebase.db_signin(name, email, password, tel, sexe)
                authen = self.Firebase.auth_with_email_pass(email, password)
                        
                if (authen & db_verify) == True:
                        self.change_screen("connexion", direction="left", mode="pop")
                else:
                        if self.Firebase.db_signin(name, email, password, tel, sexe) == False:
                                self.root.ids.inscription_screen.ids.on_error.text = "Erreur L'Email, Password, Prénom, Telephone sont invalides(vides)"
                                
                        elif self.Firebase.auth_with_email_pass(email, password) == False:
                                self.root.ids.inscription_screen.ids.on_error.text = "Erreur L'Email ou Le Mot de Passe sont invalides(vides) ou l'utilisateur existe  \ndéjà"
                                
        def change_screen(self, screen, direction="right", mode="pop"):
                self.root.transition = CardTransition(direction=direction, mode=mode)
                self.root.current = screen
                
MainApp().run()

#self.root.ids.friend_workout_screen.ids.friend_workout_screen_friend_id
#gg
#MDLabel styles ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Subtitle1', 'Subtitle2', 'Body1', 'Body2', 'Button', 'Caption', 'Overline', 'Icon']
#def say_welcome(self):
                #nom = self.Firebase.nom
                #self.dialog = MDDialog(
                        #title="Bienvenue",
                        #text="Bonjour {}".format(nom),
                        #size_hint= [.5, .5],
                        #auto_dismiss=False)
               # self.dialog.open()
