from kivy import Config

from kivy.app import App

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 325)
Config.set('graphics', 'height', 450)


class CalculatorApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = None

    def build(self):

        anchor = AnchorLayout(anchor_x='right', anchor_y='center')
        self.label = Label(size_hint=(.45, 1), text='12345', halign='right', font_size=30)
        anchor.add_widget(self.label)

        grid = GridLayout(cols=4, rows=6, padding=7, spacing=3)
        values = ['%', ' ', 'C', '<-',
                  '1/x', 'x^2', 'x^(1/2)', '/',
                  '7', '8', '9', '*',
                  '4', '5', '6', '-',
                  '1', '2', '3', '+',
                  ' ', '0', '.', '=']
        for i in values:
            if i == ' ':
                grid.add_widget(Widget())
            elif i.isnumeric():
                num = Button(text=i)
                grid.add_widget(num)
            elif i in ['%', '/', '*', '-', '+']:
                sign = Button(text=i)
                grid.add_widget(sign)
            else:
                grid.add_widget(Button(text=i))

        box = BoxLayout(orientation='vertical')
        box.add_widget(anchor)
        box.add_widget(grid)

        fl = FloatLayout()
        fl.add_widget(box)



        return fl

    def action(self):
        pass

    def print(self):
        pass




if __name__ == '__main__':
    CalculatorApp().run()
