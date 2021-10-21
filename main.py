#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Pong game using kivy

from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class PongGameApp(App):
    """
    Game of Ping Pong with Kivy Library.
    """
    def build(self):
        return PongGame()

if __name__ == '__main__':
    pongGame = PongGameApp()
    pongGame.run()
