# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import glob
import os.path

dir = './data/videos/'
files = glob.glob(os.path.join(dir, '*.mp4'))
print(files)

for file_name in files:
	
	print(file_name)

	file_stats = os.stat(file_name)
	file_size_MB = round(file_stats.st_size / (1024 * 1024), 2)

	filenameT = file_name.replace(".mp4", ".txt")

	# test for segment transcription
	if "_Seg" not in filenameT and file_size_MB >= 24:
		# this is a LARGE full or unsegmented file - have we already transcribed a segment?
		filenameT = file_name.replace(".mp4", "_Seg0.txt")

	alreadyTranscribed = os.path.isfile(filenameT)

	if file_size_MB < 24 and alreadyTranscribed == False :

		audio_file = open(file_name, "rb")

		print("Opened audio file...")

		transcript = openai.Audio.transcribe("whisper-1", audio_file)

		filenameT = file_name.replace(".mp4", ".txt")
		print(f"Writing to file... {filenameT}")

		with open(filenameT, 'w') as file:
			file.write(transcript.text)

	elif alreadyTranscribed :
		print(f"{file_name} is already transcribed")

	else :
		print(f"{file_name} is too big for OpenAI Whisper ({file_size_MB}MB); transcribing the segments instead")
