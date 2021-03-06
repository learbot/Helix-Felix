#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  day5_6.rpy
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


#day 5
label day5:
  calendar day 5
  play music musicsleepy loop
  
  a pajamas sleepy "Hm?"
  
  "Morning? I must have slept like a dead person."
  "Rubbing my eyes, I stretch my legs to try and help my body wake up, my tail straightening with them."
  "Good morning."
  "Brushing my teeth and getting dressed, I can feel my muscles complain at every act. The bed is all I want. It's like I haven't really woken up yet."
  "Maybe some breakfast will do something."
  
  a happy "Okay!"
  
  play music musicneutral loop

  scene bg hallway1
  show pumpkin happy
  with dissolve

  p "Addy, come sit with me!"
  a laugh "Alright."

  "It's usually one of the little ones who would try to get me to sit with them."
  "I think I like this change, though. I find myself looking forward to his conversations like I do with Dr. Kronauer. Maybe it's because he's an adult too."

  a "Sleep okay?"
  p "Yep."

  "He winks at me and I try not to roll my eyes as I smile. We chatter about the meaty scramble for breakfast and about what kind of trouble the kids might try to get into today."
  "I tell him about how Dr. Moore asked me to help him in the clinic."

  p confused "Huh. That's neat, but you're always working and helping. Don't you need time for yourself?"
  a nervous "That's what Dr. Kronauer said, too… But busy is good, it's nice to learn new things."
  p happy "Yeah, I get that."

  "He finishes up his plate that had been piled high."

  a happy "What are you doing today? More pictures?"
  p "No, but I guess that will start to be daily soon. They said that today I got a day off."
  a "Ha, lucky."
  p "You go help out with Dr. Moore. If you collapse from exhaustion, you know where to find me."

  "I grin. Pumpkin seems to like teasing, too."

  hide pumpkin
  with dissolve
  scene bg hallway1
  with dissolve
  pause (2)
  scene bg clinic
  with dissolve
  show steven sad
  with dissolve
  
  play music musicsteven loop

  "When I get to the clinic though, Dr. Moore looks upset."

  a nervous "What's wrong?"
  s "Oh- good morning, Addison."

  "He shuffles some papers around idly, clearly ignoring my question, or at least mulling it over."
  "I try to go straight to tidying the shelves, but Dr. Moore spooks me."

  s "It's Ainsley. She was supposed to come in to get her shot yesterday- it's a vaccine she's due for- but she didn't come in. I think she's scared."
  a thinking "Scared of you?"
  s sad smile "I am new, after all."
  a "Hmm."
  s "Can you help me find her? I tried looking for her yesterday but I couldn't find her anywhere. I worry that she's hiding from me. If you were there, she may feel more safe."
  a "Oh, yeah. I can do that."

  "That seems to calm Dr. Moore down."

  s neutral "Thank you, Addison."
  
  scene bg playroom2
  show steven neutral
  with dissolve
  $ persistent.bg_playroom2=True
  pause (2)
  
#hide-and-seek minigame for finding Ainsley
  scene bg hideandseakclosed
  a confused "Ainsley, it's okay to come out."
  show steven sad
  s "Ainsley? Are you in here?"
  hide steven with dissolve
  #start game
  $ minigame_hs=Hide_seek(5)
  $ minigame_hs.InitGame("bg playroom2", 0.0, (0, 408), "hs1",(285,408),"hs2",(603,508),"hs3",(1166,616),"hs4",(1602,740),"hs5")
  $ minigame_hs.GameAsBG()
  window hide
  $ minigame_hs.StartGame()
  $ minigame_hs.GameAsBG()
  hide screen hs_minigame with dissolve
  jump hs_end
label hs_diag0:
  a "Where could she be?"
  return
label hs_diag1:
  #open one spot
  a "Not there..."
  return
label hs_diag2:
  #open 2nd spot
  a "Not there either..."
  show steven neutral
  with dissolve
  show lukas confused
  with easeinright
  l "Addy? What are you- oh, Ste-" 
  "Dr. Kronauer's gaze seems stuck on Dr. Moore. I look between them."
  a "We're trying to find Ainsley. She won't take her medicine."
  s angry "Mh."
  l "Oh. I can help if you-"
  s "We're fine, thanks."
  hide steven
  hide lukas
  with dissolve
  a "Let's keep looking"
  return
label hs_diag3:
  #open 3rd spot
  a "Aisnley? Where are you?"
  return
label hs_diag4:
  #open fourth spot
  a "It's okay to come out."
  return
label hs_diag5:
  #open 5th spot
  s "Aha- there you are, Ainsley."
  return
#hide and seek minigame ends
label hs_end:
  scene bg hideandseakopen
  show steven neutral
  show lukas confused
  with dissolve
  
  l happy "You found her!"
  s sad smile "Yep, but now you have to come out."
  g "I don't wanna."
  a sad smile "It's okay, Ainsley. Come on, I promise it won't be that bad."
  g "Mhhhh. No."
  a "Ainsley…"
  s "It's okay. Let me talk to her."
  a thinking "Oh, okay."

  "Dr. Moore kneels in front of the cabinet and speaks quietly to Ainsley. I've never seen him this soft before."
  "I always see him frowning, and though I know he has a good smile and he doesn't mean any harm, Ainsley is probably afraid of his scary expression in the first place."
  "Right now though, he smiles and keeps his hands on his lap, talking quietly to have her come out on her own terms."
  "I'm not so sure it will work though."

  s "I can make it worth your time, too. You know I have some candy in the clinic, and you can have some. I'm not mad at you, Ainsley..."

  "Dr. Kroanuer and I watch as Ainsley peeks her head out from the cabinet."

  show ainsley sad
  with dissolve
  g "Really?"
  s happy "Really."

  "She comes out from her hiding spot and nervously glances around before taking hold of Dr. Moore's sleeve."

  s sad smile "Hah, it's okay, Ainsley. I told you, you're not in trouble."
  g "Yeah…"
  s "Okay…"

  "I take a step back as Dr. Moore stands up, taking hold of Ainsley and lifting her up to set on his shoulders."
  
  hide steven
  hide lukas
  hide ainsley
  $ config.side_image_tag = "alfa"
  show piggyback onlayer event
  with dissolve

  g "Ahh!"
  s "How about this?"
  g "Yay!"
  l "You're good at this."
  s "I am a pediatrician."

  "Dr. Moore walks off calmly with Ainsley on his shoulders."
  
  hide piggyback onlayer event
  with dissolve
  $ config.side_image_tag = None
  show steven happy
  show ainsley happy
  
  hide steven
  hide ainsley
  with easeoutleft
  
  show lukas confused
  with dissolve
  hide lukas
  with easeoutright
  show bg hallway1
  with dissolve

  "I have to hurry to catch up with them."

  scene bg clinic
  show steven happy
  show ainsley happy
  with dissolve

  s "There you go, and now you can have some candy."
  g "Yay!!"
  a happy "All done already?"
  s "Mhm. She's very good at getting her shot now that she knows she's a good girl."
  g "Yep!"
  a "-giggle-"

  "I turn around and go back to the paperwork I was going to organize for Dr. Moore today. He wanted certain pages pulled out of files, photocopied, and to be put back in."
  "I expected Ainsley to run back to the playroom, but she sticks around and holds onto Dr. Moore's pant leg as he works, and with her eyes wide she asks a lot of questions."
  "Reminds me a bit of myself, I guess."

  g "What's that?"
  g "What's this?"
  g "What does that do?"
  g "How's that work?"

  "Dr. Moore just explains everything to her."
  "I think I'm also learning while he does it too."

  play sound knock

  a "Hm?"

  show lukas neutral at left
  with easeinleft

  l "Hey- everything turn out alright?"
  s neutral "Yes."
  a "Yeah, she got her shot just fine. Now she's having fun."
  g "Yeah! I like Dr. Moore!"
  l happy "That's good!"
  s "Is there a reason why you're here?"
  l neutral "Ah, just wanted to make sure everything was okay- see if you needed some help."
  s "I'm fine. I have Addison to help me."
  l "Oh, well, let's all have lunch together then."
  a "Sure!"
  s "I'm busy right now."
  l sad smile "Oh, okay."

  "Dr. Kronauer glances at me."

  l "You want to stay and help him out, then?"
  a sad smile "Ah, yeah. I should."
  l "Okay."

  hide lukas
  with easeoutleft

  "I didn't realize Dr. Moore was busy… He even lets Ainsley keep tugging at his leg and asking questions."
  "I keep to my paper sorting until the bell for the kids' lunch rings."

  a "Ainsley, you need to go eat now."
  g "Nooooo. I wanna stay here."
  a "Come on. We'll go together, how's that?"
  g sad "Nooo. I wanna stay here with Dr. Moore."

  "Already? I thought this morning she was afraid of him."

  a "You'll get hungry."
  s happy "He's right. You should go eat, I'll be right here when you're done."
  g "Mhhh... Okay."

  hide steven
  scene bg hallway1
  with dissolve
  pause (2)
  scene bg cafeteria 
  with dissolve
  pause (2)
  hide ainsley
  with dissolve

  "Ainsley runs off to the other young children once we get to lunch. Once she picks someone, it's hard to get her off. I worry that parting her and Dr. Moore is going to be like trying to part her and Charlie." 
  "That's fine though, because Pumpkin is grabbing me by the arm as soon as he sees me."
  
  play music musicsecretspace loop

  show pumpkin neutral
  with easeinright

  p "Addy!"
  a surprised "Huh? What? Pumpkin-"
  p "Come sit with me some more."
  a "Okay?"

  "He doesn't let go the whole way, and even as we sit down he fidgets with his tail and fork."
  
#this should be changed depending on choices from day 3
if test == False:
  p excited "Uh, guess what! I passed the test!"
  a happy "See? I knew you would be fine."
  p nervous "Yeah..."
  "Oh no... Is he upset about that?"
  a thinking "What's wrong?"
  p "Oh... it's just that today they're going to do more, it'll be different."
  a "Different?"
  jump continueday5

if test == True:
  a thinking "You okay?"
  p "Yeah. Hey- you should come with me to my pictures again."
  a "? How come? Are you okay?"
  
label continueday5:

  "He shifts in his seat, sitting on his hands."

  p "Yeah, it's just this time there's going to be more than just kissing."
  a "?"
  p "We're going to have sex."
  a "? You and your fake Master?"
  p "Yeah. At least, I hope so."
  a "You hope you'll have sex?"
  p "I hope it's one I've already met."
  a "Oh."

  "He kicks his legs."

  p "So I wanted you to come with me."
  a "Oh…"
  "You want me to watch?"
  p laugh "Haha. That's not what I meant- I mean- I feel better when you're around, you know?"

  "He's blushing so hard. Of course, it's probably really embarrassing for him to ask me this .."

  a "Yeah. I can be there for you. Don't worry, I'll come with."
  p happy "Okay. Thank you Addy."

  "We finished up our lunch and we went out. Pumpkin gently wraps his fingers around mine. His hand is gentle and nothing like his usual grip. I squeeze it softly to reassure him."

  scene bg hallway1
  show pumpkin happy
  with dissolve
  pause (2)
  scene bg filmset2
  show pumpkin happy
  with dissolve

  p excited "Pumpkins!!!"
  
  play music musicupbeat loop

  "The room has been dressed up in black and orange with stuffed pumpkins and warm comfy blankets over a large bed that has been set on the stage."
  "Pumpkin is intercepted on his way up there by a woman who immediately starts to fuss over his face"

  o "Pumpkin, come here. We need to get you set up."

  a happy "..."
  
  "It's nice to see him in his makeup again. While he's doing that, I scan over the stage and cameras, wandering around the room and finding a seat between some equipment. It's where Pumpkin and I will be able to see each other clearly."
  "I kick my legs out in front of myself and wait."

  play sound ding
  
  menu:
   "Continue":
    "Sorry, that's not ready yet."
    jump skippumpkinshoot
   "Skip":
    jump skippumpkinshoot
    
#missing a scene here

label skippumpkinshoot:

  play music musicsleepy loop

  "Once he's all dressed and the makeup was wiped off, he pads over to me and rubs his eyes."

  a "Are we going to…?"
  "He shook his head."
  p "No. I have a room to myself now. You should know where it is. I'll show you."
  a surprised "Oh!"

  scene bg hallway1
  show pumpkin happy
  with dissolve

  "We walked a little while in silence, Pumpkin leaning against me the whole way. He must be awfully tired."

  p "Here."
  a "Oh, okay. That's not too far from my room."
  p "Mmhm."

  "He lifts himself up off of me and rubs his eyes."

  p "Um, I think I'm going to go straight to sleep. Sorry."
  a "Huh? No- that's okay. You should get some rest."
  p "Yeah. Um. I'll see you later."

  hide pumpkin
  with easeoutright

  "..."

  scene bg bedroomlight
  with dissolve
  pause (1)
  
  cards open card6
  
  scene bg bedroomdark
  with dissolve

  "Ah, goodnight then."

#Day 6
  calendar day 6
  scene bg bedroomlight
  with fade

  a pajamas sleepy "..."
  a sleepy "Morning."
  "I get ready slow. It's not that my hair is tangled or that I'm cold and want to stay in bed."
  "I just have a feeling I don't want to get up."

  scene bg hallway1
  with dissolve

  "Last night Pumpkin was acting strange when he went to bed. Maybe he'll be okay this morning."

  scene bg cafeteria
  with dissolve

  "..."
  "No Pumpkin? Where could he be?"
  "He can't be working already, can he? This early?"
  "I try and act like nothing is strange as a few kids drag me over to their table. I let myself laugh and smile for them."
  "I shouldn't be too worried. He was so tired last night, that's all. In fact, he's probably just sleeping in late."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg clinic
  with dissolve
  
  play music musicsteven loop

  show steven neutral
  show ainsley happy
  with dissolve
  
  "I skip the line and go straight into Dr. Moore's office."
  
  s happy "Good monring, Addison."
  a happy "Good morning! Do you still want my help with Drug Day?"
  s thinking "Mmhm. That would be nice. Can you set up more of the diazapine on the counter, and make sure everyone gets a sticker as they leave."
  a laugh "Okay!"
  s happy "Perfect."
  
  "The morning goes by pretty well, everyone getting their shots without complaint. All of the kittens are excited for their stickers and eagerly snatch them up."
  "I'm curious because Pumpkin doesn't come in. He must be busy today too... He can get a make-up shot later, but I still wonder what he's doing."
  "Once everyone is done I put away all the supplies and tie up the big garbage bag full of needle wrappers."
  
  show ainsley happy
  with dissolve

  a surprised "Ainsley? What are you doing here?"
  
  "It's as if she came out of nowhere."
  
  s happy "She wanted to help out today."
  g "I'll be like big brother and stay here with Dr. Moore."
  a happy "Oh… Okay."
  
  "She missed all the time she could have been helping earlier this morning..."
  "And actually- she's still too young to really help with anything."
  
  a confused "It's lunch time though."
  g "I'll help after lunch!"
  s "I'm trying to tell her that she still has to go to class though."
  a sad "Ainsley. You can't skip classes."
  g "Dr. Moore can teach me!"
  a "He has some important work to do!"
  g sad "He can teach me."
  a sad "Ainsley…"

  "She sits on the floor, defiantly crossing her arms."

  g "No."
  a "Ainsley, how are you going to get adopted if you act like that?"
  g "Dr. Moore will adopt me."
  s thinking "?"
  a "Ainsley…"
  s "If you go to class, you can always come back after and I'll help you with your practice sheets."
  g "Mmnn…. No."

  play sound knock
  show jesse neutral
  with easeinleft

  j "There you are."

  "Now she's really in trouble."

  j "Is she alright? What are you doing here, Ainsley?"
  s "She's fine. She's just throwing a fit."
  j "You can't keep her here."
  s "I wasn't trying to."
  j "Come on, Ainsley."
  g "No!"

  "Again, she huffs and puffs, but Mr. Jesse only picks her up by her sides and starts carrying her out the door."

  g "Let me go!"
  a "Ah…"

  hide jesse
  hide ainsley
  with easeoutleft

  a "Oh boy…"
  s smile "Well, that's one way to do it…"

  "Dr. Moore has me go through more paperwork in files. He says he likes to use the paper files more than the computer, and so having me sort them out is a big help."
  "It takes a long time to do them one by one, and the paper smells like dust and makes my nose itch."
  "I'm glad I can help, though."

  a "Okay, I'm going to go to lunch now."
  s "Alright, I'll see you soon Addison."

  "He doesn't look up from his desk."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg officespace
  with dissolve

  "I'm still pretty tired… not exactly sleepy, but today has been a bit of a daze already. I find myself looking forward to seeing Dr. Kronauer for lunch. He may have something to talk about, or at the very least just let me rest against him and pet me…"

  scene bg lukasoffice
  with dissolve
  show lukas happy
  with dissolve
  
  play music musiclukas loop

  l "Hey Addy."
  a "Hello."

  "I wrap my arms around his neck before he can stand up from his desk. Letting my eyes close I just lean against him."

  l "You alright, bud?"
  a "Mmhm."

  "He's always so concerned about me. It feels nice. Whenever I try and worry about him, he gets embarrassed. I smile a little into his hair as I rest, my arms are still around him."

label day6sex:

  "He always gets so red when it isn't all about me. But sometimes it just can't be helped, I want to take that whole cock into my mouth... I want to feel it on the back of my throat, run my tongue up and around the head..."
  "Oh, I'm day dreaming again."

  l "Addy?"
  a "Huh? Oh, sorry. I was just thinking."
  l confused "Hm?"

  "He turns around in his chair to face me, head in a cute tilt."

  l "Are you okay? Are you in heat?"
  a "No, I'm fine."
  l "Are you feeling sick?"
  a "No-"
  l "You're not lying to me?"
  a "No! I'm fine, I-"

  play sound ding

  menu:
    "Skip":
      jump skiporalday6
    "Continue":
     jump continueoralday6

label continueoralday6:

  "I don't think I could explain it to him with words, so instead I drop to my knees, pushing between his legs. His office chair rolls slightly, but I have a grip on his leg. He spreads them instinctively, but when I look up he has his cute blush."

  l blush "Oh."
  a "Is this okay?"
  l "Yes..."

  "I paw at his pants, pushing the fabric out of my way as soon as I can undo the button. His hand falls in my hair, stroking."

  l "What's gotten into you?"
  a "I just want to suck you."
  l "Oh. Is that all?"

  "It's cute he doesn't know what to do with that."
  "I pull his cock out, handling it gently. While I fondle him I press small kisses against him, running my fingertips along his balls with a firm pressure."
  "I can't last all that long before wrapping my lips around him."
  
  hide lukas
  $ config.side_image_tag = "alfa"

  show lukasblow1 onlayer event
  with dissolve

  l "Oh..."

  "Feeling his warmth, how I can make him tremble before even getting him hard all the way... It makes me feel sort of powerful."
  "My cheeks cave in as I suck on him, waiting to feel him harden in my mouth."

  l "Mmmhh..."

  "He likes it. His hand in my hair is slow and lazy. I don't know what it is about his fingers on my scalp, but it makes me shiver happily."
  "I can feel his pulse on my tongue. He's getting bigger, filling up my mouth,"

  show lukasblow2 onlayer event
  hide lukasblow1 onlayer event
  with dissolve

  "Pressing against the back of my tongue. The fullness is letting me know he wants me."

  l "Addy..."

  "Or he can be more direct, like calling my name, gripping my hair, and pulling me closer. I do my best not to choke."

  a "Mmmh."

  "The satisfaction of it all makes it hard for me to stall the best move I have."
  "Dr. Kronauer really needs me and he really wants me around. He loves me and holds me close and that's more than enough to tip me over the edge here."

  a "-purrrr-"
  l "Ah- ahh!"

  "The vibrations come from the back of my throat. I can feel them through my whole body, and I'm sure Dr. Kronauer can feel them through his tip, then his entire dick. I rub his balls slowly, feeling it there as well. I don't need a vibrator when I can do this for Dr. Kronauer all by myself."

  l "Addy..."

  "I feel him buck up into me, hand firm on the back of my head. There's nowhere for me to go and there's no room for his dick to go further so I ended up gagging."

  a "Mhh!"
  l "S-Sorry."

  "I tell him I accept his apology by continuing to purr."

  a "-purr purrr-"
  l "Ohhh..."

  "I can't smile with his cock in my mouth. He should be done soon, I can tell. The way his hips tremble and he continues to try and push into me. Even his dick is twitching against the motion of my tongue. I hollow out my cheeks again to help him along. His precum is tart in my mouth."

  l "Addy, I..."
  a "Mmhmm, -puurrrr-"
  l "Ohhh...."

  "Just a little more..."

  l "Ah, ah- ah!"
  
  show white with flash
  hide white
  pause (.5)
  show white with flash
  hide white
  pause (.5)
  show white with longflash
  hide white

  "As I feel him swelling with come I pull back purposefully, his grip having weakend. My mouth comes off with a 'pop' and immediately I can feel his warm milk on my lips and face."

  hide lukasblow2 onlayer event
  with dissolve
  $ config.side_image_tag = None
  show lukas blush
  show addison happy

  l "Addy..."

  "He hasn't opened his eyes. I can only grin as I look up at him."

  l "Mh- Addy. You did that on purpose."

  "I grin. I did. But his dick is still twitching, so it already did its job. I lean in and suck his head one last time to taste the last of his milk."

  l "Ah-"

  "Pulling back I start wiping the rest off my face."

  l "Do you like it on your face? Why would you do that?"

  "I lick my fingers and he turns redder."

  l "You're just trying to get me hard again."
  a "Maybe."
  l "Addy. -sigh- Lunch time's over. You know the rules."
  a "Aww."

  "I'm kidding, I'm not that upset over it, but my teasing isn't done yet. He fumbles with his pants, putting himself away and zipping back up."

label skiporalday6:

  l "I'm sorry, but I have to get back to work."
  a "Maybe next time then."

  "I stand, but he grabs my arm to pull me back down to his level, stealing a kiss."

  l "Next time."
  a happy "Okay."

  hide lukas
  with dissolve 
  scene bg hallway1
  with dissolve
  pause (2)
  scene bg clinic
  with dissolve
  show steven happy
  show ainsley happy
  with dissolve
  
  play music musicsteven loop

  "I get back to the clinic to finish helping. I'm not sure what I expected to find, but it probably should have been this."

  s laugh "No, Ainsley. You have to go to class."
  g "But I can help here, like Addy."
  g excited "Right Addy? I can help!"
  a thinking "Yes, but you still have to go to class. You can help when class is over."
  s happy "Mhm."
  g sad "Addyyyy. But I wanna stay here and help like you do every day!"
  a happy "That's because you're a good girl, you want to help. But good girls still have to take classes."
  g "-pout-"
  a neutral "You already got in trouble this morning. Do you really want to get in trouble again? You have to go to class tomorrow."
  g "Fine. But I'm going to get my practice sheets."

  hide ainsley
  with easeoutright

  "She stomps out of the room. When the door closes Dr. Moore takes his hand away from his face, letting his chuckling spill out."

  s laugh "Oh, I'm sorry Addison. Thank you for helping."
  a "What did she do?"
  s "Nothing, she's just so stubborn. Something about it was just-"

  "He keeps chuckling."

  s "It was just really cute."
  a laugh "They're like that."

  "It's really nice to see him smiling, let alone laughing like this."

  a "Can I help you with anything though?"
  s "No, not right now. Thank you, you did so much already."
  a "Mm. Alright, have a good night, then."

  hide steven 
  with dissolve
  scene bg hallway1
  with dissolve
  
  play music musicneutral loop

  "I haven't been doing my rounds enough lately, so I wander upstairs to check on the rest of the staff."

  scene bg officespace
  with dissolve

  "It's a little boring, but maybe a little boring is what I need right now."
  "To let my head clear ais to enjoy the feeling of someone petting my hair."
  "It's a nice reminder that nothing is as worrisome as it may seem."
  "Before I know it, I've happily wasted a few hours. The staff are packing up to go home."
  "I yawn and pad back down the stairs."
  
  play music musicsleepy loop

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg bedroomlight
  with dissolve

  "Goodnight."

  scene bg bedroomdark
  with dissolve 
  pause (1)
  
  cards open card7
  
  scene bg bedroomlight 
  with fade
  jump day7
