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

settings["project_name"] = "Hildegard-o-pastor"
settings["input_midi"]   = "MIDI/musescore.com/O_pastor-fruity.mid"

settings["banned_effects"]                      = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "tremolo", "phrase", "non-vibrato", "harmonic", "tratto", "very-long_mezzo-forte_arco-normal", "snap","trill", "glissando", "staccato", "sul", "au"]

# "violin", "viola", "cello", "double-bass", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "flute", "french-horn", "oboe", "saxophone", "trombone", "trumpet", "tuba", "guitar", "mandolin", "banjo"

settings["instruments"] = [ "violin", "flute", "guitar", "contrabassoon"] #, "viola", "guitar", "double-bass"]

settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = 0
settings["reverberance"]                        = 50
settings["reverb-room-scale"]                   = 100
settings["reverb-stereo-depth"]                 = 100
settings["master_tempo"]                        = 1.0
settings["master_volume"]                       = 0.8


settings["flute"]["octave"]                = 1
settings["flute"]["length_upperlimit"]   = 999
settings["flute"]["length_lowerlimit"]   = 0
settings["flute"]["velocity_multiplier"] = 1.0
settings["flute"]["volume"]              = .5
settings["flute"]["polyphony"]           = 1
settings["flute"]["note_length_adjust"]  = 1.0
settings["flute"]["pizz-threshold"]      = -1
settings["flute"]["midi_channel"]        = [3,4]
#settings["flute"]["low_pass"]            = 12 * 5

settings["violin"]["octave"]                = 0
settings["violin"]["length_upperlimit"]   = 999
settings["violin"]["length_lowerlimit"]   = 0
settings["violin"]["velocity_multiplier"] = .8
settings["violin"]["volume"]              = .5
settings["violin"]["polyphony"]           = 1
settings["violin"]["note_length_adjust"]  = 1.0
settings["violin"]["pizz-threshold"]      = -1
settings["violin"]["midi_channel"]       = 2


settings["cello"]["octave"]              = 0
settings["cello"]["length_upperlimit"]   = 999
settings["cello"]["length_lowerlimit"]   = 0
settings["cello"]["velocity_multiplier"] = 1.0
settings["cello"]["volume"]              = .5
settings["cello"]["polyphony"]           = 1
settings["cello"]["note_length_adjust"]  = 1.0
settings["cello"]["pizz-threshold"]      = -1
#settings["cello"]["midi_channel"]       = 1

settings["contrabassoon"]["octave"]              = -2
settings["contrabassoon"]["length_upperlimit"]   = 999
settings["contrabassoon"]["length_lowerlimit"]   = 0
settings["contrabassoon"]["velocity_multiplier"] = 1
settings["contrabassoon"]["volume"]              = .5
settings["contrabassoon"]["polyphony"]           = 1
settings["contrabassoon"]["note_length_adjust"]  = 1.0
settings["contrabassoon"]["pizz-threshold"]      = -1




arranger.arrange(settings)
