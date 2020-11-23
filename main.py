from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import requests 
import json


class HomeScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class SettingsScreen(Screen):
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):
    my_friend_id = 1
    def build(self):

        return GUI

    def on_start(self):
        # get database data
        result = requests.get("https://lost-and-found-pet-app.firebaseio.com/" + str(self.my_friend_id) + ".json")
        data = json.loads(result.content.decode())
        workouts = data['workouts'][1:]
        for workout in workouts:
            # populate workout grid in homescreen
            print(workout['workout_image'])
            print(workout['units'])

    

    def change_screen(self, screen_name):
        #get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition
        screen_manager.current = screen_name

MainApp().run()
