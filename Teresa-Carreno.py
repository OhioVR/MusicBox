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

settings["project_name"] = "Teresa-Carreño"
settings["input_midi"]   = "MIDI/musescore.com/Gottschalk_Waltz_1863.mid"

settings["banned_effects"]                      = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "tremolo", "phrase", "non-vibrato", "harmonic", "tratto", "very-long_mezzo-forte_arco-normal", "snap","trill", "glissando", "staccato", "sul", "au"]

# "violin", "viola", "cello", "double-bass", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "flute", "french-horn", "oboe", "saxophone", "trombone", "trumpet", "tuba", "guitar", "mandolin", "banjo"

settings["instruments"] = ["contrabassoon", "guitar", "tuba", "flute"]

settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = -12
settings["reverberance"]                        = 50
settings["reverb-room-scale"]                   = 100
settings["reverb-stereo-depth"]                 = 100
settings["master_tempo"]                        = 1.0
settings["master_volume"]                       = 0.8


settings["flute"]["octave"]                = -1
settings["flute"]["length_upperlimit"]   = 999
settings["flute"]["length_lowerlimit"]   = .25
settings["flute"]["velocity_multiplier"] = 1.0
settings["flute"]["volume"]              = .5
settings["flute"]["polyphony"]           = 1
settings["flute"]["note_length_adjust"]  = 1.0
settings["flute"]["pizz-threshold"]      = -1
#settings["violin"]["midi_channel"]        = 1

settings["guitar"]["octave"] = -1

settings["viola"]["octave"]                = 0
settings["viola"]["length_upperlimit"]   = 999
settings["viola"]["length_lowerlimit"]   = 0
settings["viola"]["velocity_multiplier"] = 1.0
settings["viola"]["volume"]              = .5
settings["viola"]["polyphony"]           = 1
settings["viola"]["note_length_adjust"]  = 1.0
settings["viola"]["pizz-threshold"]      = .2
#settings["viola"]["midi_channel"]       = 1

settings["cello"]["octave"]              = -1
settings["cello"]["length_upperlimit"]   = .5
settings["cello"]["length_lowerlimit"]   = 0
settings["cello"]["velocity_multiplier"] = 1.0
settings["cello"]["volume"]              = .5
settings["cello"]["polyphony"]           = 1
settings["cello"]["note_length_adjust"]  = 1.0
settings["cello"]["pizz-threshold"]      = -1
#settings["cello"]["midi_channel"]       = 1

settings["tuba"]["octave"]              = 0
settings["tuba"]["length_upperlimit"]   = 999
settings["tuba"]["length_lowerlimit"]   = .5
settings["tuba"]["velocity_multiplier"] = 1.0
settings["tuba"]["volume"]              = .25
settings["tuba"]["polyphony"]           = 1

settings["contrabassoon"]["octave"]              = -1
settings["contrabassoon"]["length_upperlimit"]   = 999
settings["contrabassoon"]["length_lowerlimit"]   = 0
settings["contrabassoon"]["velocity_multiplier"] = 1.0
settings["contrabassoon"]["volume"]              = .1
settings["contrabassoon"]["polyphony"]           = 1




arranger.arrange(settings)
