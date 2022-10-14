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
settings["master_volume"]  = 0.5
settings["global_velocity"] = 0.8
settings["project_name"] = "Bartok-romanian-dance-2.Brâul"
settings["input_midi"]   = "MIDI/el-atril-midi/bartok-romanian-folk-dances/2.Brâul.mid"
settings["instruments"] = ["violin", "cello"]



settings["violin"]["midi_channel"] = 1
settings["cello"]["midi_channel"] = 2
arrange(settings)
