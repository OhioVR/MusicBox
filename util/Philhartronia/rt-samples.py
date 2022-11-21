#!/usr/bin/env python3

# for performer-test

import os
import json
import KEYS
from instrument_data_and_scales import instruments
from instrument_data_and_scales import notes
os.system("rm -rf samples/Philhartronia-rt")
os.system("mkdir  samples/Philhartronia-rt")

# Reading the JSON database file
def read_json(file):
    with open(file, 'r') as f:
        result = json.load(f)
    return result

metadata = read_json("db/Philhartronia.json")
for instrument in instruments:
    
    os.system("mkdir samples/Philhartronia-rt/"+instrument)
    for i in range(0,12*9):
         samples = metadata[notes[i]][instrument]
         for sample in samples:
             file = sample[KEYS.SAMPLE]
             start = sample[KEYS.SAMPLE_OFFSET]
             end = sample[KEYS.NOTE_LENGTH]
             print(file)
             os.system("sox samples/Philhartronia/"+instrument+"/"+file+" -r 11025 samples/Philhartronia-rt/"+instrument+"/"+file.split(".")[0]+".wav trim "+str(start))