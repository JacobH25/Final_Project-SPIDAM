# upload_file.py
# Programmer Name: Jacob Hensley
# File Created: 4/20/2024

# import easygui for opening File Explorer
import easygui as eg
import clean_data as clean


uploaded_file = None  # Global variable to store the uploaded file path


def upload_file():
    uploaded_file = eg.fileopenbox()

    file = uploaded_file

    # reformat file to .wav
    wav_file = clean.reformat_file(file)
    # removes metadata from .wav file
    clean_wav = clean.remove_metadata(wav_file)
    # converts clean .wav file to single- or mono-channel
    clean_mono_wav = clean.handle_multi_chan(clean_wav)

    # returns selected fileInitializes
    return clean_mono_wav
