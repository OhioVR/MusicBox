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
settings = settings = defaults
settings["key_offset"] = 0
settings["master_volume"]  = 0.4
settings["project_name"] = "Bartok-romanian-dance-3.DerStampfer"
settings["input_midi"]   = "MIDI/el-atril-midi/bartok-romanian-folk-dances/3.DerStampfer.mid"
settings["instruments"] = ["violin", "cello"]

settings["violin"]["midi_channel"] = 1
settings["violin"]["velocity_multiplier"] = 1
settings["cello"]["velocity_multiplier"] = 1
settings["cello"]["midi_channel"] = 2
arrange(settings)
