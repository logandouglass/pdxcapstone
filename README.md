# pdxcapstone: Salieri (working title, but funny)

## Overview
There's lots of music composition software out there, and some of it is incredibly powerful (think Ableton Live).  However, all of them come with drawbacks.  Even the best software can be hard to learn and time-consuming to use if you are not in practice with a keyboard instrument, or if you do not know how to fluently read and write sheet music.  It would be nice if there was software to bridge the gap for those who want to enjoy the benefits of digital composition, but aren't classically-trained or proficient keyboardists.  Salieri helps fill that gap, and allows users conversant in basic to intermediate music theory to quickly compose MIDI for multiple instruments at once.  Salieri is great for experimenting and generating MIDI for a variety of purposes, and it doesn't cost a damn thing.

(Notable Dependencies: Mingus)

## Features

#### ** As a music teacher, I want to be able to create MIDI tracks my students can use to practice improvisation and keeping time with a band. **

### Tasks:
* Create a Django model for user-input chord progression
* Create django models for multiple tracks (bassline, chord accompaniment, lead) linked to chord progression
* Figure out how to harvest the user input data from models and feed it into my python program
* Allow user to download the MIDI file generated by my python program

#### ** As a developing musician, I want to be able to quickly compose digital musical experiments and hear the results. **

### Tasks: 
* Create a variety of functions that can be used to customize the rhythm, bass, and lead lines.  (different arpeggios, strum patterns, generalizable licks and phrases, etc)
* Add a site-mounted MIDI player to test the composition (if I can figure out how to implement it)

### Scheme
Honestly it's going to be hard to get the models right, I'll need to think a little before I map it all out.

### Week 1
* Create & Clone Repo
* Create Virtual Environment
* Start Django Project
* Write models that will collect user input to be passed to my improved Python music generation minicapstone (getting this to work and making the front-end intuitive will be one of the hardest parts)
* MVP of models (if lucky)
  
### Week 2
* finish MVP of models (if need be)
* write, write, write enough functions to give the user some degree of compositional freedom
* figure out how user can download the generated MIDI file 


### Week 3
* write CSS
* research site-mounted MIDI-player, see if it's viable
* if viable: begin implementation
* else: continue CSS and beefing up of functions

  
### Week 4
* if MIDI-player viable: continue implementation
* else: clean up CSS and enrich user options as much as time allows
* deploy to heroku


## Feature Tiers:
### Must Haves
* ability to write a short clip of music as MIDI (at least a decent-length chord progression)
* can take in a chord progression entered by the user
* ability to take in at least major and minor chords
* can write multiple tracks at once (at least chord accompaniment, a bassline, and a lead/melody line)
* allows users to customize each track (ex: different strum patterns, chord-picking patterns, etc)
* ability to download compositions as MIDI
* enough functions to make some fun clips and at least some musical variety possible
* intuitive UI usable by someone who knows basic to intermediate music theory but isn't exactly Mozart
  
### Should Haves
* attractive (but probably minimalistic) UI
* ability to take in at least a few more common chord varieties (dim7, maj/min/dom7s, etc)


### Can Haves
* site-mounted MIDI-player that lets you listen to your composition without downloading and opening it in an external MIDI player (uff, maybe a "should have" but I'm scared of this one...)

### (Probably) Won't Haves... (for the future, if I stick with it)
* robust chord support ("augmented 7th flat 9th?  we got those!")
* ability to write an entire song with multiple progressions in one go 
pre-selectable progression templates
* ability to generate a randomized "solo" over the progression
* robust enough function variety to make sophisticated compositions 
* ability to log in, save your compositions
* percussion (ugh, working on it)
