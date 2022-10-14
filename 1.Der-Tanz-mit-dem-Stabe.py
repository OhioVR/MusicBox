#!/usr/bin/env pypy3

from util.arranger import arrange
from util.arranger import defaults
import os
import sys

# midi file by the Lectern [ www.el-atril.com ]
# samples provided by the London Philharmonia Orchestra

###############################
# Create settings dictionary. #
###############################
settings = defaults
settings["master_tempo"] = 1
settings["key_offset"] = -4
settings["maximize_dynamics"] = False
settings["global_velocity"] = .8
settings["master_volume"]  = 0.5
settings["project_name"] = "Bartok-romanian-dance-1.Der-Tanz-mit-dem-Stabe"
settings["input_midi"]   = "MIDI/el-atril-midi/bartok-romanian-folk-dances/1.Der-Tanz-mit-dem-Stabe-fruity.mid"
settings["instruments"] = ["violin", "double-bass"]
settings["banned_effects"]                      = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "tremolo", "phrase", "non-vibrato", "harmonic", "tratto", "very-long_mezzo-forte_arco-normal", "snap","trill", "glissando", "staccato", "sul", "au"]


settings["violin"]["midi_channel"] = 1+1
settings["violin"]["volume"]   = 1
settings["violin"]["velocity_multiplier"] = .4
settings["cello"]["velocity_multiplier"] = 1
settings["double-bass"]["velocity_multiplier"] = 1
settings["double-bass"]["volume"] = 1
settings["cello"]["volume"] = 1
settings["cello"]["midi_channel"] = 2+1
settings["double-bass"]["midi_channel"] = 2+1

settings["cello"]["octave"] = 0
settings["double-bass"]["octave"] = -1
settings["double-bass"]["pizz_threshold"] = 999
settings["cello"]
arrange(settings)
