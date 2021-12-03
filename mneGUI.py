from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.core.window import Window
import matplotlib
matplotlib.use('Agg')

import os
import numpy as np
import mne
import matplotlib.pyplot as plt
import threading
import io

from time import sleep
from contextlib import redirect_stdout

f = io.StringIO()

class Logger():
    def logger_loop(self, logger):
        while True:
            logger.text = f.getvalue()
            sleep(0.5)

    def __init__(self, logger):
        thread = threading.Thread(target = self.logger_loop, args = (logger,))
        thread.start()

with redirect_stdout(f):
    class mneGUI(App):
        Window.clearcolor = (0.92, 0.89, 0.72, 1)
        def build(self):
            # generate general layout
            self.window = BoxLayout(orientation = "vertical")
            #divide into sections 
            self.section1 = BoxLayout(orientation = "horizontal") # title
            self.section2 = BoxLayout(orientation = "horizontal") # output
            self.section3 = BoxLayout(orientation = "horizontal") # buttons
           # self.section4 = BoxLayout(orientation = "horizontal")
            self.section3 = BoxLayout(spacing=20) # buttons
            self.section3 = BoxLayout(padding=0) # buttons
            self.section3 = BoxLayout(orientation = "horizontal")
            self.window.add_widget(self.section1)
            self.window.add_widget(self.section2)
            self.window.add_widget(self.section3)
            #self.window.add_widget(self.section4)

            # styling
            self.window.cols = 1
            self.window.size_hint = (0.6, 0.7)
            self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

            # self.plot = FigureCanvasKivyAgg(plt.gcf())
            # self.window.add_widget(self.plot)

            self.main_text = Label(
                            text= "Welcome to mneGUI!",
                            font_size= 30,
                            color= 'D36135'
                            )
            self.section2.add_widget(self.main_text)
            title_img = Image(source='images/title_icon.png')
            self.section1.add_widget(title_img)

            self.load_data_button = Button(text="Load Data >",background_color=(0.82,0.38,0.21,1),border=(25,25,25,25))
            self.load_data_button.bind(on_press = self.load_data)
            self.section3.add_widget(self.load_data_button)

            # self.log_text = Label(
            #                 text= "Log",
            #                 font_size= 12,
            #                 color= '#FFFFFF'
            #                 )
            # self.section4.add_widget(self.log_text)
            # # redirect stdout
            # logger = Logger(self.log_text)

            return self.window

        def load_data(self, instance):
            sample_data_folder = mne.datasets.sample.data_path()
            self.sample_data_folder = sample_data_folder
            sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',
                                                'sample_audvis_filt-0-40_raw.fif')
            raw = mne.io.read_raw_fif(sample_data_raw_file)

            self.raw_data = raw

            self.main_text.text = "Data loaded"
            self.section3.remove_widget(self.load_data_button)
            self.print_data_button = Button(text="Print raw data",size_hint=(.5, .5), background_color=(0.82,0.38,0.21,1))
            self.print_data_button.bind(on_press = self.print_data)
            self.section3.add_widget(self.print_data_button)

            self.show_data_button = Button(text="Visualize",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.show_data_button.bind(on_press = self.show_data)
            self.section3.add_widget(self.show_data_button)

            self.preprocess_data_button = Button(text="Preprocess >",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.preprocess_data_button.bind(on_press = self.preprocessing)
            self.section3.add_widget(self.preprocess_data_button)


        def print_data(self, instance):
            self.main_text.text = str(self.raw_data)

        def show_data(self, instance):
            # data = self.raw_data.get_data()
            # plt.plot(data)
            # self.plot = FigureCanvasKivyAgg(plt.gcf())
            # self.window.add_widget(self.plot)
            self.section2.remove_widget(self.main_text)
            self.img1 = Image(source='images/img1.png')
            self.img2 = Image(source='images/img2.png')
            self.section2.add_widget(self.img1)
            self.section2.add_widget(self.img2)

        # FUNCTIONALITY
        def preprocessing(self, instance):
            self.section2.remove_widget(self.img1)
            self.section2.remove_widget(self.img2)
            self.section3.remove_widget(self.preprocess_data_button)
            self.section3.remove_widget(self.print_data_button)
            self.section3.remove_widget(self.show_data_button)

            self.see_graph_button = Button(text="See graphs",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.see_graph_button.bind(on_press = self.preprocessing_see_graphs)
            self.section3.add_widget(self.see_graph_button)

            self.remove_button = Button(text="Remove components", size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.remove_button.bind(on_press = self.preprocessing_remove_components)
            self.section3.add_widget(self.remove_button)

            self.events_button = Button(text="Events >",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.events_button.bind(on_press = self.events)
            self.section3.add_widget(self.events_button)
            
        def preprocessing_see_graphs(self, instance):
            # set up and fit the ICA
            ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
            ica.fit(self.raw_data)
            ica.exclude = [1, 2]
            #ica.plot_properties(self.raw_data, picks=ica.exclude)
            self.ica = ica
            self.img3 = Image(source='images/img3.png')
            self.img4 = Image(source='images/img4.png')
            self.section2.add_widget(self.img3)
            self.section2.add_widget(self.img4)
            # logs and graph outputted

        def preprocessing_remove_components(self, instance):
            orig_raw = self.raw_data.copy()
            self.raw_data.load_data()
            self.ica.apply(self.raw_data)

            # show some frontal channels to clearly illustrate the artifact removal
            chs = ['MEG 0111', 'MEG 0121', 'MEG 0131', 'MEG 0211', 'MEG 0221', 'MEG 0231',
                'MEG 0311', 'MEG 0321', 'MEG 0331', 'MEG 1511', 'MEG 1521', 'MEG 1531',
                'EEG 001', 'EEG 002', 'EEG 003', 'EEG 004', 'EEG 005', 'EEG 006',
                'EEG 007', 'EEG 008']
            chan_idxs = [self.raw_data.ch_names.index(ch) for ch in chs]
            # orig_raw.plot(order=chan_idxs, start=12, duration=4)
            # self.raw_data.plot(order=chan_idxs, start=12, duration=4)
            self.img5 = Image(source='images/img5.png')
            self.img6 = Image(source='images/img6.png')
            self.section2.add_widget(self.img5)
            self.section2.add_widget(self.img6)

        def events(self, instance):
            # events button 
            self.section2.remove_widget(self.img3)
            self.section2.remove_widget(self.img4)
            self.section2.remove_widget(self.img5)
            self.section2.remove_widget(self.img6)
            self.section3.remove_widget(self.see_graph_button)
            self.section3.remove_widget(self.remove_button)
            self.section3.remove_widget(self.events_button)

            self.find_events_button = Button(text="Find events",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.find_events_button.bind(on_press = self.events_find)
            self.section3.add_widget(self.find_events_button)

            self.plot_events_button = Button(text="Plot events",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.plot_events_button.bind(on_press = self.events_plot)
            self.section3.add_widget(self.plot_events_button)

            self.epochs_button = Button(text="Epoch >",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.epochs_button.bind(on_press = self.epoch)
            self.section3.add_widget(self.epochs_button)
            

        def events_find(self, instance):
            events = mne.find_events(self.raw_data, stim_channel='STI 014')
            print(events[:5])  # show the first 5
            self.events = events
        
        def events_plot(self, instance):
            events = self.events
            raw = self.raw_data
            event_dict = {'auditory/left': 1, 'auditory/right': 2, 'visual/left': 3,
                'visual/right': 4, 'smiley': 5, 'buttonpress': 32}
            self.event_dict = event_dict
            # fig = mne.viz.plot_events(events, event_id=event_dict, sfreq=raw.info['sfreq'],
                            # first_samp=raw.first_samp)
            self.img7 = Image(source='images/img7.png')
            self.section2.add_widget(self.img7)


        def epoch(self, instance):
            # epoch button
            self.section2.remove_widget(self.img7)
            self.section3.remove_widget(self.find_events_button)
            self.section3.remove_widget(self.plot_events_button)
            self.section3.remove_widget(self.epochs_button)

            self.pool_button = Button(text="Pool",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.pool_button.bind(on_press = self.epoching_pool)
            self.section3.add_widget(self.pool_button)

            self.plot_button = Button(text="Plot",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.plot_button.bind(on_press = self.epoching_plot)
            self.section3.add_widget(self.plot_button)

            self.time_frequency_button = Button(text="Time frequency analysis >",font_size=12,size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.time_frequency_button.bind(on_press = self.time_frequency)
            self.section3.add_widget(self.time_frequency_button)
            

        def epoching_pool(self, instance):
            events = self.events
            raw = self.raw_data
            event_dict = self.event_dict
            reject_criteria = dict(mag=4000e-15,     # 4000 fT
                        grad=4000e-13,    # 4000 fT/cm
                        eeg=150e-6,       # 150 µV
                        eog=250e-6)       # 250 µV
            epochs = mne.Epochs(raw, events, event_id=event_dict, tmin=-0.2, tmax=0.5,
                        reject=reject_criteria, preload=True)
            # logs here
            conds_we_care_about = ['auditory/left', 'auditory/right',
                        'visual/left', 'visual/right']
            epochs.equalize_event_counts(conds_we_care_about)  # this operates in-place
            self.aud_epochs = epochs['auditory']
            self.vis_epochs = epochs['visual']
            del raw, epochs  # free up memory
            # logs here
        
        def epoching_plot(self, instance):
            # self.aud_epochs.plot_image(picks=['MEG 1332', 'EEG 021']) 
            # graph here and logs
            self.img8 = Image(source='images/img8.png')
            self.img9 = Image(source='images/img9.png')
            self.section2.add_widget(self.img8)
            self.section2.add_widget(self.img9)

        def time_frequency(self, instance):
            self.section2.remove_widget(self.img8)
            self.section2.remove_widget(self.img9)
            self.section3.remove_widget(self.pool_button)
            self.section3.remove_widget(self.plot_button)
            self.section3.remove_widget(self.time_frequency_button)

            self.frequency_plot_button = Button(text="Plot",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.frequency_plot_button.bind(on_press = self.time_frequency_plot)
            self.section3.add_widget(self.frequency_plot_button)

            self.evoked_button = Button(text="Estimate evoked responses >",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.evoked_button.bind(on_press = self.evoked)
            self.section3.add_widget(self.evoked_button)

        def time_frequency_plot(self, instance):
            frequencies = np.arange(7, 30, 3)
            power = mne.time_frequency.tfr_morlet(self.aud_epochs, n_cycles=2, return_itc=False,
                                                freqs=frequencies, decim=3)
            # power.plot(['MEG 1332'])
            self.img10 = Image(source='images/img10.png')
            self.section2.add_widget(self.img10)

        def evoked(self, instance):
            self.section2.remove_widget(self.img10)
            self.section3.remove_widget(self.frequency_plot_button)
            self.section3.remove_widget(self.evoked_button)

            self.compare_button = Button(text="Compare",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.compare_button.bind(on_press = self.evoked_compare)
            self.section3.add_widget(self.compare_button)

            self.difference_wave_button = Button(text="Difference wave",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.difference_wave_button.bind(on_press = self.evoked_difference_wave)
            self.section3.add_widget(self.difference_wave_button)

            self.detailed_plot_button = Button(text="Detailed plot",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.detailed_plot_button.bind(on_press = self.evoked_detailed_plot)
            self.section3.add_widget(self.detailed_plot_button)

            self.inverse_modeling_button = Button(text="Inverse modeling >",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.inverse_modeling_button.bind(on_press = self.inverse_modeling)
            self.section3.add_widget(self.inverse_modeling_button)
        
        def evoked_compare(self, instance):
            self.aud_evoked = self.aud_epochs.average()
            self.vis_evoked = self.vis_epochs.average()

            # mne.viz.plot_compare_evokeds(dict(auditory=self.aud_evoked, visual=self.vis_evoked),
            #                             legend='upper left', show_sensors='upper right')
            # graph and logs
            self.img11 = Image(source='images/img11.png')
            self.img12 = Image(source='images/img12.png')
            self.img13 = Image(source='images/img13.png')
            self.section2.add_widget(self.img11)
            self.section2.add_widget(self.img12)
            self.section2.add_widget(self.img13)

        def evoked_detailed_plot(self, instance):
            # self.aud_evoked.plot_joint(picks='eeg')
            # self.aud_evoked.plot_topomap(times=[0., 0.08, 0.1, 0.12, 0.2], ch_type='eeg')
            # graph and logs
            self.img14 = Image(source='images/img14.png')
            self.img15 = Image(source='images/img15.png')
            self.section2.add_widget(self.img14)
            self.section2.add_widget(self.img15)

        def evoked_difference_wave(self, instance):
            evoked_diff = mne.combine_evoked([self.aud_evoked, self.vis_evoked], weights=[1, -1])
            evoked_diff.pick_types(meg='mag').plot_topo(color='r', legend=False)
            self.img16 = Image(source='images/img16.png')
            self.section2.add_widget(self.img16)

        def inverse_modeling(self, instance):
            self.section2.remove_widget(self.img11)
            self.section2.remove_widget(self.img12)
            self.section2.remove_widget(self.img13)
            self.section2.remove_widget(self.img14)
            self.section2.remove_widget(self.img15)
            self.section2.remove_widget(self.img16)
            self.section3.remove_widget(self.compare_button)
            self.section3.remove_widget(self.difference_wave_button)
            self.section3.remove_widget(self.detailed_plot_button)
            self.section3.remove_widget(self.inverse_modeling_button)

            self.estimate_origins_button = Button(text="Estimate origins",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.estimate_origins_button.bind(on_press = self.inverse_modeling_estimate_origins)
            self.section3.add_widget(self.estimate_origins_button)

            self.modeling_plot_button = Button(text="Plot",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.modeling_plot_button.bind(on_press = self.inverse_modeling_plot)
            self.section3.add_widget(self.modeling_plot_button)

            self.finish_button = Button(text="Finish >",size_hint=(.5, .5),background_color=(0.82,0.38,0.21,1))
            self.finish_button.bind(on_press = self.finish)
            self.section3.add_widget(self.finish_button)
            

        def inverse_modeling_estimate_origins(self, instance):
            # load inverse operator
            inverse_operator_file = os.path.join(self.sample_data_folder, 'MEG', 'sample',
                                                'sample_audvis-meg-oct-6-meg-inv.fif')
            inv_operator = mne.minimum_norm.read_inverse_operator(inverse_operator_file)
            # set signal-to-noise ratio (SNR) to compute regularization parameter (λ²)
            snr = 3.
            lambda2 = 1. / snr ** 2
            # generate the source time course (STC)
            stc = mne.minimum_norm.apply_inverse(self.vis_evoked, inv_operator,
                                                lambda2=lambda2,
                                                method='MNE')  # or dSPM, sLORETA, eLORETA
            self.stc = stc
            # logs here

        def inverse_modeling_plot(self, instance):
            # path to subjects' MRI files
            subjects_dir = os.path.join(self.sample_data_folder, 'subjects')
            # plot the STC
            # self.stc.plot(initial_time=0.1, hemi='split', views=['lat', 'med'],
                    # subjects_dir=subjects_dir)
            # graph here, logs here
            self.img17 = Image(source='images/img17.png')
            self.section2.add_widget(self.img17)

        def finish(self, instance):
            quit()
        # terminates the program
    if __name__ == '__main__':
        mneGUI().run()