I decided to create a small motif-generator for melodies in a random scale. It can be useful for psychologists who study musical perception to generate the stimuli for their experiments, for musicians to get some inspiration, or anyone else interested. The code uses no AI and works relatively quickly.

If you use windows, the MIDI file that you are going to get can be played as is (it will be saved in the directory of your project). Otherwise, you might have to convert it from MIDI to mp3 manually. If you think you ever need to convert many files from midi to mp3, you can download this free converter: https://2140-4-75211970.en.softonic.com/. 

The results are unique and distinguishable from each other. The code can create > 1000 unique 4-second 120 BPM rhythms and > 1.8 * 10^15 unique 4-second melodies.

In its current state, it generates a 50-second sequence of power chords with the root in two octaves (e.g. A - F - A (octave higher than the previous A)) in an ambigous (either major or minor) scale, but it can be altered easily to play major or minor sequences, chords, intervals, and single notes in any scale (you would have to set up the first root note to be from the desired scale in this case).

The code basically assigns the sequence of 0's and 1's to a string of 200 eighths in a 4/4 measure. 1 means that the eighth is palyed, 0 means that it's not. Then I add a random number from the list of intervals in the scale to determine the pitch of the next eighth (so it would stay within the scale).

I'm new to github, so let me know if there's something else I should add or someone else I should give credit to.
