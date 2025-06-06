I decided to create a small motif-generator for melodies in a random scale. It can be useful to psychologists who study musical perception, musicians to get some inspiration, and anyone else interested. The code uses no AI.

If you use windows, the MIDI file that you are doing to get can be played as is (it will be saved in the directory of your project). Otherwise, you might have to convert it from MIDI to mp3 manually.

The results are unique and distinguishable from each other. The code can create >1000 unique 4-second rhythms and >16000 unique 4-second melodies.

In its current state, it generates a 50-second sequence of power chords with the root in two octaves (e.g. A - F - A (octave higher than the previous A)) in an ambigous (either major or minor) scale, but it can be altered easily to play major or minor sequences, chords, intervals, and single notes.


