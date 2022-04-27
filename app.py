import sys
from PyQt5 import QtWidgets, QtCore
from ui_code2 import Ui_MainWindow

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure

import contextlib

import os
import numpy as np
import mne

from sklearn.svm import SVC

import sys

import data_loading
import linear
import cnn
import rnn

import numpy as np
from sklearn import preprocessing

from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from param import Param

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
        self.ui.btn_menu7.clicked.connect(self.show_classification_page)
        self.ui.btn_choosedataset.clicked.connect(self.to_welcome)

        # Set links for buttons on main pages
        self.ui.btn_preprocess.clicked.connect(self.show_preprocess_page)
        self.ui.btn_detectevents.clicked.connect(self.show_events_page)
        self.ui.btn_epoch.clicked.connect(self.show_epochs_page)
        self.ui.btn_tfa.clicked.connect(self.show_tfa_page)
        self.ui.btn_evoked.clicked.connect(self.show_evoked_page)
        self.ui.btn_traindata.clicked.connect(self.show_classification_page)

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
        self.ui.btn_cnn.clicked.connect(self.choose_cnn)
        self.ui.btn_rnn.clicked.connect(self.choose_rnn)
        self.ui.btn_lda.clicked.connect(self.choose_lda)
        self.ui.btn_svm.clicked.connect(self.choose_svm)

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
    def show_classification_page(self):
        self.ui.stackedMain.setCurrentWidget(self.ui.classification)

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
        n_components = int(self.ui.input_number_components.text())
        random_state = int(self.ui.input_random_state.text())
        max_iter = int(self.ui.input_max_iter.text())
        ica = mne.preprocessing.ICA(n_components=n_components, random_state=random_state, max_iter=max_iter)
        ica.fit(self.raw_data)
        to_exclude = self.ui.input_exclude.text().split(", ")
        to_exclude = list(map(int, to_exclude))
        ica.exclude = to_exclude
        self.ui.figure = ica.plot_properties(self.raw_data, picks=ica.exclude)
        # self.plot_graph(self.ui.figure)
        self.ica = ica

    def preprocess_compare_signals(self):
        orig_raw = self.raw_data.copy()
        self.raw_data.load_data()
        self.ica.apply(self.raw_data)

        # show some frontal channels to clearly illustrate the artifact removal
        chs = self.ui.input_channels.toPlainText().split(", ")
        channels = ['MEG 0111', 'MEG 0121', 'MEG 0131', 'MEG 0211', 'MEG 0221', 'MEG 0231',
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
        self.ui.out_console_events.setText(str(events[:5])) 
        self.events = events

    def events_plot(self):
        events = self.events
        raw = self.raw_data
        self.event_dict = {'auditory/left': 1, 'auditory/right': 2, 'visual/left': 3,
              'visual/right': 4, 'smiley': 5, 'buttonpress': 32}
        fig = mne.viz.plot_events(events, event_id=self.event_dict, sfreq=raw.info['sfreq'],
                            first_samp=raw.first_samp)
        
    # EPOCH functions

    def epoch_pool(self):
        events = self.events
        raw = self.raw_data
        reject_criteria = dict(mag=4000e-15,     # 4000 fT
                        grad=4000e-13,    # 4000 fT/cm
                        eeg=150e-6,       # 150 µV
                        eog=250e-6)       # 250 µV
        epochs = mne.Epochs(raw, events, event_id=self.event_dict, tmin=-0.2, tmax=0.5,
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

    def windowed_means(out_features, param):
        """
        Windowed means features extraction method
        :param out_features: epoched data in 3D shape (epochs_count x channels_count x values_count)
        :param param: configuration object
        :return: 2D vector with calculated features (epochs_count x features_count)
        """
        sampling_fq = param.t_max * 1000 + 1
        temp_wnd = np.linspace(param.min_latency, param.max_latency, param.steps + 1)
        intervals = np.zeros((param.steps, 2))
        for i in range(0, temp_wnd.shape[0] - 1):
            intervals[i, 0] = temp_wnd[i]
            intervals[i, 1] = temp_wnd[i + 1]
        intervals = intervals - param.t_min
        output_features = []
        for i in range(out_features.shape[0]):
            feature = []
            for j in range(out_features.shape[1]):
                time_course = out_features[i][j]
                for k in range(intervals.shape[0]):
                    borders = intervals[k] * sampling_fq
                    feature.append(np.average(time_course[int(borders[0] - 1):int(borders[1] - 1)]))
            output_features.append(feature)
        out = preprocessing.scale(np.array(output_features), axis=1)
        return out


    def print_help():
        print("Usage: python main.py <classifier>\n")
        print("You can choose from these classifiers: lda, svm, cnn, rnn\n")


    def call_ml(cl):
        """
        The program is executable from the command line using this file with one argument represents the choice of classifier. 
        The command has the following form:

        python main.py <classifier>

        The user can choose from 4 types of classifiers, so the possible variants of the command are:

        python main.py lda
        python main.py svm
        python main.py cnn
        python main.py rnn

        All other parameters are configurable in the param.py file.
        """

        #if len(sys.argv) != 2:
        #    print("The wrong number of command line arguments!\n")
        #    print_help()
        #    exit(1)

        classifier = cl

        if classifier != 'cnn' and classifier != 'rnn' and classifier != 'lda' and classifier != 'svm':
            print("The wrong choice of classifier!\n")
            print_help()
            exit(1)

        param = Param()

        X, Y = data_loading.read_data(param)

        if classifier == 'cnn':
            X = np.expand_dims(X, 3)
        elif classifier == 'lda' or classifier == 'svm':
            X = windowed_means(X, param)

        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=param.test_part,
                                                            random_state=0, shuffle=True)

        val = round(param.validation_part * x_train.shape[0])

        shuffle_split = ShuffleSplit(n_splits=param.cross_val_iter, test_size=val, random_state=0)
        val_results = []
        test_results = []
        iter_counter = 0

        # Monte-carlo cross-validation
        for train, validation in shuffle_split.split(x_train):
            iter_counter = iter_counter + 1
            print(iter_counter, "/", param.cross_val_iter, " cross-validation iteration")

            if classifier == 'cnn':
                model = cnn.CNN(x_train.shape[1], x_train.shape[2], param)
            elif classifier == 'rnn':
                model = rnn.RNN(x_train.shape[1], x_train.shape[2], param)
            elif classifier == 'lda':
                model = linear.LinearClassifier(LinearDiscriminantAnalysis(solver='eigen', shrinkage='auto'))
            else:
                model = linear.LinearClassifier(SVC(cache_size=500))

            validation_metrics = model.fit(x_train[train], y_train[train], x_train[validation], y_train[validation])
            val_results.append(validation_metrics)

            test_metrics = model.evaluate(x_test, y_test)
            test_results.append(test_metrics)

        print("\nClassifier: ", classifier)

        avg_val_results = np.round(np.mean(val_results, axis=0) * 100, 2)
        avg_val_results_std = np.round(np.std(val_results, axis=0) * 100, 2)

        print("Averaged validation results with averaged std in brackets:")
        print("AUC: ", avg_val_results[0], "(", avg_val_results_std[0], ")")
        print("accuracy: ", avg_val_results[1], "(", avg_val_results_std[1], ")")
        print("precision: ", avg_val_results[2], "(", avg_val_results_std[2], ")")
        print("recall: ", avg_val_results[3], "(", avg_val_results_std[3], ")")

        print("\n##############################\n")

        avg_test_results = np.round(np.mean(test_results, axis=0) * 100, 2)
        avg_test_results_std = np.round(np.std(test_results, axis=0) * 100, 2)

        print("Averaged test results with averaged std in brackets: ")
        print("AUC: ", avg_test_results[0], "(", avg_test_results_std[0], ")")
        print("accuracy: ", avg_test_results[1], "(", avg_test_results_std[1], ")")
        print("precision: ", avg_test_results[2], "(", avg_test_results_std[2], ")")
        print("recall: ", avg_test_results[3], "(", avg_test_results_std[3], ")")


    def choose_lda():
        call_ml('lda')

    def choose_svm():
        call_ml('svm')

    def choose_cnn():
        call_ml('cnn')

    def choose_rnn():
        call_ml('rnn')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())