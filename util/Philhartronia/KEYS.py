#!/usr/bin/env python3

# Scott's MusicBox
# KEYS.py by Scott Yannitell
# Copyright 2022 Scott Yannitell all rights reserved

# No this has nothing to do with music notation or scales. This is for easy
# readablity in other parts of Scott's Music Box's source code.

# These names make it easy to read indexes in get_sample and the 
# database scripts. The indexes are named for what they represent.
# Sure a "real" full statck developer would poo poo this method because I don't
# use SQL. But in the end it only takes a moment or two for the implimentation
# to arrange a track on a dataset measured in hundreds of megabytes.

# So I'm happy, you're happy, we're all happy right?

# Besides this is so easy a caveman could do it. No offence to great great great
# grandads.

NOTE_INDEX          = 0 # redundancy
NOTE_NAME           = 1 # redundancy
INSTRUMENT          = 2 # redundancy
NOTE_LENGTH         = 3 # measured in seconds
FILE_LOUDNESS       = 4 # used by cross_fade_arco.py
FILE_TRUE_DURATION  = 5 # measured in seconds: just the file length
SAMPLE_OFFSET       = 6 # measured in seconds: when the sound actually begins
MIDDLE_MIN_OFFSET   = 7 # used by cross_fade_arco.py
MIDDLE_MAX_OFFSET   = 8 # used by cross_fade_arco.py
PLUCKED             = 9
RANGER_MAX_LOUDNESS = 10 # unused
RANGER_MIN_LOUDNESS = 11 # unused
MIDI_LOUDNESS       = 12 # unused
SAMPLE              = 13 # filename of sample
LOUDNESS_ID         = 14 # a numerical value representing the static values of music loudness notation
LOUDNESS_NAME       = 15 # the literal name of the intensity: mostly unused
NOTE_RELATIVE_LOUD  = 16 # unused
LONGEST             = 17 # unused
SHORTEST            = 18 # unused

# notice all the values that go unused. I'm too lazy to remove them because
# what if I change my mind later? Probably won't though. But my excuse stands.
