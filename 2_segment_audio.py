from pydub import AudioSegment
import openai
import glob
import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()

DATA_DIR = args.path + '/data/videos'

files = glob.glob(os.path.join(DATA_DIR, '*.mp4'))
print(files)

for file_name in files:
	
	print(f"\nProcessing {file_name}...")

	file_stats = os.stat(file_name)
	file_size_MB = round(file_stats.st_size / (1024 * 1024), 2)

	filenameT = file_name.replace(".mp4", ".txt")
	file_segment = file_name.replace(".mp4", "_Seg0.mp4")
	alreadySegmented = os.path.isfile(file_segment)

	if file_size_MB >= 24.0 and alreadySegmented == False :

		audio_file = AudioSegment.from_file(file_name, "mp4")

		print("Opened audio file...")
		recording_length_min = len(audio_file) / (60 * 1000)
		print(f"{file_name} is {recording_length_min} min long")

		twenty = 20 * 60 * 1000
		chunk = audio_file[:twenty]
		chunk.export(file_segment, format="mp4")

		chunk = audio_file[twenty:]
		remainder_min = len(chunk) / (60 * 1000)
		if remainder_min > 20:
			# special case for rare recordings > 40 mins
			# note: all lectures are < 60 mins
			chunk = audio_file[twenty:2*twenty]
			file_segment = file_segment.replace("_Seg0", "_Seg1")
			chunk.export(file_segment, format="mp4")
			chunk = audio_file[2*twenty:]
			file_segment = file_segment.replace("_Seg1", "_Seg2")
			chunk.export(file_segment, format="mp4")
		else :
			chunk = audio_file[twenty:]
			file_segment = file_segment.replace("_Seg0", "_Seg1")
			chunk.export(file_segment, format="mp4")

		print("Writing to file...")
	else :
		print(f"{file_name} segmentation not needed...")
