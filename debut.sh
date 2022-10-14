#!/bin/bash

set -e


# https://unix.stackexchange.com/a/314370
start_time="$(date -u +%s)"

# avoid too many open files issue
ulimit -n 50000

# Debussy
./Debussy-Rêverie.py

# Bartok: 6 Romanian folk dances
./1.Der-Tanz-mit-dem-Stabe.py
./2.Brâul.py
./3.DerStampfer.py
./4.Tanz-aus-Butschum.py
./5.Rumänische-Polka.py
./6.Schnell-Tanz.py

# custom arrangement of virtuoso piano tune
./"Bartok Romanian Dances op 8a first movement.py"

# pretty gospel song
./Be-Thou-My-Vision.py

# Melancholy Waltz
./Chopin-Mazurka.py

# Pretty song
./clara-schumann-am-strand.py

# love song
./Fanny-Mendelssohn-6-Lieder-Op.1-no-6-Gondellied.py

# Funny sounding baroque song
./Farrenc-Etude-No2.in_A_minor_op50.py

# ancient song
./Hildegard-o-pastor.py

# impressionistic song
./lili-boulanger-un-jarden-clair.py

# annoying Mozart song
./Mozart-turkish-march.py

# Baudy Waltz
./Teresa-Carreno.py

# jazz
./whispering.py

# Scott's amateur composition
./working-on-problems.py

end_time="$(date -u +%s.%N)"
elapsed="$(bc <<<"($end_time-$start_time)/60")"
echo "Total of $elapsed minutes elapsed for build and download process"
