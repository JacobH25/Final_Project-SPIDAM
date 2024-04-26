# gui_main.py

import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import upload_file as uf
import data_calc as dc

file = uf.upload_file()


def switch_graph():  # for the labels for spec and wave
    current = _graph_title.get()
    if current == "Spectrogram":
        _graph_title.set("Waveform")  # changes graph text
    elif current == "Waveform":
        _graph_title.set("Spectrogram")  # changes graph text


def get_graph_label(choice):  # for the labels for the line graph
    current = freq.get()
    if choice == -1:  # left button
        if current == "RT60 LMH":
            freq.set("RT60 M")  # changes freq text
        elif current == "RT60 M":
            # freq = 'RT60 L'
            freq.set("RT60 L")  # changes freq text

        elif current == "RT60 L":
            freq.set("RT60 H")  # changes freq text

        else:  # when freq = 'H'
            freq.set("RT60 M")  # changes freq text

    elif choice == 1:  # right button
        if current == "RT60 LMH":
            freq.set("RT60 M")  # changes freq text

        elif current == "RT60 M":
            freq.set("RT60 H")  # changes freq text

        elif current == "RT60 H":
            freq.set("RT60 L")  # changes freq text

        else:  # when freq = 'L'
            freq.set("RT60 M")  # changes freq text

    elif choice == 0:  # merge
        freq.set("RT60 LMH")  # changes freq text

def display_waveform():
    fig = dc.plot_waveform()
    canvas = FigureCanvasTkAgg(fig, master=graphContainer)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10)
    canvas.draw()


def display_spectrogram():
    fig = dc.plot_spectrogram()
    canvas = FigureCanvasTkAgg(fig, master=graphContainer)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10)
    canvas.draw()


def display_rt60_lmh_data():
    fig = dc.plot_rt60_lmh_data()
    canvas = FigureCanvasTkAgg(fig, master=graphContainer)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    canvas.draw()


def display_rt60_high_data():
    fig = dc.plot_rt60_high_data()
    canvas = FigureCanvasTkAgg(fig, master=graphContainer)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    canvas.draw()


def display_rt60_mid_data():
    fig = dc.plot_rt60_mid_data()
    canvas = FigureCanvasTkAgg(fig, master=graphContainer)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    canvas.draw()


def display_rt60_low_data():
    fig = dc.plot_rt60_low_data()
    canvas = FigureCanvasTkAgg(fig, master=graphContainer)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    canvas.draw()



if __name__ == '__main__':
    root = Tk()  # makes initial object
    root.geometry("1400x700")
    root.title(' ')

    mainFrame = tk.Frame(root, bg="grey")  # for top part... title, choose file, data
    mainFrame.pack(fill=X)  # padx = 10, pady = 10
    mainTitle = tk.Label(mainFrame, text='SPIDAM', font=('Silom', 24), highlightthickness=0, bg="grey", fg="black")
    mainTitle.pack(side=tk.TOP, pady=10)

    _file_btn = tk.Button(mainFrame, text='UPLOAD', bg="#38ABFF", font=('silom', 16), highlightthickness=0)
    _file_btn.pack(side=tk.LEFT, padx=2)  # assigns left side

    _data_btn = tk.Button(mainFrame, text='Data', bg="white", fg="black", font=('silom', 16), highlightthickness=0)
    _data_btn.pack(side=tk.RIGHT, padx=2)  # assigns right side

    # graph display
    graphFrame = tk.Frame(root, bg="white")
    graphFrame.pack(fill=X)  # padx = 10, pady = 10


    _graph_title = tk.StringVar(value="Spectrogram")
    _spec_title = tk.Label(graphFrame, textvariable=_graph_title, font=('Silom', 16), highlightthickness=0, bg="white",
                           fg="black")

    # left button made
    _graph_left_btn = tk.Button(graphFrame, text='<', bg="white", fg="black", font=('silom', 16), highlightthickness=0,
                                command=lambda: switch_graph())
    _graph_left_btn.pack(side=tk.LEFT, anchor=CENTER, expand=True, padx=2)  # lk

    # places label between the left and right buttons
    _spec_title.pack(side=tk.LEFT, anchor=CENTER, expand=True)

    # right button made
    _graph_right_btn = tk.Button(graphFrame, text='>', bg="white", fg="black", font=('silom', 16), highlightthickness=0,
                                 command=lambda: switch_graph())
    _graph_right_btn.pack(side=tk.LEFT, anchor=CENTER, expand=True, padx=2)  # puts in center

    _line_title = tk.Label(graphFrame, text='Line Graph', font=('Silom', 16), highlightthickness=0, bg="white",
                           fg="black")
    _line_title.pack(side=tk.RIGHT, anchor=CENTER, expand=True)

    freq = tk.StringVar(value="RT60 M")  # baseline
    _line_descript = tk.Label(graphFrame, textvariable=freq, font=('Silom', 16), highlightthickness=0, bg="white",
                              fg="black")
    _line_descript.pack(side=tk.RIGHT, anchor=CENTER, expand=True)

    # graph controls
    graphControlFrame = tk.Frame(root, bg="white")  # frame for graph controls
    graphControlFrame.pack(fill=tk.BOTH, expand=True)

    # add status bar  (rt60: 2.3seconds || +1.8seconds)
    reverb_label = tk.Label(graphControlFrame, text="RT60: ", font=('Silom', 16), highlightthickness=0, bg="white",
                            fg="black")
    reverb_label.pack(anchor='s', expand=True, pady=2)
    # status bar doesn't change yet

    # left arrow
    _left_btn = tk.Button(graphControlFrame, text='<', bg="white", fg="black", font=('silom', 16), highlightthickness=0,
                          command=lambda: get_graph_label(-1))
    _left_btn.pack(anchor='s', side=tk.LEFT, expand=True, pady=2, padx=2)  # puts in center
    # merge graphs
    _merge_btn = tk.Button(graphControlFrame, text='Merge', font=('Silom', 16), bg="white", fg="black",
                           highlightthickness=0, command=lambda: get_graph_label(0))
    _merge_btn.pack(anchor='s', side=tk.LEFT, expand=True, pady=2, padx=2)  # puts in center
    # right arrow
    _right_btn = tk.Button(graphControlFrame, text='>', bg="white", fg="black", font=('silom', 16),
                           highlightthickness=0, command=lambda: get_graph_label(1))
    _right_btn.pack(anchor='s', side=tk.RIGHT, expand=True, pady=2, padx=2)  # lk

    graphContainer = tk.Frame(root, bg="white")
    graphContainer.pack(fill=tk.BOTH, expand=True)

    waves = [dc.plot_spectrogram(), dc.plot_waveform()]
    no_data_graphs = [dc.plot_rt60_high(), dc.plot_rt60_low(), dc.plot_rt60_mid()]

    # test displaying plot in app window
    display_spectrogram()

    root.mainloop()  # run the program
