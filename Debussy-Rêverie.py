#!/usr/bin/env pypy3
from util.arranger import arrange
from util.arranger import defaults
from util.Philhartronia.instrument_data_and_scales import notes
from util.Philhartronia.instrument_data_and_scales import ranges
import os
import sys

os.system("clear")


###############################
# Create settings dictionary. #
###############################
settings = defaults


settings["banned_effects"] = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "tremolo", "phrase", "non-vibrato", "harmonic", "tratto", "very-long_mezzo-forte_arco-normal", "snap","trill", "glissando", "staccato", "sul", "au", "sord"]
settings["project_name"] = "Claude-Debussy-Rêverie"
settings["input_midi"]   = "MIDI/el-atril-midi/Debussy/Rêverie-fruity.mid"
settings["key_offset"]                          = 0
settings["instruments"] = ["double-bass", "contrabassoon","violin","guitar","flute", "bass-clarinet"]
settings["master_volume"]                       = 1.0
settings["master_tempo"] = 1
settings["strings_overlay_time"]                = 0.07

settings["double-bass"]["octave"] = 0
settings["flute"]["octave"] = 0
settings["contrabassoon"]["octave"] = -1
settings["bass-clarinet"]["octave"] = 0
settings["viola"]["high_pass"] = notes.index("Gs3")
settings["guitar"]["midi_channel"] = [2,3,4]
settings["violin"]["midi_channel"] = [2]
settings["double-bass"]["midi_channel"] = [4]
settings["flute"]["midi_channel"] = [4]
settings["contrabassoon"]["midi_channel"] = [4]
settings["bass-clarinet"]["midi_channel"] = [4]
settings["contrabassoon"]["high_pass"] = notes.index(ranges["bassoon"]["min"])
settings["violin"]["volume"] = 1
settings["violin"]["velocity_multiplier"] = .9
settings["viola"]["velocity_multiplier"] = .9
settings["double-bass"]["volume"] = .6
settings["double-bass"]["velocity_multiplier"] = .9
settings["contrabassoon"]["velocity_multiplier"] = .7
settings["contrabassoon"]["volume"] = .5
settings["bass-clarinet"]["velocity_multiplier"] = .7
settings["bass-clarinet"]["volume"] = .5

arrange(settings)
