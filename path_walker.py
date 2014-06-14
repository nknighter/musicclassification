import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('/Users/Samat/Music/'):
    for filename in fnmatch.filter(filenames, '*.wav'):
        matches.append(os.path.join(root, filename))

dst = '/Users/Samat/Documents/soundprocessing/src_wav/'
for path in matches:
    os.rename(path, dst + os.path.basename(path))