'''
Created on Sep 30, 2017

@author: Burkhard A. Meier
'''

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()