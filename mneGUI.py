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
        self.sample_data_folder = sample_data_folder
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

    # NOT USED FUNCTIONS
    def preprocessing(self, instance):
        # set up and fit the ICA
        ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
        ica.fit(self.raw_data)
        ica.exclude = [1, 2]
        ica.plot_properties(self.raw_data, picks=ica.exclude)
        self.ica = ica
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
        orig_raw.plot(order=chan_idxs, start=12, duration=4)
        self.raw_data.plot(order=chan_idxs, start=12, duration=4)

    def detect_events(self, instance):
        events = mne.find_events(self.raw_data, stim_channel='STI 014')
        print(events[:5])  # show the first 5
        self.events = events
    
    def plot_events(self, instance):
        events = self.events
        raw = self.raw_data
        event_dict = {'auditory/left': 1, 'auditory/right': 2, 'visual/left': 3,
              'visual/right': 4, 'smiley': 5, 'buttonpress': 32}
        self.event_dict = event_dict
        fig = mne.viz.plot_events(events, event_id=event_dict, sfreq=raw.info['sfreq'],
                          first_samp=raw.first_samp)

    def epoching(self, instance):
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
        self.aud_epochs.plot_image(picks=['MEG 1332', 'EEG 021']) 
        # graph here and logs

    def time_frequency(self, instance):
        frequencies = np.arange(7, 30, 3)
        power = mne.time_frequency.tfr_morlet(self.aud_epochs, n_cycles=2, return_itc=False,
                                            freqs=frequencies, decim=3)
        power.plot(['MEG 1332'])
    
    def evoked(self, instance):
        self.aud_evoked = self.aud_epochs.average()
        self.vis_evoked = self.vis_epochs.average()

        mne.viz.plot_compare_evokeds(dict(auditory=self.aud_evoked, visual=self.vis_evoked),
                                    legend='upper left', show_sensors='upper right')
        # graph and logs

    def evoked_detailed(self, instance):
        self.aud_evoked.plot_joint(picks='eeg')
        self.aud_evoked.plot_topomap(times=[0., 0.08, 0.1, 0.12, 0.2], ch_type='eeg')
        # graph and logs

    def evoked_difference_wave(self, instance):
        evoked_diff = mne.combine_evoked([self.aud_evoked, self.vis_evoked], weights=[1, -1])
        evoked_diff.pick_types(meg='mag').plot_topo(color='r', legend=False)

    def inverse_modeling(self, instance):
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
        self.stc.plot(initial_time=0.1, hemi='split', views=['lat', 'med'],
                subjects_dir=subjects_dir)
        # graph here, logs here

if __name__ == '__main__':
    mneGUI().run()