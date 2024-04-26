# clean_data.py

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
	# Load the audio data directly from the WAV file
	audio = AudioSegment.from_wav(input_file)

	# Check if the audio object has tags (metadata)
	# if hasattr(audio, 'tags') and audio.tags:
	if audio.channels or audio.sample_width or audio.frame_rate or audio.frame_length or len(audio):
		# If metadata/tags exist, remove them by exporting without tags
		clean_wav_file = "clean_sound.wav"
		audio.export(clean_wav_file, format="wav", tags={})
		return clean_wav_file
	else:
		# If no metadata/tags exist, simply return the input file
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
