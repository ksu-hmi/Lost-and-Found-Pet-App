from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        #get the screen manager from the kv file
        screen_manager = self.root.ids['self_manager']
        screen_manager.current = screen_name 

MainApp().run()