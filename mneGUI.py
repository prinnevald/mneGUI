from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import matplotlib
matplotlib.use('Agg')

import os
import numpy as np
import mne
import matplotlib.pyplot as plt
import threading


class mneGUI(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # self.plot = FigureCanvasKivyAgg(plt.gcf())
        # self.window.add_widget(self.plot)

        self.main_text = Label(
                        text= "Welcome to mneGUI",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.main_text)


        self.load_data_button = Button(text="Load Data")
        self.load_data_button.bind(on_press = self.load_data)
        self.window.add_widget(self.load_data_button)

        return self.window

    def load_data(self, instance):
        sample_data_folder = mne.datasets.sample.data_path()
        sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',
                                            'sample_audvis_filt-0-40_raw.fif')
        raw = mne.io.read_raw_fif(sample_data_raw_file)

        self.raw_data = raw

        self.main_text.text = "Data loaded"
        self.window.remove_widget(self.load_data_button)
        self.print_data_button = Button(text="Print raw data")
        self.print_data_button.bind(on_press = self.print_data)
        self.window.add_widget(self.print_data_button)

        self.show_data_button = Button(text="Show Data")
        self.show_data_button.bind(on_press = self.show_data)
        self.window.add_widget(self.show_data_button)

    def print_data(self, instance):
        raw = self.raw_data
        self.window.add_widget(Label(text=str(raw.info)))

    def show_data(self, instance):

        data = self.raw_data.get_data()
        plt.plot(data)
        self.plot = FigureCanvasKivyAgg(plt.gcf())
        self.window.add_widget(self.plot)

if __name__ == '__main__':
    mneGUI().run()