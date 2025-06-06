from midiutil import MIDIFile
import random

major_list = [0, 2, 4, 5, 7, 9, 11, 12, -2, -4, -5, -7, -9, -11, -12] #tones + semitones for major scales. the roots will vary by one of these numbers of semitones
minor_list = [0, 2, 3, 5, 7, 8, 10, 12, -2, -3, -5, -7, -8, -10, -12] #tones + semitones for minor
ntr_list =   [0, 2, 5, 7, 12, -2, -5, -7, -12] #all common tones + semitones btw major and minor for neutral/ambiguous scales

list_of_notes = list(range(36, 84)) #possible available notes (4 octaves seems fine)
list_of_rhythms = [1]
list_of_pitches = []
list_of_pitches.append(random.choice(list_of_notes)) #pick the first root note for the first chord in the progression
#vars
for i in range(200): #range - number of eights in the sequence in total
    list_of_rhythms.append(random.randint(0,1))
list_of_rhythms.append(1)
#the big idea here: there are 200 eights in total (imagine we are using the 4/4 measures). this action fills up the intermediate 198 eights with 1's and 0's to get a rhythm. like 10101001 means that the rhythm is smth like 4 - 4 - 4. - 8 and 11110101 means 8 - 8 - 8 - 8 - 4 - 4 -8; the first and the last eights are always filled bc I said so.
for j in range(201):
    new_note = list_of_pitches[j] + random.choice(ntr_list) # add one of the notes from the scale
    while new_note not in list_of_notes: # make sure the roots aren't too high or too low
        new_note = list_of_pitches[j] + random.choice(ntr_list) # repeat till we're happy
    list_of_pitches.append(new_note)
for k in range(1,201):
    if list_of_rhythms[k] == 0:
        list_of_pitches [k] = 0 #not really necessary; you can delete it prob

print(list_of_rhythms)
print(list_of_pitches)

#now the MIDI library magic
track = 0
channel = 0
time = 0  # In beats
duration = 2  # In beats
tempo = 120  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(list_of_pitches):
    MyMIDI.addNote(track, channel, pitch, time + (i/2), duration, volume * list_of_rhythms[i]) #add root to the audio
    MyMIDI.addNote(track, channel, pitch + 12, time + (i/2), duration, volume * list_of_rhythms[i]) # add an octave so it sounds DRAMATIC af
    MyMIDI.addNote(track, channel, pitch + 7, time + (i/2), duration, volume * list_of_rhythms[i]) #add 5'th

filename = "artificially written music.mid" #get 'em boys (files)! they'll appear in the same directory as the project
with open(filename, "wb") as output_file:
    MyMIDI.writeFile(output_file)
