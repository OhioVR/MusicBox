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

settings["project_name"] = "Hensel_Fanny_Mendelssohn_-_6_Lieder_Op.1_No.6_-_Gondellied"
settings["input_midi"]   = "MIDI/musescore.com/Hensel_Fanny_Mendelssohn_-_6_Lieder_Op.1_No.6_-_Gondellied.mid"

settings["banned_effects"]                      = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "tremolo", "phrase", "non-vibrato", "harmonic", "tratto", "very-long_mezzo-forte_arco-normal", "snap","trill", "glissando", "staccato", "sul", "au"]

# "violin", "viola", "cello", "double-bass", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "flute", "french-horn", "oboe", "saxophone", "trombone", "trumpet", "tuba", "guitar", "mandolin", "banjo"

settings["instruments"] = ["mandolin", "banjo", "guitar", "double-bass"]

settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = -2
settings["reverberance"]                        = 50
settings["reverb-room-scale"]                   = 100
settings["reverb-stereo-depth"]                 = 100
settings["master_tempo"]                        = .8
settings["master_volume"]                       = 0.8

settings["guitar"]["octave"] = -1

settings["violin"]["octave"]                = 0
settings["violin"]["length_upperlimit"]   = 999
settings["violin"]["length_lowerlimit"]   = 0
settings["violin"]["velocity_multiplier"] = 1.0
settings["violin"]["volume"]              = .5
settings["violin"]["polyphony"]           = 1
settings["violin"]["note_length_adjust"]  = 1.0
settings["violin"]["pizz-threshold"]      = -1
#settings["violin"]["midi_channel"]        = 1

settings["viola"]["octave"]                = 0
settings["viola"]["length_upperlimit"]   = 999
settings["viola"]["length_lowerlimit"]   = 0
settings["viola"]["velocity_multiplier"] = 1.0
settings["viola"]["volume"]              = .5
settings["viola"]["polyphony"]           = 1
settings["viola"]["note_length_adjust"]  = 1.0
settings["viola"]["pizz-threshold"]      = -1
#settings["viola"]["midi_channel"]       = 1

settings["cello"]["octave"]              = 0
settings["cello"]["length_upperlimit"]   = 999
settings["cello"]["length_lowerlimit"]   = 0
settings["cello"]["velocity_multiplier"] = 1.0
settings["cello"]["volume"]              = .5
settings["cello"]["polyphony"]           = 1
settings["cello"]["note_length_adjust"]  = 1.0
settings["cello"]["pizz-threshold"]      = -1
#settings["cello"]["midi_channel"]       = 1

settings["mandolin"]["octave"]              = -1
settings["mandolin"]["length_upperlimit"]   = 999
settings["mandolin"]["length_lowerlimit"]   = .5
settings["mandolin"]["velocity_multiplier"] = 1.0
settings["mandolin"]["volume"]              = .5
settings["mandolin"]["polyphony"]           = 1
settings["mandolin"]["note_length_adjust"]  = 1.0
settings["mandolin"]["pizz-threshold"]      = 0
#settings["cello"]["midi_channel"]       = 1

settings["banjo"]["octave"]              = -1
settings["banjo"]["length_upperlimit"]   = 999
settings["banjo"]["length_lowerlimit"]   = .75
settings["banjo"]["velocity_multiplier"] = 1.0
settings["banjo"]["volume"]              = .5
settings["banjo"]["polyphony"]           = 1
settings["banjo"]["note_length_adjust"]  = 1.0
settings["banjo"]["pizz-threshold"]      = 0
#settings["cello"]["midi_channel"]       = 1

settings["double-bass"]["octave"]              = -1
settings["double-bass"]["length_upperlimit"]   = 999
settings["double-bass"]["length_lowerlimit"]   = 0
settings["double-bass"]["velocity_multiplier"] = 1.0
settings["double-bass"]["volume"]              = .5
settings["double-bass"]["polyphony"]           = 1
settings["double-bass"]["note_length_adjust"]  = 1.0
settings["double-bass"]["pizz-threshold"]      = -1
#settings["double-bass"]["midi_channel"]        = 1




arranger.arrange(settings)
