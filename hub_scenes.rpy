
####################
##Lily's Hub Scene##
####################

label hub_sis:
    menu:
        "Ask her to visit the beach with you." if sisO.slut_score > 20 and beach_girl is None and beach_unlocked:
            if sisO.beach_count == 0:
                me "I wanted to see if you wanted to schedule another trip to the beach. Since I wasn't able to take you before."
                "Lily smiles and claps."
                sis "Yes! Ah, thank you [inputName]! I'll dig out my bathing suit for Saturday!"
                $ beach_girl = "Lily"
                me "Great, see you then."
            else:
                me "I wanted to see if you wanted to take another trip to the beach. What do you say?"
                sis "Sure, sounds like fun!"
                $ beach_girl = "Lily"
                me "Great, see you on Saturday."
            return False

        "Cancel your trip to the beach." if beach_girl == "Lily":
            me "Hey Lily. I've got some plans that came up, so I've got to cancel our plans on Saturday."
            sis "Oh, okay. If change your mind just let me know."
            $ beach_girl = None
            return False

        "Talk to her about her birth control." if sisO.slut_score > 100 or (sisO.slut_score > 70 and sisO.cumslut):
            if sisO.bc:
                me "Hey Lily, I wanted to ask you something. You're on the pill, right?"
                if sisO.cumslut and sisO.freeuse and not sisO.anal:
                    sis "Yeah, I pretty much have to be or I'd get pregnant in a heart beat. I know I really shouldn't, but feeling a guy cum in me raw is just so much nicer."
                else:
                    sis "Right now? Yeah, I'm trying to be pretty careful about it."
                menu:
                    "Tell her to stop taking her birth control pills.":
                        $ sisO.bc = False
                        me "I want you to stop taking in from now on, okay?"
                        if sisO.cumslut:
                            sis "Oh, I can do that if you want. You'll have to be careful about cumming inside me, unless you're planning to get your sister pregnant."
                            "She bites her lip and winks at you."
                            me "I just know it feels so much better when there's a little bit of risk."

                        else:
                            sis "If you really want me to, I can do that. Just be a little careful you don't end up getting me pregnant, okay?"
                            me "Of course, I promise I'll pull out every time. I just like the risk of it, it's super sexy."

                        sis "So is that all?"
                        me "Yeah, that's all. I'll talk to you later Lily."

                    "Don't do anything about her birth control.":
                        me "That's probably for the best, I wouldn't want you getting pregnant somehow. Just keep it up, I suppose."
                        sis "Sure. Anything else?"
                        me "No, that's all. I'll talk to you later."

                "You step back out of her room and close the door behind you."
            else:
                me "Hey Lily, I wanted to talk about your birth control. You haven't been taking the pill lately, right?"
                sis "Not since you told me to stop. Is something wrong?"
                menu:
                    "Tell her to start taking her birth control pills again.":
                        $ sisO.bc = True
                        me "No, nothing's wrong. I just think you should start taking them again."
                        if sisO.cumslut:
                            sis "Are you sure? I kind of liked the risk when you came in me. Just thinking about it gets me a little excited."
                            me "Yeah, I'm sure. I don't want you to end up getting pregnant."
                        else:
                            sis "Oh, okay. I guess I want to make sure I don't end up pregnant."
                            me "Yeah, exactly."
                        sis "Is that everything you wanted to talk about?"
                        me "Yeah, that's everything. I'll see you around."

                    "Don't do anything about her birth control.":
                        me "No, nothing's wrong. I just wanted to make sure you hadn't started taking them or something."
                        sis "Of course not, I would have asked you first [inputName] to see what you thought. Is that all?"
                        me "Yeah, that's everything. I'll talk to you later."

                "You step back out of her room and close the door behind you."
            return False

        "Ask her to strip for you." if sisO.slut_score > 20:
            #Strips down for you, lets you have her put on different outfits at higher influence
            me "Not much, I was just bored so I thought I'd come in and see what you were up to."
            "You step into the room and close the door behind you."
            sis "Well, I'm not really doing anything either. Just relaxing I guess."
            me "How about we spend some time together then? Work's been stressful lately and I could use a little relaxation."
            sis "Okay, sure. I'l help if I can."
            "You sit on the bed beside Lily."
            me "Good. Take off your dress for me then, I want to take a good look at you."
            "Lily nods, stands up, and moves a few steps in front of you."
            show sis strip1 at right
            "She pulls the straps of her dress over her shoulders and lets it fall to the ground, then steps out and kicks it to the side of the room."
            sis "Like this?"
            me "Perfect Lily. Turn around and bend over for me a little."
            show sis strip5 at right
            "Lily does what you want, turning around and planting her hands on the far wall with her legs spread."
            if sisO.slut_score > 30:
                me "That's great. You're a great little sister for doing this Lily."
                "Lily shakes her butt at you a little."
                sis "Would you like me to take everything off?"
                me "Yes I would Lily. Slips those panties off for me."
                show sis strip2 at right
                "Lily turns back to you and pulls her underwear down in one quick motion. She kicks them into the pile with her dress."
                menu:
                    "Turn around again.":
                        show sis strip6 at right
                        "Lily nods and turns around. She puts her hands back on the wall and shakes her ass for you, then takes one hand and gives it a good spank. The hit sends her ass cheeks jiggling for a few moments."
                        sis "Like that?"
                        me "Just like that. You look amazing Lily, very hot."
                        "She smiles and turns back to the wall with her legs spread, letting you look at her for a long while."
                        "Eventually she puts her legs back together and turns around."
                        sis "I hope you had fun. I think that's all for today though."
                    "Touch yourself.":
                        sis "Okay. Like this?"
                        "She spreads her pussy lips with one hand and runs a finger along it's length."
                        me "That's nice. Now slip a finger inside."
                        show sis mast6 at right
                        "Lily's obviously wet, and she has no trouble slipping one then two fingers inside herself. Her other runs down the outside of her thigh."
                        me "Do you like touching yourself like that?"
                        "Lily hesitates, then nods yes."
                        sis "It just feels so good."
                        "She moans softly and rubs her clit a little bit."
                        me "Good, you should enjoy it. You look very hot when you're touching yourself like this."
                        "She slides her fingers out of her pussy and smiles at you."
                        sis "Thanks. I think that's all for today though."

                if sisO.slut_score > 50:
                    sis "[inputName], I've got some more stuff to show off if you'd like to see it."
                    me "I think I would Lily. Tell me what you'd like to show me."
                    menu: ##Might have to make the girl object aware of what outfit they're wearing.
                        #TODO add more outfits. Do this with every girl eventually.
                        "Black Lingerie.":
                            "Lily pulls out some thin black lace lingerie. She slips it on, then poses a little for you."
                            show sis nightstrip3 at right
                            "First she shows off the front."
                            show sis nightstrip4 at right
                            "Then the back."
                            show sis nightstrip5 at right
                            sis "Like it?"
                            me "Ya, you look amazing in it."
                            "Lily smiles and blushes a little."

                        "White Lingerie.":
                            "Lily pulls out some white lace lingerie, something someone might wear on their wedding day underneath their dress."
                            "She slips it on, then poses for you."
                            show sis nightstrip6 at right
                            "First she shows off the front."
                            show sis nightstrip8 at right
                            "Then the back."
                            sis "I feel so nice in this, so pure."
                            me "But we both know that isn't true."
                            "Lily smiles and blushes a little."
                        "Finish up.":
                            "You decide you don't want to see Lily in any of her other outfits right now."

                    me "Okay Lily, I think that's enough for now. I've got some other stuff to take care of today."
                    "Lily nods and starts to put her normal clothes back on for now."
                    sis "That was fun. If you ever want me to show off for you, just let me know."
                    me "Will do."
                else:
                    show sis strip2 at right
                    me "Thanks for the show Lily, I enjoyed it."
                    sis "No problem, it was fun."
                    "Lily smiles at you as you stand up and head out of her room."
            else:
                me "That's great. Just what I wanted to see."
                "You spend a few more moments enjoying Lily's ass."
                me "Okay, that's enough for now. Thanks Sis."
                show sis strip1 at right
                "Lily turns around and smiles at you."
                sis "I'm glad I could help."
                "You stand up to leave. Lily sits back down on her bed and grabs her phone, still just wearing her panties."
            $ sisO.inc_naked()
            $ sis_hub.inc_level(1)
            $ sisO.change_resist(-sis_hub.use_red(1,sisO.resist_score))

        "Get a handjob." if sisO.slut_score > 35:
            #Jerks you off, lets you finish different places with higher influence
            me "Well, I was just feeling a little stressed out and thought you could help me take care of it."
            "You walk over and sit on Lily's bed beside her. Lily puts her phone down and looks at you."
            sis "How could I help?"
            "You undo your pants and slide them down past your cock."
            me "Like this, just stroke me off a little bit."
            show sis hand1 at right
            "Lily nods and reaches over. She holds your shaft gently and starts to slide her hand up and down."
            $ sisO.inc_hand()
            sis "How's that?"
            me "It feels great. Thanks."
            "She smiles and turns her full attention to stroking you off."
            if sisO.slut_score > 45:
                "After a while of enjoying Lily's handjob, you speak up again."
                me "I want you to take your dress off for me Lily, and get on the ground while you rub me."
                "Lily nods, lets go of your shaft, and stands up. She slides the straps of her dress off her shoulders and lets it fall to the ground, then kneels in front of you."
                show sis hand2 at right
                "She takes your cock up in both hands, rubbing the tip with her thumb as she strokes you off."
                sis "How does that feel? Am I doing this right?"
                me "You're doing great sis. Just keep going."
                "You watch Lily work her hands up and down your dick for a few minutes. Her nipples are starting to harden up, and she seems to be enjoying herself."
                "It doesn't take much more for your sister to drive you to the edge of an orgasm."
                menu:
                    "Cum on her tits.":
                        me "Just like that Lily. I'm going to cum soon."
                        "Lily looks up and smiles, then speeds up her handjob."
                        sis "Good, give me everything you can!"
                        show sis hand3 at right
                        "You tense up as you begin cumming. You fire your load onto Lily's tits, landing the first pulse on her upper chest and working your way down."
                        if sisO.cumslut:
                            "Lily leans forward a little to catch it all. Once you're all done she runs a finger through your semen, bringing her finger to her lips to lick it clean after."
                        else:
                            "Lily leans forward a little to catch it all, and wipes the last few drops off on a nipple."
                        $ sisO.inc_cum_over()
                        sis "Wow. Was it good?"
                        me "It was great Lily."
                        "You stand and pull your pants up."
                        me "Now you should get yourself cleaned up. You don't want mom seeing what a slut you are."
                        "Lily pouts and looks like she's about to say something, but stops and just nods instead."
                        "You head out of her room whlie she looks for something to wipe your cum off with."
                    "Cum on her face." if sisO.slut_score > 60 or sisO.cumslut:
                        me "Keep going Lily. Spray my cum all over your face like a good slut."
                        "Lily looks up at you and pouts, but nods and keeps stroking you off."
                        show sis hand4 at right
                        "You tense up and begin to cum. Lily gasps as your first blast of semen lands on her forehead, but she keeps rubbing your cock. When you're finished you've covered her face from top to bottom."
                        "She lets go of you carefully and wipes some of your cum away from an eye."
                        $ sisO.inc_cum_over()
                        if sisO.cumslut:
                            sis "Wow, thanks for the load [inputName]. How was it for you?"
                        else:
                            sis "How was that?"
                        me "It was great Lily. You look perfect covered in my cum, but you might want to get it cleaned up before mom sees you like this."
                        "Lily nods and starts to search around for something to clean herself off with. You pull up your pants and head out of her room."
                    "Cum in her mouth." if sisO.slut_score > 75 or sisO.cumslut:
                        "You reach forward and put a hand on the back of Lily's head."
                        me "I'm almost there, put me in your mouth."
                        "Lily looks up at you like she's going to say something, but is cut short when you press the tip of your cock against her lips."
                        show sis hand5 at right
                        sis "She opens her mouth and you're able to slip yourself inside right before you cum."
                        if sisO.slut_score > 85 or sisO.cumslut:
                            menu:
                                "Cum down her throat.":
                                    "As you start to tense up, you use your hand on the back of Lily's head to pull her down farther on your cock."
                                    "You do your best to hold your orgasm back until your tip has slid over her tongue and all the way to the back of her throat."
                                    show sis hand9 at right
                                    "Lily latches onto your thigh with one hand and tries to look up at you while you hold her all the way down on your cock."
                                    me "There we go, take it all like a good cumslut!"
                                    "You relax and start to cum down her throat. Lily tries to pull back, but your firm hand keeps her held down. Her throat clenches and spasms, which only makes your orgasm more intense."
                                    "Lily coughs, blowing spit and cum bubbles around the base of your shaft. You pull back a little, then thrust back down to enjoy the feeling of Lily's tight throat some more."
                                    "When you're certain you're finished you let go of Lily's head. She pulls back quickly and gasps for air, trailing spit and cum from her mouth that drips down onto her chest."
                                    $ sisO.inc_cum_mouth()
                                    $ sisO.inc_cum_swallow()
                                    me "Wow, that was great."
                                    "Lily nods and coughs a few times while she tries to catch her breath. Finally she seems like she's recovered."
                                    if sisO.cumslut:
                                        sis "Thank you [inputName]. Your cum felt so thick in my throat, I thought it was going choke on it for a second. Did it feel good for you?"
                                    else:
                                        sis "I hope I did alright. I tried not to cough but you were just so deep."
                                    me "It felt great Lily. Your throat feel amazing when you tense up like that."
                                    sis "Okay, good."
                                    "Lily smiles weakly at you while she sits on the floor."
                                    "You stand, pull up your pants, and leave Lily's room while she's still recovering."

                                "Cum into her mouth.":
                                    "You tense up and release right inside Lily's mouth. She moans softly as your cum shoots out over her tongue, and she licks around your tip a few times make sure she gets everything."
                                    me "Perfect. Good job Lily."
                                    $ sisO.inc_cum_mouth()
                                    show sis hand7 at right
                                    "Lily pulls back and looks up. She opens up so you can admire how much cum you just let out into your sister's mouth."
                                    menu:
                                        "Tell her to swallow.":
                                            "You lean forward and place a finger on the bottom of Lily's chin, gently pushing it closed."
                                            me "There you go, drink up sis."
                                            "She closes her mouth and swallows while she keeps her eyes locked on you."
                                            me "That's a good little cum slut. Did you like your brother's load?"
                                            $ sisO.inc_cum_swallow()
                                            if sisO.cumslut:
                                                "She nods eagerly, licking her lips and sighing."
                                                me "Good girl. I'll make sure to give you plenty more in the future."
                                                sis "Thank you, you know exactly what I want."
                                            else:
                                                "She hesitates for a moment, then nods."
                                                me "Good girl. I'll make sure to give you plenty more in the future."
                                                sis "Thank you..."
                                            "You stand and pull your pants up, then leave Lily's room while she's still kneeling on the floor."

                                        "Tell her to spit it on her tits.":
                                            me "That's a good girl. Spit it out over your tits for me now."
                                            show sis hand8 at right
                                            "Lily leans back and tilts her head down, then opens her mouth and lets out a thin stream of spit mixed with your cum."
                                            "She moves her head left and right, making sure to get some of your load all along her tits. When she's done she lifts a tit up in her hand and sucks on a nipple for a moment."
                                            sis "Like that?"
                                            me "Just like that. You're a great little whore for me Lily, so eager for my cum."
                                            if sisO.cumslut:
                                                "She nods eagerly, licking her lips and sighing."
                                                me "Good girl. I'll make sure to give you plenty more in the future."
                                                sis "Thank you, you know exactly what I want."
                                            else:
                                                "She hesitates, then nods."
                                                sis "I just like helping you out, that's all. Whatever makes you feel good."
                                                me "Well I'm sure there will be plenty of opportunities for you to make me feel good in the future."
                                            "You stand and pull your pants up, then leave Lily's room while she's still kneeling on the floor covered in cum."

                        else:
                            "You tense up and release right inside Lily's mouth. You can hear her gasp a little as the first pulse lands on the back of her tongue, but she doesn't try to pull away."
                            "With your hand on the back of her head you move in and out of her mouth a few times until you're completely finished cumming."
                            $ sisO.inc_cum_mouth()
                            show sis hand6 at right
                            "You pull out of her mouth and lean back to catch your breath. Lily tilts her head forward and spits your load out into her hands, then takes a deep breath."
                            sis "How was that?"
                            me "Good job Lily, that was great."
                            "Lily smiles proudly while holding a handful of your cum."
                            "You stand and pull up your pants and head out of her room while she starts to get cleaned up."
            else:
                "You lean back and enjoy. After a few minutes Lily's gotten you close to finishing."
                me "Keep going Lily. Don't stop."
                "Lily nods and strokes you faster. You orgasm and start to fire your load onto the floor."
                "Lily slows down, then stops and lets go of your cock."
                sis "There we go, all done."
                show sis casual1 at right
                "You stand and pull your pants back up."
                me "Thanks sis. You'll probably want to get that cleaned up before mom sees."
                "She nods and starts to look around for something to wipe up your mess as you leave the room."
            $ sis_hub.inc_level(2)
            $ sisO.change_resist(-sis_hub.use_red(2,sisO.resist_score))

        "Titfuck her." if sisO.slut_score > 50:
            #Lets you finish different places with higher influence, take more control.
            me "Well I was feeling little stressed out and I thought you would like to help me out."
            "You stand in front of Lily on the bed and pull your pants down past your waist to free your cock."
            "Lily looks at your crotch for a moment, then nods and reaches towards it with one hand."
            sis "If you really need it that badly, I'll do what I can."
            me "Wait. I want you to use your tits."
            sis "Oh, okay. I can do that."
            "She slips her arms up and out of the top of her dress and pulls it down and off, then slides off the bed onto her knees."
            show sis tit1 at right
            "Lily holds one tit in each hand and presses them on either side of your cock, then starts to slide them up and down along your shaft."
            $ sisO.inc_tit()
            me "Oh ya, just like that."
            sis "Good, I'm glad you like it."
            "For a few minutes you're both silent while you enjoy the feeling of Lily's soft warm breasts as she services you."
            menu:
                "Let her keep going.":
                    "It isn't much longer before you feel your orgasm start to build."
                    me "Keep up the good work sis, I'm almost there."
                    sis "Okay, I'll do my best."
                    "Lily speeds up her strokes, panting softly as she exerts herself. Your precum has dripped down your shaft, and made the slot between her tits wet and slippery."
                    show sis tit2 at right
                    "Finally she drives you over the edge and you tense up. You fire the first blast of cum up into her chin, then pulse the rest out over the top and in between her tits."
                    $ sisO.inc_cum_over()
                    "Lily holds you between her breasts until she's sure you're done, then spreads them open and pulls back."
                    sis "Wow, that was a lot."
                    me "It's because you did such a great job taking care of me."
                    sis "Oh. Good then."
                    if sisO.cumslut:
                        "She runs a hand under her boobs to catch a line of cum that was dripping dow. She licks her fingers clean and sighs."
                        sis "I suppose I should get the rest of this cleaned up. It's so nice and warm though..."
                    else:
                        "She runs a hand under her boobs to wipe away a line of cum that is working its way down."
                        sis "I suppose I should get all this cleaned up."
                    "You stand and pull your pants back up."
                    me "Ya, you wouldn't want mom to see you like this."
                    "You leave Lily's room as she starts to look for something to clean herself off with."
                "Tell her to lick your cock." if sisO.slut_score > 65:
                    me "I think we could use a little lubrication Lily. See if you can lick it a little."
                    sis "Like this?"
                    show sis tit3 at right
                    "Lily tilts her head down and slides her tits to the bottom of your shaft. She opens her mouth and sticks her tongue out, running it around the tip of your penis."
                    me "Just like that. Now keep going."
                    "Lily does her best to slide her breasts up and down along you while also licking the tip at the bottom of each stroke. Before long her spit has gotten her tits wet and slippery."
                    "You enjoy watching your sister on her knees servicing you for a while, and eventually feel your orgasm start to approach."
                    menu:
                        "Cum between her tits.":
                            me "You've almost got me there Lily. Don't stop."
                            sis "Okay. Finish whenever you want."
                            "Lily pants softly as she speeds up her titfuck. Her warm breath and wet tongue feel amazing each time she slides down and licks your tip."
                            "You moan a little as you reach your climax, and Lily gasps as the first burst of cum lands just under her chin."
                            show sis tit2 at right
                            "Some of your load lands on top of her breasts, running down to form drips at her nipples, and the rest pools in between her cleavage as she slows down and stops."
                            sis "Ah, wow!"
                            $ sisO.inc_cum_over()
                            "You pull back and slip out of Lily's tits, trailing thin lines of cum for a moment. Lily keeps her breasts pressed together to keep your cum from running all the way down her front."
                            me "Good job Lily. I needed that."
                            sis "Anytime. Glad I could help."
                            me "Now you shuld get yourself cleaned up, unless you want to go around like a cum covered whore."
                            "Lily pouts and shakes her head, and starts to look around for something to clean herself up with."
                            "You stand and pull up your pants, then leave Lily's room."

                        "Cum in her mouth." if sisO.slut_score > 75 or sisO.cumslut:
                            "You wait until you're ready to finish, then place a hand on the back of Lily's head and pull her just a little farther to slip your whole tip into her mouth."
                            me "Here I come!"
                            "Lily grunts something and tries to pull away, but you hold her in place as you release your cum into her mouth."
                            "After the first burst she relaxes a little, and makes sure to keep her breasts pressed tight against the bottom of your shaft as you finish."
                            "When you've stopped cumming you feel Lily's tongue work it's way around your tip again, getting every last drop."
                            me "That's a good little cum slut. Good job."
                            show sis hand7 at right
                            "You pull out of her mouth slowly, then tilt Lily's head up with a light tough so she is looking at you."
                            "Lily opens her mouth for you to see, turning left and right so you can see it all."
                            me "Good girl. Now swallow."
                            $ sisO.inc_cum_mouth()
                            $ sisO.inc_cum_swallow()
                            "She nods and closes her mouth. You can see her throat working for a moment, then she opens up again and shows her empty mouth."
                            sis "All gone."
                            me "Well done. Now you should get cleaned up before anyone sees what a whore you've become."
                            "Lily pouts a little, but nods. You pull your pants up and head out of her room."

                "Grab her tits and fuck them yourself." if sisO.slut_score > 75:
                    "You reach down and grab Lily's tits with your own hands, brushing hers to the sides."
                    me "Here, let me take over."
                    show sis tit4 at right
                    "Lily lets her hands drop to her sides, and gasps a little as you squeeze her breasts."
                    "You start to thrust your hips back and forth, holding Lily in place while you fuck her cleavage."
                    sis "Do they feel good?"
                    me "Whats that?"
                    sis "My boobs. Do they feel good?"
                    "You press her tits together harder and give them a few fast pumps, causing Lily to moan softly."
                    me "Oh ya, they feel great."
                    sis "Ah, that's good."
                    menu:
                        "Keep going until you finish":
                            "Lily turns her head away and stays still while you pleasure yourself, moaning a little any time you squeeze down particularly hard."
                            "After a few minutes of tit fucking your sister you feel your orgasm approaching."
                            menu:
                                "Cum on her face.":
                                    me "Okay Lily, I'm almost there. Look down at it for me, okay."
                                    "Lily turns her head back and nods. She stares down at your cock while it pumps in between her tits, pushing yourself over the edge."
                                    "You squeeze down tight and push your cock out of the top of her cleavage while you cum, spraying your load over her waiting face."
                                    show sis tit5 at right
                                    "Lily gasps and flinches as the first pulse hits, but doesn't turn away. You give her tits a pump between each burst of cum until you're sure you're completely finished."
                                    if sisO.cumslut:
                                        sis "Oh god, yes! There's so much cum here!"
                                    else:
                                        sis "Oh wow!"
                                    $ sisO.inc_cum_over()
                                    "Lily seems stunned for a few moments after your climax. You take the time to slide your cock up and down between her breasts some more, lubricated by the cum dripping down off her chin."
                                    me "Good job sis, that felt great. Now you should get cleaned up before mom comes in here and sees what a slut you are."
                                    "Lily pouts, but nods and starts looking for something to get cleaned up with. You pull your pants up and leave Lily's room."

                                "Step back and cum all over her." if sisO.slut_score > 80 or sisO.cumslut:
                                    me "I'm almost there! Are you ready for my cum, you little slut?"
                                    sis "Ah. Yes, I'm ready."
                                    me "Tell me you want it."
                                    "You pinch Lily's nipples and use them to pull her tits together around your cock. She gasps loudly, and you can feel her body shiver in pleasure."
                                    sis "Ah! I want it, cover me in your cum!"
                                    "Hearing your sister beg for your semen is enough to push you over the edge."
                                    "You pull back, grab your shaft, and start stroking yourself off while Lily sits on the ground and looks up at you. Her tits are a little red, and her nipples are standing on end."
                                    $ sisO.inc_cum_over()
                                    show sis tit6 at right
                                    "You reach your climax and start to fire off your load. Lily gasps when the first blast lands on her chest, but holds still for you while you point your cock at different places."
                                    "By the time you've finished you've sprayed your seed over her hair, face, and tits. Some of it is running down between her cleavage and pooling at her waist."

                        "Tell her to lie down on the floor" if sisO.slut_score > 80:
                            me "I need more leverage. Lie down Lily."
                            "You let go of Lily's tits, and she lies down on the floor for you. You kneel over her and slide your shaft back between her cleavage."
                            show sis tit7 at right
                            "Then you grab her tits again and push them against both sides of your shaft and go back to tit fucking her."
                            "With Lily pinned on the floor you're able to use your hips and thrust back and forth. Underneath your hands you can feel Lily's rock hard nipples."
                            me "Do you like that?"
                            sis "Ah. I guess."
                            me "You guess? You can tell me if you do, there's nothing wrong with it. You're just being a good slut to your brother and taking care of him."
                            "Lily moans a little as you pinch a nipple between your thumb and forefinger."
                            sis "Okay, I like it then."
                            me "What do you like?"
                            sis "I like my brother fucking my tits. I like being his slut."
                            "You speed up your strokes, pressing the tip of your cock against Lily's lips with each thrust. After a few bumps against her mouth she opens up and lets you slide the tip in at the top of each movement."
                            me "That's a good girl. Get it wet for me."
                            "She sticks her tongue out and runs it along the bottom of your shaft, and before long you've gotten her entire chest wet with her own spit."
                            "The feeling of her wet warm tits presses against you drives you right to the edge of your own orgasm."
                            menu:
                                "Cum on her face.":
                                    me "Oh ya, here I cum!"
                                    "You give her tits a few more good thrusts, then slip out the front and stroke yourself until you cum."
                                    show sis tit8 at right
                                    "Lily lays on the ground and looks up at you while you fire your load over her face. When you're done you move to the side and let Lily sit up."
                                    if sisO.cumslut:
                                        sis "Mmm, it's so warm... Did it feel good for you too?"
                                    else:
                                        sis "Was I okay then?"
                                    me "You were perfect Lily."
                                    $ sisO.inc_cum_over()
                                    "She smiles and wipes cum out from around one eye."
                                    sis "Good. I'm glad you had a good time then."
                                    me "Now you should get yourself cleaned up before anyone sees you like that."
                                    "Lily nods and starts to look for something to get cleaned up with while you pull up your pants and leave the room."

                                "Cum down her throat." if sisO.slut_score > 90 or sisO.cumslut:
                                    me "I'm almost there. Do you want to help me cum Lily?"
                                    sis "What can I do?"
                                    me "Open wide for me."
                                    sis "Like this?"
                                    show sis tit9 at right
                                    "Lily opens her mouth, and you slide yourself out from between her tits and right in. She gasps and tries to say something, but is muffled by your cock as it slides into her mouth and down her throat."
                                    "You shuffle forward a little until your waist is above Lily's face. The position lets you get as deep as possible into your sisters throat, bumping your balls against her chin."
                                    "You give her throat a few thrusts and feel it spasm and tighten at the bottom of each stroke. The feeling drives you over the edge, and you push yourself deep into Lily's mouth as you start to cum."
                                    "Lily squirms around under you, drawing her legs up and rolling a little, but doesn't move her head. When you've completely finished your orgasm you pull out of her throat and move to the side."
                                    "Lily rolls over and coughs a few times, then pants to catch her breath."
                                    $ sisO.inc_cum_mouth()
                                    $ sisO.inc_cum_swallow()
                                    if sisO.cumslut:
                                        sis "Thank you [inputName]. I think I... I think I came a little too. You felt so huge in my throat when you finished, I thought I was going to choke on it."
                                    else:
                                        sis "Did I? Ah, hah, that's good."
                                    "You stand and pull your pants up."
                                    me "Thanks for helping me out sis, I'll stop by if I need anything else."
                                    "Lily nods stays on the floor, still catching her breath, as you leave her room."

                                "Cum on the floor and have her clean it up." if sisO.slut_score > 130 or (sisO.cumslut and sisO.slut_score > 100):
                                    me "I'm almost there Lily."
                                    sis "Ah, good! Cum for me [inputName]!"
                                    me "Do you want my cum? Tell me you want it."
                                    sis "I want it! I want my brothers cum so badly, I need it!"
                                    "Hearing your sister beg for your load pushes you over the edge. You pull up and out of her cleavage and start to stroke yourself off to the side over her shoulder."
                                    sis "Hey! Wait!"
                                    "You keep Lily pinned beneath you as you finish cumming over her floor. When you're done you slide off her and over to the side."
                                    me "There you go, it's all yours Lily."
                                    "Lily sits up and looks at you, then glances at the white globs beside her."
                                    show sis tit10 at right
                                    "She pouts, then leans over and runs her tongue through the largest pool of it. She tilts her head up and swallows, then leans back down and does it again."
                                    "You watch her as she licks up all of your cum, taking a moment to swallow each time. Finally she sits up and looks at you while you pull up your pants."
                                    me "Good job. I can see you really wanted it."
                                    sis "Can I have it properly next time?"
                                    me "We'll see. Maybe if you do a very good job."
                                    "Lily nods. You head out of her room while she starts to pull her dress up."

            $ sis_hub.inc_level(3)
            $ sisO.change_resist(-sis_hub.use_red(3,sisO.resist_score))

        "Make her blow you." if sisO.slut_score > 70:
            me "Well I was feeling a little bored, and I thought that my slut of a sister might be able to help me out."
            "You pull down your pants past your hard cock. Lily glances at it, then back at you."
            sis "What would you like me to do?"
            "You sit down on the bed beside her, pulling your pants all the way free."
            me "I'd like you to get on your knees and suck me off."
            "Lily nods and slides to the ground. She goes to grab your shaft, hesitates, then pulls her dress up and off first."
            show sis blow5 at right
            "Dressed only in her pink panties, she takes your shaft in her right hand and strokes it a few times, then leans forward and kisses the tip."
            me "You'll have to do more than kiss it Lily."
            sis "I know, I'm just getting it ready."
            "She kisses it again, this time sticking her tongue out and running it along the tip."
            "Then she opens her lips, slowly sliding you into her mouth as her tongue gets your shaft wet."
            $ sisO.inc_blow()
            "She bobs up and down a little as she gets to the shaft, going a little deeper with each pass. Her mouth is wet and warm, and the feeling of her tongue swishing past sends shivers up your spine."
            menu:
                "Let her keep going.":
                    "You lean back and let Lily take care of you. She keeps going deeper, and before long she's sliding her lips along the entire length of your shaft."
                    "She pulls up and presses your wet cock against her cheek."
                    sis "Does it feel good?"
                    me "It feels great. Put me back in and keep going."
                    "Lily smiles and opens her mouth wide, then slides all the way to the bottom and bumps her nose against your stomach. After that she pulls up and starts blowing you nice and fast."
                    "A few more minutes of her enthusiastic blowjob and you're getting close to climaxing."
                    menu:
                        "Cum in her mouth.":
                            me "I'm getting close Lily. Keep it up and I'm going to unload into your sweet little mouth."
                            "Lily nods as best she can while blowing you. When you start to tense up she pulls back and opens wide. She grabs your shaft and jerks you off until you start to cum, firing your load right into her waiting mouth."
                            "Lily slows down her handjob once you're done cumming and licks some sperm off of her lips. Then she lets go of you entirely and brings the hand up to her face to spit your load into it."
                            $ sisO.inc_cum_mouth()
                            show sis blow7 at right
                            me "What, too good to swallow?"
                            sis "Oh, uh. Sorry, I just wasn't thinking."
                            if sisO.slut_score > 80 or sisO.cumslut:
                                "Lily looks at her hand, then puts it back to her mouth and starts to drink your cum again. After a few seconds she's drunk it all, and licks up the last little bit."
                                sis "There. All gone."
                                $ sisO.inc_cum_swallow()
                                me "That's a good girl. Well done."
                            else:
                                "Lily looks around and finds some tissue, then wipes off all of your cum."
                                sis "I'll try and do better next time."
                            "You stand and head out of her room while Lily starts to get herself cleaned up."

                        "Cum on her face.":
                            me "I'm almost there Lily. Keep it up, I want to cover you in my cum."
                            "Lily nods as best she can while blowing you. When you get close to orgasming you pull yourself out of her wet mouth with a pop and start to stroke yourself off."
                            show sis blow6 at right
                            "Lily sits back on her knees and looks up at you, tongue out. You start to blast your cum over her, working your way from top to bottom."
                            "After a few sizable spurts of cum you're done, and Lily is covered from forehead to chin. You slide forward a little and rest your tip on Lily's tongue, and she starts to lick the last few drops off."
                            me "Ahh, that was great. You look like the perfect cum slut now."
                            $ sisO.inc_cum_over()
                            "Lily licks your tip clean then pulls back and looks up."
                            if sisO.cumslut:
                                sis "I'm glad you had a good time. I did too, your cum feels so nice and warm on me. I guess I should get cleaned up before Mom finds us though."
                            else:
                                sis "I'm glad you had a good time. I should get cleaned up now, before Mom finds us."
                            "You pull your pants up and head out of Lily's room while she finds something to wipe her face off with."

                "Make her deepthroat you." if sisO.slut_score > 80:
                    "You reach forward and put a hand on the back of Lily's head, pushing her a little deeper."
                    me "Come on, you can do better than that."
                    show sis blow8 at right
                    "Lily turns her eyes up to look at you, then pushes herself as deep as she can go. You feel the tip of your cock tap the back of her throat, then she pulls back until her lips are wrapped around your tip, and goes back down and does it again."
                    me "There we go, that's the Lily I know."
                    "She keeps her eyes locked with yours while she makes sure to take every inch of your shaft into her throat. As she speeds up her throat makes soft wet smacking noises as you bump against the back."
                    "You enjoy her deepthroating for a few moments, then wait until she's bottomed out on your cock to press hard against her head and hold her in place."
                    "You grind yourself up against Lily, who manages to somehow fit a little more of you into her mouth. Lily's tongue doesn't waste any time and runs back and forth along the bottom of your dick."
                    "Finally you let her go, and she bounces off your cock to take a deep breath. Once she's recovered, she goes back to blowing you without any complaints."
                    me "That's a good girl. You're doing great."
                    "Her wet mouth and skillful tongue have gotten you right up to the edge of climax."
                    menu:
                        "Cum in her mouth.":
                            me "Okay Lily, I'm almost there. Finish me off now."
                            "Lily moans in response and keeps running her lips up and down, up and down. One of her hands is playing with a breast now, pinching the nipple between her thumb and finger."
                            "A few more thrusts into her throat and you start to climax. Lily slips your tip just inside her lips and keeps them wrapped around, eyes locked on yours while you fire your cum into her mouth."
                            "Her eyes flutter as the first pulse of semen lands on her tongue, and she lets out a long moan as you let out burst after burst of cum."
                            "Finally you're done, and she pulls gently off your sensitive tip."
                            me "Open up for me now."
                            show sis hand7 at right
                            "Lily does as she's told and opens her mouth. Her tongue plays through the pool of white liquid you put in her mouth."
                            me "Good girl. Now swallow."
                            $ sisO.inc_cum_mouth()
                            $ sisO.inc_cum_swallow()
                            "She closes up and you can see her throat work up and down. When she opens up again her mouth is empty."
                            if sisO.cumslut:
                                sis "Mmm, so nice and warm. I love how it feels sliding down my throat..."
                                "Lily shivers with pleasure, licking her lips and savouring the taste."
                            else:
                                sis "There, all done."
                            "You pat Lily on the head and stand up."
                            me "Excellent. Now you should get cleaned up, if I need any more help I'll be sure to come back."
                            "Lily nods and starts to put her dress back on while you leave the room."

                        "Cum down her throat." if sisO.slut_score > 85 or sisO.cumslut:
                            "You wait until you're just about to cum, then start to push down on the back of Lily's head again."
                            show sis blow9 at right
                            "This time there's no resistance and no surprise. Lily slides all the way down your cock while looking at you. She shakes a little as the first blast of cum shoots down her throat, but still doesn't move."
                            "You thrust your hips back and forth in time with your cum, making sure to get yourself as deep as you can for each blast. Lily's throat spasms a little, making it feel even better."
                            "When you're done you pull out, leaving her mouth with a wet pop. Lily pants a few times as she tries to catch her breath."
                            me "Good job sweetheart. You took that throat pie like the perfect little cum slut you are."
                            $ sisO.inc_cum_mouth()
                            $ sisO.inc_cum_swallow()
                            if sisO.cumslut:
                                sis "Thank you [inputName]. Your cum was so nice and thick in my throat, I can still feel it dripping down. Ah..."
                                "She licks her lips and sighs contently."
                                sis "Anyways, I'm just glad I could help."
                            else:
                                sis "Ah. I'm just glad I could help."
                            "You stand and pull up your pants."
                            me "Well if I need any more help I'll be back."
                            "You leave Lily's room as she starts to get her dress back on."

                "Grab her head and skull fuck her." if sisO.slut_score > 90:
                    "You reach forward with both hands and place them on the side of Lily's head, pulling her deeper."
                    me "Here, I'll take over."
                    show sis blow9 at right
                    "Lily locks eyes with you and moans. You pull her all the way down onto your cock, then pump your hips up and down to fuck her throat."
                    "Lily does a great job of keeping her tongue moving, swirling it around your shaft and running it along the underside."
                    "After a moderately gentle start you speed up, drawing farther back with each stroke and pushing into Lily's mouth faster."
                    "She does her best to hold her mouth open, and seems to shudder and moan with each time you hit the back of her throat."
                    me "That's a good little slut. Do you like having your mouth fucked like this?"
                    "You move your hips as fast as they will go and really fuck Lily's mouth. Her eyes flutter as she makes gurgling noises each time you hit the back of her throat."
                    "After a few moments her spit is overflowing her mouth and dripping down her lips and chin. As you pull her back and forth it drapes across her tits and chest."
                    "Eventually you need a break and stop thrusting. Instead, you use your hands and pull Lily all the way down your cock and hold her there. She looks up at you with big eyes as her tongue swirls around your shaft."
                    "You hold Lily down for a few long seconds, enjoying the feeling of her tight throat wrapped around your tip."
                    menu: #TODO add better images for each step
                        "Let her up.":
                            "Before too long you let Lily slide up and off."
                        "Keep going." if sisO.slut_score > 95 or sisO.freeuse:
                            "You keep holding Lily down, mouth wrapped around your dick."
                            "Lily's throat starts to spasm, getting tighter and looser in turns. She seems to take it as a challenge, and pushes herself even deeper onto your dick."
                            menu:
                                "Let her up.":
                                    "You enjoy Lily's tight throat for a while, then let her slide up and off."
                                "Keep going." if sisO.slut_score > 100 or sisO.freeuse:
                                    "You hold your sister down on your cock even longer."
                                    "Lily's eyes flutter a little bit, and she starts to purr like a cat as she grinds down on you."
                                    menu:
                                        "Let her up.":
                                            "You enjoy Lily's tight throat for a while, then let her slide up and off."
                                            "Lily stays down a few extra seconds before she pulls off with a wet pop."
                                        "Keep going." if sisO.slut_score > 105 or sisO.freeuse:
                                            "You hold her down even longer."
                                            "Something triggers Lily's gag reflex and she coughs, blowing spit bubbles around the base of your shaft. She bounces up a little bit, but pushes herself back down as soon as she can."
                                            "Lily's eyes are half closed now, and she seems to have gotten comfortable with your cock lodged down her throat. She shakes her head left and right a little, trying to go deeper."
                                            menu:
                                                "Let her up.":
                                                    "You let go of Lily's head so she can slide up for air, but she stays pressed down. A few long seconds pass, then she comes back up with a wet pop."
                                                "Keep going.":
                                                    "Eager to see how long she can manage, you keep the pressure up on the back of Lily's head."
                                                    "Lily starts to squirm around, but doesn't try to pull back. One of her hands is playing with a breast while the other has started to rub her clit through her panties."
                                                    menu:
                                                        "Let her up.":
                                                            "Lily slides up and off with a wet pop a short while after you let go of her head."
                                                        "Keep going." if sisO.slut_score > 110 or sisO.freeuse:
                                                            "Lily's eyes start to open a little now, and she tries to pull back. Looking down you see her nipples are rock hard, and there's a wet patch where she's soaked through her panties."
                                                            menu:
                                                                "Let her up.":
                                                                    "Lily slides up and off your cock with a wet pop as soon as you let go of her head."
                                                                "Keep going." if sisO.slut_score > 115 or sisO.freeuse:
                                                                    "The feeling of Lily's tightening throat is driving you closer to climax. You keep holding her down as she starts to struggle a little."
                                                                    "Lily twists and turns, but doesn't offer any real resistance. The wet spot on her panties continues to grow, and you feel her whole body shiver."
                                                                    menu:
                                                                        "Let her up.":
                                                                            "Lily slides up and off your cock with a wet pop as soon as you let go of her head."
                                                                        "Keep going." if sisO.slut_score > 120 or sisO.freeuse:
                                                                            "Sensing that she's still enjoying this, you don't let up. Lily struggles a little bit more, but her eyelids start to slide slowly down again."
                                                                            "Her panties are practically drenched now, even though she stopped touching herself to put her hands on your thighs. You feel her start to shake underneath you, and she tries to moan past your cock."
                                                                            menu:
                                                                                "Let her up.":
                                                                                    "You let go of Lily's head, and she pulls back almost immediately. She falls over to her side and thrusts both hands between her legs."
                                                                                    sis "Ah! AH! AH!!!!"
                                                                                    "Lily screams loudly as she fingers herself, suddenly released in the middle of a huge orgasm."
                                                                                    "You grab your shaft and stroke yourself off while Lily writhes and twitches on the ground, panties pulled to the side and both hands drenched in her juices."
                                                                                    me "Fuck that's hot. I'm going to cum."
                                                                                    sis "Ah! Do it! AH!"
                                                                                    "You get up and stand over Lily, who's still lying on the ground fingering herself. She rolls over so she's face up, arching her back while she continues to orgasm."
                                                                                    show sis blow11 at right
                                                                                    "The sight drives you over the edge and you start to cum. You fire your load over your sister, starting with her face and working your way down until you've covered every inch of her with some of your sperm."
                                                                                    "Lily lets out one last high pitch moan, then collapses to the ground. She looks up at you, eyes half closed and obviously left in a daze."
                                                                                "Keep going." if sisO.slut_score > 125 or sisO.freeuse:
                                                                                    "Lily must be very well conditioned to let you go this far with her. Her eyelids are half closed again, and she's shaking and spasming."
                                                                                    "Her pussy is absolutely drenched, and from the way she's still moaning you think she's having one long drawn out orgasm."
                                                                                    show sis blow10 at right
                                                                                    "Suddenly her eyes close completely and she slumps forward, her full weight pushing her down on your cock. The feeling drives you over the edge, and you start to cum."
                                                                                    "Before you can act you fire your first pulse of cum down her throat. You pull her head back, firing the rest of it over her face and down onto her tits. Lily gasps for air as soon as she's free, but doesn't come around right away."
                                                                                    "You check her pulse and make sure she's breathing okay, then feel down between her legs. Her pussy twitches as you touch it, and Lily moans weakly."
                                                                            $ sisO.inc_cum_over()
                                                                            #Needed because this jumps early, before the rest of the statements fall through to the normal exit point
                                                                            $ sis_hub.inc_level(4)
                                                                            $ sisO.change_resist(-sis_hub.use_red(4,sisO.resist_score))
                                                                            "You lift Lily onto her bed lay her down. You pull your pants up and head out, leaving Lily lying on her bed covered in your cum while she recovers."

                    "Lily takes a moment to catch her breath, panting softly while you hold your cock against her cheek. When she's ready you slip yourself back into her mouth and start to fuck it again."
                    "For a few more minutes you hold Lily's head in place while you pump your cock in and out of her mouth. Eventually the warm, wet, slippery hole drives you to the climax."
                    menu:
                        "Cum on her face.":
                            me "Here I cum Lily!"
                            "Lily does her best to nod while you fuck her face right to the edge of your orgasm, then pull out and stroke yourself off with one hand while you hold Lily in place with the other."
                            show sis blow12 at right
                            "You fire off your load, spraying cum all over your sister's eager face. She keeps her mouth open and puts out her tongue for you, letting you shoot some of your seed inside."
                            "When you're finished you let go of Lily and yourself, then lean back on the bed. Lily's face is a mess, covered with spit and cum, but she's still smiling up at you from the floor."
                            if sisO.cumslut:
                                sis "It's so nice and thick. Ah... Did I do a good job?"
                            else:
                                sis "Did I do a good job?"
                            me "Ha, ya. You did a great job."
                            $ sisO.inc_cum_over()
                            "You catch your breath, then stand and pull your pants up."
                            me "Now you should get cleaned up, I've got some stuff to do."
                            "Lily nods and starts looking for something to wipe your cum off with while you leave the room."

                        "Cum down her throat." if sisO.slut_score > 95:
                            me "Here I cum Lily!"
                            show sis hand9 at right
                            "Lily does her best to nod while you fuck her face right to the edge of your orgasm. At the last moment you push down hard on the back of her head and send her plunging deep onto your dick."
                            "Almost immediately you start to fire you cum down her throat. Lily does her best to look up at you and maintain eye contact while you empty yourself into her stomach."
                            "When you are finished you let go of Lily, who slides off of you and takes a deep breath. Then she looks up at you, still panting, and smiles."
                            if sisO.cumslut:
                                sis "Mmm, it's so nice and thick in my throat... Did I get it all out of you?"
                            else:
                                sis "I got it all, right?"
                            me "Ya you did. Good job."
                            $ sisO.inc_cum_mouth()
                            $ sisO.inc_cum_swallow()
                            "Lily smiles and seems proud of herself. You stand and pull your pants up and start heading for the door."
                            me "Now you should get dressed before mom finds out that you're my own personal cum slave now."
                            "Lily nods and starts to put her dress back on while you leave her room."
            $ sis_hub.inc_level(4)
            $ sisO.change_resist(-sis_hub.use_red(4,sisO.resist_score))

        "Fuck her." if sisO.slut_score > 80:
            me "I'm feeling stressed and need you to take care of me Lily. You can start by getting naked."
            "Lily looks like she's about to say something, but nods instead and stands up. She slips her dress straps off her shoulders and pulls it down to the ground, then pulls her panties down and steps out of them as well."
            menu:
                "Bend her over the bed and fuck her.":
                    me "That's a good girl. Now bend over for me."
                    sis "Okay. Like this?"
                    show sis fuck9 at right
                    "Lily turns around and leans over her bed, stretching out and shaking her ass towards you."
                    "You walk up behind her and slip your pants down past your waist to free your hard cock. You bounce it up and down on her ass cheeks a few times and watch the way they shake each time."
                    me "That's great Lily, just like that."
                    "You reach a hand down and run it between your sister's legs. She's already wet when you slide a finger inside her to play with her pussy a little."
                    $ sisO.inc_sex()
                    "Once you feel you've teased her enough you hold your shaft and line it up with her slit. You run your tip up and down a few times to get it wet, then press forward and slip all the way into Lily."
                    "She gasps a little when you slide all the way to the back, but after a few pumps she's comfortable and moaning."
                    "Lily's pussy is wet and tight, and each thrust seems to make her even wetter."
                    me "How does that feel? Having a good time Lily?"
                    sis "Ah! Oh god, you feel so good!"
                    me "Good, I want my slut of a sister to have the time of her life!"
                    "You grab her ass and fuck her fast and hard for a few moments. Lily gasps and moans, panting for breath in between each thrust."
                    sis "Please don't stop. Oh, please please please don't stop!"
                    me "Are you going to cum soon?"
                    "Lily nods and wimpers a few times, and you can feel her pussy twitch around your shaft."
                    "You go back to fucking Lily as fast as you can manage. Her ass jiggles each time you slam into her, and her dangling tits swing back and forth underneath her."
                    show sis fuck10 at right
                    "Lily's gasps get higher and higher pitched and she starts to squirm and shake underneath you. Before long she's buried her head in a pillow and is screaming as she has a powerful orgasm of her own."
                    "Lily's pussy gets even tigher around you, and the feeling pushes you over the edge."
                    "You grab her hips and use them as leverage to pull her back into you, getting yourself as deep into her as you can manage."
                    menu:
                        "Cum inside her.":
                            "When you reach your own climax you hold yourself deep down inside her, then pull back for a moment after the first pulse and thrust in again for the next."
                            show sis fuck11 at right
                            "Finally you've finished unloading inside of Lily. You give her a few more thrusts for good measure, then pull out with a wet pop. Lily's gone mostly limp, lying face down on the bed and panting loudly."
                            me "That was great. Now make sure to get cleaned up before I need you again."
                            $ sisO.inc_cum_inside()
                            if sisO.preg_response_ok():
                                "Lily nods weakly as you pull up your pants. You head out of the room just as your cum starts to leak and run down one of her legs."
                            else:
                                sis "Okay... But you really shouldn't cum inside me when I'm not on the pill..."
                                "You shrug and pull your pants up. You head out of the room just as your semen starts to leak and run down one of her legs."


                        "Cum over her ass.":
                            show sis fuck12 at right
                            "Right before you finish you pull out of Lily with a wet pop and grab your shaft. You stroke yourself off over Lily's ass, covering it with hot cum."
                            "When you're done you rub the tip of your penis around her slipperly ass cheek."
                            me "That was great. You look amazing covered in cum Lily."
                            "Lily nods weakly as she lays on the bed face down, still panting loudly."
                            $ sisO.inc_cum_over()
                            me "Now you should get yourself cleaned up in case I need you again."
                            "You pull your pants up and head out of Lily's room, leaving her bent over and covered in cum."

                "Fuck her on the bed.":
                    me "That's a good girl. Now lay down for me and spread your legs."
                    show sis fuck13 at right
                    "Lily lays down on her bed and looks up at you. She moves her legs to the side and presents her pussy to you."
                    sis "Like this?"
                    me "That's perfect Lily, just like that."
                    "You pull your clothes off, then get onto Lily's bed and settle in on top of her. You keep yourself steady with one hand while you use the other one to guide the tip of your penis to her slit."
                    "You rub it up and down a few times, getting it wet with Lily's juices."
                    me "Are you ready?"
                    sis "Ya, I'm ready. Use me however you want."
                    "Lily smiles, then gasps as you thrust all the way into her."
                    $ sisO.inc_sex()
                    "You settle into a steady rhythm pumping in and out of your sister while she moans underneath you. Her pussy is wet and tight, and feels simply amazing."
                    "Lily looks up into your eyes while you fuck her, moaning and gasping softly as you plunge deep inside her."
                    show sis fuck14 at right
                    "After a few minutes you grab Lily's legs and push them up so they're spread wide and to the sides. Lily reaches forwards and holds them in place, and the new position lets you get even deeper."
                    sis "Ah, that feels amazing. Don't stop, please don't stop."
                    "Lily's pussy twitches around your shaft as you fuck her. You shift forward slightly so you're rubbing up against her clit with each stroke and fuck her even faster."
                    "After a few more minutes of vigorous fucking Lily has been driven to the edge of an orgasm. Her eyes are rolled up and she's moaning loudly, pushing her hips against you as much as she can manage."
                    "Finally she lets out one long scream and her core muscles spasm a few times. Her pussy gets even tighter around you as she cums, and it drives you to your own orgasm."
                    menu:
                        "Cum inside her.":
                            "You give Lily a few more good thrusts to put yourself over the edge, then press yourself deep inside while you climax. You and Lily orgasm together, and you pump her full of your cum."
                            "When you're both done you pull out, leaving her pussy with a wet pop. You roll off of her and sit up on the bed."
                            show sis fuck16 at right
                            me "Ah, good job Lily."
                            if sisO.preg_response_ok():
                                if sisO.cumslut:
                                    sis "Ah... It's so thick and warm. I hope you aren't trying to get your own sister pregnant like this..."
                                else:
                                    sis "Oh god. You felt... You felt so good."
                            else:
                                sis "Oh god [inputName], you really shouldn't do that when I'm not on the pill. What if you got me pregnant?"
                            $ sisO.inc_cum_inside()
                            "You stand and start to get dressed while Lily lies on the bed and recovers. Your semen starts to leak out of her pussy and onto her bed."
                            me "You should get cleaned up soon, in case I need you to take care of me again."
                            "Lily nods weakly, and you leave her in her room to recover for a while."

                        "Cum over her.":
                            "You give Lily a few more good thrusts to put yourself over the edge, then pull out and keep stroking yourself off."
                            show sis fuck15 at right
                            "Lily looks up at you and manages to get her mouth open and tongue out while you blast your load all over her. You start with her face, then work your way down leaving a trail of cum along her entire body."
                            me "Good job, that's a good little slut."
                            "Lily moans and twitches some more, having another mini orgasm."
                            $ sisO.inc_cum_over()
                            "When you're done you sit down on the edge of her bed and catch your breath. Lily stays lying down, covered in your semen from head to toe."
                            me "That was great Lily, well done. Now you should get cleaned up in case I need you to take care of me again."
                            "Lily nods weakly and tries to sit up. She gives up half way, and collapses back onto the bed."
                            "You get dressed and leave Lily in her room to recover."

                "Anal her." if sisO.slut_score > 110 or (sisO.anal and sisO.slut_score > 80):
                    me "That's a good girl. Now bend over your bed for me, nice and low."
                    show sis fuck17 at right
                    "Lily turns around and bends over for you. At first she sticks her ass high in the air, but you put a firm hand on it and push it lower."
                    "You pull your clothes off and plant your hard dick on her ass cheek, bouncing it up and down on it a few times."
                    me "Okay, now lets see if I can fit into this tight ass of yours."
                    "You hold your shaft and line yourself up with Lily's asshole. You press against it, but have trouble making it inside."
                    sis "Ah! It feels so big!"
                    me "Damn, you're tight. I'm going to need some lube for this."
                    "You move around to the side and kneel on Lily's bed so your waist is level with her face."
                    me "Suck me off and get me wet Lily."
                    show sis fuck18 at right
                    "She nods and opens her mouth wide for you. You slide inside, and she starts to work her tongue around your shaft."
                    "After a few moments you pull out of her mouth again, your cock now covered in her spit, and line up behind Lily again."
                    show sis fuck17 at right
                    "Now that you're all lubed up you're able to press into Lily, slipping into her tight asshole bit by bit."
                    $ sisO.inc_sex()
                    "Lily gasps and pants as you slide deeper into her."
                    if sisO.anal:
                        sis "Keep going, I can take it!"
                    else:
                        sis "I can't do it! It's too big!"
                        me "You can do it, you've almost got it all in."
                    "You press harder and slip your full length into Lily's ass. It's way tighter than her pussy, and seems to squirm around your dick a little."
                    "You wait a few moments to let Lily get used to your cock balls deep in her, then pull back and start to fuck her."
                    sis "Ah, oh fuck, oh fuck!"
                    "Lily grunts in a combination of pain and pleasure as you anal her. The tight wet hole does a great job pushing you towards your own orgasm though, and very soon you're feeling ready to finish."
                    menu:
                        "Cum inside her ass.":
                            "You hold Lily's waist and fuck her hard for a few moments, causing her to whine and moan. You don't slow down as you start to cum, using the liquid as lubrication to go faster and deeper."
                            if sisO.cumslut:
                                sis "Ahh! Oh fuck yes, fill my ass up with your thick cum! Please!"
                            else:
                                sis "Ahhh! Oh fuck, I can feel it all!"
                            $ sisO.inc_cum_inside_ass()
                            "You keep fucking for a few more moments until you're completely finished, then pull out of her ass with a wet pop."
                            show sis fuck19 at right
                            "Lily slumps forward onto her bed, ass stuck up in the air with her anus red and puffy. A little bit of your cum starts to leak out and run down towards her pussy, which is wet and twitching."
                            me "Damn, that felt great Lily. Now you should get cleaned up in case I need you to help me out again later."
                            "Lily doesn't respond and keeps panting for air. You get dressed and leave her in her room to recover."

                        "Cum over her ass.":
                            "You hold Lily's waist and fuck her hard for a few moments, causing her to whine and moan. When you start to cum you pull out with a wet pop and stroke yourself off over her ass."
                            show sis fuck20 at right
                            "Lily screams a little when you pull out, then slumps forward as you cover her cheeks with cum. Her anus is red and puffy from your pounding, but underneath her pussy is wet and twitching."
                            $ sisO.inc_cum_over()
                            me "Ah! That's just what I needed. Now you should get cleaned up in case I need you to help me out again later."
                            "Lily doesn't respond and keeps panting for air. You get dressed and leave her in her room to recover."
            $ sis_hub.inc_level(5)
            $ sisO.change_resist(-sis_hub.use_red(5,sisO.resist_score))
        "Give her some serum and train her.\n-15 Influence, -2 Serum" if sisO.slut_score > sisO.training_threshold and (player_blue_serum + player_purple_serum + player_red_serum > 1):
            menu:
                "Train her to be a cum slut from now on." if not sisO.cumslut:
                    call cumslut_descrip("Lily")
                    menu:
                        "Continue with the training.":
                            call sis_train_cumslut
                        "Change your mind and leave.":
                            return False

                "Train her to be an anal lover from now on." if not sisO.anal:
                    call anal_descrip("Lily")
                    menu:
                        "Continue with the training.":
                            call sis_train_anal
                        "Change your mind and leave.":
                            return False

                "Train her to be a free use slut from now on." if not sisO.freeuse:
                    call freeuse_descrip("Lily")
                    menu:
                        "Continue with the training.":
                            call sis_train_freeuse
                        "Change your mind and leave.":
                            return False

                "Train her to be an exhibitionist from now on." if not sisO.exhib:
                    call exhib_descrip("Lily")
                    menu:
                        "Continue with the training.":
                            call sis_train_exhib
                        "Change your mind and leave.":
                            return False

                "Change your mind and leave.":
                    return False

        "Just talk with her.":
            me "Oh, not much, just bored and coming to see what's up with you."
            "You spend a few minutes talking with Lily about nothing in particular."
            return False
    return True

###################
##Mom's Hub Scene##
###################

label hub_mom:
    menu:
        "Ask her to strip for you." if momO.slut_score > 20:
            me "By the way Mom, you're looking great today. That shirt makes your tits look amazing."
            "Mom smiles and laughs a little."
            me "Seriously. I'd love to take a look if you don't mind."
            mom "At my breasts?"
            me "Ya, at all of you really."
            "Mom thinks for a moment, then stands up and starts to unbutton her shirt."
            mom "You really think I look that good?"
            me "Damn right I do! You've got a body to kill for."
            show mom strip9 at right
            "She smiles and pulls her shirt off, throwing it over the back of the couch."
            mom "How's this?"
            me "Great. Lose the pants too."
            show mom strip17 at right
            "Mom nods and loosens her pants too, letting them fall to the ground and then stepping out of them."
            show mom strip18 at right
            "She gives you a turn, showing off her ass in her beige panties."
            if momO.slut_score > 30:
                menu:
                    "Show off for me.":
                        me "Fuck I'm lucky. Bend over for me Mom."
                        show mom strip12 at right
                        "Your mom complies, bending over so her ass is pointing towards you."
                        mom "Like this?"
                        me "Just like that, ya."
                        "You enjoy looking at her large, tight ass for a few moments."
                        me "Spread your legs for me."
                        show mom strip19 at right
                        "Mom nods and follows your instructions, straightening up a little and spreading her legs so you can get a good look at her crotch from behind."
                        mom "Like what you see?"
                        me "Ya, very much so."
                        show mom strip20 at right
                        "She shakes her ass at you a little, then reaches back and pulls her panties to the side to give you a clear view of her pussy."
                        mom "Good. I've always thought of myself as a MILF, I'm glad you agree."
                        show mom strip17 at right
                        "Mom gives you a few more moments to enjoy yourself, then straightens up and pulls her panties back into position."

                    "Touch yourself.":
                        me "Fuck I'm lucky. Touch yourself a little for me mom."
                        show mom mast1 at right
                        "Your mom complies, slipping a hand between her legs and running a finger over her pussy through her underwear."
                        mom "Mmm, that does feel good actually. Maybe I'll just get this out of the way."
                        show mom mast2 at right
                        "She slips her panties to the side and starts to play with her cunt while you watch."
                        show mom strip17 at right
                        "After a few moments she slips a finger into her wet slit, pumping it in and out a few times. Finally she lets out a soft moan and stands up again, pulling her underwear back into position."
                        #Mom touching herself

                if momO.slut_score > 50:
                    mom "Do you think I look good in this underwear?"
                    "She puts a hand on her ass and poses for you."
                    me "Ya, I think you do. You'd look good wearing a paper bag though for all it matters."
                    mom "Well I don't have any paper bags, but I've got a few things hanging around I could try on for you if you'd like. Stuff I never get a chance to wear normally."
                    me "Sure, what sort of stuff do you have?"
                    "Mom disappears for a second, then comes back with a collection of clothing. She holds up a few pieces, letting you pick what you'd like to see."
                    menu:
                        "Black lingerie.":
                            me "That black set looks hot. How about you put that on for me."
                            show mom nightstrip3 at right
                            "Mom nods and strips down to nothing in front of you, then starts to put the lingerie on one piece at a time."
                            show mom strip24 at right
                            "Finally she's dressed and turns to face you again, boobs and pussy covered by a translucent bra and panty set."
                            me "Wow, you look great in that Mom. It really shows off your tits."
                            "She smiles and jiggles them for you. The thin fabric barely stops them from slipping out the side."
                            mom "Thank you sweetheart, I like it too. What do you think about the heels?"
                            show mom strip25 at right
                            "She turns around, bending over and look back at you."
                            me "Very hot, they make your legs look fantastic."
                            "Mom lets you watch her for a few more minutes, posing in her lingerie for you."
                            mom "Okay, I should really get dressed now. Lily might come around and this would be a little hard to explain."
                            me "Sure thing, thanks for the show Mom."
                            "She takes the outfit off and grabs her old clothes, putting them them back on."
                            show mom casual at right

                        "Swimsuit.":
                            me "Is that a new swimsuit? It looks a little smaller than what you normally wear."
                            "Mom pulls out the two piece swimsuit, holding it up against her body."
                            mom "I suppose it is. Here, tell me what you think about it."
                            show mom strip26 at right
                            "She strips off her underwear and puts on the swimsuit. The top barely covers her tits, and the bottom is so low cut you can see her trimmed bush poking out of the top."
                            mom "Well?"
                            me "You look great in it Mom. Turn around for me, lets see what it looks like from behind."
                            "She turns around for you and takes a few steps, her ass jiggling as she walks."
                            show mom strip27 at right
                            me "Fuck, that's hot."
                            mom "Good, I'm glad you like it."
                            show mom strip26 at right
                            "She turns back to you and poses for a few minutes, letting you look her over from every angle."
                            mom "Okay, I should really get dressed now. Lily might come around and this would be a little hard to explain."
                            me "Sure thing, thanks for the show Mom."
                            "She takes the swimsuit off and grabs her old clothes, putting them back on."
                            show mom casual at right

                        "Naked.":
                            me "Hmm. Those all look great, but I think I'd just like to see you without anything on."
                            mom "Is that so?"
                            show mom strip21 at right
                            "She reaches behind her back and undoes her bra, holding it in place for a moment to tease you."
                            mom "You'd like to see these? That's just so naughty though, showing off my tits to you."
                            show mom strip22 at right
                            "She lets the bra fall to the floor and leans forward so her tits dangle in front of her."
                            mom "Oops."
                            me "Wow, looking good mom. Really good."
                            "Mom smiles and reaches for her panties, slipping her thumbs under the waistband and playing with them for a moment."
                            mom "Now it would definitely be way too naughty for me to take these off, right? I mean, you're my son..."
                            show mom strip23 at right
                            "She turns around and starts to bend over, pulling her panties down as she goes. She ends with her ass high in the air, legs straight, with her panties on the ground."
                            mom "But you've been such a good boy lately, you deserve some sort of reward."
                            "She straightens up and spreads her legs, letting you get a good look at her pussy from behind."
                            "You sit back on the couch and enjoy the view."
                            me "Ya, that's a pretty good reward."
                            show mom nightstrip3 at right
                            "Mom turns around and smiles at you, bouncing her tits in her hands."
                            mom "I'm glad you liked it. I should get dressed though, Lily might come around and this would be a little hard to explain."
                            "She grabs her panties and slides them back on, then her bra, followed by the rest of her clothing."
                            show mom casual at right

                    "Once she's fully dressed again she sits back on the couch next to you, and the two of you watch TV together for a while."
                else:
                    mom "Well I hope you enjoyed yourself, I certainly had some fun."
                    me "That was hot Mom, thanks."
                    show mom casual at right
                    "Mom begins putting her clothes on and rejoins you on the couch. You watch TV with her for a little while longer, then say goodbye."
            else:
                me "Fuck I'm lucky."
                "Mom turns back to you."
                mom "Glad I could make you happy. Now if you don't mind, it's a little chilly in here."
                me "Sure, thanks mom."
                show mom casual at right
                "Your mom gets dressed again and sits back down on the couch. You watch some TV together for a little while longer."

            $ momO.inc_naked()
            $ mom_hub.inc_level(1)
            $ momO.change_resist(-mom_hub.use_red(1,momO.resist_score))

        "Ask for a handjob." if momO.slut_score > 35:
            "After a few minutes watching TV you turn to your mom."
            me "Hey, I actually have a small favour to ask."
            mom "Hmm? What's that?"
            "You unzip your pants and pull them down, letting your hard cock free."
            me "I'm a little worked up, and I was thinking you could just give me a hand with this. Your hand would get me off faster than mine would."
            if momO.slut_score > 50:
                # Lets you cum somewhere else
                show mom hand4 at right
                "Mom nods and reaches out, taking your cock in her hand and giving it a few slow strokes."
                mom "Just sit back and leave this to me, I'll take care of it."
                show mom hand12 at right
                $ momO.inc_hand()
                "She slides off the couch, getting on her knees in front of you and placing her other hand on your balls."
                mom "Here, I'm sure this will feel even better."
                "She pauses for a moment and brings her hand to her face. She licks her palm, then spits into her hand before wrapping it around your shaft again and stroking you off again."
                me "Fuck, that feels so damn good."
                mom "Enjoy it, you've been working really hard lately. The least I can do is help you relax."
                "She speeds up at the end of her sentence, stroking you fast and hard. Her slippery hand makes wet smacking noises as it goes up and down, up and down."
                "Before long her handjob has brought you to the edge of your orgasm. She slows down and looks up at you, rubbing a thumb over your tip and sending shivers down your spine."
                mom "Almost there? I can feel you twitching."
                me "Ya, almost."
                mom "Just let it all out, wherever you want."
                menu:
                    "Cum on her tits.":
                        me "Get your tits out, I want to cum on them."
                        "Mom nods and lets go of your cock so she can unbutton her shirt. She pulls it open, then pulls her bra up so her tits fall free."
                        mom "Here you go, whenever you're ready."
                        show mom hand15 at right
                        $ momO.inc_cum_over()
                        "She holds her tits up for you while you grab your shaft and stroke yourself to completion. She gasps softly as the first blast of cum lands over her breasts, then waits quietly until you've finished."
                        me "Ha, wow."
                        if momO.cumslut:
                            mom "Mmm, thank you sweetheart. You gave me a nice big load right over my tits. I hope you had a good time."
                        else:
                            mom "I'm glad you had a good time sweetheart."
                        "Mom stands up and bends over, giving you a quick peck on the cheek. Her spunk covered tits dangling in front of you."
                        mom "Now I've got to go and get cleaned up. Maybe next time you should just finish in my mouth, less to fuss about after."
                        hide mom
                        "She gives you a wink and walks off, running a finger up her cleavage to catch some of your cum dripping down."
                        "You pull up your pants, then take a few minutes to catch your breath."

                    "Cum on her face.":
                        me "Just keep going, I want to cum on your face."
                        "Mom nods and strokes you faster, getting the whole length of your shaft with each pass. Her warm slippery hands drive you over the edge, and you start to blow your load all over your mom's face."
                        mom "Ahh!"
                        me "Oh ya, just like that!"
                        show mom hand14 at right
                        $ momO.inc_cum_over()
                        "She turns her head to the side, and you send a few more pulses of spunk across her cheek. She doesn't stop rubbing you off until you're completely spent, then she lets go and sits back with a sigh."
                        if momO.cumslut:
                            mom "Wow, thank you sweetheart. Your semen feels so nice and warm on my face. Do I look good covered in it?"
                            me "Ya, you look great like that Mom."
                        else:
                            mom "Wow..."
                            me "Ya, that felt great."
                        mom "Well, I'm glad you had a good time sweetheart."
                        "Mom stands up and wipes a little bit of cum away from her eye."
                        mom "Now I've got to go and get cleaned up. Maybe next time you should just finish in my mouth, less to fuss about after."
                        hide mom
                        "She gives you a wink and walks off towards the bathroom. You pull your pants up and take a few minutes to catch your breath before getting up and going about your day."

                    "Cum in her mouth" if momO.slut_score > 75 or momO.cumslut:
                        me "Open your mouth, I want to fill it up with cum."
                        "Mom nods and opens wide for you. She leans forward and places the tip of your cock right on her bottom lip, still stroking you off as fast as she can go."
                        me "Ya, just like that. Just like a good slut should."
                        show mom hand13 at right
                        $ momO.inc_cum_mouth()
                        "Her handjob finally pushes you over the edge, and you start to spray your seed into her mouth. She moans softly and keeps her eyes locked on yours as you fill up her mouth."
                        "She doesn't stop stroking your shaft until you're completely done cumming, then she sits back and hesitates for a moment."
                        "After a second of thought she swallows, pauses, then swallows again. With all of your cum gone she takes a deep breath and looks up at you."
                        me "Damn, well done Mom."
                        if momO.cumslut:
                            mom "Oh, it's nothing. It tasted so good, I just wish there was some more."
                            "She licks her lips and sighs happily."
                            mom "Anyway, I hope you had a good time sweetheart."
                        else:
                            mom "Thank you. I'm glad you had a good time sweetheart."
                        show mom casual at right
                        "She gets back onto the couch beside you as you pull up your pants. You watch TV together for another hour or so before you say goodbye and separate."

            else:
                show mom hand4 at right
                "Mom stares at your crotch for a few seconds, clearly thinking. Finally she nods her head and reaches over, wrapping her hand around your shaft."
                mom "Just sit back, I'll do what I can."
                "You lean back and relax while your mom starts to jerk you off, slowly at first but building up speed."
                "After a little while your precum drips down onto her hand. She gasps softly, then swirls her palm up over the tip of your cock to get it wet before stroking you even faster."
                me "Fuck, that feels great."
                mom "Good. Just let go whenever you want to."
                "Mom keeps going, pleasuring you with one hand while she half-heartedly watches TV. Before long her slippery grip has got you right on the edge of climax."
                me "Ah, here I come."
                "Mom stays silent as you start to fire your load out and onto the floor. She slows down her strokes as you finish cumming, then stops entirely as the last few pulses dribble down your shaft and onto her fingers."
                show mom casual at right
                "She wipes her hand on her pants, then smiles at you."
                mom "There, I hope you feel better now."
                me "Ya, much better."
                mom "Good. Go grab some paper towel and clean that up before it stains."
                me "Right, sure."
                "You pull your pants up, then head to the kitchen. Once everything is cleaned up you watch TV for another hour or so before saying goodbye."
            $ mom_hub.inc_level(2)
            $ momO.change_resist(-mom_hub.use_red(2,momO.resist_score))

        "Ask for a titfuck." if momO.slut_score > 50:
            "After a few minutes watching TV you turn to your mom, placing a hand on her leg and squeezing it gently."
            me "Hey Mom, could you do me a favour?"
            mom "Mmhmm, what do you need?"
            me "I've been thinking about your boobs this whole time. Think you could get them out for me and take care of this?"
            "You pull your cock out from your pants, presenting it for your mom to see."
            "She thinks for a moment, then nods and starts to unbutton her shirt."
            mom "I'll see what I can do for you."
            show mom strip9 at right
            "She finishes unbuttoning her shirt and pulls it open, then pulls her bra up and lets her tits flop out of the bottom."
            show mom tit5 at right
            $ momO.inc_tit()
            "Your mom gets onto her knees in front of you, holding her tits together while she leans forward and slips your cock into her cleavage."
            me "Ah, that feels great."
            mom "Good, just relax and let me take care of this for you."
            "She holds her breasts tight on either side of your cock and guides them up and down, stroking you off with the soft warm tunnel of her cleavage."

            if momO.slut_score > 70 or momO.cumslut:
                "After a few minutes she pauses and lets your cock slide out from between her tits."
                mom "Here, this should feel even better."
                show mom tit7 at right
                "She leans in farther and places her lips on the tip of your penis, then bobs her head down slowly, lips parting to let you slip into her mouth. Your mom's tongue wraps around your shaft as you slide down into her throat."
                "She pauses for a moment, then slowly slides back out and off your cock. Once that's done she grabs her tits again and squeezes them around your now wet and slippery dick."
                me "Oh fuck..."
                mom "Does it feel good, sliding between my breasts? It feels so dirty."
                "She giggles a little and keeps titfucking you."
                "Before long her spit has gotten her entire chest wet and slippery, and you're sliding up and down between her cleavage at a solid pace."
                menu:
                    "Take over and fuck her tits." if momO.slut_score > 80:
                        #Take over and fuck her
                        me "Oh ya, that feels great. Hold still for a moment."
                        "You reach down and slide your hands over your mom's tits, brushing hers to the side. You squeeze her breasts together around your cock, then start to work your hips up and down."
                        mom "Oh wow, ah!"
                        show mom tit11 at right
                        "You stand up from the couch, causing your mom to fall back onto her ass. You hold her boobs together and fuck the slippery tunnel formed by her cleavage."
                        me "Your tits feel great Mom. Lick my tip."
                        show mom tit12 at right
                        "She pants a little and nods, opening her mouth and sticking out her tongue. On the top of each stroke she gives the top of your cock a little lick before it slips back down."
                        "You keep going like this for a few more minutes, fucking your mom's wet warm tits until you feel your orgasm getting close."
                        menu:
                            "Cum on her tits.":
                                me "Here we go!"
                                "You squeeze down tight, and piston your hips back and forth a few times as you start to cum. Mom gasps softly as you spray your cum out the top of her cleavage and over her tits."
                                "You give a few more thrusts as you're cumming, letting out more of your seed between her breasts. When you're completely finished you let go and sit back heavily on the couch."
                                show mom tit8 at right
                                $ momO.inc_cum_over()
                                mom "Wow, that's a lot. Ah..."
                                if momO.cumslut:
                                    "Mom runs a finger between her tits, catching a drop of your cum before it can run down onto her shirt. She brings it to her lips and licks it clean, sighing happily as she savours the taste."
                                else:
                                    "Mom runs a finger between her tits, catching a drop of your cum before it can run down onto her shirt. She hesitates for a moment, then wipes it off on the back of her pants."
                                me "That was amazing Mom. Thanks."
                                mom "I'm just glad you had a good time. Now I should go get cleaned up."
                                hide mom
                                "Mom stands up and takes a moment to steady herself, then walks towards the bathroom."

                            "Cum on her face.":
                                me "Here we go!"
                                "You squeeze down tight on her boobs and give her a few more thrusts until you're right on the edge. Then you pull out from between her slippery cleavage and grab your cock, stroking yourself off over her face."
                                show mom tit14 at right
                                $ momO.inc_cum_over()
                                "She looks up at you and gives you a small smile as you start to unload onto her. You cover her with your sperm, forehead to chin. Once you're done you sit back on the couch with a sigh, admiring your work."
                                mom "Wow, that's a lot. Ah..."
                                "She nods and wipes some of your cum away from around her eyes. She hesitates for a moment, then licks her finger clean while she looks at you."
                                me "That was amazing Mom. Thanks."
                                if momO.cumslut:
                                    mom "No, thank you sweetheart. It feels so nice and warm on my skin. I suppose I should go and get cleaned up though, I can't stay like this all day."
                                else:
                                    mom "I'm just glad you had a good time. Now I should go get cleaned up."
                                hide mom
                                "Mom stands up and takes a moemnt to steady herself, then walks towards the bathroom."

                            "Cum in her mouth.":
                                me "Here we go! Open up for me Mom!"
                                "You squeeze down on her boobs and give a few more thrusts until you're right on the edge. Mom opens her mouth and sticks her tongue out, ready to catch your load."
                                show mom tit13 at right
                                $ momO.inc_cum_mouth()
                                "Right before you start to cum you thrust all the way up, sticking the tip of your cock into her waiting mouth. She lets out a muffled gasp as the first blast of semen shoots out across her tongue."
                                "You both hold still as you finish cumming in your Mom's mouth. As you start to relax you feel her tongue dart across the tip of your cock, sending a sudden shiver of pleasure down your spine."
                                me "Holy crap! Easy there Mom!"
                                $ momO.inc_cum_swallow()
                                "You let go of your mom's tits and she sits back, pausing for a moment to swallow your load before she speaks."
                                if momO.cumslut:
                                    mom "Mmm, I just couldn't waste a single drop of your delicious cum sweetheart. I hope you didn't mind."
                                    me "No, it just suprised me a little bit. It felt amazing."
                                else:
                                    mom "Sorry, I just wanted to make sure I got it all."
                                    me "I think you did a pretty good job."
                                show mom casual at right
                                "You sit back on the couch, sighing as you land. Mom sits beside you, starting to button up her shirt again. You watch TV together for another hour or so before you say goodbye."

                            "Cum down her throat." if momO.slut_score > 90:
                                me "Here we go! Open up wide for me like a good slut!"
                                "You let go of her boobs and take a step forward, pressing the tip of your cock against her lips. Your Mom opens her mouth wide, and you slide yourself as far down her throat as you can."
                                me "Ya, just like that. Good girl!"
                                show mom tit15 at right
                                "You pump your hips back and forth, sliding in and out of your mom's wet mouth. She looks up at you as she starts to lick the bottom of your cock as you fuck her throat."
                                $ momO.inc_cum_mouth()
                                $ momO.inc_cum_swallow()
                                "It doesn't take much to push you over the edge completely, and you grab onto her head and hold her tight to your hips as you start to unload right down her throat into her stomach."
                                "You wait until you're completely done, then slowly slide out and sit back down on the couch with a sigh. Mom gives a single cough, then breathes heavily to catch her breath."
                                if momO.cumslut:
                                    mom "Wow, you felt so nice and big in my throat when you finished. Your cum really felt good sliding down into me too."
                                    "She licks her lips and sighs happily."
                                else:
                                    mom "Wow, I could really feel that..."
                                me "Whew, that was great Mom. Now, should we get back to watching some TV?"
                                show mom casual at right
                                "She nods and gets back onto the couch, doing up her shirt again. You watch TV again for another hour, then say goodbye."

                        "You stay on the couch for a few more minutes catching your breath, then get up and go about your day."
                    "Let her keep going.":
                        #Just keep going.
                        me "Oh ya, that feels great Mom. Just keep going like that."
                        mom "I can feel you twitching sweetheart. When you're ready to finish just let me know, okay?"
                        me "Sure thing Mom. Wow..."
                        "You sit back and enjoy the feeling of her warm wet tits sliding up and down your shaft. After a few minutes you can feel your orgasm approaching."
                        me "Okay, here I come Mom!"
                        mom "Just let it all out for me, anywhere you want."
                        menu:
                            "Cum on tits.":
                                me "Just keep going, I'll cum on your tits."
                                "She nods and speeds up, titfucking you until you start to climax. You moan softly as you start to spray your load between your mom's cleavage, shooting some up and out over the top of her breasts."
                                if momO.cumslut:
                                    mom "There we go, give it all to me. I want you to give me as much cum as you can, right on my tits."
                                else:
                                    mom "There it is. Good boy, just let it all out. That's it."
                                show mom tit8 at right
                                $ momO.inc_cum_over()
                                "She keeps stroking you off with her breasts until you're completely spent, then sits back and looks down at your work."
                                mom "Wow, that certainly was a lot..."
                                me "That felt great Mom. Thanks."
                                mom "No problem sweetheart, I'm glad I could help you feel good. Now I should go get this cleaned up."
                                hide mom
                                "She stands up, running a finger along the underside of her breasts to catch a trickle of cum as she heads to the bathroom."
                                "You pull your pants up and stay on the couch for a few minutes, catching your breath before you go about your day."
                            "Cum on face.":
                                me "Your face, I want to cover your face."
                                "She nods and speeds up, titfucking you until you start to climax. When you do she holds onto your cock and points it up, tilting her face back so you can spray your load all over it."
                                "You let out a soft moan as you start to cum. Mom strokes your shaft slowly with one hand while she guides your cock left and right, getting some of your semen over every inch of her face."
                                show mom tit9 at right
                                $ momO.inc_cum_over()
                                "When you're finally done she lets go, using her thumb to wipe the last few drops from the tip of your cock. You sit back with a sigh and look down at her, admiring your work."
                                mom "Wow, that was certinaly a lot..."
                                if momO.cumslut:
                                    "She runs a finger below an eye, wiping away some of your cum. She looks at her finger for a moment, then licks your sperm off of it while she looks up at you."
                                else:
                                    "She runs a finger below an eye, wiping away some of your cum."
                                me "That was great. Thanks Mom."
                                mom "No problem, I'm glad you had a good time. Now I should go get this cleaned up."
                                hide mom
                                "You pull your pants up and stay on the couch for a few minutes, catching your breath before you go about your day."

                            "Cum in her mouth.":
                                me "Right in your mouth Mom, I want to cum in your mouth."
                                show mom tit10 at right
                                "She nods and speeds up, titfucking you until you start to climax. As you start to cum she leans far down, slipping the tip of your cock inside her mouth while her tits sandwhich your shaft."
                                "Mom gives a muffled moan as you start to unload into her mouth, spraying your seed across her tongue."
                                show mom tit5 at right
                                $ momO.inc_cum_mouth()
                                $ momO.inc_cum_swallow()
                                "When you're done she slips you out of her mouth carefully and pauses for a moment to swallow it all."
                                mom "Wow, that was certainly a lot..."
                                me "You did a great job Mom, that was amazing."
                                show mom casual at right
                                "She licks her lips quickly and smiles at you, standing up and buttoning up her shirt."
                                mom "No problem, I'm glad you had a good time."
                                hide mom
                                "She sits back beside you on the couch while you pull up your pants. You watch TV together for another hour before saying goodbye to each other."
            else:
                mom "Just let me know when you're going to cum, okay?"
                me "Ya, sure thing."
                "Your mom keeps titfucking you, picking up speed as she goes. After a while she pauses and holds her breasts tight in each hand, then rubs them in opposite directions."
                "The feeling of her warm soft tits is enough to bring you right to the edge of climaxing."
                mom "Oh, I can feel you twitching. Almost there?"
                me "Ya, I'm almost there. Ah!"
                show mom tit6 at right
                "Mom keeps stroking your cock with her tits until the last moment, then pulls off and grabs your shaft. She strokes you off with one hand, and wraps the other around your tip as you start to cum."
                mom "There we go, that's a good boy."
                "She doesn't stop until you've fired off every last bit of sperm into her hand, then she slows down and lets go of your shaft. Mom peels her other hand off the tip of your cock, careful not to let any of your spunk drip onto the floor."
                mom "Well I hope you had a good time sweetheart, I've got to go get cleaned up."
                "She stands up and bends towards you, giving you a quick peck on the cheek. Her large warm tits dangle in front of you while she does so."
                hide mom
                "Then she heads off towards the bathroom as you pull up your pants and catch your breath. After a few minutes you get up and go about your day."

            $ mom_hub.inc_level(3)
            $ momO.change_resist(-mom_hub.use_red(3,momO.resist_score))

        "Ask for a blowjob." if momO.slut_score > 70:
            "After a few minutes of watching TV you turn to your mom and pull your pants down, letting your hard cock spring up."
            me "Hey Mom, could you take care of this for me?"
            mom "Hmm? Oh, sure."
            "She reaches over and wraps her hand around your cock, stroking it gently while she watches TV."
            me "It would really speed things along if you sucked me off a little."
            "She thinks for a moment, then nods and stands up."
            mom "In that case, let me get rid of all of this. I'm sure that will speed things along even more."
            show mom blow10 at right
            "She strips off her shirt, then her pants, and finally drops her bra onto the floor beside your feet. Wearing nothing but her panties she drops to her knees in front of you on the couch, running her hands up your inner thigh."
            mom "Alright, lets see what we can do about this."
            show mom blow11 at right
            $ momO.inc_blow()
            "Mom runs her tongue from the base of your cock up to the tip. She gives it a little kiss, then changes her angle a little and starts from the bottom again. Once the whole length is nice and wet she opens her mouth and slides you in."
            me "Fuck, that feels amazing Mom."
            "Mom responds by giving you a few quick strokes with her head, making wet smacking sounds as the tip of your cock bounces off the back of her throat."
            "After that she settles down into a steady rhythm bobbing her head up and down the length of your cock, wrapping her tongue around it as she goes."
            show mom blow10 at right
            "She pops off of your shaft, stroking you off with one hand while she talks."
            mom "Do you like that honey?"
            menu:
                "Take over and skullfuck her." if momO.slut_score > 90:
                    #Hold her head and skull fuck her."
                    me "Oh ya, you're really good at that Mom. Here, I want to try something."
                    "You stand up, making your mom sit back on her ass to make room."
                    me "Just open your mouth for me, keep it just like that."
                    show mom blow14 at right
                    "Mom opens wide for you, and you plant your cock on her lips. You place your hands on her head, holding her steady as you start to slide your shaft into her mouth and down her throat."
                    me "Ahh, damn that feels good. Just stay like that for me Mom, I'll take care of myself."
                    "She grunts something, but the sound is muffled by your dick in her mouth."
                    "You start to work your hips back and forth, fucking her wet warm mouth."
                    show mom blow15 at right
                    "After a few moments she's gotten comfortable in the position, arms limp at her sides while you hold her head in place."
                    "You hold her tight and give her a series of good fast thrusts, bouncing your balls off her chin and slamming the tip of your cock down her throat. She coughs a few times as you go, spit dripping down her chin."
                    me "I like when you get messy like that Mom. Very hot."
                    "She's not in a position to answer with anything other than a series of wet smacking sounds as you skullfuck her faster. She keeps her tongue running along your shaft as you slide in and out of her though, making it feel even better."
                    "Before long you're getting close to your climax. You give a few more fast thrusts while you think about how to finish."
                    menu:
                        "Cum down her throat.":
                            me "Alright, here I cum Mom!"
                            "You hold tight onto her head and thrust forward, pushing your cock as far down her throat as you can as you start to orgasm."
                            show mom blow16 at right
                            $ momO.inc_cum_mouth()
                            $ momO.inc_cum_swallow()
                            "Her throat spasms around your shaft as you fire your load right into her stomach, but she doesn't try and push you off and the feeling just makes you feel even better."
                            "When you're done you pull out slowly, dragging your tip across her tongue as you leave. She gasps for air as soon as you're clear of her mouth, looking up at you with watery eyes."
                            mom "Wow... Just... Wow..."
                            me "That felt great Mom, you did a amazing job."
                            "She nods and wipes the spit from her chin, panting softly for a few moments to catch her breath."
                            if momO.cumslut:
                                mom "Thank you, you did too. You felt so big in my throat, I thought I was going to choke for a moment. It was worth it for all your delicious semen though."
                                "She licks her lips and sighs happily."
                                mom "I'm glad you had a good time too, I think I should go get cleaned up."
                            else:
                                mom "Well I'm glad you had a good time sweetheart. I think I should go get cleaned up."
                            hide mom
                            "She grabs her clothes from the couch beside you and heads off to the bathroom. You take a few minutes to catch your breath, then get up and go about your day."

                        "Cum on her face.":
                            me "Alright Mom, get ready! Lets cover you like a good cum slut!"
                            "You pull out of her mouth with a wet pop and grab your shaft with one hand, holding your mom's head in place with the other while you stroke yourself off."
                            show mom blow17 at right
                            $ momO.inc_cum_over()
                            "She pants softly as you start to cum, plastering her face with your semen. When you're done you let your cock fall down onto her face, dragging it around to make little wet trails."
                            mom "Wow... Just... Wow..."
                            me "That felt great Mom, you did an amazing job."
                            "You sit down on the couch and pull your pants back up, catching your breath."
                            if momO.cumslut:
                                mom "Mmm, so did you sweetheart. Your semen feels so nice and warm on my skin. I like it when you spread it around like that..."
                                "She runs her own fingers over her face, spreading your cum some more. After a few moments she licks her fingers clean and sighs happily."
                                mom "I'm glad you had a good time too. I think I should go get cleaned up now."
                            else:
                                mom "I'm glad you had a good time sweetheart. I think I should go get cleaned up now."
                            hide mom
                            "She stands up, wiping some cum off her chin as it drips down. She grabs her clothes and heads to the bathroom, and you get up and go about your day."

                "Tell her to keep going.":
                    #More blowjob stuff
                    me "Oh ya, you're really good at that Mom. Just keep going for me."
                    show mom blow11 at right
                    "She smiles and slips you back inside her mouth, swirling her tongue around your tip a few times before she slides you to the back of her throat again."
                    "For a few minutes you're both quiet, the only sound in the room is the occasional wet pop or smack as your mom blows you."
                    "Eventually you feel your climax approaching. Mom pulls off and looks up at you again."
                    mom "I can feel you twitching. Are you almost there sweetheart? You can finish anywhere you'd like."
                    "Without waiting for a response she opens wide again, plunging you down into her throat."
                    menu:
                        "Cum in her mouth.":
                            me "Keep going, I want to cum in your mouth Mom."
                            show mom blow13 at right
                            "She gives a small nods and speeds up her blowjob, quickly drawing you over the edge. You let out a quiet moan as you climax into your mom's mouth, spraying your load across her tongue."
                            "Once you're done she pulls off slowly, running her thumb along the bottom of your sensitive cock to catch the last drip of cum on it."
                            "Mom sits back and looks up at you, pausing for a moment to swallow your load before she speaks."
                            $ momO.inc_cum_mouth()
                            $ momO.inc_cum_swallow()
                            if momO.cumslut:
                                mom "Mmm, thank you sweetheart. You taste so good, I love it."
                            else:
                                mom "Wow, there certainly was a lot..."
                            me "Thanks Mom, that was amazing."
                            "She nods and stands up, grabbing her clothes from the couch."
                            mom "Any time sweetheart. I'm glad you had a good time. Now I should go get cleaned up."
                            hide mom
                            "Mom heads off to the bathroom. You pull your pants back up and relax for a few minutes to catch your breath, then get up and go about your day."

                        "Cum on her face.":
                            me "Wait, I want to cum on your face!"
                            "She gives one last pass, then pulls back and lets go of your cock with a wet pop. She grabs your shaft with one hand and starts to stroke you off."
                            if momO.cumslut:
                                mom "Go ahead, give your slutty mom just what she wants and cover her with your cum! Ah!"
                            else:
                                mom "Do it, let it all out for me!"
                            show mom blow12 at right
                            $ momO.inc_cum_over()
                            "Her hand sliding up and down your slippery cock pushes you right over the edge, and you give a soft moan as you start to fire your load across her face. She turns left and right slowly, making sure you cover the entire thing."
                            "When you're done she sits back and looks up at you, running a finger along her chin to catch a drip of cum."
                            mom "Wow, that certainly was a lot..."
                            me "Thanks Mom, that was amazing."
                            "She nods and stands up, grabbing her clothes from the couch."
                            mom "any time sweetheart. I'm glad you had a good time. Now I should go get cleaned up before someone sees me like this."
                            hide mom
                            "Mom heads off to the bathroom, and you pull your pants back up. You spend a few minutes catching your breath, then get up and go about your day."

            $ mom_hub.inc_level(4)
            $ momO.change_resist(-mom_hub.use_red(4,momO.resist_score))

        "Fuck her." if momO.slut_score > 80:
            me "Hey Mom, if you aren't too busy..."
            "You pull your pants down, letting your hard cock spring up."
            me "How about me and you have some fun. I'm feeling like a quick fuck right now."
            show mom strip9 at right
            "Mom looks over at you, eyes running up and down your body for a split second. She nods and stands up, unbuttoning her shirt and peeling it off."
            mom "Keep an ear out for Lily though. We don't want her catching us."
            show mom nightstrip3 at right
            "You watch your mom strip down until she's wearing nothing at all while you think about how to fuck her."
            menu:
                "Have her ride you.":
                    #Sex
                    me "Alright Mom, climb on."
                    show mom fuck30 at right
                    $ momO.inc_sex()
                    "You lean back on the couch and wait while your mom gets onto the couch and straddles you. Her large breasts hang down into your face while she lines your shaft up with her pussy."
                    "She gasps as you lean forward and plant your lips on one of her nipples. You suck on it gently, flicking your tongue across the sensitive tip."
                    mom "Oh [inputName]!"
                    "You keep sucking on her breast and plant your hands on her hips. With a gently push you encourage her to sit down, sliding your cock into her wet pussy."
                    "She waits for a moment, sitting on your shaft and moaning softly. You grab her ass and give her a little push to get her started sliding up and down."
                    mom "Oh [inputName], that feels so good."
                    "You let go of her tit after running your tongue in a circle around her nipple."
                    me "You feel great too Mom, fuck you're wet."
                    show mom fuck31 at right
                    "You squeeze tight on her ass and drive it up and down. She moans louder this time, wrapping her arms around your back."
                    mom "It just feels so good to have you inside me. So warm."
                    "You give her ass a smack, then go back to driving it up and down as fast as she can manage."
                    "Mom's tight pussy twitches around your cock as she moans and gasps. Her fingers dig into your back as she rides you."
                    me "Oh ya, cum for me Mom! Just like the fucking slut you are!"
                    "She takes a few shuddering breaths, legs spasming against yours. She tries to slow down, but you keep pushing her hips up and down."
                    mom "Oh god! Oh god!"
                    "Her cunt seems even wetter now, and the way she twists and moves drives you right up to your orgasm."
                    menu:
                        "Cum inside her.":
                            me "Fuck ya, here we go!"
                            "You keep your hold on her hips, forcing her to move even as she's recovering from her climax. After a few more strokes you're ready to cum."
                            "You push her down hard onto your shaft, making her give another loud gasp. You hold her there while you fire your load deep inside of her cunt."
                            if momO.preg_response_ok():
                                if momO.cumslut:
                                    mom "Oh god, yes! Just pump me full of it!"
                                else:
                                    mom "Oh god..."
                            else:
                                mom "Wait! You might get me pregnant!"
                            "You wait until you've fired off everything that you can, then let go of her hips and relax. Mom leans against you, panting in your ear for a few minutes."
                            me "Damn, that was great Mom."
                            show mom fuck32 at right
                            $ momO.inc_cum_inside()
                            "She nods, and you feel your hot semen dripping out of her pussy onto your thigh."
                            "When she's recovered she slides up and off your shaft, then rolls over and collapses on the couch beside you."
                            me "You should probably get cleaned up before Lily wanders in. We wouldn't want her to see her mother like this."
                            hide mom
                            "She nods again and takes a few more deep breaths before getting up and collecting her clothes from the floor. She heads off to the bathroom, cum trickling down her leg as she goes."

                        "Cum on her face.":
                            me "Fuck, I'm almost there Mom. I want to cover your face with cum."
                            "You give her a few more thrusts, then let go of her hips and let her slide off."
                            "Without a word your mom falls to her knees in front of you, tilting her head to look at you."
                            show mom fuck33 at right
                            $ momO.inc_cum_over()
                            "You sit on the couch and stroke yourself off to completion, spraying your load all over her face. She pants softly as you cover her with spunk, and you land some in her open mouth."
                            if momO.cumslut:
                                mom "Mmm, yes! Thank you sweetheart, that feels amazing."
                            else:
                                mom "Oh god..."
                            "You wipe the tip of your cock off on her chin and sit back with a heavy sigh."
                            me "Damn, that was great Mom."
                            "She nods, swallowing the little bit of cum that landed in her mouth."
                            me "You should probably get cleaned up before Lily wanders in. We wouldn't want her to see her mother like this."
                            hide mom
                            "She nods again and takes a few deep deep breaths before getting up and collecting her clothes from the floor. She heads off to the bathroom, wiping your cum away from her eyes."

                        "Cum on her body.":
                            me "Fuck, I'm almost there Mom. I want to cum all over you!"
                            "You give a few more thrusts, then let go of her hips and let her slide off."
                            "Without a word your mom falls to the ground and sits back, looking up at you while she waits for you to cum."
                            show mom fuck34 at right
                            $ momO.inc_cum_over()
                            "You sit forward on the couch and stroke yourself to completion, spraying your load all over her body. You start at the top, sending a few pulses over her face, and work your way down to her pussy."
                            "When you're done, she lies back on the ground, covered in your cum and panting softly."
                            if momO.cumslut:
                                mom "Mmm, yes! Thank you sweetheart, that feels amazing."
                            else:
                                mom "Oh god..."
                            "You lean back and give a heavy sigh, feeling content."
                            me "Damn, that was great Mom."
                            "She gives a weak nod from the floor, still breathing heavily."
                            me "You should probably get cleaned up before Lily wanders in. We wouldn't want her to see her mother like this."
                            hide mom
                            "She nods again and gets to her feet. She collects her clothes from the floor and heads off to the bathroom, wiping up some of the cum that drips down her body as she goes."

                    "You pull your pants up again and relax on the couch for a few minutes, then get up and go about your day feeling much more relaxed."

                "Fuck her doggy style." if momO.slut_score > 100:
                    #Sex:
                    "You get up from the couch, wrapping your arms around your mom's naked body. She sighs happily as you run your fingers over her skin."
                    mom "Oh [inputName]..."
                    me "You look amazing Mom. So goddamn sexy."
                    "You end up behind her, cock brushing against her ass. You reach around and grab her tits, kneading them gently."
                    "Mom moans softly as you play with her body, rolling her hips against yours to grind her ass against your hard shaft."
                    mom "[inputName], I think I need you."
                    show mom fuck35 at right
                    $ momO.inc_sex()
                    "You pinch her nipples, making her gasp, then let go and push on her shoulders gently. She bends over easily, planting her hands on the seat of the couch."
                    me "There we go, lets give you what you want then."
                    "You hold onto your shaft and line it up with her slit. You flick your tip up and down the length of it, feeling how wet she's gotten."
                    "With one smooth motion you push yourself into her pussy, sliding in as far as you can go. Mom moans and pushes her hips back to meet you."
                    me "Wow, you're so wet Mom. You really did want this."
                    mom "Mmhm, you feel so warm inside me. Ah, keep going please."
                    "You slide yourself in and out of your mom's tight wet cunt, playing with her ass as you fuck her from behind."
                    "After a few minutes you notice her breath getting faster and she starts to push her hips back to meet yours."
                    me "Almost there Mom?"
                    mom "Ah! Ya, I'm almost there."
                    me "Good, cum like a little slut for me then."
                    "You grab her hips and fuck her as fast as you can, making her scream and pant as you push towards her orgasm."
                    mom "Fuck! Ah!"
                    "Mom quivers against you as she climaxes, her pussy twitching around your hard shaft. You keep fucking her, pounding her cunt as she moans and driving towards your own orgams as well."
                    menu:
                        "Cum inside her.":
                            me "Here I cum Mom!"
                            "She responds with a gasp and a moan as you slam deep inside of her again, holding yourself tight against her ass while you start to cum. You keep yourself there as you fire off your load deep into her cunt."
                            show mom fuck37 at right
                            $ momO.inc_cum_inside()
                            "For a few moments you're both still, then you step back and let your softening dick slip out of her pussy. Mom slumps to her knees, chest resting on the couch as she breathes heavily with your cum trickling down her leg."
                            "You sit down on the couch next to her with a heavy sigh, feeling content."
                            me "Damn, that was great Mom."
                            if momO.preg_response_ok():
                                if momO.cumslut:
                                    mom "Ah... It seems like you really tried to get me pregnant. It's so thick, so warm..."
                                else:
                                    "She lifts her head and gives a weak nod, still panting heavily."
                            else:
                                mom "It was but... We need to be more careful if you don't want me on my birth control. You don't want me to get pregnant, right?"
                            me "You should probably get cleaned up before Lily wanders in. We wouldn't want her to see her mother like this."
                            hide mom
                            "She nods again and gets to her feet. She collects her clothes from the floor and heads off to the bathroom, one hand between her legs to catch your sperm as it drips out of her."

                        "Cum on her face.":
                            me "Here I cum Mom! I want you to take it on your face!"
                            mom "Ah! Whatever you want!"
                            "You give her a few more thrusts until you're ready to finish, then pull out and wait for her to get in position."
                            "Mom drops to the floor and turns around, sitting against the couch as you step forward and start to cum over her face."
                            if momO.cumslut:
                                mom "Ah! It's so nice and warm! Give it all to me sweetheart!"
                            else:
                                mom "Ah! It's so warm..."
                            show mom fuck38 at right
                            $ momO.inc_cum_over()
                            "You spray your load over as much as you can, from her forehead to her chin. When you're done you rest the tip of your cock against her lips, and she licks it clean for you."
                            me "Damn, that was great Mom."
                            "She nods and takes a few deep breaths."
                            me "Now you should probably get cleaned up before Lily wanders in. We wouldn't want her to see her mother like this."
                            hide mom
                            "She nods again and gets to her feet while you sit down on the couch with a heavy sigh. She collects her clothes from the floor and heads off to the bathroom."

                        "Cum on her ass.":
                            me "Oh ya, you dirty fucking whore. Lets cover that ass of yours!"
                            "You give her a few more fast thrusts until you start to cum, then pull out and stroke yourself off onto her ass cheeks."
                            "Mom gasps as each new pulse of hot cum lands on her cheeks, legs shaking from her recent orgasm."
                            mom "Ah! There's so much..."
                            me "That's right, you did a great job."
                            show mom fuck36
                            $ momO.inc_cum_over()
                            "You keep stroking yourself until you're completely finished, then wipe the last few drops off onto her ass and step back to admire your work."
                            me "Now you should probably get cleaned up before Lily wanders in. We wouldn't want her to see her mother like this."
                            hide mom
                            "Mom nods and stands up, using one hand to catch any of your sperm that runs down her legs. She collects her clothes and heads off to the bathroom while you sit down on the couch with a heavy sigh."

                    "You pull your pants up again and relax on the couch for a few minutes, then get up and go about your day feeling much more relaxed."

                "Anal her." if momO.slut_score > 130 or (momO.anal and momO.slut_score > 80):
                    #Sex:
                    "You get up from the couch, wrapping your arms around your mom's naked body. She sighs happily as you run your fingers over her skin."
                    mom "Oh [inputName]..."
                    me "You look amazing Mom. So goddamn sexy."
                    "You end up behind her, cock brushing against her ass. You reach around and grab her tits, kneading them gently."
                    "Mom moans softly as you play with her body, rolling her hips against yours to grind her ass against your hard shaft."
                    mom "[inputName], I think I need you."
                    show mom fuck35 at right
                    "You pinch her nipples, making her gasp, then let go and push on her shoulders gently. She bends over easily, planting her hands on the seat of the couch."
                    me "How about we try something a little more adventurous this time."
                    "You spit into your hand, then stroke your shaft to get it wet and slippery. Mom looks over her shoulder at you while you line your cock up with her asshole."
                    mom "What do you mean?"
                    me "You hold onto her hips with one hand and use the other to guide your shaft as you press your head against her tight ass."
                    mom "Oh. Oh!"
                    show mom fuck39 at right
                    $ momO.inc_sex()
                    "It takes a moment, but you're able to slide your wet cock into your mom's ass. She gasps loudly, and you give her a few seconds to get used to the feeling."
                    me "That's what I mean. Ready?"
                    if momO.anal:
                        mom "Yes, I'm ready. Give it to me [inputName], I can take it."
                    else:
                        mom "Ah... I think so."
                    "You start to slide yourself in and out of her, starting slowly and picking up speed as you go. She's incredibly tight, and it feels like she clamps down on you with each thrust."
                    me "Damn, that feels amazing Mom. You're just the perfect slut, you know that?"
                    mom "I just want you to be happy. That's all. Ah!"
                    "You give her ass a slap and speed up some more, fucking her pretty little asshole."
                    me "Well, you do a good job. Amazing tits, tight pussy, and an ass that just can't. Be. Beat."
                    "You slam yourself deep inside of her on the last few words, making her yelp. When you slow down again you can feel her legs shaking against yours."
                    me "Are you going to cum? From getting your ass fucked by your son?"
                    "There's a moment of hesitation before she nods and presses her hips back against yours, helping you fuck her."
                    mom "Yes, fuck I'm almost there. Keep going please."
                    "You oblige and keep fucking her until she gasps loudly. Her ass gets tight around your cock as she cums, and the feeling is enough to push you over the edge as well."
                    menu:
                        "Cum inside her.":
                            "Without a word you push yourself deep inside your Mom, holding her tight against you as you start to cum."
                            if momO.cumslut:
                                mom "Oh shit, yes! Pump it right into me!"
                            else:
                                mom "Ah! Did you..."
                            "You finish dumping your load inside of her, then start to thrust in and out of her again. Your semen makes her ass nice and slippery, making her tight hole feel even better."
                            me "Ya, I did. I just filled you up like you wanted Mom."
                            "She nods slowly, panting for breath."
                            show mom fuck41 at right
                            $ momO.inc_cum_inside_ass()
                            "After a few more seconds of enjoying her slippery asshole you step back and slide your sensitive cock out. Almost immediately your cum starts to leak out and run down her leg."
                            me "You should probably go get cleaned up, unless you want Lily to see what a cum slut you are now."
                            hide mom
                            "Mom shakes her head and stands up, legs still shaking. She gathers her clothes as you sit down on the couch, then moves off to the bathroom."

                        "Cum on her face.":
                            me "Here we go Mom, get on your floor for me!"
                            "You give her asshole one more good thrust, then pull out and step back. Mom drops to the ground and turns around, sitting against the edge of the couch."
                            show mom fuck38 at right
                            $ momO.inc_cum_over()
                            "You stroke yourself off until you start to cum, firing your sperm across her face. You start with her forehead, then work your way down to her chin, letting the last few drops of cum drip down onto her tits."
                            me "Fuck, that was great. Here, clean me off."
                            if momO.cumslut:
                                "You step forward and present your cock to your mom. She opens her mouth and sticks her tongue out, eagerly presenting her mouth to you."
                            else:
                                "You step forward and present your cock to your mom. She hesitates for a moment, then opens her mouth so you can slip yourself inside."
                            "She wraps her tongue around your sensitive cock and runs it up and down your length while you thrust in and out of her mouth gently."
                            me "That's a good girl, you take such good care of me Mom."
                            "When you're done you step back and slip out of her mouth. She takes a few deep breaths and starts to stand up."
                            me "Now you should get cleaned up, unless you want Lily to see what a cum slut you are now."
                            hide mom
                            "Mom shakes her head and starts to gather her clothes. You sit down on the couch with a heavy sigh, feeling content, while she moves off to the bathroom."

                        "Cum on her ass.":
                            show mom fuck40 at right
                            $ momO.inc_cum_over()
                            "You give a few more deep thrusts, then pull out at the last moment and start to cum over your mom's ass cheeks. She gasps softly as each pulse of hot cum lands over her body."
                            mom "Ah! Oh god."
                            me "Fuck, that felt great. You're ass felt amazing Mom, especially when you came."
                            "She nods slowly, panting for breath."
                            mom "I had a good time too. Ah..."
                            "She leans against the couch, seemingly stunned."
                            me "You should probably go get cleaned up, unless you want Lily to see what a cum slut you are now."
                            hide mom
                            "Mom shakes her head and stands up, legs still shaking. She gathers her clothes as you sit down on the couch, them moves off to the bathroom."

                    "You pull your pants up again and relax on the couch for a few minutes, then get up and go about your day feeling much more relaxed."

            $ mom_hub.inc_level(5)
            $ momO.change_resist(-mom_hub.use_red(5,momO.resist_score))

        "Give her some serum and train her.\n-15 Influence, -2 Serum" if momO.slut_score > momO.training_threshold and (player_blue_serum + player_purple_serum + player_red_serum > 1):
            menu:
                "Train her to be a cum slut from now on." if not momO.cumslut:
                    call cumslut_descrip("Mom")
                    menu:
                        "Continue with the training.":
                            call mom_train_cumslut
                        "Change your mind and leave.":
                            return False

                "Train her to be an anal lover from now on." if not momO.anal:
                    call anal_descrip("Mom")
                    menu:
                        "Continue with the training.":
                            call mom_train_anal
                        "Change your mind and leave.":
                            return False

                "Train her to be a free use slut from now on." if not momO.freeuse:
                    call freeuse_descrip("Mom")
                    menu:
                        "Continue with the training.":
                            call mom_train_freeuse
                        "Change your mind and leave.":
                            return False

                "Train her to be an exhibitionist from now on." if not momO.exhib:
                    call exhib_descrip("Mom")
                    menu:
                        "Continue with the training.":
                            call mom_train_exhib
                        "Change your mind and leave.":
                            return False
                "Change your mind and leave.":
                    return False

        "Just chat for a while.":
            "You spend a few minutes watching TV with your mom, chatting about nothing in particular."
            return False

    return True

####################
##Nora's Hub Scene##
####################

label hub_nora:
    #TODO: make sure you head back to campus after this hub scene.
    menu:
        "Ask her to strip for you." if noraO.slut_score > 20:
            #Show off a little
            me "I've been watching you around the lab recently, and it would be nice to get a better look at you."
            nora "A better look?"
            me "Yeah, without your clothes. You're just such a good looking woman, I can't keep you out of my mind."
            "Nora thinks for a moment, looking at her work and whispering to herself. Finally she looks up at you and nods, pulling her labcoat off as she talks."
            nora "I think I'm about done here anyway, a quick break couldn't hurt."
            show nora strip1 at right
            "Nora sets her labcoat on the back of her chair, then pulls her sweater off as well. She turns left and right, letting you stare at her sizable breasts."
            me "Wow, looking very good Nora."
            nora "Thank you [inputName], I'm glad you approve."
            show nora strip4 at right
            "She turns around and undoes the zipper on her pants, sliding them down slowly and giving you a nice look at her ass."
            show nora strip10 at right
            "Nora lets them drop to the ground once she's lowered them past her knees, then kicks them to the side and stands up to face you again. She looks amazing in just her underwear and high heels."
            if noraO.slut_score > 30:
                nora "Nora gives a few slow turns, placing her hands on her tits and ass as she goes to show them off."
                show nora strip22 at right
                "After a few turns she stops and looks at you, bending forward with her breasts in her arms."
                nora "So, anything else you would like me to do?"
                menu:
                    "Keep showing off for me.":
                        me "Keep showing off for me, I want to see you from every angle."
                        "She nods and straightens up, then turns around and bends over again. She spreads her legs a few steps and reaches down with her hands, running them along her legs."
                        show nora strip10 at right
                        "Nora stops with her body parallel with the ground, ass stuck high in the air and hands on her legs for support. She wiggles her butt at you."
                        "Then she slowly stands up, once again caressing her legs as she goes."
                        nora "So you like watching me like this?"
                        me "Oh ya, you're super hot Nora."
                        show nora strip23 at right
                        "She turns back to you and smiles, cupping a breast in one hand and rubbing it gently."
                        nora "Mmm, I'm glad you think so. We spend so much time working here in the lab, it's good to have a chance to relax. It's good to be wanted."
                        show nora strip24 at right
                        "She puts her arms above her head, stretching and taking a deep breath, both of which serve to push her tits out and make them look even larger."
                        "With a sigh she finishes the stretch, placing her hands on her hips while she thinks for a moment."
                        show nora strip10 at right

                    "Touch yourself.":
                        me "I want to watch you touch yourself."
                        "Nora bites her lip and nods. She straightens up and runs a hand down the length of her body, caressing her chest, stomach, leg, and finally brushing it over her crotch."
                        show nora mast6 at right
                        "She spreads her legs a little, standing in front of you while she runs a finger along her pussy through her underwear. You see the fabric stick to her cunt as it gets wet."
                        me "Perfect. Just pull your underwear to the side now."
                        show nora mast7 at right
                        "She nods and hooks her panties with a finger, pulling them to the side and giving you a clear view of her pussy. She runs her finger over it again, pausing to circle her clit a few times."
                        nora "Oh... So you like watching me like this?"
                        me "Oh ya, you're super hot Nora."
                        "She sighs and slides a finger into herself, fingering herself slowly."
                        nora "Mmm, I'm glad you think so. We spend so much time working here in the lab, it's good to have a chance to relax. It's good to be wanted."
                        show nora mast8 at right
                        "Her other hand drops to her waist and she starts to rub her clit while she fingers herself. She takes a sudden sharp breath, and you can see her legs quiver."
                        me "Almost there?"
                        "She nods wordlessly and keeps going, finger pumping in and out, in and out. A second later she tenses up and shakes like a leaf, then relaxes and lets out a long sigh."
                        nora "There we go. Ah..."
                        me "Good job Nora. That was great."
                        show nora strip10 at right
                        "She takes a moment to recover, then straightens out her underwear and looks at you, hands on her hips while she thinks for a moment."

                if noraO.slut_score > 50:
                    #Show off other outfits
                    nora "If you'd like to... see some more, I think I'd be okay with that. I've got some outfits here that I keep around just in case."
                    me "Just in case of what?"
                    nora "Well sometimes I need to stay overnight to get something done, and it's nice to have a fresh change of clothes."
                    me "Okay, well lets see what you have."
                    "Nora pulls out a collection of outfits, holding them up for you to take a look at one at a time."
                    nora "So what do you think? Anything you'd like me to try on?"
                    menu:
                        "Black Babydoll.":
                            me "How about that black lingerie, I'm sure you look amazing in that."
                            nora "This? Sure. I wanted something a little more comfortable to sleep in, and it just seemed so cute."
                            "Nora strips down and slides on the babydoll, then thin panties and fishnet stockings. She finishes by pulling on the lace gloves and placing her glasses on her desk."
                            show nora strip25 at right
                            nora "Well? Does it suit me?"
                            "She turns a little, showing off her body to you. You can see the shape of her tits through the translucent fabric."
                            me "You look fantastic in it Nora. Turn around for me."
                            show nora strip26 at right
                            "She nods and turns around, looking over her shoulder at you while you check out her ass."
                            me "Beautiful. You're beautiful Nora."
                            nora "Stop, you're making me blush."
                            "She gives her ass a light smack, making it jiggle a little, then turns around again."
                            show nora strip25 at right
                            nora "That was fun, but I should be getting back to work."
                            me "Sure. Thanks Nora, I had a great time."
                            show nora work at right
                            "Nora strips out of her lingerie and gets back into her work clothes."
                            nora "Actually, if you have some time to spare I could use some help. Could you take inventory in the back?"
                            me "Uh, sure. I guess I can do that."
                            "You spend another hour with Nora, counting the stock in the lab and reporting it back to her. Once you're done you say goodbye and head back to ground level."

                        "Swimsuit.":
                            me "Is that a swimsuit? I'd like to see you in that."
                            nora "Sure. One moment."
                            show nora strip27 at right
                            "Nora strips down and slides the swimsuit on. It's black and orange, patterned with tiger strips, and has a large cut away in the middle showing off her cleavage."
                            nora "There. I've got to be a little careful, it doesn't exactly have much holding it on."
                            "She runs a finger from the nape of her neck, down the exposed patch of skin, between her cleavage and down to her belly button."
                            nora "It seems worth it though, it feels so sexy."
                            me "It looks sexy too. Turn around so I can take a look at you from behind."
                            show nora strip28 at right
                            "She nods and spins, bending over and sticking her butt out towards you. The swimsuit has a tight curve to it, and barely covers her ass at all."
                            me "Wow, you look fantastic in it Nora. You've got a top notch ass."
                            "She bends over a little and wiggles it at you."
                            nora "You think so? Thank you."
                            show nora strip27 at right
                            "She reaches back and gives it a light tap, making it jiggle. After that she turns around again to face you."
                            nora "Now I should really be getting back to work, you've gotten me distracted."
                            show nora work at right
                            "She pulls off the swimsuit, quickly getting dressed again."
                            nora "Actually, if you aren't doing anything important right now, I could use a hand. Could you go and take inventory in the back for me?"
                            me "Uh, sure. I guess I can do that."
                            "You spend another hour with Nora, counting the stock in the lab and reporting it back to her. Once you're done you say goodbye and head back to ground level."

                        "Naked.":
                            me "I think I just want to see more of you. Take off everything for me."
                            show nora strip6 at right
                            "Nora thinks about it for a moment, then reaches behind her back and undoes her bra. She lets it fall forward and off, then hooks her panties with her thumbs and plays with the waistband for a moment."
                            nora "I spent all that money on lingerie, and you just want to see me naked. Almost seems like a shame."
                            show nora strip5 at right
                            "She pulls her panties down past her thighs and lets them fall the rest of the way to the ground."
                            nora "Almost."
                            me "You don't need any of that stuff to look beautiful. I like you just the way you are. Great tits, amazing ass, you've got it all Nora."
                            show nora strip29 at right
                            "She smiles and turns around for you, spreading her legs a little so you can see her pussy from behind."
                            nora "Stop, you're making me blush."
                            "She gives her ass a quick slap, then turns around again and cups her breasts in her hands."
                            nora "There, I think that's all I have to show you then. I really should be getting back to work."
                            show nora strip10 at right
                            "She collects her underwear and starts to put it all back on."
                            me "Thank you Nora, I had a great time."
                            nora "Any time. Now, if you have time to spare I could use some help. That should make up for distracting me."
                            me "Right. Sure. What do you need."
                            show nora work at right
                            "She pulls her labcoat back on and sits down at her desk."
                            nora "Just do an inventory of the back room for me. Some of my counts must have been off earlier today."
                            "You spend another hour with Nora, counting the stock in the lab and reporting it back to her. Once you're done you say goodbye and head back to ground level."

                    #End the show
                else:
                    nora "Well that was fun [inputName], but I think I should be getting back to work. Since you're here, do you think you could help me with some inventory?"
                    "She picks up her pants and sits down while she slides them on."
                    me "Uh, sure thing Nora."
                    show nora work at right
                    "You spend another hour with Nora, counting the stock in the lab and reporting it back to her. Once you're done you say goodbye and head back to ground level."
            else:
                nora "There you go, take a good look."
                show nora strip21 at right
                "She spins on the spot slowly while you ogle her, keeping her hands behind her back and thrusting her chest forward to make it even more prominent."
                "After a few turns she stops and looks at you."
                nora "Now I should really be getting back to work, if you don't mind."
                me "Right, of course. Thanks Nora."
                nora "Any time. Now if you've got a few spare minutes, there's some paperwork that you could help me out with."
                show nora work at right
                "Nora slips on her pants again, then her sweater and labcoat."
                me "Sure, lets take a look."
                "You sit down across the desk from Nora and help her fill out a few forms. Once that's done you say goodbye and head back to the ground level on campus."
                #End the show

            $ noraO.inc_naked()
            $ nora_hub.inc_level(1)
            $ noraO.change_resist(-nora_hub.use_red(1,noraO.resist_score))

        "Ask for a handjob." if noraO.slut_score > 35:
            "You rub your hard shaft through your pants, letting Nora watch you for a moment."
            me "Well I've been feeling a little pent up, and I don't have any way to really take care of it. It would be great if you could help me get off."
            if noraO.slut_score > 50:
                nora "Sure, I can spare a few minutes. Here, jump up."
                "She slides her chair back and pats the desk, making room for you to sit down in front of her."
                show nora hand6 at right
                "You drop your pants and underwear, then get onto the desk with your hard cock standing ready. Nora watches you get in position, then takes the palm of her hand and licks it a few times before wrapping it around your shaft."
                $ noraO.inc_hand()
                me "Oh fuck, that feels great."
                "You shiver slightly as Nora's wet warm hand starts to stroke you off. She smiles at you and runs her other hand up and down your thighs."
                nora "Good, just enjoy it. Give me a little warning before you finish, okay?"
                me "Sure thing Nora."
                "You lean back on Nora's desk and let out a sigh. For a few minutes the only sound in the lab is the wet smacking of her hand as it slides up and down your cock. When it starts to get a little dry, she pauses and licks her palm again."
                "After a little while you feel your orgasm approaching. You sit forward on the desk as you start to tense up."
                me "Here we go Nora!"
                nora "Let it all out for me, you deserve it. Where do you want to finish?"
                # Lets you cum somewhere else
                menu:
                    "Tits":
                        me "Your tits. All over your tits."
                        "She nods and lets go of your cock for a moment. With a few quick movements she pulls her sweater and bra up and over her breasts, letting them fall free in front of you."
                        "That done she grabs your cock again, stroking you as fast as she can manage as you start to cum."
                        show nora hand9 at right
                        $ noraO.inc_cum_over()
                        "You let out a quiet moan and grip the edge of her desk as you climax, spraying your load over the curves of Nora's boobs. She keeps jerking you off until you're done completely, then lets go and slides her chair back."
                        if noraO.cumslut:
                            nora "Well thank you [inputName], look at everything you gave me."
                            "She uses her finger to scoop up some of your cum from the slope of her breasts, then licks it clean."
                            "She savours the taste for a few moments, then wipes her hand on her pants and pulls her bra and sweater back down into place."
                        else:
                            nora "There we go, all done."
                            show nora work at right
                            "She wipes her hand onto her pants, then pulls her bra and sweater back down into place."
                        me "Ah, thanks Nora. That was great."
                        nora "I'm glad you had a good time. Now I should really get back to work."
                        "You pull your pants up again and head towards the door of the lab."
                        nora "Actually, if you've got a few free minutes I could use a hand with taking inventory."
                        me "Uh, sure. I guess I can."
                        "You spend another hour with Nora, counting the stock in the lab and reporting it to her. When you're done you both head up to ground level and say goodbye."

                    "Face":
                        me "Right on your face."
                        "She nods and keeps going, stroking you as fast as she can manage. After a few passes with her wet hand you tense up and start to cum."
                        show nora hand7 at right
                        $ noraO.inc_cum_over()
                        "You grip the edge of Nora's desk and give a soft moan as you start to fire off your load. Nora points your cock at her face, moving it a little between each new pulse to make sure you cover everything."
                        "She keeps sliding her hand along your shaft until you're completely spent, then lets go carefully and wipes her thumb over your tip to get the last few drips of cum off."
                        if noraO.cumslut:
                            nora "Mmm, thank you [inputName]. Your cum feels so nice and warm."
                            "She runs a finger along her chin, catching a drip of sperm before it can fall onto her sweater. She licks the finger clean, closing her eyes and savouring the taste."
                        else:
                            nora "Wow. I hope I got it all."
                            "She runs a finger along her chin, catching a drip of sperm before it can fall onto her sweater."
                        me "Ah, thanks Nora. That was great."
                        "Nora nods and slides her chair back, making room for you to stand and pull up your pants."
                        nora "I think I'm going to have to go and get cleaned up. I'll be back in a few minutes."
                        show nora hand8 at right
                        "She gets up and walks over to the door, using a tissue to wipe your cum off her face as she goes. Before she opens the door she pauses and turns back."
                        nora "When I'm gone, could you do some inventory for me? It would really be a huge help."
                        me "Uh, sure. I guess I can spare a few minutes."
                        show nora work at right
                        "You get started counting the stock in the lab. A few minutes later Nora comes back, face all cleaned up, and starts to record the numbers. After an hour of work you both head up to ground level and say goodbye."

                    "Mouth" if noraO.slut_score > 80 or noraO.cumslut:
                        me "Open up, I want to cum in your mouth."
                        "She nods and strokes you faster, leaning forward in her chair and opening her mouth wide. She places the tip of your cock on her bottom lip, licking you gently as she jerks you off."
                        "You let out a soft moan and grip her desk as you start to cum. She gasps as the first pulse of hot semen lands on her tongue, but doesn't move her head back until you've let everything out."
                        "When you're completely spent she lets go of your shaft and slides her chair back."
                        me "Damn, that was great. Open up for me, I want to see."
                        show nora hand10 at right
                        $ noraO.inc_cum_mouth()
                        $ noraO.inc_cum_swallow()
                        "Nora opens her mouth, running her tongue through the puddle of white inside as you watch."
                        me "Good girl, now swallow."
                        "Nora closes her mouth and you can see her throat bob as she drinks your cum down. When she's done she opens up and takes a deep breath."
                        nora "There, all done. Now, I had some work to get back to."
                        show nora work at right
                        "You hop off of Nora's desk and pull your pants back up. Nora slides her chair back in and pulls a few papers towards her, getting right into it."
                        me "That was great Nora, thanks. Good luck with the work."
                        nora "Any time [inputName]. See you later."
                        hide nora
                        "You leave the lab and head back to the center of campus."
            else:
                "Nora thinks for a long few moments, staring at the bulge in your pants. Finally she nods and slides her chair back."
                nora "Fine. Sit on the desk and I'll take care of it."
                "You drop your pants and underwear, then sit down on Nora's desk in front of her. She stays seated, reaching out with one hand and gently wrapping it around your cock."
                me "Ah, that feels great. Thanks Nora."
                show nora hand6 at right
                "She just nods and starts to stroke you off. Her other hand comes up and massages your balls lightly."
                "For a few minutes there's silence in the lab as she slides her warm soft hand along your shaft. Eventually your precum drips down onto her hand, and she spreads it around to get you slippery."
                me "Oh ya, just like that. Keep going please."
                nora "Warn me before you finish."
                me "Sure thing."
                "She speeds up her handjob, and soon you start to tense up as your orgasm approaches."
                me "Here we go!"
                "Nora slides her chair to the side and keeps stroking. You let out a soft moan as you cum, firing your load past Nora and onto the lab floor. She keeps going until you're completely spent, then lets go of your hand."
                nora "There we go, that should be better now."
                "She looks at her hand, a few drips of cum still on it, and reaches forwards. She wipes it onto your pants while you're catching your breath."
                me "Much better. Thank you."
                nora "Any time. Now I've got some work to get done. If you don't have anything else to do, I could use a hand with taking inventory."
                show nora work at right
                "You stand up and pull your pants back up."
                me "I guess I have some time."
                "You spend the rest of the hour with Nora, counting the stock in the lab and reporting it back to her. Once you're done you say goodbye and head back to ground level."
                #Cum on the floor

            $ nora_hub.inc_level(2)
            $ noraO.change_resist(-nora_hub.use_red(2,noraO.resist_score))

        "Ask for a titfuck." if noraO.slut_score > 50:
            #Titfucks you for a while.
            "You reach forward and grab Nora's breasts, rubbing them through her sweater."
            me "It's a shame to not put these girls to good use. How about you get them out and take care of me for a few minutes. I'm sure your work can wait."
            show nora tit2 at right
            "Nora thinks for a moment, then nods. You let go of her tits, and she pulls her sweater and bra up to let them out."
            nora "Here, get up."
            "She taps the desk, sliding her chair back to make room for you. You slide your pants down then sit on her desk, spreading your legs to make room for her as she slides forward again."
            show nora tit3 at right
            $ noraO.inc_tit()
            "Nora takes her tits in her hands and leans forward, gently wrapping them around your dick. She starts to slide them up and down slowly, caressing you with her warm cleavage."
            me "That feels great Nora. Keep going."
            if noraO.slut_score > 70:
                #Blows you a little to lube you up
                nora "Wait, I'm sure this will help a little bit."
                show nora tit4 at right
                "She holds her tits up higher and leans down, opening her mouth and slipping you inside. She licks your cock a few times, then lets her tits go and slides down until your full length is inside of her mouth."
                me "Oh fuck..."
                "She pauses at the base of your cock, shaking her head slightly, then slides back up and off with a wet pop."
                nora "There, that'll be better."
                show nora tit3 at right
                "She grabs her tits again and sqeezes them around your wet slippery shaft. She starts to titfuck you again, her cleavage feeling even better as you slide up and down inside of it."
                menu:
                    "Take over and fuck her tits." if noraO.slut_score > 80:
                        #Take over and fuck her
                        me "Here, let me take over Nora."
                        show nora tit9 at right
                        "You stand up, pushing Nora's chair back a little bit. You grab her tits and squeeze them around your dick even tighter. Nora lets go and looks up at you, gasping softly."
                        me "There we go. Now lets give these a good fuck."
                        "You work your hips, sliding your dick between Nora's slippery tits."
                        nora "Ah, easy there."
                        me "I'm sure you can handle it Nora. Open your mouth for me, lets see if you can lick it like this."
                        show nora tit10 at right
                        "You get yourself as high up in Nora's cleavage as you can with each thrust, pushing the tip of your cock towards her mouth. Nora hunches over and sticks out her tongue, licking your tip when you come close."
                        me "Fuck yeah, just like that. Good girl."
                        menu:
                            "Cum between her tits.":
                                me "Oh, here we go Nora!"
                                "You clamp down on her breasts and give them a few more solid pumps as you start to cum."
                                "Nora gasps as you start to fire your load off between her cleavage. You keep titfucking her as you cum, spraying your load along the sides of her breasts as you go."
                                show nora tit11 at right
                                $ noraO.inc_cum_over()
                                "When you're finally done you let go and step back, enjoying the view of Nora's now sticky cum covered tits."
                                nora "Wow..."
                                me "That was great Nora. Thanks."
                                nora "Any time [inputName]. Now, I should get cleaned up and back to work. Have a good evening."
                                hide nora
                                "You pull your pants up and head out of the lab while Nora searches for some tissues. You head back towards the center of campus."

                            "Cum on her face.":
                                me "Oh, here we go Nora!"
                                "You clamp down on her breasts and give them a few more solid pumps, then press yourself tight against them as you start to cum."
                                show nora tit12 at right
                                $ noraO.inc_cum_over()
                                "Nora gasps as you start to fire off your load up onto her face. You give a few short pumps between bursts of cum until you're done, then slip out and step back to admire your work."
                                nora "Wow..."
                                me "You look great like that Nora. That felt amazing."
                                nora "Any time [inputName]. Now, I should get cleand up and back to work. Have a good evening."
                                hide nora
                                "You pull your pants up and head out of the lab while Nora searches for some tissues. You head back towards the center of campus."

                            "Cum in her mouth.":
                                me "Open up for me Nora. I'm going to cum in your mouth."
                                "You clamp down on her breasts and give them a few more solid pumps. Nora opens her mouth for you, and you place the tip of your cock on her lips as you start to climax."
                                "She gasps softly as you start to cum into her mouth, spraying your load over her tongue and back of her throat. When you're done she licks your tip a few times, getting the last drops."
                                show nora tit13 at right
                                $ noraO.inc_cum_mouth()
                                $ noraO.inc_cum_swallow()
                                "You step back and admire your work. Nora keeps her mouth open for you, flicking her tongue through the off white puddle."
                                me "You look great like that Nora. I should fill your mouth up more often, it felt amazing."
                                "Nora closes her mouth and swallows, wiping her lips with the back of her hand."
                                nora "Any time [inputName]. Now, I should really be getting back to work. Have a good evening."
                                hide nora
                                "You pull your pants up and head out of the lab while Nora grabs her pen and starts working again. You head back upstairs and towards the center of campus."

                            "Cum down her throat." if noraO.slut_score > 100:
                                me "Here I come!"
                                "You clamp down hard on her breasts and give a few more solid pumps. Right before you cum you slip up and out of her cleavage, pressing the tip of your cock against her lips until she lets you slide in."
                                show nora tit14 at right
                                $ noraO.inc_cum_mouth()
                                $ noraO.inc_cum_swallow()
                                "Nora gasps as you slam your cock all the way to the back of her throat, holding her tight against you as you start to cum."
                                me "That's it, drink it up you cum slut!"
                                "With each pulse of cum you give a small thrust, tapping the tip of your cock against the back of her mouth. She gags once but doesn't try to pull back."
                                "You place your hand on the back of Nora's head and pull her towards you, keeping her stuck on your shaft long after you've finished firing your load into her stomach."
                                me "Good girl, very good girl."
                                "Finally you let go and step back. Nora gasps for air, leaning back in her chair for support."
                                me "That was great Nora, we'll have to do it again some time."
                                nora "Ah, sure thing [inputName]. Now I've really got to get back to work. Have a good evening."
                                hide nora
                                "You pull up your pants and head out of the lab while nora grabs her pen and starts working again. You head back upstairs and towards the center of campus."

                    "Let her keep going.":
                        #Just keep going.
                        me "Keep going like that Nora, I'm going to cum soon."
                        "She nods and speeds up, pressing her breasts together just a little bit harder."
                        nora "Let it go whenever you want."
                        menu:
                            "Cum on tits.":
                                me "Alright, let me cum on your tits."
                                "Nora nods and keeps going, speeding up a little as you approach your climax."
                                show nora tit6 at right
                                $ noraO.inc_cum_over()
                                "You grip the edge of the desk as you start to cum, firing your load between Nora's tits as she titfucks you. She gasps softly as your warm cum lands on the top of her breasts."
                                "She keeps going until you're completely finished, then slows down and finally slips off of you entirely."
                                me "That felt great Nora. Thanks."
                                nora "Any time [inputName]. Now, I should really be getting back to work. Have a good evening."
                                hide nora
                                "You pull your pants up and head out while Nora searches for a tissue to clean up with. You head upstairs and back towards the center of campus."

                            "Cum on face.":
                                me "Alright, I'm going to finish on your face then."
                                "Nora nods and keeps going, speeding up a little as you approach your climax."
                                show nora tit7 at right
                                $ noraO.inc_cum_over()
                                "Right before you start to cum you slide out of her cleavage and start to stroke yourself off. Nora gasps as you start to spray your load onto her waiting face."
                                "You make sure to cover her as best you can, then lean back and admire your work."
                                nora "Wow, well done."
                                me "Thanks, that felt great Nora."
                                nora "Good, we can do it again some time. I should be getting back to work now though. Have a good evening."
                                hide nora
                                "You pull your pants up and head out while Nora searches for a tissue to clean up with. You head upstairs and back towards the center of campus."

                            "Cum in her mouth.":
                                me "Finish me off in your mouth, I want to watch you swallow."
                                "Nora nods and keeps going, speeding up a little as you approach your climax."
                                "Before you start to orgasm she slips you out from between her cleavage and rests the tip of your cock on her lips. She strokes you with her hand as you start to cum."
                                "She moans softly as your warm load shoots across her tongue, and doesn't stop jerking you off until you're completely finished."
                                show nora tit8 at right
                                $ noraO.inc_cum_mouth()
                                $ noraO.inc_cum_swallow()
                                "When you're done she lets go and slides her chair back, opening her mouth and letting you get a good look at the pool of off white cum you put there."
                                me "Damn, good job Nora. That was amazing."
                                "She closes her mouth and pauses to drink down your cum."
                                show nora work at right
                                nora "Good, we can do it again some time. I should be getting back to work now though. Have a good evening."
                                hide nora
                                "You pull your pants up and head out while Nora pulls her shirt down and gets her pen. You head upstairs and back towards the center of campus."
            else:
                #Get it over with and cum into her hand.
                "She nods, and for a few minutes you're both quiet while she services you with her tits."
                nora "Warn me before you finish, okay?"
                me "Sure thing Nora. I think I'm going to be there soon."
                "Nora speeds up, pausing for a moment to reposition her tits around your shaft. Your precum drips down your cock and spreads along her cleavage, getting it nice and slippery."
                "Soon you tense up, feeling your orgasm getting close."
                me "Alright, here we go Nora!"
                show nora tit4 at right
                "Nora keeps going until you start to cum. Then she lets go and move her hand up, cupping the tip of your cock with it. You unload into her warm hand, gripping the edge of the desk and letting out a soft moan."
                "When you're done she carefully slides her hand off and stands up, walking towards one of the lab sinks."
                nora "There we go. All done."
                show nora work at right
                "She turns on the water and starts to wash her hands while you pull up your pants."
                me "Ah, thanks Nora. That felt great."
                nora "Any time. Now I should get back to work before I fall too far behind. If you've got a few minutes, I could use some help with taking inventory."
                me "Uh, sure I guess. I'll see what I can do."
                "You spend the rest of the hour helping Nora around the lab. When you're done you both head up to ground level and say goodbye."

            $ nora_hub.inc_level(3)
            $ noraO.change_resist(-nora_hub.use_red(3,noraO.resist_score))

        "Ask for a blowjob." if noraO.slut_score > 70:
            #Starts to blow you.
            "You pull down your pants, letting your hard cock spring free. Nora watches it bounce up and down for a moment."
            me "I could use your help taking care of this. Would you mind sucking me off?"
            "Nora thinks for a moment, then nods and slides her chair back."
            nora "Here, sit on the desk."
            "You pull your pants off completely and sit down on her desk, legs spread so she can slide her chair forward again."
            show nora strip6 at right
            "Nora takes a second to pull her labcoat off, then pulls her sweater up and off as well. She reaches behind her back and unclips her bra, shrugging it forward and placing it with the rest of her clothing."
            nora "This way you won't get anything dirty."
            show nora blow12 at right
            $ noraO.inc_blow()
            "She slides her chair forward, running her hands along your thighs and up to your shaft. She gives you a few strokes, then lowers her head and licks your cock from base to tip."
            me "Ah, fuck that feels good."
            "Nora keeps licking your dick until it's wet all the way around, then wraps her lips around the tip and starts to slide it into her mouth."
            "You rest your hand on the back of her head as she starts to blow you, encouraging her to go a little deeper with each pass."
            "A few minutes pass in silence before Nora pulls off of your shaft and strokes you off with her hand while she catches her breath."
            nora "Having a good time? Anything I could do differently?"
            menu:
                "Take over." if noraO.slut_score > 85:
                    #Hold her head and skull fuck her."
                    me "Just keep your mouth open for me, I'll show you what I want."
                    "You place your hands on either side of Nora's head and pull her close. She opens her mouth for you and leans forwards, letting you slip your cock back inside."
                    show nora blow18 at right
                    "You pull her close to you on the desk and guide her head up and down, fucking her mouth for a few minutes."
                    "You let her up for air, and she pants softly with your shaft resting against her cheek."
                    me "Doing okay Nora?"
                    nora "Ah, ya. I'm fine, keep going."
                    "She opens her mouth wide again, and you grab her head and slam yourself down her throat. You speed up, grabbing her hair for control as you throat her."
                    me "Oh ya, that feels great Nora. I love feeling you wrapped around my cock, taking care of me like a good slut."
                    show nora blow19 at right
                    "Her mouth is wide open, spit running down her chin and dripping onto the floor or being flung onto her tits. All she can respond with are a few wet gurgles."
                    me "I know you like this too. Getting throated like a whore right here in the lab."
                    "More wet gargling while her eyes turn up to try and look at you."
                    me "I hope you're ready, 'cause I'm almost done!"
                    menu:
                        "Cum down her throat.":
                            "You hammer Nora's head back and forth, skullfucking her as you start to climax."
                            show nora blow20 at right
                            $ noraO.inc_cum_mouth()
                            $ noraO.inc_cum_swallow()
                            "You pull her against your waist as you fire off your first pulse of cum, pushing the tip of your cock down her throat and rubbing her nose against your pubes."
                            me "Drink it all up you fucking cum dumpster!"
                            "Nora twitches and writhes on her office chair, throat spasming around your shaft as you empty your balls into her stomach."
                            "You keep her held in place with a firm hand on the back of her head until you're completely finished. Then you let her slide slowly back up, shivering with pleasure as you slip out."
                            me "Fuck me, that was great."
                            "Nora turns to the side and coughs loudly, panting for breath. You get up and grab your pants, pulling them back on while she recovers."
                            if noraO.cumslut:
                                nora "Ah... Thank you [inputName], that was great. Your cum feels so thick in my throat."
                                "She pants softly and licks her lips, still savouring the taste."
                                nora "I should really get back to work now though."
                            else:
                                nora "Ah... I'm glad you had a good time. I should really get back to work now though."
                            me "You do that. Have a good night Nora."
                            hide nora
                            "She nods weakly, pulling herself back towards her desk and grabbing a pen. You head upstairs and back towards the center of campus."

                        "Cum on her face.":
                            "You hammer Nora's head back and forth, skullfucking her as you start to climax."
                            "Just before you start to cum you yank her head back, grabbing your cock with one hand while you hold her by the hair with the other."
                            me "Here we go, lets make sure you look like the cum dumpster you are!"
                            show nora blow21 at right
                            $ noraO.inc_cum_over()
                            "You stroke yourself to completion while Nora pants for breath, spraying your hot semen over her face. She moans softly as you empty your balls onto her."
                            "When you're done you let go and lean back with a sigh. Nora coughs a few times and slumps in her chair, catching her breath."
                            me "Fuck, that was great."
                            if noraO.cumslut:
                                nora "Ah... Thank you [inputName], your cum feels amazing on me. So thick and warm..."
                                "She licks her lips, catching some of your sperm that landed close to her mouth. She swallows and sighs, savouring the taste."
                                nora "I should really get back to work now though."
                            else:
                                nora "Ah... I'm glad you had a good time. I should really get back to work now though."
                            "You get up from the desk and grab your pants, pulling them back on."
                            me "You do that. Have a good night Nora."
                            hide nora
                            "She nods weakly, pulling herself back towards her desk and grabbing a pen. She leaves her breasts exposed and her face covered in your cum. You head upstairs and back towards the center of campus."

                "Let her keep going.":
                    #More blowjob
                    me "No, just keep going like that and you'll have me cumming soon."
                    "Nora smiles and kisses the top of your cock, then slides you back down her throat. She starts to take you deep and fast, making soft gagging noises as your tip hits the back of her mouth."
                    "You use your hand to guide Nora up and down your shaft, slowly speeding up as she gets more comfortable. Her tongue licks all up and down your sensitive dick as she blows you."
                    "Soon you feel your core start to tense as your climax approaches."
                    menu:
                        "Cum in her mouth.":
                            me "Alright, here we go Nora! Just keep going while I cum!"
                            "Nora tries to say something with your cock in her mouth, but you can't make it out. She keeps going though, throating you until you start to finish."
                            "Your first blast of cum lands at the back of her mouth, making her gasp in surprise. She then pulls back a little, keeping your tip just inside her lips while you empty your balls inside of her."
                            show nora blow15 at right
                            $ noraO.inc_cum_mouth()
                            "You give a loud sigh when you're done, leaning back on the desk. Nora pulls back slowly, careful not to let anything slip out of her mouth."
                            menu:
                                "Tell her to spit it on her tits.":
                                    me "Good girl. Now spit it onto your tits and spread it around for me."
                                    "Nora nods and tilts her head down, letting the mix of spit and cum dribble onto her tits in a thin stream."
                                    "As your semen spreads over her breasts she takes her hands and runs them up and down, getting her tits wet with the mixture."
                                    show nora blow17 at right
                                    $ noraO.inc_cum_over()
                                    "She ends by spitting the last little bit down between her cleavage, then looks back to you while she rubs her nipples slowly."
                                    nora "Like that?"
                                    me "Perfect. Just perfect."
                                    "Nora smiles and stands up, walking over to one of the lab sinks."
                                    nora "Good, I'm glad you had fun. Now I've really got to get cleaned up and back to work. I hope you have a good evening."
                                    hide nora
                                    "You get up and grab your pants, pulling them on while Nora wipes down her tits. You say goodbye and head upstairs."

                                "Tell her to swallow it.":
                                    me "Good girl. Now swallow it for me like a good slut should."
                                    show nora blow16 at right
                                    $ noraO.inc_cum_swallow()
                                    "Nora nods and pauses for a moment. You can see her throat working as she drinks down your sperm. When she's done she opens her mouth and tilts her head left and right, letting you see that it's all gone."
                                    me "Well done. That was perfect."
                                    "Nora smiles and stands up, grabbing her bra and putting it back on."
                                    if noraO.cumslut:
                                        nora "Good. Thank you for finishing in my mouth, I just love the way you taste."
                                        "She licks her lips and sighs contently."
                                    else:
                                        nora "Good, I'm glad you had fun. Now I've really got to get cleaned up and back to work. I hope you have a good evening."
                                    hide nora
                                    "You get up and grab your pants, pulling them on while Nora wipes down her tits. You say goodbye and head upstairs."

                        "Cum on her face.":
                            me "Alright Nora, here we go! I want to finish on your face!"
                            "Nora tries to say something with your cock in her mouth, but you can't make it out. She keeps going though, throating you until you start to climax."
                            "You tense up as you start to cum, and Nora pulls you out of her mouth. She grabs your wet cock with her hand and strokes you off, pointing you towards her face."
                            "She closes her eyes as you unload on her face, spraying your sperm onto her. She moves your shaft left and right to make sure you cover her entirely."
                            show nora blow13 at right
                            $ noraO.inc_cum_over()
                            "When you're done she lets go and slides her chair back, letting you admire your work."
                            me "Damn, you look good like that Nora."
                            if noraO.cumslut:
                                nora "It feels so good... So warm and thick..."
                                "She smiles and sighs happily."
                                nora "I've got to get back to work though. Have a good evening."
                            else:
                                nora "Well thank you. I'm glad you had fun. Now I've really got to get cleaned up and back to work. I hope you have a good evening."
                            hide nora
                            "She stands up and heads over to one of the lab sinks while you get your pants back on and leave the lab. You head back towards the center of campus."

                        "Cum on her tits.":
                            me "Alright Nora, here we go! Finish me over those huge tits!"
                            "Nora tries to say something with your cock in her mouth, but you can't make it out. She keeps going though, throating you until you start to finish."
                            "You tense up as you start to cum, and Nora pulls you out of her mouth. She grabs your wet cock with her hand and strokes you off, pushing out her chest to give you a nice large target."
                            show nora blow14 at right
                            $ noraO.inc_cum_over()
                            "Nora gasps quietly as you fire your warm load over her tits. She moves your shaft left and right to make sure you cover her entirely."
                            "When you're finished she lets go and slides her chair back, letting you admire your work. Her tits are covered with your white sticky semen, and it's dripping down between her cleavage."
                            me "Damn, you look good like that Nora."
                            if noraO.cumslut:
                                nora "Thank you [inputName], it feels good to have your warm cum spread over me."
                                "She runs a finger along the slope of her breasts, scooping up some of your cum, then licks the finger clean. She sighs happily while she savours the taste."
                                nora "I've got to get back to work though. I hope you have a good evening."
                            else:
                                nora "Well thank you. I'm glad you had fun. Now I've really got to get cleaned up and back to work. I hope you have a good evening."
                            hide nora
                            "She stands up and heads over to one of the lab sinks while you get your pants back on and leave the lab. You head back towards the center of campus."

            $ nora_hub.inc_level(4)
            $ noraO.change_resist(-nora_hub.use_red(4,noraO.resist_score))

        "Fuck her." if noraO.slut_score > 80:
            "You drop your pants in front of her, letting your hard cock spring out."
            me "I'd really like to take your pussy for a ride, if you've got the time."
            show nora strip6 at right
            "Nora nods and stands up, pulling her labcoat off and dropping her pants."
            nora "I think I can spare a few minutes. It would be a shame not to take advantage of that."
            show nora strip5 at right
            "She nods towards your cock and smiles as she peels off her bra, then turns around and strips off her panties as well."
            menu:
                "Have her sit on your cock.":
                    "You sit down in Nora's chair, spinning it around to face her with your legs spread."
                    me "Come on over and turn around, I want you to sit on my cock."
                    nora "Like this?"
                    "She walks over and turns around, bending at the knees so your shaft brushes against her ass. You hold onto your dick and flick the tip against her pussy, feeling how wet she is."
                    show nora fuck22 at right
                    $ noraO.inc_sex()
                    "You place your other hand on her hip, guiding her down as she sits back and slides you into her cunt."
                    nora "Oh god..."
                    me "Do you like that?"
                    "Nora moans softly and nods her head as she settles onto your dick. She wiggles her ass against your crotch, then starts to move her hips up and down."
                    "For a few minutes you're both quiet, and the only sound in the lab are the wet smacks as Nora rides up and down on your cock and the occasional moan."
                    me "Fuck, you feel so tight. I think I'm going to cum soon."
                    nora "Oh god, do it wherever you want. Ah!"
                    show nora fuck23 at right
                    "She pumps her hips up and down, sliding you in and out of her warm tight pussy as fast as she can manage."
                    menu:
                        "Cum inside her.":
                            "You grab Nora's hips and guide her as she fucks you. You give a soft moan as you climax, unloading all along her pussy."
                            if noraO.cumslut:
                                nora "Oh god yes! Pump me full of your delicious cum. Oh please, give me even more!"
                            else:
                                nora "Oooh! Ah, I feel you..."
                            "Nora gasps loudly and shivers for a moment, having her own orgasm. You keep guiding her as you finish cumming, making sure she gets every last drop of your seed inside of her."
                            show nora fuck24 at right
                            $ noraO.inc_cum_inside()
                            "When you're done you let go of her hips and sit back. She sighs deeply and leans back against you, lifting up her hips so your cock slips free."
                            me "Damn, that felt amazing."
                            nora "Ya, it did..."
                            "You stay like that for a few minutes, catching your breath. You play idly with her tits until she starts to get up."
                            if noraO.preg_response_ok():
                                nora "I'm glad you had a good time [inputName]. I should really get back to work though, if you don't mind."
                            else:
                                nora "I'm glad you had a good time [inputName]. Next time please be a little more careful where you finish though, I know it's easy to get carried away but we don't want any accidents, right? Now, I should get back to work."
                            "You get up from her chair and grab your clothes. Nora sits down at her desk, still naked, and grabs her pen."
                            hide nora
                            "You get dressed and say goodbye, leaving Nora to her work. You head upstairs and back towards the center of campus."

                        "Cum on her ass.":
                            "You grab Nora's hips and guide her as she fucks you. As you approach your climax you push up on her ass, forcing her off the top of your cock."
                            me "Here I come! Bend over!"
                            "Nora gasps and bends, ending up with her ass high in the air and hands on the floor so she doesn't fall over. You grab your wet cock and stroke yourself off onto her ass while you both pant for air."
                            show nora fuck25 at right
                            $ noraO.inc_cum_over()
                            "You spray your load over Nora's ass cheeks, landing some around her dripping pussy. When you're done you sit back and admire your work."
                            nora "It's so warm..."
                            me "You look great like that Nora. I should cum on you more often."
                            "Nora takes a deep breath, then stands up again."
                            nora "Maybe you should. Now, I really should be getting cleaned up and back to work."
                            me "Right, sure. Have fun."
                            hide nora
                            "You grab your clothes and get dressed while Nora gets some tissue and starts to wipe your semen off her ass. You say goodbye and head upstairs, heading back towards the center of campus."


                "Fuck her doggy style." if noraO.slut_score > 100:
                    "You grab Nora by the hips and thrust your crotch against her ass, rubbing your cock between her ass cheeks. She yelps in surprise as you reach around and grab one of her tits."
                    nora "Oh! I didn't realize you needed it that bad."
                    me "I do, I need to be inside of you right fucking now."
                    show nora fuck26 t right
                    $ noraO.inc_sex()
                    "You walk forward slowly until Nora's in front of Stephanie's desk, then push on her shoulders so she bends over for you. You hold your cock and line it up with her slit, pausing for a moment to appreciate how wet she already is."
                    nora "Go for it then, do whatever you want to me."
                    "You push into Nora's warm, wet pussy and slide to the back with a single thrust. She gasps loudly, then grinds her hips back against you."
                    "You grab her hips and start to thrust, settling into a rhythm as you fuck her from behind. Her ass bounces and jiggles as you hit it."
                    me "Fuck, that feels amazing. You're so wet, I can tell how much you love it. Tell me how much you love it Nora."
                    "You spank her ass, making it her yelp again."
                    nora "I love you inside me, I love it when you fuck me!"
                    me "Tell me what a slut you are."
                    nora "I'm a dirty cum slut who loves your cock. Ah! I want to do everything I can to help you cum!"
                    "You smile and fuck Nora harder, making her scream your name. It's not long before her tight cunt brings you to the edge of your orgasm."
                    menu:
                        "Cum inside her.":
                            me "Here we go!"
                            "You grip her hips and slam yourself deep inside of her as you start to unload. Nora gasps loudly as your hot seed starts to fill her up."
                            if noraO.cumslut:
                                nora "Oh god yes! Pump me full of it, dump it as deep as you can! Ah!"
                            else:
                                nora "Oh god..."
                            "You hold yourself tight against her ass until you're completely finished, then give her slippery pussy a few more pumps for good measure."
                            me "Damn, that was great Nora."
                            "She moans and twitches as you fuck her slowly."
                            if noraO.preg_response_ok():
                                nora "Yeah, it was. Ah..."
                            else:
                                nora "Yeah, it was... I should really go back on my birth control if you're going to finish inside me though."
                            show nora fuck27 at right
                            $ noraO.inc_cum_inside()
                            "You pull out of her wet cunt, stepping back and watching as your cum starts to leak out of her almost immediately."
                            me "Now you had work to do, you should probably get back to that."
                            nora "Right, of course. Thank you [inputName]."
                            hide nora
                            "You collect your clothes and head out of the lab while Nora tries to find some tissues to clean up with. You head back to ground level and towards the center of campus."

                        "Cum on her face.":
                            me "Here we go, get on your knees you slut!"
                            "You give her pussy one last thrust, then pull out with a wet pop and step back. Nora spins around and drops to her knees in front of you, playing with her own tits."
                            show nora fuck29 at right
                            $ noraO.inc_cum_over()
                            "You stroke yourself off until you start to cum. Nora pants softly as you spray your seed over her face, leaving her covered from forehead to chin with the sticky white liquid."
                            "You let go of your shaft and take a deep breath, admiring your work."
                            if noraO.slut_score > 120 or noraO.cumslut:
                                show nora fuck30 at right
                                "Nora leans forward, opening her mouth wide and slipping the tip of your sensitive cock inside before you can say anything else."
                                "Her tongue wraps around your shaft, licking off her own juices and the last few drips of cum from it. The feeling sends shivers up your spine, almost too much for you."
                                show nora fuck29 at right
                                "She takes one deep pass, tapping your tip aginst the back of her throat, then pulls off completely and looks up at you with a cum covered face."
                            else:
                                "Nora leans back and looks up at you once you're finished, panting softly with her face covered in cum."
                            nora "Wow, that was great."
                            me "It was, you felt amazing Nora. Now, I think you have work to get back to."
                            nora "Right, of course. Thank you [inputName]."
                            hide nora
                            "You collect yor clothes and head out of the lab while Nora tries to find some tissues to clean up with. You head back to ground level and towards the center of campus."

                        "Cum on her ass.":
                            me "Here we go!"
                            "You give her pussy one last thrust, then pull out with a wet pop and stroke yourself off with the tip of your cock resting on her ass cheeks."
                            show nora fuck28 at right
                            $ noraO.inc_cum_over()
                            "Nora pants softly as you spray your load over her ass, shifting from left to right to make sure you cover her completely."
                            nora "Oh... It's so warm..."
                            "You wipe the last few drops of cum off onto her, then step back and give a deep sigh."
                            me "Damn, that was great Nora."
                            nora "Yeah, it was."
                            me "Now, you had some work to do. You should probably get back to that."
                            nora "Right, of course. Thank you [inputName]."
                            hide nora
                            "She stands up, legs shaking slightly as she walks, and starts to search for some tissues to clean up with. You get dressed and head back to the center of campus."

                "Anal her" if noraO.slut_score > 130 or (noraO.anal and noraO.slut_score > 80):
                    "You grab Nora by the hips and thrust your crotch against her ass, rubbing your cock between her ass cheeks. She yelps in surprise when you reach around and grab one of her tits."
                    nora "Oh! Fuck, please don't make me wait and tease me like that. Just slip it inside me."
                    "You pinch her nipple, making her gasp and writhe against you."
                    me "Alright then, lets just slip it inside."
                    "You push on her shoulders to have her bend over a little and hold your shaft to line it up. You run your shaft between her legs and against her pussy a few times, appreciating how wet she's already gotten."
                    show nora fuck31 at right
                    $ noraO.inc_sex()
                    "After a few thrusts between her thighs you pull back and line up with her asshole, pressing your tip against it."
                    if noraO.anal:
                        nora "Mmm, go for it [inputName], I'm sure it'll fit."
                    else:
                        nora "Wait, that's not..."
                        me "I know, just relax and enjoy it."
                    "You press forward, having to work hard to slip into Nora's tight ass. Finally you slide in, and she gives a loud gasp."
                    nora "Oh fuck..."
                    show nora fuck32 at right
                    "You reach down and grab her arms, pulling them back to keep Nora upright while she bends forward. You start to thrust slowly, giving her time to get used to your cock up her ass."
                    me "God, aren't you just the biggest whore. Not a peep out of you when I wanted to fuck you in the ass."
                    "You pick up speed, making her yelp with each push."
                    me "Look even if I stop..."
                    "You plunge yourself deep inside of her and hold yourself there. Nora shivers slightly, ass twitching around your shaft."
                    me "You're shaking like a leaf. I bet you're going to cum soon, aren't you."
                    "Nora hesitates, then nods."
                    nora "Yes, I'm almost there. Please help me finish."
                    me "Lets see what we can do."
                    "You start moving again and fuck her fast and hard. Nora pants and moans with each stroke as you fuck her in the ass."
                    "Soon you feel your orgasm start to build up, and you think about how you want to finish."
                    menu:
                        "Cum inside her.":
                            me "Here we go Nora!"
                            "You pull her arms back and slam into her as you start to cum. She yelps loudly when you fire your first pulse of semen into her ass."
                            nora "Oh fuck!"
                            "She quivers around you, climaxing as you fill her asshole up with your seed."
                            "When you're finished you go back to fucking her, slowly this time, enjoying how wet and slippery you've made her. She pants softly, legs weak and shaking."
                            show nora fuck33 at right
                            $ noraO.inc_cum_inside_ass()
                            "Finally you pull out with a wet pop and let go of her arms. She steps forward and slumps against Stephanie's desk, cum dripping out of her ass and down her legs."
                            me "Fuck, that was great Nora."
                            "She nods slowly, still panting."
                            me "Now you had some work to do, you should probably get back to that."
                            nora "Right... Yeah... Thanks [inputName]."
                            hide nora
                            "You get dressed again and head out of the lab, leaving Nora against the desk while she recovers. You head towards the center of campus."

                        "Cum on her face.":
                            me "I'm almost there Nora, I'm going to cum all over your face!"
                            nora "Yes! Cover me like a good cum slut!"
                            "You pull out of her tight asshole and step back, stroking yourself off whie Nora turns and drops to her knees and looks up at you."
                            me "That's a good girl, here you go!"
                            show nora fuck29 at right
                            $ noraO.inc_cum_over()
                            "You start to cum, spraying your load all over her face. She keeps her mouth open for you, and you land some of your semen inside."
                            "When you're done you take a deep breath, feeling content."
                            if noraO.slut_score > 150 or noraO.cumslut:
                                show nora fuck30 at right
                                "Nora leans forwards and takes your cock in her mouth, running her tongue around your tip and sending shivers down your spine."
                                me "Fuck, that feels good."
                                "She nods and bobs her head up and down your shaft a few times, cleaning your dick with her mouth."
                                show nora fuck29 at right
                                "Finally she pulls off again and looks up, face covered in cum."
                            else:
                                "Nora sits back and looks up at you, face covered in cum."
                            nora "That felt amazing, thank you [inputName]."
                            me "No problem. Now, don't you have work to do?"
                            nora "Right, of course. Have a good evening."
                            hide nora
                            "You get dressed and head back upstairs while Nora looks for some tissue to get cleaned up with."

                        "Cum on her ass.":
                            me "Here we go Nora!"
                            "You pull back on her arms and give her a few deep thrusts, then pull out of her tight asshole and let go of her to stroke yourself off."
                            "She stumbles forwards onto Stephanie's desk, sticking her ass towards you as you blow you load over her cheeks."
                            nora "Ah! It's so... warm..."
                            show nora fuck34 at right
                            $ noraO.inc_cum_over()
                            "You wipe the last few drops off onto her ass, taking a moment to spread your cum around with the tip of your cock."
                            me "That felt great Nora. Now, don't you have work to do?"
                            nora "Ah, right... thank you [inputName]."
                            hide nora
                            "You get dressed and head out of the lab, leaving Nora to search for some tissues to get cleaned up. You head towards the center of campus."

            $ nora_hub.inc_level(5)
            $ noraO.change_resist(-nora_hub.use_red(5,noraO.resist_score))

        "Give her some serum and train her.\n-15 Influence, -2 Serum" if noraO.slut_score > noraO.training_threshold and (player_blue_serum + player_purple_serum + player_red_serum > 1):
            menu:
                "Train her to be a cum slut from now on." if not noraO.cumslut:
                    call cumslut_descrip("Nora")
                    menu:
                        "Continue with the training.":
                            call nora_train_cumslut
                        "Change your mind and leave.":
                            return False

                "Train her to be an anal lover from now on." if not noraO.anal:
                    call anal_descrip("Nora")
                    menu:
                        "Continue with the training.":
                            call nora_train_anal
                        "Change your mind and leave.":
                            return False

                "Train her to be a free use slut from now on." if not noraO.freeuse:
                    call freeuse_descrip("Nora")
                    menu:
                        "Continue with the training.":
                            call nora_train_freeuse
                        "Change your mind and leave.":
                            return False

                "Train her to be an exhibitionist from now on." if not noraO.exhib:
                    call exhib_descrip("Nora")
                    menu:
                        "Continue with the training.":
                            call nora_train_exhib
                        "Change your mind and leave.":
                            return False

                "Change your mind and leave.":
                    return False

        "Ask for a tour of the lab.":
            me "I was wondering if you could show me around here, I feel like you have a lot going on that I haven't seen."
            "Nora thinks about it for a moment, then nods and starts to lead you around. For the better part of an hour she points out various machines, or talks about her past research projects."
    return True

#####################
##Steph's Hub Scene##
#####################

label hub_steph:
    menu:
        "Ask her to strip for you." if stephO.slut_score > 20:
            me "So Stephanie, I've been watching you around the lab a little and I've got to tell you that you look amazing."
            steph "Thank you [inputName], I'm glad you think so."
            me "Seriously, you're smoking hot. Since we've got some time, maybe you could do me a favour and give me a little show."
            "Stephanie thinks for a moment, then smiles and nods."
            steph "I think I can do that for you. Here, sit down and enjoy."
            show steph strip3 at right
            "She spins one of the office chairs around for you and walks in front of it, pulling her sweater and shirt off and dropping them to the ground."
            show steph strip6 at right
            "You sit down in the chair and lean back, watching as Stephanie strips off her pants next and turns around, showing her ass off to you."
            steph "Is this what you wanted to see?"
            "She gives her butt a smack, making it bounce and jiggle for you."
            me "That's exactly what I wanted to see."
            #Show off a little
            if stephO.slut_score > 30:
                "Stephanie spins around and cups her breasts in her hands, squeezing them together while she looks at you."
                steph "You don't want to see these girls? Not at all?"
                me "Well, I wouldn't say no to a quick peek."
                show steph strip26 at right
                "Stephanie laughs and slides her hands under her bra, lifting it up slowly. She lifts it all the way up and leaves just her hands covering her breasts."
                me "Oh come on, you can't tease me like that!"
                steph "I can, and I will!"
                show steph strip27 at right
                "She turns around again, letting go of her tits and placing them on her ass. She peels her panties down a little bit, low enough that you can almost see her pussy. Then she pulls them back up again, peeking over her shoulder and laughing."
                steph "Well then? What do you want to see?"
                menu:
                    "Show off for me.":
                        me "All of you, every last inch."
                        show steph strip26 at right
                        "Stephanie laughs and turns around, hands back on her tits."
                        steph "So it's really these that you want to see then, right? I guess it's mean to tease you like this without at least giving a peek."
                        show steph strip28 at right
                        "She lifts her hands up more, letting her boobs fall out from her hands and bounce to a stop."
                        me "That would have been very mean. Bounce those around for me, that'll make up for it."
                        "Stephane pinches her nipples between her thumb and forefingers, pulling her tits up and then letting them drop."
                        "She gasps softly as she pinches her nipples again, pulling her tits up again and holding them like that."
                        me "Perfect, you have great boobs Stephanie."
                        steph "Thank you [inputName]. It's hot to have you watch me play with them. I guess I just don't do this very often any more."
                        me "Any more?"
                        steph "I was a little wilder when I was younger."
                        "She gives you a wink and turns around, spanking her ass to make it bounce."
                        me "Hard to imagine how much wilder you could be."
                        steph "I'm sure you can, if you try real hard."
                        show steph strip29 at right
                        "She pulls her panties to the side, just for a moment, and gives you a glimps of her pussy. It's dripping wet, practically begging to be filled."
                        show steph strip1 at right
                        "She straightens up again and pulls her bra back in place."
                        #A few different angles

                    "Touch yourself.":
                        me "Well if you're going to tease me, I want you to tease yourself too. Touch yourself a little for me."
                        steph "Ooh, I like the way you think."
                        "She spreads her legs, slipping a finger between her thighs and rubbing her pussy through her panties."
                        show steph strip30 at right
                        "You sit back and enjoy the view as Stephanie plays with her cunt. After a little while she pulls her panties to the side, running a finger along her slit and moaning softly."
                        me "You're looking pretty wet there Stephanie."
                        "She nods and gasps, slipping her finger inside of her pussy."
                        steph "Yeah, I guess I am. Wow, this actually feels realy good."
                        me "I bet it does. Keep going, it would be hot to watch you cum."
                        steph "Mmm, I bet it would be. Just give me a... ah, a second."
                        show steph strip31 at right
                        "Stehpanie bends over a little more, slipping a second finger into her pussy. She moans quietly as she fingers herself in front of you."
                        "After another minute she takes a sharp breath and knocks her knees together. She stays tensed up for a moment, then relaxes with a sigh."
                        steph "Ah, well there we go..."
                        show steph strip1 at right
                        "She straightens up, pulls her bra back into place, and turns to you."
                        #Steph touching herself

                if stephO.slut_score > 50:
                    steph "So, if you liked that I might have some other stuff you'd like."
                    me "And what would that be?"
                    steph "Well, I keep some clothes here on campus so I can change out after work. Let me see what I have and you tell me what you'd like to see me in."
                    "Stephanie searches around for a moment, comming back with an armful of clothing."
                    #Show off other outfits
                    menu:
                        "Naked":
                            me "That all looks nice, but I think you look better wearing nothing at all."
                            steph "You think so? Let me just get rid of all this then..."
                            show steph strip7 at right
                            "Stephanie puts the clothing to the side, then reaches behind her back and undoes her bra. She pulls it off and drops it to the ground."
                            show steph strip2 at right
                            "Next she loops her thumbs through the sides of her panties and pulls them down, stepping out of them and throwing them onto the pile."
                            "She stands in front of you, just wearing her socks and shoes. You take a moment to look her up and down, appreciating the view."
                            me "Very nice, you look beautiful."
                            show steph strip34 at right
                            "Stephanie turns around, leaning over and planting her hands on her desk so you can take a look at her from behind."
                            steph "Did you get a good look at everything?"
                            "She jiggles her ass, then spreads her legs so you can see her pussy."
                            me "I think so, thanks Steph."

                        "Swimsuit":
                            me "Is that your swimsuit for the summer? It looks cute."
                            "Stephanie puts down the rest of the clothes and holds up a red two piece swimsuit."
                            steph "I thought it was. Here, give me a moment."
                            show steph strip32
                            "She strips down quickly and slips the bikini on, turning back to you and posing."
                            steph "There, what do you think?"
                            me "I was right, that does look cute on you. Turn around, I want to see your butt."
                            show steph strip33
                            "Stephanie turns for you, planting her hands on her desk and bending over a little so you can take a look."
                            "You enjoy the view for a little while, then Stephanie stands back up again."
                            steph "Did you get a good look at everything?"
                            me "I think so, thanks Steph."

                        "Lingerie.":
                            me "That underwear looks hot, how about you put that on for me."
                            show steph strip35 at right
                            "Stephanie nods, quickly stripping out of her current underwear. She slips on the black and blue lingerie, posing for you once she's done."
                            steph "It actually came with a matching set of heels, but those things are just an accident waiting to happen."
                            me "Your legs look great without them anyway. All of you looks great actually. Turn around for me so I can take a look from behind."
                            show steph strip36 at right
                            "Stephanie spins for you, bending forward a little so you can admire her ass."
                            steph "Thanks [inputName], I'm glad you think so. Besides, who needs heels when you're just going to end up on your knees anyways."
                            "She jiggles her ass at you, then turns back and smiles."
                            steph "Get a good look at everything?"
                            me "Yea, I think so. Thanks Steph."
                            #TODO

                    show steph work at right
                    "Stephanie gets back into her normal underwear, then pulls her pants and shirt back on."
                    steph "Well that was fun, we should do it again [inputName]."
                    me "We definitely should. I think I'm going to take a break before Nora gets in, I'll talk to you later."
                    steph "Yeah, see you soon."
                    hide steph
                    "You head back upstairs and walk towards the center of campus."
                    #End the show
                else:
                    steph "Well that was fun, hope you had a good time."
                    me "I really did, thanks Stephanie."
                    show steph strip3 at right
                    "She smiles and grabs her pants, pulling them back on."
                    steph "I've got some work to get done before Nora gets in, want to help me out?"
                    me "Uh, sure. Lets take a look."
                    show steph work at right
                    "Stephanie gets her shirt back on, then gives you some paperwork to help out with. You spend the rest of the hour helping her out, then head back towards the center of campus to stretch your legs before Nora gets in."
                    #End the show
            else:
                "She bounces her ass a few more times, then turns around again."
                show steph strip1 at right
                steph "Good, I enjoyed the show. Now I had some paperwork I needed to get done. If you wanted to lend a hand I'd appreciate it."
                me "Uh, sure."
                "You grab a seat while Stephanie put her clothes back on. You spend the rest of the hour helping her with paperwork for the lab."
                "When you're done you say goodbye and head back towards the center of campus, taking a few minutes to stretch your legs before Nora shows up."
                #End the show

            $ stephO.inc_naked()
            $ steph_hub.inc_level(1)
            $ stephO.change_resist(-steph_hub.use_red(1,stephO.resist_score))

        "Ask for a handjob." if stephO.slut_score > 35:
            "You sit down in a chair, swivelling it around to face Stephanie."
            me "If you've got a few minutes, could I ask a favour?"
            steph "Uh, sure. What's up?"
            "You rub the bulge in your pants, spreading your legs to make the movement more obvious."
            me "I'm a little pent up right now, I was hoping you could lend a hand and help me get off."
            "Stephanie thinks for a moment, glances up at the clock on the wall, then nods and slides her chair closer."
            steph "Sure, since we've got some time before Nora gets in."
            "She positions her chair in front of you while you pull your pants down, letting your hard cock spring free."
            show steph hand6 at right
            $ stephO.inc_hand()
            "Stephanie positions herself in front of you, leaning forward and wrapping a hand around your shaft."
            steph "Oooh, you're so hard already. Let me just take care of that."
            if stephO.slut_score > 50:
                "She runs her hand up and down your dick, squeezing gently. Her technique is perfect, it's obvious she knows what she's doing."
                steph "Hmm, it's a little dry..."
                "She pauses for a moment, bringing her hand up to her mouth and spitting into it. When she wraps it around your cock again it's wet and warm, and she strokes you off as fast as she can."
                steph "Much better."
                me "Fuck that's hot."
                steph "Glad you think so. Just relax and enjoy."
                "You lean back and give a deep, contented sigh while she jerks you off. After a few minutes you start to tense up as your orgasm approaches."
                # Lets you cum somewhere else
                menu:
                    "Tits":
                        me "Ah, here we go Stephanie."
                        steph "I thought so, I can feel you twitching. That's so cute."
                        me "Get your tits out, I want to cum on them."
                        if stephO.slut_score > 70 or stephO.cumslut:
                            steph "Aw, not in my mouth? I just love how you taste."
                            me "Not this time, now hurry up!"
                        "Stephanie gets off her chair, getting on her knees in front of you while she pulls up her shirt with her other hand."
                        "Her tits fall out of her bra, bouncing around while she strokes you to completion. You grip the edge of the chair as you start to cum onto her."
                        show steph hand7 at right
                        $ stephO.inc_cum_over()
                        "You spray your load over the slope of her breasts, gasping as she keeps playing with your wet cock long after you're finished."
                        me "Jesus Stephanie, that's all there is."
                        steph "Just making sure. Ah, that was hot."
                        "She lets go of your dick, pausing to lick a few drips of sperm off of her hand before she goes and finds some tissues to get cleaned up."
                        steph "I've got some work to get back to, but I had a lot of fun [inputName]. We should do that again some time."
                        me "Sounds like a plan to me. Talk to you later Stephanie."
                        hide steph
                        "You head out of the lab before Nora gets in for the afternoon, heading back to the center of campus to stretch your legs."

                    "Face":
                        me "Ah, here we go Stephanie."
                        steph "I thought so, I can feel you twitching. That's so cute."
                        me "Get on your knees, I want to cum on your face."
                        "Stephanie nods and slides onto the floor, stroking you off while she looks up at you."
                        if stephO.slut_score > 70 or stephO.cumslut:
                            steph "On my face, right?"
                            me "Ya, I 'm going to cover you like a slut."
                            steph "Are you sure you don't want to cum in my mouth? Let me drink it up like a good girl should?"
                            show steph hand10 at right
                            "She opens her mouth, sticking her tongue out. Her breath is hot against the tip of your cock as you come dangerously close to climaxing."
                            menu:
                                "Cum on her face.":
                                    me "Not today Stephanie, you'll just have be patient. Maybe next time."
                                    "Stephanie pouts, but nods and closes her mouth again. She looks up at you, still excited for you to cum."
                                    "She jerks you off until you start to cum, looking up at you while you cover her face with hot semen."
                                    me "Ah fuck Stephanie, that feels great."
                                    show steph hand9 at right
                                    $ stephO.inc_cum_over()
                                    "She moves your cock left and right, making sure you get every inch of her face. When you're done she gives you a few more playful strokes, making sure she gets every last drop."
                                    if stephO.cumslut:
                                        steph "Mmm, you covered me like the slut I am. Thank you [inputName]."
                                        "Stephanie leans forward and licks the side of your cock a few times, cleaning off the last few drops of cum."
                                    else:
                                        steph "There we go, all done."
                                        "Stephanie checks her hand and pauses for a moment to lick some cum off of it."
                                    steph "I hope you had a good time [inputName]."
                                    me "I did, we should do it again some time."
                                    steph "Well, you know where to find me. Now I should get cleaned up and back to work, I've got some stuff to finish before Nora gets here."
                                    "You pull your pants up and leave the lab, taking a walk towards the center of campus to stretch your legs before work."

                                "Cum in her mouth.":
                                    me "Well, if you're going to twist my arm like that..."
                                    "Stephanie winks up at you and leans forward, slipping your cock into her mouth. She swirls her tongue around your tip a few times, jerking you off with one hand while she pulls up her shirt and bra with the other."
                                    "You gasp as you start to cum, firing your hot load right into Stephanie's mouth. She moans and keeps stroking you until you're completely done."
                                    "When you're finished emptying your balls into Stephanie you take a deep breath and sigh contentedly."
                                    show steph hand8 at right
                                    $ stephO.inc_cum_mouth()
                                    $ stephO.inc_cum_swallow()
                                    "Stephanie slips off your cock and looks at you, opening up so you can see her flick her tongue through your semen."
                                    me "Fuck, good girl."
                                    "She closes her mouth and smiles, swallowing loudly a few times then opening up so you can see it's all gone."
                                    if stephO.cumslut:
                                        steph "Thank you so much [inputName], you taste delicious."
                                        "She leans forward and licks the side of your shaft, cleaning up every last drop of cum she can find."
                                        "Eventually she pulls back and sighs contently, standing up once she's caught her breath."
                                    else:
                                        steph "Ah, thank you [inputName]. That was hot."
                                        "She stands up, taking a moment to catch her breath."
                                    me "No problem. We should do it again some time."
                                    steph "Well, you know where to find me. Now I've got some work to get done before Nora gets in."
                                    "You pull up your pants and leave the lab, taking a walk towards the center of campus to stretch your legs before work."

                                "Slam your cock down her throat." if stephO.slut_score > 90 or stephO.cumslut:
                                    me "Well if that's what you want..."
                                    "You stand up in front of Stephanie, placing your hands on the back of her head and bringing her forward."
                                    "She licks the tip of your cock eagerly as it slips into her mouth, then tries to gasp as you suddenly slam yourself as deep down her throat as you can."
                                    show steph hand11 at right
                                    $ stephO.inc_cum_mouth()
                                    $ stephO.inc_cum_swallow()
                                    "You piston your hips back and forth, bouncing your balls off of Stephanie's chin as you throat fuck her. Her hands drop to her sides, dangling limp as you take control."
                                    me "Do you like that Stephanie? I bet you can't wait to have my cum shot right into your stomach. You're such a cum slut, just begging for it."
                                    "She moans as much as she can past your cock, her throat rumbling around your shaft. You keep going, not pausing as you climax."
                                    "You fire your load all up and down her throat, letting it out as you skull fuck her. Stephanie quivers beneath you, eyes rolled up in their sockets as you use her like a toy."
                                    "When you're done you give a few more deep thrusts, then pull out with a wet pop and sit back down. Stephanie leans forward and coughs, panting to catch her breath."
                                    steph "Oh fuck... Oh fuck that was...."
                                    me "That felt great Stephanie."
                                    "She looks up at you and nods slowly."
                                    steph "You made me... just by fucking my... Wow."
                                    "You pull up your pants and walk next to her, slipping two fingers into her mouth. She sucks on them gently from the floor."
                                    me "I know you love being my cum dumpster Stephanie, I just give you what you want."
                                    "You pull your fingers out of her mouth and head to the door, leaving Stephanie on the floor while she catches her breath."
                                    hide steph
                                    "You take a walk towards the center of campus, stretching your legs before work."
                        else:
                            "Stephanie jerks you off until you start to cum, closing her eyes and mouth while you cover her face with hot semen."
                            me "Ah fuck, that feels great."
                            show steph hand9 at right
                            $ stephO.inc_cum_over()
                            "She moves your cock left and right, making sure you get every inch of her face. When you're done she gives you a few more playful strokes, then lets go and opens her eyes."
                            steph "There we go, all done."
                            "Stephanie checks her hand and pauses for a moment to lick some cum off of it."
                            steph "I hope you had a good time [inputName]."
                            me "I did, we should do it again some time."
                            steph "Well, you know where to find me. Now I should get cleaned up and back to work, I've got some stuff to finish before Nora gets here."
                            "You pull your pants up and leave the lab, taking a walk towards the center of campus to stretch your legs before work."


                    "Mouth" if stephO.slut_score > 60 or stephO.cumslut:
                        #Lets you cum in her mouth instead of her tits.
                        me "Ah, here we go Stephanie."
                        if stephO.cumslut:
                            steph "I can feel you twitching. Are you going to give me a nice, big load now?"
                        else:
                            steph "I thought so, I can feel you twitching. That's so cute."
                        me "Get on your knees, I want you to take it in your mouth for me."
                        "Stephanie nods eagerly, dropping onto the floor in front of you while she strokes you off. She pulls up her shirt and bra with her other hand, letting her tits free while she finishes you off."
                        "She places the tip of your cock onto her lips, wrapping them around and sucking on you gently. Her hand keeps sliding up and down until you start to cum."
                        "You grip the edge of the office chair as you unload into her mouth. Stephanie moans softly as you fill her up with your warm semen."
                        "When you're completely done she swirls her tongue around your tip to get every last drop, then slides off and looks up at you."
                        show steph hand8 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "She opens her mouth wide, showing off the pool of white liquid inside. Her tongue flicks around, playing with it for a while."
                        me "Holy crap. Good girl Stephanie."
                        "She nods and closes her mouth, swallowing loudly and opening up again so you can check that it's all gone."
                        steph "Ah, thank you [inputName]. That was hot."
                        show steph strip8 at right
                        "She stands up, taking a moment to catch her breath."
                        me "No problem. We should do it again some time."
                        steph "We should, you know where to find me. Now I've got some work to get done before Nora gets in, if you don't mind."
                        hide steph
                        "You pull your pants up and leave the lab, taking a walk towards the center of campus to stretch your legs before work."
            else:
                "She jerks you off with her warm hand, running her thumb over the tip of your dick and spreading around your precum."
                me "That feels great Steph, thanks."
                steph "No problem. Are you going to cum soon?"
                me "Ah, ya. Keep going like that."
                "She smiles and slides her chair a little to the side, out of the line of fire. She works her hand up and down your shaft, picking up speed as you start to climax."
                "You moan out loud as you orgasm, firing your load onto the floor next to Stephanie's desk. You dribble the last few pulses of cum onto Stephanie's hand."
                steph "Wow, good boy. That was nice."
                "She gives you a few more passes along your sensitive cock, making you shiver with pleasure, before letting go and looking at the semen on her hand."
                "After a split second pause she sticks her tongue out and runs it along her thumb, then slips her forefinger into her mouth and cleans it off too."
                me "Holy fuck that's hot."
                show steph work at right
                "She laughs and licks the last of your seed off her hand and turns back towards her desk."
                steph "I hope so. Now you should get that cleaned up before Nora shows up, cleaning supplies are over there."
                hide steph
                "You pull your pants back up and grab some tissues to clean up with. After a few minutes you're done and say goodbye. You head upstairs and back towards the center of campus."
                #Cum on the floor

            $ steph_hub.inc_level(2)
            $ stephO.change_resist(-steph_hub.use_red(2,stephO.resist_score))

        "Ask for a titfuck." if stephO.slut_score > 50:
            #Titfucks you for a while.
            "You unzip your pants and pull them down, letting your hard cock spring out. Stephanie watches it for a second, eyes tracking it as it bounces up and down."
            me "We've got a little bit of time before Nora gets in, would you be able to help me out?"
            steph "What did you have in mind?"
            "You step in front of her and run your hands over her shirt, feeling the shape of her breasts."
            me "I was thinking you could get these two out and put them to work."
            "Stephanie moans softly as you rub your thumb in a circle around her hardening nipple."
            steph "That... sounds like a good idea. One moment."
            show steph strip3 at right
            "She peels her shirt up and off, throwing it beside her desk. She spins around in her office chair, presenting her back to you."
            steph "Unhook me please."
            show steph strip37 at right
            "You do so, and she shrugs the piece of clothing forward and drops it to the ground as well. She swivels back to you, boobs jiggling slightly as she stops."
            me "Damn, those look amazing Stephanie."
            "She cups her tits, bouncing them in her hands a few times."
            steph "Well then slip between them and let me take over from there."
            "Stephanie leans forward, holding her boobs apart so you can slip your hard cock between them."
            show steph tit4 at right
            $ stephO.inc_tit()
            "Once you're settled between her breasts Stephanie starts to slide them up and down, pausing occasionally to jiggle them around or reposition."
            me "You're really good at that Steph, you'll have me cumming in no time."
            if stephO.slut_score > 70:
                #Blows you a little to lube you up
                steph "I'm sure I will."
                show steph tit6 at right
                "She winks at you and bends forward, letting your cock slip out from between her tits and catching it in her mouth."
                me "Oh fuck..."
                "Stephanie bobs her head forward, her tongue licking the bottom of your shaft as she blows you. After a few passes she pulls off with a wet pop, pressing her breasts around your cock again."
                steph "There, much better."
                show steph tit4 at right
                "She goes back to tifucking you, your wet cock easily sliding up and down in her cleavage. Her breasts are soft and warm, pressing in on either side of your shaft."
                menu:
                    "Take over and fuck her tits." if stephO.slut_score > 80:
                        #Take over and fuck her
                        "You reach down, placing your hands over Stephanie's and pressing them even tighter around your cock."
                        steph "Oh! Not fast enough for you?"
                        me "Just couldn't hold myself back."
                        show steph tit9 at right
                        "You pump your hips up and down, fucking Stephanie's tits while she sits in her chair. After a few strokes she looks down and sticks out her tongue, licking the tip of your penis each time you thrust out the top of her cleavage."
                        me "That's right, keep it nice and wet for me. Good girl, very good girl."
                        "Stephanie moans as you pinch her nipples and press her boobs together even harder. Fucking her tight, warm, wet cleavage has you quickly approaching your orgasm."
                        menu:
                            "Cum on between her tits.":
                                me "Alright, here I come Stephanie!"
                                steph "Go for it [inputName], wherever you want."
                                "You pump your hips as fast as you can manage, pushing yourself over the edge. You fire off your load between Stephanie's breasts as you fuck them, shooting pulses of hot sperm out the top with each thrust."
                                steph "Oh god!"
                                show steph tit5 at right
                                $ stephO.inc_cum_over()
                                "You keep going until you're completely spent, then slip out and take a deep breath."
                                if stephO.slut_score > 100 or stephO.cumslut:
                                    show steph tit10 at right
                                    "You're startled when Stehapnie starts to suck on your sensitive cock, running her tongue around it and sending shivers down your spine."
                                    me "Fuck! Easy there Steph."
                                    "She pulls off and looks up at you, pausing for a moment to swallow."
                                    steph "Sorry, just cleaning up for you."
                                    me "Go easy on the little guy, he's still sensitive."
                                    "She nods and opens her mouth, letting you slip back inside. She gives you a few slow, gentle passes and slides off when you're all clean."
                                    show steph tit5 at right
                                me "That felt amazing Stephanie. We should do it again some time."
                                steph "Well, you know where to find me. I should get this cleaned up before Nora gets here though."
                                me "Yeah. I'm going to go for a quick walk and stretch my legs. See you later."
                                hide steph
                                "You pull up your pants and head out of the lab, walking back towards the center of campus."

                            "Cum on her face.":
                                me "Alright, here I come Stephanie!"
                                steph "Go for it [inputName], wherever you want."
                                "You pump your hips as fast as you can manage, pushing yourself over the edge. You pull back at the last moment, grabing your cock and stroking it while you point it towards Stephanie's face."
                                me "Here you go, lets cover that pretty face of yours!"
                                show steph tit7 at right
                                $ stephO.inc_cum_over()
                                "You spray your hot cum over Stephanie's face, who gasps softly as it lands on her. Before you're even finished the warm liquid starts to trickle down, running into her mouth or off her chin."
                                "You jerk yourself off until you're completely spent, then relax and take a deep breath."
                                if stephO.slut_score > 100 or stephO.cumslut:
                                    show steph tit11 at right
                                    "You're startled when Stephanie starts to suck on your sensitive cock, running her tongue around it and sending shivers down your spine."
                                    me "Fuck! Easy there Steph."
                                    "She pulls off and looks up at you, pausing for a moment to swallow."
                                    steph "Sorry, just cleaning up for you."
                                    me "Go easy on the little guy, he's still sensitive."
                                    "She nods and opens her mouth, letting you slip back inside. She gives you a few slow, gentle passes and slides off again when you're all clean."
                                    show steph tit5 at right
                                me "That felt amazing Stephanie. We should do it again some time."
                                steph "Well, you know where to find me. I should get this cleaned up before Nora gets here though."
                                me "Yeah. I'm going to go for a quick walk and stretch my legs. See you later."
                                hide steph
                                "You pull up your pants and head out of the lab, walking back towards the center of campus."

                            "Cum in her mouth.":
                                me "Alright, here I come Stephanie!"
                                steph "Go for it [inputName], wherever you want."
                                me "Open wide, I want to fill up that pretty mouth of yours."
                                "Stephanie smiles up at you, pressing down on her own tits as you give them a few final thrusts."
                                steph "God, I was hoping you'd say that."
                                "She opens her mouth wide and sticks her tongue out, waiting to receive your hard cock. You wait until the last moment, then pull out from her tits and slip into her mouth as you start to cum."
                                "Stephanie moans loudly as you empty your balls into her mouth and across her tongue. You give a few half hearted pumps into her mouth, which she eagerly allows, then step back and give a contented sigh."
                                me "Damn that felt good. Open up for me, I want to see it."
                                show steph tit8 at right
                                $ stephO.inc_cum_mouth()
                                $ stephO.inc_cum_swallow()
                                "Stephanie nods and opens her mouth wide, tilting her head side to side so the pool of white liquid flows around."
                                me "Good girl. Now swallow it like the little cum slut you are."
                                "She nods and closes her mouth. You can see her throat working as she drinks down your sperm, then she opens her mouth wide and shows it off to you."
                                steph "It's just that easy. You tasted amazing, by the way."
                                me "Glad you liked it. We should do it again some time."
                                steph "Well, you know where to find me. I should get dressed before Nora gets back though."
                                me "Alright, I'm going to go for a quick walk and stretch my legs. See you later."
                                hide steph
                                "You pull your pants up and head out of the lab, walking towards the center of campus."

                            "Cum down her throat." if stephO.slut_score > 100:
                                me "I'm not sure your tits are going to do it for me Stephanie."
                                steph "What do you mean? Is there some...!"
                                "You cut her off by sliding up and out of her tits, pressing the tip of your cock against her lips. She opens up willingly, and you slam your cock as deep as you can inside of her mouth and down her throat."
                                show steph tit12 at right
                                $ stephO.inc_cum_mouth()
                                $ stephO.inc_cum_swallow()
                                "Stephanie moans and shivers in her chair as you hold her deep on your cock. Even without moving she works her throat, tightening and relaxing it around your shaft to draw you even closer to orgasm."
                                me "That's right, I know you want this Stephanie. I'll just throat fuck you until I'm ready to cum and give you exactly what you want."
                                "You let go of her tits and hold her by the head, keeping it still while you start to pump your hips back and forth. She writhes in her chair as you deepthroat her, eyes turned up in their sockets towards you and arms limp at her side."
                                "After a few more thrusts you can't hold back any longer. You pump as fast as you can, making loud, wet smacking sounds as you slam down Stephanie's throat."
                                me "Here you go bitch! Drink it all down like the fucking slut you are!"
                                "As you start to cum you press down hard on the back of Stephanie's head, pulling her forward and keeping the tip of your cock as far down her throat as you can manage."
                                "She quivers again under your hands as you start to fire your hot load right down her throat and into her stomach."
                                me "Are you cumming right now? Did you like having my cum forced down your throat?"
                                "Stephanie twitches again, trying to nod while you hold her on your cock."
                                me "I bet you did. You're such a massive cum slut, I bet you'd throat anyone if they promised to do this to you."
                                "She moans again, turning it into a gargle around your cock."
                                "Finally you pull out of her throat, stepping back and letting her slump forward and gasp for breath."
                                steph "Oh fuck... Oh fuck fuck fuck..."
                                "Stephanie looks up at you, eyes watering, face red, spit trailing down her chin."
                                steph "That was so fucking hot..."
                                me "Well I expect we'll be doing it again real soon. For now you should probably get dressed before Nora gets here."
                                steph "Oh, right."
                                me "I'm going to stretch my legs for a bit, I'll see you later."
                                hide steph
                                "You pull your pants up and head out of the lab, taking a short walk towards the center of campus."

                    "Let her keep going.":
                        #Just keep going.
                        "You give a deep sigh and relax, just enjoying the feeling of Stephanie servicing you for a few minutes. She pauses occasionally to slip you back in her mouth, blowing you to get your shaft wet again."
                        "Eventually you feel your climax approaching. You tense your cock, and Stephanie giggles a little."
                        steph "I felt that. Getting close?"
                        me "Yeah, I'm almost ready."
                        steph "Good. Where do you want to finish?"
                        menu:
                            "Cum on her tits.":
                                me "All over your tits. They've done such a good job they deserve a reward."
                                if not stephO.cumslut:
                                    steph "Not in my mouth? That's a shame."
                                    me "Maybe next time, I want to see you covered in cum right now though."
                                "She nods and titfucks you faster, squeezing tight on your cock from either side."
                                "You pull out from her tits just before you start to cum, stroking yourself to completion as she holds her tits up in front of you."
                                steph "That's right, just let it all out for me [inputName]! I want you to cover me in it!"
                                show steph tit5 at right
                                $ stephO.inc_cum_over()
                                "You moan softly and start to spray your load over her waiting breasts. You move your cock left and right, making sure you cover as much as you can with your semen."
                                "When you're done you rub the tip of your penis over the top of her boobs, spreading around your sperm a little."
                                me "Holy fuck that's hot. You're an amazing cum slut Stephanie. I love it."
                                steph "I can't say I mind being one, it feels really hot. Now pass mes some tissues, I need to get cleaned up before Nora gets here."
                                me "Right, sure. I'm going to go for a quick walk and stretch my legs. See you later."
                                hide steph
                                "You pull your pants up and head out of the lab while Stephanie gets dressed. You head up to the ground level and take a short walk back to the center of campus."

                            "Cum on her face.":
                                me "Right on your face."
                                if not stephO.cumslut:
                                    steph "Not in my mouth? That's a shame."
                                    me "Maybe next time, I want to see you covered in cum right now though."
                                "She nods and titfucks you faster, squeezing tight on your cock from either side."
                                "You pull out from her tits just before you start to cum, stroking yourself to completion as she looks at your cock from her office chair."
                                show steph tit7 at right
                                $ stephO.inc_cum_over()
                                "You moan softly and start to spray your load over her face. She holds still until you're done then looks at you, semen dripping down her face."
                                steph "Is this what you wanted to see?"
                                "She runs a finger along her cheek, then slips it into her mouth and licks your semen off of it."
                                me "Holy fuck that's hot. You're an amazing cum slut Stephanie. I love it."
                                steph "I can't say I mind being one, it feels really hot. Now pass me some tissues, I need to get cleaned up before Nora gets here."
                                me "Right, sure. I'm going to go for a quick walk and strech my legs. See you later."
                                hide steph
                                "You pull your pants up and head out of the lab while Stephanie gets dressed. You head up to the ground level and take a short walk back to the center of campus."

                            "Cum in her mouth.":
                                me "Right into your mouth."
                                steph "I was hoping you'd say that."
                                "She smiles and titfucks you faster, squeezing tight on your cock from either side."
                                "You moan softly as you start to cum, and Stephanie dips her head down and slips your tip into her mouth. She holds you there as you fire your load of semen into her."
                                me "That's a good girl, fuck that's nice."
                                show steph tit8 at right
                                $ stephO.inc_cum_mouth()
                                $ stephO.inc_cum_swallow()
                                "She waits until you're completely done, then swirls her tongue around your tip to get the last bit of sperm off of it before sliding off and looking up at you."
                                "She opens her mouth, revealing the puddle of white liquid you put there. She blows a few bubbles through it while you watch, licking her lips occasionally to make sure nothing slips out."
                                if stephO.cumslut:
                                    "Stephanie finally closes her mouth and starts to drink down your cum. She shivers with pleasure as she swallows it all, and opens up when she's done so show it's all gone."
                                    steph "Mmm, thank you [inputName]. Your cum tasted so damn good today, I loved it."
                                    "She licks her lips and sighs happily."
                                else:
                                    "Finally Stephanie closes her mouth again and swallows, opening up after so you can see it's all gone."
                                    steph "There, all done. That was great [inputName], you taste amazing."
                                me "Well I know where to find you, so I might be back. I'm going to go stretch my legs for a few minutes before Nora gets in."
                                hide steph
                                "You pull your pants up and head out of the lab while Stephanie gets dressed again. From there you take a short walk back to the center of campus."

            else:
                steph "Good, just cum whenever you want between my tits, I can clean up after."
                "She speeds up, titfucking you for another few minutes before you feel your orgasm approaching."
                me "Here we go Stephanie, keep going!"
                show steph tit5 at right
                $ stephO.inc_cum_over()
                "She nods and keeps servicing you with her tits until you start to cum. You blow your load in her cleavage, and she keeps sliding up and down along your shaft until you're completely finished."
                steph "Wow, well done."
                "You take a step back, pulling your dick out from between her cum covered breasts."
                me "That was great Stephanie. Thanks."
                steph "Any time. Pass me those tissues, would you?"
                "You pull up your pants and pass the tissues over to Stephanie, who starts to wipe your sperm from between her boobs."
                me "Well, I'm going to go stretch my legs before work. See you later."
                hide steph
                "You head back upstairs and take a walk towards the center of campus."

            $ steph_hub.inc_level(3)
            $ stephO.change_resist(-steph_hub.use_red(3,stephO.resist_score))

        "Ask for a blowjob." if stephO.slut_score > 70:
            #Starts to blow you.
            "You unzip your pants and pull them down, letting your hard cock spring free. She watches it bounce up and down for a few seconds."
            me "We've got a little time before Nora gets here. I could really use a quick blowjob before we get busy with work."
            $promised_cum = False
            show steph strip3 at right
            "Stephanie thinks for a moment, then starts to pull her shirt off."
            if stephO.cumslut:
                steph "Okay, but I want you to promise me you'll cum in my mouth. You know how much I like it when you do that. Promise?"
            else:
                steph "Alright, I think we've got time for that. Promise you'll cum in my mouth?"
            menu:
                "Of course.":
                    me "Of course Stephanie, I'll make sure to fill up that pretty little mouth of yours."
                    $promised_cum = True
                    steph "Good, you know exactly what I like."
                "We'll see.":
                    me "We'll see what I'm feeling like when I'm ready."
                    $promised_cum = False
                    steph "Fine, I'll just have to find some way to convince you."
            "Stephanie undoes her bra and drops it to the floor, letting her tits bounce free. She gets up from her chair and kneels down in front of you, taking your cock in her hand."
            show steph blow20 at right
            $ stephO.inc_blow()
            "She looks up at you and runs her tongue along the bottom of your shaft, pausing to kiss the tip before moving back down and licking it along the side."
            me "Ah, that feels great Steph."
            "She keeps licking you until your whole dick is completely wet, then presses her lips against your tip and lets you slide in slowly."
            "Stephanie pauses when you're completely in her mouth, using just her tongue to pleasure you. After a few moments she starts to bob her head up and down, blowing you slowly."
            if promised_cum:
                me "That's a good girl. Just keep going like that and you'll be swallowing cum in no time."
            else:
                me "That's a good girl. Keep it up and maybe I'll finish in your mouth like you want."
            show steph blow21 at right
            "Stephanie moans softly up at you as she speeds up her blowjob. She puts her hands behind her back, using just her mouth to service you."
            "You enjoy the feeling of her wet mouth and skillful tongue for a few minutes. The only sound in the lab is the rhythmic wet smacking from Stephanie's mouth and the occasional quiet moan."
            menu:
                "Grab her head and take over." if stephO.slut_score > 85:
                    #Hold her head and skull fuck her."
                    me "God, I love the way your throat feels Steph."
                    "You reach down and place your hands on either side of Stephanie's head. She mumbles up at you, the sound muffled because of your cock down her throat."
                    me "Just hold still, I want to face fuck you a little."
                    show steph blow24 at right
                    "You piston your hips back and forth, pumping your dick in and out of Stephanie's mouth. She keeps her mouth wide open for you, spit running down her chin and dripping onto her tits."
                    "After a few minutes you press yourself down her throat and stay there. Stephanie works her tongue along your shaft and looks up at you."
                    me "Fuck, you look good with a cock down your throat. I bet you like it, don't you."
                    "She purrs like a kitten, throat rumbling pleasantly around your sensitive shaft."
                    me "I thought so. Now lets give the little cum slut what she wants."
                    "You finally pull back and go back to fucking her throat some more. She breaths heavily through her nose, but doesn't pull off and keeps her mouth wide open."
                    "Soon her wet, tight throat has drawn you to the edge of your orgasm. You pump faster for a few strokes, getting ready to finish."
                    menu:
                        "Cum down her throat.":
                            me "Ah, here we go!"
                            "You skull fuck Stephanie until you start to cum, then push yourself deep down her throat again. She quivers like a leaf as you shoot your load right into her stomach."
                            if promised_cum:
                                me "That's a good slut. Just drink it all down."
                            else:
                                me "Just what you wanted, right? A stomach full of hot cum? Well, you've certainly earned it."
                            show steph blow25 at right
                            $ stephO.inc_cum_mouth()
                            $ stephO.inc_cum_swallow()
                            "She shivers again, eyes rolled up as she tries to moan past your cock. Her hands are between her legs now, rubbing her pussy through her pants."
                            "Her throat spasms a few times, drawing out the last drops of semen from it. You keep one hand on the back of her head and stroke her cheek with the other."
                            me "That's right, cum for me Stephanie. Cum like a whore with my cock down your throat."
                            "Her moans turn into wet gurgles as she looks up at you, eyes half shut and shaking with pleasure. Finally you let go of her head and she pulls back, gasping for air."
                            steph "Oh god..."
                            "She finally relaxes, hands dropping to her side as she pants loudly."
                            "You take a deep, contented sigh and pull your pants back up."
                            me "That was great Stephanie, we'll have to do it again. I'm sure you'd like that."
                            "Stephanie nods, still a little dazed from her orgasm."
                            steph "Yeah... I should get ready before Nora gets here."
                            me "You do that, I'm going to stretch my legs before work. See you soon."
                            hide steph
                            "You head out of the lab while Stephanie collects her clothes, taking a short walk towards the center of campus."

                        "Cum on her face.":
                            if promised_cum:
                                me "Sorry Steph, but I want to see your face covered in cum!"
                            else:
                                me "Here we go Steph!"
                            "You skull fuck Stephanie until you start to cum, then pull out and stroke yourself off."
                            if promised_cum:
                                steph "Wait, I want it in my mouth!"
                                me "Sorry, too late!"
                            else:
                                steph "Fine, do it! I want it in my mouth next time though!"
                            show steph blow26 at right
                            $ stephO.inc_cum_over()
                            "Stephanie drops her hands between her legs, rubbing her pussy through her pants while you blow your load onto her face. She pants softly as you cover her from forehead to chin."
                            "She shivers with pleasure, approaching her own orgasm as you finish covering her face."
                            steph "At least let me clean you up. Please?"
                            me "Fine, here you go you dirty cum slut."
                            show steph blow27 at right
                            "You present your cock to Stephanie again. She leans forward and slips you into her mouth, licking it eagerly."
                            "She rubs her crotch while she drinks up the last few drops of cum, quivering as she finally climaxes."
                            "When she's done she sits back and takes a deep breath."
                            steph "Wow..."
                            me "That was great Stephanie, we'll have to do it again. You look great covered in cum, by the way."
                            if stephO.cumslut:
                                "She runs a finger along her chin, then licks it clean. She sighs happily as she savours the taste of your sperm."
                            else:
                                "She runs a finger along her chin, then licks the sperm off of it."
                            steph "Thank you [inputName], you know where to find me. I should really get cleaned up now, Nora's going to be here soon."
                            me "Right. I'm going to take a quick walk and stretch my legs, see you later."
                            hide steph
                            "You pull up your pants and leave the lab while Stephanie looks for some tissue to clean up with. You take a short walk back to the center of campus."

                        "Cum on the floor and have her lick it up." if stephO.slut_score > 115 or (stephO.cumslut and stephO.slut_score > 80):
                            me "Here we you fucking slut!"
                            "You skull fuck Stephanie until you're right on the edge, then pull out with a wet pop and grab your cock to stroke yourself off."
                            if promised_cum:
                                steph "Wait! I want it in my mouth!"
                                "You hold Stephanie's head in place with one hand while you turn to the side and cum onto the tile floor beside her."
                                me "Ah... There you go Stephanie, clean it up."
                                "Stephanie scowls back at you, crossing her arms."
                                steph "Dick, I wanted it in my mouth."

                            else:
                                steph "Wait, what are you doing?"
                                "You hold Stephanie's head in place with one hand while you turn to the side and cum onto the tile floor beside her."
                                me "Well, there it is if you really want it."
                                steph "You couldn't have just finished in my mouth?"
                            "You shrug, and after a moment she sighs and bends over, lowering her head to the floor."
                            show steph blow28 at right
                            $ stephO.inc_cum_swallow()
                            "Stephanie's breasts brush against the ground as she runs her tongue through the largest puddle of cum, her ass in the air pointing towards you."
                            "She pauses to swallow, then does it again."
                            me "Good girl, make sure to get it all. A cum slut like you wouldn't let it go to waste, right?"
                            "With Stephanie bent over you can see a faint wet patch on her pants. She must have cum hard while you were face fucking her."
                            "When she's finally finished licking up your sperm from the floor she sits up and looks at you."
                            steph "Can I please have it in my mouth next time?"
                            me "We'll see. You should get dressed before Nora gets back. I'm going to take a walk and stretch my legs."
                            hide steph
                            "Stephanie nods and grabs her clothes. You pull up your pants and head out of the lab, taking a short walk towards the center of campus."

                "Let her keep going.":
                    #More blowjob
                    "You run your hand along Stephanie's cheek, brushing her hair to the side. She looks up at you, making eye contact while she takes your cock down her throat."
                    me "Mmm, you've almost got me there Steph. Just a little longer."
                    "She moans again and speeds up. She keeps her tongue flat on the bottom of her mouth, letting you slide over it and right into her throat on each stroke."
                    "After another minute of pleasure your core starts to tense up as you approach your climax."
                    menu:
                        "Cum in her mouth.":
                            if promised_cum:
                                me "I'm almost there Steph. Lets fill up that slut mouth of yours, I can tell how much you want it."
                            else:
                                me "I'm almost there Steph, keep going. I think you've earned your treat."
                            "Stephanie moans loudly, throating you while she plays with one of her breasts."
                            "You tense up and grunt as you start to cum. Stephanie pulls back until just your tip is in her mouth, letting you fill it up with your sperm."
                            show steph blow22 at right
                            $ stephO.inc_cum_mouth()
                            $ stephO.inc_cum_swallow()
                            "She waits until you're done, then swirls her tongue around your sensitive tip to get the last few drops and pulls off. She looks up at you with her mouth open so you can have a good look."
                            me "Fuck that's hot. Now swallow it."
                            "Stephanie nods and closes her mouth, taking a few seconds to drink down your load. She sighs when she's finished, then opens up again so you can see it's all gone."
                            if promised_cum:
                                steph "Ah, thank you [inputName], that tasted amazing."
                                "She sighs and licks her lips."
                            else:
                                steph "Ah, I knew I could convince you."
                                "She winks at you, licking her lips."
                            steph "We should probably get dressed before Nora gets back, we should do this again though."
                            "You pull up your pants while Stephanie collects her clothes from the floor."
                            me "We definitely should. I'm going to take a short walk and stretch my legs, talk to you soon."
                            hide steph
                            "You leave the lab and head upstairs, heading towards the center of campus."

                        "Cum on her face.":
                            "You let Stepahnie suck you off until you're right on the edge, then take a step back and pull out of her mouth with a wet pop. You grab your cock and stroke yourself off."
                            me "I'm almost there Stephanie. I'm going to cover that pretty face of yours!"
                            if promised_cum:
                                steph "But you said you'd let me drink it!"
                                "You grunt and start to orgasm, blowing your load over Stephanie's face. She opens her mouth and lets as much cum as possible land inside."
                            else:
                                steph "Fine, just please let me drink it next time."
                                "You nod and grunt as you start to orgasm, blowing your load over Stephanie's face. She opens her mouth and lets as much cum as possible land inside."
                            show steph blow23 at right
                            $ stephO.inc_cum_over()
                            "When you're done you give a deep contented sigh and step back, admiring your work. She looks up at you, running a finger along her chin then licking the sperm off of it."
                            if promised_cum:
                                steph "You bastard, you promised me."
                                "She pouts and crosses her arms, cum dripping down her face with one eye stuck shut."
                                me "Ah, sorry Steph, I just couldn't resist. You look so good like that though."
                                "She sighs, but finally smiles up at you."
                                steph "Thank you. How about next time then?"
                                me "We'll see, maybe if I'm in the mood."
                                "Stephanie nods and shrugs, wiping up some more cum with her finger and licking it off."
                            else:
                                steph "Wow, it feels so warm..."
                                "She looks up at you and smiles, cum dripping down her face with one eye stuck shut. Wipes up some more cum and drinks it up."
                                me "Ah, thanks Steph. You look so good like that, by the way."
                            steph "I should probably get dressed before Nora gets here."
                            me "That's a good idea. I'm going to take a quick walk and stretch my legs. See you soon."
                            hide steph
                            "You head out of the lab, leaving Stephanie to collect her clothes and get cleaned up. You take a short walk towards the center of campus."

            $ steph_hub.inc_level(4)
            $ stephO.change_resist(-steph_hub.use_red(4,stephO.resist_score))

        "Fuck her." if stephO.slut_score > 80:
            #Asks you how you want to do it.
            "You unzip your pants, letting your hard cock spring free. Stephanie watches it bounce up and down, biting her lip a little."
            me "Nora won't be here for a little bit, how do you feel about a quick fuck?"
            "Stephanie nods, standing up and pulling off her shirt almost immediately."
            steph "That sounds like a great idea. Lets get all of this out of the way."
            show steph strip38 at right
            "She strips down in front of you, finally kicking her panties to the side. She crosses her arms behind her back, pushing her tits out towards you."
            steph "So, how do you want me?"
            menu:
                "Have her ride you.":
                    "You grab Stephanie's chair and turn it around so you can sit down."
                    me "Come on and ride me Steph, I want to see you bouncing on my dick."
                    show steph fuck33 at right
                    $ stephO.inc_sex()
                    "She smiles and nods, walking towards you. She spreads her legs and stradles you, arms on the back of the chair while she lowers herself down."
                    "When the tip of your cock brushes her pussy you feel how wet she is, and she lets out a soft sigh."
                    steph "I really, really need this."
                    "You rest your hands on her hips, guiding her farther down. You slip into her wet pussy easily and feel her shiver with pleasure."
                    "Stephanie takes a moment to get comfortable once you're fully inside her, then starts to move her hips up and down. She leans forwards into you, pressing her tits into your chest and moaning in your ear."
                    me "That feels amazing Steph. Keep going, you'll have me cumming soon."
                    steph "Mmhmm, me too. Fuck, that's nice."
                    show steph fuck34 at right
                    "She gasps as you tighten your grip on her hips and start to drive them up and down. Her pussy makes wet smacking sounds each time you thrust into it."
                    "It's not long before her tight, dripping cunt has you on the edge. Stephanie shivers against your body, obviously having an orgasm of her own."
                    menu:
                        "Cum inside her.":
                            "You reach around and grab Stephanie's ass in both hands, guiding her as she rides your cock."
                            me "Ah, here we go Steph!"
                            "Stephanie moans into your ear as you squeeze her ass cheeks and work you own hips to meet hers, fucking her as hard as you can."
                            "You pull her down hard as you start to cum, pushing yourself as deep as possible. She quivers against you, climaxing as you empty your balls into her tight cunt."
                            "When you're done you relax your grip, bouncing her ass cheeks up and down a few times and then giving them a light slap to get her moving."
                            if stephO.cumslut:
                                steph "Oh god, there's so much. It's like you're just trying to get me pregnant."
                            else:
                                steph "Oh god that was hot."
                            show steph fuck35 at right
                            $ stephO.inc_cum_inside()
                            "Stephanie pulls off slowly, legs shaking. Almost immediately your cum starts to drip out of her pussy and down her inner thigh."
                            me "That was great, we should do it again some time."
                            "She nods, leaning against her desk for support."
                            if stephO.preg_response_ok():
                                steph "Well, you know where to find me. I should get cleaned up before Nora gets in."
                            else:
                                steph "Try not to cum in me next time if you do. I know I get carried away, but I can't afford to get pregnant or something. Now I need to get cleaned up before Nora gets in."
                            "You stand up and get dressed while Stephanie tries to find some tissues."
                            me "You do that. I'm going to take a walk and stretch my legs. See you soon."
                            hide steph
                            "You head out of the lab and take a quick walk to the center of campus."

                        "Cum in her mouth.":
                            me "Ah, I'm almost there Stephanie. Do you want it in your mouth?"
                            "She nods and whispers into your ear."
                            steph "Yes, please! Oh, fuck yes!"
                            "You guide her up and down for a few more quick strokes, then slap her ass to get her up and moving."
                            show steph fuck37 at right
                            $ stephO.inc_cum_mouth()
                            $ stephO.inc_cum_swallow()
                            "Stephanie gets off, falling to her knees in front of you and opening her mouth wide."
                            "You grab your cock and stroke yourself off to completion, placing the tip of your cock on her lips. She moans loudly as you fire your hot load right onto her tongue."
                            me "There we go, good girl!"
                            show steph fuck36 at right
                            "Stephanie waits until you're completely done, then swirls her tongue around your tip to get the last few drips and pulls off. She sits back, opening her mouth so you can have a look."
                            me "Fuck that's hot. Does it taste good?"
                            "Stephanie moans softly and nods, hands between her legs as she rubs her own clit."
                            me "Okay, you can swallow."
                            "She closes her mouth, maintaining eye contact as she drinks down your cum. When she's done she takes a deep sigh and opens wide, letting you see that it's all gone."
                            steph "Oh god, that was great."
                            me "I thought you'd like that, you dirty cum slut."
                            "Stephanie takes a second to catch her breath, then stands up and leans against her desk."
                            steph "We should do it again some time, you know where to find me."
                            me "We should. Right now I'm going to take a walk before Nora gets here. I'll see you in a little bit."
                            hide steph
                            "You leave the lab while Stephanie collects her clothing and head towards the center of campus."

                        "Cum on her body.":
                            me "I'm almost there Stephanie. I want to cover you with it."
                            "In response she moans softly into your ear. You squeeze her ass and work it up and down a few more times, then give her a spank to get her up and moving."
                            "She slides up and off, the last stroke of her wet pussy pushing you over the edge."
                            "You sit forward on the chair and stroke yourself off as Stephanie drops to the floor, leaning back with her legs spread as you start to cum."
                            show steph fuck38 at right
                            $ stephO.inc_cum_over()
                            "She gasps as your hot sperm lands on her body. You start with her tits and work towards her cunt, with each pulse landing farther down than the last."
                            "You shake off the last few drops onto her and sit back, both of you taking a moment to catch your breath."
                            "After a moment Stephanie gets onto her knees and looks up at you from between your legs."
                            if stephO.cumslut:
                                steph "Can I clean that up for you?"
                                show steph fuck39 at right
                                "You nod, and Stephanie leans forward and slips your sensitive cock into her mouth. Her tongue works up and down it's length, licking off her own juices and your own cum."
                                "Soon she's licked every inch of your dick and slides off again. She stands up, legs shaking, and looks down at herself."
                                steph "Wow, you really did cover me..."
                            me "And it felt amazing. We should do this again some time."
                            steph "Well, you know where to find me. I should really get cleaned up before Nora gets here."
                            "You stand and pull up your pants while Stephanie looks for some tissue."
                            me "Sure. I'm going to take a quick walk to stretch my legs. See you later."
                            hide steph
                            "You leave the lab and head towards the center of campus."

                "Fuck her doggy style." if stephO.slut_score > 100:
                    #Sex
                    "You wrap your arms around Stephanie and pull her against you. You kiss her and she kisses you back, tongues wrapped around each other."
                    "Your hands drop to her ass, playing with her cheeks while you make out. After a few moments you break the kiss."
                    me "Turn around, I want to fuck you from behind."
                    show steph fuck40 at right
                    $ stephO.inc_sex()
                    "She bites her lip and nods, turning around to face her desk. She slides her chair out of the way and plants her hands on the surface, ass pointed towards you."
                    "You stand behind her, cock resting between her cheeks for a moment. She wiggles her ass at you, legs spread and pussy obviously wet."
                    steph "Come on, don't make me wait."
                    "You line your cock up with her cunt, taking a moment to rub your tip up and down to get it wet. She gasps when you slide into her, slipping your full length in on the first stroke."
                    me "That's what you want? A nice big dick in your pussy?"
                    "She moans as you start to thrust in and out of her. She presses her hips back to meet yours, helping you get even deeper."
                    steph "Fuck yes! Ah, I love how you feel!"
                    show steph fuck41 at right
                    "You grab her hips and fuck her as fast as you can manage. She drops her shoulders and moans loudly, tits rubbing against her desk and scattering her paperwork."
                    me "Do you like being a dirty fucking slut?"
                    steph "Yes! Oh god yes! Fuck me however you want, cum wherever you want! I'm just your dirty little toy!"
                    "Her legs quiver against the desk as you fuck her, each thrust making her ass bounce and jiggle. Her tight wet pussy feels amazing, and you can feel your orgasm approaching."
                    menu:
                        "Cum inside her.":
                            me "Here I come Steph!"
                            "She moans in response, enjoying her own climax as you fuck her from behind. You give her a few quick thrusts, then hold yourself deep inside of her as you start to cum."
                            "You give a few small thrusts as you empty your balls into Stehanie's cunt, making her gasp softly with each new pulse. When you're done you step back and slip out of her."
                            show steph fuck42 at right
                            $ stephO.inc_cum_inside()
                            "She pants heavily as she leans against the desk, your cum almost immediately dripping out of her pussy."
                            if stephO.cumslut:
                                steph "Wow... There's just so much of it. Ah... I wonder if you're going to get me pregnant like this..."
                            else:
                                steph "Wow... it's so warm..."
                            me "That felt great Stephanie, we should do it again some time."
                            "You pull up your pants while she nods weakly, slowly standing up on shaking legs."
                            if stephO.preg_response_ok():
                                steph "Yeah, we should. I should get cleaned up before Nora gets here."
                            else:
                                steph "Yeah, but... You really shouldn't cum in me when I'm not on my birth control. I need to get cleaned up before Nora gets here now."
                            me "Sure. I'm going to take a walk and stretch my legs, see you around."
                            hide steph
                            "You leave the lab while Stephanie collects her clothes and head towards the center of campus."

                        "Cum in her mouth.":
                            me "I'm almost there, I want to fill up your mouth!"
                            "Stephanie moans loudly in response, pussy twitching around your cock as you fuck her from behind. You give her a few quick thrusts, then pull out of her wet cunt and wait for her to turn around."
                            show steph fuck27 at right
                            "She drops to her knees and faces you, mouth open wide and hands behind her back."
                            "You place the tip of your cock on her lips and stroke yourself to completion, blowing your load into her eager mouth. With each pulse of hot cum she moans again."
                            me "Fuck you're a good cum dumpster Steph. Enjoy!"
                            "When you're done she tilts her head forward and slips your full length into her mouth. She gives your sensitive cock a slow blowjob, licking off her own juices from it while she has a mouthful of your semen."
                            show steph fuck26 at right
                            $ stephO.inc_cum_mouth()
                            $ stephO.inc_cum_swallow()
                            "Finally she pulls back and looks up, opening her mouth so you can look at the pool of white. While you watch she slips her hands between her legs, rubbing her own clit."
                            "You enjoy the view for a while as Stephanie gargles your cum in her mouth. She plays with it a little, her tongue dipping in and out of it a few times."
                            me "Alright, now swallow for me."
                            "She nods and closes her mouth, throat working for a moment as she drinks down your sperm. When that's done she opens up again, showing that it's all gone."
                            me "Damn, that was hot. I can tell what you like."
                            steph "Yeah. It tasted really good, by the way. I should get dressed, Nora's going to be here any minute now."
                            me "Alright, I'm going to take a quick walk and stretch my legs. See you soon."
                            hide steph
                            "You leave the lab while Stephanie collects her clothes and head towards the center of campus."

                        "Cum on her ass.":
                            me "Here I come Steph!"
                            "She moans in response, enjoying her own climax as you fuck her from behind. You keep going until you're right on the edge, then pull out of her wet pussy and stroke yourself off."
                            show steph fuck43 at right
                            $ stephO.inc_cum_over()
                            "Stephanie gasps softly as you spray your load onto her ass cheeks. When you're done you've covered her butt with your hot sperm, with some of it dripping down onto her pussy as well."
                            steph "Wow... it's so warm..."
                            "You enjoy the view for a few moments, then wipe the last few drips of cum off your tip onto her ass and pull your pants up."
                            me "That felt great Steph, we should do it again some time."
                            "She stands up, legs shaking a little, and turns to face you."
                            steph "We should. You know where to find me."
                            "She steps close to you, pressing her tits against your chest while she whispers in your ear."
                            steph "I want it in my mouth next time, don't go waisting it on my ass."
                            me "I'll see what I can do."
                            "Stephanie steps back and starts to collect her clothes."
                            steph "I should get cleaned up, Nora's going to be here any second."
                            me "Alright, you do that. I'm going to take a quick walk and stretch my legs before work. See you soon."
                            hide steph
                            "You leave the lab while Stephanie starts to clean up and head towards the center of campus."

                "Anal her" if stephO.slut_score > 130 or (stephO.anal and stephO.slut_score > 80):
                    #Sex
                    "You wrap your arms around Stephanie and pull her against you. You kiss her and she kisses you back, tongues wrapped around each other."
                    "Your hands drop to her ass, playing with her cheeks while you make out. After a few moments you break the kiss."
                    me "Turn around, I want to fuck that tight little asshole of yours."
                    "She bites her lip and nods, turning around to face her desk. She slides her chair out of the way and plants her hands on the surface, ass pointed towards you."
                    "You stand behind her and line your cock up with her asshole, pressing the tip against it gently."
                    me "Ready?"
                    if stephO.anal:
                        steph "Yeah, I'm ready. Fuck me like a dirty little slut [inputName]. Give me what I want."
                    else:
                        steph "I think so, yeah."
                    show steph fuck44 at right
                    $ stephO.inc_sex()
                    "You spit on your hand and stroke your shaft a few times, getting it wet and slippery. With that done you push yourself into Stephanie's ass."
                    steph "Oh fuck... Easy, easy."
                    "You push yourself into Stephanie inch by inch, letting her ass get used to your size. She's incredibly tight, gripping your shaft the whole time."
                    "Once she's had some time to adjust you start to thrust in and out, holding her hips while you fuck her."
                    steph "Fuck, oh shit, ah..."
                    "Stephanie lets out a few breathless words, leaning forward and dropping her shoulders onto the desk while you use her ass."
                    me "You feel amazing Steph, so god damn tight."
                    show steph fuck45 at right
                    "You speed up, pulling back on her hips as you fuck her to get a little deeper into her. Stephanie yelps with each thrust, breasts sliding along her desk."
                    steph "Keep, ah... Keep going! Fuck me until you cum!"
                    "Stephanie quivers like a leaf, shaking against the desk while you fuck her. Her tight ass feels amazing, and it's not long before you tense up, orgasm approaching."
                    menu:
                        "Cum inside her.":
                            me "I'm almost there!"
                            "Stephanie moans loudly as you speed up, plunging in and out of her asshole. You push yourself as deep as you can manage when you start to cum."
                            "She gasps as you empty your balls into her, filling her up with hot semen. You wait for a few moments until you're finished, then start to fuck her again."
                            me "Damn, that feels even better. Nice and lubed up."
                            steph "Fuck! Oh fuck!"
                            "Stephanie yells out and collapses, putting her full weight against the desk while you fuck her slippery ass. She quivers as she climaxes, tightening around your shaft."
                            show steph fuck46 at right
                            $ stephO.inc_cum_inside_ass()
                            "After a few more thrusts you pull your softening cock out of her and step back, watching as your cum leaks out of her asshole and down onto her pussy."
                            me "Wow, that felt great. We'll have to do that again some time."
                            if stephO.cumslut:
                                steph "Yeah, we will. Hey [inputName], could I clean you up a little bit? I think there's still a little bit of cum I could get off of you."
                                "She slides to the ground and turns around, ending up on her knees in front of you. You rest the tip of your cock on her lips."
                                me "Sure, go to town Stephanie."
                                show steph fuck37 at right
                                "Stephanie tucks her arms behind her back and just uses her tongue to clean along the bottom and sides of your shaft. She eagerly licks up any trace of semen she can find on you, then leans back and sighs happily."
                                me "Nora's going to be here soon, so you should probably get cleaned up. I'm going to take a walk and stretch my legs."
                                hide steph
                                "Stephanie nods, licking her lips while your cum drips out of her ass onto the floor. You pull up your pants and head out of the lab, heading towards the center of campus."
                            else:
                                steph "Yeah..."
                                me "Nora's going to be here soon, so you should probably get cleaned up. I'm going to take a walk and stretch my legs."
                                hide steph
                                "Stephanie nods weakly, still leaning on her desk for support. You pull up your pants and head out of the lab, heading towards the center of campus."

                        "Cum in her mouth.":
                            me "I'm almost there, get on your knees!"
                            "You give her ass a few more thrusts, then pull out and step back. Stephanie turns and gets onto her knees, looking up at you."
                            me "Suck me off, I want to finish in your mouth."
                            show steph fuck37 at right
                            "She nods eagerly and leans forward, slipping your cock into her mouth. She wastes no time, blowing you fast and deep with her tongue licking at the bottom of your shaft."
                            "A short while later she pushes you over the edge. You and Stephanie both let out a moan as you start to cum."
                            "She pulls back, leaving just your tip in her mouth as you empty your balls inside. She shivers and moans, climaxing as you fill her mouth up with hot sperm."
                            show steph fuck48 at right
                            $ stephO.inc_cum_mouth()
                            $ stephO.inc_cum_swallow()
                            "you reach down and run a hand over her cheek while she orgasms, pushing your cock a little deeper into her mouth at the same time."
                            me "That's it, cum like a dirty fucking whore. You're just a cock hungry cum dumpster, aren't you Stephanie?"
                            "She nods and moans, careful not to let your shaft slip out of her mouth."
                            me "Now drink it down, every last drop."
                            "She takes a breath in through her nose, then her throat bobs up and down as she swallows your load. When she's done you step back and she takes a deep, shuddering breath."
                            steph "Fuck..."
                            me "That was hot, we should do it again some time."
                            "Stephanie nods, standing up slowly and leaning against her desk for support."
                            me "I'm going to take a quick walk before Nora gets here. You should probably get dressed."
                            hide steph
                            "You head out of the lab while Stephanie collects her clothes and head towards the center of campus."

                        "Cum on her ass.":
                            me "I'm almost there!"
                            "Stephanie moans loudly as you speed up, plunging and out of her asshole. You pull out at the last moment, stroking your cock as you cum over her ass cheeks."
                            show steph fuck47 at right
                            $ stephO.inc_cum_over()
                            "You make sure to get every last drop onto her butt, then use your tip to spread it around. When you're done you step back and admire your work."
                            steph "Wow... It feels so warm..."
                            me "That felt great Stephanie. Could you come clean me up a bit?"
                            show steph fuck37 at right
                            "Stephanie turns around and nods, dropping to her knees in front of you. She leans in and opens up her mouth, slipping your shaft inside."
                            "For a few moments she licks around your sensitive cock, cleaning it up for you. When she's done she sits back and takes a deep breath."
                            me "We'll have to do that again some time. Nora's going to be here soon though, so you should probably get cleaned up."
                            steph "Yeah..."
                            me "I'm going to take a walk before work and stretch my legs. I'll see you in a little bit."
                            hide steph
                            "You pull up your pants and head out of the lab, leaving Stephanie to get herself cleaned up. You take a short walk towards the center of campus."

            $ steph_hub.inc_level(5)
            $ stephO.change_resist(-steph_hub.use_red(5,stephO.resist_score))

        "Give her some serum and train her.\n-15 Influence, -2 Serum" if stephO.slut_score > stephO.training_threshold and (player_blue_serum + player_purple_serum + player_red_serum > 1):
            menu:
                "Train her to be a cum slut from now on." if not stephO.cumslut:
                    call cumslut_descrip("Stephanie")
                    menu:
                        "Continue with the training.":
                            call steph_train_cumslut
                        "Change your mind and leave.":
                            return False

                "Train her to be an anal lover from now on." if not stephO.anal:
                    call anal_descrip("Stephanie")
                    menu:
                        "Continue with the training.":
                            call steph_train_anal
                        "Change your mind and leave.":
                            return False

                "Train her to be a free use slut from now on." if not stephO.freeuse:
                    call freeuse_descrip("Stephanie")
                    menu:
                        "Continue with the training.":
                            call steph_train_freeuse
                        "Change your mind and leave.":
                            return False

                "Train her to be an exhibitionist from now on." if not stephO.exhib:
                    call exhib_descrip("Stephanie")
                    menu:
                        "Continue with the training.":
                            call steph_train_exhib
                        "Change your mind and leave.":
                            return False

                "Change your mind and leave.":
                    return False

        "Chat about the lab for a bit.":
            "You spend a few minutes chatting about your lives."
            return False
            #TODO add a minor scene at high influence where you bring her home to fuck Lily/Mom

    return True

######################
##Alexia's Hub Scene##
######################

label hub_alex:
    menu:
        "Ask her to visit the beach with you." if alexO.slut_score > 20 and beach_girl is None and beach_unlocked:
            if alexO.beach_count == 0:
                me "So, I heard they've opened up the beach for the summer. I think I'm going to take a trip up there this Saturday if you wanted to come along."
                alex "Oh cool, the beach sounds awesome. How would we get up there?"
                me "There's a direct bus that runs in the morning and evening. Should make the trip a breeze."
                alex "Count me in then! I'll get my stuff ready when I get home."

            else:
                me "So I'm going to take another trip up to the beach this weekend, if you'd like to come along with me."
                alex "Sure, that sounds awesome."

            "You and Alexia chat about nothing in particular for a few more minutes, until she has to head out to her class."
            $ beach_girl = "Alex"
            return False

        "Cancel your trip to the beach." if beach_girl == "Alex":
            me "Oh, well you're here I should let you know. Something came up on Saturday, so I'll have to take a rain check on our trip to the beach."
            alex "Ah, damn. Okay, we can make plans for some other weekend."
            me "Sure, I'll let you know if I'm free."
            "You and Alexia chat about nothing in particualr for a few more minutes, until she has to head out to her class."
            $ beach_girl = None
            return False

        "Talk to her about her birth control." if alexO.slut_score > 100 or (alexO.slut_score > 70 and alexO.cumslut):
            if alexO.bc:
                #intro
                me "Oh, since we've got some time alone I wanted to ask you something. Are you on the pill right now?"
                if alexO.cumslut or alexO.freeuse:
                    alex "Yeah. Thank god for it, or I'm sure I'd be pregnant already. Why do you ask?"
                else:
                    alex "Yeah, I am. Why do you ask?"
                menu:
                    "Tell her to stop taking her birth control pills.":
                        $ alexO.bc = False
                        me "I wanted you to stop taking. Could you do that for me?"
                        if alexO.freeuse:
                            alex "Oh wow... I'd have to be a lot more careful when I fool around then, or I'd end up getting pregnant."
                        else:
                            alex "Oh wow... we would have to be a lot more careful when we fool around then, so you don't get me knocked up."
                        me "I think I can handle being careful. I love the risk each time we do it, it's such a rush."
                        alex "Mmm, I know what you mean. Alright, I'll stop taking the pill starting tomorrow."

                    "Don't do anything about her birth control.":
                        me "I was just curious and wanted to make sure we weren't going to get ourselves into any trouble together."
                        alex "I mean, it's not 100% effective I guess. If you really kept at it we might have to worry, but I think we're pretty safe." #might need an escape character for the percent, not sure.
                        me "Alright, that's good to know."

            else:
                #intro
                me "Since we've got some time alone, I wanted to ask you something. You stopped taking the pill, right?"
                alex "Yeah, I stopped when you asked me to. Is everything alright?"
                menu:
                    "Tell her to start taking her birth control pills again.":
                        $ alexO.bc = True
                        me "Everything is fine, I just think you should start taking it again. I don't want you to get knocked up if we keep having sex."
                        alex "Okay, if you want me to I'll start taking them again tomorrow."

                    "Don't do anything about her birth control.":
                        me "Everything is fine, I just wanted to make sure nothing had changed."
                        if alexO.cumslut:
                            alex "Don't worry [inputName], I know there's a chance you'll knock me up and I still love it when you cum in me. Keep filling me up and I'll be a happy woman."
                            me "Good to know, I'll do what I can for you."
                        else:
                            alex "Don't worry [inputName], I'll ask you before I change anything important like that."
                            me "Good to know, thanks Alexia."

            "You and Alexia spend a few more minutes chatting before she has to leave for her next class."
            return False

        "Ask her to strip for you." if alexO.slut_score > 20:
            #Show off a little
            me "This is a pretty nice find, nice and private."
            alex "Yeah, it's a great place to come and relax between classes."
            me "Since it's just the two of us, could I ask a favour?"
            alex "And what would that be?"
            me "You're looking particularly hot today, I'd love to see you without that shirt on."
            if alexO.slut_score > 30:
                show alex strip17 at right
                "She reaches for her sweater right away, pulling it up and off."
                alex "There you go. Like the underwear?"
                me "Yeah, it's cute. You don't really need that skirt either, do you?"
                show alex strip3 at right
                "She winks at you and turns around, undoing her skirt and letting it fall to the ground."
                alex "I think you're right. Nobody ever comes in here anyway."
                show alex strip18 at right
                "Alexia turns back to you and cups her breasts in her hands, gently bouncing them up and down."
                alex "God, could you imagine if someone came in right now? They'd see me here, half naked and showing off for you."
                "More boob jiggling, nearly causing them to slip out of their cups. She giggles and takes a moment to make sure they're settled in."
                menu:
                    "Show off for me.":
                        #A few different angles
                        me "I'm sure they'd be just as impressed as I am. How about you give me a peek of what they're missing?"
                        alex "Missing? Oh, you want an even better look at my tits?"
                        show alex strip19 at right
                        "She pulls up her bra, pausing for a moment to tease you before letting her boobs fall out from the bottom of her cups."
                        me "Wow, very nice Alexia."
                        show alex strip20 at right
                        "She smiles and blushes, and you can see her nipples get hard while you stare at them. After a few moments she turns around and bends over, hands on her thighs."
                        alex "And I'm sure you wanted to see this too, right?"
                        show alex strip21 at right
                        "She reaches between her legs with one hand, pulling her panties to the side and letting you catch a glimpse of her pussy, then plants her hands on the wall."
                        me "Having a good time showing off? I know I'm enjoying watching you."
                        alex "Yeah, I am. It feels so dirty, doing it here at school."
                        show alex strip3 at right
                        "She shakes her ass at you a little, then stands up again and straightens out her underwear."

                    "Touch yourself.":
                        #Alex touching herself
                        me "I'm sure they'd be just as impressed as I am. How about you touch yourself a little for me."
                        alex "Mmm, that sounds like a good idea. Just a little."
                        "She turns around, planting a hand on the wall and slipping the other between her legs."
                        show alex strip22 at right
                        "Alexia moans softly as she slides a finger up and down the length of her pussy, rubbing it through her panties."
                        me "That's really hot. Just pull those to the side and go for it."
                        alex "[inputName], you really are a terrible influence."
                        show alex strip23 at right
                        "She giggles a little, then sighs when she pulls her panties out of the way and slides a finger into her own cunt."
                        alex "Oh fuck, that's nice..."
                        "For a few minutes you watch while Alexia fingers herself while leaning up against the wall."
                        alex "Just keep an eye out for anyone coming in, ah..."
                        me "I'm not sure what I could really do about that Alexia. You're already naked and touching yourself, that would be hard to explain."
                        alex "Oh god, they'd really just see me like this. Fuck..."
                        show alex strip3 at right
                        "Her legs quiver while she talks, her breath comming faster and faster. Finally she stops and tenses up, gasping suddenly as she climaxes. She takes a moment to recover, then turns back to face you."



                if alexO.slut_score > 50:
                    #Show off other outfits
                    alex "That was actually really fun [inputName]. I've got a locker nearby with some other stuff, if you'd like to take a look."
                    me "I'd definitely like to."
                    show alex casual at right
                    "Alexia smiles and nods, getting dressed quickly and heading over to the door."
                    alex "Back in a second."
                    "She leaves and reappears a few minutes later. She drops a backpack onto the table next to you, opening it up and pulling out a collection of clothing."
                    me "You just have all this hanging around here?"
                    alex "I wanted to wear some of it around, but never found the right opportunity I guess. It's not exactly the kind of stuff you'd wear every day. Now, what do you want to see?"
                    menu:
                        "Swimsuit":
                            me "Alright, how about that swimsuit."
                            show alex strip25 at right
                            "Alexia nods and strips down, putting on the orange two piece swimsuit and posing in front of you."
                            alex "What do you think? I was worried it might be a little to transparent, but I like the way it feels."
                            "She bounces up and down a little, jiggling her tits for you some more."
                            me "I think it looks fine, and you look amazing in it. Turn around so i can take a look at it from behind."
                            show alex strip26 at right
                            "She spins around and leans against the wall, spreading her legs for you while she's at it."
                            me "Very nice, thanks for showing it to me."
                            alex "Any time, I'm glad you like it. I should probably get ready for class now though, don't want to be late."
                            show alex casual at right
                            "Alexia turns back and changes back into her normal clothes, stuffing the swimsuit back into her backpack. You say goodbye and walk with her out of the building before splitting up."

                        "Pasties and Miniskirt.":
                            me "What about these? They don't exactly seem like school atire."
                            "You point out a very short skirt and a small bag with red pasties in it."
                            alex "Oh, those. I had an idea for them, but I haven't gone through with it yet. Here, let me put them on for you."
                            show alex strip27 at right
                            "Alexia strips down completely, then pulls the miniskirt up and get's it settled into place. It's barely long enough to cover anything at all."
                            show alex strip28 at right
                            "Next she takes out the pasties, making sure they're the right way up before applying them. They turn out to be heart shaped. When she's ready she turns and poses for you, pushing her chest out to make her tits even more prominent."
                            alex "There, that's everything. What do you think?"
                            me "No underwear to go with it?"
                            "She blushes a little and shakes her head."
                            alex "Nope, if I bend over a little too much..."
                            show alex strip29 at right
                            "She turns around, bending over to illustrate her point. Just a little movement and her skirt rides up her ass, showing off her pussy to anyone behind."
                            "Alexia turns around and bends over again, letting her tits dangle in front of you. She shakes her shoulders, bouncing them around while you watch."
                            alex "I was reading the student code of conduct a little while ago, and it turns out there was a big push against dress codes about a decade ago. So this..."
                            show alex strip28 at right
                            "She runs her hands over her body. You can see her nipples getting hard, straining against the adhesive pasties over them."
                            alex "Is the skimpiest outfit I could put together that still met the code. Seems a little ridiculous, right?"
                            if alexO.slut_score > 70 or alexO.exhib:
                                menu:
                                    "Offer to walk around with her.":
                                        me "Well, the rules are the rules. How about we go for a walk and stretch our legs?"
                                        alex "Uh, sure. One moment."
                                        "Alexia starts to slip the skirt down."
                                        me "No, I mean with you wearing that. If it's within school rules, there shouldn't be any problem, right?"
                                        alex "Well, technically not, but..."
                                        me "Come on, I'll be there to take care of you. Wouldn't it be hot to show off to everyone? I'd bet they'd be dying to have a piece of you."
                                        "Alexia runs a hand over her breast, playing with her hard nipple for a second. Finally she takes a deep breath and nods."
                                        alex "Okay, lets do it. Stay close to me though, please."
                                        "She leaves her stuff in the lecture hall and takes your arm. Together you head upstairs and towards the exit. You can feel Alexia shaking a little as you walk."
                                        me "Alright, here we go."
                                        "You open the door and lead the way out. This part of campus isn't very busy, but there are a handful of people walking around nearby."
                                        "You start walking, and soon a few guys farther along your path have noticed you. They watch as you walk past, staring at Alexia's barely covered tits."
                                        me "I think you dropped something."
                                        alex "Hmm? Oh."
                                        show alex strip30 at right
                                        "She bends over slowly, letting her tiny skirt ride up onto her ass. The group of men stop and stare at Alexia's pussy while she flashes them."
                                        "She pauses for a moment, then stands up and starts walking again. She's picking up speed, taking charge of the walk and guiding the two of you around."
                                        show alex strip28 at right
                                        alex "Fuck, I'm really turned on. Do you think they could see how wet I was."
                                        me "I don't know, but I'm sure they liked the view. We can head back whenever you want."
                                        if alexO.slut_score > 90 or (alexO.slut_score > 70 and alexO.exhib):
                                            alex "Actually, I was feeling a little hungry. Lets swing by food court."
                                            "You follow Alexia while she leads you towards the center of campus. Before long you're at your destination with people milling around in every direction."
                                            "A number of guys have noticed Alexia and are staring at her as she walks past. She winks at a few of them, taking long exaggerated steps that show off her legs."
                                            alex "Hmm, how about over there. I don't exactly feel like waiting in a line."
                                            "She heads over to one of the cashiers, leaning on the counter while she talks to him. Her breasts dangle forward a little, and you can see her wet pussy from behind."
                                            alex "Hi, I'd like the number one combo, please."
                                            "Cashier" "Uh... Sorry?"
                                            "Alexia wiggles her ass at you, and everyone else who's staring at her now. You're close enough that you can see her juices trickling down her inner thigh and notice the quiver in her legs."
                                            alex "The number one combo. Up there."
                                            "She points to the sign, and the cashier seems to clue in."
                                            "Cashier" "Oh, right. Sorry, right away."
                                            "He punches in the order on his register, having trouble concentrating while Alexia's barely concealed tits bounce in front of him."
                                            "You wait a minute or two while the food is prepared, Alexia standing next to you and holding your arm. You can feel her shaking like a leaf against you now, and she's taking short sharp breaths."
                                            me "Do you like this Alexia? Everyone's watching you."
                                            "She nods, moaning softly under her breath. Plenty of men have gathered around, either catching glances or blatantly staring. A few girls are watching too, seemingly disappointed they aren't the center of attention now."
                                            me "I can see how badly the guys want you. I bet they want to throw you onto your knees and ram their cocks down your throat. I know you'd love that, getting throated right here in front of the whole school."
                                            show alex strip31 at right
                                            "Alexia leans against you and moans again, louder this time."
                                            me "You'd let them cum wherever they wanted, not that you could stop them. Down your throat, over your pretty face. Then they'd put you over that table and fuck your tight pussy too. That skirt isn't exactly going to stop them."
                                            alex "[inputName]..."
                                            me "Bent over a table, One guy down your throat, one guy in your cunt. I wonder if they'd try and double up? Think you could manage two cocks in your pussy? I'm pretty sure they'd do it anyways."
                                            "She gasps and leans against you completely, clinging to your arm. Her legs shuffle back and forth involuntarily."
                                            me "You'd just be out there, a cum covered fuck toy for everyone to use. And you'd love every minute of it, wouldn't you, you dirty fucking slut."
                                            "Cashier" "Excuse me, you're order's ready."
                                            "Alexia glances up at the cashier and whimpers, legs spasming while she leans against you. You grab the bag he's holding out."
                                            "Cashier" "Is she alright?"
                                            me "Yeah, she's fine. She's just cumming for you like a slut."
                                            "Cashier" "Oh, okay. Wait, what?"
                                            "You turn around and hurry off, pulling Alexia after you. She stumbles along, still too caught up in her orgasm to walk right."
                                            "Cashier" "Shit, wait! You need to pay! Ah, fuck it..."
                                            show alex strip28 at right
                                            if alexO.slut_score > 100 and alexO.freeuse:
                                                "Soon you and Alexia are outside of the food court, cutting off the paths to get away from the crowds. Part way back Alexia has mostly recovered and takes the lead again."
                                                alex "Fuck, I think I need more than that [inputName]. I need a cock in me right now. I need a bunch of cocks in me."
                                                "She takes a slow breath, legs quivering in anticipation. You think for a moment, then point towards the alley between two buildings near by."
                                                me "Go wait down there, I'll circle back and see if you caught anyone's interest with your show."
                                                alex "Okay. Don't be too long."
                                                hide alex
                                                "You and Alexia split up. When you get back to the food court you start to walk around, looking for anyone who might be interested."
                                                if alex_gangbang.check_event():
                                                    "After a few minutes of wandering around you spot the cashier you were talking to earlier. He seems to be on break and has his phone out to show something to a small group of guys."
                                                    "You walk over, standing close enough to overhear their conversation."
                                                    "Cashier" "... right? I mean, she looked super into it."
                                                    "Friend 1" "I'm so fucking pissed you didn't call us faster. I was right next door!"
                                                    "Cashier" "I tried man. They left right away."
                                                    "Friend 2" "Shit, send that picture to me at least. She's fucking hot!"
                                                    "You step up beside the cashier and clear your throat. All four guys look up at you."
                                                    me "Hey, did you like what you saw?"
                                                    "The cashier turns around, startled. A split second later he's recognized you."
                                                    "Cashier" "Oh sit, it's you! Uh, guys, this is the guy that was with her."
                                                    "Friend 2" "Seriously? What're you doing back here?"
                                                    me "She's a friend of mine, and looking for a group to have a little fun with. If you want to get a close up look we can go meet her now."
                                                    show alex mast11 at right
                                                    "They exchange glances, then look back and all nod. You lead the four of them out of the food court and back to the alley where Alexia is waiting."
                                                    "You find her with her back up against the wall, rubbing her clit slowly."
                                                    alex "Oh, hello everyone. I see you found our friend again. And some of his friends."
                                                    show alex strip28 at right
                                                    "Alexia straightens up, pulling her skirt back down in a rediculous attempt to cover herself up. The cashier waves awkwardly, eagerly looking Alexia up and down."
                                                    me "Well Alexia? I hope you weren't going to make us all wait."
                                                    "You pull your pants down low enough to let your hard cock flop out. The other guys look at each other for a moment, then do the same."
                                                    alex "Oh boy... I guess I've got my work cut out for me."
                                                    show alex blow21 at right
                                                    "Alexia walks over to the group, biting her lower lip while she stares at your cocks. She squats down in front of you, letting your dick rest on her cheek."
                                                    alex "Gather 'round. I'll see what I can do for all of you."
                                                    "Friend 3" "Hey guys, I've got some condoms if you need 'em."
                                                    $condom = True
                                                    if alexO.slut_score >125 or alexO.cumslut:
                                                        $condom = False
                                                        alex "Oh no, I want to feel you all raw inside my mouth."
                                                        "She gives your cock a lick from base to tip."
                                                        "Friend 2" "You heard the lady, it's her show."
                                                    else:
                                                        alex "That's a good idea. Except for you."
                                                        "She gives your cock a lick from base to tip."
                                                        alex "You can have me raw."
                                                        "The other guys quickly distribute the condoms and slip them on while Alexia licks your shaft a few more times."
                                                    show alex blow22 at right
                                                    "The four other men circle around Alexia while she opens her mouth and slips you inside. She reaches up with her hands, taking one cock in each and stroking them off at the same time."
                                                    "Cashier" "Holy crap that feels amazing."
                                                    "Alexia gives your shaft a few quick passes, then slides off with a wet pop. She gives a wide smile, then turns a little and starts to blow the guy beside you."
                                                    "She makes a complete circle of the group, giving everyone a chance to slide their cock down her throat. The rest of you enjoy her handjob, or reach down and play with her tits."
                                                    "She pops off one dick and giggles, stroking off two guys while she talks."
                                                    alex "This takes some serious multi-tasking. Sorry to keep you waiting."
                                                    me "Maybe we need a few more holes to play with then Alexia. Stand up."
                                                    show alex strip31 at right
                                                    "Alexia nods and gets onto her feet. Pairs of hands roam over her body, squeezing her breasts, spanking her ass, and playing with her pussy."
                                                    "Friend 2" "Damn, you're dripping wet. I need a piece of this."
                                                    alex "[inputName] first. I want to feel you inside me."
                                                    "You place your hands on Alexia's hips and spin her around. She bends forward for you, presenting her tight pussy."
                                                    me "Just like this. Have fun everyone, there's plenty to play with."
                                                    "You hold onto your shaft and line up with Alexia's cunt, slipping in slowly. Alexia's moans are cut short as a dick is pushed into her open mouth."
                                                    "Friend 3" "There we go girl, eat up!"
                                                    show alex fuck51 at right
                                                    $ alexO.inc_sex()
                                                    "You settle into a rhythm pumping in and out of Alexia from behind while she sucks off the guy in front of her. It doesn't take long before both of her hands have shafts in them as well."
                                                    me "Good job Alexia, you're doing great."
                                                    "Alexia mumbles something, but it's completely muffled. She must be having a good time, because she's dripping wet and working her hips against yours as you fuck her."
                                                    "You enjoy the feeling of Alexia's tight pussy while the other guys take turns with her hands and mouth. Soon you've been drawn to the edge of your orgasm."
                                                    menu:
                                                        "Cum inside of her.":
                                                            me "Here we go! Lets fill you up!"
                                                            "Friend 1" "Yeah, give it to her!"
                                                            $ alexO.inc_cum_inside()
                                                            "You hold onto Alexia's hips and fuck her hard and fast. You hold yourself tight against her hips as you orgasm, pumping your cum deep into her."
                                                            "Cashier" "Fuck, I'm going to cum too!"
                                                            if condom:
                                                                "The cashier grunts as Alexia blows him, filling his condom up with cum. He steps back, and Alexia starts to suck off the next guy too."
                                                                show alex fuck53 at right
                                                                "Soon all four of them have finished and step back while Alexia stands up, legs shaking and panting loudly. Your cum runs down her leg onto the floor."
                                                            else:
                                                                "The cashier grunts as Alexia blows him. When he steps back she lets his cum dribble out of her mouth. The next guy steps up and slides into her now free mouth."
                                                                show alex fuck54 at right
                                                                "Soon all four of them have finished, filling her mouth up and covering her face with warm sperm. You slide out of Alexia's pussy and let her stand up, legs shaking and panting loudly."
                                                            "You take a moment to catch your breath, then pull your pants up."
                                                            me "Well guys, that was fun. We've got to head out, but we'll see you around."
                                                            alex "Ah... Goodbye guys..."

                                                        "Cum on her face.":
                                                            me "Here we go, get on your knees!"
                                                            "You pull out of Alexia, and she drops to the ground quickly. You stroke yourself off, spraying your load over her face."
                                                            if condom:
                                                                "The other guys follow your lead and pull their condoms off, jerking themselves off until they cum as well."
                                                            else:
                                                                "The other guys follow your lead, jerking themselves off until they cum as well."
                                                            show alex fuck52 at right
                                                            if alexO.cumslut:
                                                                alex "Oh god yes! Pump it right here, all over my face!"
                                                                "Alexia shivers with pleasure as another pulse of semen shoots out over her chin and cheek."
                                                            "When they're finished Alexia is completely drenched in their sperm. She closes her eyes as it runs under her glasses, covering them and glueing them shut."
                                                            $ alexO.inc_cum_over()
                                                            me "Whew. Good job everyone, I think she looks pretty good like that."
                                                            alex "Ah... That was... Wow..."
                                                            me "We've got to head out, but we'll see you around."
                                                            "Alexia stands up and takes your arm, letting you lead her around the corner. She pauses to wipe some of the semen from her eyes so she can see."

                                                    show alex casual at right
                                                    "You lead Alexia away from the group and back to the lecture hall. She strips off her pasties and miniskirt, then pulls on her normal outfit."
                                                    if alexO.cumslut:
                                                        alex "That was a lot of fun [inputName], I've never gotten to take so many loads at once before. Want to do it again some time?"
                                                    else:
                                                        alex "That was a lot of fun [inputName]. We need to do that again some time."
                                                    me "We'll see. You have a class to get to, right?"
                                                    alex "Shit, right. I've got to run, see you later!"
                                                    "Alexia hurries off, leaving you to collect your own stuff and leave as well."


                                                else:
                                                    "After a few minutes of looking around you haven't seen anyone who looks like they might be interested. When campus security shows up and starts asking questions you decide to give up and head back to Alexia."
                                                    show alex mast11 at right
                                                    "You find her in the alleyway you had pointed to earlier, back against the wall while she touches herself."
                                                    alex "Well? How did it go?"
                                                    me "Security showed up before I could find anyone. They may be comming this way, we should get going."
                                                    "Alexia rubs her clit a few times, moaning loudly."
                                                    alex "Ah... Okay. We should try this again though, maybe we can find someone then."
                                                    show alex casual at right
                                                    "After a short walk you've made it back to the lecture hall you started from. Alexia strips off the pasties and miniskirt and pulls on her normal outfit. When she's done she wraps her arms around you and kisses you, tongue wrapping around yours."
                                                    alex "That was a lot of fun [inputName]. We need to do that again some time."
                                                    me "We'll see. Now didn't you have a class to get to?"
                                                    alex "Shit, right. I've got to run, see you later!"
                                                    "Alexia hurries off, leaving you to collect your own stuff and leave as well."

                                            else:
                                                "Soon you and Alexia are outside of the food court, cutting off the paths to get away from the crowds. By the time you get back to the building you started at she's mostly recovered. You head downstairs, and Alexia starts getting dressed."
                                                alex "Holy shit [inputName]. That felt... fuck."
                                                show alex casual at right
                                                "She takes a deep breath, then strips off her pasties and miniskirt and pulls on her normal outfit. When she's done she wraps her arms around you and kisses you, her tongue wrapping around yours."
                                                alex "We need to do that again some time. Please."
                                                me "We'll see. Now didn't you have class to get to?"
                                                alex "Shit, right. I've got to run, see you later!"
                                                "Alexia hurries off, leaving you to collect your own stuff and leave as well."

                                        else:
                                            alex "Maybe that's a good idea, before we attract too much attention."
                                            "You loop back, heading towards the building you were in before. Just before you reach the entrance you spot a guy with his phone out, taking pictures of Alexia."
                                            show alex strip32 at right
                                            "Alexia smiles at him as you pass, then slows down and grabs a tit in one hand, lifting it up to her mouth and licking her nipple through the pastie. He smiles and nods, taking more pictures."
                                            "After that she picks up speed, racing back into the building. Once she's inside she stops and takes a deep breath, shaking against you."
                                            show alex strip28 at right
                                            alex "Oh fuck, I think I just came... I didn't expect that to feel so intense."
                                            me "I guess you just love to show people what a cute slut you are, right?"
                                            "You give Alexia's ass a smack. She looks up at you and smiles, biting her lip a little."
                                            alex "I should get dressed again though, I've got class soon and I don't think this is the outfit I should be wearing."
                                            me "Not unless you want to get fucked during class."
                                            alex "Well..."
                                            show alex casual at right
                                            "She laughs and leads you back down to the lecture hall. She peels the pasties off, then slides the skirt down and puts her normal clothes back on."
                                            "After that, you and Alexia walk back out of the building, saying goodbye before splitting up."

                                    "Watch her show off a little more.":
                                        me "A little, but it's certainly nice to look at."
                                        "Alexia does another spin for you, letting you take one last look at her tits and ass in the minimalist outfit."
                                        alex "That's what I thought. I should get ready for class though, before I'm late."
                                        show alex casual at right
                                        "She peels off the pasties, then slides the skirt down and puts her normal clothes back on."
                                        "You and Alexia walk out of the building together, then say goodbye and split up."
                            else:
                                me "A little, but it's certainly nice to look at."
                                "Alexia does another spin for you, letting you take one last look at her tits and ass in the minimalist outfit."
                                alex "That's what I thought. I should get ready for class though, before I'm late."
                                show alex casual at right
                                "She peels off the pasties, then slides the skirt down and puts her normal clothes back on."
                                "You and Alexia walk out of the building together, then say goodbye and split up."

                        "Naked.":
                            me "Actually, I don't think I want to see any of that. I just want to see all of you, nothing in the way."
                            alex "Guess I didn't need to go and get all of this then."
                            show alex strip17 at right
                            "She shrugs and takes a few steps back, pulling her shirt off and throwing it onto the table as she goes."
                            show alex strip12 at right
                            "You sit back and watch while she slips her skirt off, then undoes her bra and throws it onto the growing pile."
                            show alex strip4 at right
                            "Last she pulls down her panties, kicking them away with her toe before posing in front of you."
                            alex "Like this, able to see everything you want?"
                            me "Almost. Turn around for me."
                            show alex strip24 at right
                            "She turns and plants her hands on the wall, spreading her legs so you can see her pussy. She shakes her ass, making it bounce around for you."
                            alex "There, that should be everything, right?"
                            me "I think so, just a few moments while I enjoy the show."
                            show alex strip4 at right
                            "She shakes her butt a little more, then turns around and jiggles her tits at you."
                            show alex strip12 at right
                            "Finally she grabs her panties and slides them back on."
                            alex "That was fun, but I've got to get ready for class. Don't want to be late."
                            show alex casual at right
                            "Alexia changes back into her normal clothes and picks up her backpack. You walk with her out of the building and say goodbye before splitting up."

                    #End the show
                else:
                    "Alexia takes a final spin, showing off her tits and ass while you sit and watch."
                    alex "That was fun [inputName]. Hope you had a good time too."
                    me "I did, thanks Alexia."
                    hide alex
                    "She puts her shirt back on and sits down again, blushing a little. You talk about nothing in particular until Alexia has to go."
                    #End the show
            else:
                "Alexia thinks for a long moment, then gives you a small smile and nods."
                alex "Alright, but just for a little while, okay? You're lucky nobody else ever comes over here."
                show alex strip17 at right
                "She plays with the bottom her sweater for a few seconds, then pulls it up and off."
                show alex strip3 at right
                "She turns around and undoes the side of her skirt next, letting it fall to the ground around her feet. She steps out of it and turns back to you."
                alex "How's this?"
                me "Amazing. You look beautiful Alexia."
                alex "Well thank you."
                "She stands around for a few more moments in her bright red underwear, then grabs her skirt and starts to put it back on."
                alex "Wow, that feels so strange to do, I feel so..."
                me "Naked?"
                alex "Funny. I was going to say vulnerable, but I kind of like it."
                show alex casual at right
                "She pulls her clothes back on and sits on the long table at the front of the lecture hall."
                me "Thank you Alexia, that was hot."
                alex "It was, wasn't it."
                hide alex
                "You grab a chair, and the two of you spend another hour or two chatting about nothing in particular. Eventually you say goodbye and Alexia heads off to her next class."

            $ alexO.inc_naked()
            $ alex_hub.inc_level(1)
            $ alexO.change_resist(-alex_hub.use_red(1,alexO.resist_score))

        "Ask for a handjob." if alexO.slut_score > 35:
            me "This is a pretty nice find, nice and private."
            alex "Yeah, it's a great place to come and relax between classes."
            "You sit down on the table facing the front of the class and rub your crotch."
            me "Hey, since we have some time, could you do me a favour and help me relax?"
            alex "How could I do that?"
            "Alexia sits beside you, running her hand along your thigh while you unzip your pants."
            me "A quick handjob would be perfect."
            show alex hand4 at right
            $ alexO.inc_hand()
            "You pull your pants down and let your hard cock spring up. Alexia gasps softly, then leans to her side and wraps her hand around your shaft. She pulls up her skirt quickly, starting to touch herself as well."
            alex "Can't let you have all the fun."
            "She starts to stroke you off, slowly at first and picking up speed as she goes. After a few minutes she pauses to spread your precum around and get your shaft a little wet."
            me "That feels great Alexia. Thanks."
            alex "Any time. Just let me know when you're going to cum, okay?"
            "You lean back and relax, enjoying the feeling of her warm soft hand as it slides up and down your cock. Soon you can feel your core muscles tighten as your orgasm approaches."
            if alexO.slut_score > 50:
                # Lets you cum somewhere else
                menu:
                    "Cum on her tits":
                        me "I'm almost there. Get on your knees and get your tits out for me."
                        "Alexia nods and lets go of your shaft so she can pull up her shirt and bra. She drops to the floor and holds her breasts up, ready for you."
                        show alex hand5 at right
                        $ alexO.inc_cum_over()
                        "You stroke yourself to completion, moaning softly as you climax. You spray your load onto Alexia's waiting tits, covering them from top to bottom."
                        if alexO.cumslut:
                            alex "Oh yeah, give it to me. You know I want every last drop of your hot load."
                        else:
                            alex "Wow..."
                        "When you're done you sit back and give a contented sigh, admiring your work. Alexia stays on the floor for a few moments longer while you watch."
                        alex "That was really, really hot [inputName]."
                        me "Yeah, it was. Thanks for the help."
                        show alex casual at right
                        "Alexia stands up and looks around for something to get cleaned up with. When she's not able to find anything she shrugs and pulls her bra and shirt back over her cum covered tits."
                        "You pull up your pants while she sits down next to you, and you talk about nothing in particular for the next hour. Eventually she has to head to her class, and you say goodbye to each other."

                    "Cum on her face":
                        me "I'm almost there. Get on your knees and look up at me."
                        "Alexia nods and lets go of your shaft. She drops the the floor and looks up at you while you stroke yourself off to completion."
                        show alex hand6 at right
                        $ alexO.inc_cum_over()
                        "You moan softly as you climax, spraying your load over Alexia's face. She gasps as your hot cum lands, but holds still until you're finished."
                        if alexO.cumslut:
                            alex "Mmm, thank you. I love being covered in your cum like this."
                        else:
                            alex "Wow..."
                        "When you're finished you sit back and give a contented sigh, admiring your work. Alexia stays on the floor for a few moments longer while you watch."
                        alex "That was really, really hot [inputName]."
                        me "Yeah, it was. You look great like that."
                        show alex casual at right
                        "She winks at you and stands up, looking around for something to get cleaned up with. When she's not able to find anything she shrugs and just uses her sleeve to clean her face off."
                        "You pull up your pants while she sits down next to you, and you talk about nothing in particular for the next hour. Eventually she has to head to her class, and you say goodbye to each other."

                    "Cum in her mouth" if alexO.slut_score > 80:
                        #Lets you cum in her mouth instead of her tits.
                        me "I'm almost there. Get on your knees and suck me off."
                        "Alexia nods and lets go of your shaft, dropping to her knees in front of you. She wastes no time and slips her mouth around your shaft, working her tongue along the bottom of your cock."
                        "You tense up as you start to climax, and she pulls back so your tip is just inside of her mouth. She looks up at you and keeps eye contact while you empty your balls into her mouth."
                        me "Fuck, that's great. Drink it up."
                        show alex hand7 at right
                        $ alexO.inc_cum_mouth()
                        $ alexO.inc_cum_swallow()
                        "She waits until you're completely finished, then slides off your cock and opens up for you. She uses her tongue to play with your cum, splashing it around inside her mouth."
                        "After a few moments she closes her mouth and swallows, taking a deep breath after."
                        alex "Fuck, that was really, really hot [inputName]."
                        me "Yeah, it was. Thanks for the help."
                        show alex casual at right
                        "You pull up your pants while Alexia stands up and sits next to you. You talk about nothing in particular for the next hour until she has to leave, then say goodbye to each other."
            else:
                #Cum on the floor
                me "I'm almost there. Fuck that feels nice."
                "Alexia speeds up even more, stroking you off as fast as she can manage."
                "You let out a soft moan as you climax, spraying your load across the floor in front of you."
                show alex casual at right
                "Alexia slows down as you finish, your warm cum dribbling onto her hand. Finally she lets go completely and wipes her hand off on the under side of her skirt."
                alex "That was hot, I'm glad you had a good time."
                "You pull your pants back up and sit down with a contented sigh. You and Alexia talk about nothing in particular for another hour or so before she has to head off to her class."

            $ alex_hub.inc_level(2)
            $ alexO.change_resist(-alex_hub.use_red(2,alexO.resist_score))

        "Ask for a titfuck." if alexO.slut_score > 50:
            #Titfucks you for a while.
            me "This is a pretty nice place."
            alex "Yeah, it's a great place to come and relax."
            me "Speaking of..."
            "You pull your pants down, letting your hard cock spring free. Alexia gasps softly and watches it bounce."
            me "How about you get your tits out and take care of this for me. I'd really appreciate it."
            "Alexia bites her bottom lip and nods, pulling her shirt up and throwing it to the side. You sit down on the table at the front of the lecture hall while Alexia gets onto her knees in front of you, undoing her bra and sliding it off as well."
            show alex tit1 at right
            $ alexO.inc_tit()
            "She takes her breasts in her hands and leans forward, wrapping them around your shaft."
            alex "Oh, you feel so big. Just relax and have a good time."
            "You lean back a little, letting Alexia service you with her tits."
            if alexO.slut_score > 70:
                #Blows you a little to lube you up
                alex "Here, this should feel even better."
                show alex tit3 at right
                "She lets your cock slip out of her tits and leans forward even farther, licking your cock. She works her head around, making sure to get every inch of it."
                me "Fuck, that's feels great."
                "Alexia licks along the bottom of your cock again, then opens her mouth and slips you inside."
                show alex tit1 at right
                "She blows you for a few short moments, then pulls off and grabs her tits again to titfuck you."
                "Her warm, wet tits slide up and down your shaft easily, sending a shiver up your spine."
                menu:
                    "Take over and fuck her tits." if alexO.slut_score > 80:
                        #Take over and fuck her
                        me "Shit, that feels way too good. Wait a moment."
                        show alex tit7 at right
                        "You stand up and grab Alexia's tits, letting her hands fall to the side. You start to work your hips back and forth, fucking her tits yourself."
                        "Alexia looks up at you, maintaining eye contact while you fuck her wet cleavage."
                        alex "You can use me however you want, just have fun!"
                        menu:
                            "Cum between her tits.":
                                "You keep pumping your hips until you climax, emptying your balls between Alexia's breasts. She moans softly as she's covered in your hot cum."
                                show alex tit8 at right
                                $ alexO.inc_cum_over()
                                "You wait until you're completely finished, then sit back down on the table and admire your work. Alexia sits back and takes a few deep breaths, running a finger through the semen on her chest."
                                me "You look really good like that Alexia, we'll have to do this again some time."
                                if alexO.cumslut:
                                    "Alexia brings her sperm covered finger to her lips and licks it clean, shivering with pleasure as she savours the taste."
                                    alex "Mmm, we definitely should."
                                else:
                                    alex "We definitely should. Wow."
                                show alex casual at right
                                "You pull up your pants while Alexia looks around for something to clean herself off with. When she can't find anything she shrugs and just puts her bra and shirt back on over her sperm covered tits."
                                alex "I should probably head out to class, I'll see you around."
                                "You say goodbye and head your seperate ways."

                            "Cum on her face.":
                                me "Look down at it for me, I want to cover your fucking face."
                                "Alexia nods and looks down, watching your cock as it slides in and out between her breasts."
                                show alex tit10 at right
                                $ alexO.inc_cum_over()
                                "You fuck her tits until you start to cum, then leave your tip poking out of the top between her cleavage as you empty your balls onto her face. She gasps as your hot load hits her, and catches some of it in her mouth."
                                "When you're done you let go of her boobs and sit back, admiring your work. Alexia looks up at you and smiles, taking a moment to swallow the semen that landed in her mouth."
                                if alexO.cumslut:
                                    alex "Oh wow, you really did cover me didn't you [inputName]. Look at me now, covered in your hot cum..."
                                    "She runs a finger along her cheek, scooping up some of your semen before licking it clean. She shivers with pleasure as she swallows your spunk."
                                    me "My pleasure Alexia. You look great covered in it, it suits you."
                                else:
                                    alex "Wow... You really did cover me didn't you."
                                    me "Damn right I did. You look great like that, it suits you."

                                if alexO.slut_score > 110 or alexO.cumslut or alexO.exhib:
                                    show alex tit11 at right
                                    "Alexia grabs her shirt and bra and puts them on again, but doesn't bother cleaning off her face."
                                    alex "I've really got to run to class or I'm going to be late. See you around!"
                                    "She heads out of the lecture hall, face still covered in your cum."
                                else:
                                    show alex casual at right
                                    "Alexia grabs her shirt and bra, pausing for a moment to use them to wipe her face clean. After that she puts them on and heads towards the door."
                                    alex "I've really got to run or I'm going to be late. See you around!"
                                    "You say goodbye, and she heads out of the lecture hall."

                            "Cum down her throat." if alexO.slut_score > 90 or alexO.cumslut:
                                me "Open up for me Alexia, I'm going to cum right down your throat."
                                show alex tit9 at right
                                $ alexO.inc_cum_mouth()
                                $ alexO.inc_cum_swallow()
                                "Alexia nods and opens her mouth wide. You slide out of her tits and into her mouth, placing your hands on either side of her head as you start to skull fuck her."
                                "It doesn't take many strokes in and out of her tight throat before you start to cum. You press yourself as deep down as you can, emptying your balls into her stomach while her throat spasms around your shaft."
                                me "Fuck, that's right. Drink it up like a good slut should!"
                                "You hold yourself there for a few more seconds, then pull out and sit down. Alexia takes a few deep breaths, then looks up and smiles at you."
                                alex "Fuck, that was hot..."
                                me "Yeah, it was. I'll make sure to do it again some time."
                                show alex casual at right
                                "Alexia grabs her bra and shirt, putting them on quickly and heading for the door."
                                alex "I've got to head out or I'm going to be late. See you around!"
                                "You say goodbye, and she heads out of the lecture hall."

                    "Let her keep going.":
                        #Just keep going.
                        "You let Alexia keep going for a few minutes, and soon you feel your core tense up as your orgasm approaches."
                        me "Shit, that feels way too good, I'm going to cum soon."
                        alex "Where do you want to finish?"
                        menu:
                            "Cum between her tits.":
                                me "Right between your tits, just keep going like that."
                                "She nods and keeps titfucking you. After a few moments you start to climax, spraying your load between her cleavage."
                                alex "Oh fuck, there it is!"
                                show alex tit4 at right
                                $ alexO.inc_cum_over()
                                "She keeps working her tits up and down as you orgasm, letting you fire your load all along her chest. When you're finally done she sits back and lets your cock slide out from between her boobs."
                                me "Fuck, that felt great."
                                alex "Yeah, I could tell. Wow."
                                show alex casual at right
                                "Alexia stands up and looks for something to get cleaned up with. When she can't find anything she shrugs and just puts her bra and shirt back on over her sperm covered tits."
                                alex "I should probably head out to class so I'm not late. I'll see you around."
                                "You say goodbye, and she heads out of the lecture hall."

                            "Cum on her face.":
                                me "Right on your slutty fucking face!"
                                alex "You're the boss!"
                                "She gives you a few more fast strokes, then sits back a little and takes your cock in her hand. She strokes you off as you cum, looking up at you while you spray your load over her face."
                                show alex tit5 at right
                                $ alexO.inc_cum_over()
                                "Alexia makes sure to move your cock left and right, letting you cover every inch of her face with your semen. When you're done she licks the last few drops off your tip and lets go."
                                alex "Wow, you really did cover me."
                                me "You look great like that, I'll have to do it more often."
                                alex "You definitely should."
                                show alex casual at right
                                "Alexia gets up and looks around for something to clean up with. When she can't find anything she shrugs and uses the inside of her shirt to wipe your cum off with, then puts it back on."
                                alex "I've got to head out or I'm going to be late. See you around!"
                                "You say goodbye, and she heads out of the lecture hall."

                            "Cum in her mouth.":
                                me "Right in your mouth, I want to watch you swallow it all!"
                                "Alexia nods and gives you a few more strokes with her tits, then lets go of them completely and leans down to slip the tip of your cock into her mouth."
                                "You climax while she licks the tip of your cock with her tongue, emptying your balls into her mouth. She moans softly and looks up at you, keeping eye contact until you're finished."
                                me "Fuck, that felt great. Open up and show me."
                                show alex tit6 at right
                                $ alexO.inc_cum_mouth()
                                $ alexO.inc_cum_swallow()
                                "She nods and opens her mouth, letting you see the pool of white liquid you've put in there."
                                me "And swallow."
                                "She closes her mouth, and you can see her throat working while she drinks down your cum. When she's done she takes a deep breath and smiles up at you."
                                if alexO.cumslut:
                                    alex "Mmm, thank you [inputName], you tasted great."
                                    me "Good to hear, I'll make sure to give you some more later."
                                else:
                                    alex "That was really hot [inputName]."
                                    me "It was, we'll have to do it again some time."
                                show alex casual at right
                                "Alexia stands and grabs her clothes, getting dressed again."
                                alex "I've got to head out or I'm going to be late. See you around!"
                                "You say goodbye, and she heads out of the lecture hall."

            else:
                #Get it over with and cum into her hand.
                "After a few minutes spent enjoying her warm, tight cleavage you feel your orgasm approaching."
                me "Fuck, I'm going to cum soon Alexia."
                "She nods and speeds up, squeezing her tits against your shaft on either side."
                show alex tit2 at right
                "At the last moment she leans back, letting your cock fall out from between her breasts and taking it into her hand to stroke it off. She uses her other hand to cover your tip as you start to cum."
                alex "There we go!"
                "She slows down as you finish, dribbling your semen onto her hand. Finally she lets go entirely and sits back and sighs, smiling up at you."
                me "That felt great Alexia, thanks."
                alex "No problem, it was fun."
                "She looks around for something to clean up with, but can't find anything. Finally she shrugs and wipes your cum off onto the inside of her skirt."
                show alex casual at right
                "You pull your pants up again, and Alexia puts her shirt and bra back on. The two of you sit together and chat for the rest of the hour, then say goodbye and split up."

            $ alex_hub.inc_level(3)
            $ alexO.change_resist(-alex_hub.use_red(3,alexO.resist_score))

        "Ask for a blowjob." if alexO.slut_score > 70:
            #Starts to blow you.
            me "This is a pretty nice hang out spot."
            "You pull your pants down, showing your hard cock to Alexia."
            alex "Oh, hello there."
            me "We've got some time to kill, how do you feel about a quick blowjob?"
            alex "I'm not so sure. If you make it a nice long blowjob I think you've got a deal though. Just stand right there and I'll take care of you."
            show alex blow14 at right
            $ alexO.inc_blow()
            "She gives you a wink as she walks over to you and drops to her knees. She gives your shaft a few strokes with her hand, then runs her tongue along its side and bottom a few times."
            me "Damn, that feels nice Alexia."
            "Next she slides you into her mouth, bobbing her head up and down while she runs her tongue along the bottom of your cock."
            "For the next few minutes you enjoy the feeling of Alexia's warm wet throat as she sucks you off."
            menu:
                "Take over." if alexO.slut_score > 85:
                    #Hold her head and skull fuck her.
                    "You place your hands on either side of Alexia's head, holding it still."
                    me "Just open wide, I'll take care of myself."
                    show alex blow17 at right
                    "Alexia tries to mumble something past your cock, but you aren't able to make out what it is. You start to work your hips back and forth, fucking her open mouth."
                    "You pick up speed over the next few minutes. Her drool runs down her chin, dripping down onto the floor and her shirt."
                    me "Fuck, you just feel so good Alexia!"
                    "You slam yourself as far down her throat as you can, holding yourself there for a few seconds. She turns her eyes up to you and purrs, throat rumbling around your cock."
                    menu:
                        "Cum down her throat.":
                            me "Get ready to drink it all down you dirty slut!"
                            "You go back to pumping in and out of her mouth until you start to cum. Then you push yourself deep down her throat again, holding her tight against your hips as you fire your load right into her stomach."
                            "Alexia twists and moans as you fill her up, but doesn't try to pull off your cock. When you're finished you take a step back, slipping out of her mouth and letting her take a deep breath."
                            $ alexO.inc_cum_mouth()
                            $ alexO.inc_cum_swallow()
                            if alexO.cumslut:
                                alex "Wow... I think I just came a little bit too. Thank you [inputName], that was super hot."
                            else:
                                alex "Wow... That was intense."
                                me "Yeah, it was. You felt amazing, thanks Alexia."
                                alex "Any time. Wow."
                            show alex casual at right
                            "She takes a few moments to catch her breath, then stands up and grabs a chair. You pull up your pants and join her, talking about nothing in particular for the next hour until she has to head to class."

                        "Cum on her face.":
                            me "Get ready, I'm going to cover your slutty face!"
                            "You go back to pumping in and out of her mouth until you start to cum. Then you pull back, leaving her mouth with a wet pop and start to stroke yourself to completion while she looks up at you."
                            show alex blow15 at right
                            $ alexO.inc_cum_over()
                            "Alexia sticks her tongue out and holds still while you cum. You spray your load over her face, starting with her forehead and working your way down to her chin."
                            "Once you're done Alexia leans forward and starts to lick at the tip of your cock."
                            me "Good girl, get me all cleaned up now."
                            "She takes a few minutes, gently sucking on your sensitive cock until she's gotten every last drop of cum."
                            alex "Wow... You really did unload."
                            me "Yeah, I did. You felt amazing, thanks Alexia."
                            alex "Any time. Wow."
                            "She takes a few moments to catch her breath, then stands up and looks around for something to get cleaned up with. When she can't find anything she shrugs and uses her sleeve to wipe your cum off her face."
                            "You pull your pants up, and the two of you grab chairs and sit down. You talk about nothing in particular for the next hour until she has to head to class."

                "Let her keep going.":
                    #More blowjob
                    me "Fuck Alexia, keep that up and I'm going to cum soon."
                    "She pulls off with a wet pop, stroking your slippery dick while she talks to you."
                    if alexO.cumslut:
                        alex "Oh yeah, I want you to give me a nice big load. Just let me know where you want to finish. You can put that hot cum wherever you want [inputName]."
                    else:
                        alex "Sounds good to me. Just let me know where you want to finish, okay?"
                    "With that she slides you back into her mouth, blowing you faster and deeper than before. She pauses occasionally to push herself as far down your cock as she can manage, rubbing her nose against your pubes."
                    "It's not long before you feel your core tensing up as your orgasm approaches."
                    menu:
                        "Cum in her mouth.":
                            me "Alright Alexia, I'm going to finish right in your mouth."
                            "She moans something up at you, nodding as much as she can while she sucks you off. She speeds up even more, your cock making wet smacking noises as it bounces against the back of her throat."
                            "Alexia pulls back just before you cum, leaving her lips wrapped around the tip of your penis. She looks up at you, staring into your eyes while you empty your balls into her mouth."
                            me "Fuck, that's right! That's a good girl!"
                            show alex blow16 at right
                            $ alexO.inc_cum_mouth()
                            $ alexO.inc_cum_swallow()
                            "When you're finished you feel her tongue swirl against your tip, licking off the last few drips, then she leans back and opens up her mouth. Her tongue plays through your semen while you watch her."
                            "After a few moments she closes her mouth, swallows, and takes a deep breath."
                            alex "Wow, you really gave me a lot..."
                            me "You handled it like a champ. Thanks Alexia."
                            show alex casual at right
                            "She takes a moment to catch her breath, then stands up and grabs a chair while you pull your pants up. The two of you talk about nothing in particular for another hour or two until she has to leave for her class."

                        "Cum on her face.":
                            me "Alright Alexia, I'm going to finish all over your pretty little face."
                            "She moans something up at you, nodding as much as she can while she sucks you off. She speeds up even more, your cock making wet smacking noises as it bounces against the back of her throat."
                            "You take a step back just before you're going to cum, leaving Alexia's mouth with a sudden pop. You grab your cock and stroke yourself off while she looks up at you."
                            show alex blow15 at right
                            $ alexO.inc_cum_over()
                            "Alexia gasps as you fire your load onto her face, starting with her forehead and working your way down to her chin."
                            me "Fuck, there we go! That's a good girl!"
                            "You shake your cock, flicking the last few drops of cum onto her face, then take a step back and admire your work."
                            alex "Wow, that was a lot..."
                            me "That was great Alexia, thanks."
                            "She takes a moment to catch her breath, then stands up and looks around for something to get cleaned up with."
                            show alex casual at right
                            "When when she can't find anything she shrugs and just uses her sleeve to wipe your cum off her face."
                            "You pull up your pants, and the two of you talk about nothing in particular for another hour or two until she has to leave for her class."

            $ alex_hub.inc_level(4)
            $ alexO.change_resist(-alex_hub.use_red(4,alexO.resist_score))

        "Fuck her." if alexO.slut_score > 80:
            #Asks you how you want to do it.
            "You pull down your pants, revealing your hard cock."
            me "Yeah, this seems like a nice place. How about you lose the clothes and we take advantage of it."
            show alex strip4 at right
            "Alexia eyes your crotch for a few seconds, then nods and starts to strip down. Within a few moments she's completely naked."
            alex "How do you want to do it?"
            menu:
                "Have her ride you.":
                    #Sex
                    "You grab a chair from behind the desk at the front of the class and sit down, legs spread."
                    me "Come over here and sit on it."
                    show alex fuck38 at right
                    $ alexO.inc_sex()
                    "Alexia comes over to you and bends over a little, getting ready to sit down. The tip of your cock brushes against her ass while she gets in position."
                    "You hold onto your shaft and keep it steady while Alexia slips your tip into her pussy. You can feel how wet she already is."
                    alex "Okay, here we go."
                    "She slides down onto your cock, sighing happily as she goes. When she reaches the bottom she takes a moment and jiggles her ass left and right for you."
                    show alex fuck39 at right
                    "You use one hand to grab her ass cheek and start to guide her up and down. Alexia moans softly while she fucks you."
                    alex "Oh [inputName], that feels so good. Fuck..."
                    "You lean back in the chair and relax, guiding her up and down with one hand and enjoying the feeling of her tight wet cunt. It's not long before you can feel your orgasm approaching."
                    menu:
                        "Cum inside her.":
                            me "Keep it up Alexia, I'm going to cum soon."
                            "She moans loudly and leans forward even more. Her legs are quivering against yours, and you think her pussy is getting even wetter."
                            if alexO.cumslut:
                                alex "Yes! Fuck yes! Pump me full of your hot cum, it's going to make me cum too! Ah!"
                            else:
                                alex "Me... Ah, me too!"
                            "Her moans turn into a short squeak as she climaxes suddenly. You grab her hips with both hands and keep her moving up and down until you orgasm."
                            "You pull Alexia tight against you, pumping your cum as deep into her pussy as you can manage. She pants loudly, legs still shaking as you fill her up."
                            "When you're finally finished you let go and lean back with a sigh. Alexia takes a few steps forward, sliding your cock out of her cunt, and drops to her knees."
                            alex "Wow... Holy shit..."
                            show alex fuck40 at right
                            $ alexO.inc_cum_inside()
                            "You watch as she pants on the floor, cum dripping out of her and down her leg."
                            me "That felt great Alexia. Thanks."
                            show alex casual at right
                            if not alexO.preg_response_ok():
                                alex "Fuck [inputName], you need to be more careful. I know I can get carried away but I don't want you knocking me up, okay?"
                            "She takes a moment to catch her breath, then gets up and starts to get dressed. She uses her panties to wipe your cum off of her leg and pussy before putting them on."
                            alex "I should probably be getting to class. I hope we can do that again soon."
                            "You say goodbye, and Alexia leaves the lecture hall."

                        "Cum on her face.":
                            me "Get on your knees Alexia, I'm going to cum on your face."
                            if alexO.cumslut:
                                alex "Yeah, are you going to cover me with your hot load? Spray it all over me [inputName]!"
                            else:
                                alex "Okay, whatever you want."
                            "She slides off of your cock, sighing when you slip out completely, then turns around and drops to her knees. She looks up at you and maintains eye contact while you stroke yourself to completion."
                            show alex fuck43 at right
                            $ alexO.inc_cum_over()
                            "You start to cum, blowing your load over her waiting face. You move your cock left and right, covering every inch."
                            "When you're done Alexia slides forward and starts to lick the tip of your sensitive cock."
                            me "Damn, that feels great Alexia. Get me all cleaned up, please."
                            "She nods and slides you into her mouth, running her tongue along the side and bottom of your shaft. After a few bobs of her head she pulls off again with a wet pop."
                            alex "Mmm, you taste so good."
                            show alex casual at right
                            "She gives your cock one last kiss, then stands up and grabs her clothes. She uses her panties to wipe her face clean before putting them on."
                            alex "I should probably be getting to class. I hope we can do that again soon."
                            "You say goodbye, and Alexia leaves the lecture hall."

                        "Cum on her body.":
                            me "Get on the floor, I'm going to cover you like a fucking slut."
                            if alexO.cumslut:
                                alex "Yeah, are you going to cover me with your hot load? Spray it all over me [inputName]!"
                            else:
                                alex "Okay, do it!"
                            "She slides off of your cock, sighing when you slip out completely, and gets onto the floor in front of you. You stroke yourself to completion while she looks up at you."
                            show alex fuck41 at right
                            $ alexO.inc_cum_over()
                            "You start to cum, blowing your load all over Alexia's body. She sticks her tongue out, catching a little of your sperm on it."
                            "When you're done you sit back and sigh."
                            me "Damn, that felt great Alexia. Could you get me cleaned up, please?"
                            show alex fuck42 at right
                            "She nods and gets on her knees, quickly slipping you into her mouth. She runs her tongue along the bottom and side of your shaft, licking up your cum and her juices. After a few bobs of her head she pulls off with a wet pop."
                            alex "Mmm, you taste so good."
                            show alex casual at right
                            "She gives your cock one last kiss, then stands up and grabs her clothes. She uses her panties to wipe her body down, then puts them back on."
                            alex "I should probably be getting to class. I hope we can do that again soon."
                            "You say goodbye, and Alexia leaves the lecture hall."

                "Fuck her against the wall." if alexO.slut_score > 100:
                    #Sex
                    "You step up next to Alexia and wrap your arms around her, grabbing her ass while you pull her in for a kiss. Her tongue meets yours, and you make out in the middle of the lecture hall."
                    "As you kiss you walk forward, guiding her back until she reaches the wall. You break the kiss, a line of spit still running between your mouths."
                    show alex fuck44 at right
                    $ alexO.inc_sex()
                    "You wrap your arm around her thigh, lifting it up and pushing her against the wall. Your cock brushes against her stomach while you look into her eyes."
                    me "I'm going to fuck you right here."
                    "She nods and bites her lip while you line your cock up. You can feel how wet she is when you press your tip against her cunt."
                    "You slide into her slowly, enjoying the tight wetness of her pussy and the quiet moans she lets out."
                    alex "Oh god, you feel so good. Fuck me however you want, please."
                    "You start to pump in and out of her, holding her leg up with one hand and playing with her breasts with the other. For a few minutes you're both quiet, other than her moans and the wet smacking as you fuck her."
                    "Eventually you feel your orgasm approaching, getting closer with each stroke."
                    menu:
                        "Cum inside her.":
                            me "Fuck, I'm going to cum soon Alexia."
                            "She leans forward, whispering into your ear while she holds onto you."
                            if alexO.cumslut:
                                alex "God yes! Pump me full of it, fill me right up with your hot cum!"
                            else:
                                alex "Do it, I'm almost there too!"
                            "You speed up, fucking her as fast as you can until you start to climax. Then you push yourself as deep into her as you can, pressing her against the wall while you empty your balls into her pussy."
                            "She moans loudly and quivers in your arms, enjoying an orgasm of her own. You give her a few slow thrusts once you're finished, fucking her slippery cum filled cunt."
                            if alexO.cumslut:
                                alex "It's so warm... I wonder if you're going to get me pregnant one of these days..."
                            else:
                                alex "Oh god, it's so warm... Holy shit..."
                            show alex fuck45 at right
                            $ alexO.inc_cum_inside()
                            "You ease her leg to the ground and step back. Your cum starts to drip down her leg almost as soon as you slide out of her."
                            me "That was great Alexia, we'll have to do it again soon."
                            if alexO.preg_response_ok():
                                alex "Yeah, we should. Wow..."
                            else:
                                alex "Yeah, we should. We should be more careful though, I don't care how good it feels, I don't want you to get me knocked up."
                            show alex casual at right
                            "She takes a few moments to catch her breath, then collects her clothes. She uses her panties to wipe the cum off of her leg, then puts them on."
                            alex "I should probably be getting to class. See you around [inputName]."
                            "You say goodbye, and Alexia leaves the lecture hall."

                        "Cum in her mouth.":
                            me "Fuck, I'm going to cum soon Alexia. Get on your knees!"
                            "You take a step back, sliding easily out of Alexia's pussy. She drops to the ground and opens her mouth when you press your tip against her lips."
                            me "That's right, here we go!"
                            "You take a few thrusts in and out of her mouth until it pushes you over the edge, then hold your tip just inside of her lips as you fire your load inside."
                            "Alexia moans loudly as she stares up at you, waiting until you're finished. Then she swirls her tongue around your tip, getting the last few drops of cum off before you pull out."
                            me "Good girl, open up so I can see now."
                            show alex fuck46 at right
                            $ alexO.inc_cum_mouth()
                            $ alexO.inc_cum_swallow()
                            "She opens her mouth and gargles with the pool of white inside."
                            me "Alright, now drink up."
                            "You watch as she closes her mouth and swallows a few times, drinking down all of your hot cum. Finally she takes a deep breath and shows you that it's all gone."
                            if alexO.cumslut:
                                alex "Wow, you tasted so good [inputName]. Thank you so much."
                                "She licks her lips and sighs happily."
                                me "Yeah, that was great. We'll have to do it again soon."
                            else:
                                alex "Wow, it was so warm and tasted... Wow."
                                me "Yeah, that was great Alexia. We'll have to do it again soon."
                            alex "I hope so. Now I should be getting ready for class. See you around [inputName]."
                            show alex casual at right
                            "Alexia gets up and collects her clothes, putting them on before she heads out of the lecture hall."

                "Anal her." if alexO.slut_score > 130 or (alexO.anal and alexO.slut_score > 80):
                    #Sex:
                    me "Turn around and get on your hands and knees."
                    "Alexia nods and turns away, getting onto all fours for you. You crouch down behind her, lining your hard cock up with her asshole."
                    "You spit into your hand then stroke yourself a few times, then press your wet tip against her ass."
                    me "Ready Alexia?"
                    if alexO.anal:
                        alex "Yeah, hurry up and fuck me. I can take it."
                    else:
                        alex "Yeah, I think so."
                    show alex fuck47 at right
                    $ alexO.inc_sex()
                    "You hold her hips and press forward, slowly forcing your way into her impossibly tight asshole. Alexia grunts quietly as you finally slide inside."
                    me "There we go. Fuck you're tight."
                    if alexO.anal:
                        alex "You better fix that then! Stretch me out with that huge cock of yours!"
                    else:
                        alex "Ah! Keep doing that and I won't be for long!"
                    "You fuck her faster, enjoying the way her tight ass clamps down on your shaft as you go. Slowly Alexia's grunts turn to moans as she gets used to you inside her."
                    "It's not long before you feel your orgasm approaching, getting closer with each stroke."
                    menu:
                        "Cum inside her.":
                            me "Ah, here we go! I'm going to fill you up you dirty cum slut!"
                            if alexO.cumslut:
                                alex "Yes, pump my ass full of your hot cum! I want it all [inputName], give it to me!"
                            else:
                                alex "Yes, please!"
                            "You give her a few more fast strokes, pushing yourself over the edge, then slam your cock as deep into her ass as you can manage. She yelps and slumps forward as you start to fire your load inside of her."
                            alex "Oh god! Fuck!"
                            "She shivers against you, pushed to her own orgasm as well. You wait until you're completely finished, then give her asshole a few more pumps."
                            me "Ah, that's better. Nice and lubed up now."
                            alex "Easy! Holy shit. Easy back there."
                            show alex fuck48 at right
                            $ alexO.inc_cum_inside_ass()
                            "She shivers again as you stand up and pull out. Your cum starts to run down onto her pussy, then drip onto the floor."
                            me "That felt great Alexia, we'll have to do it again soon."
                            alex "Yeah, I might need a few days though."
                            show alex casual at right
                            "She stands up, legs still shaking, and collects her clothes. She uses her panties to wipe up your cum before putting them back on."
                            alex "I think I should be getting off to my class. See you around [inputName]."
                            "You say goodbye, and Alexia leaves the lecture hall."

                        "Cum on her ass.":
                            me "Here we go!"
                            "You give her ass a solid spank and a few more pumps with your cock, then pull out and stroke yourself off. Alexia gasps as you cover her ass cheeks with hot cum."
                            alex "Oh wow! Ah!"
                            show alex fuck49 at right
                            $ alexO.inc_cum_over()
                            "When you're completely done you wipe the last few drops off onto her and step back to admire your work."
                            me "You look really good like that Alexia. Being covered in cum suits you."
                            show alex casual at right
                            "She takes a few moments on the floor to catch her breath, then stands up and collects her clothes. She uses her panties to wipe your semen off her ass before putting them back on."
                            alex "There, all cleaned up. Hope nobody notices if they're a little sticky. I should be getting off to my class. See you around [inputName]."
                            "You say goodbye, and Alexia leaves the lecture hall."

                        "Cum down her throat." if alexO.slut_score > 140 or alexO.cumslut:
                            "You pull out of Alexia's ass suddenly, making her yelp in surprise. You quickly walk around to her other side and get on your knees, cock level with her face."
                            alex "Hey, what..."
                            "You place a hand on the back of her head and pull her forward, pressing the tip of your cock against her lips."
                            me "Come on, take it like a good slut should."
                            show alex fuck50 at right
                            $ alexO.inc_cum_mouth()
                            $ alexO.inc_cum_swallow()
                            "Alexia opens her mouth and you pull her head down, slamming your cock down her throat. She gurgles something up at you, but you can't understand what it is."
                            "You work your hips and fuck Alexia's throat for a little while until you start to cum. Then you push yourself nice and deep again while you unload right into her stomach."
                            "Alexia squirms a little, but doesn't try to pull off. You enjoy the feeling of her throat as it spasms around your sensitive shaft."
                            me "Good girl, did you like that?"
                            "You press Alexia's face into your crotch, rubbing her nose in your pubes. She moans something again and tries to nod."
                            me "I though you would. You just can't resist a cock down your throat, can you?"
                            "More moaning and gurgling. She coughs, blowing spit bubbles around the base of your dick."
                            "After a few more seconds you let go of her head, and she slides off with a wet pop. Alexia takes a gasp of air, then stays on her hands and knees panting for a few more seconds."
                            alex "Fuck... Holy fuck... Wow..."
                            me "That was great Alexia, thanks. We'll have to do it again some time."
                            show alex casual at right
                            "She nods weakly, and eventually stands up on shaking legs. She collects her clothes and puts them on."
                            alex "I should be getting off to class before I'm late. See you around [inputName]."
                            "You say goodbye, and Alexia leaves the lecture hall."

            $ alex_hub.inc_level(5)
            $ alexO.change_resist(-alex_hub.use_red(5,alexO.resist_score))

        "Give her some serum and train her.\n-15 Influence, -2 Serum" if alexO.slut_score > alexO.training_threshold and (player_blue_serum + player_purple_serum + player_red_serum > 1):
            menu:
                "Train her to be a cum slut from now on." if not alexO.cumslut:
                    call cumslut_descrip("Alexia")
                    menu:
                        "Continue with the training.":
                            call alex_train_cumslut
                        "Change your mind and leave.":
                            return False

                "Train her to be an anal lover from now on." if not alexO.anal:
                    call anal_descrip("Alexia")
                    menu:
                        "Continue with the training.":
                            call alex_train_anal
                        "Change your mind and leave.":
                            return False

                "Train her to be a free use slut from now on." if not alexO.freeuse:
                    call freeuse_descrip("Alexia")
                    menu:
                        "Continue with the training.":
                            call alex_train_freeuse
                        "Change your mind and leave.":
                            return False

                "Train her to be an exhibitionist from now on." if not alexO.exhib:
                    call exhib_descrip("Alexia")
                    menu:
                        "Continue with the training.":
                            call alex_train_exhib
                        "Change your mind and leave.":
                            return False

                "Change your mind and leave.":
                    return False

        "Chat about school for a bit.":
            "The two of you sit around and talk about nothing in particular for a few minutes. Alexia says goodbye and waves as she leaves."
            return False

    return True

###########################
###Training Descriptions###
###########################

label public_descrip(name):
    "This will turn [name] into a public slut, ready and willing to have sex with anyone, anywhere. If she's not on birth control she'll try and be careful, but may end up getting pregnant."
    "This training cannot be undone, and will make it harder to train [name] further going forward."
    return

label cumslut_descrip(name):
    "This will turn [name] into a cumslut. She will eagerly swallow your cum, ask you to cover her with it, and still beg you for more. She may also be more willing to go off of her birth control after this training."
    "This training cannot be undone, and will make it harder to train [name] further going forward."
    return

label anal_descrip(name):
    "This will turn [name] into an anal lover. She will be much more open to the idea of anal sex, and have more fun doing it. If she gets to choose, she'll prefer anal over normal sex."
    "This training cannot be undone, and will make it harder to train [name] further going forward."
    return

label freeuse_descrip(name):
    "This will turn [name] in a free use slut. She will be far more willing to have sex with other people, with or without you. The idea of being used like a sex toy gets her incredibly horny, but if she's not on birth control she may end up getting pregnant."
    "This training cannot be undone, and will make it harder to train [name] further going forward."
    return

label exhib_descrip(name):
    "This will turn [name] into an exhibitionist. She will love to flash people or be watched as you have sex with her. The idea of being caught while having sex in a public place makes her instantly wet."
    "This training cannot be undone, and will make it harder to train [name] further going forward."
    return
