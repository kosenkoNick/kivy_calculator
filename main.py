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

    def build(self):

        anchor = AnchorLayout(anchor_x='right', anchor_y='center')
        self.label = Label(size_hint=(.45, 1), halign='right', font_size=30)
        anchor.add_widget(self.label)

        grid = GridLayout(cols=4, rows=5, padding=7, spacing=3)
        values = ['%', 'C', '<-', '/',
                  '7', '8', '9', '*',
                  '4', '5', '6', '-',
                  '1', '2', '3', '+',
                  ' ', '0', '.', '=']
        for i in values:
            if i == ' ':
                grid.add_widget(Widget())
            elif i.isnumeric():
                num = Button(text=i, on_press=self.add_num)
                grid.add_widget(num)
            elif i in ['%', '/', '*', '-', '+']:
                sign = Button(text=i, on_press=self.operation)
                grid.add_widget(sign)
            elif i == '=':
                equal = Button(text=i, on_press=self.calculate, background_color=[0, 179, 242, .8])
                grid.add_widget(equal)
            elif i == 'C' or i == '<-':
                grid.add_widget(Button(text=i, on_press=self.remove))
            else:
                grid.add_widget(Button(text=i, on_press=self.add_num))

        box = BoxLayout(orientation='vertical')
        box.add_widget(anchor)
        box.add_widget(grid)

        fl = FloatLayout()
        fl.add_widget(box)

        return fl

    def remove(self, instance):
        if instance.text == '<-':
            string = str(self.label.text)
            self.label.text = string[:-1]
        elif instance.text == 'C':
            self.label.text = ''

    def add_num(self, instance):
        self.label.text += str(instance.text)

    def operation(self, instance):
        self.label.text += str(instance.text)

    def calculate(self, instance):
        self.label.text = str(eval(self.label.text))


if __name__ == '__main__':
    CalculatorApp().run()
