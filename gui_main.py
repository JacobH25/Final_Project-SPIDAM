# gui_main.py

import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import data_calc as dc


def upload():
    dc.handle_file_upload()
    update_status_bar("New file successfully uploaded!")
    display_blank_left()
    display_blank_right()


def display_blank_left():
    fig = dc.plot_blank()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=2, sticky="w")
    canvas.draw()


def display_blank_right():
    fig = dc.plot_blank()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky="e")
    canvas.draw()


def display_waveform():
    fig = dc.plot_waveform()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=2, sticky="w")
    canvas.draw()


def display_spectrogram():
    fig = dc.plot_spectrogram()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=2, sticky="w")
    canvas.draw()


def display_rt60_lmh_data():
    dc.update_high_data()
    dc.update_low_data()
    dc.update_low_data()
    fig = dc.plot_rt60_lmh_data()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky="e")
    update_status_bar(f"RT60 = {dc.rt60_avg()}  ||  {dc.rt60_diff(dc.rt60_avg())}")
    canvas.draw()


def display_rt60_lmh():
    dc.update_high_data()
    dc.update_low_data()
    dc.update_low_data()
    fig = dc.plot_rt60_lmh()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky="e")
    update_status_bar(f"RT60 = {dc.rt60_avg()}  ||  {dc.rt60_diff(dc.rt60_avg())}")
    canvas.draw()


def display_rt60_high_data():
    dc.update_high_data()
    fig = dc.plot_rt60_high_data()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky="e")
    update_status_bar(f"RT60 = {dc.rt60_high()}  ||  {dc.rt60_diff(dc.rt60_high())}")
    canvas.draw()


def display_rt60_high():
    dc.update_high_data()
    fig = dc.plot_rt60_high()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky="e")
    update_status_bar(f"RT60 = {dc.rt60_high()}  ||  {dc.rt60_diff(dc.rt60_high())}")
    canvas.draw()


def display_rt60_mid_data():
    dc.update_mid_data()
    fig = dc.plot_rt60_mid_data()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky="e")
    update_status_bar(f"RT60 = {dc.rt60_mid()}  ||  {dc.rt60_diff(dc.rt60_mid())}")
    canvas.draw()


def display_rt60_mid():
    dc.update_mid_data()
    fig = dc.plot_rt60_mid()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky="e")
    update_status_bar(f"RT60 = {dc.rt60_mid()}  ||  {dc.rt60_diff(dc.rt60_mid())}")
    canvas.draw()


def display_rt60_low_data():
    dc.update_low_data()
    fig = dc.plot_rt60_low_data()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky="e")
    update_status_bar(f"RT60 = {dc.rt60_low()}  ||  {dc.rt60_diff(dc.rt60_low())}")
    canvas.draw()


def display_rt60_low():
    dc.update_low_data()
    fig = dc.plot_rt60_low()
    canvas = FigureCanvasTkAgg(fig, master=graphControlFrame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky="e")
    update_status_bar(f"RT60 = {dc.rt60_low()}  ||  {dc.rt60_diff(dc.rt60_low())}")
    canvas.draw()


def update_status_bar(message):
    status_bar.config(text=message)


if __name__ == '__main__':
    root = Tk()  # makes initial object
    root.geometry("1375x760")
    root.title(' ')

    mainFrame = tk.Frame(root, bg="grey")  # for top part.. title, choose file, data
    mainFrame.grid(row=0, column=0, columnspan=7, sticky="ew")  # padx = 10, pady = 10
    mainTitle = tk.Label(mainFrame, text='SPIDAM', font=('Silom', 24, 'bold'), highlightthickness=0, bg="grey",
                         fg="black")
    mainTitle.grid(row=0, column=2, padx=540, pady=2, sticky="n")

    _file_btn = tk.Button(mainFrame, text='UPLOAD', bg="#38ABFF", font=('silom', 16), highlightthickness=0,
                          command=upload)
    _file_btn.grid(row=1, column=0, sticky='w', padx=2)  # assigns left side

    # _data_btn = tk.Button(mainFrame, text='Data', bg="white", fg="black", font=('silom', 16), highlightthickness=0)
    # _data_btn.grid(row=1, column=7, sticky="e", padx=100)  # assigns right side

    # graph display
    graphFrame = tk.Frame(root, bg="white")
    graphFrame.grid(row=1, column=0, columnspan=7, sticky="ew")  # padx = 10, pady = 10

    _graph_title = tk.StringVar(value="          ")
    _spec_title = tk.Label(graphFrame, textvariable=_graph_title, font=('Silom', 16), highlightthickness=0, bg="white",
                           fg="black")
    _spec_title.grid(row=0, column=1, padx=0, pady=10)

    _spectrogram_btn = tk.Button(graphFrame, text='       Spectrogram       ', bg="white", fg="black",
                                 font=('silom', 16), highlightthickness=0, command=display_spectrogram)
    _spectrogram_btn.grid(row=0, column=0, padx=15)  # lk

    _waveform_btn = tk.Button(graphFrame, text='       Waveform       ', bg="white", fg="black", font=('silom', 16),
                              highlightthickness=0, command=display_waveform)
    _waveform_btn.grid(row=0, column=2, padx=15)  # puts in center

    _line_title = tk.Label(graphFrame, text='Frequency & RT60 Plots', font=('Silom', 16), highlightthickness=0,
                           bg="white",
                           fg="black")
    _line_title.grid(row=0, column=7, padx=300, pady=10)

    # freq = tk.StringVar(value="RT60 M")  # baseline
    # _line_descript = tk.Label(graphFrame, textvariable=freq, font=('Silom', 16), highlightthickness=0, bg="white",
    # 						  fg="black")
    # _line_descript.grid(row=0, column=4, padx=10, pady=10)

    graphControlFrame = tk.Frame(root, bg="white")  # frame for graph controls
    graphControlFrame.grid(row=2, column=0, columnspan=7, sticky="e")

    # reverb_label = tk.Label(graphControlFrame, text="RT60: ", font=('Silom', 16), highlightthickness=0, bg="white",
    # 						fg="black")
    # reverb_label.grid(row=0, column=0, padx=10, pady=2)

    # plot display buttons without data labels
    _low_btn = tk.Button(graphControlFrame, text='      Low Freq      ', bg="white", fg="black", font=('silom', 16),
                         highlightthickness=0, command=display_rt60_low)
    _low_btn.grid(row=1, column=1, padx=2, pady=2)
    _mid_btn = tk.Button(graphControlFrame, text='      Mid Freq      ', font=('Silom', 16), bg="white", fg="black",
                         highlightthickness=0, command=display_rt60_mid)
    _mid_btn.grid(row=1, column=2, padx=2, pady=2)
    _high_btn = tk.Button(graphControlFrame, text='     High Freq     ', bg="white", fg="black", font=('silom', 16),
                          highlightthickness=0, command=display_rt60_high)
    _high_btn.grid(row=1, column=3, padx=2, pady=2)
    _merge_btn = tk.Button(graphControlFrame, text='    Merge Freq    ', font=('Silom', 16), bg="white", fg="black",
                           highlightthickness=0, command=display_rt60_lmh)
    _merge_btn.grid(row=1, column=4, padx=2, pady=2)

    # plot display buttons with data labels
    _lowdata_btn = tk.Button(graphControlFrame, text='  Low Freq Data  ', bg="white", fg="black", font=('silom', 16),
                             highlightthickness=0, command=display_rt60_low_data)
    _lowdata_btn.grid(row=2, column=1, padx=2, pady=2)
    _middata_btn = tk.Button(graphControlFrame, text='  Mid Freq Data  ', font=('Silom', 16), bg="white", fg="black",
                             highlightthickness=0, command=display_rt60_mid_data)
    _middata_btn.grid(row=2, column=2, padx=2, pady=2)
    _highdata_btn = tk.Button(graphControlFrame, text=' High Freq Data ', bg="white", fg="black", font=('silom', 16),
                              highlightthickness=0, command=display_rt60_high_data)
    _highdata_btn.grid(row=2, column=3, padx=2, pady=2)
    _mergedata_btn = tk.Button(graphControlFrame, text='Merge Freq Data', font=('Silom', 16), bg="white", fg="black",
                               highlightthickness=0, command=display_rt60_lmh_data)
    _mergedata_btn.grid(row=2, column=4, padx=2, pady=2)

    graphContainer = tk.Frame(root, bg="white")
    graphContainer.grid(row=3, column=0, columnspan=3, sticky="nsew")

    status_bar = tk.Label(root, text="...waiting for file upload...", bd=1,
                          relief=tk.SUNKEN, anchor=tk.CENTER)
    status_bar.grid(row=5, column=0, columnspan=7, sticky="ew", pady=25)

    display_blank_right()
    display_blank_left()

    root.mainloop()  # run the program
