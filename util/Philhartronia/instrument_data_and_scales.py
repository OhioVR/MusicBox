#!/usr/bin/env python3

# Scott's MusicBox
# instrument_data_and_scales.py by Scott Yannitell
# Copyright 2022 all rights reserved

# I had some of this data scattered everywhere at some point that lead
# to inconsistancies and errors so it is all held here now. 

instruments = [ "guitar", "mandolin", "banjo", "violin", "viola", "cello", "double-bass", "flute", "oboe", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "french-horn", "saxophone", "trombone", "trumpet", "tuba"]

# shell silencer
nuller=" >/dev/null 2>&1"

# orchestra registers
ranges = {}
ranges["philhatronia"] = {}
ranges["philhatronia"]["min"] = "As0"
ranges["philhatronia"]["max"] = "C8"
ranges["philhatronia"]["1st_C"] = "C1"

# Strings Family
# string Mom
ranges["cello"] = {}
ranges["cello"]["min"] = "C2"
ranges["cello"]["max"] = "Cs6"
ranges["cello"]["1st_C"] = "C2"

# string Dad
ranges["double-bass"] = {}
ranges["double-bass"]["min"] = "C1"
ranges["double-bass"]["max"] = "G4"
ranges["double-bass"]["1st_C"] = "C1"

# Litte Sis (Dad's favorite)
ranges["violin"] = {}
ranges["violin"]["min"] = "G3"
ranges["violin"]["max"] = "C8"
ranges["violin"]["1st_C"] = "C4"

# string Big Sis (Mom's Favorite)
ranges["viola"] = {}
ranges["viola"]["min"] = "C3"
ranges["viola"]["max"] = "Fs7"
ranges["viola"]["1st_C"] = "C3"

ranges["strings_family"] = {}
ranges["strings_family"]["min"] = "G3"
ranges["strings_family"]["max"] = "G4"
ranges["strings_family"]["1st_C"] = "C4"

# Plucked Family
# string mom
ranges["mandolin"] = {}
ranges["mandolin"]["min"] = "G3"
ranges["mandolin"]["max"] = "Gs6"
ranges["mandolin"]["1st_C"] = "C4"

# guitar as it is supposed to be
#ranges["guitar"] = {}
#ranges["guitar"]["min"] = "A2"
#ranges["guitar"]["max"] = "C6"
#ranges["guitar"]["1st_C"] = "C3"

# but since I think it sounds more like a harp I'll use it that way
ranges["guitar"] = {}
ranges["guitar"]["min"] = "C1"
ranges["guitar"]["max"] = "F7"
ranges["guitar"]["1st_C"] = "C1"

# string son
ranges["banjo"] = {}
ranges["banjo"]["min"] = "C3"
ranges["banjo"]["max"] = "E6"
ranges["banjo"]["1st_C"] = "C3"

# air Great Uncle
ranges["tuba"] = {}
ranges["tuba"]["min"] = "As0"
ranges["tuba"]["max"] = "F4"
ranges["tuba"]["1st_C"] = "C1"

# air brother
ranges["trumpet"] = {}
ranges["trumpet"]["min"] = "A2"
ranges["trumpet"]["max"] = "E6"
ranges["trumpet"]["1st_C"] = "C3"

# air brother
ranges["trombone"] = {}
ranges["trombone"]["min"] = "B2"
ranges["trombone"]["max"] = "Gs5"
ranges["trombone"]["1st_C"] = "C3"

# air brother
ranges["french-horn"] = {}
ranges["french-horn"]["min"] = "C2"
ranges["french-horn"]["max"] = "F5"
ranges["french-horn"]["1st_C"] = "C2"

# air cousin
ranges["saxophone"] = {}
ranges["saxophone"]["min"] = "B3"
ranges["saxophone"]["max"] = "G6"
ranges["saxophone"]["1st_C"] = "C4"

# air Grandpa
ranges["contrabassoon"] = {}
ranges["contrabassoon"]["min"] = "As0"
ranges["contrabassoon"]["max"] = "Cs4"
ranges["contrabassoon"]["1st_C"] = "C1"

# air Aunt
ranges["oboe"] = {}
ranges["oboe"]["min"] = "C4"
ranges["oboe"]["max"] = "Gs6"
ranges["oboe"]["1st_C"] = "C4"

# air cousin
ranges["flute"] = {}
ranges["flute"]["min"] = "C4"
ranges["flute"]["max"] = "F7"
ranges["flute"]["1st_C"] = "C4"


ranges["english-horn"] = {}
ranges["english-horn"]["min"] = "F3"
ranges["english-horn"]["max"] = "Gs5"
ranges["english-horn"]["1st_C"] = "C4"

ranges["clarinet"] = {}
ranges["clarinet"]["min"] = "Ds3"
ranges["clarinet"]["max"] = "C7"
ranges["clarinet"]["1st_C"] = "C4"

ranges["bassoon"] = {}
ranges["bassoon"]["min"] = "C2"
ranges["bassoon"]["max"] = "F5"
ranges["bassoon"]["1st_C"] = "C2"

ranges["bass-clarinet"] = {}
ranges["bass-clarinet"]["min"] = "C2"
ranges["bass-clarinet"]["max"] = "C6"
ranges["bass-clarinet"]["1st_C"] = "C2"



wav_setting = " -r 44100 -e signed -b 16 "
compression_setting = " -C 256 "

# scales
chromatic_scale=["C", "Cs", "D", "Ds", "E", "F", "Fs", "G", "Gs", "A", "As", "B"]
notes = []
for i in range(0,12):
    for ii in range(0,len(chromatic_scale)):
        note = chromatic_scale[ii]+str(i)
        notes.append(note)

# common scale primitives
# (more to come)
# these are intervals

chromatic_progression = []
for i in range(0,12*12):
    chromatic_progression.append(i)

major_scale = []
for i in range(0,12*12):
    major_scale.append(0+(i*12))                           # Example C
    major_scale.append(major_scale[-1]+2+(i*12))           # Example D
    major_scale.append(major_scale[-1]+2+(i*12))           # Example E
    major_scale.append(major_scale[-1]+1+(i*12))           # Example F
    major_scale.append(major_scale[-1]+2+(i*12))           # Example G
    major_scale.append(major_scale[-1]+2+(i*12))           # Example A
    major_scale.append(major_scale[-1]+2+(i*12))           # Example B

dbl_major_scale = []
for i in range(0,12*12):
    dbl_major_scale.append(0+(i*12*2))                             # Example C
    dbl_major_scale.append(dbl_major_scale[-1]+4+(i*12))           # Example E
    dbl_major_scale.append(dbl_major_scale[-1]+4+(i*12))           # Example Gs
    dbl_major_scale.append(dbl_major_scale[-1]+2+(i*12))           # Example As
    dbl_major_scale.append(dbl_major_scale[-1]+4+(i*12))           # Example D
    dbl_major_scale.append(dbl_major_scale[-1]+4+(i*12))           # Example Fs
    dbl_major_scale.append(dbl_major_scale[-1]+4+(i*12))           # Example As

minor_scale = []
for i in range(0,12*12):
    minor_scale.append(0+(i*12))                           # Example C
    minor_scale.append(minor_scale[-1]+2+(i*12))           # Example D
    minor_scale.append(minor_scale[-1]+1+(i*12))           # Example Ds
    minor_scale.append(minor_scale[-1]+2+(i*12))           # Example F
    minor_scale.append(minor_scale[-1]+2+(i*12))           # Example G
    minor_scale.append(minor_scale[-1]+1+(i*12))           # Example Gs
    minor_scale.append(minor_scale[-1]+2+(i*12))           # Example As

dbl_minor_scale = []
for i in range(0,12*12):
    dbl_minor_scale.append(0+(i*12*2))                     # Example C
    dbl_minor_scale.append(dbl_minor_scale[-1]+4+(i*12))           # Example E
    dbl_minor_scale.append(dbl_minor_scale[-1]+2+(i*12))           # Example Fs
    dbl_minor_scale.append(dbl_minor_scale[-1]+4+(i*12))           # Example As
    dbl_minor_scale.append(dbl_minor_scale[-1]+4+(i*12))           # Example D
    dbl_minor_scale.append(dbl_minor_scale[-1]+2+(i*12))           # Example Gs


pentatonic_scale = []
for i in range(0,12*12):
    pentatonic_scale.append(0+(i*12))               # Example C     
    pentatonic_scale.append(pentatonic_scale[-1]+2) # Example D
    pentatonic_scale.append(pentatonic_scale[-1]+3) # Example E
    pentatonic_scale.append(pentatonic_scale[-1]+2) # Example Fs
    pentatonic_scale.append(pentatonic_scale[-1]+2) # Example Gs

whole_tone_scale = []
for i in range(0,12*12*7):
    whole_tone_scale.append(0+(i*12))               # Example C     
    whole_tone_scale.append(whole_tone_scale[-1]+2) # Example D
    whole_tone_scale.append(whole_tone_scale[-1]+2) # Example E
    whole_tone_scale.append(whole_tone_scale[-1]+2) # Example Fs
    whole_tone_scale.append(whole_tone_scale[-1]+2) # Example Gs
    whole_tone_scale.append(whole_tone_scale[-1]+2) # Example As

double_tone_scale = []
for i in range(0,12*12*7):
    double_tone_scale.append(0+(i*12))               # Example C     
    double_tone_scale.append(double_tone_scale[-1]+4) # Example E
    double_tone_scale.append(double_tone_scale[-1]+4) # Example Gs


major_1 = []
for i in range(0,12*12):
    major_1.append(0+(i*12))
    major_1.append(major_1[-1]+4)
    major_1.append(major_1[-1]+3)

major_1_7 = []
for i in range(0,12*12):
    major_1_7.append(0+(i*12))
    major_1_7.append(major_1_7[-1]+4)
    major_1_7.append(major_1_7[-1]+3)
    major_1_7.append(major_1_7[-1]+4)

major_2 = []
for i in range(0,12*12):
    major_2.append(5+(i*12))
    major_2.append(major_2[-1]+4)
    major_2.append(major_2[-1]+3)

major_2_7 = []
for i in range(0,12*12):
    major_2_7.append(5+(i*12))
    major_2_7.append(major_2_7[-1]+4)
    major_2_7.append(major_2_7[-1]+3)
    major_2_7.append(major_2_7[-1]+4)


major_3 = []
for i in range(0,12*12):
    major_3.append(7+(i*12))
    major_3.append(major_3[-1]+4)
    major_3.append(major_3[-1]+3)

major_3_7 = []
for i in range(0,12*12):
    major_3_7.append(7+(i*12))
    major_3_7.append(major_3_7[-1]+4)
    major_3_7.append(major_3_7[-1]+3)
    major_3_7.append(major_3_7[-1]+4)



minor_1 = []
for i in range(0,12*12):
   minor_1.append(2+(i*12))
   minor_1.append(minor_1[-1]+3)
   minor_1.append(minor_1[-1]+4)

minor_1_7 = []
for i in range(0,12*12):
   minor_1_7.append(2+(i*12))
   minor_1_7.append(minor_1_7[-1]+3)
   minor_1_7.append(minor_1_7[-1]+4)
   minor_1_7.append(minor_1_7[-1]+3)


minor_2 = []
for i in range(0,12*12):
   minor_2.append(4+(i*12))
   minor_2.append(minor_2[-1]+3)
   minor_2.append(minor_2[-1]+4)

minor_2_7 = []
for i in range(0,12*12):
   minor_2_7.append(4+(i*12))
   minor_2_7.append(minor_2_7[-1]+3)
   minor_2_7.append(minor_2_7[-1]+4)
   minor_2_7.append(minor_2_7[-1]+3)

minor_3 = []
for i in range(0,12*12):
   minor_3.append(9+(i*12))
   minor_3.append(minor_3[-1]+3)
   minor_3.append(minor_3[-1]+4)

minor_3_7 = []
for i in range(0,12*12):
   minor_3_7.append(9+(i*12))
   minor_3_7.append(minor_3_7[-1]+3)
   minor_3_7.append(minor_3_7[-1]+4)
   minor_3_7.append(minor_3_7[-1]+3)

diminished= []
for i in range(0,12*12):
   diminished.append(-1+(i*12))
   diminished.append(diminished[-1]+3)
   diminished.append(diminished[-1]+3)

minor_7_flat_5= []
for i in range(0,12*12):
   minor_7_flat_5.append(-1+(i*12))
   minor_7_flat_5.append(minor_7_flat_5[-1]+3)
   minor_7_flat_5.append(minor_7_flat_5[-1]+3)
   minor_7_flat_5.append(minor_7_flat_5[-1]+4)







# https://www.youtube.com/watch?v=nK2jYk37Rlg
# [equal temperment]
inter_semitone_ratio = (2.0**(1.0/12.0))

# Rhythm
the_16nds_relationship = (2.0**(1.0/16.0))
the_8ths_relationship = (2.0**(1.0/8.0))
the_4ths_relationship = (2.0**(1.0/4.0))

