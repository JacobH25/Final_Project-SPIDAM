# SPIDAM (Sound Processing and Interactive Data Analysis Module)

SPIDAM is a Python based application designed for sound processing and interactive data analysis. It provides functionalities for uploading sound files, visualizing waveforms, spectrograms, and performing analysis such as RT60 calculation for low, mid, and high frequencies.

## Features

- **Upload Sound Files:** Users can easily upload sound files in various formats including MP3 and WAV.
  
- **Visualization:** SPIDAM offers visualization of waveforms and spectrograms for the uploaded sound files.
  
- **RT60 Calculation:** Calculation of RT60 (reverb time) for low, mid, and high frequencies to analyze the acoustic properties of the sound.

## Dependencies

Before running SPIDAM, make sure to have ffmpeg installed on your system.

- **easygui:** For opening a file explorer dialog for file selection.
  
- **pydub:** For audio file manipulation and conversion.
  
- **numpy:** For numerical calculations and array manipulation.
  
- **matplotlib:** For plotting waveforms, spectrograms, and line graphs.
  
- **scipy:** For scientific computing tasks such as reading WAV files.

To install the required dependencies, run the following command in your terminal or command prompt from the directory where the requirements.txt file is located:

pip install -r requirements.txt
