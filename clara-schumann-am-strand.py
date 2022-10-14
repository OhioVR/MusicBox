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

settings["project_name"] = "Clara-Schumann-am_strand"
settings["input_midi"]   = "MIDI/recmusic.org/Clara-Schumann/am_strand.mid"

settings["banned_effects"]                      = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "tremolo", "phrase", "non-vibrato", "harmonic", "tratto", "very-long_mezzo-forte_arco-normal", "snap","trill", "glissando", "staccato", "sul", "au", "sord"]

# "violin", "viola", "cello", "double-bass", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "flute", "french-horn", "oboe", "saxophone", "trombone", "trumpet", "tuba", "guitar", "mandolin", "banjo"

settings["instruments"] = ["guitar", "double-bass", "violin", "flute"]

settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = 0
settings["reverberance"]                        = 50
settings["reverb-room-scale"]                   = 100
settings["reverb-stereo-depth"]                 = 100
settings["master_tempo"]                        = 1.0
settings["master_volume"]                       = 0.8

settings["guitar"]["midi_channel"] = [4,5,6]
settings["double-bass"]["midi_channel"] = [4,5,6]
settings["violin"]["midi_channel"] = [4]
settings["flute"]["midi_channel"] = [4,5,6]

settings["double-bass"]["length_lowerlimit"]   = .28
settings["flute"]["length_lowerlimit"]   = .13
settings["double-bass"]["octave"] = -1
settings["double-bass"]["volume"] = .2


arranger.arrange(settings)
