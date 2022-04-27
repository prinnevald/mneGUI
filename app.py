import sys
from PyQt5 import QtWidgets, QtCore
from ui_code import Ui_MainWindow

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure

import os
import numpy as np
import mne
import threading
import io

# run this for converting ui to py
# pyuic5 main_window.ui -o ui_code.py

MY_DPI = 192

def pos_by_pixel(num):
    return num/MY_DPI

class MainWindow:
    def __init__(self):
        self.main_win = QtWidgets.QMainWindow() # Call the inherited classes __init__ method
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Hide output window

        # PAGES
        # Set main widget
        self.ui.stackedWelcome.setCurrentWidget(self.ui.welcome)
        self.ui.stackedMain.setCurrentWidget(self.ui.raw)

        self.ui.btn_upload.clicked.connect(self.upload_dataset)
        self.ui.btn_sample.clicked.connect(self.select_dataset)

        # Set links for buttons on side menu
        self.ui.btn_menu1.clicked.connect(self.show_raw_page)
        self.ui.btn_menu2.clicked.connect(self.show_preprocess_page)
        self.ui.btn_menu3.clicked.connect(self.show_events_page)
        self.ui.btn_menu4.clicked.connect(self.show_epochs_page)
        self.ui.btn_menu5.clicked.connect(self.show_tfa_page)
        self.ui.btn_menu6.clicked.connect(self.show_evoked_page)
        self.ui.btn_choosedataset.clicked.connect(self.to_welcome)

        # Set links for buttons on main pages
        self.ui.btn_preprocess.clicked.connect(self.show_preprocess_page)
        self.ui.btn_detectevents.clicked.connect(self.show_events_page)
        self.ui.btn_epoch.clicked.connect(self.show_epochs_page)
        self.ui.btn_tfa.clicked.connect(self.show_tfa_page)
        self.ui.btn_evoked.clicked.connect(self.show_evoked_page)

        # BUTTONS connect
        self.ui.btn_text_info.clicked.connect(self.print_data)
        self.ui.btn_visualize.clicked.connect(self.raw_visualize)
        self.ui.btn_plot_pds.clicked.connect(self.raw_plot_pds)
        self.ui.btn_preprocess_plot.clicked.connect(self.preprocess_plot)
        self.ui.btn_comparesignals.clicked.connect(self.preprocess_compare_signals)
        self.ui.btn_findevents.clicked.connect(self.events_find)
        self.ui.btn_plotevents.clicked.connect(self.events_plot)
        self.ui.btn_dropepochs.clicked.connect(self.epoch_pool)
        self.ui.btn_imagemap.clicked.connect(self.epoch_plot)
        self.ui.btn_tfa1.clicked.connect(self.tfa_plot)
        self.ui.btn_evoked1.clicked.connect(self.evoked_compare)
        self.ui.btn_evoked2.clicked.connect(self.evoked_detailed_plot)
        self.ui.btn_evoked1.clicked.connect(self.evoked_difference_wave)

    # plot graphs driver
    # def plot_graph(self, figure):
    #     try:
    #         self.ui.canvas.setParent(None)
    #         self.ui.toolbar.setParent(None)
    #     except AttributeError:
    #         print("Canvas doesnt exist!")
    #     self.ui.canvas = FigureCanvas(figure)
    #     self.ui.toolbar = NavigationToolbar(self.ui.canvas, self.ui.out_raw)
    #     self.ui.canvas.setGeometry(QtCore.QRect(0, 0, 900/MY_DPI, 900/MY_DPI))
    #     self.ui.layout.addWidget(self.ui.toolbar)
    #     self.ui.layout.addWidget(self.ui.canvas)
    #     # axes
    #     self.ui.canvas.draw()

    # UPLOAD dataset

    def upload_dataset(self):
        # returns a tuple (fname, ".ext")
        # throw exception if file was not chosen
        fname, ext = QtWidgets.QFileDialog.getOpenFileName(self.main_win, "Open File", "", "All Files (*);; Sample (*.fif)")
        # only fif for now // works
        if fname.endswith('.vhdr'):
            raw = mne.io.read_raw_brainvision(fname)
            self.raw_data = raw
        elif fname.endswith('.fif'):
            raw = mne.io.read_raw_fif(fname[0])
            self.raw_data = raw
        self.to_main()
        
    def select_dataset(self):
        # if fif
        if (self.ui.combo_box.currentIndex() == 0):
            print ("here bitch")
            sample_data_folder = mne.datasets.sample.data_path()
            self.sample_data_folder = sample_data_folder
            sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',
                                                'sample_audvis_filt-0-40_raw.fif')
            raw = mne.io.read_raw_fif(sample_data_raw_file)
            self.raw_data = raw
            self.to_main()

    # NAVIGATION
    def show(self):
        self.main_win.show()
    def to_main(self):
        self.ui.stackedWelcome.setCurrentWidget(self.ui.main)
        self.show_raw_page()
    def to_welcome(self):
        self.ui.stackedWelcome.setCurrentWidget(self.ui.welcome)
    def show_raw_page(self):
        self.ui.stackedMain.setCurrentWidget(self.ui.raw)
    def show_preprocess_page(self):
        self.ui.stackedMain.setCurrentWidget(self.ui.preprocess)
    def show_events_page(self):
        self.ui.stackedMain.setCurrentWidget(self.ui.events)
    def show_epochs_page(self):
        self.ui.stackedMain.setCurrentWidget(self.ui.epoch)
    def show_tfa_page(self):
        self.ui.stackedMain.setCurrentWidget(self.ui.tfa)
    def show_evoked_page(self):
        self.ui.stackedMain.setCurrentWidget(self.ui.evoked)

    # RAW functions

    def print_data(self):
        # Print to the console        
        try:
            self.ui.canvas.setParent(None)
            self.ui.toolbar.setParent(None)
        except AttributeError:
            print("Canvas doesnt exist!")
        self.ui.out_console.setText(str(self.raw_data.info))

    def raw_visualize(self):
        self.ui.out_console.hide()
        self.ui.figure = self.raw_data.plot()
        # self.plot_graph(self.ui.figure)

    def raw_plot_pds(self):
        self.ui.out_console.hide()
        self.ui.figure = self.raw_data.plot_psd()
        # self.plot_graph(self.ui.figure)
   
    # PREPROCESS functions
    def preprocess_plot(self):
        ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
        ica.fit(self.raw_data)
        ica.exclude = [1, 2]
        self.ui.figure = ica.plot_properties(self.raw_data, picks=ica.exclude)
        # self.plot_graph(self.ui.figure)
        self.ica = ica

    def preprocess_compare_signals(self):
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

    # EVENTS functions

    def events_find(self):
        # REPLACE PRINTS
        events = mne.find_events(self.raw_data, stim_channel='STI 014')
        print(events[:5])  # show the first 5
        self.events = events
        print(events)

    def events_plot(self):
        events = self.events
        raw = self.raw_data
        event_dict = {'auditory/left': 1, 'auditory/right': 2, 'visual/left': 3,
                'visual/right': 4, 'smiley': 5, 'buttonpress': 32}
        self.event_dict = event_dict
        fig = mne.viz.plot_events(events, event_id=event_dict, sfreq=raw.info['sfreq'],
                            first_samp=raw.first_samp)

    # EPOCH functions

    def epoch_pool(self):
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

    
    def epoch_plot(self):
        self.aud_epochs.plot_image(picks=['MEG 1332', 'EEG 021']) 
        # graph here and logs

    # TFA functions
    
    def tfa_plot(self):
        frequencies = np.arange(7, 30, 3)
        power = mne.time_frequency.tfr_morlet(self.aud_epochs, n_cycles=2, return_itc=False,
                                            freqs=frequencies, decim=3)
        power.plot(['MEG 1332'])
    
    # EVOKED functions

    def evoked_compare(self):
        self.aud_evoked = self.aud_epochs.average()
        self.vis_evoked = self.vis_epochs.average()

        mne.viz.plot_compare_evokeds(dict(auditory=self.aud_evoked, visual=self.vis_evoked),
                                     legend='upper left', show_sensors='upper right')
        # graph and logs

    def evoked_detailed_plot(self):
        self.aud_evoked.plot_joint(picks='eeg')
        self.aud_evoked.plot_topomap(times=[0., 0.08, 0.1, 0.12, 0.2], ch_type='eeg')
        # graph and logs

    def evoked_difference_wave(self):
        evoked_diff = mne.combine_evoked([self.aud_evoked, self.vis_evoked], weights=[1, -1])
        evoked_diff.pick_types(meg='mag').plot_topo(color='r', legend=False)
    
    # ML functions

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())