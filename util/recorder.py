#!/usr/bin/env python3

# Scott's MusicBox
# recorder.py by Scott Yannitell
# Copyright 2022 all rights reserved

# arranger.py sends a list of samples and tempos to this script
# which uses ffmpeg to place each sample in a progression to produce a musical
# track per instrument. Then it uses sox to combine the tracks into a mixed
# final soundtrack depending on levels determined from the project settings

# FFMPEG's file number limitation isn't so bad when breaking apart the rendering
# process into chunks because ffmpeg works very well in paralell. It would
# indeed be possible to make a kind of primitive renderfarm with this method
# to enable vastly faster previews of composition results. Although as it stands
# now unless you are rendering bach or baroque, its plenty fast enough not to
# get annoyed by the rendering wait time.

# Significant challenges were first found due to earlier versions of ffmpeg
# having a wierd issue with decreasing the volume of consecutive inputs but
# in versions after 5.0 an alternative was found. I used a custom compiled 
# version of FFMPEG to get this to work as repos for it don't have this 
# facility built in.

# I found the limit to shell command line max size to be annoying but fortunately
# this is not a problem for ffmpeg, thankfully, because it can put filter graphs
# in external files to greatly minimize command string lengths.

# currently there is a problem with stopping the script while it is in the 
# middle of processing with mutliple FFMPEG instances. Sometimes FFMPEG
# instances refuse to die and become zombie processes. You'd think this should
# never be a problem in Linux. But it sure is...

import os
from time import sleep
from time import time
import signal
from os.path import exists
import audioread

def get_sound_length(filename):
    with audioread.audio_open(filename) as f:
        return f.duration

def render(settings, track, instrument, instrument_designation_):
    global instrument_designation
    instrument_designation = instrument_designation_
    # a simple killall ffmpeg wouldn't work no matter what I tried
    # but ffmpeg must all die before we begin
    # Ask user for the name of process

    try:
        # iterating through each instance of the process
        for line in os.popen("ps ax | grep ffmpeg | grep -v grep"):
            fields = line.split()
             
            # extracting Process ID from the output
            pid = fields[0]
             
            # terminating process
            os.kill(int(pid), signal.SIGKILL)
        print("Process Successfully terminated")
         
    except:
        print("Error Encountered while running script")

    starting_time = time()
    nuller=" >/dev/null 2>&1"
    os.system("rm FFMPEG-PROCESS-FOLDER/*")
    os.system("sox -n -r 44100 FFMPEG-PROCESS-FOLDER/tail.wav trim 0.0 8.0")
    ffmpeg              = "util/Philhartronia/bin/ffmpeg/./ffmpeg -y "
    ffmpeg_inputs       = ""
    ffmpeg_filters      = ""
    ffmpeg_filter_tail = ""
    ffmpeg_end     = " -ac 2 -c:a pcm_s24le"
    sequence_index = 0
    sequence_prefix = "file"
    operation_count = 0
    ffmpeg_render_files = 0
    file_count = 0
    used_note_count = 0
    concatter = ""
    data_counter = 0
    
    for sample_num in range(0, len(track)):
        # sample, ontime-offset, note_speed, plucked
        sample_info            = track[sample_num]
        sample                 = "util/Philhartronia/samples/Philhartronia/"+instrument+"/"+sample_info[0]
        sample_on_time         = sample_info[1] * 1000 # convert seconds to ms
        sample_speed           = sample_info[2]
        sample_is_plucked      = sample_info[3]
        search_level           = sample_info[4]
        note                   = sample_info[5]
        sample_loudness_adjust = sample_info[6]
        true_length            = sample_info[7]
        pan_shift              = sample_info[8]
        
        if len(settings["instruments"]) > 1:
            sample_pan             = -1.0 + (2.0 / (len(settings["instruments"])-1)) * settings["instruments"].index(instrument_designation) + pan_shift 
        else:
            sample_pan = 0
        
        play_command = "play -v "+str(sample_loudness_adjust)+" "+sample+" tempo "+str(sample_speed)+nuller
        print(note)
        print(sample_speed)
        print(search_level)
        #print(play_command)
        print()
        #sleep(1)
        #os.system(play_command)
        # calculate gain for pan
        left_pan  =1.0+sample_pan
        right_pan =1.0-sample_pan
        
        if sample_is_plucked: sample_speed = 1
    
        operation_count+=1
        used_note_count+=1
        
        fade_length = 0.033333
        fade_start  = true_length - fade_length
        
        ffmpeg_inputs  +=" -i "+sample+" "

        # rubberband tempo
        filter_ = "[$sequence_index1]\nvolume=$volume1,\nrubberband=tempo=$tempo1,\nadelay=$delay1|$delay1,\npan=stereo|c0=$pan1a*c0|c1=$pan1b*c0\n[$seqenceID1];\n\n"
        
        # atempo: inferor to rubberband
        #filter_ = "[$sequence_index1]\nvolume=$volume1,\natempo=$tempo1,\nadelay=$delay1|$delay1,\npan=stereo|c0=$pan1a*c0|c1=$pan1b*c0\n[$seqenceID1];\n\n"
        
        # no tempo
        #filter_ = "[$sequence_index1]\nvolume=$volume1,\nadelay=$delay1|$delay1,\npan=stereo|c0=$pan1a*c0|c1=$pan1b*c0\n[$seqenceID1];\n\n"
        
        filter_ = filter_.replace("$sequence_index1", str(sequence_index))
        filter_ = filter_.replace("$volume1", str(sample_loudness_adjust))#+"*FIXIT")
        filter_ = filter_.replace("$delay1", str(sample_on_time))
        filter_ = filter_.replace("$pan1a", str(left_pan))
        filter_ = filter_.replace("$pan1b", str(right_pan))
        filter_ = filter_.replace("$tempo1", str(sample_speed))
        filter_ = filter_.replace("$seqenceID1", sequence_prefix+str(sequence_index))
        ffmpeg_filters += filter_ 
        
        ffmpeg_filter_tail+="["+sequence_prefix+str(sequence_index)+"]"
        sequence_index+=1
        
        if operation_count > 100:
            ffmpeg_filter_tail+="amix=inputs="+str(sequence_index)+":normalize=false"
            complete_filter = ffmpeg_filters+ffmpeg_filter_tail
            filters_file = "FFMPEG-PROCESS-FOLDER/ffmpeg_filters."+str(file_count)+".txt"
            file1 = open(filters_file, "w")
            file1.write(complete_filter)
            file1.close()    
            
            output_file_part = "FFMPEG-PROCESS-FOLDER/music."+str(file_count)+".wav"
            concatter+=" -v 1 "+output_file_part+" "
            ffmpeg+=ffmpeg_inputs+" -filter_complex_script "+filters_file+" "+ffmpeg_end+" "+output_file_part
        
            ffmpeg_file = "FFMPEG-PROCESS-FOLDER/ffmpeg."+str(file_count)+".sh"
            file1 = open(ffmpeg_file, "w")
            file1.write(ffmpeg)
            file1.close()
            os.system("chmod +x "+ffmpeg_file)

            file_count+=1
            operation_count     = 0
            sequence_index      = 0
            ffmpeg_inputs       = ""
            ffmpeg_filters      = ""  
            ffmpeg_filter_tail  = "" 
            ffmpeg              = "util/Philhartronia/bin/ffmpeg/./ffmpeg -y "
                            
        data_counter+=1
        # if there are remaining samples, take care of them here
        if data_counter == len(track):
            ffmpeg_inputs  +=" -i FFMPEG-PROCESS-FOLDER/tail.wav"
            tail_filter = "["+str(sequence_index)+"]adelay="+str(sample_on_time+3000)+"|"+str(sample_on_time+3000)+"["+sequence_prefix+str(sequence_index)+"];"
            ffmpeg_filters += tail_filter 
            ffmpeg_filter_tail+="["+sequence_prefix+str(sequence_index)+"]"
            ffmpeg_filter_tail+="amix=inputs="+str(sequence_index+1)+":normalize=false"
            complete_filter = ffmpeg_filters+ffmpeg_filter_tail
            filters_file = "FFMPEG-PROCESS-FOLDER/ffmpeg_filters."+str(file_count)+".txt"
            file1 = open(filters_file, "w")
            file1.write(complete_filter)
            file1.close()    
            
            output_file_part = "FFMPEG-PROCESS-FOLDER/music."+str(file_count)+".wav"
            concatter+=" -v 1 "+output_file_part+" "
            ffmpeg+=ffmpeg_inputs+" -filter_complex_script "+filters_file+" "+ffmpeg_end+" "+output_file_part

            ffmpeg_file = "FFMPEG-PROCESS-FOLDER/ffmpeg."+str(file_count)+".sh"
            file1 = open(ffmpeg_file, "w")
            file1.write(ffmpeg)
            file1.close()
            os.system("chmod +x "+ffmpeg_file)

            file_count+=1
            operation_count     = 0
            sequence_index      = 0
            ffmpeg_inputs       = ""
            ffmpeg_filters      = ""  
            ffmpeg_filter_tail  = "" 
            ffmpeg              = "ffmpeg -y "

    print("fix annoying gain issues")

    # The only useful reddit comment in the entire universe:
    # https://www.reddit.com/r/ffmpeg/comments/d63fki/comment/i3woeif/?utm_source=share&utm_medium=web2x&context=3
    
    # and it solves a huge problem I had with figuring out the stupid gain problem

    print("activate parallel processor")
    for i in range(0,file_count):
        ffmpeg_file = "FFMPEG-PROCESS-FOLDER/ffmpeg."+str(i)+".sh "+" &"
        os.system(ffmpeg_file)
        os.system("ps -Al | grep -c ffmpeg > /tmp/numFFMPEG.txt")
        sleep(0.1)
        number_of_ffmpegs = int(open("/tmp/numFFMPEG.txt").read())
        while number_of_ffmpegs > 8:
            os.system("ps -Al | grep -c ffmpeg > /tmp/numFFMPEG.txt")
            sleep(0.1)
            number_of_ffmpegs = int(open("/tmp/numFFMPEG.txt").read())
            print("waiting")

    print("wait for ffmpegs to exit")
    number_of_ffmpegs = int(open("/tmp/numFFMPEG.txt").read())

    while number_of_ffmpegs > 0:
        os.system("ps -Al | grep -c ffmpeg > /tmp/numFFMPEG.txt")
        sleep(0.1)
        number_of_ffmpegs = int(open("/tmp/numFFMPEG.txt").read())
        print("waiting")
    # this is a hack so that if only one music file is spit out, the rest of the commands don't go down like dominos
    os.system("cp FFMPEG-PROCESS-FOLDER/music.0.wav FFMPEG-PROCESS-FOLDER/concatted.wav")
    print("concatinating segments")        
    
    sox_command="sox -m " + concatter + "FFMPEG-PROCESS-FOLDER/concatted.wav"
    os.system(sox_command)
    print(sox_command)
    print("normalize sequence") 

    outpath = "project_outputs/"+settings["project_name"]+"/"
    final_output = outpath+instrument_designation+".wav"
    
    reverberance = str(settings["reverberance"])                       
    room_scale   = str(settings["reverb_room_scale"])                  
    stereo_depth = str(settings["reverb_stereo_depth"])                  
    hf_dampening = "50" 
    sox_command="sox FFMPEG-PROCESS-FOLDER/concatted.wav FFMPEG-PROCESS-FOLDER/verbed.wav reverb "+reverberance+" "+hf_dampening+" "+room_scale+" "+stereo_depth
    print(sox_command)
    os.system(sox_command)
    os.system("sox --norm FFMPEG-PROCESS-FOLDER/verbed.wav FFMPEG-PROCESS-FOLDER/normalized.wav")
    instrument_level = settings[instrument_designation]["volume"] * (1.0/len(settings["instruments"]))
    sox_command="sox -v "+str(instrument_level) + " FFMPEG-PROCESS-FOLDER/normalized.wav FFMPEG-PROCESS-FOLDER/volumed.wav"
    print(sox_command)
    os.system(sox_command)
    os.system("cp FFMPEG-PROCESS-FOLDER/volumed.wav "+str(final_output))
    
def mixdown(settings):
    global instrument_designation
    mix_string = ""
    outpath = "project_outputs/"+settings["project_name"]+"/"
    for instrument in settings["instruments"]:
        file = outpath+instrument+".wav"
        # sometimes an instrument is so far out of range there are no notes and thus, no file either.
        if exists(file):
            mix_string+=" -v 1 "+file+" "
            
    final_filename =settings["input_midi"].split("/")[-1].split(".mid")[0]+".wav"
    print("final_filename", final_filename)
    if len(settings["instruments"]) > 1:
        sox_command = "sox -m " + mix_string + " /tmp/mix.wav"
        print("sox_command", sox_command)
        os.system(sox_command)
        sox_command = "sox --norm /tmp/mix.wav /tmp/mix-norm.wav"
        os.system(sox_command)
        sox_command = "sox -v "+str(settings["master_volume"])+" /tmp/mix-norm.wav /tmp/pretrim.wav"
        os.system(sox_command)
    else:
        os.system("sox --norm "+mix_string+" /tmp/mix-norm.wav")
        os.system("sox -v "+str(settings["master_volume"])+" /tmp/mix-norm.wav /tmp/pretrim.wav")

    # just removing extra silence from the start and end of a file
    sox_command = "sox /tmp/pretrim.wav /tmp/front.wav silence 1 .1 .1"
    os.system(sox_command)

    sox_command = "sox /tmp/front.wav /tmp/back.wav reverse silence 1 .1 .1"
    os.system(sox_command)

    file_duration0 = get_sound_length("/tmp/pretrim.wav")
    file_duration1 = get_sound_length("/tmp/front.wav")
    file_duration2 = get_sound_length("/tmp/back.wav")
    os.system("sox /tmp/pretrim.wav -b 16 "+outpath+final_filename+" trim "+str(file_duration0-file_duration1-1)+" "+str(file_duration2+1.5))


