"""This script takes the path of the directory where the Audios are contained
and Converts all the Audios to a MP3 format and stores all the Converted Audios
to a directory specified.

Usage
-----
Enter the Source Directory path: ''
Enter the Destination Directory path: ''
"""
print('The script starts.')

import time

tik = time.time()
print(tik)

import os
import pydub

source_path = input('Enter the Source Directory path: ')
destination_path = input('Enter the Destination Directory path: ')

# Listing all the files from the Source Directory
files = os.listdir(source_path)
# Now this line of codes also catches some files those are not necessary and
# even not visible by the File Manager GUI. So let's make another list that
# will exclude thsoe files.
files = [file for file in files if file[-1] != '~']

no_of_files = len(files)
print('There are a total of {} files in the Source Directory.'.format(no_of_files))

print('Process on progress..')

for file in files:
    file_path = source_path + file
    inst_audio = pydub.AudioSegment.from_file(file_path)

    file_saving_path = destination_path + file.split('.')[0] + '.mp3'
    inst_audio.export(file_saving_path, format='mp3')

tok = time.time()
print(tok)

time_taken = (tok - tik) * (10 ** (-1))

print('Script ends. Took {} seconds.'.format(time_taken))
