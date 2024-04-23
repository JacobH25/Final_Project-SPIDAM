# clean_data.py
# Programmer Name: Jacob Hensley
# File Created: 4/22/2024

# import objects and headers
from pydub import AudioSegment


# function to reformat file from .mp3 to .wav
def reformat_file(input_file):
	# if input file is mp3
	if ".mp3" in input_file:
		# extracts audio from mp3
		audio = AudioSegment.from_mp3(input_file)
		# initializes wav file to hold audio
		wav_file = "sound.wav"
		# exports audio to wav file format
		audio.export(wav_file, format="wav")
		# returns new wav file
		return wav_file
	# if input file is already wav
	else:
		# returns input file that is already wav
		return input_file


# function to remove metadata from .wav file
def remove_metadata(input_file):
	# extracts raw audio from file
	audio = AudioSegment.from_wav(input_file)
	# if metadata tags are found in file
	if audio.tags:
		# initializes new .wav file for cleaned audio
		clean_wav_file = "clean_sound.wav"
		# exports audio without metadata to new clean wav file
		audio.export(clean_wav_file, format="wav", tags={})
		# returns new clean wav file
		return clean_wav_file
	# if no metadata is found
	else:
		# returns input file
		return input_file


# function to convert multi-channel to mono-channel
def handle_multi_chan(input_file):
	# extracts raw audio from file
	audio = AudioSegment.from_file(input_file)
	# if audio had multi-channel
	if audio.channels > 1:
		# initializes new file to hold mono-audio
		clean_mono_file = "clean_mono.wav"
		# converts multi-channel audio to mono-channel audio
		mono_wav = audio.set_channels(1)
		# exports new mono-channel audio to new file
		mono_wav.export(clean_mono_file, format="wav")
		# returns clean mono file
		return clean_mono_file
	# if raw audio is already mono-channel
	else:
		# returns input file
		return input_file
