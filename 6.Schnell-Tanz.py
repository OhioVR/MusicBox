#!/usr/bin/env pypy3

from util.arranger import arrange
from util.arranger import defaults
import os
import sys

os.system("clear")

# midi file by the Lectern [ www.el-atril.com ]
# samples provided by the London Philharmonia Orchestra

###############################
# Create settings dictionary. #
###############################
settings = defaults
settings["master_tempo"] = 1
settings["key_offset"] = 0
settings["maximize_dynamics"] = False

settings["project_name"] = "Bartok-romanian-dance-6.Schnell-Tanz"
settings["input_midi"]   = "MIDI/el-atril-midi/bartok-romanian-folk-dances/6.Schnell-Tanz-fruity.mid"
settings["instruments"] = ["violin", "cello", "double-bass"]

settings["violin"]["midi_channel"] = 1+1
settings["violin"]["velocity_multiplier"] = .9
settings["cello"]["midi_channel"] = 2+1
settings["viola"]["midi_channel"] = 2+1
settings["double-bass"]["midi_channel"] = 2+1
settings["double-bass"]["pizz_threshold"] = 0
settings["viola"]["octave"] = 0
settings["cello"]["octave"] = 0
settings["double-bass"]["octave"] = 0
settings["viola"]["volume"] = .5
settings["cello"]["volume"] = .5
settings["double-bass"]["volume"] = .5
arrange(settings)
