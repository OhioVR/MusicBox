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
settings["master_volume"] = .65
settings["key_offset"] = 0
settings["project_name"] = "Bartok-romanian-dance-4.Tanz-aus-Butschum"
settings["input_midi"]   = "MIDI/el-atril-midi/bartok-romanian-folk-dances/4.Tanz-aus-Butschum-fruity.mid"
settings["banned_effects"]                      = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "tremolo", "phrase", "non-vibrato", "harmonic", "tratto", "very-long_mezzo-forte_arco-normal", "snap","trill", "glissando", "staccato", "sul", "au"]
settings["instruments"] = ["violin", "double-bass", "cello"]
settings["violin"]["octave"] = 0
settings["violin"]["midi_channel"] = 1 + 1
settings["violin"]["velocity_multiplier"] = .92
settings["cello"]["midi_channel"] = 2 + 1
settings["viola"]["midi_channel"] = 2 + 1
settings["viola"]["pizz-threshold"] = 0
settings["double-bass"]["midi_channel"] = 2 + 1
settings["double-bass"]["pizz-threshold"] = 0


settings["double-bass"]["volume"] = .5
settings["cello"]["volume"] = .5
settings["viola"]["volume"] = .5

settings["double-bass"]["octave"] = 0
settings["cello"]["octave"] = 0
settings["viola"]["octave"] = 0

settings["viola"]["length_lowerlimit"] = .5
settings["cello"]["length_lowerlimit"] = .7
settings["double-bass"]["length_lowerlimit"] = .5


arrange(settings)
