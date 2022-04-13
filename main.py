import numpy as np
import pretty_midi

markovMatrix = np.zeros((87, 87))
transitionMatrix = np.zeros((87, 87))
noteArray = []
piMatrix = np.zeros([87])
piMatrix.fill(1)

# Load MIDI file into PrettyMIDI object
midi_data = pretty_midi.PrettyMIDI(inputMidi)
# Shift all notes up by 5 semitones
for instrument in midi_data.instruments:
    for note in instrument.notes:
        noteArray.append(note.pitch)
print(noteArray)
# need to be able to find probability using "occurrences/total"
noteArraylen = len(noteArray)
noteArraymeasure = len(noteArray)-1
#print(noteArraymeasure)
#print(markovMatrix)

i = 0
for i in range(noteArraymeasure):
    hold = 1
    #print(noteArray[i])
    #print(noteArray[i+1])
    markovMatrix[noteArray[i]][noteArray[i+1]] = (markovMatrix[noteArray[i]][noteArray[i+1]])+1
    #markovValue = markovMatrix[i][i+1]
    #[0][0] = (markovMatrix[0][0]) + 1

#markovMatrix.tofile('matrix.txt', ' ')
#print(np.sort(markovMatrix, axis=None))

piMatrix[0] = 1

for j in range(87):
    for k in range(87):
        transitionMatrix[j][k] = (markovMatrix[j][k])/noteArraylen

transitionMatrix.tofile('matrix2.txt', ' ')
print(np.sort(transitionMatrix, axis=None))

for h in range(20):
    state = np.dot(noteArray, transitionMatrix)

print(state)
