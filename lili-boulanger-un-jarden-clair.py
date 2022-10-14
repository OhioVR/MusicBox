#!/usr/bin/env pypy3

from util import arranger
import os
import sys

os.system("clear")


# midi file credit: ?
# samples provided by the London Philharmonia Orchestra

###############################
# Create settings dictionary. #
###############################
settings = arranger.defaults

settings["project_name"] = "un_Jardin_Clair"
settings["input_midi"]   = "MIDI/musescore.com/Dun_Jardin_Clair_-_Lili_Boulanger.mid"

settings["banned_effects"]                      = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "tremolo", "phrase", "non-vibrato", "harmonic", "tratto", "very-long_mezzo-forte_arco-normal", "snap","trill", "glissando", "staccato", "sul", "au"]

# "violin", "viola", "cello", "double-bass", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "flute", "french-horn", "oboe", "saxophone", "trombone", "trumpet", "tuba", "guitar", "mandolin", "banjo"

settings["instruments"] = ["guitar", "violin", "viola", "cello", "double-bass"]

settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = 0
settings["reverberance"]                        = 50
settings["reverb-room-scale"]                   = 100
settings["reverb-stereo-depth"]                 = 100
settings["master_tempo"]                        = 1.0
settings["master_volume"]                       = 0.8

settings["guitar"]["octave"]  = -1
settings["violin"]["octave"]                = 0
settings["violin"]["length_upperlimit"]   = 999
settings["violin"]["length_lowerlimit"]   = 0
settings["violin"]["velocity_multiplier"] = 1.0
settings["violin"]["volume"]              = .5
settings["violin"]["polyphony"]           = 1
settings["violin"]["note_length_adjust"]  = 1.0
settings["violin"]["pizz-threshold"]      = -1
#settings["violin"]["midi_channel"]        = 1

settings["viola"]["octave"]                = -1
settings["viola"]["length_upperlimit"]   = 999
settings["viola"]["length_lowerlimit"]   = 0
settings["viola"]["velocity_multiplier"] = 1.0
settings["viola"]["volume"]              = .5
settings["viola"]["polyphony"]           = 1
settings["viola"]["note_length_adjust"]  = 1.0
settings["viola"]["pizz-threshold"]      = -1
#settings["viola"]["midi_channel"]       = 1

settings["cello"]["octave"]              = -1
settings["cello"]["length_upperlimit"]   = 999
settings["cello"]["length_lowerlimit"]   = 0
settings["cello"]["velocity_multiplier"] = 1.0
settings["cello"]["volume"]              = .8
settings["cello"]["polyphony"]           = 1
settings["cello"]["note_length_adjust"]  = 1.0
settings["cello"]["pizz-threshold"]      = -1
#settings["cello"]["midi_channel"]       = 1

settings["double-bass"]["octave"]              = 0
settings["double-bass"]["length_upperlimit"]   = 999
settings["double-bass"]["length_lowerlimit"]   = 0
settings["double-bass"]["velocity_multiplier"] = 1.0
settings["double-bass"]["volume"]              = .8
settings["double-bass"]["polyphony"]           = 1
settings["double-bass"]["note_length_adjust"]  = 1.0
settings["double-bass"]["pizz-threshold"]      = -1
#settings["double-bass"]["midi_channel"]        = 1




arranger.arrange(settings)
