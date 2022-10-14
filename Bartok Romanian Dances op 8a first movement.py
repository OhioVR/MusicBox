#!/usr/bin/env pypy3
from util.arranger import arrange
import os

os.system("clear")


###############################
# Create settings dictionary. #
###############################
settings = {}

# saxophone sounds terrible :(
# trumpet sounds terrible
# trombone is ok
# tuba sounds bad
settings["instruments"] = ["violin", "viola", "cello", "double-bass", "flute", "guitar", "mandolin", "oboe", "bassoon", "trombone", "contrabassoon"]
settings["banned_effects"] = ["trill"]
settings["effect_exceptions"] = []

settings["round_robin"]                         = 0
settings["project_name"]                        = "Bela-Bartok-Romanian-Dances-op-8-Custom-Arrangement"
settings["input_midi"]                          = "MIDI/example_midi_files/Bartok-Romanian-Dances-op-8a-first-movement.mid"
settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = 0
settings["reverberance"]                        = 50
settings["reverb_room_scale"]                   = 100
settings["reverb_stereo_depth"]                 = 100
settings["master_tempo"]                        = .8
settings["master_volume"]                       = 0.55
settings["strings_overlay_time"]                = 0.07

settings["flute"]                              = {}
settings["flute"]["octave"]                    = -1
settings["flute"]["length_upperlimit"]         = 999
settings["flute"]["length_lowerlimit"]         = 0
settings["flute"]["velocity_multiplier"]       = 1
settings["flute"]["volume"]                    = 2
settings["flute"]["polyphony"]                 = 1
settings["flute"]["note_length_adjust"]        = 1.0


settings["mandolin"]                              = {}
settings["mandolin"]["octave"]                    = 0
settings["mandolin"]["length_upperlimit"]         = 999
settings["mandolin"]["length_lowerlimit"]         = 1.4
settings["mandolin"]["velocity_multiplier"]       = 1
settings["mandolin"]["volume"]                    = 1
settings["mandolin"]["polyphony"]                 = 1
settings["mandolin"]["note_length_adjust"]        = .7
settings["mandolin"]["pizz_threshold"]            = 1.4


settings["violin"]                              = {}
settings["violin"]["octave"]                    = -1
settings["violin"]["length_upperlimit"]         = 5
settings["violin"]["length_lowerlimit"]         = .18
settings["violin"]["velocity_multiplier"]       = 1.0
settings["violin"]["volume"]                    = 1
settings["violin"]["polyphony"]                 = 1
settings["violin"]["note_length_adjust"]        = 1.0
settings["violin"]["pizz_threshold"]            = 0

settings["viola"]                               = {}
settings["viola"]["octave"]                     = 0
settings["viola"]["length_upperlimit"]          = 999
settings["viola"]["length_lowerlimit"]          = 0.18
settings["viola"]["velocity_multiplier"]        = 1
settings["viola"]["volume"]                     = 0.7
settings["viola"]["polyphony"]                  = 1
settings["viola"]["note_length_adjust"]         = 1.0
settings["viola"]["pizz_threshold"]            = -1

settings["cello"]                               = {}
settings["cello"]["octave"]                     = 0
settings["cello"]["length_upperlimit"]          = 999
settings["cello"]["length_lowerlimit"]          = 0.18
settings["cello"]["velocity_multiplier"]        = 0.7
settings["cello"]["volume"]                     = 0.3
settings["cello"]["polyphony"]                  = 1
settings["cello"]["note_length_adjust"]         = .7
settings["cello"]["pizz_threshold"]             = -1

settings["double-bass"]                         = {}
settings["double-bass"]["octave"]               = -1
settings["double-bass"]["length_upperlimit"]    = 4
settings["double-bass"]["length_lowerlimit"]    = 0.18
settings["double-bass"]["velocity_multiplier"]  = 1.0
settings["double-bass"]["volume"]               = 1.0
settings["double-bass"]["polyphony"]            = 1
settings["double-bass"]["note_length_adjust"]   = 1.0
settings["double-bass"]["pizz_threshold"]       = -1

settings["guitar"]                                = {}
settings["guitar"]["octave"]                      = 0
settings["guitar"]["length_upperlimit"]           = 999
settings["guitar"]["length_lowerlimit"]           = 0
settings["guitar"]["velocity_multiplier"]         = 1.0
settings["guitar"]["volume"]                      = 0.8
settings["guitar"]["polyphony"]                   = 1
settings["guitar"]["note_length_adjust"]          = 1.0

settings["bass-clarinet"]                                = {}
settings["bass-clarinet"]["octave"]                      = 0
settings["bass-clarinet"]["length_upperlimit"]           = 999
settings["bass-clarinet"]["length_lowerlimit"]           = 0.09
settings["bass-clarinet"]["velocity_multiplier"]         = 1.0
settings["bass-clarinet"]["volume"]                      = 0.4
settings["bass-clarinet"]["polyphony"]                   = 1
settings["bass-clarinet"]["note_length_adjust"]          = 1.0

settings["bassoon"]                                = {}
settings["bassoon"]["octave"]                      = 0
settings["bassoon"]["length_upperlimit"]           = 3
settings["bassoon"]["length_lowerlimit"]           = 0.18
settings["bassoon"]["velocity_multiplier"]         = 1.0
settings["bassoon"]["volume"]                      = 0.4
settings["bassoon"]["polyphony"]                   = 1
settings["bassoon"]["note_length_adjust"]          = 1.0

settings["contrabassoon"]                                = {}
settings["contrabassoon"]["octave"]                      = -2
settings["contrabassoon"]["length_upperlimit"]           = 4
settings["contrabassoon"]["length_lowerlimit"]           = 0.18
settings["contrabassoon"]["velocity_multiplier"]         = 1.0
settings["contrabassoon"]["volume"]                      = 0.4
settings["contrabassoon"]["polyphony"]                   = 1
settings["contrabassoon"]["note_length_adjust"]          = 1.0

settings["french-horn"]                                = {}
settings["french-horn"]["octave"]                      = 0
settings["french-horn"]["length_upperlimit"]           = 3
settings["french-horn"]["length_lowerlimit"]           = 0.18*2
settings["french-horn"]["velocity_multiplier"]         = 1.0
settings["french-horn"]["volume"]                      = 0.5
settings["french-horn"]["polyphony"]                   = 1
settings["french-horn"]["note_length_adjust"]          = 1.0


settings["trombone"]                                = {}
settings["trombone"]["octave"]                      = 0
settings["trombone"]["length_upperlimit"]           = 3
settings["trombone"]["length_lowerlimit"]           = 0.18
settings["trombone"]["velocity_multiplier"]         = 1.0
settings["trombone"]["volume"]                      = 0.5
settings["trombone"]["polyphony"]                   = 1
settings["trombone"]["note_length_adjust"]          = 1.0

settings["trumpet"]                                = {}
settings["trumpet"]["octave"]                      = 0
settings["trumpet"]["length_upperlimit"]           = 5
settings["trumpet"]["length_lowerlimit"]           = 0.18
settings["trumpet"]["velocity_multiplier"]         = 1.0
settings["trumpet"]["volume"]                      = 0.4
settings["trumpet"]["polyphony"]                   = 1
settings["trumpet"]["note_length_adjust"]          = 1.0

settings["tuba"]                                = {}
settings["tuba"]["octave"]                      = -1
settings["tuba"]["length_upperlimit"]           = 5
settings["tuba"]["length_lowerlimit"]           = 0.25
settings["tuba"]["velocity_multiplier"]         = 1.0
settings["tuba"]["volume"]                      = 0.4
settings["tuba"]["polyphony"]                   = 1
settings["tuba"]["note_length_adjust"]          = 1.0

settings["clarinet"]                            = {}
settings["clarinet"]["octave"]                  = 0
settings["clarinet"]["length_upperlimit"]       = 4
settings["clarinet"]["length_lowerlimit"]       = 0.18
settings["clarinet"]["velocity_multiplier"]     = 1.0
settings["clarinet"]["volume"]                  = 0.5
settings["clarinet"]["polyphony"]               = 1
settings["clarinet"]["note_length_adjust"]      = 1.0


settings["english-horn"]                        = {}
settings["english-horn"]["octave"]              = 0
settings["english-horn"]["length_upperlimit"]   = 3
settings["english-horn"]["length_lowerlimit"]   = 0.18
settings["english-horn"]["velocity_multiplier"] = 1
settings["english-horn"]["volume"]              = 0.7
settings["english-horn"]["polyphony"]           = 1
settings["english-horn"]["note_length_adjust"]  = 1.0

settings["oboe"]                        = {}
settings["oboe"]["octave"]              = 0
settings["oboe"]["length_upperlimit"]   = 9
settings["oboe"]["length_lowerlimit"]   = 0
settings["oboe"]["velocity_multiplier"] = 1
settings["oboe"]["volume"]              = 0.7
settings["oboe"]["polyphony"]           = 1
settings["oboe"]["note_length_adjust"]  = 1.0



#######################
# Execute the project #
#######################

arrange(settings)
