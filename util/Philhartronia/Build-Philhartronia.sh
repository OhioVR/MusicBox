#!/bin/bash
set -e # exit above 0

# MusicBox - Build-Philhartronia.sh
# copyright 2022 Scott Yannitell

# Build-Philhartronia.sh
# this script downloads all required dependancys if needed
# and then downloads, processes, and catalogs the samples
# for the get_sample.py script

# you need to run this at least once before you can use the
# SIPR engine aka Philhartronia Synthesizer to record your
# midi files into wavs.

# You can safely run this script any number of times without
# having to redownload and compile the samples or ffmpeg.
# The whole script takes at least an hour to finish perhaps
# two on a desktop. On a raspberry pi it could take a day.



# https://unix.stackexchange.com/a/314370
start_time="$(date -u +%s)"

# this little pattern of || {} means that
# the bracketed code will only execute
# if apt does not find ffmpeg in the installed
# packages

################################################
# download all dependancies and compile ffmpeg #
################################################
apt-cache show ffmpeg || {

    # we meed ffmpeg's main apt package for sox
    # sox doesn't handle even mp3s by default
    # so the full codec package is installed

    # pypy3 is a turbo compiler for python3
    # rubberband-cli is needed for healing the samples
    # pip is needed for installing python3 packages
    sudo apt install \
        curl pypy3-dev sox libsox-fmt-all rubberband-cli python3-pip ffmpeg -y

    # mido is what makes midi work in MusicBox
    # audioread is needed by pypy scripts that
    # can't use librosa
    # numpy is a dependancy of audioread IIRC
    pypy3 -mpip install audioread numpy mido
    pip3 install librosa pydub

    #############################################
    # custom ffmpeg required build dependancies #
    #############################################
    sudo apt-get install git make nasm pkg-config libx264-dev libxext-dev libxfixes-dev zlib1g-dev librubberband-dev rubberband-ladspa  -y


}

mkdir -p bin/ffmpeg
    # if git sees the folder is not empty it will not download
    # and compile
    git clone https://git.ffmpeg.org/ffmpeg.git bin/ffmpeg && {
        cd bin/ffmpeg
        ./configure --enable-nonfree --enable-gpl --enable-libx264 --enable-zlib --enable-librubberband

    make
}


###############################
# download if necessary and   #
# unpack the philharmonia     #
# samples into a fresh folder #
###############################

rm -rf samples/Philharmonia_original 2>&1 || true
rm -rf /tmp/Philharmonia 2>&1 || true

philhatronia=$PWD
mkdir -p samples
cd samples
set -e
[ -f Philharmonia.zip ]  || {
    curl "https://archive.org/compress/philharmonicorchestrasamples/formats=ZIP&file=/philharmonicorchestrasamples.zip"  -L -o Philharmonia.zip
}
cd $philhatronia

mkdir -p samples/Philharmonia_original
cd samples/Philharmonia_original
finaldir=$PWD

mkdir -p banjo bass-clarinet bassoon cello clarinet contrabassoon double-bass english-horn flute
mkdir -p french-horn guitar mandolin oboe percussion trombone trumpet tuba viola violin

cd ..
mkdir -p /tmp/Philharmonia/
unzip Philharmonia.zip -d /tmp/Philharmonia/
cd /tmp/Philharmonia
unzip cello.zip -d $finaldir/cello/
unzip trombone.zip -d $finaldir/trombone/
unzip tuba.zip -d $finaldir/tuba/
unzip "bass clarinet.zip" -d $finaldir/bass-clarinet/
unzip "double bass.zip" -d $finaldir/double-bass/
unzip "guitar.zip" -d $finaldir/guitar/
unzip bassoon.zip -d $finaldir/bassoon/
unzip violin.zip -d $finaldir/violin/
unzip "french horn.zip" -d $finaldir/french-horn/
unzip banjo -d $finaldir/banjo/
unzip trumpet.zip -d $finaldir/trumpet/
unzip mandolin.zip -d $finaldir/mandolin/
unzip percussion.zip -d $finaldir/percussion/
unzip clarinet.zip -d $finaldir/clarinet/
unzip contrabassoon.zip -d $finaldir/contrabassoon/
unzip oboe.zip -d $finaldir/oboe/
unzip viola.zip -d $finaldir/viola/
unzip flute.zip -d $finaldir/flute/
unzip "cor anglais.zip" -d $finaldir/english-horn/
unzip "saxophone.zip" -d $finaldir/saxophone/





#####################################
# heal, filter, and catalog samples #
# extend arco strings               #
#####################################

cd $philhatronia

rm -rf samples/Philharmonia_healed
rm db/Philharmonia_healed-unsorted.json 2>&1 || true
rm db/Philhartronia-unsorted.json 2>&1 || true
rm -rf db/Philharmonia_healed.json >/dev/null 2>&1 || true
rm -rf samples/Philhartronia 2>&1 || true
rm -rf samples/Philharmonia_extended 2>&1 || true

# First heal the samples by filling in places we took out or that were
# left out.
./heal-Philharmonia-samples.py
# filter the healed samples and place the results right back in
./sample-filter.py Philharmonia_healed
# run the database to get the middle min and max information for
# crossfade_arco.py
./database_builder.py Philharmonia_healed

#./crossfade_arco.py

# the extended samples are really already prefiltered anyway.
######./sample-filter.py Philharmonia_extended
rsync -av samples/Philharmonia_extended/ samples/Philhartronia/
rsync -av samples/Philharmonia_healed/ samples/Philhartronia/

./database_builder.py Philhartronia

end_time="$(date -u +%s.%N)"

elapsed="$(bc <<<"($end_time-$start_time)/60")"
echo "Total of $elapsed minutes elapsed for build and download process"
