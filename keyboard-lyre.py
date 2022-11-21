#!/usr/bin/env python3

# Scott's Music Box
# keyboard-lyre.py by Scott Yannitell
# Copyright 2022 all rights reserved

from util.Philhartronia import get_sample
from util.arranger import defaults
from util.Philhartronia.instrument_data_and_scales import nuller
from util.Philhartronia.instrument_data_and_scales import major_scale
from util.Philhartronia.instrument_data_and_scales import minor_scale
from util.Philhartronia.instrument_data_and_scales import pentatonic_scale
from util.Philhartronia.instrument_data_and_scales import whole_tone_scale
from util.Philhartronia.instrument_data_and_scales import double_tone_scale
from util.Philhartronia.instrument_data_and_scales import dbl_major_scale
from util.Philhartronia.instrument_data_and_scales import dbl_minor_scale
from util.Philhartronia.instrument_data_and_scales import chromatic_progression
from util.Philhartronia.instrument_data_and_scales import major_1
from util.Philhartronia.instrument_data_and_scales import major_1_7
from util.Philhartronia.instrument_data_and_scales import minor_1
from util.Philhartronia.instrument_data_and_scales import minor_1_7

from util.Philhartronia.instrument_data_and_scales import major_2
from util.Philhartronia.instrument_data_and_scales import major_2_7
from util.Philhartronia.instrument_data_and_scales import minor_2
from util.Philhartronia.instrument_data_and_scales import minor_2_7

from util.Philhartronia.instrument_data_and_scales import major_3
from util.Philhartronia.instrument_data_and_scales import major_3_7
from util.Philhartronia.instrument_data_and_scales import minor_3
from util.Philhartronia.instrument_data_and_scales import minor_3_7

from util.Philhartronia.instrument_data_and_scales import diminished
from util.Philhartronia.instrument_data_and_scales import minor_7_flat_5


settings = defaults
settings["banned_effects"]                      = ["-c", "trill"]
settings["mandolin"]["pizz_threshold"]          = 999
# importing pygame module
import pygame
 
# importing sys module
import sys, os


 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((300, 300))
pygame.mixer.set_num_channels(256)
pygame.mixer.init()  # Initialize the mixer module.
# creating a running loop
instrument="guitar"
#scales=[major_1,minor_2,minor_2_7,major_3,minor_1_7,minor_2, major_2,major_2_7,minor_3,minor_1,pentatonic_scale]
scales=[major_3,major_3_7,major_2,major_2_7,major_1,major_1_7,pentatonic_scale,minor_3_7,minor_3,minor_2_7,minor_2,minor_3_7,minor_3]
scale_index = 0
key = 9
shifters=[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
shift = 3
while True:
       
    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        note = 0
        # z key
        if event.type == pygame.KEYDOWN: 
            print("k")
            # checking if key "A" was pressed
            
            note = None
            index = None
            if event.key == pygame.K_1:
                index = 0
            if event.key == pygame.K_2:
                index = 1
            if event.key == pygame.K_3:
                index = 2
            if event.key == pygame.K_4:
                index = 3
            if event.key == pygame.K_5:
                index = 4
            if event.key == pygame.K_6:
                index = 5
            if event.key == pygame.K_7:
                index = 6
            if event.key == pygame.K_8:
                index = 7
            if event.key == pygame.K_9:
                index = 8
            if event.key == pygame.K_0:
                index = 10 
            if event.key == pygame.K_MINUS:
                index = 11 
            if event.key == pygame.K_EQUALS:
                index = 12 
            
            if event.key == pygame.K_KP1:
                instrument = "guitar"
            if event.key == pygame.K_KP2:
                instrument = "banjo"
            if event.key == pygame.K_KP3:
                instrument = "mandolin"
            if event.key == pygame.K_KP4:
                instrument = "oboe"
            if event.key == pygame.K_KP5:
                instrument = "violin"
            if event.key == pygame.K_KP6:
                instrument = "cello"
            

            if event.key == pygame.K_LEFT:
                scale_index-=1
                if scale_index<0: scale_index = 0
            if event.key == pygame.K_RIGHT:
                scale_index+=1
                if scale_index>len(scales)-1: scale_index = len(scales)-1

            if event.key == pygame.K_UP:
               shift+=1


            if event.key == pygame.K_DOWN:
               shift-=1
               if shift < 0:
                   shift = 0


            scale = scales[scale_index]
            if index != None:
                note = scale[index]
                if note != None:
                    note += shift*shifters[scale_index]
                    note+=key
                    print(scale[:12], note, index)
                    sample, offset, note_speed, plucked, search_level, loudness_adjust, true_length = get_sample.get_sample(note, instrument, 64, 0.5, settings,instrument )
                    
                    if sample != None:
                        print(sample)  
                        sample=sample.split(".")[0]+".wav"    
                        sound = "util/Philhartronia/samples/Philhartronia-rt/"+instrument+"/"+sample
                        pygame_snd = pygame.mixer.Sound(sound)
                        pygame.mixer.Sound.play(pygame_snd)
                
                