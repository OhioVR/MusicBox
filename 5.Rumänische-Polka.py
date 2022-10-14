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
settings["project_name"] = "Bartok-5-Romanian-Polka"
settings["input_midi"]   = "MIDI/el-atril-midi/bartok-romanian-folk-dances/5.Rumänische-Polka.mid"
settings["instruments"] = ["violin", "viola", "cello", "double-bass"]
settings["banned_effects"]                      = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "tremolo", "phrase", "non-vibrato", "harmonic", "tratto", "snap","trill", "glissando", "staccato", "sul", "au"]



settings["violin"]["volume"]   = 1
settings["violin"]["velocity_multiplier"] = .4
settings["cello"]["velocity_multiplier"] = 1
settings["double-bass"]["velocity_multiplier"] = 1
settings["double-bass"]["volume"] = 1
settings["cello"]["volume"] = 1
settings["cello"]["octave"] = -1
settings["double-bass"]["octave"] = -1
arrange(settings)
