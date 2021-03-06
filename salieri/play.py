# ## For acquiring and using music theoretical data
# import mingus.core.progressions as progressions
# import mingus.core.chords as chords
# import mingus.core.scales as scales
# import mingus.core.intervals as intervals
# import mingus.core.notes as notes

# ## For writing notes, chords bars, tracks, comps
# from mingus.containers import Note
# from mingus.containers import NoteContainer
# from mingus.containers import Bar
# from mingus.containers import Composition as Mcomposition
# from mingus.containers import Track as Mtrack

# ## For improvisation and randomized generation
# # import random

# ## For writing MIDI
# from mingus.midi import midi_file_out

from Sfunctions import *
tonic = "C"

# print(chords.seventh(tonic)) ## gives Cdom7???
# print(chords.dominant7("C"))  ## Gmaj7!?
# print(chords.major_seventh("G"))

tonic = "D"
# note = Note(tonic)
# print(note)
# note.transpose("1", False)
# print(intervals.minor_seventh("D"))
# print(type(intervals.minor_seventh("D")))
chord = chords.major_triad(tonic)
minor_7 = intervals.minor_seventh(tonic)
chord.append(minor_7)
print(chord)













































































# #####===================================================================

# def silence():
#     """
#     ===prototype===
#     Fills a bar with silence...
#     Helpful logistically and musically!

#     """
#     bar = Bar()
#     # print(bar.current_beat)
#     # bar.place_rest(1)
#     bar.place_rest(4)
#     bar.place_rest(4)
#     bar.place_rest(4)
#     bar.place_rest(4)
#     # print(bar.current_beat)
#     # print(bar.length)
#     return bar

# #####

# def rest_test():
#     bar = Bar()
#     note = Note("A")
#     bar.place_notes(note, 4)
#     bar.place_rest(4)
#     bar.place_rest(4)
#     bar.place_notes(note, 4)
#     # bar.place_notes(note, 4)
#     # bar.place_notes(note, 4)
#     return bar

# #####
# def quarters():
#     bar = Bar()
#     note = Note("A")
#     bar.place_notes(note, 4)
#     bar.place_notes(note, 4)
#     bar.place_notes(note, 4)
#     bar.place_notes(note, 4)
#     return bar


# #####===========================================================

# test_track = Mtrack()
# b1 = silence()
# b2 = quarters()


# # test_bar = rest_test()
# # print(type(test))
# test_track.add_bar(b1)
# test_track.add_bar(b2)


# # midi_file_out.write_Bar("stests/silence.mid", test_bar, 120)
# midi_file_out.write_Track("stests/moretests.mid", test_track, 120)

# ##=====================

# # def rest_test():
# #     bar = Bar()
# #     note = Note("A")
# #     bar.place_notes(note, 4)
# #     bar.place_notes(note, 4)
# #     bar.place_notes(note, 4)
# #     bar.place_notes(note, 4)
# #     return bar