#!/usr/bin/env python3

# Scott's MusicBox
# get_sample.py by Scott Yannitell
# Copyright 2022 all rights reserved

# This is the script which hunts down the most ideal sample for the given
# paramters of note, instrument, intensity, and length. Ideal in this case
# refers to minimizing tempo stretching, and getting as close as possible to the
# desired intensity. It accomplishes this without SQL and seems pretty fast when
# exeucted from the main script by pypy. So as it stands now it is about as good
# as it can be. It accounts for plucked instruments or styles along with
# variable length sounds.


import json
import os
from random import uniform as randuniform
import collections
import bisect
from time import sleep
from  util.Philhartronia import KEYS
import copy
from util.Philhartronia.instrument_data_and_scales import notes
from util.Philhartronia.instrument_data_and_scales import chromatic_scale
from util.Philhartronia.instrument_data_and_scales import ranges
from util.Philhartronia.instrument_data_and_scales import instruments
from util.Philhartronia.instrument_data_and_scales import nuller
from util.Philhartronia.instrument_data_and_scales import inter_semitone_ratio
from util.Philhartronia.instrument_data_and_scales import the_8ths_relationship

# just for spot checking bad samples before even the addendium database is run
# it makes the search far slower so remove the comment to replace the
# proceeding line only temporarily to examine little changes during
# debugging of the sample library
bad_samples = []#open("/media/scott/Philhartronic/util/stinkers.dat").read().splitlines()

# Reading the JSON database file
def read_json(file):
    with open(file, 'r') as f:
        result = json.load(f)
    return result

print("importing large database")
metadata = read_json("util/Philhartronia/db/Philhartronia.json")

sample_manager = {}
for note_index in range(0, len(notes)):
    sample_manager[note_index] = {}
    for instrument in instruments:
        sample_manager[note_index][instrument] = []

def get_sample(note_index, instrument, target_midi_loud, target_length, settings, instrument_designation):
    global sample_manager, metadata, shadow_metadata, notes
    try:
        expression_multiplier = settings["expression_multiplier"]
    except:
        expression_multiplier = 1
    # some expressions I did not like
    forbidden     = ["snap"]

    #if note_index < notes.index(ranges[instrument]["min"])-1:
    #    return None, None, None, None, None, None, None
    #if note_index > notes.index(ranges[instrument]["max"])+1:
    #    return None, None, None, None, None, None, None
    print("note_index", note_index)
    samples = metadata[notes[note_index]][instrument]

    start_length_change = 9999999999999999999
    finished = False
    exhastion_flipper = True

    print(note_index, instrument, target_midi_loud, target_length)
    ########################################
    # first determine the mode of the file #
    # there are 11K normal files           #
    ########################################
    mode = "normal"
    try:
        if instrument in ["violin", "viola", "cello", "double-bass"] and target_length <= settings[instrument_designation]["pizz_threshold"]: mode = "pizz-normal"
    except:
        pass

    if instrument == "mandolin":
        mode = "pizz-normal"
    if instrument == "mandolin" and target_length >= settings[instrument_designation]["pizz_threshold"]:
        mode = "tremolo"

    #print("mode", mode)

    try:
        special_mode = settings[instrument_designation]["special_mode_name"]
        if settings[instrument_designation]["special_mode_min_length"] > target_length:
            mode = special_mode
    except:
        pass

    # todo short-note clamping (lengthen short notes) for violins etc..

    ##############################################################
    # search for the closest plain vannilla sample tempo         #
    # make search find closest length and intensity combination  #
    # it is ok to search in alternative pitches as they often    #
    # have a diversity of lengths that could be helpful          #
    # Not to mention, we nearly always get at least 4 variations.#
    # with 4 variations x 12 shifts that is a possible           #
    # selection of up to 96 samples per intensity 96 times 6     #
    # intensities is 576 possiblitys.                            #
    #############################################################
    best_score = 999999
    best_index = None
    prime_index = None
    for search_index in range(0, len(samples)):
        sample  = samples[search_index][KEYS.SAMPLE]
        # find purely un changed tempo files
        # reason being if there is any pitch variation, speeding or slowing
        # makes it sound uglier than if you don't do that as much.
        #if "t1.0-" not in sample: continue

        length    = samples[search_index][KEYS.NOTE_LENGTH]
        intensity = samples[search_index][KEYS.LOUDNESS_ID]

        unallowed = False

        banned_by_forbidden_effect = False
        for effect in settings["banned_effects"]:
            if effect in sample:
                banned_by_forbidden_effect = True

        for effect in settings["effect_exceptions"]:
            if effect in sample:
                banned_by_forbidden_effect = False

        if banned_by_forbidden_effect: continue

        # some sounds I wish not to use
        for blocked_sample in forbidden:
            if blocked_sample in sample:
                unallowed = True

        if samples[search_index][KEYS.LOUDNESS_ID] == 0: continue

        for bad_sample in bad_samples:
            if bad_sample in sample:
                unallowed = True
        if unallowed: continue
        if mode == "pizz-normal" and instrument != "mandolin":
            if "pizz-normal" not in sample: continue
        if mode == "normal":
            if "pizz" in sample: continue
        if samples[search_index][KEYS.LOUDNESS_ID] == 0: unallowed = True

        stub = samples[search_index][KEYS.SAMPLE].split("-t")[0]
        if stub in sample_manager[note_index][instrument] and instrument != "guitar" \
        and instrument != "mandolin" and instrument != "banjo": continue

        if mode == "tremolo" and "tremolo" not in sample: continue

        if length > 0 and target_length > 0:
            tempo_score = (length/target_length) * expression_multiplier
            if tempo_score < 1:
                # slowing down samples is worse sounding than speeding them up
                tempo_score = ((target_length / length) * expression_multiplier)*1.666666
        else:
            tempo_score = expression_multiplier

        # the multiplier has to be bigger with fewer and fewer
        # right sized samples in that register
        intensity_score = ( abs(intensity - target_midi_loud) / 128 ) * 8

        final_score = intensity_score + tempo_score
        #print(length, target_length, tempo_score, intensity_score, final_score)
        if final_score < best_score:
            best_score = final_score
            best_index = search_index

        if mode != "pizz-normal" and target_length > 0:
            if final_score <= best_score:
                best_score = final_score
                best_index = search_index
                prime_index = best_index
                print(samples[search_index])
        elif mode == "pizz-normal" or instrument == "guitar" or instrument == "banjo":
            if instrument == "mandolin" and "tremolo" in sample: continue
            if final_score <= best_score:
                best_score  = final_score
                best_index = search_index
                prime_index = best_index


    ############################ use this to find the best speed note for our
    # tempo variation selector # note length after finding the closest native
    ############################ sample. All non native samples are inferior.
    if best_index == None:
        print("error 204: no sample found meeting critera")
        return None, None, None, None, None, None, None

    #best_stub = samples[best_index][KEYS.SAMPLE].split("-t")[0]

    #if mode != "pizz-normal" and target_length > 0:
    #    best_tempo_score = 9999
    #    for search_index in range(0, len(samples)):
    #        sample = samples[search_index][KEYS.SAMPLE]
    #        length = samples[search_index][KEYS.NOTE_LENGTH]

    #        if best_stub not in sample: continue

    #        if length > 0 and target_length > 0:
    #            tempo_score = (length/target_length)
    #            if tempo_score < 1:
    #                tempo_score = (target_length / length)
    #        else:
    #            tempo_score = 1

            # do not overly stretch strings as they sound sickly if you do
    #        if instrument in ["violin", "viola", "cello", "double-bass"]:
    #            attempted_best_tempo = length / samples[prime_index][KEYS.NOTE_LENGTH]
    #            if attempted_best_tempo != 1.0: continue
    #        if tempo_score < best_tempo_score:
    #            best_index = search_index
    #            best_tempo_score  = tempo_score

    #elif mode == "pizz-normal" or instrument == "guitar" or instrument == "banjo":
    #    pass

    #print("is now", samples[best_index][KEYS.SAMPLE])

    #if best_index == None:
    #    print("error 215: no sample found meeting critera")
    #    return None, None, None, None, None, None, None

    # the sample file
    sample      = samples[best_index][KEYS.SAMPLE]

    # OFFSET the beginning of the sound happens a few miliseconds after the start of wav
    #        so the offset is used to compensate this for good timing control
    offset      = samples[best_index][KEYS.SAMPLE_OFFSET]

    # TEMPO It is ok to allow ffmpeg's version of rubber band to stretch samples
    #       by 25% up or down but not much further. It is hoped that this is normally
    #       the case from the tempo variation selector. No matter how many derived
    #       samples I have it is needed to fine tune the tempo of the sample for
    #       timing purposes.
    if target_length != 0:
        tempo       = samples[best_index][KEYS.NOTE_LENGTH] / target_length
    else:
        tempo = 1

    # PLUCKED If the database determines a sample to be plucked, make note of it here:
    plucked     = samples[best_index][KEYS.PLUCKED]

    if mode == "pizz" or instrument == "guitar" or instrument == "banjo": plucked = True
    if mode != "tremolo" and instrument == "mandolin": plucked = True

    if plucked:
        tempo = 1

    # SCORE increasing numbers means bad in the score. the first value is the tempo level
    #       the second value is the pitch level. ideally it would be zero for both
    #       but sample length may have to increase or decrease...
    #       depending on the computed allowed tempo range
    #score       = 16-len(tempo_levels)
    score        = 1

    # LOUD_ADJUST the loudness might need to be bumped up a little or down depending on how
    #             close it is to the midi loud. In here we only have 6 different intensities
    #             So we compare the translated midi loud of the note to the requested one

    loud_adjust =  target_midi_loud / samples[best_index][KEYS.LOUDNESS_ID]
    if plucked:
        loud_adjust /=3

    # TRUE_LENGTH the true length of the sample is based on it's audio file.
    #             the note length is always less
    #             I put it there for some other function so best leave it in
    true_length = samples[best_index][KEYS.FILE_TRUE_DURATION]

    # don't repeat play a sample unless we find it after the 12th time of looking for it
    #sample_manager[note_index][instrument].append(best_stub)

    # if the buffer fils up pas 12, pop off the first element.
    #if len(sample_manager[note_index][instrument]) > settings["round_robin"]:
    #    del sample_manager[note_index][instrument][0]

    if not plucked:
        result_length = samples[prime_index][KEYS.NOTE_LENGTH]
        # clamp low tempos:
        if instrument in ["violin", "viola", "double-bass", "cello"]:
            if tempo < 0.7:
                tempo = 0.7


    print(notes[note_index], sample, offset, tempo, plucked, score, loud_adjust, true_length)
    return sample, offset, tempo, plucked, score, loud_adjust, true_length
