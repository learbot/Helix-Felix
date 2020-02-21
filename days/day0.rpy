#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  day1.rpy
#  
#  Copyright 2020
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#day 0
label day0:
  
  cards:
    with_in dissolve
    delta_t 5.0
    with_out False
    card partone
    start #always last command
  
  #if with_out is False, always need  an scene to do transsition (dissolve,bites,etc) or hide(card)
  scene bg playroom
  with bites#dissolve
  #show side Addison surprised
  #with dissolve
  $ persistent.bg_playroom=True
  $ config.side_image_tag ="addison"

  a surprised "Oof!"
  a surprised "Ahh-"
  a surprised "Now who left their toys around here?"

  show charlie sad
  with easeinright
  show ainsley sad 
  with easeinleft

  c sad "I'm sorry Addison--I was going to put them away!"

  a sad "How are you going to get adopted if you can't clean up after yourself?"
  a happy "Well, let's put them away together okay?"

  c happy "Okay!"
  g happy "Okay!"

  hide charlie
  with easeoutleft
  hide ainsley
  with easeoutright

  "There's something so charming about them. I can never stay mad at them."
  "All the kids here are like that."
  "It's hard to be a Big Brother for all 87 siblings, but the effort is worth every bit. Whenever they smile, I would always smile back."
  "The smallest ones like to play the most, and it's important that I tire them out."

  a "What kind of games do we want to play today?"

  show ainsley happy 
  with easeinright

  g "Tag!"

  show charlie happy
  with easeinleft

  c "Sardines!"

  "All of the children gathered around start to shout their recommendations at once."
  
  hide charlie
  hide ainsley
  hide addison
  
  $ config.side_image_tag = "alfa" # when you use CG
  show simonsays onlayer event
  with dissolve

  a "Okay, okay, how about Simon Says?"
  g "Addy Says! Let's play Addy Says!"
  a "Alright everybody, then spread out a little bit so you don't bump into each other."
  a "Are you ready to start?"
  a "Simon says... touch your elbow."
  g "Hehehe!"

  "Most of the kids are between four and ten."
  "By that age most have been adopted, but there are always a few that are older."
  "I'm the eldest at 23, but I'm not up for adoption so I don't really count."
  "After that is Pumpkin at 18, and then a handful of others waiting to find their Masters."
  "They're a bit old for games, so they stay off in other corners of the play room, reading, relaxing, or studying."

  a "Simon says... raise your hands!"

  "Of course I can't play with all of the kids at once. Today's Simon Says game has about 20 kids in it."

  a "Simon says... twirl like a ballerina!"

  "Today I have to keep them distracted every time they come out of class."
  "Stacy was adopted and left us last night. It's always bittersweet when someone gets to go."
  "A loving Master is all any of the children want, but missing their friend is really hard on their little hearts."

  a "Simon says... hug your tummy!"

  "It always makes my heart feel small and tight, but I'm happy for them. At the same time, I'm jealous of them, too."

  a "Simon says... jump up and down!"

  "It's been ten years since I was taken off of the sales list, so I've had a long time to come to terms with the fact that I'm never going to have a Master."
  "In the beginning, it hurt more than I could describe, I felt ashamed and unworthy--dirty, even."
  "I was selfish because all I wanted was a Master to love me and take care of me."
  "Since then the feeling has healed to a dull ache. I have lots of responsibility to take from now on." 
  "Between my role as a Staff Companion and as a Big Brother, I'm going to distract myself from those sad feelings every day from now on."

  a "Simon says... clap your hands!"

  "It can't be helped."

  a "... Touch your nose!"
  a "Aw! I got you! I didn't say 'Simon Says!'"
  c "Awww. I'm out."
  g "Hehehe. Let's keep going!"
  
  hide simonsays onlayer event
  with dissolve
  $ config.side_image_tag = None #end CG
  
  show ainsley happy
  show charlie happy

  "The game continued, then eventually we started playing Telephone in a big circle on the floor."
  "Watching everyone whisper into each others' ears, accidentally giving tickles, the muffled giggling at whatever silly phrase had been mutated. It's nice to see them getting along so well."
  "I take a glance at the clock. Another hour until the dinner bell rings meant more playtime and more giggles."
  "I lean in for Charlie to whisper in my ear."

  c "Go faster, there's a beehive in his dresser."
  a laugh "I started with 'My Master is the best at playing Checkers,' and now it's 'Go faster, there's a beehive in his dresser.' Who would have guessed a beehive in their dresser?"
  g "Hehehehe!"

  hide charlie
  with easeoutleft
  hide ainsley
  with easeoutright

  "We get a few more laughs before I turn the kids loose to play on their own while I walk around the playroom and check on everyone."
  "I've found out that it's best to do this so I can find anything wrong before it's big enough to be brought to me."
  "I've stopped fights, helped reach shelves, sat with lonely children. I’m always here to help by making everyone happy and that’s what I’m here for.."
  "It seems like today everyone is alright though, even though a few are still understandably upset by Stacy's adoption. I'm proud that I've taught them how to handle this without acting out."
  "The dinner bell sounds through the room, a gentle reminder for everyone to set down their toys."
  
  a happy"Dinner time! Make a single-file line!"

  "They all clamor to form the line. I keep to the side so that I can still have my eye on everyone."
  "Of course, I don't really need to be here for this."
  "Mr. Jesse is the supervisor and he can form the line, or the kids could probably even do it by themselves. But they're always glad to have me around, and I'm always glad to be here too."

  scene bg hallway1
  with dissolve
  pause (2)
  $ persistent.bg_hallway1=True
  scene bg cafeteria
  with dissolve
  $ persistent.bg_cafeteria=True
 
  "The smell of warm vegetables and a wonderful sauce surrounds the cafeteria. Now that everyone is out of class, all of us are here together."
  "Big mounds of mashed potatoes, gravy, chicken, and green beans fill everyone's plates. The chatter echoes off the walls into a comforting hum as I sit quietly and eat."
  "We're so lucky to be so well taken care of, and the only thing the humans ask of us is to live with them and love them. Felixes must have the best lives in the whole world."
  "After dinner, the kids line up again and head back to the barracks for showers and bedtime."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg barracks
  with dissolve
  $ persistent.bg_barracks=True
 
  "With a lot of squabbling and fussing, they pick out a book for me to read to them before bed it looks like they pick a silly story about a stuffed bear and his friends having an adventure." 
  "This time, almost everyone is listening to me, wiggling their toes and their tails under the covers while I try to make silly voices for each character."
  "When the story comes to a close, I give out a soft 'Goodnight' and turn out the barrack's lights."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg bedroomlight
  with dissolve
  $ persistent.bg_bedroomlight=True

  play music musicsleepy loop

  "My own room feels cozy compared to the large and open barracks. It took me a while to get used to, but now that I've settled in I couldn't imagine leaving." 
  "I have a few pictures taped to the walls, both mine and a few of the kitten's."
  "My desk is a mess of papers and colored pencils, even a row of coloring books pushed to the side." 
  a pajamas happy "Hmm...~"
  "I would usually use this time to draw for myself, but today has been long and tiring. I spent it almost entirely with the children."
  "With a big yawn, I turn out the lights and crawl under my covers."

  scene bg bedroomdark
  with dissolve

  "Another dream tonight and another day tomorrow."
  a "Goodnight."

  scene bg bedroomdark
  with dissolve
  $ persistent.bg_bedroomdark=True
  pause (1)
  
  cards open card1
  
  scene bg bedroomlight
  with fade
  jump day1
