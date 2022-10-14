#!/usr/bin/env pypy3

# Scott's MusicBox
# heal-Philharmonia-samples.py by Scott Yannitell
# Copyright 2022 all rights reserved

# It turns out that after tearing out the samples and discovering
# how many of the registeres came with vast expanses with misssing samples
# I can see why my music had an unpredictable intensity at times that was very
# degrading for the overall sound. This script is like a surgeon, taking a
# patient that that has a wound, and cleaning the wound further and filling in
# the missing parts with new flesh. 

# The surgeon has to use other parts of the body to fill the patient's wound
# so a selection is prefered for upper parts rather than lower parts for the 
# replacement.

# if the replacement was a shift up it is labeled -d- or -dd- or -ddd- for
# its relative amount of shift

# if the replacement was a shift down it is labeled -u- or -uu- or -uuu- for
# its relative amount of shift

# if an expression has too few notes it must be amputated for the health of the
# body.

# when complete, the body isn't perfect, but it has the most vital parts working

import os
import sys
from os.path import exists
from instrument_data_and_scales import instruments
from instrument_data_and_scales import notes
from instrument_data_and_scales import ranges
from instrument_data_and_scales import nuller
from instrument_data_and_scales import inter_semitone_ratio
from instrument_data_and_scales import wav_setting
from instrument_data_and_scales import compression_setting

bad_samples = open("scale-check-results.dat").read().splitlines()


os.system("rm -rf samples/Philharmonia_healed"+nuller)

# instead of copying the files are reincoded. Should the reecoding fail the file simply
# vanishes from the healed directory
# bad files will mess things up further up the chain of filters
for folder in os.listdir("samples/Philharmonia_original/"):
    os.system("mkdir -p samples/Philharmonia_healed/"+folder)
    for file in os.listdir("samples/Philharmonia_original/"+folder):
        sox = "sox samples/Philharmonia_original/"+folder+"/"+file+compression_setting+" samples/Philharmonia_healed/"+folder+"/"+file

        if os.system(sox) != 0:
            print(file, "was poopy")
        else:
            print(file)



for bad_sample in bad_samples:
    if ".mp3" in bad_sample:
        print("2.heal-Philharmonia-samples.py error 1: please remove all .mp3 substrings from 1a.scale-check-results.dat")
        quit(1)
    for instrument in instruments:
        if instrument in bad_sample:
            os.system("rm samples/Philharmonia_healed/"+instrument+"/"+bad_sample+".mp3")

exlusion_filter = ["1_mezzo-piano_molto-vibrato","ponticello", "tratto", "tasto", "harmonic","shifted", "martele", "cresc-decresc", "fluttertonguing", "slap-tongue", "phrase", "au-talon", "non-vibrato", "long_decrescendo_arco-normal", "mezzo-piano_pizz-glissando", "very-long_decrescendo_arco-normal", "very-long_mezzo-piano_arco-tremolo", "15_forte_molto-vibrato"]

# clear out unusable phrases
for instrument in instruments:
    for file1 in os.listdir("samples/Philharmonia_healed/"+instrument):
        for excluded in exlusion_filter:
            if excluded in file1: 
                print("delete "+file1)
                os.system("rm \"samples/Philharmonia_healed/"+instrument+"/"+file1+"\"")



#######################
# collect expressions #
#######################
os.system("rm recheck.sh"+nuller)
file1 = open("recheck.sh", "a")
file1.write("#!/bin/bash")

# step one gather all expressions
expressions = {}
for instrument in instruments:
    file1.write("\n")
    expressions[instrument] = []
    for note_index in range(  notes.index(ranges[instrument]["min"]),   notes.index(ranges[instrument]["max"])   + 1):
        for sample in os.listdir("samples/Philharmonia_healed/"+instrument+"/"):
            if notes[note_index] in sample:
                base_expression = sample.split(instrument+"_"+notes[note_index]+"_")[1]
                if base_expression not in expressions[instrument]:
                    print(base_expression)
                    expressions[instrument].append(base_expression)
                        
# step two find out how filled the expressions are   
deleters = []        
for instrument in instruments:
    for expression in expressions[instrument]:
        
        for sample in os.listdir("samples/Philharmonia_healed/"+instrument+"/"):
            counter = 0
            if expression in sample:
                counter += 1
        register = notes.index(ranges[instrument]["max"]) - notes.index(ranges[instrument]["min"])
        if counter/register < 0.5:
            expressions[instrument].remove(expression)
            deleters.append(expression)
            
for delete in deleters:
    os.system("rm "+delete)

os.system("rm recheck.sh")
file1 = open("recheck.sh", "a")
file1.write("#!/bin/bash\n")

for instrument in instruments:
    file1.write("\n# "+instrument+"\n")
    for expression in expressions[instrument]:
        file1.write("./scale-check.py Philharmonia_healed "+instrument+" "+expression+"\n")

file1.close()
os.system("chmod +x recheck.sh")

searcher = {}
for instrument in expressions:
    for expression in expressions[instrument]:
        for note_index in range(  notes.index(ranges[instrument]["min"]),   notes.index(ranges[instrument]["max"])+1):
            sample_file = "samples/Philharmonia_healed/"+instrument+"/"+instrument+"_"+notes[note_index]+"_"+expression
            if not exists(sample_file):
                searcher[sample_file] = {}
                searcher[sample_file]["lower_replacement"]       = "none"
                searcher[sample_file]["lower_replacement_shift"] = None
                searcher[sample_file]["lower_replacement_score"] = 99999
                searcher[sample_file]["upper_replacement"]       = "none"
                searcher[sample_file]["upper_replacement_shift"] = None
                searcher[sample_file]["upper_replacement_score"] = 99999
                counter1 = 0
                for i in range(note_index, 128):
                    replacement_file = instrument+"_"+notes[i]+"_"+expression   
                    replacement_file_and_path = "samples/Philharmonia_healed/"+instrument+"/"+replacement_file
                    if exists(replacement_file_and_path):
                        searcher[sample_file]["upper_replacement"]       = replacement_file_and_path
                        searcher[sample_file]["upper_replacement_shift"] = -1*counter1
                        searcher[sample_file]["upper_replacement_score"] = counter1
                        print("down: "+sample_file)
                        nothing1 = False
                        break

                    counter1+=1
                    
                    
                counter2 = 0
                nothing2 = True
                for i in range(note_index, 0,-1):
                    
                    replacement_file = instrument+"_"+notes[i]+"_"+expression
                    replacement_file_and_path = "samples/Philharmonia_healed/"+instrument+"/"+replacement_file
                    if exists(replacement_file_and_path):
                        searcher[sample_file]["lower_replacement"]       = replacement_file_and_path
                        searcher[sample_file]["lower_replacement_shift"] = counter2
                        searcher[sample_file]["lower_replacement_score"] = counter2*1.3
                        print("up:   "+sample_file)
                        break

                    counter2+=1
                
                if searcher[sample_file]["lower_replacement_score"] == 99999 and searcher[sample_file]["upper_replacement_score"] == 99999:
                    print("2.heal-Philharmonia-samples.py error 2: nothing found to replace "+sample_file)
                    quit(1)
            else:
                print("ok:   "+sample_file)      
               
for sample_file in searcher:
    lower_replacement_score = searcher[sample_file]["lower_replacement_score"]
    upper_replacement_score = searcher[sample_file]["upper_replacement_score"]
    if upper_replacement_score >= lower_replacement_score:
        sign = "lower"
        shift = searcher[sample_file]["lower_replacement_shift"]
        tag  = round(searcher[sample_file]["lower_replacement_score"], 3)
        tag  = "-z"+str(shift)
        
    elif upper_replacement_score < lower_replacement_score:
        sign = "upper"
        shift = searcher[sample_file]["upper_replacement_shift"]
        tag  = round(searcher[sample_file]["upper_replacement_score"], 3)
        tag  = "-z"+str(shift)

    replacement_file_and_path = sample_file.split(".mp3")[0]+tag+".mp3"

    # I wish to prevent super shifts and let the sample finder find something close to the right intensity
    if abs(shift) < 18:
        print(replacement_file_and_path)
        os.system("sox "+searcher[sample_file][sign+"_replacement"]+wav_setting+" /tmp/healer.wav")
        os.system("rubberband --pitch "+str(shift)+" /tmp/healer.wav /tmp/tmpwav.wav "+nuller)
        os.system("sox /tmp/tmpwav.wav "+compression_setting+replacement_file_and_path)
    
                
