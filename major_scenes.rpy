##This file contains all of the labels for major scenes##

##How to add new major scenes:
##Find where you want the major scene to be in the script file.
##Create a Major_Scene object for the scene.
##use  call resistance_gain_report(the_scene,the_girl,the_second_girl) to get the expected Resistance gain from the scene. Second girl only needed in threesomes
##Add an option to take the action or not. Check to make sure the player has at least one serum on them before going forward.


#######################
##Lily's Major Scenes##
#######################



label maj_spikeMovie: ##Lily has an extra movie ticket and no date for tonight. Take her out and have some fun in the theater.
    $ sis_movie_event_object.happened = True
    $ temp_slut_score = 0
    call serum_give(sisO) from _call_serum_give_6
    $ temp_slut_score = _return
    "You check around you quickly to make sure nobody is paying attention to you, then slip a vial of serum into Lily's drink and shake it around gently."
    "Task complete, you head back to the movie theater."
    show sis casual2 at right
    sis "Thanks. You missed a pretty good joke."
    me "Oh well, I think I'll survive without it."
    "A man a row below turns around and shushes at you."
    me "Sorry."
    "You sit down beside Lily and give her the drink, then eat some of your own popcorn."
    "Lily takes a sip of her drink, then turns her attention back to the movie."
    "You give the drug a few minutes to take effect, then lean over and whisper in her ear."
    me "You should finish off your drink."
    "Lily gives you a strange look, but nods and sucks the rest of the small beverage back."
    sis "Why did I need to do that?"
    me "Well I bought you the drink, I wanted to make sure you finished it."
    "She nods, eyes loosely focused on the movie screen."
    menu:
        "Have her flash her tits at you.":
            $sisO.set_action_exhib()
            me "So Lily, I'm finding the movie a little bit boring. Since I was nice enough to come with you to this, would you do a favor for me?"
            sis "Hmm? What do you want?"
            me "Just slip your dress top down so I can take a look at your tits. That would make things more entertaining for me."
            show sis moviestrip1 at right
            $ sisO.inc_naked()
            "Lily thinks about it for a moment, then reaches up to the top of her dress and undoes the ties. She glances left and right to make sure nobody is looking, then pulls the top down and out."
            "Her tits fall free of the dress, illuminated by the changing colours of the movie screen."
            sis "Like this?"
            me "Just like that."
            "You take a good long look at her boobs."
            me "You should just watch the movie like that for a while. I doubt anyone would notice."
            if temp_slut_score > 40:
                sis "You think so? Let me know if anyone looks back."
                "Lily sits back in her chair and goes back to watching the movie. For the next few minutes she sits with her tits out like nothing is unusual."
                "Finally you see a few people coming back from the hallway who might notice, and tap Lily on the thigh."
                show sis casual2 at right
                "Without saying anything she puts her boobs back in her dress and does the ties back up."
            else:
                sis "Ha, you wish."
                show sis casual2 at right
                "Lily starts doing up her dress again, hiding her tits away."
            "You enjoy the rest of the movie and catch a bus back home. Before you go in Lily gives you a hug and a kiss on the cheek."
            sis "Thanks for being a good date."
            "As you both head inside you feel satisfied you had a [sisO.effect_string] impact on her tonight."
            $ sisO.change_slut_rebalanced(action_difficulty)
            $sisO.change_resist(sis_movie_event_object.get_resist_change(1))
            $ sis_movie_event_object.inc_level(1)
        "Have her give you her underwear.":
            $ action_difficulty = 15
            $sisO.set_action_exhib()
            me "Actually, since I was nice enough to cover for your date tonight I think I deserve something special in return."
            sis "What's that?"
            me "I want your underwear."
            if sisO.check_willing(action_difficulty):
                sis "Really? Why?"
                me "Well, if your date was going to get a look at it I want to too."
                "Lily considers it for a moment, then nods and reaches down to her thighs."
                "She slides her dress up and reaches her hands under it, then slides her hands back down. She hands you a pair of small black panties, still warm."
                #TODO extra masturbation options for having her underwear?
                sis "Here."
                me "Wow, these are a little small."
                sis "Well, I was going on a date. I wanted to make sure I was prepared if I needed them."
                me "You're just a grade A skank."
                sis "I am not, I just like like knowing I've got sexy underwear when I need it."
                sis "Now come on, lets watch the movie."
                "You stash Lily's underwear in your pocket and turn your attention back to the movie. For the rest of the run time you're acutely aware that Lily isn't wearing anything underneath her short dress."
                "When the credits roll you head out and catch a bus home. Lily gives you a hug and a kiss on the cheek when you get to the front door."
                sis "Thanks for being a great date. I had a good time."
                "As you both head inside you feel satisfied you had a [sisO.effect_string] impact on her tonight."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_movie_event_object.get_resist_change(2))
                $ sis_movie_event_object.inc_level(2)
            else:
                sis "My underwear? Why would you want that?"
                me "Well if your date was going to get a look at it, it's only fair that I do too."
                sis "He wasn't going to see my underwear! How easy do you think I am?"
                "The man below turns around again and gives you both a stern look."
                me "Sorry sir, won't happen again."
                "Lily crosses her arms and pouts. She's looking like she's in control of herself, she must have resisted the drug."
                me "Sorry Lily. Forget I even said anything. Let's just enjoy the movie."
                "You spend the rest of the movie in awkward silence, then catch a bus home. You feel like you could have done more with the opportunity by not pushing her so hard."
                $ sisO.change_slut_failed()
                $sisO.change_resist(sis_movie_event_object.get_resist_change(0))
                $ sis_movie_event_object.inc_level(0)

        "Have her give you a handjob.":
            $ action_difficulty = 30
            $sisO.set_action_cumslut()
            me "You know, I'm giving up my evening to see this movie with you. I had some plans to spend some time with myself, but that's interrupted now."
            sis "Time with yourself?"
            me "Jerking off, I was going to jerk off sis. I think it's only fair you help take care of me now."
            if sisO.check_willing(action_difficulty):
                sis "Oh, why did you come here then?"
                me "Well I thought you needed a friend for the evening. I didn't want to be a shitty brother."
                "Lily thinks about this for a moment, then nods. She whispers back in your ear."
                sis "Okay, get it out. Be ready to hide it if someone notices."
                "You unzip your pants and slip your cock out. Lily glances left and right, then grabs your shaft and starts rubbing you."
                show sis moviehand1 at right
                $ sisO.inc_hand()
                "You feign interest in the movie while you enjoy your sisters handjob. A few minutes into it your precum starts dripping onto her hand and lubricates it for you."
                "Lily speeds up her strokes and leans close to you to whisper."
                sis "How did you plan on finishing?"
                me "I don't know, on the floor I guess."
                sis "Ew, we're in public."
                "She uses her other hand and slides her dress up, then pulls her panties down her legs and off. They're black, small, and lacy."
                sis "I'll use this to catch it."
                "Seeing your sister strip her underwear off for you so willingly drives you closer to orgasm, and a few seconds later you're getting ready for release."
                me "Okay, now's the time."
                "Lily slips her panties over your tip and wraps them around, then strokes you as fast as she can. The silky feeling of the fabric pushes you over the edge."
                "You hold back a moan as you begin releasing, filling her black lingerie with your cum."
                "Lily lets go of her underwear and leaves it plastered to your cock."
                sis "There, now we can focus on the movie."
                me "Ya. Thanks sis."
                show sis casual2 at right
                "You slip back into your pants, leaving her lingerie in place for now."
                "You watch the rest of the movie together, then catch a bus home. When you get to the front door Lily gives you a hug and a kiss on the cheek."
                sis "Thanks for being a great date."
                "As you both head inside you feel satisfied you had a [sisO.effect_string] impact on her tonight."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_movie_event_object.get_resist_change(3))
                $ sis_movie_event_object.inc_level(3)
            else:
                sis "Ew, what?"
                me "It's not that complicated, I just want you to help get me off."
                sis "In a movie theater? No, that's disgusting."
                "The man below turns around again and gives you both a stern look."
                me "Sorry sir, won't happen again."
                "Lily crosses her arms and pouts. She's looking like she's in control of herself and must have resisted the drug."
                me "Fine. Forget I even said anything. Let's just enjoy the movie."
                "You spend the rest of the movie in awkward silence, then catch a bus home. You feel like you could have done more with the opportunity by not pushing her so hard."
                $ sisO.change_slut_failed()
                $sisO.change_resist(sis_movie_event_object.get_resist_change(0))
                $ sis_movie_event_object.inc_level(0)

        "Have her give you a blowjob.":
            $ action_difficulty = 45
            $sisO.set_action_cumslut()
            $sisO.set_action_freeuse()
            me "It was pretty nice of me to take time out of my schedule and spend time with you sis. How about you get down on the floor and pay me back?"
            if sisO.check_willing(action_difficulty):
                sis "Well, you did want to buy the ticket from me."
                me "I was doing that as a favour, so you didn't have to spend the night alone."
                "Lily thinks about it for a long while, then glances left and right to check for people."
                sis "Fine, but let me know if anyone looks our way."
                show sis movieblow1 at right
                $ sisO.inc_blow()
                "Your sister gets off her chair and crouches in front of you while you pull your pants down enough to get your cock out. Lily slides her dress up and spreads her knees so she can stay on her feet."
                "Down in the aisle she's barely more than a shadow as she takes your cock in her hand and moves it to her mouth."
                sis "Warn me when you're going to finish, okay?"
                "You nod, and Lily slips your tip into her mouth. She licks it quickly, then moves it deeper. After a few seconds she has most of your length wet and starts bobbing her head up and down."
                "You sit back and pretend to watch the movie while Lily blows you. You rest a gentle hand on her head, stroking her hair as she services you."
                "After a few minutes of Lily taking your cock in her mouth you can feel yourself getting close to finishing."
                menu:
                    "Surprise her and cum down her throat.":
                        show sis movieblow2 at right
                        "You wait until you're ready to finish, then press Lily's head down on your shaft. Her mouth tightens up suddenly, but she doesn't make a sound while you hold her down."
                        "You pump your hips a little bit, bumping your tip into the back of her throat, then tense and begin releasing your load."
                        if sisO.cumslut:
                            "Lily grips your thighs tightly, eyes rolling up and fluttering with pleasure as you pump your cum directly into her stomach."
                        else:
                            "Lily grips your thighs tightly and closes her eyes, but does her best not to make a sound while you pump your cum directly into her stomach."
                        "When you're done you pull out suddenly and pull your pants up quickly. Lily takes a deep breath and coughs loudly."
                        "The man below you turns around and looks at you both."
                        me "Sorry, she just inhaled a little bit of popcorn."
                        show sis casual2 at right
                        $ sisO.inc_cum_mouth()
                        $ sisO.inc_cum_swallow()
                        "Lily nods and takes her seat again, and the man turns back to the movie."
                        if sisO.cumslut:
                            sis "There was so much... I wasn't sure I could take it all like that."
                            me "You did a great job Lily, that felt great."
                            "She nods and cuddles up close to you."
                        else:
                            sis "I told you to warn me!"
                            me "Well, you got me there a little faster than I thought you would. Besides, I didn't want to make a mess. Unless you want people to see you covered in cum."
                            sis "Of course not, I had a plan."
                            me "So did I, and it all worked out. Thank you sis."
                            sis "You're welcome, I guess. Now lets watch the movie."
                        "You and Lily watch the rest of the movie, then catch a bus home. When you reach the door she gives you a hug and a kiss on the cheek."
                        sis "Thanks for coming with me, I had fun."

                    "Warn her and let her deal with it.":
                        "You tap Lily on the shoulder and lean down a little."
                        me "I'm getting close."
                        "Lily nods and speeds up, taking you as deep as she can into her throat."
                        "A few more strokes and you're ready to finish. You begin tensing up and Lily pulls you from her mouth."
                        show sis movieblow3 at right
                        $ sisO.inc_cum_over()
                        "With quick hands she slips your tip into the top of her cleavage and strokes you off. You unload inside her dress, shooting most of it between her tits."
                        "Lily stands up quickly and takes her seat again. You can see a few drops of cum that landed outside the dress or soaked their way through already, but Lily seems to be ignoring them."
                        if sisO.cumslut:
                            sis "It feels so warm... Thank you [inputName]."
                        else:
                            sis "There, now we're even."
                        show sis casual2 at right
                        me "Thanks. Now we can enjoy the movie together."
                        "You and Lily watch the rest of the movie, then catch a bus home. You spend the entire trip watching how her dress fabric clings tightly to her upper body, outlining her tits."
                        "When you get home Lily gives you a hug and a kiss on the cheek."
                        sis "Thanks for being a good date. I had fun."
                "As you both head inside you feel satisfied you had a [sisO.effect_string] impact on her tonight."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_movie_event_object.get_resist_change(4))
                $ sis_movie_event_object.inc_level(4)
            else:
                sis "What? You want me to get on the floor?"
                me "Yes, and take care of me."
                sis "Ew, no. Besides, I didn't make you come here with me. You offered."
                "Lily crosses her arms and turns away from you. She looks like she's already back in control of herself and has resisted the drug."
                me "Fine. Forget I even said anything."
                "You spend the rest of the movie in awkward silence, then catch a bus home. You feel like you could have done more with the opportunity by not pushing her so hard."
                $ sisO.change_slut_failed()
                $sisO.change_resist(sis_movie_event_object.get_resist_change(0))
                $ sis_movie_event_object.inc_level(0)

        "Have her sit on your lap and fuck her.":
            $ action_difficulty = 75
            $sisO.set_action_cumslut()
            $sisO.set_action_freeuse()
            $sisO.set_action_exhib()
            me "Hey Lily, this movie is kind of boring me. Slide over here onto my lap and I'll make things a little more interesting."
            if sisO.check_willing(action_difficulty):
                sis "You really aren't liking this? I love it!"
                me "Of course you do, you got to pick the movie."
                "Lily laughs quietly, but pulls her dress up a little bit and slides over onto your lap."
                show sis moviefuck1 at right
                $ sisO.inc_sex()
                "She grinds her hips against yours, rubbing her ass against your erection."
                me "Come on, I need you to take care of me Lily. You're a good little sister, right?"
                "Lily reaches down between her legs and rubs your crotch, then pulls your zipper down and slips your cock out of your underwear."
                if sisO.exhib:
                    sis "Shush, I'm watching the movie. Just sit back and enjoy."
                else:
                    sis "Shush, someone might hear. Please make it quick."
                show sis moviefuck2 at right
                "She rubs your cock gently and presses it against her underwear, grinding her pussy against it through the fabric."
                "You sit back and let Lily stroke you gently. Before long you can feel her underwear getting damp while she rubs against you."
                me "Come on sis, you know you want it. Slide those panties aside and get to work."
                "Lily nods and pulls her underwear out of the way. She stands slightly, slips your tip into her pussy, and sits back down slowly."
                "She's already dripping wet, and sighs quietly as you slide into her. She places her hands between both of your legs on the chair and uses them to help push herself up and down."
                me "That's a good girl. You feel great."
                sis "You too."
                show sis moviefuck3 at right
                "She speeds up her strokes, leaning forward slightly to get a better angle. You also get a nice view of her ass bouncing up and down from behind her."
                "After a few more strokes Lily's legs start to shake and she moans even louder. You slip your hand around her mouth to stop her from making noise that might alert someone."
                me "Easy there. You don't want people to see you like this do you?"
                "Lily pumps her hips up and down on your shaft and breaths heavily into your hand."
                me "Or maybe you do, maybe you want people to see what a slut you are."
                if sisO.exhib:
                    "She nods her head up and down. her pussy twitches around your cock, on the verge of an orgasm while you fuck her."
                    me "You like being fucked by your brother, surrounded by people?"
                else:
                    "She shakes her head left and right, but keeps pumping her ass up and down. Her pussy twitches around your cock, on the verge of an orgasm."
                    me "You don't want them to know? Maybe you like being my personal slut then?"
                "Lily nods yes and her legs tighten suddenly. She tries to moan, but you clamp down hard on her mouth to stop any sound from escaping. Her pussy tightens suddenly, then flutters a few times while she cums."
                "Feeling her orgasming on you brings your own orgasm suddenly close."
                menu:
                    "Cum inside of her.":
                        "You whisper right into her ear."
                        me "Okay then slut, I'm going to fill you up."
                        "She shivers with pleasure and slides herself up and down as fast as she can without making any noise."
                        "You keep one hand over her mouth and put the other on her hip. She pumps as fast as she can on shaky legs."
                        "When you start to cum you pull Lily down onto it as hard as you can. She collapses onto your spasming cock, shaking from her own orgasm and moaning into your hand as loud as she dares."
                        "You hold her there until you're completely finished, then let go of her mouth and give her ass a quick slap."
                        show sis moviefuck4 at right
                        $ sisO.inc_cum_inside()
                        "She stands up slowly and slides her panties back into position to catch any drips. Then she slumps down into the chair beside you and takes a few deep breaths."
                        "You pull your pants back up quickly and check to make sure nobody saw. It looks like you're in the clear."
                        me "Well done sis, you were great."
                        "Lily nods weakly and smiles, still breathing heavily."
                        show sis casual2 at right
                        "You watch the last few minutes of the movie, then catch a bus home. Lily shifts awkwardly while you're standing around, trying to stop your cum from dripping down her legs."
                        "When you get to the door she gives you a hug and a kiss on the cheek."
                        sis "Thanks for taking me out tonight, I had fun."

                    "Cum in her mouth.":
                        "You whisper right into her ear."
                        me "Okay then slut, I'm almost ready to cum. I want you to catch it in your mouth so there's no mess."
                        "Lily shivers with pleasure as she rides you and nods a few times."
                        "You place a hand on her hip and use it to guide her up and down faster. You get the feeling she's going as fast as she can on her shaking legs."
                        "After a few more strokes you're ready to cum and slap her lightly on the ass to let her know."
                        show sis moviefuck5 at right
                        $ sisO.inc_cum_mouth()
                        $ sisO.inc_cum_swallow()
                        "Lily stands up and spins around, dropping into a crouch at your feet. She wraps her mouth around your tip and gives you a quick and fast blowjob."
                        "You tense up and begin to unload into your sisters mouth. She grunts in surprise when the first pulse lands, but stays quiet for the rest. She licks your tip as you finish, making sure you're completely clean."
                        me "Good girl. Now open up so I can see."
                        show sis moviefuck6 at right
                        "Lily opens her mouth and shows you your own cum. She plays her tongue through it, pooling it on one side then the other."
                        me "Excellent. Now swallow for me, whore."
                        "She closes her mouth and looks away for a moment, then looks back and opens her now empty mouth."
                        if sisO.cumslut:
                            sis "Thank you [inputName], you tasted great."
                        show sis casual2 at right
                        "You sit back, completely spent, and Lily collapses beside you into her chair. You watch the last few minutes of the movie absentmindedly, then catch a bus home."
                        "When you get to the door Lily gives you a hug and a kiss on the cheek. You can still smell your semen on her breath."
                        sis "Thanks for taking me out tonight, I had fun."
                "As you both head inside you feel satisfied you had a [sisO.effect_string] impact on her tonight."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_movie_event_object.get_resist_change(5))
                $ sis_movie_event_object.inc_level(5)
            else:
                sis "Hmm? I'm liking the movie just fine."
                me "Well it would make it more interesting for me. Just slide your dress up and leave the rest to me."
                sis "Ew, what? No, it's a movie theater."
                me "Come on sis, this is taking up most of my day."
                sis "Well, you should have thought of that before you bought the ticket."
                "The man below turns around again and gives you both a stern look."
                me "Sorry sir, won't happen again."
                "Lily crosses her arms and ignores you. She's looking like she's in control of herself, she must have resisted the drug."
                me "Sorry Lily. Forget I even said anything. Let's just enjoy the movie."
                "You spend the rest of the movie in awkward silence, then catch a bus home. You feel like you could have done more with the opportunity by not pushing her so hard."
                $ sisO.change_slut_failed()
                $sisO.change_resist(sis_movie_event_object.get_resist_change(0))
                $ sis_movie_event_object.inc_level(0)
    jump jumpTimeSkip

label maj_spikeSisNight: ##Run into Lily at night and offer to get her some water, then head back to her room and have some fun.
    $ sis_night_event_object.happened = True
    $ temp_slut_score = 0
    call serum_give(sisO) from _call_serum_give_7
    $ temp_slut_score = _return
    "You get some serum from your room, pour it into Lily's water, and mix it in with a fork. In the dark it's impossible to see what colour the water is."
    show sis casual_night at right
    "With drink in hand you head back upstairs to Lily's room. Her door is open but the lights are off. She's sitting on her bed looking at her phone."
    me "Knock knock."
    sis "Thanks [inputName]."
    "Lily takes the drink and takes a long sip of it."
    sis "Did you get me juice or something?"
    me "No, just normal water. You should keep drinking."
    "Lily looks at you strangely, but the small dose must be having some effect. She drinks the rest of the glass without saying a word."
    me "That's good. How do you feel?"
    sis "Sleepy, but I'm not thirsty any more."
    "Her eyes are unfocused. The drug has taken effect."
    "You close the door to her room and turn on the light."
    me "Well don't get too comfortable. It's too early for us to be going to sleep."
    sis "Too early?"
    me "Right, we've got plenty of stuff to do tonight."
    "She nods lightly, waiting for you to suggest something."
    menu:
        "Have her take her pajamas off for you.":
            $ action_difficulty = 0
            $sisO.set_action_exhib()
            $sisO.check_willing(action_difficulty)
            me "You might have been right about the humidifier Lily. It's feeling really warm in here, isn't it?"
            sis "A little bit, it's hard to tell."
            me "It's definitely warmer than usual. You're probably getting too hot in your pajamas."
            "Lily shifts uncomfortably in her clothes and nods."
            sis "Ya, I am getting uncomfortable."
            me "There's no reason to be uncomfortable at night in your own room. You should strip down and sleep in your underwear."
            "Lily nods."
            sis "That's a good idea. That way I'm not so hot."
            "She stands up, unbuttoning her long green shirt. When she finishes she peels it off and throws it into her dirty laundry pile."
            show sis nightstrip1 at right
            $ sisO.inc_naked()
            "Underneath she's wearing a loose pink bra. She reaches for her waist and pulls down her pants, revealing a matching set of panties."
            "She stands up and sighs."
            sis "You were right, that's much better."
            me "See how much more free you feel? You can do stretches, jump around, touch your toes."
            sis "Yep. Look how far I can bend over now, without all that stuff in the way."
            "Lily leans forward as far as she can, brushing her toes with her fingertips."
            show sis nightstrip2 at right
            "You walk around to the far side to get a nice look at her ass and pussy through her underwear."
            sis "What are you doing back there?"
            me "Looking at your pose. You're really flexible sis. That's good."
            "Lily straightens up and smiles."
            sis "Thank you! Now I'm feeling nice and comfortable, I think it's time for bed."
            "You nod and head for the door."
            me "Have some great dreams Lily."
            sis "You too. Night bro."
            "You flick the lights off as you leave and head back to your room. You're sure you had a moderate effect on Lily with that."
            $sisO.change_slut_rebalanced(action_difficulty)
            $sisO.change_resist(sis_night_event_object.get_resist_change(1))
            $sis_night_event_object.inc_level(1)

        "Have her try on different outfits for you while you masturbate.":
            $ action_difficulty = 15
            $sisO.set_action_exhib()
            me "You always seem to wear the same sort of stuff around the house. I'm sure you have other clothes hanging around."
            "Lily nods in agreement."
            me "I'm sure you even have some really sexy stuff, stuff you don't want mom to know about."
            "Lily nods again."
            me "I want you to show me some of that stuff, it's a shame it never gets used."
            if sisO.check_willing(action_difficulty):
                sis "Ya, it is a waste. I should show it off some more."
                "Lily goes to her closet and reaches as high up as she can. She drags down a large hat box and brings it over to the bed."
                sis "This is where I keep everything I don't want people to know about."
                "She opens the box, and reveals a pile of lace and frills."
                sis "You want me to try it on?"
                me "Yes I do sis, I want to see how sexy you can look."
                "Lily hesitates for a moment, then reaches into the box and shuffles some stuff around. She finally comes up with a black lace bra and matching panties."
                sis "How about this?"
                me "Sure, show me how it looks."
                show sis strip2 at right
                "Lily takes off her pajamas, then strips out of her normal pink bra and panties."
                show sis nightstrip3 at right
                $ sisO.inc_naked()
                "Then she slips on the thin black panties, and slides the bra over her shoulders."
                sis "The bra is a little small, I don't feel like I fit in it."
                me "You look great. You've already got me rock hard."
                "To demonstrate, you slip your cock out the top of your pants."
                sis "Oh wow, I didn't realise it would be so quick."
                me "Well that happens when you find out your sister is a closet slut."
                sis "I'm not a slut, I just like having fancy clothes."
                me "Turn around for me."
                show sis nightstrip4 at right
                "Lily does, turning to show her butt to you."
                me "An expensive coat is fancy clothes, a new shirt could be fancy clothes."
                "You spank her on the ass and she yelps quietly."
                me "This is fancy lingerie, used for being slutty for someone."
                sis "So what if it is. I can be slutty for someone if I want."
                show sis nightstrip5 at right
                "She bends over more and spreads her legs, showing off the gap between."
                me "That's right, nothing wrong at all with being a slut."
                "You spank her again, this time she moans instead."
                me "Now, what else to you have to show off?"
                "You sit back on her bed and start stroking yourself."
                sis "Well, I've got something I was saving."
                me "Saving for what?"
                "Lily pulls a white corset out from the bottom of the box, then a matching garter belt and tissue thin set of panties."
                sis "A special occasion."
                me "Try them on, I want to see."
                show sis nightstrip6 at right
                "You stroke faster as Lily strips out of the black lingerie in front of you and begins sliding on the white. It looks like she's getting ready for her wedding."
                "As she tightens up the corset you can feel yourself getting close to cumming."
                sis "Do you like this?"
                "You nod fiercely, building yourself right up to the edge."
                me "I do. Turn around and bend over for me."
                show sis nightstrip7 at right
                "Lily does, her pristine ass and virginal looking pussy call for you as you blow your load all over her."
                "You land your cum on her back, ass and thighs, then lean back panting heavily."
                show sis nightstrip6 at right
                "Your sister jumps in shock, then turns around."
                sis "Did I just make you cum?"
                "You nod, panting."
                sis "Just by changing clothes in front of you?"
                me "What do you expect sis. You're a gorgeous babe in sexy underwear. I'd fuck you right now if I could."
                "She seems to think about that."
                sis "Well now that you're done you should get going and let me get to sleep."
                me "Sure thing."
                sis "Thanks for the drink."
                "Lily is peeling off the white lingerie already."
                me "No problem, sleep tight."
                "You head back to your room, confident that you had a large effect on her,"
                $sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_night_event_object.get_resist_change(2))
                $sis_night_event_object.inc_level(2)
            else:
                show sis nightstrip1 at right
                "Lily nods and begins stripping down in front of you. She throws her pajamas into the dirty hamper and is standing in her pink underwear."
                sis "So I never tell anyone about this stuff."
                me "It's okay to tell me. You can trust me."
                sis "Are you sure? I'm kind of nervous."
                me "Nothing at all to be nervous about. Look, you're already in your underwear right now."
                "Lily nods."
                sis "How about I just show this off to you first. To get used to it."
                me "Fine, if that helps."
                "Lily turns around and bends over a little."
                sis "I like this because it's so soft and silky, like someone's always touching me."
                me "Do you have anything else silky like that."
                sis "Some stuff, ya."
                "She turns around and presses her tits together so the bra bunches up."
                me "How about you show me some of the other stuff now."
                "Lily hesitates, then shakes her head."
                sis "No, I don't think I can do it."
                "She sits down on the bed quickly and starts pushing at you."
                sis "You should get out of here, we don't want to wake mom up."
                me "Come on sis, a little show and then I'll be gone."
                sis "I can't do it [inputName], it just feels too weird."
                "It looks like she's resisted the drug. Maybe you pushed her too far."
                me "Okay. Maybe some other night then."
                "Lily nods and slips under her covers as you leave the room. You might have had some effect, but you feel like you could have done better."
                $sisO.change_slut_failed()
                $sisO.change_resist(sis_night_event_object.get_resist_change(0))
                $sis_night_event_object.inc_level(0)
        "Have her jerk you off on her bed.":
            $ action_difficulty = 25
            $sisO.set_action_cumslut()
            me "Now that I'm in here, I'm wondering something. Do you ever masturbate in here?"
            "Lily hesitates, then nods."
            sis "Yes, sometimes when I'm horny."
            me "I know what that feels like. I'm horny a lot, and masturbating just doesn't seem to help."
            sis "That must be hard, I know I can't focus when I'm horny."
            me "Me neither. And it's always you making me hard, so I can't get any relief here at home."
            sis "Me?"
            me "You sis, you're always running around in a short dress or hot pants, leaning over to get things or reaching for a high shelf. I can't go a single day without wanting to fuck you."
            sis "We couldn't do that. It wouldn't be right."
            me "No, but you could help me by giving me a handjob, right? That wouldn't be weird."
            if sisO.check_willing(action_difficulty):
                sis "I guess you're right. Just a handjob is fine. You should lie down."
                "You lie down on Lily's bed and prop your head up with a pillow. Lily lies down beside you and reaches a hand into your pants."
                show sis nighthand1 at right
                $ sisO.inc_hand()
                "You help her slip your cock out of your pants, and she begins stroking it."
                sis "Like this?"
                me "That's the idea."
                "Lily strokes your cock slowly for a few minutes."
                sis "It's a little too dry to do this well."
                me "I don't suppose you keep any lube..."
                "Lily sits up onto her knees and bends over, then licks your cock from the base to the tip. She repeats it for the other side."
                sis "That should help."
                "She returns to lying next to you, and resumes stroking your now wet shaft. Her warm wet hands get you close to cumming very quickly."
                me "I'm going to cum soon. Keep going."
                sis "Wait, you'll get my bed dirty!"
                "Despite this, she doesn't stop jerking you off."
                show sis nighthand2 at right
                "Lily struggles with her pants, trying to get them off while still stroking you. She succeeds, and you realise she's brought her panties too."
                sis "Here, cum into this."
                "She places her used panties around your tip and strokes you faster than ever. You build up to climax and release."
                sis "There we go, use my underwear."
                "She twists the soft panties around, and you shiver from the feeling. When you're finished cumming she pulls them off, trailing thick strands of cum."
                me "That was some good thinking sis."
                "Lily smiles and nods."
                sis "You should be able to get to sleep now. Have a good night."
                me "You too."
                "You head out of Lily's room satisfied and certain you made a [sisO.effect_string] impact tonight."
                $sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_night_event_object.get_resist_change(3))
                $sis_night_event_object.inc_level(3)
            else:
                "Lily pauses then shakes her head."
                sis "I'd still have to touch you, it would be weird."
                me "Even if it's just a little bit?"
                "She nods repeatedly."
                sis "But I don't want you being horny because of me. How about you masturbate while looking at me?"
                me "It would be better if you did it yourself."
                sis "I won't do that, it's crossing a line."
                me "Okay, I'll jerk myself off then and watch you."
                show sis nightstrip1 at right
                "Lily stands up and starts stripping down. She's in a pink bra and panties."
                sis "How about this?"
                "You pull your cock out and start stroking while Lily looks away shyly."
                "Lily stands still in her underwear and doesn't stay a word."
                me "Are you sure you don't want to help, just a few strokes?"
                "She shakes her head, still not making eye contact."
                "Disapointed in how the night has gone, but not wanting to risk anything more, you eventually cum gently over your own hand."
                sis "There you go, you can go now."
                me "Thanks sis. Have a good night."
                "Lily nods and closes her door after you as you leave. You must have pushed her too far all at once."
                $sisO.change_slut_failed()
                $sisO.change_resist(sis_night_event_object.get_resist_change(0))
                $sis_night_event_object.inc_level(0)

        "Have her suck you off.":
            $ action_difficulty = 40
            $sisO.set_action_cumslut()
            $sisO.set_action_freeuse()
            me "You know what I've always had fun with? Blowjobs. I love getting head, especially from a cute little slut like you."
            if sisO.check_willing(action_difficulty):
                "Lily doesn't move for a moment, but then nods."
                sis "I kind of like giving head too. I hope that doesn't make me too much of a slut."
                me "There's no such thing sis. Come on, lets have some fun."
                "She moves towards you, but you hold out a hand."
                me "But first, I want you to get out of your pajamas. I want to see your tits bounce while you suck me off, and your pussy get wet."
                sis "Okay, I can do that."
                show sis strip2 at right
                "Lily takes off her pajamas, then slips off her pink bra and panties and throws them into the dirty clothes hamper as well."
                "Her nipples are hard already."
                me "That's better. Okay, come kneel down in front of me."
                "She follows your directions and gets down in front of where you sit on her bed while you pull your cock out."
                show sis nightblow1 at right
                $ sisO.inc_blow()
                "She reaches out and takes it, then runs her tongue along the bottom. The sensation of her warm wet tongue sends shivers down your spine."
                "As she reaches the top of your cock she opens her mouth and slides it inside. She bobs up and down slowly, going a little deeper with each stroke."
                "She pulls off, sucking on the tip before she lets go, and looks at you."
                sis "How's that?"
                me "Great, it feels great."
                "She smiles and puts your shaft back in her mouth, sliding it up and down."
                "Her tongue works it's way around your cock, licking up the left and right side as she slides it into her throat."
                "After a few minutes of skillful work, you can feel yourself getting close to orgasming."
                menu:
                    "Cum in her mouth.":
                        me "Sis, I'm going to cum soon. Just keep going and don't let go no matter what."
                        "Lily nods as she goes up and down, up and down. If anything she speeds up when she hears you're close."
                        me "You're a good little slut Lily, other people might not know how much of a cock gobbler you are, but I know."
                        "She doesn't say anything, but blows you even faster."
                        if sisO.cumslut:
                            "Finally you tense up and begin to unload into her mouth. Lily shivers with pleasure as your hot cum splashes out over her tongue."
                        else:
                            "Finally you tense up and begin unloading yourself into her mouth. Lily almost pulls your cock out, but you place a firm hand on the back of her head and keep her still, and she slids back on slowly."
                        show sis nightblow2 at right
                        $ sisO.inc_cum_mouth()
                        "A few seconds after the last pulse of sperm enters your sister's mouth you let her pull off."
                        me "Oh god, you're a good slut Lily."
                        "Lily pants heavily, trying to breath around a mouth full of cum. She looks at you, unsure of what to do."
                        menu:
                            "Tell her to swallow":
                                me "I want to watch you swallow that sis, swallow the whole thing."
                                $ sisO.inc_cum_swallow()
                                "Lily tries to say something, but only makes bubbles with your cum. After a moment she nods and closes her mouth, swallowing loudly."
                                me "Good girl."
                                "She pants heavily and leans on the bed frame at your feet."
                                "Satisfied, you head out of Lily's room as she pulls herself into bed. You definitely had a major effect on her mind tonight."

                            "Tell her to spit it onto her tits":
                                me "You can spit it out, but let it out onto your tits."
                                show sis nightblow3 at right
                                "Lily nods, leans back onto her ass and one hand and looks down. She opens her mouth and lets your cum drizzle out onto her tits. She even moves her head left and right to drape it between the two."
                                "She looks up at you with tired eyes and tries to smile. Your cum is draped across her tits and over her erect nipples."
                                sis "Like that?"
                                me "Just like that."
                                "Satisfied, you head out of Lily's room as she reaches for her used underwear to wipe herself off. You definitely had a major effect on her mind tonight."

                    "Cum on her face.":
                        me "I'm going to cum soon. I want to spray it over your face. Look at me and don't close your eyes. Okay?"
                        "Lily mumbles something, but doesn't stop sucking."
                        "A few more strokes of her throat and you're ready. You pull your shaft out of her mouth and point it at her face."
                        "Lily opens her mouth wide and sticks her tongue out for you, and looks you in the eyes as you start releasing cum across her."
                        show sis nightblow4 at right
                        $ sisO.inc_cum_over()
                        "You finish with the last pulse of cum and let your cock fall on your sister's face. She moans softly, panting with exertion."
                        "You wonder how much of the drug is still in effect."
                        me "Now sis, listen to me."
                        "You rub your sensitive shaft over Lily's face, spreading your cum around."
                        me "I want you to leave this on for the night. Make sure you don't rub it off until morning, okay?"
                        if sisO.cumslut:
                            "Lily nods eagerly as your ccock glides over her slippery face."
                            sis "Why would I ever want to get rid of this? It feels so nice."
                        else:
                            "Lily nods slowly as your cock glides over her slippery face."
                            me "Good. It's good for your skin, I'm sure. A slut like you needs perfect skin."
                            sis "Of course. I'll do it for you."
                        "Satisfied, you head out of Lily's room as she gets into bed naked and plastered with your cum. You definitely had a major effect on her mind tonight."
                $sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_night_event_object.get_resist_change(4))
                $sis_night_event_object.inc_level(4)
            else:
                sis "A blowjob? Right now?"
                "She shakes her head, but begins unbuttoning her shirt anyway."
                me "Why not. We're both up, I'm excited."
                sis "But it's late, we should be in bed."
                "Her shirt comes off, she's got a cute pink bra on."
                me "Don't worry about that. Come on, just get on your knees and take care of me."
                "Lily hesitates as she plays with her waistband."
                sis "I don't think this is a good idea."
                "She nods, agreeing with herself."
                sis "I think you should go for now. Maybe some other time."
                "Damn, she must have resisted the drug. Maybe you pushed her too hard."
                me "Okay sis, if you don't want to."
                sis "Not right now. Goodnight, thanks for the drink."
                "You head back to your room, frustrated that you couldn't make better use of the situation."
                $ sisO.change_slut_failed()
                $sisO.change_resist(sis_night_event_object.get_resist_change(0))
                $sis_night_event_object.inc_level(0)

        "Fuck her on her own bed.":
            $ action_difficulty = 60
            $sisO.set_action_freeuse()
            me "Take off your clothes and get on the bed Lily, I'm horny and you need to take care of it."
            if sisO.check_willing(action_difficulty):
                sis "Did I make you horny?"
                "Lily begins stripping off her clothes, throwing her pink panties into the dirty laundry hamper."
                me "You did, you're always walking around in a skirt begging to be fucked. I've held it back for so long, you need to take responsibility for it though."
                show sis nightfuck1 at right
                "She nods as she gets her bra off and drops it to the floor. Lily lies down on the bed, legs spread open."
                me "Not so quick. Spin sideways."
                "You push on Lily's shoulder as you stand beside the bed and push at Lily's shoulder. She shuffles around until her head is off the side of the bed."
                me "First I need you to get me warmed up."
                "You drop your pants to your feet and pull our your cock, letting it rest on Lily's cheek."
                me "Open up, slut."
                show sis nightfuck2 at right
                "Lily nods and opens her mouth, presenting her throat for you to use."
                "You slide the tip into her mouth slowly, letting her work her tongue over it to get it wet."
                "Inch by inch you slide deeper in your sister's throat. Lily's hands fondle her breasts and she moans and gags as you slide your full length into her throat."
                "You hold yourself deep in her, then slide out slowly. When you pull out of her mouth she breaths deeply, then you slide back in."
                "Fully wet now, you hold Lily's head with your hands and move your waist back and forth. Her throat makes pleasant bubbling sounds as you hit the back, and she gags and coughs gently as you throat fuck her."
                me "That's a good little whore. Take me down your throat."
                "You put yourself in as deep as you can and hold your cock down Lily's throat. She works her tongue along the base while she waits for you to pull out."
                "Seconds pass, and you stay fully sunk into her throat. She pats you gently on the thigh."
                me "Just wait sis, you're doing great."
                show sis nightfuck3 at right
                "Lily gasps for air, but only sucks harder on your cock. She pats your leg again, harder."
                me "Not quite yet. Keep it up, slut."
                "Lily digs her nails into your thighs as her lungs start to spasm. Her throat constricts around your cock, gripping it tight like it doesn't want to let go."
                "Almost brought to orgasm you pull yourself out of her throat suddenly, and Lily gasps for air and coughs violently."
                sis "You almost choked me!"
                me "You felt amazing. I didn't feel teeth once. You're incredible at deepthroat sis."
                if sisO.cumslut:
                    sis "Could you... finish in my throat next time you do that?"
                    me "Sure thing Lily, maybe next time."
                "Lily gets onto the bed properly and coughs some more. You can see she's dripping wet between her legs."
                me "Spread yourself. Your throat got me nice and close, I want to fuck you till I cum now."
                show sis nightfuck1 at right
                $ sisO.inc_sex()
                "She nods and spreads her legs, arms above her head to make room for you."
                sis "Hurry up and fuck me then!"
                "You climb on top of your sister and slide yourself into her. She's wet enough that you glide to the end of her pussy on the first stroke."
                sis "Oh fuck that's nice."
                "You slide in and out of your sister, feeling her twitch with every stroke. One of her hands is rubbing her clit furiously as you fuck her."
                me "That's a good little whore, I want you to cum before I do."
                "She nods and grinds against your hips as you thrust, touching herself and moaning softly."
                "Within seconds you feel Lily tense up, her thighs wrap around your back and she shudders in your arms as she cums. You pump faster as she orgasms."
                sis "Fuck, I'm cumming, fuck fuck fuck!"
                me "I'm close too! Get ready!"
                menu:
                    "Cum inside her":
                        "You grab Lily's hips and pull her into you, releasing at the apex of your stroke. Your cum floods into her drenched pussy as she orgasms again."
                        if sisO.cumslut:
                            sis "Yes, pump me full of your sperm! Oh god yes!"
                        else:
                            sis "Fuck!"
                        "You slide in and out a few more times for good measure, then pull your wet cock out of her."
                        show sis nightfuck4 at right
                        $ sisO.inc_cum_inside()
                        "Lily lies on the bed, twitching slightly. Her stomach finally relaxes and you see a trickle of your cum run out and down her ass."
                        me "There we go. That was great sis."
                        "She nods, but doesn't seem to be able to make words."
                        "You get yourself cleaned up and head back to your room, happy to know you've made a [sisO.effect_string] impact on her tonight."

                    "Cum on her stomach":
                        "You pull out at the last moment and rub your shaft along Lily's pussy. She moans and grinds up against it, pushing you the last way to orgasm."
                        show sis nightfuck5 at right
                        $ sisO.inc_cum_over()
                        "You stroke your cock as you pump your seed onto her stomach, then drip cum onto her pussy below you."
                        "Both of you pant heavily for a few minutes before you get up."
                        me "That was amazing. We should do that again."
                        "Lily nods, but doesn't seem to be able to form any words right now."
                        "You get yourself cleaned up and head back to your room, happy to know you've made a [sisO.effect_string] impact on her tonight."
                $sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_night_event_object.get_resist_change(5))
                $sis_night_event_object.inc_level(5)
            else:
                sis "Right now, on the bed?"
                show sis nightstrip1 at right
                "She hesitates, but starts taking her clothes off."
                me "Right now, I want to lay you down and fuck you till I cum. You're my good little slut, right?"
                sis "I'm not your slut, don't say that!"
                "She throws her pants at you."
                sis "Get out of here before I tell mom what you did and get you kicked out!"
                "You duck out of the room as Lily slams the door. You must have pushed her too quickly and she resisted the drug."
                $sisO.change_slut_failed()
                $sisO.change_resist(sis_night_event_object.get_resist_change(0))
                $sis_night_event_object.inc_level(0)
    jump newDay

label maj_spikeLilyMorning: ##Bribe your mom to slip Lily some serum in the morning and give you some time alone with her to have some fun.
    $ sis_morning_event_object.happened = True
    me "Actually, I could use your help with something mom. We've been doing some experiments down at the lab, and we've come up with some pretty impressive stuff."
    "Mom nods, listening intently."
    me "It's a sort of medicine, and I think Lily would be a great test subject. It won't work as well if she knows about it though, so I need to sneak it into her drink or something."
    me "Could you help me with that? For $100?"
    "Mom hesitates and shuffles back and forth."
    mom "You're sure it's safe? I wouldn't want anything hurting my baby girl."
    me "Of course it's safe, plenty of people have tested it out before. I just need you to slip it into her drink this morning."
    "Mom thinks some more, then nods."
    mom "Okay, if you say it's safe."
    $ temp_slut_score = sisO.slut_score
    call serum_give(sisO) from _call_serum_give_8
    $ temp_slut_score = _return
    "Once that's done, we'll need the house to ourselves. I'll need to perform an interview and run some tests, and you being around might upset them."
    mom "Okay, I can go out and get groceries for us all."
    me "Sounds good. Here's your cash."
    "You hand over $100"
    $ player_money += -100
    "Mom gets a two glasses of orange juice ready, and the two of you pass the time chatting while you wait for Lily to get up."
    "Finally, you hear her door open and close, and her footsteps get closer."
    "Mom opens the vial and pours it into one of the glasses."
    show mom casual at left
    show sis casual1 at right
    sis "Good morning you two. You're both up early."
    me "Mom had my check, I'm not just going to let her run away with my money!"
    mom "Good morning Lily. I'm going out to get some groceries for breakfast, but I poured you both some juice."
    sis "Oh, thanks."
    "Lily takes the drink from mom and begins sipping it."
    mom "You two play nice, I'll be back in an hour or so."
    "Mom looks at you one last time, then turns and hurries out the door."
    hide mom
    sis "That was weird, I thought we still had eggs or something left for breakfast."
    me "Maybe they went bad. Anyway, make sure to drink up."
    "You down your own drink, and wait for Lily to do the same."
    sis "Hmm, maybe you're right. The orange juice tasted a little off too. Glad we finished it then."
    "Lily's eyes lose focus, and she stares past you. The drug must be taking effect."
    me "Everything okay Lily, feeling good?"
    sis "Ya, feeling fine. Like nothing is bothering me kind of fine."
    me "That's good."
    menu:
        "Have her take her dress off.":
            $ action_difficulty = 0
            $sisO.set_action_exhib()
            $sisO.check_willing(action_difficulty)
            me "So sis, we're at home all alone. There's no reason for you to be so dressed up. You should take your dress off and just relax."
            "Lily looks at you, then nods in agreement."
            sis "You're right, it's silly for me to be wearing this around the house. It's so much more comfortable without it."
            "She slips the straps of her dress over her shoulders and lets it drop to the ground. She's not wearing a bra underneath it, and has a cute set of pink panties on."
            show sis strip1 at right
            $ sisO.inc_naked()
            me "That's better. You look great sis."
            sis "You think so?"
            "She twirls on the spot, showing off her ass from all angles and jiggling her free tits."
            me "Definitely. You act all pure and sweet, but you're body definitely thinks otherwise. You'd make a great slut."
            sis "Hey, don't say that! I'm a good girl!"
            "Lily pouts and crosses her arms under her tits."
            me "Of course you are, but good girls can be good sluts too, right?"
            "She tilts her head and thinks about it."
            sis "I guess so, I hadn't thought about it."
            me "You should, it's a shame for such a beautiful body to go to waste."
            "The drug might start wearing off, better get her back in some clothes before she comes around."
            me "Okay Lily, you better get dressed in case mom comes back early."
            "Lily nods and steps back into her dress."
            sis "That was fun, we shouldn't have to worry about clothes as much as we do."
            $ sisO.change_slut_rebalanced(action_difficulty)
            $sisO.change_resist(sis_morning_event_object.get_resist_change(1))
            $ sis_morning_event_object.inc_level(1)

        "Have her get naked for you so you can masturbate.":
            $ action_difficulty = 15
            $sisO.set_action_exhib()
            me "Sis, you know that you're a really good looking woman, right?"
            "Lily nods, staring off into the distance."
            me "Well, I know that too. I spend a lot of my time at home just watching you, because you're so hot."
            me "Sometimes it's really hard to do other things, because of how distracting you are."
            sis "Oh, I didn't know. I'll make sure to cover up more for you."
            me "No, that's not what I meant. It would be a lot easier for everyone if I could get off while watching you sometimes, so I could focus on other things."
            if sisO.check_willing(action_difficulty):
                sis "Oh, that would work too I guess. So you just want to watch me then?"
                "You unzip your pants and slide your cock out."
                me "Ya, that's all. Just hang around the kitchen and do what you normally do."
                "You grab your cock and start rubbing."
                "Lily is watching you as you stroke yourself, but walks around the kitchen like she's looking for something."
                me "I could get myself off even faster if you were naked Lily."
                sis "You could? If it helps you finish faster..."
                "Lily shrugs the straps of her dress off her shoulders. She's not wearing a bra underneath, and has some cute pink panties on underneath."
                show sis strip2 at right #TODO, redo bend over with panties
                $ sisO.inc_naked()
                sis "Does this help?"
                "It does. You get even harder and start leaking pre-cum. You speed up your strokes and look at your sister's tits."
                me "Ya, a lot. You're doing a great job sis."
                "Lily smiles at the complement."
                sis "How about this?"
                "She walks in front of you and turns around, leaning over so her ass is pointed straight at you."
                show sis strip3 at right
                me "Oh wow, that's great."
                "Lily giggles. You continue to stroke yourself, and can feel your orgasm approaching."
                sis "You said I should be naked, right? I should get rid of this."
                "You keep jerking yourself off as Lily pulls her panties down to her ankles, then steps out of them."
                "She turns back to you and holds both her tits in her hands."
                show sis strip4 at right
                sis "Come on [inputName], I know you can cum for me."
                me "I'm going to, real soon."
                "Lily stares at your cock, and kneads her breasts in her hands."
                "You're ready to cum, and pump your cock as hard as you can. You aim your load towards Lily, and land your first shot on her lower leg. The rest splatters on the floor between you and her."
                sis "Wow, good job! I'm glad I could help you get rid of all that."
                me "Damn that felt good. I'm glad you could help me too."
                me "You should get dressed though, in case mom comes back early. I'll get this cleaned up."
                "Lily nods and gathers up her clothing."
                "You've definitely made a change in what she thinks is appropriate."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_morning_event_object.get_resist_change(2))
                $ sis_morning_event_object.inc_level(2)
            else:
                "Lily hesitates."
                sis "I don't think that's a good idea."
                "You unzip your pants and grab your cock."
                me "It'll be over soon, no big deal."
                sis "But what if mom came home, or the neighbours peeked in."
                me "They'd just see a caring sister taking care of her brother, right?"
                sis "I don't think that's what they would think."
                "Her eyes are watching your hand slide up and down your shaft."
                sis "No, I don't think I want to do this."
                "She begins leaving the room."
                me "Come on sis!"
                sis "Jerk off in your own room!"
                "Damn, you must have pushed her too far all at once. Maybe next time."
                $ sisO.change_slut_failed()
                $sisO.change_resist(sis_morning_event_object.get_resist_change(0))
                $ sis_morning_event_object.inc_level(0)

        "Have her blow you.":
            $ action_difficulty = 40
            $sisO.set_action_cumslut()
            $sisO.set_action_freeuse()
            me "Hey sis, just watching you around the house got me really hard. I need your help."
            sis "Me? What could I do?"
            me "I need you to give me a blowjob, so I'm not so hard when mom gets back."
            if sisO.check_willing(action_difficulty):
                "Lily hesitates, then nods."
                sis "Of course. It's my fault I got you hard anyway."
                me "It is. You have no idea how hot it is to see you and know you're a total slut."
                "Lily comes over to your chair and kneels down in front of it."
                if sisO.exhib:
                    sis "I know. I just love the way you look at me. I'll make sure to take care of you."
                    "She undoes your pants and pulls your cock out."
                    $ sisO.inc_blow()
                    show sis blow1 at right
                    "Lily licks along your shaft, then places the tip in her mouth. She moves it back and forth there for a while, not taking it any deeper."
                    me "That's a good girl. Take it nice and deep for me."
                    "You place a hand on the back of Lily's head and apply pressure. She resists for a moment, then starts moving and taking your cock down her throat."
                    me "There we go. Do you like having your brother's in your mouth?"
                    "Lily gargles something, but you can't hear what."
                    "You let up the pressure and let her head come back up to the top, then press her down slowly again. The third time you don't have to press to get her to keep taking you down her throat."
                    me "God, that feels so good!"
                else:
                    sis "I'm not a total slut. I just have some dirty thoughts sometimes."
                    "She undoes your pants and pulls your cock out."
                    me "Dirty thoughts like blowing your brother?"
                    show sis blow1 at right
                    $ sisO.inc_blow()
                    "Lily licks along your shaft, then places the tip in her mouth. She moves it back and forth there for a while, not taking it any deeper."
                    me "I think you're more of a slut than you know. You just need to accept it."
                    "You place a hand on the back of Lily's head and apply pressure. She resists for a moment, then starts moving and taking your cock down her throat."
                    me "That's right, that's a good girl."
                    "Lily gargles something, but you can't hear what."
                    "You let up the pressure and let her head come back up to the top, then press her down slowly again. The third time you don't have to press to get her to keep taking you down her throat."
                    me "See, it feels better when you just accept it."
                    "Lily nods as much as she can, and keeps sucking."
                "You reach a hand down and slip it underneath her dress and grab a tit. She's not wearing a bra, and her tit is heavy and soft."
                me "Keep going, you've almost got me there sis."
                "Lily speeds up slightly, and moans as you massage a breast."
                "A few minutes later you're ready to climax."
                me "Okay, when I'm ready I'm going to pull you back and cum on your face."
                "A muffled reply, which you assume is okay."
                $ sisO.inc_cum_over()
                "You wait as your orgasm builds up, then pull Lily back by the hair. Her mouth comes off of your cock with an audible pop, and she pants heavily for air as soon as she's free."
                "You stroke yourself with your other hand while holding Lily's head back and up, and begin cumming on your sister's face."
                "You land your first glob of cum in her panting mouth and she flinches, closing her mouth. You hold her steady while you blast a few more times over her eyes and cheeks, then press your tip onto her mouth."
                show sis blow2 at right
                me "Open up, slut."
                "She does, and you slide your cock slowly to the back of her throat, shivering as your tender cock is serviced."
                "Then you slide out again, and let go of her head. Lily sits back on her ass and coughs a few times, leaning to the side to spit."
                if sisO.exhib or sisO.cumslut:
                    sis "Wow, if feels so warm..."
                    me "You look like such a good little whore, covered in my cum like that."
                    "Lily smiles at you and nods."
                    sis "I'm glad you had a good time. It just feels so... right."
                    me "We'll make sure to do it again some time. You should get this cleaned up before mom gets home."
                else:
                    sis "You were a little rough with me."
                    me "Sorry, you were just being such as good little whore I couldn't hold back. It's really your fault that it happened like that."
                    "Lily looks sad, but nods."
                    sis "I'm sorry."
                    me "It's okay. You should get this cleaned up before mom gets home."
                "She nods again, and starts buttoning her clothes back on while you pull your pants up and head to the living room."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_morning_event_object.get_resist_change(3))
                $ sis_morning_event_object.inc_level(3)
            else:
                sis "A blowjob?"
                me "Ya. You know, use your mouth to make me cum."
                "Lily nods and moves over to you. She kneels down in front of you."
                sis "Like this?"
                me "Exactly. Now just take my penis out."
                sis "Ugh, but what if mom saw?"
                "Her hands move to your crotch anyway."
                me "She won't be back for a while, I promise."
                sis "Are you sure? I don't want to get caught."
                me "Positive."
                "Lily strokes you through your pants, but doesn't go any farther"
                sis "Maybe we should wait until later. Until we're all alone."
                me "We're alone right now, just the two of us."
                "Lily stops and stands up."
                sis "No, I don't think this is the right time."
                "She hurries away before you can say another word. You must have pushed her too far all at once and she resisted."
                $ sisO.change_slut_failed()
                $sisO.change_resist(sis_morning_event_object.get_resist_change(0))
                $ sis_morning_event_object.inc_level(0)

        "Fuck her on the counter.":
            $ action_difficulty = 65
            $sisO.set_action_freeuse()
            me "Sis, we've got some time before mom comes back, and you got me really horny."
            sis "I didn't do that, you did it to yourself."
            me "Nope. It was your hot ass and tits, bouncing all over the place. I know you're a huge slut, and I need you to take care of me."
            "Lily looks away from you, but doesn't move."
            me "Come on, bend over the counter slut!"
            if sisO.check_willing(action_difficulty):
                "Lily looks back."
                sis "I really got you that horny?"
                "You pull your pants down, revealing your rock hard cock."
                me "Yep, you did this all by yourself."
                "Lily takes a step towards the table."
                if sisO.freeuse:
                    sis "I'm so sorry. I think I can do something to make it up for you though."
                else:
                    sis "I'm sorry, I didn't mean to. I'll help if I can."
                    me "Of course you can help. Bend over the table and pull your dress up."
                "Lily nods and bends over, pulling her dress up past her ass."
                show sis fuck1 at right
                $ sisO.inc_sex()
                me "That's a good girl, presenting yourself for me."
                "You step and give her ass a solid smack."
                sis "Ow!"
                me "Shh, quiet down sis."
                "You smack her again, and this time she yelps loudly into an elbow."
                me "That's a good girl."
                "You grab her pink panties and pull them to the side, giving you access to her tight cunt."
                me "Are you horny now too?"
                if sisO.freeuse:
                    sis "Yeah, I am. Can you please help me out?"
                    me "I'm sure I can. Grab your cheeks and spread them for me."
                    "Lily nods and reaches back with both arms, pulling her ass cheeks to the side. You can see her pussy is dripping wet."
                else:
                    sis "No, of course not. I just want to help you."
                    me "Are you sure? Grab your cheeks and spread them for me."
                    "Lily hesitates, but reaches back with both arms and pulls her ass cheeks aside. You can see her pussy is dripping wet."
                    me "So you just got yourself dripping wet for me then? You're a bigger slut than I realised."
                "You rub your tip along her pussy, getting it wet from her. She shudders as you drag it past her clit."
                "Without warning you enter her, as deep as you can."
                sis "Ahh!"
                me "There you go whore, here's what you wanted."
                "Lily pants loudly as you slide in and out of her. She doesn't let go of her ass cheeks, and keeps them spread for you while you fuck her."
                "You reach forward and wrap a hand around Lily's neck, pulling her closer. You can feel her shuddering already, close to cumming herself."
                me "I knew you wanted it, you little slut. My own personal whore at home."
                "She shakes her head, but you can feel her pussy tighten when you say that. She's loving every minute and every word."
                "You tighten your grip on her neck, and she pushes her pussy hard on your shaft, moaning loudly."
                menu:
                    "Cum inside her.":
                        me "That's right, lean into it. I'm going to pump you full of cum."
                        "Lily breaks her silence."
                        if sisO.cumslut:
                            sis "Oh god, I'm your slut and I want you to pump me full of cum! I want you to try and get me pregnant!"
                        else:
                            sis "Oh god, I'm your slut and I want you to cum in me, I want your cum."
                        "Her legs spasm as you fuck her, stuck in constant orgasm."
                        "You build up to the edge, then grab her waist with both hands and pull her into your cock as you release."
                        "Lily screams and goes limp against the counter as you pump your cum inside of her."
                        "Finally, you finish and pull out. A line of cum sticks to the tip of your cock, connected to her pussy."
                        show sis fuck2 at right
                        $ sisO.inc_cum_inside()
                        "She quivers, and more cum begins dripping down her leg."
                        me "You should get yourself cleaned up when you can walk."
                        "Lily mumbles something, and you leave her bent over the counter dripping cum while you head to the living room."

                    "Cum on her.":
                        me "That's right, take it all. I'm going to cover you in cum."
                        "Lily quivers on your cock as you speak."
                        "She orgasms once, and her shaking pussy drives you to the edge."
                        "You pull out and plant your cock between her ass cheeks. Your load shoots across her back, landing on the back of her head. You then leave a stream of cum down her spine and onto her ass."
                        show sis fuck3 at right
                        $ sisO.inc_cum_over()
                        "You step back and admire your work. Lily's collapsed against the counter, cum on the back of her dress, her head, her ass cheeks, and dripping between the cheeks down her leg."
                        sis "Oh my god."
                        me "That was great sis. You should get yourself cleaned up before mom gets home and sees what you're really like."
                        "You walk off to the bathroom to get yourself cleaned up, leaving Lily where she is."

                    "Cum down her throat.":
                        me "Do you like that, slut? Like my cock?"
                        "Lily moans loudly as you fuck her, legs quivering wildly and pussy convulsing around your shaft."
                        me "When I'm ready I'm going to cum as deep down your throat as I can."
                        "Lily nods, neck still cradled in your hand and back arched."
                        "You pump a few more times, then pull out suddenly. Her pussy makes a popping sound as you pull out."
                        "Lily stumbles to the ground, turning as she goes. You grab her hair and set her head against the cabinets, then press your cock into her mouth."
                        "She moans as it slides across her tongue and down her throat. You move your hips back and forth a few times, fucking her mouth until you begin cumming."
                        "Lily's hands grab and scratch at your ass and thighs as you cum, and she moans loudly as you pump your load down her throat."
                        "You hold her there nice and long, then slide your sensitive cock back up her throat. You manage one extra pump of cum right before you leave her mouth, spraying it over her tongue."
                        show sis fuck4 at right
                        $ sisO.inc_cum_mouth()
                        $ sisO.inc_cum_swallow()
                        "Lily leans over coughing and trying to catch her breath."
                        me "That's a good girl, my sweet slutty sister."
                        me "You really helped me out."
                        "She nods but doesn't say anything, panting loudly."
                        me "You should get this cleaned up before mom gets home."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(sis_morning_event_object.get_resist_change(4))
                $ sis_morning_event_object.inc_level(4)
            else:
                sis "I keep telling you I'm not a slut!"
                "Lily crosses her arms and doesn't move."
                me "Oh come on, you know you want to. I'll fuck you quick and be done before anyone knows."
                "She shakes her head."
                sis "No, I'm not a slut, yours or otherwise! Go jerk off in your own room if you're that horny."
                "She turns around and storms down the hallway. Hopefully she won't remember what happened when the drug wears off, but you're sure you didn't effect her very much."
                $ sisO.change_slut_failed()
                $sisO.change_resist(sis_morning_event_object.get_resist_change(0))
                $ sis_morning_event_object.inc_level(0)

    "Mom gets back a little while later and doesn't say a word as she unloads the groceries into the fridge."
    jump morning

label maj_sis_shower:
    $ sis_bathroom_event_object.happened = True
    $ temp_slut_score = 0
    call serum_give(sisO) from _call_serum_give_20
    $ temp_slut_score = _return
    "You open up Lily's tube of toothpaste and pour the serum into the top, then squish it around gently to mix it in."
    "With that done you put it back under the counter and go about your own morning routine, leaving the door unlocked."
    show sis casual_night at right
    "Ten minutes later the bathroom door opens and your sister comes in."
    sis "Oh, sorry."
    me "No problem, I'm just trying to get my hair looking alright. You can use the sink if you need it."
    "You step to the side and make room for Lily. She comes into the room and closes the door, then moves to the sink and grabs her toothbrush."
    sis "Sure, thanks."
    "You keep busy with your hair while she squeezes out the toothpaste and starts to brush her teeth. You take a glance in the mirror at her and see her pupils dilating."
    me "Hey, do you swallow your toothpaste or spit it out?"
    "Lily tilts her head up to talk past the toothpaste."
    sis "Spit. Who swallows? That seems weird."
    me "It's not that weird. Give it a try."
    "Lily looks at you and cocks an eyebrow, but pauses for a moment and swallows her toothpaste."
    me "Good. How do you feel?"
    sis "Fine, I guess."
    "She nods slowly, pupils widening even further as the serum takes full effect."
    menu:
        "Stay in the room while she strips down.":
            $ action_difficulty = 0
            $sisO.set_action_exhib()
            $sisO.check_willing(action_difficulty)
            me "Anyways, I'm sure you have stuff to get done today Lily. You just do what you need to do, I'll stay out of your way."
            show sis showerstrip1 at right
            "Lily nods and turns back to the sink, rinsing out her mouth and then lets her hair down. She steps towards the shower, then hesitates for a moment."
            sis "I'm going to grab a shower..."
            "She looks at you expectantly, pausing with her hand on the top button of her shirt."
            me "That's fine, I don't mind. You just go ahead."
            show sis showerstrip2 at right
            "Lily thinks for a moment, then seems to make up her mind and starts to unbutton her shirt. She strips it off and drops it to the ground, then pulls her pants down too."
            show sis showerstrip3 at right
            "Next, she turns around and reachs back for the clasp on her bra, undoing it quickly and letting it fall onto the growing pile of clothes at her feet."
            "Finally she reaches for her panties, looping her thumbs through the waistband before she hesitates."
            show sis showerstrip4 at right
            "After a moments thought she leaves her underwear in place and grabs her towel from the rack beside her. She wraps it around herself, then reachs under it and pulls her panties down and off."
            "She steps into the shower, still in her towel, and looks at you."
            sis "Okay, I'm going to need the room now. I'll be done in a few minutes."
            "Not wanting to push her too far, you smile at her and nod."
            me "Alright, sure. Have a good shower."
            hide sis
            "You step out of the room and close the door. A second later you hear the lock click shut."
            $ sisO.inc_naked()
            $ sisO.change_slut_rebalanced(action_difficulty)
            $ sisO.change_resist(sis_bathroom_event_object.get_resist_change(1))
            $ sis_bathroom_event_object.inc_level(1)

        "Stay in the room while she has her shower.":
            $ action_difficulty = 15
            $sisO.set_action_exhib()
            me "Anyways, I'm sure you have stuff to get done today Lily. If you wanted to grab a shower or something, don't let me stop you. I don't mind."
            show sis showerstrip1 at right
            "Lily nods and turns back to the sink, rinsing out her mouth and then letting her hair down. She steps towards the shower, then hesitates for a moment."
            if sisO.check_willing(action_difficulty):
                #Success
                show sis showerstrip2 at right
                "After a moments hesitation she starts to undo her shirt, eventually pulling it off and dropping it to the floor. Next she pulls her pajama pants down and steps out of them."
                show sis showerstrip3 at right
                "She reaches back and undoes her bra, shrugging it forward then off as well. She looks back at you and smiles, then reaches for her panties."
                show sis showerstrip5 at right
                "With one smooth motion she slips them down and off, kicking them onto the growing pile of clothes. Then Lily opens up the shower door and steps in, turning on the water and getting wet."
                "You stand at the counter, glancing sideways to watch your sister as she washes herself in the shower. She grabs the bar of soap and begins to run it up and down her body."
                "After a few minutes she looks directly at you, raising her voice a little to be heard over the rushing water."
                sis "You can look you know, I don't mind."
                me "No?"
                show sis showerstrip6 at right
                "She shakes her head and spins around, pointing her ass towards you. You turn and lean on the counter, gazing at your sister as she plays with the water a little."
                me "Wow, you're looking great."
                sis "Thanks. Can you pass me the conditioner? Mom must have moved it."
                "You check under the counter and find the bottle, then walk over to the shower and hand it to Lily."
                sis "Perfect."
                "She squirts some into her hand and combs it through her hair, waits a few minutes, then starts to rinse it off. You spend the next few minutes watching the water as it runs down Lily's body."
                show sis showerstrip7 at right
                "Finally she turns off the water and reaches for her towel, wrapping it around herself."
                sis "Alright, it's all yours now. See you later."
                hide sis
                "Lily gathers up her clothes and heads back to her room, leaving you alone in the bathroom."
                "You get into the shower yourself and jerk your still hard cock off to the memories of your sister's body."
                "When you're done you head back to your own room, with plenty of time left in the morning."
                $ sisO.inc_naked()
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ sisO.change_resist(sis_bathroom_event_object.get_resist_change(2))
                $ sis_bathroom_event_object.inc_level(2)
            else:
                #Failure
                sis "Actualy, uh..."
                me "Seriously Lily, just go for it. I won't care."
                "She plays with the top button of her shirt, eventually undoing it and moving down to the next."
                sis "No, how about I just wait until your done."
                me "Come on, you're being silly."
                "She shakes her head and heads to the door, opening it."
                sis "Just come get me when you're done, okay?"
                "You must have pushed her too far, and she's resisted the serum."
                me "Fine, I'll try to be quick."
                "Lily leaves, and you grab a short shower by yourself. You feel like you could have accomplished more here if you weren't so aggressive."
                $ sisO.change_slut_failed()
                $ sisO.change_resist(sis_bathroom_event_object.get_resist_change(0))
                $ sis_bathroom_event_object.inc_level(0)

        "Get a handjob while she showers.":
            $ action_difficulty = 30
            $sisO.set_action_exhib()
            $sisO.set_action_cumslut()
            me "Hey, were you going to grab a shower?"
            sis "Uh, ya, why?"
            show sis showerstrip1 at right
            "Lily turns to the sink and washes her mouth out. When she turns back she starts to let her hair down."
            me "I was going to too. Think we could share one to save some time?"
            "Lily takes a moment before she answers."
            if sisO.check_willing(action_difficulty):
                #Success
                sis "I guess that makes sense. We can take turns under the shower head. You better not just hog it all."
                me "I promise I'll share."
                show sis shower at right
                "Lily strips off her clothes and steps into the glass shower enclosure, stepping to one side to make room for you."
                "You pull your shirt off, then drop your pants and underwear and step into the shower with your sister. It doesn't take long for Lily to notice that your cock is already hard."
                sis "Uh, wow."
                "You reach past her and turn the water on, taking a moment to make sure it's not too hot or too cold for the both of you."
                me "Ya, I just got up and I guess I've got some morning wood."
                "You start to get wet under the shower, turning slowly so your cock brushes up against Lily's leg. You feel her shiver as you touch her."
                me "Actually, it would be great if you took care of that for me. Just put your hand on it."
                show sis showerhand1 at right
                "You take Lily's hand in yours and press it up against your cock. She hesitates a moment, then wraps her hand around your shaft and starts to slide it up and down a bit at a time."
                sis "Like this?"
                me "Just like that, perfect."
                "After a little while Lily gains confidence and speeds up, stroking your cock as you both stand under the shower. You watch as the water runs in little rivulets over her shoulders and between her breasts."
                sis "Would it feel better if we got it a little slippery?"
                me "I think it would."
                "Lily pauses for a moment and reaches for the shampoo bottle on a small rack in the shower. She guides you forwards a little so you're out of the water, then squirts some shampoo on her hand and wraps it around your cock again."
                "Her hand is warm and slippery when she starts to jerk you off this time, and she runs it up and down your length quickly."
                me "Oh god Lily, I'm almost there."
                "Lily puts her arm around you and pulls you close, pressing her tits against your chest while she strokes you off just beside her waist."
                "You reach around and grab her ass, squeezing her cheeks as you start to cum."
                me "Ah fuck."
                show sis shower at right
                "Lily gasps softly as you start to unload, shooting your cum onto the shower floor. She gives you a few more strokes to make sure you're done, then lets go and steps back."
                sis "How was that?"
                me "Perfect. Ah, wow."
                show sis showerstrip7 at right
                "She smiles and steps out of the shower, grabbing her towel on the way."
                sis "I think I'm all done anyway, you take as long as you need."
                hide sis
                "You watch as Lily gathers up her clothes and slips out of the bathroom. As you finish your own shower you feel like you've had a major effect on her right now."
                $ sisO.inc_hand()
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ sisO.change_resist(sis_bathroom_event_object.get_resist_change(3))
                $ sis_bathroom_event_object.inc_level(3)
            else:
                #Failure
                sis "Ah, I'm not so sure about that. If you're in a hurry I can just wait until you're done."
                me "Oh come on, it's not a big deal. Just a quick shower then we're both on our way."
                "Lily steps over towards the glass door of the shower, playing with the top button of her shirt. Finally she shakes her head and looks you square in the eye."
                sis "No, I think I'll just wait if it's that important."
                "She moves over to the door and opens it up. You must have pushed her too far, and she's resisted the serum."
                sis "Tell me when you're done, okay?"
                me "Fine, I'll try to be quick then."
                "Lily leaves, and you grab a short shower by yourself. You feel like you could have accomplished more here if you weren't so aggressive."
                $ sisO.change_slut_failed()
                $ sisO.change_resist(sis_bathroom_event_object.get_resist_change(0))
                $ sis_bathroom_event_object.inc_level(0)

        "Get a blowjob while she showers.":
            $ action_difficulty = 45
            $sisO.set_action_cumslut()
            $sisO.set_action_freeuse()
            me "Hey, were you going to grab a shower?"
            sis "Uh, ya, why?"
            show sis showerstrip1 at right
            "Lily turns to the sink and washes her mouth out. When she turns back she starts to let her hair down."
            me "Well, I just got up and I've got some morning wood. I figured if we're both going to grab a shower anyway, you could do me a favour and take care of it."
            "Lily steps back and looks at your crotch. To demonstrate your point you undo your pants and pull your hard cock out to show her."
            if sisO.check_willing(action_difficulty):
                #Success
                sis "Wow. Uh, sure I guess. Here, lets get the shower started first."
                show sis shower at right
                "You and Lily peel off all your clothes, then she gets the water going and adjusts the temperature. Once it's ready you both step into the glass enclosure and Lily turns to look at you."
                me "Ya, I'm definitely going to need your help here Lily."
                show sis showerhand1 at right
                "She nods and wraps her hand around your cock, stroking slowly."
                sis "How's this?"
                me "Mmm, that feels good but I think I'm going to need a little bit more."
                sis "Like what?"
                me "Get on your knees for me."
                show sis showerhead1 at right
                "Your sister hesitates, then nods and drops to her knees in front of you. She looks up at you, your cock level with her face."
                "You hold onto your shaft and tap your tip against your sister's face. She flinches a little, but doesn't say anything."
                me "Good, now open up your mouth."
                show sis showerhead2 at right
                "Lily does what you ask, opening up her mouth. You place the tip of your cock on her lips then move your hips a little to slide in and out of her mouth."
                me "Ah, fucking great. Now you take over, I'm sure a slut like you knows how to suck a cock."
                "She nods and starts to bob her head back and forth along your shaft, licking along the bottom."
                "You relax and enjoy the feeling of the warm water running over your body alongside your sister's warm mouth around your dick."
                "A bit at a time Lily starts to speed up, blowing you faster and deeper with each pass."
                me "There we go, that's what I like. See how deep you can get for me."
                "Lily nods, braces herself for a moment, then presses herself down onto your cock. You feel her nose bump your stomach, and she shivers slightly as you tap the back of her throat with your tip."
                me "Damn, you're just such a good cock gobbler. Just stay like that."
                "She stays down on your shaft for a few long seconds, throat spasming lightly around you, then pulls off and takes a deep breath."
                sis "Fuck... I!"
                show sis showerhead3 at right
                "You cut her off and push yourself back into her mouth, working your hips to slide yourself in and out."
                me "I'm almost there, don't stop!"
                "Lily nods and takes over again, blowing you fast and deep."
                menu:
                    "Cum down her throat.":
                        me "Oh ya, here we go!"
                        show sis showerhead4 at right
                        "You place a hand on the back of Lily's head as you start to cum and hold her in place as you thrust forward, ramming your full length down her throat."
                        "Lily shakes under your hand and coughs a few times as you start to cum right into her stomach. Her spasming throat feels amazing around your sensitive shaft, and you stay there a few extra seconds to enjoy it."
                        "Finally you pull back, leaving her mouth with a wet pop. She take a sudden gasp of air, then looks up at you."
                        if sisO.cumslut:
                            sis "Did that do it? Let me make sure I've got it all."
                            "She leans forward and runs her tongue along the sides and bottom of your sensitive shaft, cleaning up every last trace of cum she can find."
                            me "I think you got it all Lily, you did a great job."
                        else:
                            sis "Did that take care of it?"
                            me "Ya, you did a great job."
                        "Lily smiles and takes a few deep breaths, then stands up beside you."
                        sis "Well, I think I'm all done here then. You take as long as you want."
                        show sis showerstrip1 at right
                        "She steps out of the shower and grabs her towel. As you watch her gather her clothes you feel like you've had a major effect on her."
                        $ sisO.inc_cum_mouth()
                        $ sisO.inc_cum_swallow()
                    "Cum on her face.":
                        me "Oh ya, here we go!"
                        "You wait until the last moment, then pull back out of Lily's mouth and stroke yourself off as you cum."
                        show sis showerhead5 at right
                        "Lily sits back and looks at you as cover her face with your semen. When you're done you let your cock flop onto her face, moving it slowly to spread your seed around."
                        "She smiles and waits until you're done, then turns her face towards the shower head and starts to get cleaned up."
                        if sisO.cumslut:
                            sis "Mmm, it's such a shame to wash this all off so soon. I hope I took care of everything ofr you."
                        else:
                            sis "I hope that took care of it then."
                        me "Ya, you did a great job. Fuck you look good with cum on your face."
                        sis "I definitely think I'm going to need a few more minutes in here now."
                        me "Well I think I'm done. See you around."
                        hide sis
                        "You step out of the shower, grab a towel, and collect your clothes. As you leave Lily to finish cleaning your cum off you feel like you've had a major effect on her."
                        $ sisO.inc_cum_over()

                $ sisO.inc_blow()
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ sisO.change_resist(sis_bathroom_event_object.get_resist_change(4))
                $ sis_bathroom_event_object.inc_level(4)
            else:
                #Failure
                sis "Oh, wow."
                me "Ya. I thought you could just wrap your lips around it and suck me off, it wouldn't take too long."
                "Lily plays with the top button of her shirt, undoing and redoing it a few times before she comes to a decision."
                sis "Ah, I don't think so. I'm not really in a hurry, so you take as long as you need in here to take care of... that."
                me "Come on, it's not that big of a deal Lily."
                "She shakes her head and moves to the door. You do up your pants quickly as she opens it and steps into the hall."
                "You must have pushed her too far, and she's resisted the serum."
                sis "Let me know when you're done, okay?"
                me "Fine, I may be a little bit then."
                "Lily nods and leaves. You grab a short shower by yourself, plagued by the feeling that you could have accomplished more here if you weren't so aggressive."
                $ sisO.change_slut_failed()
                $ sisO.change_resist(sis_bathroom_event_object.get_resist_change(0))
                $ sis_bathroom_event_object.inc_level(0)

        "Fuck her in the shower.":
            $ action_difficulty = 60
            $sisO.set_action_freeuse()
            me "Hey, you were going to grab a shower, right?"
            sis "Ya, why?"
            show sis showerstrip1 at right
            "You step back and pull your pants down, revealing your hard cock to your sister as she lets her hair down."
            me "I've got some morning wood, and thought you might have somewhere for me to put it."
            if sisO.check_willing(action_difficulty):
                #Success
                "Lily takes a step back and looks at your erect penis for a moment."
                sis "Ya, I think I have somewhere you can put that. Lets get into the shower first though."
                show sis shower at right
                "You and your sister strip down and get into the shower, pausing for a moment to let the water get to a comfortable temperature."
                "Once you're inside the glass enclosed shower you face your sister, pressing your body against hers and letting your cock brush against her waist."
                me "Turn around for me."
                show sis showerfuck1 at right
                "Lily nods and turns around, pointing her ass towards you."
                "You bounce your cock off her wet ass cheeks a few times, then slip it down and run it against her pussy. Lily moans softly and arches her back, pressing her hips towards you."
                me "Wow, it really looks like you want it."
                "Lily nods and moans softly as you press your tip against her lips, almost slipping it in."
                me "Come on, say it."
                if sisO.freeuse:
                    sis "Ah, I'm a dirty little slut who wants your cock deep inside me!"
                    "You let the tip of your cock slip just a little farther in, then pull back out again."
                    sis "Oh god, just please fuck me!"
                else:
                    sis "What?"
                    me "Tell me you want it. Tell me what a dirty whore you are."
                    "You let the tip of your cock slip just a little farther in, then pull back out again."
                    sis "Ah! Fine, I'm a dirty little slut who wants your cock deep inside me. Please, just fuck me already!"
                show sis showerfuck2 at right
                "Satisfied, you hold onto Lily's hips and thrust yourself forward. She's already dripping wet, and the water from the shower hasn't done much to wash that away. You're able to glide all the way to the back of her cunt in a single thrust."
                sis "Oh fuck!"
                "You waste no time and lay into your sister from behind, holding onto her hips and thrusting back and forth rapidly. Her cries quickly devolve into a string of gasps and moans as you fuck her against the glass wall of the shower."
                me "You seem like you're having a great time. Are you going to cum soon?"
                sis "Ah! Uh huh!"
                me "Good, a good little slut like you deserves to have a good time."
                show sis showerfuck3 at right
                "You lean down and wrap an arm around Lily's leg, lifting it up so you can spread her legs apart and get even deeper. Lily gasps non-stop as you fuck her, with her tits sliding up and down on the glass with each thrust."
                "A few moments later you feel Lily's body shake as she gives one long moan. Her pussy tightens up around your dick as she climaxes, and it pulls you over the edge too."
                menu:
                    "Cum inside of her.":
                        "You keep thrusting until you start to cum, then you lean forward and push as deep as you can into Lily's tight cunt as you begin firing your load inside of her."
                        "Lily's moans die off slowly as you pump your seed deep inside of her. When you're finished you lower her leg and slide out of her."
                        show sis showerfuck4 at right
                        "Your sister pants loudly as the water from the shower runs over both of you. She slides to the floor and turns over looking up at you as your cum leaks out of her slit and is washed away."
                        if sisO.cumslut:
                            sis "Holy fuck, you filled me up so nicely. Thank you so much..."
                        else:
                            sis "Holy fuck."
                        me "Fuck, that was great. Here, you need to clean this off."
                        show sis showerfuck6 at right
                        if sisO.cumslut:
                            "You press your cock against her mouth, and she eagerly starts to lick the shaft clean. Her tongue sends shivers down your spine as it gathers up any trace of semen left on you."
                        else:
                            "You press your cock against her mouth, and after a moment she opens up and starts to lick your shaft clean. Her tongue sends shivers down your spine as it plays over your newly sensitive shaft."
                        "After a few more moments you pull out and step out of the shower."
                        me "Alright, I think I'm done here. You should get yourself cleaned up."
                        "Lily nods and stands up, her legs shaking slightly. As you collect your clothes and head to your room, you feel like you've had a [sisO.effect_string] impact on her."
                        $ sisO.inc_cum_inside()

                    "Cum all over her.":
                        me "Fuck, here I cum!"
                        "You give Lily's pussy a few more thrusts, then pull out and step back. Without your support Lily slumps to the ground, panting loudly."
                        me "Look here, get ready!"
                        show sis showerfuck5 at right
                        "You stroke yourself off as Lily rolls over and looks up at you. You unload all over her body, starting with her face and working your way down to her waist."
                        "By the time you're done the water has already begun to wash away your cum where you started."
                        sis "Holy fuck."
                        if sisO.cumslut:
                            "You press your cock against her mouth, and she eagerly starts to lick the shaft clean. Her tongue sends shivers down your spine as it gathers up any trace of semen left on you."
                        else:
                            "You press your cock against her mouth, and after a moment she opens up and starts to lick your shaft clean. Her tongue sends shivers down your spine as it plays over your newly sensitive shaft."
                        show sis showerfuck7 at right
                        "You press your cock against her mouth, and after a moment she opens up and starts to lick your shaft clean. Her tongue sends shivers down your spine as it plays over your newly sensitive shaft."
                        "After a few more moments you pull out and step out of the shower."
                        me "Alright, I think I'm done here. You should get yourself cleaned up."
                        "Lily nods and stands up, her legs shaking slightly. As you collect your clothes and head to your room, you feel like you've had a [sisO.effect_string] impact on her."
                        $ sisO.inc_cum_over()
                $ sisO.inc_sex()
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ sisO.change_resist(sis_bathroom_event_object.get_resist_change(5))
                $ sis_bathroom_event_object.inc_level(5)
            else:
                #Failure
                "Lily takes a step back and looks at your erect penis, stunned for a moment. Finally she speaks up."
                sis "Uh, I don't think so. Not today."
                me "Come on, just a few minutes. I promise you'll have a great time too."
                "Lily plays with the top button on her shirt, undoing and redoing it a few times. Finally she shakes her head and looks you square in the eye."
                sis "I said no. Now get out, I want to have a shower. Alone."
                "She's got a sharp look in her eye now, and her voice is steady and determined. You must have pushed her too far and she's resisted the serum. Pushing her any farther would be dangerous."
                me "Fine, fine. Just let me know when you're done, okay?"
                "Lily nods, and you retreat from the bathroom. Lily locks the door behind you, and you return to your room confident you could have accomplished more if you weren't so aggressive."
                $ sisO.change_slut_failed()
                $ sisO.change_resist(sis_bathroom_event_object.get_resist_change(0))
                $ sis_bathroom_event_object.inc_level(0)
    jump jumpTimeStay

label maj_sis_beach:
    $ sis_beach_event_object.happened = True
    $temp_slut_score = 0
    call serum_give(sisO) from _call_serum_give_22
    $ temp_slut_score = _return
    "You pull out some serum and mix it into Lily's drink before catching up with her at the picnic tables."
    sis "Thanks [inputName], I think I really needed this!"
    me "Me too. I'm starving!"
    "The two of you dig in. You wait a few minutes until Lily's had most of her drink."
    me "Hey Lily, I think I forgot something up by the change rooms earlier today. Would you mind comming with me while I check?"
    "Lily looks at you and nods slowly."
    sis "Okay."
    "You lead Lily to the change rooms, finding them mostly empty at this time of day. You pick the stall farthest away from the parking lot and open up the curtain to it."
    me "Hmm, I guess I was wrong. While we've got a moment up here, there's something else I wanted to do."
    sis "What's that?"
    #Move up to the changing rooms.
    menu:
        "Have her flash you her tits.":
            $ action_difficulty = 0
            $sisO.set_action_exhib()
            $sisO.check_willing(action_difficulty)
            me "I've been watching you in that swimsuit all day, and it's driving me a little wild. I was hoping you could just pull your top off and give me a look at your boobs."
            if sisO.exhib:
                "Lily barely even thinks about it before she pulls up her top and lets her tits fall free."
                sis "Are these what you wanted to see?"
                show sis strip22 at right
                "She shakes her shoulders back and forth, jiggling her tits for you. You notice her nipples getting hard as you watch her."
                me "Yeah, just like that. You look great Lily."
                "She smiles and cups her tits, squeezing them together."
                sis "Thank you. Let me know when you've seen enough."
                "You enjoy the view for a few more seconds, until you see another couple heading your way from the beach."
                me "Okay Lily, that will be enough for now."
                show sis swim2 at right
                "She pulls her top back down, shaking her tits again to get them into place."
            else:
                "Lily thinks about it for a brief moment, then nods and steps into the stall. She motions for you to follow, and closes the curtain behind her."
                if slut_outfit:
                    show sis strip22 at right
                else:
                    show sis strip21 at right
                "Once you're in the privacy of the changing room Lily pulls up her top, letting her tits fall free."
                sis "Are these what you wanted to see?"
                "She shakes her shoulders back and forth, jiggling her tits for you. You notice her nipples getting hard as you watch her."
                me "Yeah, just like that. You look great Lily."
                "She smiles and cups her tits, squeezing them together."
                sis "Thank you. Let me know when you've seen enough."
                "You enjoy the view for a minute or two, watching your sisters breasts bounce as she plays with them."
                me "Okay Lily, that will be enough for now."
                if slut_outfit:
                    show sis swim2 at right
                else:
                    show sis swim1 at right
                "She pulls her top back down, shaking her tits one last time to get them into place."

            me "Lets head back to the bench and relax for a little while."
            "You and Lily return to your seats. The serum wears off completely over the next half hour."
            $ sisO.inc_naked()
            $ sisO.change_slut_rebalanced(action_difficulty)
            $ sisO.change_resist(sis_beach_event_object.get_resist_change(1))
            $ sis_beach_event_object.inc_level(1)


        "Have her get naked for you.":
            $ action_difficulty = 15
            $sisO.set_action_exhib()
            me "I've been watching you in that swimsuit all day, and it's been driving me wild. I want you to come in here and take it off for me so I can get a good look at you."
            if sisO.check_willing(action_difficulty):
                "Lily barely even thinks about it before stepping into the changeing room. You follow her in and close the curtain behind the two of you."
                sis "So, you want to see me naked then?"
                if slut_outfit:
                    show sis strip24 at right
                else:
                    show sis strip23 at right
                "She reaches behind her neck and undoes the top of her bikini, letting it fall forward first before pulling it off completely."
                me "Yeah, I do. You look amazing Lily."
                sis "Thank you. I guess I need to take these off too..."
                show sis strip25 at right
                $ sisO.inc_naked()
                "She pulls the knots on either side of her bikini bottom, letting it fall to the floor as it comes undone. In the small changing room, she's almost pressed up against you."
                sis "There you go [inputName]. Anything else?"
                me "Turn around for me, so I can take a look at you from behind."
                show sis strip26 at right
                "She nods and turns around, planting her hands on the wooden sides of the shack and bending over as much as she can in the small space."
                "You place a hand on her ass and give it a good squeeze, making Lily yelp."
                sis "Hey! Easy back there."
                me "Sorry. Just couldn't resist."
                "You give her butt another squeeze, then let go entirely."
                me "Thank you Lily, that was exactly what I wanted."
                show sis strip25 at right
                "She turns back to you and picks up her bikini."
                sis "Good. Give me a moment to get dressed, please."
                if slut_outfit:
                    show sis swim2 at right
                else:
                    show sis swim1 at right
                "You step out of the change room and wait until Lily has her outfit put back together. Once that's done, you head back to your seats at the picnic bench and hang out until the serum has worn off completely."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ sisO.change_resist(sis_beach_event_object.get_resist_change(2))
                $ sis_beach_event_object.inc_level(2)


            else:
                "Lily thinks about it for a long moment, taking a slow step towards the changing stall."
                sis "You want me to take it all off? So you can see my..."
                "She trails off, obviously unsure."
                me "That's right. I want to get a good look at my hot little sister."
                sis "I'm not sure..."
                me "It's no big deal Lily. Come on, a quick peek and then we can head back to the table."
                "She's quiet for another few seconds, then takes a step back and shakes her head."
                sis "I don't think I'm comfortable with that [inputName]. If you can't find whatever you're looking for can we please just go?"
                "She's got a sharper look in her eye now; she must have resisted the serum. Pushing her any farther now would do more harm than good."
                me "Alright. Sorry Lily, lets go get back to our seats."
                "You and Lily return to the picnic table, where you wait until the serum wears off completely."
                $ sisO.change_slut_failed()
                $ sisO.change_resist(sis_beach_event_object.get_resist_change(0))
                $ sis_beach_event_object.inc_level(0)

        "Have her titfuck you.":
            $ action_difficulty = 30
            $sisO.set_action_cumslut()
            $sisO.set_action_freeuse()
            me "I've been watching you in that swimsuit all day, and I've just wanted slip my dick between those perky tits of yours. Would you like to help me out with that?"
            if sisO.check_willing(action_difficulty):
                "Lily thinks about it for a brief moment, then nods and steps past you into the stall. You follow her in, and close the curtain behind you."
                sis "I guess you can just lean against the wall and let me take care of you."
                "You pull your swimsuit down, letting your hard cock spring free. Lily watches it bounce for a moment, then drops to her knees in front of you."
                me "Here you go Lily, go to town."
                if slut_outfit:
                    show sis tit12 at right
                else:
                    show sis tit11 at right
                $ sisO.inc_tit()
                "You lean back while Lily takes her breasts up in her hands. She pulls them up and slips the tip of your dick between, then lets them down so you slide between her clevage."
                "Lily pushes her tits together, sandwiching your cock, and starts to slide them together. Her bikini top stops you from sliding out the front as she goes."
                me "Ah, that feels great Lily. Keep going just like that."
                "She nods and continues, rubbing her soft breasts up and down along your shaft. Soon your precum has gotten her cleavage nice and slippery as well."
                sis "Let me know when you're going to cum, okay?"
                me "Sure. It won't be long now."
                "She speeds up, panting softly from the exertion. Her smooth, steady strokes drive you closer and closer to climaxing."
                menu:
                    "Warn her before you cum.":
                        me "Fuck, I'm almost there."
                        "Lily looks up at you and speeds up even more."
                        sis "Just let it all out between my tits, okay [inputName]?"
                        if slut_outfit:
                            show sis tit14 at right
                        else:
                            show sis tit13 at right
                        $ sisO.inc_cum_over()
                        "You nod and tense up as you start to cum. Lily gasps softly as you spray your load onto the top of her chest, the last few drops dribbling down between her cleavage."
                        "When you're done you slip free of her tits and step back."
                        sis "Thanks for giving me a warning."

                    "Don't warn her before you cum.":
                        "You stay quiet as your orgasm approaches, enjoying your sisters tits. She speeds up even more as you tense up and start to cum."
                        if slut_outfit:
                            show sis tit14 at right
                        else:
                            show sis tit13 at right
                        $ sisO.inc_cum_over()
                        "Lily shouts in suprise as you start to spray your load onto her chest. She tries to pull back, but your cock ends up caught on her bikini until you've finished anyway."
                        sis "Hey! Fuck!"
                        "You finally slip free of her tits and step back. Your sperm drips down the slope of her breasts and between her cleavage."
                        sis "I told you to warn me!"
                        me "Sorry, I guess it snuck up on me."
                        "She looks down at your semen and sighs."
                        sis "Whatever. I was going to let you do that anyways."
                "She catches a few drips of cum with a finger as they run out from the bottom of her cleavage."
                me "I think there are some showers outside if you want to get cleaned up." #TODO: For cumslut tag just have her walk around like this.
                if slut_outfit:
                    show sis swim2 at right
                else:
                    show sis swim1 at right
                "Lily gets onto her feet and nods. You leave the changing room and head over to the showers. Once she's washed your sperm off of her chest, the two of you head back to your picnic bench and relax until the serum has worn off completely."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ sisO.change_resist(sis_beach_event_object.get_resist_change(3))
                $ sis_beach_event_object.inc_level(3)

            else:
                "Lily thinks about it for a long moment, taking a slow step towards the changing stall."
                sis "You want me to use my boobs to get you off?"
                me "That's right. That bikini makes them look so good, I can't take my eyes off of them."
                sis "I'm not sure..."
                me "It's no big deal Lily. Come on, a quick titfuck, then we can head back to the beach."
                "She's quiet for another few seconds, then takes a step back and shakes her head."
                sis "No, I don't think so [inputName]. You'll just have to control yourself until you get home and can jerk off or something."
                "She's got a sharper look in her eye now; she must have resisted the serum. Pushing her any farther now would do more harm than good."
                me "Alright. Sorry Lily, lets go back to our seats."
                "You and Lily return to the picnic table, where you wait until the serum wears off completely."
                $ sisO.change_slut_failed()
                $ sisO.change_resist(sis_beach_event_object.get_resist_change(0))
                $ sis_beach_event_object.inc_level(0)


        "Have her blow you.":
            $ action_difficulty = 45
            $sisO.set_action_cumslut()
            $sisO.set_action_freeuse()
            me "I've been watching you in that swimsuit all day, and keep thinking about how good you would look on your knees in it. Lets step in here for a few minutes so you can suck me off."
            if sisO.check_willing(action_difficulty):
                "Lily thinks about it for a brief moment, then nods and steps past you into the stall. You follow her in, and close the curtain behind you."
                sis "You just lean against the wall and leave everything to me."
                "Your sister drops to her knees in front of you, pulling your swimsuit down low enough to let your hard cock spring free."
                "She watches it bounce for a moment, then leans forward and kisses it. Lily swirls her tounge around the tip, then turns her head and runs it down the side of your shaft."
                me "That's it, get it all wet first."
                if slut_outfit:
                    show sis blow26 at right
                else:
                    show sis blow25 at right
                $ sisO.inc_blow()
                "She changes side and licks that side, then moves lower and licks up from your balls to the tip again. When she reaches the top she opens her mouth and slides you inside, starting off with a few shallow thrusts."
                "Lily's mouth is warm and wet as she blows you, going a little bit deeper with each pass."
                me "Come on, you can go deeper than that Lily."
                "You place your hand on the back of her head and guide her, putting a little more pressure each time she slides your cock down her throat."
                if slut_outfit:
                    show sis blow28 at right
                else:
                    show sis blow27 at right
                "Soon you've got her taking the full length of your cock, the tip rubbing against the back of her mouth each time she bobs her head forward."
                me "Fuck, that feels amazing Lily. You're going to have me cumming soon."
                "Your sister pulls off for air, taking a few deeps breaths before looking up at you again."
                sis "I don't have anything to get cleaned up with here. Just cum in my mouth, okay?"
                me "Sure. Come on, I'm almost there."
                "You guide her gently back to your dick, and she resumes blowing you. Soon you feel your orgasm building as she throats you."
                me "Here I come, get ready!"
                "Lily moans something and slides her head back, leaving your tip just inside her lips. She grabs your shaft with one hand and strokes you off, giving a muffled gasp as you fire your first pulse of cum onto her tongue."
                me "That's it, take it all you little cum slut!"
                "After a few seconds you've finished filling your little sisters mouth up with semen. She lets go of your shaft and slides your tip away from her lips."
                me "Open up for me, please."
                if slut_outfit:
                    show sis blow30 at right
                else:
                    show sis blow29 at right
                $ sisO.inc_cum_mouth()
                "Lily rolls her eyes, then opens her mouth to show off the pools of cum you just put there."
                me "God that's so hot."
                "Lily leans to the side and lets it all flow out into the sand. She spits out the last few drops at the end, then runs the back of her hand over her mouth."
                if sisO.cumslut:
                    sis "All done. You tasted amazing [inputName]."
                else:
                    sis "There, all done."
                me "Thank you Lily, that was just what I needed. Lets head back to the table."
                if slut_outfit:
                    show sis swim2 at right
                else:
                    show sis swim1 at right
                "She gets up off her knees and follows you out of the changing room. You hang out together at the picnic table until the serum wears off completely."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ sisO.change_resist(sis_beach_event_object.get_resist_change(4))
                $ sis_beach_event_object.inc_level(4)

            else:
                "Lily thinks about it for a long moment, taking a slow step towards the changing stall."
                sis "You want me to give you a blowjob? Here?"
                me "That's right. Something nice to finish the day off with."
                sis "I'm not sure..."
                me "It's no big deal Lily. A quick blowjob, then we can head back to the beach."
                "She's quiet for another few seconds, then takes a step back and shakes her head."
                sis "No, I don't think so [inputName]. You just go in there and jerk yourself off or something, I'm going to head back to the table."
                "She's got a sharper look in her eye now; she must have resisted the serum. Pushing her any farther now would do more harm than good."
                me "Alright, I'm sorry. Just forget I said anything at all, and lets get back to the table."
                "You and Lily return to the picnic table, where you wait until the serum wears off completely."
                $ sisO.change_slut_failed()
                $ sisO.change_resist(sis_beach_event_object.get_resist_change(0))
                $ sis_beach_event_object.inc_level(0)

        "Fuck her.":
            $ action_difficulty = 60
            $sisO.set_action_freeuse()
            me "I've been watching you in that swimsuit all day, wanting to rip it off of you. Lets just slip in here and have a quick fuck."
            if sisO.check_willing(action_difficulty):
                if slut_outfit:
                    show sis fuck43 at right
                else:
                    show sis fuck42 at right
                "Lily thinks about it for a brief moment, then steps past you into the stall. By the time you've stepped in after her and closed the curtain she's leaning against the far wall, wiggling her ass at you."
                sis "I'm so sorry, I didn't realise I was teasing you so badly."
                "You step behind her and pull your swimsuit down, bouncing your hard cock against one of her ass cheeks."
                me "Well you were, and I'm going to need to take care of this now."
                "You give her ass a smack, and she moans in response."
                sis "Whatever you have to do [inputName]..."
                "You squeeze Lily's ass a few times, letting your cock rest between her cheeks. After that you lean forward and cup her breasts, sliding your hands under her bikini top."
                "Lily rocks her hips against yours, grinding against your dick while you play with her tits."
                me "Turn around for me, I want to fuck you up against the wall."
                "Lily stands up and turns around. You pull her top up and play with her breasts some more, enjoying the way her nipples harden as you do."
                "Next you reach down and pull the bottom to the side, running a pair of fingers over her pussy. She gasps as you touch her, her cunt already dripping wet."
                sis "Oh [inputName]... Ah..."
                me "Here, lets give you what you want."
                if slut_outfit:
                    show sis fuck45 at right
                else:
                    show sis fuck44 at right
                $ sisO.inc_sex()
                "You lift up one of her legs and step forward, pinning her between the thin wooden wall of the changing room and your body. The tip of your penis brushes against her slit, making her moan again."
                sis "Please, please give it to me."
                "You reach a hand down and line yourself up, then thrust forward slowly. Lily shivers against your body as you slide your cock as deep as you can into her."
                me "There we go. You're so wet Lily, I can tell you need it."
                "She nods and mumbles something, interupted by a yelp as you start to pump in and out of her."
                me "What was that?"
                sis "Ah! I... I need your cock so badly!"
                me "I know you do, you dirty slut!"
                "You lean forward and kiss Lily's neck while you fuck her. She moans louder and rolls her hips to meet yours."
                sis "Oh god you feel so good! Ah! Yes!"
                me "Easy there sis, keep it down. Or maybe you want people to know how much you like getting fucked."
                if sisO.exhib:
                    sis "Ah! Fuck, I don't care! Just keep fucking me, I need it so badly [inputName]. You feel so... good!"
                    "Lily moans loudly again, and you feel her pussy twitch around your cock."
                else:
                    "Lily shakes her head and bites her lip, stifling another moan. You feel her pussy twitch around your cock."

                "Your sister's pussy is warm and tight, drawing you towards your own orgasm with each thrust."
                menu:
                    "Cum inside of her.":
                        me "Fuck, I'm going to cum! Here we go Lily!"
                        if sisO.exhib or sisO.cumslut:
                            sis "Do it! Fill up your little cum slut sister! Ah!"
                            "Lily's whole body quivers as she climaxes. She bucks her hips towards you, desperate to get you deeper."
                        else:
                            sis "Ah! Oh god!"
                            "Lily lets out a short yelp as she climaxes, then bites down on her lip again."
                        "You press yourself against her, holding your cock deep inside of her pussy as you orgasm. She gasps for breath in between each pulse of hot cum."
                        if slut_outfit:
                            show sis fuck47 at right
                        else:
                            show sis fuck46 at right
                        $ sisO.inc_cum_inside()
                        "The two of you stay still for a long moment after you're done, holding each other and breathing heavily. When you finally slide your cock out of her a trickle of semen runs down her leg."
                        sis "It's so warm... Oh god..."
                        me "That was great Lily."
                        "She nods weakly, still trying to catch her breath."
                        me "Come on, get your swimsuit sorted out and lets go sit down."
                        if slut_outfit:
                            show sis swim2 at right
                        else:
                            show sis swim1 at right
                        "She pulls her top back into place, then follows you as you head back to the picnic table. You hang out there until the serum has worn off completely, and you've both recovered from the exertion."

                    "Cum on her tits.":
                        me "Fuck, I'm going to cum! I'm going to cover those hot tits of yours!"
                        "You pull out of Lily's cunt with a wet pop and step back. She drops to her knees, grabbing her breasts to present them to you."
                        if sisO.exhib or sisO.cumslut:
                            sis "Do it, cover your cum slut sister!"
                        else:
                            sis "Ah, do it!"
                        if slut_outfit:
                            show sis fuck51 at right
                        else:
                            show sis fuck50 at right
                        $ sisO.inc_cum_over()
                        "You give yourself a few strokes, then start to fire your load onto your sisters waiting boobs. She gasps as each pulse of hot cum lands on them."
                        me "That's it, take it all for me. Ah..."
                        "When you're done you lean against one of the walls, enjoying how Lily looks when she's covered in your semen."
                        sis "It's so warm... Wow..."
                        "She runs a finger through it, spreading it around the slope of her breasts."
                        if sisO.exhib or sisO.cumslut:
                            sis "I don't have anything to clean it up with..."
                            "She hesitates for a moment, then takes both of her hands and rubs them over her cum covered tits. She spreads your sperm around until it's an even, shiny coating."
                            sis "There, nobody should notice."
                        else:
                            sis "I don't have anything to clean up with..."
                            "She hesitates for a moment, then just pulls her top back into place."
                            sis "I hope nobody notices."
                        me "I'm sure it'll be fine. Come on, lets head back and sit down for a while."
                        if slut_outfit:
                            show sis swim2 at right
                        else:
                            show sis swim1 at right
                        "Lily follows you as you head back to the picnic table, pulling her bikini bottom back into place as you go. You hang out at the table until the serum has worn off completely, and you've both recovered from the exertion."

                    "Cum on her face.":
                        me "Fuck, I'm going to cum! I'm going to cover that cute face of yours!"
                        "You pull out of Lily's cunt with a wet pop and step back. She drops to her knees, looking up at you with wide eyes while you stroke yourself off."
                        if sisO.exhib or sisO.cumslut:
                            sis "Do it, cover me like a fucking cum slut! I want it all over!"
                        "You spray your sisters face with lines of hot cum, then wipe the last few drops off of your tip onto her lips."
                        me "There we go, that's a good girl. Ah..."
                        if slut_outfit:
                            show sis fuck49 at right
                        else:
                            show sis fuck48 at right
                        $ sisO.inc_cum_over()
                        "Once you're done you lean against one of the walls, enjoying how Lily looks when she's covered in your semen."
                        sis "It's so warm... Ah..."
                        "Lily looks around the tiny room when you are done."
                        sis "I don't have anything to get cleaned up with..."
                        if sisO.exhib or sisO.cumslut:
                            if slut_outfit:
                                show sis swim2 at right
                            else:
                                show sis swim1 at right
                            "She shrugs and stands up, pulling her top into place over her semen covered tits. She spreads the biggest puddles around until they're hard to notice."
                            sis "I don't think anyone will care. I left some napkins at our table that I can use when we get there."
                        else:
                            "Eventually she shrugs, and begins cleaning your semen off with her finger. At the end of each pass she licks her finger clean, then starts again on another area."
                            if slut_outfit:
                                show sis swim2 at right
                            else:
                                show sis swim1 at right
                            "Soon she's swallowed most of it, and stands up. She pulls her bottom back in place, then gets her tits back in their top."
                            sis "There, did I get it all?"
                            me "Yeah, you're good. Come on, lets head back to the table."
                        "Lily follows you back to the picnic table. You hang out there until the serum has worn off completely, and you've both recovered from the exertion."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ sisO.change_resist(sis_beach_event_object.get_resist_change(5))
                $ sis_beach_event_object.inc_level(5)

            else:
                "Lily thinks about it for a long moment, taking a slow step towards the changing stall."
                sis "You really want to have sex with me? Right here?"
                me "That's right. I can't think of anything better to end the day with."
                sis "I'm not sure..."
                me "It's no big deal Lily. It's just a quicky, then we can head back to the beach."
                "She's quiet for another few seconds, then takes a step back and shakes her head."
                sis "No, I don't think so [inputName]. You just go in there and jerk yourself off or something, I'm going to head back to the table."
                "She's got a sharper look in her eye now; she must have resisted the serum. Pushing her any farther now would do more harm than good."
                me "Alright, I'm sorry. Just forget I said anything at all, and lets get back to the table."
                "You and Lily return to the picnic table, where you wait until the serum wears off completely."
                $ sisO.change_slut_failed()
                $ sisO.change_resist(sis_beach_event_object.get_resist_change(0))
                $ sis_beach_event_object.inc_level(0)


    return


######################
##Mom's Major Scenes##
######################

label maj_spikeMovieDrinksMom:
    $mom_movie_event_object.happened = True
    $temp_slut_score = 0
    call serum_give(momO) from _call_serum_give_4
    $ temp_slut_score = _return
    "You mix some serum into mom's wine and stir it around quickly."
    mom "Finding it alright?"
    me "Ya, no problem, on my way back already."
    show mom casual at right
    mom "Perfect. Just what I needed."
    "Mom takes the drink from you as you sit down and takes a deep drink."
    mom "Aaaaah."
    "She leans back and sinks deep into the couch. staring at the paused movie on the TV."
    me "You should finish up your wine, I'm sure you'll feel even better after."
    "Mom nods and drinks the rest of the wine. She's taken a full dose now."
    me "How are you feeling? Has the wine relaxed you?"
    mom "Mmhm. Very relaxed. It's been a great evening."
    menu:
        "Have her take off her shirt.":
            $ action_difficulty = 0
            $momO.set_action_exhib()
            $momO.check_willing(action_difficulty)
            me "Good. You deserve a nice relaxing evening. There's something that's definitely not helping you though."
            mom "Oh? What's that?"
            me "You're still wearing a bra. Surely you don't need one when you're just watching a movie around the house. It must get so restrictive after an entire day."
            "Mom nods slowly."
            mom "It does get annoying sometimes."
            me "Why don't you just take it off then? You're at home and we're all family, right?"
            mom "That does make sense..."
            show mom strip1 at right
            "She slowly sits up from the couch and begins unbuttoning her shirt. When the last button is undone she pulls it off and places it on the floor. Her breasts strain against her beige bra underneath."
            mom "Could you help me with this?"
            "Mom turns around, presenting the back of her bra to you."
            me "My pleasure."
            show mom strip2 at right
            $ momO.inc_naked()
            "You unhook the back and mom shrugs it forward. She turns around as she pulls the bra off her arms."
            mom "There we go, that is much better."
            "She sighs and leans back on the couch. The drug must be doing it's work, she doesn't seem the least bit self concious as you look at her chest."
            mom "Should we start the movie again?"
            me "Oh, right. The movie."
            "You pick up the remote and turn the movie on again. You don't know how long the drug will last, but you can't stop yourself from staring at mom's tits."
            "Finally you bring yourself to speak up."
            me "It's getting a little chilly, you may want to put your shirt back on mom."
            mom "Chilly? I didn't notice anything."
            show mom casual at right
            "She moves for her shirt anyway and puts it on. Her bra is still on the floor, and now her nipples show clearly through her shirt."
            me "Just a little chilly. Anyway, we should finish the movie."
            "You and mom enjoy the rest of the movie. She gives you a kiss goodnight, and you both head to bed."
            $ momO.change_slut_rebalanced(action_difficulty)
            $momO.change_resist(mom_movie_event_object.get_resist_change(1))
            $mom_movie_event_object.inc_level(1)

        "Have her get naked.":
            $ action_difficulty = 15
            $momO.set_action_exhib()
            me "Good. You deserve a nice relaxing evening. There's definitely more you could do to relax though."
            mom "Oh? What's that?"
            me "You're still wearing clothes. Everyone knows those are way too restrictive to completely relax in. You should take them off for a while. We're at home after all."
            if momO.check_willing(action_difficulty):
                "Mom nods slowly."
                mom "That makes sense, and this is supposed to be my relaxing day off."
                show mom strip3 at right
                "She slowly sits up and undoes her shirt, placing it over the back of the couch. Next she takes off her bra, then undoes her pants and slides them down."
                show mom nightstrip3 at right
                $ momO.inc_naked()
                "Finally she stands up and slips her panties down past her thighs and lets them fall to the ground. She takes a deep breath, completely naked."
                mom "That does feel nice, doesn't it."
                show mom strip4 at right
                "You watch her tits jiggle as she sits back down on the couch."
                "You aren't sure how long the drug will last, but you enjoy a few minutes watching mom laugh and move around completely naked."
                me "It's getting a little chilly in here, you may want to put your clothes back on. Wouldn't want to catch a cold."
                mom "Of course not, that would be terrible."
                show mom casual at right
                "She slips her panties and pants back on, then does up her shirt. Her bra is left hanging over the back of the couch."
                "You and mom enjoy the rest of the movie. She gives you a kiss goodnight, and you both head to bed."
                $ momO.change_slut_rebalanced(action_difficulty)
                $momO.change_resist(mom_movie_event_object.get_resist_change(2))
                $mom_movie_event_object.inc_level(2)
            else:
                mom "Watch the movie naked?"
                me "Think of it as being your most relaxed."
                "She sits forward and starts undoing her shirt."
                mom "I don't know..."
                show mom strip5 at right
                "The second to last button comes undone, and she pulls her shirt open to reveal her breasts pressed against her bra."
                mom "I don't think I could be comfortable like that."
                me "I'm sure you will be. Don't worry about it at all."
                "Mom hesitates, then sits back on the couch."
                mom "No, I think this is good enough for me. No more tight shirt pressing is all I want."
                "She must be resisting the drug. No point pressing the issue farther then."
                "You and mom enjoy the rest of the movie, though you keep stealing glances at her tits. You wish you could have gotten her out of her bra."
                show mom casual at right
                "Eventually the movie ends, and mom does up her shirt completely. She gives you a goodnight kiss, and the two of you both head to bed."
                $ momO.change_slut_failed()
                $momO.change_resist(mom_movie_event_object.get_resist_change(0))
                $mom_movie_event_object.inc_level(0)

        "Have her give you a handjob.":
            $ action_difficulty = 30
            $momO.set_action_cumslut()
            me "That's good. It's nice that you're able to relax so completely."
            mom "Are you not able to relax?"
            me "No, I've been having some trouble relaxing recently. I've been horny a lot, and there's no way to take care of it right now, unless you'd be willing to give me a handjob."
            if momO.check_willing(action_difficulty):
                mom "A handjob? Here on the couch?"
                me "Sure, while we watch the movie. It'll help me relax so we can both enjoy the evening."
                "Mom hesitates, then slides closer to you on the couch."
                mom "Okay, if it'll help you relax."
                "You slide your pants down a little and pop your cock out, then resume the movie."
                show mom hand4 at right
                $ momO.inc_hand()
                "Mom reaches out with her right hand and grips you by the shaft gently, then slides it up and down slowly."
                mom "Like this?"
                me "Perfect. Now we can just relax."
                "You lean back on the couch and sigh as mom gives you a slow handjob."
                "A few minutes later the movie takes a sudden turn in tone, and you and mom are watching the main characters make out in a closet while their friends prepare a surprise party."
                "Neither of you say anything, but mom starts moving her hand faster along your shaft."
                "The main characters are getting more heated, the woman grabs her shirt and rips it open. Buttons fly past the camera."
                "Mom speeds up even more, eyes locked on the TV."
                "The busty blonde lead reaches down for the main characters crotch while he kisses her between her breasts."
                "The scene and your mom's excitement is getting you close. You're almost ready to cum."
                me "I'm almost there mom."
                show mom hand5 at right
                "Mom doesn't look away from the TV, but reaches over her other hand and takes your full length in both her hands. She slides them up and down quickly, getting you slippery with your own precum."
                "You tense and sigh loudly as you begin cumming. The blonde has her bra lifted up, but is pointed away from the camera, and the man slips his pants down."
                "Your cum gushes out and down, running over mom's hands as she continues to stroke you. In the movie, the door to the closet is thrown open as a bunch of party guests yell \"Surprise!\""
                show mom casual at right
                "Mom slows her stroking down and finally releases you. The back of her hands have thick lines of cum running down them, and the insides look wet and slippery."
                me "There we go, that was great."
                mom "Feeling more relaxed now?"
                me "Definitely, I feel like I'm ready for bed right now."
                mom "Well the movie's almost over, lets watch the end and then call it a night."
                "You and mom sit on the couch for the last fifteen minutes of the movie. Mom keeps her hands folded carefully in her lap, still covered in your seed."
                "Finally the credits roll. Mom gives you a goodnight kiss and you both head off to bed. You feel confident you had a major effect on her tonight."
                $ momO.change_slut_rebalanced(action_difficulty)
                $momO.change_resist(mom_movie_event_object.get_resist_change(3))
                $mom_movie_event_object.inc_level(3)

            else:
                "Mom hesitates, then reaches a hand out for your crotch."
                mom "You haven't been able to masturbate?"
                me "No, I've been thinking about you and Lily, and my own hand just isn't good enough any more."
                "Mom brushes against your crotch, and you flex your cock in response."
                mom "Thinking about Lily? She's your sister though."
                me "I know, but I just can't help it. She's so sexy, I have to hold myself back all the time."
                "Mom's hand withdraws from your waist."
                mom "You can't be thinking about your sister like that though. Or me for that matter, we're family!"
                me "But what if I can't get it off any other way?"
                mom "I'm sure there's plenty of porn out there. Just keep it to yourself in your room and we won't bother you."
                "She's crossed her hands in her lap and is staring straight at the TV now. She must have resisted the drug."
                me "Alright mom, I'll stop then. Lets get back to watching the movie."
                "Damn, you're certain you could have made more progress, but you must have pushed her too far all at once."
                "The movie ends and you and mom say goodnight to each other."
                $ momO.change_slut_failed()
                $momO.change_resist(mom_movie_event_object.get_resist_change(0))
                $mom_movie_event_object.inc_level(0)


        "Have her give you a blowjob.":
            $ action_difficulty = 45
            $momO.set_action_cumslut()
            $momO.set_action_freeuse()
            me "That's good. I know something that would help me relax a huge amount as well."
            mom "Oh? What's that?"
            me "Well I've always enjoyed blowjobs, but I've never had the chance to get one while sitting back and watching a movie. I imagine it would relax me for the entire week."
            if momO.check_willing(action_difficulty):
                mom "I could do that for you then."
                "Mom slides off the couch to her knees and pivots to end up between your legs."
                me "Thanks mom, that would be great."
                "Mom reaches up to your waist and pulls your pants and underwear down to your thighs. Your hard cock stands ready, flexing slightly."
                mom "Oh wow, you do need this don't you sweetheart."
                show mom hand6 at right
                $ momO.inc_blow()
                "She reaches up and takes hold of your shaft. Her soft hand slides up and down slowly."
                me "Ya, I really needed this."
                mom "Just sit back and relax then."
                "Mom grabs the remote and resumes the movie for you to watch over her head."
                "She gives you a gentle handjob for a minute, then leans forward and runs her tongue over the bottom of your cock."
                show mom blow1 at right
                "She licks your shaft repeatedly along all of it's sides, then finally leans it forward slightly and places the tip between her lips."
                "Mom slides her head forward slowly, lips gliding on your wet skin until you feel you tip touch the back of her throat. Her tongue works skillfully inside her mouth."
                "Her head bobs up and down for a few minutes, and you enjoy watching both her and the movie."
                "She slides her head off of you, giving the tip one last kiss."
                mom "Enjoying yourself?"
                me "Oh ya. Your throat feels great."
                mom "Let me know when you're going to finish, okay?"
                me "Sure thing."
                "With that, she returns your cock to her throat and slides you back and forth more quickly."
                "A few more minutes of your mom pleasuring you and you feel your orgasm building up."
                menu:
                    "Hold her down on your cock while you cum.":
                        me "I'm going to cum mom, get ready!"
                        show mom blow2 at right
                        "You reach your hands forward and put them around the back of her head. She tries to slide back, but you hold her in place."
                        "She tries to mumble something past your cock, but you can't hear what it is."
                        me "Almost there, keep going!"
                        "Mom pauses for a moment, and you can hear her breathing through her nose, then she moves her head back and forth quickly on your cock."
                        "A few seconds of her blowing you and you tense as your orgasm comes."
                        "You move your hands and hold her deep on your cock while you spasm and pump your cum into her throat. She places her hands on your thighs and tries gently to pull back, but you don't let her."
                        $ momO.inc_cum_mouth()
                        $ momO.inc_cum_swallow()
                        show mom casual at right
                        "Finally you finish and let your hands fall to your side. Mom slides you out of her throat right away and breaths deeply."
                        "She stays on the floor for a few moments panting heavily."
                        me "You okay mom?"
                        "Mom looks up and nods."
                        if momO.cumslut:
                            mom "Yes, I'm fine. You just tasted so good, I wanted to take a moment to savour it."
                        else:
                            mom "Yes, I'm fine. I didn't realise you needed that so badly. I would have offered earlier if I knew."
                        "She sits back down on the couch and leans close to you."
                        me "Well thank you, that helped a lot."
                        mom "Any time. How about we finish the movie now then."
                        me "Sure."
                    "Let her know you're about to cum.":
                        me "I'm going to cum mom!"
                        "Mom throats you as quickly as she can for a few seconds, making soft slurping noises with her mouth."
                        "As you begin tensing up she slides back a little bit and smiles at you."
                        mom "Okay honey, let it go when you're ready."
                        "Her head is titled up to you, to give you a perfect platform for you to unload on."
                        show mom blow3 at right
                        $ momO.inc_cum_over()
                        "You grab your cock and stroke yourself to completion. Your cock pulses out some thick streams of cum onto your moms waiting face."
                        "As you finish you drop your tip onto her chin, smearing the last few drops onto her."
                        if momO.cumslut:
                            mom "Is that everything sweetheart? You were really storing it up for me, weren't you."
                            me "Yeah, I know how much you like it when I cum on you."
                            mom "Aww, thank you."
                        else:
                            mom "All finished there?"
                            me "Oh ya. All done."
                            mom "Good."
                        "She stands up and sits close to you on the couch."
                        mom "The movie's almost finished, how about we watch the last few minutes then call it a night."
                        "Mom doesn't seem to mind that her face is plastered with your cum right now."
                "The two of you sit close and watch the rest of the movie. Mom gives you a goodnight kiss and you both head to bed."
                "You feel confident that you made a major effect on her tonight."
                $ momO.change_slut_rebalanced(action_difficulty)
                $momO.change_resist(mom_movie_event_object.get_resist_change(4))
                $mom_movie_event_object.inc_level(4)

            else:
                mom "You want me to give you a blowjob?"
                "She slides closer to you on the couch and begins running a hand along your leg."
                me "Ya, definitely. It would help me focus so much better at work."
                "Mom slides her hand up your thigh and under your shirt."
                mom "Is work making you that anxious though?"
                me "Sometimes. It's hard work, and sometimes I think they expected me to already be an engineer."
                "Mom withdraws her hand and looks at you."
                mom "Well you know, if it's bothering you that much maybe you should consider quitting."
                me "I couldn't do that, I signed the contract already. All I need is a little help at home."
                mom "I don't know about that. That much stress can't be good for you, and I can't be here for you all the time."
                "She slides back to her initial spot."
                mom "I can call them and talk to them for you if you'd like."
                me "No really, it's okay."
                "She must have resisted the drug. Maybe you pushed her too far all at once."
                mom "Okay, but if they keep piling on the work let me know."
                me "Sure thing mom."
                "You watch the rest of the movie and finish around midnight. Mom gives you a goodnight hug and you both head to bed."
                $ momO.change_slut_failed()
                $momO.change_resist(mom_movie_event_object.get_resist_change(0))
                $mom_movie_event_object.inc_level(0)

        "Fuck her on the couch.":
            $ action_difficulty = 60
            $momO.set_action_cumslut()
            $momO.set_action_freeuse()
            me "Good. Just stay nice and relaxed. There's plenty we could do while watching the movie to help us both relax more."
            mom "Oh ya? What did you have in mind?"
            me "Well, if you come and sit on my lap I can slide inside of you and we can both keep watching. Satisfy two wants at once."
            if momO.check_willing(action_difficulty):
                mom "Think we could do that?"
                me "I think we could manage."
                "You slide your pants down to your ankles, revealing your erect penis."
                mom "Wow, it looks like you really need this."
                "Mom stands up and unzips her own pants in front of you, then slides them down."
                me "Yep. I really need you to take care of me mom."
                "She undoes her shirt and pulls her bra up so her breasts are free, then turns around."
                show mom strip6 at right
                "She bends over, showing off her ass to you."
                mom "You need this, do you?"
                "You reach forward and grab a hold of her ass with your hands, giving it a good squeeze."
                me "Come on mom, don't keep me waiting."
                mom "Wait, one last thing."
                "She grabs the remote and resumes the movie."
                show mom fuck1 at right
                $ momO.inc_sex()
                "Then she pulls her panties to the side, revealing her wet pussy. She puts a hand behind her onto the couch and begins sitting down."
                "You guide your cock into her slit, and slide into the wet passage."
                "She sits back fully on you, and you slide your full length into her pussy. Mom moans quietly as you slide in."
                mom "There we go, this should help."
                show mom fuck2 at right
                "She braces herself on your thighs and begins lifting herself up and down. Her wet cunt grips you tightly as she slides along your shaft."
                me "That feels great mom, keep going."
                "It doesn't seem like there's any danger of her stopping. She moans and leans back, thrusting her tits into the air."
                "You wrap a hand around and give a breast a squeeze, then pinch a nipple. Mom moans in response and speeds up her pumps."
                me "Lean forward mom, I want to watch your ass move."
                show mom fuck3 at right
                "Mom nods and leans forward, placing her hands on her thighs and using her hips to move her pussy up and down your cock."
                "You take hold of mom's ass with both your hands, pulling it up and down to guide her faster and faster."
                "She's panting and moaning now, shaking from the exertion of being on top."
                me "Do you feel close mom? I want to help you orgasm."
                mom "It's okay. This is all for you."
                "You drive her ass up and down quickly, pumping your own hips up to meet her."
                "She pants heaviy and her legs spasm lightly. Her head is looking down, watching your cock slide into her."
                "Her tight pussy is bringing you close to finishing, and you can feel it quivering around you as well, locked in mini orgasms."
                menu:
                    "Cum inside her.":
                        me "I'm almost there, finish me off mom!"
                        "Mom pants quickly and speeds up her pumping with renewed vigor."
                        mom "Cum whenever you want honey!"
                        "You hold on tight to her ass as you get ready to release and pull her tight against you as the first spasm hits you."
                        "Mom yelps and moans, and you release your spunk deep inside. Her body shakes and her pussy spasms around your shaft."
                        if momO.cumslut:
                            mom "Oh yes! Yes, yes, yes! Give it all to mommy!"
                        "She leans back and slumps while you finish releasing, letting her whole body weight push you deep inside her."
                        "You both sit on the couch and pant for a few moments, your cock still inside her."
                        me "Wow, that felt great mom."
                        show mom fuck4 at right
                        $ momO.inc_cum_inside()
                        "She nods and keeps panting. Eventually she stands up a little bit and lets you flop out of her, then sits down on your lap again."
                        "A small trickle of cum leaks out, and you push her panties back in position to catch the rest for her."
                        mom "I don't think I know what happened in the movie."
                        "You both laugh, and eventually she slides off of you and onto the couch. She buttons her shirt and puts her pants back on."
                        "She gives you a deep goodnight kiss, and you both head off to bed. You feel confident you had a major effect on her tonight."

                    "Cum on her tits.":
                        me "I'm almost ready. I'm going to cum over your tits, okay?"
                        "Mom pants quickly and speeds up her pumping to get you ready."
                        if momO.cumslut:
                            mom "That sounds great, I want you to pump it all out onto my tits for me. Come on, give it to me!"
                        else:
                            mom "Of course honey, you can finish wherever you want."
                        "You tense up as your orgasm approaches and give mom a quick slap on the ass to get her off."
                        "She moans loudly as you slide your cock out of her one last time, then gets on her knees. She holds her tits up in both hands, kneading them softly while she watches you stroke yourself to completion."
                        me "Here I come!"
                        show mom fuck5 at right
                        $ momO.inc_cum_over()
                        "You release, shooting your load over your mom's breasts. Your first string of cum lands on her left breast, then you move to her right and unload some more there."
                        "You let the last few drips land on her tits, then smear them around with your tip. Finally you let go of yourself and sit back with a loud sigh."
                        mom "There you go, all taken care of."
                        me "Ya, wow. Thanks mom."
                        "She nods and begins getting dressed again. She does her shirt up over your load without wiping it away. The fabric clings to her breasts as she moves."
                        mom "Any time. I don't think I quite know what's going on in the movie now."
                        "You both laugh, and once you're ready get up to head to bed."
                        "Mom gives you a deep goodnight kiss, and the two of you head off for the night. You feel confident you had a major effect on her tonight."

                    "Cum on her face.":
                        me "I'm almost there! I want to spray my cum on your face!"
                        "Mom pants and speeds up her pumping until you slap her ass quickly to get her off."
                        "She gets down on her knees and holds her tits in her hands. Her head tilts back and she opens her mouth, tongue out."
                        mom "Ready! Finish on me honey!"
                        "You grab your cock and stroke yourself off until you tense and begin cumming."
                        show mom fuck6 at right
                        $ momO.inc_cum_over()
                        "You unload yourself on your mom's waiting face. You land a spurt into her mouth, the rest landing over her eyes, nose, and dripping down her chin onto her tits."
                        "Mom swallows the small amount that ended up in her mouth, and you both pant for a few moments."
                        if momO.cumslut:
                            mom "Ah, lets make sure I got it all."
                            "She leans forward and starts to lick the sides and bottom of your shaft, eagerly drinking up the last few drops of cum."
                        mom "There we go. How was that sweetheart?"
                        me "Great. You felt great."
                        "Mom smiles and starts doing up her shirt and putting on her pants."
                        mom "I don't think I know what happened in the movie though."
                        "You both laugh, and once she's put back together she gives you a deep goodnight kiss. You feel confident you had a major effect on her tonight."

                    "Cum in her mouth.":
                        me "I'm almost there! I want you to take my load in your mouth mom!"
                        "Mom pants and speeds up her pumping until you slap her on the ass quickly to get her off."
                        "She gets down on her knees and grabs your cock up in her mouth right away."
                        "You tense quickly as she gives you a quick blowjob, licking up her own fluids from your cock."
                        me "Here I come!"
                        "Mom holds your tip in her mouth and looks at you while you stroke your shaft."
                        "You begin releasing, letting your load out into her mouth. She moans and her eyes flutter while she looks at you."
                        $ momO.inc_cum_mouth()
                        "You stroke yourself for a few seconds until you're completely finished, then let mom let go of your cock."
                        me "Let me see it."
                        show mom fuck7 at right
                        "Mom leans back and opens her mouth. Her mouth is filled with your load, and she plays her tongue through the pool of white while she looks at you."
                        menu:
                            "Spit it onto her tits":
                                me "Spit it out onto your tits mom."
                                "She nods. First she tilts her head up and gargles, sending bubbles through the cum and mixing her spit in with it."
                                show mom fuck8 at right
                                "Then she leans her head forward and opens her mouth, letting out a thin stream of white for a few seconds. She moves her head around to drape the line across her tits and nipples."
                                "She ends with a loud spit, spraying a final blob of cum onto her breasts, then looks at you and smiles."
                                if momO.cumslut:
                                    mom "Ah... there we go. Do you think your old mom looks good covered in your hot cum?"
                                    "She pouts a little and runs a finger through the pools of sperm on her breasts."
                                else:
                                    mom "There we go, all done."
                                me "Oh ya, you look beautiful mom."
                                mom "Thank you. I don't think we've been paying attention to the movie though."
                                "You both laugh. You enjoy looking at your cum covered mom, but eventually you both get up."
                                "Mom collects her clothes and gives you a deep goodnight kiss. As she heads off to bed you feel confident you had a major effect on her."
                            "Swallow it all.":
                                me "Perfect mom. Now swallow it all for me."
                                show mom fuck9 at right
                                $ momO.inc_cum_swallow()
                                "She nods and closes her mouth. She gulps loudly, then opens her empty mouth."
                                me "Good girl."
                                mom "Anything for my boy. I think I've lost track of where we are in the movie though."
                                "You both laugh, and mom gets up from the floor. She collects her clothes and gives you a deep goodnight kiss."
                                "As you both head off to bed, you feel confident you had a major effect on her."
                $ momO.change_slut_rebalanced(action_difficulty)
                $momO.change_resist(mom_movie_event_object.get_resist_change(5))
                $mom_movie_event_object.inc_level(5)
            else:
                mom "Slide inside of me... like have sex?"
                "She looks at you sternly."
                mom "I don't think that's such a good idea. Lily may come back any time now. And besides, this is the family couch!"
                "A brief look of disgust crosses her face."
                mom "I can't believe you even said that."
                "Damn, she must have resisted the drug. Maybe you moved too fast."
                me "I was just joking! Me and some of the kids at school have an inside joke, but I guess it just sounds crude if you don't know it."
                mom "Yes, it does."
                me "I'm sorry mom. I didn't mean for it to sound like that."
                "Her look softens."
                mom "That's alright. Lets finish the movie then, shall we?"
                "You watch the movie together, but you can't shake the feeling that you could have done more with this opportunity."
                "Afterwards you and mom say goodnight and head to bed."
                $ momO.change_slut_failed()
                $momO.change_resist(mom_movie_event_object.get_resist_change(0))
                $mom_movie_event_object.inc_level(0)

    jump jumpTimeSkip

label maj_spikeMomNight:
    $ mom_night_event_object.happened = True
    $ temp_slut_score = 0
    "You open the door ever so slowly and slip into her room. You creep forward a few steps at a time, then pause and wait."
    "Your heart beats loudly in your chest as you approach, but mom doesn't move. She breaths shallowly on the bed beside you as you get next to the night stand."
    call serum_give(momO) from _call_serum_give_5
    $ temp_slut_score = _return
    "You carefully take out a vial of serum and open it. You pour it into mom's glass of water and stir it in slowly."
    "Then, creeping backwards again, you back out of the room and slip out of the door again. All that is left to do now is wait until she wakes a little bit and takes a drink."
    "You sit down next to the door and come up with a rough plan of what you're going to say. Tens of minutes pass before you hear her roll over on the bed."
    "There's the creaking of wood, and then the faint sound of water being drunk. You hear her put the glass down again and the bed creaks some more, then silence again."
    "You count to thirty before standing up and moving back to the door."
    "You gently tap on the door, and it swings inwards slightly as well as making a noise."
    me "Mom, are you awake?"
    "You whisper into the dark room, and see the red-outlined shape of mom roll over in bed."
    mom "Huh? Oh, is that you [inputName]?"
    me "Ya, it's me. I've been having trouble sleeping. Sorry to wake you up."
    mom "No problem, come in. What's wrong sweetie?"
    show mom night at right
    "You move into the room and close the door. Mom sits up and clicks a lamp on, bathing the room in yellowish light. Beside her on the nightstand her glass of water is almost all finished."
    me "I'm not sure, just couldn't sleep and I figured I saw that your door was open."
    "Mom pats the edge of the bed, and you come over and sit down beside her. She's wearing a loose tanktop and a pair of old sweatpants as pajamas."
    mom "You can talk to me, if there's something wrong."
    me "I know, I just don't want to upset you. Are you feeling relaxed right now?"
    "Mom nods, and in the lamplight you can see her eyes are having trouble focusing directly on you. Hopefully the drug has taken full effect by now."
    me "Okay, well I've been having some dreams lately. About you."
    mom "Oh? What kind of dreams?"
    me "It's a little embarrassing... sometimes you're naked in them."
    mom "Oh, those kind of dreams. I figured you had grown past that by now."
    me "Me too, but they keep coming back now. I've done some reading, and I think I know something that would take care of it."
    menu:
        "Have her take her shirt off.":
            $ action_difficulty = 0
            $momO.set_action_exhib()
            $momO.check_willing(action_difficulty)
            me "One of the things that keeps popping up are your breasts; they're always either huge or too small, or something strange."
            mom "That sounds really weird."
            me "I know. I did some research and it's because I don't have a mental image of what they should look like. If I got a good look it would stop bothering me entirely."
            "Mom thinks about it for a while while you sit together on the bed. Finally her hands go to the bottom of her tanktop."
            mom "Well, I think I can help you out then. I'm sure this is nothing you haven't seen before by accident. This way there's no mystery."
            show mom nightstrip1 at right
            $ momO.inc_naked()
            "She pulls her top up and off completely, throwing it into a hamper across the room."
            "Her breasts jiggle slightly as she turns to look at you."
            mom "So this is what you need to see?"
            me "Ya, that's it. Could you shake them a little for me?"
            mom "Shake them?"
            me "Right, it happens in my dreams sometimes so I want to make sure it doesn't come back."
            "She nods, then shakes her shoulders so her tits move left and right for you."
            "You spend a few minutes studying her boobs. Finally you speak up."
            me "Okay, that should be enough. Thanks a ton mom, this should really help."
            mom "Anything for you sweetheart. Getting a good night's sleep is important."
            "She opens her arms and gives you a hug, her bare breasts pressing against your chest."
            "Afterwards you head to your room, confident you had a major effect."
            $momO.change_slut_rebalanced(action_difficulty)
            $momO.change_resist(mom_night_event_object.get_resist_change(1))
            $mom_night_event_object.inc_level(1)

        "Have her get completely naked.":
            $ action_difficulty = 15
            $momO.set_action_exhib()
            me "If I could see you completely naked my subconscious might be satisfied, and the dreams would stop."
            if momO.check_willing(action_difficulty):
                mom "Seeing me naked would stop these dreams?"
                me "It would definitely help. There would be no mystery, so my mind could move onto other topics."
                mom "I guess that makes sense. If it'll help you out, it's okay. Besides, it's nothing you haven't seen by accident when you were younger."
                "She grabs the bottom of her shirt and pulls it up and off. Her tits jiggle as they drop free of the garment."
                show mom nightstrip1
                me "Right, we've all caught glances occasionally. It's part of being a family."
                show mom nightstrip2
                "Mom stands up and walks in front of you. She slides her sweatpants down and kicks them to the side, then reaches for her beige underwear."
                mom "You need to see it all?"
                me "That would be the most effective."
                mom "Okay. Here we go."
                show mom nightstrip3
                $ momO.inc_naked()
                "She takes a deep breath and pulls her panties down past her knees and lets them drop. She kicks those into the pile of her clothes and stands naked for a moment."
                me "Wow, you look great."
                mom "Thanks. So you have to see everything so there's no mystery, right?"
                me "Right."
                show mom nightstrip4
                "Mom turns around and bends over slightly. Her hands reach around to her ass and pull her buttcheeks wide so you can see her anus and pussy clearly."
                mom "Can you see everything okay?"
                me "Oh ya, I can see it all. You're doing great mom."
                show mom nightstrip5
                "She turns around and plants her legs wide, then reaches down with a hand and spreads the lips of her pussy for you too."
                mom "There, I think that's everything a horny boy would want to see."
                "You nod and enjoy the view for a few minutes. Finally you speak up."
                me "Okay, I think that's enough mom. Thank you so much for your help."
                "You stand up to go, and mom gives you a big hug. Her warm body presses up against yours."
                mom "It's no problem sweetheart. Thank you for feeling comfortable enough to talk to me about this."
                "You hug her back, then head to your room. You feel confident you had a major effect."
                $momO.change_slut_rebalanced(action_difficulty)
                $momO.change_resist(mom_night_event_object.get_resist_change(2))
                $mom_night_event_object.inc_level(2)
            else:
                mom "You would have to see me naked?"
                me "Right, so that there's no mystery any more."
                "Mom puts a hand on the bottom of her tank top and thinks about it for a while."
                mom "There must be another way though. This just seems like it would make your fantasies worse."
                me "Trust me, I've done a lot of reading about this trying to find a solution."
                mom "Well you can't trust everything you read on the internet. I think the best thing for it is a quick cold shower, it's worked for generations."
                "She seems determined, she must have resisted the drug. Maybe you pushed her too far."
                me "If you think that's best, I'll try. Sorry to have woken you up."
                mom "No problem honey, now you should head off and try and get some sleep."
                "You nod and head back to your room, knowing you could have done more with the situation."
                $momO.change_slut_failed()
                $momO.change_resist(mom_night_event_object.get_resist_change(0))
                $mom_night_event_object.inc_level(0)

        "Have her give you a titfuck.":
            $ action_difficulty = 30
            $momO.set_action_cumslut()
            $momO.set_action_freeuse()
            me "If the subject of my dream helped me actually realise the fantasy they might finally stop. Would you use your breasts and help me mom?"
            if momO.check_willing(action_difficulty):
                mom "You need me to use my breasts to make you cum? Are you sure this will help?"
                me "Of course, I've done my research. By doing this for me you cross the fantasy off the list my subconscious has, so I can focus on other things."
                "Mom sits on the bed and thinks for a long moment, then nods."
                mom "Okay, if you think it will help you. Slide your pants down sweetheart."
                "Mom gets on the floor and pulls her shirt up and over her head. She throws it towards a hamper on the other side of the room, then turns her attention back to you."
                "You slide your pants down to your ankles and sit on the edge of the bed. Mom moves up between your legs and looks up at you."
                mom "Now remember, this is just to help you, and nobody can know."
                me "Whatever you say mom."
                show mom nighttit1 at right
                $ momO.inc_tit()
                "She takes her tits up in her hands and wraps them around your hard cock. The warmth and softness make you sigh with pleasure."
                "She slowly begins to slide them up and down your shaft, making sure you don't slide out of her cleavage by pushing her tits together with her hands."
                "For a few minutes neither of you speak as she titfucks you."
                mom "How am I doing? Are you feeling good?"
                me "Feeling great. You're doing a great job."
                mom "Good. Let me know if there's anything I can do to make it better."
                me "Well, it would be even nicer if you got me wet."
                if temp_slut_score > 50:
                    "Mom nods and opens her mouth. On her next down stroke she slides her tits off and moves her mouth on to your tip, then slides herself even further down."
                    "She licks your cock with her tongue and slides you all the way down her throat slowly. When she reaches your base she begins sliding off, ending with a wet pop."
                    mom "There, that should help."
                    "She begins sliding her breasts up and down again."
                else:
                    "Mom nods and looks down at the cock between her tits. She opens her mouth and sticks her tongue out, letting a long thick line of drool fall down and over your shaft."
                    "She spits to get the last bit of saliva out, then starts sliding her breasts up and down again."
                "Your mom strokes you for another minute or two, her warm wet tits bringing you close to orgasming."
                me "Mom, I'm getting close to finishing."
                mom "Okay honey, that's good. Just let it out whenever you want."
                "A few more strokes and you tense up as your orgasm begins."
                show mom nighttit2 at right
                $ momO.inc_cum_over()
                "Mom keeps sliding her tits up and down as you fire your load. She keeps your tip pointed up and away from her face, so your load shoots up and then falls back down over her tits and leaks down her cleavage."
                "You pulse out your last few spurts and sigh loudly, while mom slides back and slips your cock out from between her tits."
                mom "There you go, well done sweetheart."
                "She grabs a tissue from a box by her bed and starts wiping your cum off of her."
                me "Thanks mom. That really helped. I should be getting back to bed now."
                mom "Have a good night, I'll see you in the morning."
                "She smiles at you as you walk out and return to your bedroom. You feel confident you had a major effect on her tonight."
                $momO.change_slut_rebalanced(action_difficulty)
                $momO.change_resist(mom_night_event_object.get_resist_change(3))
                $mom_night_event_object.inc_level(3)
            else:
                mom "You would need me to make you orgasm? That seems a little strange."
                me "It's what I've dreamed about, and I think it's the only way to make it stop."
                "Mom thinks about it for a long moment while you sit together on the bed."
                mom "There must be another way though. The internet isn't always right about these things. Maybe you should try masturbating more right before bed."
                "Her speech is more determined, her eyes more focused on you. She must be resisting the drug."
                me "If you think that would work I'll give it a try. Sorry I woke you up mom."
                mom "No problem honey. Now you should head off and try and get some sleep."
                "You nod and head back to your room, knowing you could have done more with the situation if you didn't push her so far."
                $momO.change_slut_failed()
                $momO.change_resist(mom_night_event_object.get_resist_change(0))
                $mom_night_event_object.inc_level(0)

        "Have her give you a blowjob.":
            $ action_difficulty = 45
            $momO.set_action_cumslut()
            $momO.set_action_freeuse()
            me "These dreams are making me really horny, and it's getting in the way of my sleep. Blowjobs always finish me quick and make me sleepy. Could you help me mom?"
            if momO.check_willing(action_difficulty):
                mom "Well, sleep is very important for someone your age. It's important you get enough of it."
                me "So you can help me?"
                "She thinks about it for a long moment while you sit together on the bed. Finally she signs and nods."
                mom "I'll help however I can."
                "She gets off the bed and onto her knees, turning to face you."
                mom "We'll need to get these off before we do anything though."
                "She reaches forwards, and you help her slide your pants down and off completely. Your hard cock stands ready and waiting."
                show mom nightblow1 at right
                $ momO.inc_blow()
                "Mom takes your cock in her hand and strokes it gently. Then she leans down and gives it a kiss on the tip, sticking her tongue out and swirling it around."
                mom "Ready?"
                me "Ya, ready."
                "She lowers her head and wraps her mouth around your shaft completely. She bobs up and down, getting lower with each stroke. You can feel her tongue lick along the bottom of your dick as she goes deeper."
                "Finally her nose hits your waist and she has all of your cock in her mouth. She moves up and down some more, going along the entire length with her mouth."
                "For a few minutes you enjoy watching your mom suck your cock."
                me "Hey mom, it would be even better if you could show me your tits while you do this."
                show mom nightblow2 at right
                "She doesn't stop sucking, but pulls her tanktop up past her breasts and lets them fall out."
                "She speeds up her blowjob, making little wet noises at the bottom of every stroke as your tip hits the back of her throat."
                "Finally she comes up for air, taking a deep breath."
                me "That's feeling great."
                mom "Good, I want to make you feel as good as I can."
                "She returns to sucking you, and you can feel your orgasm start to build."
                menu:
                    "Cum in her mouth.":
                        me "Mom, you're getting me really close. Can I cum in your mouth?"
                        "Mom nods and tries to mumble something past your cock. She speeds up her sucking some more, and before long you're ready to finish."
                        $ momO.inc_cum_mouth()
                        "You tap her on the shoulder as you begin releasing, and she holds your tip in her mouth while you release. You stroke your shaft while you shoot your cum into her mouth."
                        if momO.cumslut:
                            "When you're finished she pulls back slowly, careful not to let any of your semen slip out. She pauses for a moment and swallows, drinking your load in two big gulps."
                            mom "Ah, you always taste so good. You gave me so much too, you definitly needed that."
                            $ momO.inc_cum_swallow()
                        else:
                            "When you're finished she pulls back slowly and reaches towards her nightstand. She grabs her water glass and spits your load into it."
                            mom "Wow, good job sweetheart. You definitely needed that."
                        me "I really did. Thanks mom."

                    "Cum on her face.":
                        me "Mom, you're getting me really close. Can I finish on your face?"
                        "Mom slides off of your cock for a moment."
                        mom "Watching a lot of porn, are we?"
                        me "Maybe, but it would be really hot."
                        mom "If it makes you feel better, fine."
                        "She puts you back in her mouth and blows you as quickly as she can. Before long you're tensing as you get ready to release."
                        show mom nightblow3 at right
                        $ momO.inc_cum_over()
                        "Mom leans back and looks up at you, breathing through her nose and closing her eyes. You stroke your shaft a few times and unload onto her face. Your cum covers her nose, one eye, and dribbles down her chin."
                        me "Ahh! That's great!"
                        if momO.cumslut:
                            "She waits for a few seconds, then starts to scoop your cum towards her mouth. She licks it up with her tongue and swallows, and soon your mom has cleaned herself off entirely."
                            $momO.inc_cum_swallow()
                        else:
                            "She waits for a few seconds, then reaches for some tissues and starts wiping her face."
                        mom "Glad you enjoyed yourself honey."

                    "Cum on her tits.":
                        me "Mom, you're getting me really close. I want to finish on your tits."
                        "Mom nods and tries to mumble something past your cock. She speeds up her sucking some more. Before long you're ready to finish."
                        me "Here it is, get ready!"
                        show mom nightblow4 at right
                        $ momO.inc_cum_over()
                        "Mom pulls you out of her mouth and strokes you off while pointing your tip at her tits. You fire your load and she guides your cock left and right to cover her breasts with it."
                        "When you're done she lets go and looks down at her chest."
                        mom "Wow, good job honey. You definitely needed that."
                        me "I really did, wow. Thanks."

                    "Take over and cum down her throat.":
                        "The sight of mom's head on your cock is too much. You reach forward and grab her by the sides of her head."
                        me "You feel great, I'm almost there!"
                        "You use your hands to move her head up and down even faster. You can hear her gag when your tip hits the back of her throat hard, and feel her mouth wrap tighter around you with each stroke."
                        show mom nightblow5 at right
                        $ momO.inc_cum_mouth()
                        $ momO.inc_cum_swallow()
                        "Mom puts her hands on your thighs and grips tightly, but doesn't try and pull off."
                        "You work your hips up and down, bouncing on the bed to get your cock going even deeper. Mom gargles something and blows spit bubbles around the base of your shaft while you fuck her mouth."
                        "You tense up and get ready for release. You knit your fingers together behind her head and pull your mom down as far as she will go."
                        "You can feel your tip pressed up against the back of her throat as you begin cumming. Mom's whole mouth squirms around as you unload down her throat, making the feeling even more intense."
                        "After a few seconds you're done, and let go of mom's head. She pulls back quickly and gasps for air."
                        me "Sorry about that mom, I just got carried away I guess."
                        "Mom leans over and breaths deeply, then coughs lightly."
                        if momO.cumslut:
                            mom "It's okay, you know I love feeling you finish in my throat like that. Are you feeling okay now?"
                        else:
                            mom "It's okay. I didn't know you needed it that badly. Are you feeling okay now?"
                        me "Ya, feeling much better. You were great."
                        mom "Good. I'm glad I helped."
                        "She takes a moment to catch her breath, then stands up."

                mom "Now you should be getting off to bed, it's late."
                me "Right, of course. Goodnight mom."
                "You head back to your room, confident you had a major effect on her."
                $momO.change_slut_rebalanced(action_difficulty)
                $momO.change_resist(mom_night_event_object.get_resist_change(4))
                $mom_night_event_object.inc_level(4)
            else:
                mom "Wow honey, that's asking a lot of me."
                me "I know, but I really think I need it to get a good nights sleep."
                "Mom thinks for a few moments while you sit together on the bed."
                mom "I don't think I can do that, there must be another way. How about you head to your room and try masturbating before going to sleep."
                me "I've tried that, but it just doesn't help."
                mom "Maybe you need to do it a few times before bed then, to take care of your urges. I'm sure the internet has plenty of... inspiration for you."
                "Her speech is more determined and her eyes are focusing better. She must be resisting the drug. Maybe you pushed her too far."
                me "If you think so I'll give it a try, I'm not sure how well it will work though."
                mom "Well there's only one way to find out. It's late, you should head back and try and get some sleep."
                "You nod and head back to your room, knowing you could have done more with the situation."
                $momO.change_slut_failed()
                $momO.change_resist(mom_night_event_object.get_resist_change(0))
                $mom_night_event_object.inc_level(0)

        "Have her ride you on her bed.":
            $ action_difficulty = 60
            $momO.set_action_cumslut()
            $momO.set_action_freeuse()
            me "If I could carry out my fantasy to completion there wouldn't be anything left to dream about. I would need you to have sex with me though, could you do that for me mom?"
            if momO.check_willing(action_difficulty):
                mom "I suppose that makes sense. It's important you're getting your sleep. I wouldn't be a very good mother if I didn't help out when I can."
                "You lean forward and give your mom a deep kiss. She holds back for a moment, then returns the kiss. Your tongues meet and wrap around each other. Finally you break the kiss."
                mom "How about you lie down and let me take care of everything, okay?"
                me "Okay mom."
                "You strip out of your pants and shirt quickly, then lie down in the middle of the bed."
                show mom nightstrip3 at right
                "Mom pulls her shirt up and off, then drops her pants off too. Finally she pulls her panties down and leaves them with the rest of the pile."
                "She climbs onto the bed and gets on all fours between your legs. She takes your cock in her hand and rubs it gently."
                mom "I'll have to get this wet before we do anything else, of course."
                show mom nightfuck1 at right
                "Your mom runs her tongue along the bottom of your cock, then licks around your tip. After getting that wet, she slides her mouth over and starts giving you a blowjob."
                "She sucks you off for a few minutes, getting your shaft dripping wet with her spit."
                me "That feels amazing."
                "She pulls off of your dick and looks up at you."
                mom "Just wait for the rest of it then."
                "She crawls forward and kisses you again. She grinds her hips against yours, and your cock rubs against her pubic hair."
                "Mom gets up to a kneeling position, legs on either side of you and pussy positioned directly above your cock."
                "She takes hold of your shaft with one hand and spreads herself with the other, rubbing your tip along her slit."
                mom "Oh, that feels good for me too."
                show mom nightfuck2 at right
                $ momO.inc_sex()
                "She closes her eyes and sighs, then slowly begins lowering herself onto you."
                "Her pussy is suprisingly tight and dripping wet. Without any effort you slide in to your full length and mom moans with pleasure."
                "She begins riding you cowgirl style, and you watch while your cock slides in and out of her rhythmically."
                me "You feel great mom, you're dripping wet and tight."
                mom "Thank you honey. This feels really good."
                show mom nightfuck3 at right
                "Mom leans forward and places her hands on either side of your chest. Her hips work up and down while she fucks you."
                "You grab her tits with your hands and play with them gently. Your thumbs rub her nipples, and you let her tits bounce in your hands as she rides you."
                mom "Oh ya, keep doing that!"
                me "Whatever you say mom."
                "You lean your head up and latch your mouth onto one of mom's tits. She gasps in pleasure as you run your tongue in circles around her areola."
                "Her hips pump faster, and you feel her pussy twitch around your cock. She moans loudly and leans back, pulling her tit from your mouth."
                show mom nightfuck4 at right
                "With her hands back and behind her she rides you hard and fast. The bed creaks loudly as she goes, and you can see your cock slide in and out of her clearly."
                if momO.exhib:
                    "Mom moans loudly, caught up in her own orgasm."
                    me "Easy there Mom, you're going to wake up Lily if you keep going at it like that."
                    mom "Ah! I don't care, just keep fucking me! She's be moaning like this too if she had such a nice cock in her!"
                    "She tenses up, pussy twitching around your cock as she orgasms. Seeing her cum drives you towards finishing as well."
                else:
                    "Mom moans and twitches, caught up in her own orgasm. Seeing her cum drives you towards finishing as well."
                menu:
                    "Cum inside her.":
                        me "I'm almost there mom. Don't stop."
                        "Mom nods and moans again."
                        if momO.cumslut:
                            mom "I promise I won't. I want you to cum deep inside me, like you want to get me pregnant again!"
                        else:
                            mom "Okay, I won't."
                        "She bounces up and down on the bed, taking your full length into her."
                        mom "Give it to me, cum inside your mom!"
                        "Her tits jiggle and sway, getting air time at the top of each stroke."
                        mom "I want it all inside me!"
                        "You reach forward and grab her hips as you begin cumming. You pull your mom down onto your cock as deeply as you can while you release your cum inside."
                        mom "Oh fuck! Yes!"
                        show mom nightfuck5 at right
                        $momO.inc_cum_inside()
                        "Mom spasms and she orgasms hard. She struggles against your hips and you let her go. She gives your cock a few more thrusts inside her pussy, then pulls out and lies down on top of you."
                        "You both breath heavily for a moment, catching your breath."
                        me "That felt great mom."
                        mom "Ya, it did."
                        "She rolls off of you, and you lie together on the bed."

                    "Cum on her face.":
                        me "I'm almost there mom. I want to cum on your face, okay?"
                        mom "Okay, I'll take care of everything!"
                        "She bounces up and down, taking your full length into her with each stroke and moaning constantly."
                        "You reach the edge of your orgasm and reach forward, slapping your mom on the ass to get her off."
                        "She pulls out and crawls backwards, getting her face over your cock. Then she grabs it with one hand and strokes you as fast as she can."
                        show mom nightfuck6 at right
                        $momO.inc_cum_over()
                        "You groan and release your load, shooting it up into her face. Your cum splashes where it lands, some of it falling back to land on the sheets and your legs."
                        "Mom keeps stroking until you're finished, then rubs your tip along her face to smear in your load."
                        mom "All done?"
                        me "All done. That's all I've got."
                        mom "Good job honey, you did great."
                        "She climbs up to the top of the bed and collapses beside you, face still covered in cum."

                    "Cum in her mouth.":
                        me "I'm almost there mom! I want to cum in your mouth!"
                        mom "Okay darling! I'll take care of everything!"
                        "She bounces up and down as fast as she can, taking in your full length."
                        "As you reach the edge of your own orgasm you give her a hard spank on the ass to get her moving."
                        "Mom gets up off your cock and crawls backwards. She wraps her lips around your tip and slides her head down. Your shaft is already wet from her pussy, and slides in easily."
                        "After a few seconds of her blowing, you tense and begin releasing your load. Mom pulls back and holds your tip in her mouth while you let your cum go."
                        show mom nightfuck7 at right
                        $momO.inc_cum_mouth()
                        $momO.inc_cum_swallow()
                        "When you finish she slides off carefully and sits up. She opens her mouth and shows you your own cum in her mouth."
                        "She closes her mouth and swallows loudly, then pants loudly. Mom climbs up beside you and collapses on the bed."
                mom "You're probably really tired after that. You can just stay here for the rest of the night if you want."
                me "That sounds nice, thanks mom."
                "She looks at you and gives you a kiss."
                mom "You can be the big spoon."
                "She rolls over, and you cuddle up behind her. Your still wet cock rubs against her warm ass as you fall asleep. As you drift off you feel confident you've had a major effect on her tonight."
                $momO.change_slut_rebalanced(action_difficulty)
                $momO.change_resist(mom_night_event_object.get_resist_change(5))
                $mom_night_event_object.inc_level(5)
            else:
                mom "Wow. Thats a lot to ask."
                me "I know, but if this keeps up I might never have a good night's sleep again."
                mom "There must be another way though, it's not like other moms have sex with their kids..."
                me "Well, I don't know what to do then."
                mom "How about you head back to your room and masturbate and see if that helps. Maybe you need to think about finding a nice girl and have her satisfy your...urges."
                mom "Safely of course! Always make sure you're taking care of yourself!"
                "Her eyes are focusing better now, and she seems pretty determined now. She must have resisted the drug because she was pushed too far."
                me "Right, I guess that might work. Well I'm sorry I woke you up."
                mom "No problem, I'm glad you could trust me with this. It's late, you should head off and see if you can get some sleep."
                "You nod and head back to your room, knowing you could have done more with the situation."
                $momO.change_slut_failed()
                $momO.change_resist(mom_night_event_object.get_resist_change(0))
                $mom_night_event_object.inc_level(0)
    jump jumpTimeSkip

label maj_mom_shower:
    $ mom_bathroom_event_object.happened = True
    $ temp_slut_score = 0
    call serum_give(momO) from _call_serum_give_21
    $ temp_slut_score = _return
    "You open up mom's mouthwash bottle and grab the plastic cup she uses for it. You pour out a mouthful, then add in the serum and stir it in."
    "That done, you start to go about your own morning routine, leaving the door unlocked."
    show mom night at right
    "After a few minutes the door opens, and your mom steps in. She yawns, then realizes you're there."
    mom "Oh! I'm sorry [inputName], I should have knocked."
    me "It's okay mom, I'm just trying to get my hair looking alright. I figured you might be busy and poured out your mouthwash for you."
    "Mom steps into the room and closes the door behind her. You step to the side and make room for her at the counter."
    mom "Thank you, I've just got to grab a shower and get ready for work."
    "She takes the mouthwash and drinks it, swishing it around for a few seconds and humming. After a few moments the humming gets slower, and when you look at her in the mirror her pupils are dilating."
    "You wait until your mom goes to spit out the mouthwash, then speak up."
    me "Hey, you should swallow that, it's even better for your breath."
    "Mom looks at you and seems puzzled for a moment, but eventually swallows her mouthwash and the rest of the serum."
    mom "Are you sure about that?"
    me "Absolutely, just trust me."
    "Mom nods slowly, and you can see the serum taking hold quickly."
    menu:
        "Stay in the room while she strips down.":
            $ action_difficulty = 0
            $momO.set_action_exhib()
            $momO.check_willing(action_difficulty)
            me "I know you're in a rush, so you can just get ready for your shower while I try and sort out my hair."
            mom "Sure, if you don't mind. Thanks."
            me "No problem. No problem at all."
            "Mom washes out her mouth, then steps over to the glass shower door. She gets her towel in place, then reaches for her shirt."
            show mom nightstrip1 at right
            "She pulls it up and over her head in a single motion, dropping it to the ground and freeing her large breasts."
            show mom nightstrip2 at right
            "Then she turns around and puts her thumbs into the waistband of her pants, sliding them down to the ground and stepping out of them."
            "She turns and looks at you, just in her panties."
            mom "Okay, I'm going to need the room if you don't mind [inputName]. I'll let you know when I'm done."
            me "Sure thing mom. Have a great shower."
            hide mom
            "You step out of the room and close the door behind you, hearing the sound of the shower start in the room."
            "You head back to your room and wait until your mom is done, confident you've had a [momO.effect_string] impact on her this morning."
            $ momO.inc_naked()
            $ momO.change_slut_rebalanced(action_difficulty)
            $ momO.change_resist(mom_bathroom_event_object.get_resist_change(1))
            $ mom_bathroom_event_object.inc_level(1)

        "Stay in the room while she has her shower.":
            $ action_difficulty = 15
            $momO.set_action_exhib()
            me "I know you're in a rush, so go ahead and grab a shower while I try and sort my hair out."
            "Mom nods and washes out her mouth, then steps over to the glass shower door. She gets her towel in place, then reaches for her shirt."
            if momO.check_willing(action_difficulty):
                #Success
                show mom nightstrip2 at right
                "She pulls the tanktop up and off, dropping it to the ground beside her. A moment later she's dropped her pants as well, adding them to the pile of clothing."
                "Mom hesitates for a moment and looks at you, wearing nothing but her panties."
                me "Seriously, don't worry about it. Just go ahead."
                show mom nightstrip3 at right
                "She nods and turns back to the shower, hooking her underwear with her thumbs and sliding them down. Now completely naked, your mom steps into the glass shower enclosure and starts the water."
                "You stand at the counter, glancing sideways to watch your mom while she starts to wash herself. After a few minutes she turns to face you as the water runs down her body."
                mom "You don't have to keep hiding it, if you want to watch you can."
                me "Sorry Mom, I didn't mean to bother you."
                "Mom smiles turns back to face the shower head, running her hands down her front."
                mom "It's okay, I know you've got urges sometimes and it's hard to resist. If you have to, um, take care of something you can do that too."
                "Watching your mom's glistening naked body really has gotten you turned on, and your hard cock is pressing against your pants."
                me "Well, if you're sure you don't mind."
                show mom showerstrip1 at right
                "Mom shakes her head and turns away from you, showing off her ass. You aren't sure if she's doing it on purpose or not."
                "You lower the lid on the toilet beside the shower and sit down, pulling your pants down enough to slip your cock out. You don't waste any time and start to jerk yourself off while looking at your mom."
                show mom showerstrip2 at right
                "For a few minutes the only sound in the room is the splashing of water from the shower. Mom grabs the soap and rubs it over her body, covering herself in bubbles for a little bit before she washes it all away."
                mom "I'm going to have to get going soon. Are you almost done?"
                "She turns to you and watches for a moment while you stroke your hard shaft."
                me "Ya, I'm almost there. If you want to help out, press your tits against the glass for me."
                show mom showerstrip3 at right
                "She hesitates and thinks for a moment, then nods and leans forward to plant her breasts on the plate glass of the shower. You swivel on your seat and point towards her, stroking yourself faster."
                me "Mmm, just like that. Fuck, you look so good Mom."
                "Mom doesn't say anything, but rubs her tits up and down on the glass a little."
                "A few more strokes and you push yourself over the edge. You take a sharp breath as you start to blast your cum towards your mom, splattering it over the glass at her waist level."
                mom "Oh!"
                show mom shower at right
                "You take a moment to collect yourself while Mom turns the shower off and gets her towel. She gathers her clothes up and heads for the door."
                me "Thanks for that Mom, that was great."
                mom "I'm glad you had a good time. Make sure to clean that up before you leave, okay?"
                me "Will do."
                hide mom
                "She smiles and slips out of the bathroom, closing the door behind her. You're confident you had a major effect on her here."
                "You take a fast shower yourself, then head back to your room with plenty of time left in the morning."
                $ momO.inc_naked()
                $ momO.change_slut_rebalanced(action_difficulty)
                $ momO.change_resist(mom_bathroom_event_object.get_resist_change(2))
                $ mom_bathroom_event_object.inc_level(2)
            else:
                #Failure
                "She hesitates for a moment, then looks at you and shakes her head."
                mom "Ah, I think it would actually be best if you gave me a few minutes."
                me "Seriously Mom, it's okay."
                mom "I know, I just would feel more comfortable alone. I'll let you know when I'm done, okay?"
                "Mom has a sharper look in her eye, and has taken on a firmer tone. You must have pushed her too far, and she's resisted the serum."
                me "Alright, fine. Have a good shower mom."
                "You step out of the room and mom locks the door behind you. You head back to your room to wait until she's done, knowing you could have done more if you hadn't been so aggressive."
                $ momO.change_slut_failed()
                $ momO.change_resist(mom_bathroom_event_object.get_resist_change(0))
                $ mom_bathroom_event_object.inc_level(0)

        "Get a handjob while she showers.":
            $ action_difficulty = 30
            $momO.set_action_exhib()
            $momO.set_action_cumslut()
            me "I know you're in a rush to get ready for work Mom. Lets just share a shower, that way we can save some time."
            "Mom washes out her mouth, then turns to look at you."
            if momO.check_willing(action_difficulty):
                #Success
                mom "I think that'll be fine. You'll need to get my back for me though, okay?"
                me "Sounds fine to me."
                show mom nightstrip3 at right
                "Mom strips off her clothes, leaving them in a pile on the floor, and steps into the glass shower enclosure. While she gets the water going you ditch your clothes as well and step in behind her."
                "After letting the water run over both of you for a few moments your mom hands you a block of soap."
                mom "Here, just give it a little scrub please."
                me "Sure thing."
                "You take the soap and start to rub it along her back. You take a step closer, letting your hard cock brush up against her ass while you wash her."
                mom "Oh! Uh, is that..."
                me "Ya, sorry. I guess it's a little early, and seeing you like this isn't exactly helping get rid of my morning wood."
                "Mom is silent for a few seconds while you wash her, the tip of your penis resting gently on her ass cheek."
                mom "Here, I'll take care of you then. Just stay still."
                show mom showerhand1 at right
                "She turns around to face you and reaches her hand down, wrapping her hand around your shaft. She steps against you, breasts pressing against your chest while she starts to stroke you slowly to her side."
                me "Ah, wow. That feels great."
                mom "Good, just let it go whenever you're ready."
                "For a few minutes you enjoy the feeling of your mom's warm body pressed up against yours as the water flows over both of you. Her handjob speeds up a little at a time, lubricated by the shower water."
                "Eventually you feel your climax getting closer. You reach your hands around and grab your moms ass, squeezing tightly as you start to cum."
                me "Fuck, keep going."
                show mom nightstrip3 at right
                "Your mom moans softly as you grip her cheeks and start to fire your load into the glass wall beside you. After a few moments you're done, and she lets go of you slowly."
                mom "There, I hope you feel better now."
                "You nod while she washes her hand off quickly, then steps out of the shower and grabs her towel."
                mom "Make sure to clean that up before you're done."
                me "Sure thing. Thanks mom."
                hide mom
                "Mom collects her clothes and slips out of the room. You feel confident you've had a major effect on her, and head back to your room after your shower with plenty of time left in the day."
                $ momO.inc_hand()
                $ momO.change_slut_rebalanced(action_difficulty)
                $ momO.change_resist(mom_bathroom_event_object.get_resist_change(3))
                $ mom_bathroom_event_object.inc_level(3)
            else:
                #Failure
                mom "I'm not so sure."
                "She plays with the edge of her shirt, pulling it up a little then smoothing it out."
                me "It'll save us both some time, it's no big deal."
                "Mom thinks for a few long moments, then shakes her head."
                mom "I think I'd prefer to be alone. I promise I won't be long."
                "She's got a sharper look in her eye, and a firm tone to her voice. You must have pushed her too far, and she's resisted the serum."
                me "Alright, fine. Have a good shower mom."
                "You step out of the room and mom locks the door behind you. You head bck to your room to wait until she's done, knowing you could have done more if you hadn't been so aggressive."
                $ momO.change_slut_failed()
                $ momO.change_resist(mom_bathroom_event_object.get_resist_change(0))
                $ mom_bathroom_event_object.inc_level(0)

        "Get a blowjob while she showers.":
            $ action_difficulty = 45
            $momO.set_action_cumslut()
            $momO.set_action_freeuse()
            me "Hey Mom, I just got up and I've got some morning wood. I know you're in a rush, but do you think you could take care of it for me while we have a shower?"
            "Mom takes a step back and looks at you for a moment, thinking."
            if momO.check_willing(action_difficulty):
                #Success
                mom "I don't have much time before work, but if we make it quick I think I can do that for you."
                show mom nightstrip3 at right
                "You and Mom peel off your clothes and step into the shower. It takes a moment for Mom to get the water adjusted to the right temperature, then she turns and looks at you as the water runs over you both."
                mom "So, this is the problem?"
                "She takes your cock in her hand, rubbing it softly while she looks into your eyes."
                me "Ya, that's it. If you don't have much time, a blowjob would be best way to take care of it."
                show mom showerhead1 at right
                "She nods and slips to her knees. Without a word she runs her tongue along the bottom of your shaft, then opens her mouth wide and slips you inside."
                me "Oh fuck. That feels great."
                "Mom starts slow, picking up speed as she sucks you off. The warm water from the shower runs over both of you, making the whole experience even better."
                "You lower a hand and brush it along your mom's cheek. She looks up at you with big eyes, sliding your shaft down her throat and back up again a few times."
                "After a moment she pulls off, kissing the tip before speaking again."
                mom "How's that working for you?"
                me "It feels great Mom. Fuck, you look so hot."
                mom "Would it feel better if you guided it yourself? Since we're in the shower I don't mind my, uh, spit getting everywhere."
                me "Lets give it a try and find out."
                show mom showerhead2 at right
                "Mom nods and opens her mouth for you, holding her head still while she looks up at you. You take her head in both hands, tensing your cock to brush it against her face, then slip the tip into her waiting mouth and thrust forward."
                "She takes your cock to the back of her throat like a champ, running her tongue up and down as you go to make it feel even better."
                "You give her a few more slow passes to get comfortable then start to speed up your thrusts."
                "After a few moments you're holding tight onto her head as you face fuck her, slamming yourself down her throat then pulling out to do it again."
                "On each pass her mouth makes loud wet smacking noises, and after a little while she's got a face covered with her own drool as it's flung around."
                "You pull back and tilt her head up to look at you as she pants for breath."
                me "How are you doing?"
                mom "Fine, are you almost there?"
                "You nod, and Mom opens her mouth up wide again."
                mom "Keep going then!"
                show mom showerhead3 at right
                "You slam your shaft back into her mouth and down her throat, holding her head tight against your hips for a few seconds before you start to skull fuck her again."
                me "Fuck, that feels so good. I'm so glad you're a cock hungry slut Mom."
                "If she tries to respond, it's lost in all the wet smacks and gagging as you speed up even more. You can feel your orgasm approaching fast and get ready for it."
                menu:
                    "Cum down her throat.":
                        "A few more thrusts down her wet warm throat and you're ready to cum."
                        me "Here we go! Hope you like it!"
                        "As you start to climax you hold onto her head tight, pushing yourself as far down her throat as you can manage. She coughs once as you fire your semen right into her stomach, but doesn't try and fight you."
                        "When you're done you hold yourself in place for a little bit, then slide out of her throat slowly. On the way out you feel your mom's tongue running over your shaft one last time."
                        mom "Ah... I need to get going..."
                        show mom nightstrip3 at right
                        "Mom gets to her feet and steps out of the shower, grabbing a towel and collecting her clothes."
                        me "Thanks for that Mom, that was great."
                        if momO.cumslut:
                            mom "No, thank you sweetheart. That was a great way to start the day."
                        else:
                            mom "Good, I'm glad you enjoyed yourself. Enjoy your shower."
                        hide mom
                        "She slips out of the bathroom. You feel like you've had a major effect on her today."
                        "A little bit later you head back to your own room and get dressed, with plenty of time left in the morning."
                        $ momO.inc_cum_mouth()
                        $ momO.inc_cum_swallow()

                    "Cum on her face.":
                        "A few more thrusts down her wet warm throat and you're ready to cum."
                        me "Here we go! I'm going to cover your face with it!"
                        show mom showerhead4 at right
                        "As you start to finish you pull out and grab your cock with one hand, using the other to hold your mom's head still while you blast your load over her."
                        "She pants loudly as you cover her in your semen, looking up at you with big eyes."
                        "When you're done you let go of her head and give a contented sigh."
                        if momO.cumslut:
                            mom "Ah... thank you [inputName], this is a great way to start the day. Did you have a good time too?"
                        else:
                            mom "Ah... I hope you had a good time then."
                        show mom nightstrip3 at right
                        "You nod as Mom gets to her feet, facing the shower head while she tries to get herself cleaned up."
                        show mom shower at right
                        "Once she's done that she gets out of the shower, grabbing a towel and collecting her clothes."
                        me "Thanks for that Mom, that was great."
                        mom "No problem. Enjoy your shower."
                        hide mom
                        "She slips out of the bathroom. You feel like you've had a major effect on her today."
                        "A little bit later you head back to your own room and get dressed, with plenty of time left in the morning"
                        $ momO.inc_cum_over()

                    "Cum on her tits.":
                        "A few more thrusts down her wet warm throat and you're ready to cum."
                        me "Here we go! Lets cover those fucking hot tits!"
                        "Mom grunts something and grabs her tits, holding them up for you as you pull out and start to stroke yourself to completion."
                        mom "Just give it all here, I'll take it all from you sweetheart!"
                        show mom showerhead5 at right
                        "You grunt softly as you start to cum, spraying your load all over her tits. She looks up at you and smiles as your semen runs down her cleavage, quickly being washed away by the water."
                        if momO.cumslut:
                            mom "Oh, thank you for giving me so much sweetheart. This is a great way to start the day. Did you have a good time too?"
                        else:
                            mom "Ah... I hope you had a good time then."
                        show mom nightstrip3 at right
                        "You nod as Mom gets to her feet, facing the shower head while she tries to get herself cleaned up."
                        show mom shower at right
                        "Once she's done that she gets out of the shower, grabbing a towel and collecting her clothes."
                        me "Thanks for that Mom, that was great."
                        mom "No problem. Enjoy your shower."
                        hide mom
                        "She slips out of the bathroom. You feel like you've had a major effect on her today."
                        "A little bit later you head back to your own room and get dressed, with plenty of time left in the morning"
                        $ momO.inc_cum_over()
                $ momO.inc_blow()
                $ momO.change_slut_rebalanced(action_difficulty)
                $ momO.change_resist(mom_bathroom_event_object.get_resist_change(4))
                $ mom_bathroom_event_object.inc_level(4)
            else:
                #Failure
                mom "I really have to get ready for work [inputName]."
                me "We'll do it while we shower, it won't take any time at all."
                "She plays with the bottom of her shirt, pulling up the edge then smoothing it down again."
                mom "If it's really that bad for you, how about I just let you have a few minutes to yourself."
                me "Come on, it's no big deal."
                "She shakes her head and steps over to the door."
                mom "No. Now just come let me know when you're done, okay?"
                "She's got a sharper look in her eye now. You must have pushed her too far and she's resisted the serum."
                me "No, it's fine then. Just have your shower."
                "You walk past your mom and leave. She hesitates for a second, then closes the door and starts the shower."
                "You wait in your room until she's done, knowing you could have done more if you hadn't been so aggressive."
                $ momO.change_slut_failed()
                $ momO.change_resist(mom_bathroom_event_object.get_resist_change(0))
                $ mom_bathroom_event_object.inc_level(0)

        "Fuck her in the shower.":
            $ action_difficulty = 60
            $momO.set_action_cumslut()
            $momO.set_action_freeuse()
            "You turn to your mom and pull your pants down, revealing your hard cock."
            me "I know you're in a rush to get ready for work, but I really need you to take care of this for me Mom."
            "Your mom takes a step back and stares at your erect penis, not saying anything."
            me "How about we get into the shower and I'll slip it inside you."
            if momO.check_willing(action_difficulty):
                #Success
                mom "I... If we hurry we should have time."
                show mom nightstrip3 at right
                "She starts to strip down right away, and you do the same. Once you're both naked she gets into the shower and starts the water, adjusting it so it's a comfortable temperature."
                "You step into the shower behind her, brushing your hard cock against her ass."
                me "I won't waste any time, I know you're in a hurry."
                show mom showerfuck1 at right
                "Mom nods and spreads her legs, planting her hands on the wall underneath the shower head. You hold your cock in one hand and run the tip up and down her slit, feeling how wet she already is."
                "With one smooth motion you slip inside your mom, sliding all the way to the back of her tight pussy before pausing, then pulling out. She moans loudly and presses her hips against yours."
                mom "Oh god [inputName]..."
                "You settle into a steady rhythm, holding onto her hips with both hands to make sure you don't slip."
                me "Do you like that?"
                mom "Mmmhm. You feel so big and warm."
                me "Good, I want you to have a good time too."
                "You give her a few fast thrusts, making her ass jiggle as you bump your hips against it. She gasps and moans as you slide in and out of her."
                "For a few minutes the only sound is the splashing of the running water, the slaps of you slamming into her ass cheeks, and your mom's loud moans."
                mom "Oh fuck... I think, I think I'm going to cum soon."
                me "Fuck ya. Cum for me Mom, cum like a dirty little slut while I fuck you."
                "Mom moans in response again, slapping her hand against the tile wall a few times."
                "She takes a sudden breath and arches her back, legs shaking while she orgasms. You keep going, fucking her pussy while it's most sensitive and enjoying the way she gets tighter when she cums."
                mom "Ahhh! Fuck! Ahhhh....."
                "Watching her climax pushes you over the edge, and you give a few more thrusts as you get ready to match her orgasm with your own."
                menu:
                    "Cum inside of her.":
                        me "Here I cum! Enjoy it you fucking cum slut!"
                        "Mom just moans as you hold yourself balls deep and start to unload inside of her. Her pussy twitches gently around your shaft as you finish."
                        show mom showerfuck3 at right
                        "For a moment both of you just pant, then you slip out of her and step back, watching as your cum drips out of her cunt and is washed away."
                        $ momO.inc_cum_inside()


                    "Cum in her mouth.":
                        me "I'm going to cum! I want you to take it in your mouth like a good cum slut!"
                        "Mom just moans in response as you pull out. She drops to her knees and opens her mouth for you as you stroke yourself off, the tip of your cock resting on her lips."
                        show mom showerfuck4 at right
                        "You fire your entire load off inside of her mouth, then watch as she opens wide and lets you see."
                        "After lettting you enjoy the view for a few seconds she turns to the side and spits your cum out down the drain, then looks back up at you."
                        $ momO.inc_cum_mouth()

                    "Cum on her ass.":
                        me "I'm going to cum! I'm going to cover you like the cum slut you are!"
                        show mom showerfuck2 at right
                        "Mom just moans in response as you pull out. You grab your cock and stroke yourself off as you fire your load over her ass cheeks and lower back."
                        "When you're done you both spend a few moments panting to catch your breath. You watch as the shower starts to wash your semen off of her almost immediately."
                        $ momO.inc_cum_over()

                mom "I... ah, I'm glad you had a good time. I think I'm going to need the shower for a little longer to get cleaned up."
                me "Sure. I think I'm done anyway."
                "You grab a towel and collect your clothes, heading back to your room confident you've had a major effect on her. Once you're dressed you still have plenty of time left in the morning."
                $ momO.inc_sex()
                $ momO.change_slut_rebalanced(action_difficulty)
                $ momO.change_resist(mom_bathroom_event_object.get_resist_change(5))
                $ mom_bathroom_event_object.inc_level(5)
            else:
                #Failure
                mom "I... I don't think so [inputName]."
                me "Come on mom, you can't leave me like this."
                "She stares at your shaft for a few seconds, then shakes her head."
                mom "No, I need to get ready for work. Just go to your room and take care of it."
                "She's got a sudden sharp look in her eye, and her tone leaves no room for confusion. You must have been too aggressive and she's resisted the serum."
                me "Fine, sure. Have a good shower."
                "You pull your pants up and leave. Mom locks the door behind you, and you hear the shower start up shortly after."
                "You wait in your room until she's done, knowing you could have accomplished more if you didn't push her so far."
                $ momO.change_slut_failed()
                $ momO.change_resist(mom_bathroom_event_object.get_resist_change(0))
                $ mom_bathroom_event_object.inc_level(0)

    jump jumpTimeStay

label maj_mom_beach:
    $ mom_beach_event_object.happened = True
    $temp_slut_score = 0
    call serum_give(momO) from _call_serum_give_23
    $ temp_slut_score = _return
    "You pull out some serum and mix it into your mom's drink before taking the tray of food up to her."
    mom "Thank you [inputName], I could feel myself fading."
    me "No problem. Dig in!"
    "The two of you have lunch, chatting a little between bites. You wait until Mom has finished her drink."
    me "Hey Mom, I think I forgot something up by the change rooms earlier today. Would you mind comming with me while I check?"
    "Mom looks at you, eyes slightly unfocused, and nods."
    mom "Sure, if you'd like me to."
    "You lead Mom up to the change rooms, finding them mostly empty at this time of day. You pick the stall farthest away from the parking lot and open up the curtain to it."
    me "Hmm, I guess I was wrong. Nothing here. While we've got a moment though, there's something else I wanted to do."
    mom "What's that? I'll help however I can."
    menu:
        "Have her strip for you.":
            $ action_difficulty = 0
            $momO.set_action_exhib()
            $momO.check_willing(action_difficulty)
            "You give your mom a look up and down, appreciating the way her swimsuit shows off her body."
            me "I've been looking at you all day, and I just can't stop thinking about how good you look. Could you please give me a better look?"
            "Mom thinks about it for a moment, glancing at the bulge in your swimsuit, then nods."
            mom "Come in here."
            "She steps into the changing room and closes the curtain behind you."
            show mom strip36 at right
            if slut_outfit:
                "You watch while she quickly pulls off her top, then slides the bottom of her small bikini down."
            else:
                "You watch while she slides the straps of her swimsuit over her shoulders, then pulls the entire piece down and off. She steps out of it and pushes it to the side."
            mom "Here you go, is this everything you wanted to see?"
            show mom strip37 at right
            $ momO.inc_naked()
            "She turns, letting you take a look at her butt as well."
            me "Yeah, it is. You look great Mom."
            show mom strip36 at right
            "She turns back to you and smiles. One of her feet plays with the sand idly while she stands naked."
            mom "Thank you. I'm glad you think so."
            "You enjoy looking at her for a few more moments, then speak up again."
            me "I think I've seen enough for now. Lets head back to the table."
            if slut_outfit:
                show mom swim2 at right
            else:
                show mom swim1 at right
            "Mom reaches down and grabs her swimsuit. She puts it back on, then steps out of the changing room."
            "The two of you return to the picnic table and sit down again. You chat for another half hour, letting the serum wear off completely. You feel like you had a major effect on her here."
            $ momO.change_slut_rebalanced(action_difficulty)
            $ momO.change_resist(mom_beach_event_object.get_resist_change(1))
            $ mom_beach_event_object.inc_level(1)

        "Have her pose while you masturbate.":
            $ action_difficulty = 15
            $momO.set_action_exhib()
            "You give your mom a look up and down, appreciating the way her swimsuit shows off her body."
            me "I've been looking at you all day and it's driving me crazy. I need to blow off some steam, and I was hoping you could pose for me a little and help me with that."
            if momO.check_willing(action_difficulty):
                "Mom glances at the bulge in your swim trunks, then nods and steps into the changing room."
                mom "Come in here and lets see what I can do for you."
                "You follow behind her and close the curtain behind you."
                mom "Pull your pants down and do what you have to do sweetheart. I'll try and help you out."
                show mom strip36 at right
                if slut_outfit:
                    "Mom smiles at you and pulls her top up, letting her tits fall free. She pulls it over her head and drops it to the sand, then hooks the waist of her bikini bottom and pulls it down too."
                else:
                    "Mom smiles at you and slides the straps of her swimsuit over her shoulders. She pulls it down past her tits, letting them fall free, then all the way to the ground. She steps out of it and slides it to the side."
                me "Wow, you look great Mom."
                "You pull your own swimsuit down and let your hard cock spring free. Mom watches it bounce up and down a few times, then looks away."
                "You take your shaft in your hand and start to stroke it slowly, letting your eyes roam up and down your mom's naked body."
                mom "What would you like me to do now?"
                me "Turn around and spread your legs a little."
                show mom strip38 at right
                $ momO.inc_naked()
                "She does so, placing the palms of her hands against the far wall and bending forward. The changing room is small, and your cock is almost touching her ass while you jerk yourself off."
                me "Ah, perfect. Now tell me that you're a dirty slut."
                if momO.slut_score < 60 and not momO.exhib:
                    mom "What? Don't say that about your mother [inputName]."
                    me "It's just to get me in the mood, so I finish faster. I know it's not true Mom."
                    "She glances over her shoulder, staring at your cock before turning back."
                mom "I'm a dirty slut who's letting my son jerk off while watching me."
                me "That's right, you are. Turn around again, I want to see your tits."
                show mom strip39 at right
                "She spins around and leans back, placing her shoulders on the wall and thrusting her hips out at you. She spreads her legs, giving you a good look at her pussy."
                mom "I'm a filthy whore of a mother, who just wants her son to cum all over her."
                "You stroke yourself off faster, completely absorbed in your mother's show."
                mom "Will you cum for me [inputName]? Will you give me what I want and cum all over me?"
                me "Fuck, yeah I will! Here I cum!"
                show mom strip40 at right
                $ momO.inc_cum_over()
                "You grip your cock tightly as you orgasm, firing your load onto your Mom. She gasps softly as your hot semen lands on her chest, stomach, and legs."
                mom "Oh sweetheart. Wow..."
                "You pull your swim trunks back up and take a good long look at your Mom while she's covered in your load."
                me "That was great Mom. Thank you."
                if slut_outfit:
                    show mom swim2 at right
                else:
                    show mom swim1 at right
                "She nods and bends over to pick her swimsuit up off the ground. With nothing else around, she uses the inside of the swimsuit to wipe your cum off of her, then puts it back on."
                mom "I'm glad you had a good time. Should we head back to the table now?"
                me "That seems like a good idea."
                "The two of you leave the changing room and head back to the picnic table. You sit down again and chat while you wait for the serum to wear off completely. You feel like you had a major effect on her here."
                $ momO.change_slut_rebalanced(action_difficulty)
                $ momO.change_resist(mom_beach_event_object.get_resist_change(2))
                $ mom_beach_event_object.inc_level(2)

            else:
                "Mom glances at the bulge in your swim trunks and thinks for a long moment."
                mom "You want me to show off while you... masturbate?"
                me "That's right Mom. It would be a huge help."
                mom "I don't know [inputName]. I'm your mother, it doesn't seem right."
                me "We won't be hurting anyone. It'll just take a few moments, then we can get back to the beach."
                "She thinks a few seconds longer, then shakes her head."
                mom "No, it isn't right. If you need to... take care of yourself you can do it in there. I'll wait for you back at the table."
                "From the look in her eye and tone of her voice you can tell she's resisted the serum. Maybe you pushed her too far this time."
                me "I'm sorry Mom. Lets just forget I said anything about it."
                "She nods, and the two of you return to the picnic table. You chat a little, spending half an hour there until the serum has worn off completely."
                $ momO.change_slut_failed()
                $ momO.change_resist(mom_beach_event_object.get_resist_change(0))
                $ mom_beach_event_object.inc_level(0)

        "Have her give you a handjob.":
            $ action_difficulty = 30
            $momO.set_action_cumslut()
            "You give your mom a look up and down, appreciating the way her swimsuit shows off her body. You rub the bulge in your shorts a little bit, drawing Mom's eyes to them."
            me "I've been looking at you all day and it's been driving me crazy. You're so hot, I need to blow off some steam before I can do anything else. Do you think you could lend a hand and help me out with that?"
            mom "How could I do that?"
            me "A quick handjob would be perfect."
            if momO.check_willing(action_difficulty):
                "Mom glances at the bulge in your swim trunks, then nods and steps into the change room."
                mom "Come in, lets see what I can do about that."
                "You step in with her, and she closes the curtain."
                mom "You just lean against that wall and leave everything else to me, okay?"
                me "Okay Mom. Thank you."
                "You lean against one of the thin wooden walls while your mother gets onto her knees in front of you. She reaches for the waist of your swimsuit and pulls it down past your cock, gasping a little as it springs free."
                mom "Oh my. You really do need some help, don't you?"
                if slut_outfit:
                    show mom hand19 at right
                else:
                    show mom hand18 at right
                $ momO.inc_hand()
                "You stay quiet as she takes your shaft in her hand, gently rubbing up and down it's length."
                mom "There we go. Just relax and enjoy, I'll do my best with this."
                "She reaches her other hand up and cups your balls, massaging them gently while she strokes you off. The feeling sends shivers up your spine."
                mom "I want you to warn me before you finish, okay sweetheart?"
                me "Okay Mom. That feels amazing."
                "She smiles and speeds up her strokes, pausing only to spread your precum around. Soon your whole shaft is wet, and her hand makes soft wet noises as it slides up and down."
                "Soon after you feel your orgasm approaching, a growing tightness in your balls."
                me "I'm almost there Mom. Ah..."
                mom "Good, I want you to let it all out for me, okay? Don't hold anything back."
                "She angles your cock almost straight up and strokes you as fast as she can manage. She keeps going as you climax, spraying your cum straight up into the air so it comes back down and lands on her arms and hands."
                mom "That's a good boy, let it all out."
                "You shiver with pleasure as she keeps going, hand gliding over your wet, sensitive dick."
                me "Oh god Mom, that's enough!"
                "She finally slows down, then lets go completely."
                mom "There, all taken care of. I hope you feel better now [inputName]."
                me "I do Mom, thank you."
                if slut_outfit:
                    show mom swim2 at right
                else:
                    show mom swim1 at right
                "Mom wipes her arms off in the sand, cleaning off your semen as best she can before standing up."
                mom "Should we head back to the table now?"
                me "Seems like a good idea."
                "The two of you leave the changing room and head back to the picnic table. You sit down again and chat while you wait for the serum to wear off completely. You feel like you've had a major effect on her here."
                $ momO.change_slut_rebalanced(action_difficulty)
                $ momO.change_resist(mom_beach_event_object.get_resist_change(3))
                $ mom_beach_event_object.inc_level(3)


            else:
                "Mom stares at your bulge while you rub it slowly. She thinks for a long moment before responding."
                mom "You want me to... give you a handjob right here?"
                me "That's right Mom. It would be a huge help."
                mom "I don't know [inputName]. I'm your mother, it doesn't seem right."
                me "We aren't hurting anyone. You're just a loving mother helping out her son, right?"
                "She thinks about it for a few more seconds, then shakes her head."
                mom "No, it wouldn't be right. If you need to take care of that you can do it in there yourself. I'll wait for you back at the table, and we won't say any more about it."
                "From the look in her eye and tone of her voice you can tell she's resisted the serum. Maybe you pushed her too far this time."
                me "I'm sorry Mom. Lets just forget that I said anything about it."
                "She nods, and the two of you return to the picnic table. You chat a little, spending half an hour there until the serum has worn off completely."
                $ momO.change_slut_failed()
                $ momO.change_resist(mom_beach_event_object.get_resist_change(0))
                $ mom_beach_event_object.inc_level(0)

        "Have her blow you.":
            $ action_difficulty = 45
            $momO.set_action_cumslut()
            $momO.set_action_freeuse()
            "You give your mom a look up and down, appreciating the way her swimsuit shows off her body. You rub the bulge in your shorts, drawing Mom's eyes to them."
            me "I've been looking at you all day, you're so hot and it's driving me crazy. I need you to come in here and help me blow off some steam."
            if momO.check_willing(action_difficulty):
                "Mom looks at the bulge in your swim trunks for a few moments."
                mom "You would like me to give you a blowjob?"
                me "Yeah, that would be great."
                "She nods and steps into the change room."
                mom "Come in, lets see if I can't take care of that for you."
                "You step in with her, and she closes the curtain."
                mom "You just lean against that wall and leave everything else to me, okay?"
                me "Okay Mom. Thank you."
                "You lean against one of the thin wooden walls while your mother gets onto her knees in front of you. She reaches for the waist of your swimsuit and pulls it down past your cock, gasping as it springs free."
                mom "It looks so big. I hope I can fit it all in my mouth."
                if slut_outfit:
                    show mom blow24 at right
                else:
                    show mom blow23 at right
                $ momO.inc_blow()
                "She holds it still with one hand and starts to lick it, running her tongue from the base to the tip before starting over again. After a few passes she's gotten you completely wet."
                "With that done, she sits up a little and slides you between her lips. She bobs her head forwards and backwards a little, going a little deeper each time."
                me "Oh god Mom, that feels amazing."
                if slut_outfit:
                    show mom blow26 at right
                else:
                    show mom blow25 at right
                "She says something, the sound muffled by your cock in her mouth, and speeds up. After a few minutes she's taking your full length down her throat on each pass."
                "She takes you particularly deep and holds herself there for a few seconds, then slides off with a wet pop and looks up at you."
                mom "Are you going to finish soon sweetheart? I could feel you twitching."
                me "I think so Mom."
                mom "Good. I don't have anything to get cleaned up with so just finish in my mouth, okay?"
                "Before you can respond she slides you back down her throat, blowing you quickly and deeply."
                "It's not long before she brings you to climax. You tap her on the shoulder, and she slides your tip back so it's just inside of her lips."
                "She jerks you off with one of her hands, gasping in suprise as your first pulse of cum lands across her tongue."
                $ momO.inc_cum_mouth()
                if momO.cumslut:
                    $ momO.inc_cum_swallow()
                    if slut_outfit:
                        show mom swim2 at right
                    else:
                        show mom swim1 at right
                    "Mom keeps you in her mouth until you've finished cumming, then slides off carefully. She tilts her head up and starts to drink down your semen, taking a few big gulps to swallow it all."
                    me "Fuck that felt good Mom."
                    "Your mom licks her lips and sighs contently."
                else:
                    if slut_outfit:
                        show mom blow28 at right
                    else:
                        show mom blow27 at right
                    "Mom keeps you in her mouth until you've finished cumming, then slides off carefully. She leans to the side and opens her lips, letting your semen out in a long thin stream."
                    me "Fuck, that felt good."
                    "Mom spits out the last of your sperm into the sand and looks up at you, smiling."
                mom "Good, I'm really glad you had a good time. Should we get back to the table now?"
                me "That seems like a good idea."
                if slut_outfit:
                    show mom swim2 at right
                else:
                    show mom swim1 at right
                "You pull up your swim suit, and the two of you leave the changing room to head back to the picnic table. You sit down again and chat while you wait for the serum to wear off completely. You feel like you've had a major effect on her here."
                $ momO.change_slut_rebalanced(action_difficulty)
                $ momO.change_resist(mom_beach_event_object.get_resist_change(4))
                $ mom_beach_event_object.inc_level(4)

            else:
                "Mom stares at your bulge for a few seconds before responding."
                mom "How would you want me to help?"
                me "I was thinking you could suck me off. That should have me cumming pretty quickly."
                mom "Oh god [inputName], really? I'm your mother, I don't think that's okay."
                me "We wouldn't be hurting anyone. You would just be helping your son out."
                "She pauses, then pulls her gaze away from your obvious erection and looks you in the eye."
                mom "No, it wouldn't be right. You can go in there and do whatever you have to do. I'll wait for you back at the table, and won't say a word about it again."
                "From the look in her eye and tone of her voice you can tell she's resisted the serum. Maybe you pushed her too far this time."
                me "I'm sorry Mom. Lets just forget that I said anything about it."
                "She nods, and the two of you return to the picnic table. You chat a little, spending half an hour there until the serum has worn off completely."
                $ momO.change_slut_failed()
                $ momO.change_resist(mom_beach_event_object.get_resist_change(0))
                $ mom_beach_event_object.inc_level(0)

        "Fuck her.":
            $ action_difficulty = 60
            $momO.set_action_cumslut()
            $momO.set_action_freeuse()
            "You give your mom a look up and down, appreciating the way her swimsuit shows off her body. You rub the bulge in your shorts, drawing Mom's eyes to them."
            me "I've been looking at you all day and it's been driving me crazy. I want to strip you out of that swimsuit and fuck you."
            if momO.check_willing(action_difficulty):
                #Include public section if applicable
                "Mom reaches out and rubs the bulge in your swim trunks, feeling the shape of your erection."
                mom "Oh sweetheart. Come in here and let me take care of that for you."
                "You both step inside the change room, and she closes the curtain behind her."
                mom "You should have told me earlier you were this worked up. I'm sure I could have done something for it."
                show mom strip36 at right
                if slut_outfit:
                    "Mom reaches behind her and undoes her bikini top. She lets it fall to the sand, then grabs the bottoms and pulls them down as well."
                else:
                    "Mom slides the straps of her swimsuit over her shoulders, then pulls the whole thing down and off. She kicks it to the side of the change room and stands in front of you, naked."
                me "It's okay Mom, we can take care of it right now."
                show mom fuck46 at right
                $ momO.inc_sex()
                "Mom nods and turns around, placing her hands on the far wall. She spreads her legs a little, giving you a good look at her pussy."
                "You pull your own swimsuit down and off, then step up behind your mom. You bounce your cock off of her ass cheeks a few times, then rub its tip against her wet slit."
                mom "Use me however you want [inputName]. I just want you to feel good."
                "You hold onto her hips and push forward, plunging your full length into her cunt. Mom gasps, then rocks her hips against your so help you get even deeper."
                me "God that feels good. You're already drenched Mom."
                "You start the trust back and forth, fucking her from behind."
                mom "I know, I wanted you too. Keep going, please!"
                "You settle into a steady rhythm, sliding your cock in and out of your mom's pussy. She moans softly as you fuck her, obviously enjoying herself too."
                "After a few minutes you feel your orgasm starting to build. You speed up, enjoying yourself as much as you can before you climax."
                menu:
                    "Cum inside of her.":
                        me "Fuck, I'm going to cum Mom!"
                        mom "Do it, cum for me sweetheart!"
                        "You give her a few quick thrusts, then pull back on her hips and push yourself as deep into her as you can manage. She gasps loudly as you start to pump her full of your hot cum."
                        mom "Oh god, [inputName]..."
                        show mom fuck47 at right
                        $ momO.inc_cum_inside()
                        "You take a few more short thrusts, then step back and pull out. Your mom stays leaning against the wall for a few seconds, still catching her breath."
                        mom "It's so warm... Ah..."
                        me "Thanks Mom, that felt amazing."
                        "When she's regained her strength she stands up, your cum still trickling down her leg, and collects her swimsuit."
                        mom "I hope this will keep it all inside for a little bit..."
                        if slut_outfit:
                            show mom swim2 at right
                        else:
                            show mom swim1 at right
                        "She pulls the swimsuit back on, pausing for a moment to get her tits properly in position."
                        mom "I suppose we should head back to the table now."
                        me "That sounds like a good idea."

                    "Cum on her ass.":
                        me "Fuck, I'm going to cum Mom!"
                        mom "Do it, cum for me sweetheart!"
                        show mom fuck48 at right
                        $ momO.inc_cum_over()
                        "You give her a few quick thrusts, then step back and pull out with a wet pop. You stroke yourself off as you cum, spraying her ass and back with your hot semen."
                        mom "Oh god, that's right. Cover me with it..."
                        "You wait until you're completely finished, then wipe the last few drops off on her ass cheek."
                        me "Thanks Mom, that felt amazing."
                        "She peeks over her shoulder, looking at your sperm all over her butt."
                        mom "There's so much of it, and it's so warm..."
                        if slut_outfit:
                            show mom swim2 at right
                        else:
                            show mom swim1 at right
                        "She takes a few seconds to catch her breath, then stands up and collects her swimsuit. She uses the inside of it to wipe up your cum, then slides it on again."
                        mom "I suppose we should head back to the table now."
                        me "That sounds like a good idea."

                "The two of you return to the picnic table and chat for a little while. You spend half an hour there until the serum has worn off completely."
                $ momO.change_slut_rebalanced(action_difficulty)
                $ momO.change_resist(mom_beach_event_object.get_resist_change(5))
                $ mom_beach_event_object.inc_level(5)

            else:
                "Mom stares at your bulge for a few seconds before responding."
                mom "You want to... have sex with me?"
                me "That's right. I'm so horny right now, I need you to take care of me."
                mom "But... I'm your mother [inputName]. We can't do that. Can we?"
                me "We aren't hurting anyone. You would just be taking care of your son in the best way you can."
                "She thinks about it for a few more seconds, making circles in the sand with one of her feet. Finally she looks you in the eye and shakes her head."
                mom "No, it wouldn't be right. If you need to take care of that you can do it in there yourself. I'll be back at the table, I won't ask any questions when you get back."
                "From the look in her eye and tone of her voice you can tell she's resisted the serum. Maybe you pushed her too far this time."
                me "I'm sorry Mom. Lets just forget that I said anyting at all."
                "She nods, and the two of you return to the picnic table. You caht a little, spending half an hour there until the serum has worn off completely. You feel like you've had a major effect on her here."
                $ momO.change_slut_failed()
                $ momO.change_resist(mom_beach_event_object.get_resist_change(0))
                $ mom_beach_event_object.inc_level(0)


    return

#######################
##Nora's Major Scenes##
#######################

label maj_blueberryEvent:
    $ blueberry_event_object.happened = True
    $ temp_slut_score = noraO.get_serum_result("blue")
    "You begin the preparations for the serum. Slipping materials out of supply cabinets, turning on machines as you're cleaning them."
    hide steph
    show nora work at right
    nora "[inputName]? What are you doing?"
    "You jump as Nora appears behind you."
    me "What? Oh, nothing. Just a little science experiment I read about online."
    nora "Oh? And what does it do?"
    "Thinking fast, you improvise."
    me "It produces a bright blue liquid that tastes like... blueberry."
    nora "That's all? You should know it's not safe to taste substances made in a lab."
    me "It's perfectly harmless. I tried it already at home, but the supplies we have here are so much better. I was going to make you and Stephanie a blueberry surprise."
    nora "That's nice of you. Alright, you've got ten minutes to get this done then it's back to work."
    me "Right, sure thing."
    "Nora leaves you to work at the bench. Heart pounding you follow the instructions for your serum, producing a small vial of vivid blue liquid."
    "Nora comes back over to investigate."
    nora "So this is it?"
    "You nod."
    me "It tastes just like blueberry, you'll swear it's the same thing."
    "Nora looks at you sternly."
    nora "Now remember, you should never drink or eat something made in a lab."
    "She smiles."
    nora "But one exception can't hurt. Besides, you say you've made it before."
    "You nod."
    nora "Alright, lets give it a try."
    call resistance_gain_report(blueberry_event_object,noraO) from _call_resistance_gain_report_17
    "She puts the vial next to her mouth and tilts it back. She smacks her lips a few times and scowls."
    nora "I think you might have done it wrong, that didn't taste like blueberry at all..."
    "Her pupils dialate slightly and look off into the distance. It must be working."
    me "Nora, can you hear me?"
    nora "Of course I can [inputName]."
    me "Excellent."
    "A quick glance around the lab shows that Stephanie is out for supplies right now. It's just you and Nora."
    menu:
        "Have her take off her shirt.":
            $ action_difficulty = 0
            $noraO.set_action_exhib()
            $noraO.check_willing(action_difficulty)
            me "You've got such awesome tits, it's a shame to keep them hidden away. How about you take your shirt off?"
            "Nora nods slowly."
            if noraO.exhib:
                nora "Sure. I love being able to show off for someone who appreciates a good pair of tits."
            else:
                nora "Sure, that sounds like fun. We're always so bunched up around here with our clothes and our labcoats. About time we had some fun."
            "She shrugs off her labcoat and lifts up the sweater underneath. Her breasts spring out at you, barely contained by a practical and form fitting bra."
            show nora strip1 at right
            me "Wow."
            "Nora smiles."
            nora "Do you like what you see?"
            show nora strip2 at right
            "She leans forward, pinching her breasts between her biceps."
            if noraO.exhib:
                nora "There was a meeting with the rest of the department yesterday. I guess my shirt had shrunk a little because it was tigher than normal, and really showed off my breasts."
                "Nora places her hands under her tits and lifts them slightly, then lets them drop. They bounce and jiggle around."
                nora "The guys were staring at them the whole time. I could see how badly they wanted them."
                me "You should let them have them next time. It sounds like a good time."
                nora "Hmm, I'll think about it and see what I can do."
                me "It would certainly be great for morale."
            else:
                nora "I never get to do this kind of thing with anyone. I'm always worried people will see how large my chest is, or notice my nipples. It's great to finally let loose."
                "You wonder if she fantasied about this kind of thing before."
                "Nora places her hands under her tits and lifts them slightly, then lets them drop. They bounce and jiggle around."
                me "You should let loose more often. There's nothing wrong with showing off a little bit of cleavage."
                nora "You think so? I worry it might make me look less professional."
                "You try hard not to laugh when she says that. She's squeezing her tits together with her palms and staring down at her own cleavage."
                me "I think it would be fine. Great for morale in fact."
            show nora strip3 at right
            $ noraO.inc_naked()
            "She nods."
            me "Okay, you should probably get dressed before Stephanie gets back."
            nora "Alright, thanks again [inputName]. This really helped me relax."
            me "No problem at all."
            "Nora puts her lab coat back on, tugs her sweater back into place, and heads back to work."
            "You're rock hard, but you'll have to wait until you get home to take care of it. You're also certain you made a lasting impression on Nora."
            $ noraO.change_slut_rebalanced(action_difficulty)
            $ noraO.change_resist(blueberry_event_object.get_resist_change(1))
            $ blueberry_event_object.inc_level(1)
        "Have her get naked for you.":
            $ action_difficulty = 10
            $noraO.set_action_exhib()
            me "I've always wondered what you look like naked. You look so hot I just want to tear your clothes off. How about you give me a show."
            if noraO.check_willing(action_difficulty):
                "Nora nods."
                nora "Sure thing. I've seen how you look at me, it's cruel to keep you in suspense."
                "Nora grabs her labcoat and throws it on a chair. Then she turns around and pulls her sweater off too."
                show nora strip1 at right
                nora "I learned this when I was younger, lets see if I can still do it."
                "She places her hands on her hips, loops her thumbs through her waistband, and begins bending over with her legs straight."
                "Her pants hit the floor, and she's holding onto her ankles, amazing ass high in the air."
                show nora strip4 at right
                $ noraO.inc_naked()
                nora "Like what you see?"
                "She shakes her ass back and forth at you for a moment."
                me "Oh ya, you're gorgeous."
                "Nora stands up slowly, turns around, and smiles."
                if noraO.exhib:
                    nora "Mmm, I love doing this for people. It's so nice to be watched."
                else:
                    nora "You're too sweet. It's been a while since I got to do this for a man."
                "She reaches behind her back and thumbs the clasp of the bra. When it comes undone, she slides her hands forward until they're on her tits and holding the cups in place."
                nora "Ready?"
                "You nod."
                "She drops her hands down, taking the cups with them and revealing her perfectly shaped breasts. She shakes left and right slightly, bouncing them for you."
                "Next, she grips her underwear by both hands and begins leaning forward as her hands slide it down. Her tits dangle from her chest and sway back and forth as she looks at you and smiles."
                me "Wow."
                nora "Thank you."
                "Nora stands back up, completely naked with her underwear in one hand. Her nipples are standing on end, and she's starting to blush heavily. Maybe the drug is wearing off already. You better end this quick."
                show nora strip5 at right
                me "You look incredible Nora. You should really show that body of yours off around the office a little more."
                if noraO.freeuse:
                    nora "I think you're right. Maybe I'll give the other men a few ideas."
                else:
                    nora "Oh I shouldn't. The men might get ideas."
                    me "Well, how about just here at the lab then, loosen up a bit when you're around me. I'd love to get to see your tits more often."
                    "She smiles, eyes slightly unfocused."
                    nora "I'd like that, it feels so hot to have you watching me."
                    "She reaches down with one hand and spreads her lips. You can tell she's soaking wet."
                    me "Feel free to show off to me whenever you want Nora, it'll be our secret."
                me "Now, you should get dressed before Stephanie shows back up."
                "Nora nods and begins gathering her clothes. In a few minutes she's fully dressed again and back to work."
                "You're painfully hard, but you'll have to wait until you get home to take care of it. You're also certain you made a lasting impression on Nora."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ noraO.change_resist(blueberry_event_object.get_resist_change(2))
                $ blueberry_event_object.inc_level(2)
            else:
                #Resists
                "Nora nods slowly."
                nora "I've never done this in the lab before."
                "Her labcoat hits the floor, her tits are contained only by a sweater. Her hands reach for the bottom of it."
                nora "I guess because I'd lose my job if I got caught."
                "She pulls her sweater up to her boobs. You can see the bottom of her bra."
                "She hesitates."
                nora "Actually, if someone walked in right now we'd both be in a lot of trouble."
                me "No I'm sure we'll be fine."
                "Her hands lower, putting the sweater back in place."
                nora "I don't think it's worth the risk. Maybe later [inputName]"
                "It must have been too large a jump, she's resisted it."
                me "Alright, that's fine. Maybe later."
                "The serum must have had some sort of effect, but you doubt you used it to it's fullest potential."
                $ noraO.change_slut_failed()
                $ noraO.change_resist(blueberry_event_object.get_resist_change(0))
                $ blueberry_event_object.inc_level(0)
        "Put her on her knees and have her blow you.":
            $ action_difficulty = 35
            $noraO.set_action_cumslut()
            $noraO.set_action_freeuse()
            me "I'm feeling awfully distracted by my erection. Could you suck me off to get rid of it?"
            if noraO.check_willing(action_difficulty):
                nora "Of course. It's only fair if I'm the one causing it."
                "She smiles and walks over to you, then drops to her knees."
                nora "I am the one causing it, right?"
                "She looks you right in the eyes. You can feel her breasts pressing against your legs, and her hands drift to your waist."
                me "Oh ya, you're definitely the cause."
                "Nora undoes your fly and reaches a hand into your underwear. Her hands are warm and soft as they drift up and down your shaft."
                me "Oh wow."
                nora "We haven't even gotten started yet."
                "She pulls your pants down, grabs the waistband of your underwear, and pops your cock out into the open."
                nora "There we are!"
                show nora blow1 at right
                $ noraO.inc_blow()
                "She ducks her head down low, sticks her tongue out and licks along the shaft. Your body shivers with tingles as she approaches the tip."
                "She looks up at you, locking eyes as her mouth wraps around the tip. Then, slowly, she lowers her head onto your shaft."
                "Inch by inch your cock disappears into her mouth as she stares into your eyes. Her nose touches your stomach, and she pauses. She shakes her head left and right slightly, then bobs up and down a little."
                "Finally, she pulls back suddenly and gasps for air."
                nora "Guah aha aha aha"
                "Before you can say anything she plants your cock back in her mouth and slides it back and forth. You notice her other hand has drifted to her waist and slipped into her pants."
                me "Oh man, that's incredible."
                "Nora responds by speeding up. You can feel her tongue along the bottom of your cock as you slide back and forth."
                "After a few minutes of blissful pleasure you're approaching climax."
                me "I'm going to cum soon."
                "Nora pulls off your cock after one last dip."
                nora "We can't get my uniform dirty. Cum in my mouth."
                "You didn't even have to ask."
                "She throws her mouth back on your cock, devouring it hungrily."
                "You feel yourself getting closer, and she's not slowing down."
                "Finally, you're right at the edge. She bobs her head back and forth on the tip, keeping it in her mouth."
                $ noraO.inc_cum_mouth()
                me "Take it!"
                "She does. You cum into her mouth and feel her tense up on your cock."
                "She slides down your shaft one last time before taking it out. Your sensitive cock sends shivers down your spine."
                $ noraO.inc_cum_swallow()
                "With a POP! she lets you go, swallows quickly, and stands up."
                if noraO.cumslut:
                    nora "Mmm, thank you [inputName]. You tasted amazing. you really didn't hold anything back."
                    me "Neither did you, and I know how much you like to taste my cum."
                    "She smiles and licks her lips."
                else:
                    nora "Wow, you really didn't hold back."
                    me "Neither did you."
                    "She smiles and nods."
                nora "I've got work to get back to, you should be able to continue undistracted now."
                me "Of course."
                "You're certain you made a lasting impression on Nora. She seems to shake her ass at you a little as she walks away."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ noraO.change_resist(blueberry_event_object.get_resist_change(3))
                $ blueberry_event_object.inc_level(3)
            else:
                #Resists
                "Nora nods and drops to her knees in front of you."
                nora "This is so naughty to be doing it in the lab."
                "She reaches out and touches your waist."
                nora "If someone came in, we'd both be in huge trouble."
                "Her hand drifts across your crotch, then holds the waistband of your pants."
                nora "Actually..."
                "She lifts her hand back."
                nora "I don't think this is a good idea."
                me "Are you sure, there's nothing wrong with what we're doing."
                nora "I know, but if we get caught they might punish both of us."
                "She stands up."
                nora "Maybe some other time, I just don't feel like it now."
                "It must have been too large a jump, she's resisted it."
                me "Alright, that's fine. Maybe later."
                "The serum must have had some sort of effect, but you doubt you used it to it's fullest potential."
                $ noraO.change_slut_failed()
                $ noraO.change_resist(blueberry_event_object.get_resist_change(0))
                $ blueberry_event_object.inc_level(0)
        "Bend her over and fuck her.":
            $ action_difficulty = 50
            $noraO.set_action_cumslut()
            $noraO.set_action_freeuse()
            me "We've got the lab to ourselves Nora. How about you bend over the desk and we have some fun."
            if noraO.check_willing(action_difficulty):
                #does it
                #pics
                "She nods happily."
                nora "That does sound like a good way of having fun!"
                "She brushes some papers off of a lab desk and leans over it, tits pressed against the far edge."
                show nora fuck1 at right
                nora "Well? Going to keep me waiting?"
                "She wiggles her ass at you."
                me "Of course not!"
                "You step up and drop your pants down to your feet, revealing your hard cock."
                nora "Oh hurry up, I've been wet all day!"
                "You're not sure how long the serum will last. Better take advantage of this while you have the chance."
                "You pull Nora's pants down and grab ahold of her right ass cheek with your right hand, guiding your cock towards her with your left."
                "She moans as you grab her butt and squirms towards you anxiously. She reaches back and pulls her own panties down and out of the way for you."
                "You drag the tip of your penis against her slit, up and down. Nora moans louder and twitches as you brush against her clit."
                me "Do you want it?"
                nora "What?"
                me "Tell me you want it."
                nora "Oh god I want it, I want you inside me. Fuck me [inputName]!"
                $ noraO.inc_sex()
                "With that you plunge inside. She's already dripping wet, and you slide all the way in."
                nora "Oh fuck! Oh fuck oh fuck oh fuck!"
                "Nora moans into the desk as you begin sliding back and forth. You plant both your hands on her ass cheeks, pushing them together and pulling them apart."
                "Nora bucks wildly towards you with each stroke, desperate to get every last inch."
                me "How's that?"
                nora "It's so good. Oh fuck it's good."
                me "We should do this all the time in the lab."
                "You grind yourself deep into her, pushing her against the lab desk. Nora yelps and pants heavily."
                nora "I would love... Oh god... I would love that."
                me "I could fuck you every night before we go home and leave you quivering on the floor."
                nora "Oh yes! Fuck me!"
                "Nora has lost the ability to buck, and is now twitching with each thrust of your cock deep into her."
                "You can feel your orgasm building as you fuck Nora from behind. You're almost there."
                menu:
                    "Cum inside.":
                        me "Here I come Nora!"
                        if noraO.cumslut:
                            nora "Yes, please give it to me! Fill me up and get me pregnant!"
                        else:
                            nora "Give it to me. Fill me up!"
                        "You pump one last time into her sweet pussy, then hold yourself deep as you release. Your thighs spasm, and you feel Nora tense up against you as you cum into her."
                        show nora fuck2 at right
                        $ noraO.inc_cum_inside()
                        "The two of you stay coupled for a moment, panting and covered in sweat."
                        me "Okay, you should go get cleaned up."
                        "Nora nods slowly, face resting sideways on the bench as she pants loudly."
                        "You pull out, and pull her panties back in place to catch any drips."
                        "Nora stands slowly on shaking legs as you pull your own pants up."
                    "Cum on her ass.":
                        "Without a word you pump faster and faster, then pull out at the last moment and plant the tip of your cock against Nora's left ass cheek."
                        me "Ugh!"
                        if noraO.cumslut:
                            nora "Oh yes! That's right, cover me with your load!"
                        "You pump a stream onto her left cheek, then shift to the right and stroke yourself a few times as you tense and shoot more onto her."
                        show nora fuck3 at right
                        $ noraO.inc_cum_over()
                        "Nora stays slumped on the desk breathing heavily."
                        me "Ya. Wow."
                        me "You should get cleaned up quickly before anyone comes."
                        nora "Right. Ya."
                        "Nora stands up carefully on shaky legs and pulls up her panties to wipe away your cum."
                    "Cum on her face.":
                        me "Get down on your knees! I want to cover you in cum!"
                        nora "Yes! Plaster me with your cum!"
                        "Nora slumps off the desk and spins around."
                        me "Look at me, eyes open!"
                        "Nora does as you say, and opens her mouth as well. Her tongue sticks out, ready to receive your load."
                        "You grab your cock and stroke it a few times as you hurry yourself towards climax. Nora grabs a breast through her shirt and fondles it, while her other hand works between her legs."
                        "Finally you climax. Your cock sends out thick streams of cum that Nora catches on her face. She jerks slightly from the first one, but then locks eyes with you and doesn't move as the rest land."
                        show nora fuck4 at right
                        $ noraO.inc_cum_over()
                        if noraO.cumslut:
                            "You pant as you finish, cum plastered over Nora's left eye, forehead, and cheek. You rest your sensitive cock on her tongue, and she eagerly starts to lick it's shaft."
                        else:
                            "You pant as you finish, cum streams covering Nora's left eye, forehead, and cheek. You rest your sensitive cock on her tongue, which she uses to lightly lick the length of your shaft."
                        "Eventually you step back and pull your pants back up. Nora stays sitting against the bench, breathing heavily and covered in cum."
                        me "Come on Nora, you should get cleaned up before Steph gets back."
                        nora "What? Oh, right."
                        "Seemingly remembering where she is, Nora stands up on shaky legs. She uses the edge of her lab coat to wipe the cum off her face and heads off to the ladies room to tidy up."
                    "Cum in her mouth.":
                        me "Get down on your knees, I want to cum in your mouth!"
                        if noraO.cumslut:
                            nora "Yes! I want to take all of your load! Let me taste it all!"
                        else:
                            nora "Do it [inputName], let it all out for me!"
                        "Nora drops to the ground and spins around. She grabs your cock and quickly wraps her lips around it."
                        show nora fuck5 at right
                        me "Oh ya, blow me till I cum!"
                        "She slids backwards and forwards, tongue licking the tip, and you feel yourself getting ready to finish."
                        me "Here I cum!"
                        "You can't make out what she mumbles in reply, but she bobs up and down with increased vigor."
                        $ noraO.inc_cum_swallow()
                        "She doesn't stop moving as you finish, and you feel yourself blast cum first into her mouth, then down her throat as she works herself up and down, up and down."
                        "She doesn't even stop when you're done. For a few seconds she keeps going, eagerly working your sensitive post-orgasm cock."
                        me "Oh god, that's enough!"
                        "You pull out of her mouth. Nora smiles at you, panting slightly."
                        nora "That was a big load."
                        "She stands up on shaky legs."
                        me "Ya, it was. That was amazing."
                        "You pull your pants back up."
                        me "We should get things cleaned up before anyone comes in."
                        nora "Right. Of course."


                "You can tell by the way Nora looks at you that you've had a huge effect on her. You're not sure how much of that was the serum working, and how much was her."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ noraO.change_resist(blueberry_event_object.get_resist_change(4))
                $ blueberry_event_object.inc_level(4)
            else:
                #Resists
                "Nora nods slowly."
                nora "It always feels good from behind."
                "She leans over one of the lab desks, pushing papers out of the way."
                me "That looks great Nora. Drop your pants for me."
                "She does, revealing a perfect ass. She wiggles it slightly."
                nora "Like that? It feels strange doing it in the lab."
                me "It's okay, we're not doing anything wrong here, right?"
                "You walk up behind her and place your hands on her ass."
                nora "Well, it feels a little strange to have you touching me."
                "You knead her cheeks together, then reach for her underwear."
                nora "Actually, I don't think this is the time."
                "She stands up abruptly, brushing her hands from you."
                nora "Maybe later [inputName], maybe somewhere else."
                "It must have been too large a jump, she's resisted it."
                me "Alright, that's fine. Maybe later."
                "The serum must have had some sort of effect, but you doubt you used it to it's fullest potential."
                $ noraO.change_slut_failed()
                $ noraO.change_resist(blueberry_event_object.get_resist_change(0))
                $ blueberry_event_object.inc_level(0)

    "Stephanie comes back soon, and you spend the rest of your shift working normally in the lab."
    jump campusJumpTimeSkip

label maj_scienceParty:
    $party_event_object.happened = True
    $temp_slut_score = 0
    call serum_give(noraO) from _call_serum_give_19
    $ temp_slut_score = _return
    "You take a detour to a quiet side of the building and place the drinks down. You get out a vial of serum and check to make sure nobody is watching, then pour it into Nora's drink and swirl it around."
    "You pick the drinks up again and return to Nora in her hiding corner."
    show nora work at right
    me "Here you go, it looks like you'll need this."
    nora "Ah, thanks."
    "She takes the glass and immediately takes a big gulp."
    me "So you're really not a fan of this kind of thing, eh?"
    if noraO.exhib:
        nora "No, I hate it. I't much rather be under that podium than listing to whoever's talking at it."
        me "I'll keep my eye out for an opportunity to sneak you up there. Don't forget to finish your drink."
    else:
        nora "No, I hate it. It's all office politics. Once the head of the department makes his speech and I'm sure people saw me here we can head out."
        me "That might be a while, you might as well finish your wine now."
    "Nora thinks for a long moment, but you can see her eyes losing focus as the drug kicks in. She raises the glass and drinks some more, pauses, then finishes the rest."
    me "That's good, I'm sure it will help."
    nora "I am feeling a little bit more relaxed. Although I really would like to walk out there and tell everyone what I really think about this party."
    me "That doesn't seem like a good idea. How about we just hang out together and try and enjoy ourselves."
    nora "I suppose that's the right thing to do."
    me "I was checking out the rest of the building after I got the drinks, and I think I saw some empty rooms over there. Lets head over there so nobody bothers us with party stuff."
    "Nora nods and puts her wine glass down on a nearby table, then follows you."
    "You lead her back to the quiet part of the building and look for some empty rooms. Most of the doors are locked, but you find one that seems to be a conference room that has been left open."
    "You open the door and slip inside, Nora follows and closes the door behind her. You flick the lights on, revealing a long table in the middle of the room with office chairs set around it."
    nora "This looks nice and quiet. We can wait here until the department head gives his speech."
    me "Ya, that sounds like a plan. We can even make the most of our time while we're here, have a mini party of our own."
    nora "That sounds nice, an actual party between friends."
    menu:
        "Have her take her shirt off.":
            $ action_difficulty = 0
            $noraO.set_action_exhib()
            $noraO.check_willing(action_difficulty)
            me "Right. Just the two of us, able to relax however we want."
            "Nora pulls up a chair and sits down with a sigh. You do the same and sit beside her."
            me "I guess you don't go to a lot of real parties any more. At this point there would already be someone with their shirt off."
            nora "Seriously?"
            me "Oh ya, those girls can be crazy. Everyone else is into it though."
            "Nora seems to think about this for a moment, then pulls her lab coat off and throws it on the table."
            nora "Well, we're having a real party in here then."
            show nora strip1 at right
            "She stands up and pulls her sweater up and off, putting it on top of her lab coat."
            me "Wow, looking good Nora. You could definitely be one of those girls."
            show nora strip7 at right
            $ noraO.inc_naked()
            "She smiles, then reaches behind her back and undoes her bra. She leans forward and lets it drop into her hands, then adds it to the pile."
            nora "There, proper party attire. How do I compare to your party girls?"
            me "I think you could definitely keep up. You've got a little more class to you though."
            nora "Well thank you [inputName]. I try to keep things classy."
            "She sits down topless and you make small talk for a while. After a few minutes you hear the crowd outside getting quiet."
            nora "Oh, that must be the speech!"
            show nora work at right
            "She gets up and pulls her sweater and labcoat on quickly."
            nora "Here, hold onto this!"
            "She shoves her bra into your hands and heads out towards the lobby."
            "When the speech is finished she comes back and retrieves her bra. She tucks it inside her lab coat and blushes."
            nora "All done here, we can head out now."
            "The two of you head out and say goodbye. As she walks away you feel confident you made a [noraO.effect_string] impact on her tonight."
            $noraO.change_slut_rebalanced(action_difficulty)
            $noraO.change_resist(party_event_object.get_resist_change(1))
            $party_event_object.inc_level(1)
        "Have her get naked and dance on the table.":
            $ action_difficulty = 15
            $noraO.set_action_exhib()
            me "Right. And I know something that a party like they're having outside would never have. A dancing Nora on a table. They're missing out on a whole lot of fun."
            if noraO.check_willing(action_difficulty):
                nora "You think I could pull that off? I'm not exactly much of a dancer."
                me "I'm certain. Besides, a beautiful girl dancing isn't about the dancing, it's about the girl."
                "Nora thinks about it for a moment, then shrugs."
                nora "Screw it, why not."
                "You lend a hand while she gets on the table. She dances left and right slowly, and you cheer her on."
                me "Keep it up Nora. You should lose some of those clothes."
                nora "Oh, is that what you're used to from girls dancing on tables?"
                show nora strip1 at right
                "She laughs, and pulls her lab coat off. Quickly following is her sweater."
                show nora strip8 at right
                "She spins around and looks away from you while she undoes her bra and drops that to the table too. She glances over her shoulder and smiles at you."
                nora "Want to see more?"
                me "Oh ya, keep going baby!"
                show nora strip6 at right
                "Nora laughs some more and undoes her pants. She drops them to the ground, then turns around and dances a little for you in only her panties."
                me "Only one more thing to go."
                show nora strip5 at right
                $ noraO.inc_naked()
                "Nora smiles and pulls her panties down, dangling her tits in front of you while she does so."
                "She kicks her underwear off the table and dances even more sexily than she did in her underwear."
                "You enjoy her show for a few minutes. The crowd outside the door gets quiet suddenly."
                nora "Oh, the speech must be starting!"
                show nora work at right
                "Nora jumps down quickly and grabs her pants. She pulls them on, then her sweater and labcoat."
                nora "Get my underwear, I'll be back when we're done."
                "Nora rushes out the door, and you grab her bra off the table and underwear off the floor."
                "A few minutes later she comes back and takes her underwear back while blushing. She tucks the clothing into her labcoat."
                nora "All done, we can head out now."
                "The two of you head out and say goodbye. As she walks away you feel confident you made a [noraO.effect_string] impact on her tonight."
                $noraO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(party_event_object.get_resist_change(2))
                $party_event_object.inc_level(2)
            else:
                nora "Ha, ya I doubt anyone out there is dancing on anything."
                "Nora sits down in a chair and sighs."
                me "Well how about you give it a try, we can have our own little party in here."
                nora "Well, I'm not much of a dancer."
                me "I'm sure you'd do great. Here, I'll help you up."
                "Nora thinks for a moment then nods, and you help her onto the conference table."
                "She shakes left and right, putting her arms up and moving them back and forth."
                me "Great, now take off the labcoat for me."
                nora "Here? I don't think so, anyone could walk in."
                me "I doubt it, it's just the two of us in here."
                "Nora dances a little more, but seems to be losing her enthusiasm."
                nora "No, I don't think so. I've never really liked dancing all that much."
                "She hops down off the table and sits back down."
                nora "I think I'd like to just sit and relax while we wait."
                "Here eyes are looking more focused, she must have resisted the drug."
                me "Okay, that's fine too."
                "You sit opposite her and chat for a while. She goes out to make an appearance during the speech, then the two of you head out. As you say goodbye you feel like you could have done more with the situation."
                $noraO.change_slut_failed()
                $noraO.change_resist(party_event_object.get_resist_change(0))
                $party_event_object.inc_level(0)
        "Have her give you a handjob.":
            $ action_difficulty = 30
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            me "Right. We should sit back and relax here, just the two of us. I don't know about you, but I've been pretty worked up the whole day. I could use a chance to \"Relax\"."
            if noraO.check_willing(action_difficulty):
                nora "Oh ya? Well that's no good, this is supposed to be a party, right?"
                me "Exactly!"
                "You slip your pants down past your cock. Nora stares at it for a moment."
                me "So what do you say Nora, mind helping me out?"
                show nora hand1 at right
                $ noraO.inc_hand()
                "Nora bites her lower lip, then nods. She reaches a hand out and takes your cock in her hand, rubbing you slowly."
                nora "I'll help you take care of this [inputName]. Leave it to me."
                "Nora strokes you off for a few minutes, and drops a hand to her waist and rubs herself through her pants too."
                nora "Wait, one moment."
                show nora hand2 at right
                "She takes her hand off of you and unzips her pants. She pulls them down and kicks them off, then pulls her panties to the side and slips a finger into her pussy."
                "Her hand reaches back to your shaft and she resumes her handjob while also fingering herself."
                me "That feels great Nora."
                nora "Good, enjoy it."
                "Nora sighs and fingers herself faster, and jerks you off faster as well."
                "You watch her slide her finger in and out of her wet pussy and can feel your own orgasm building up."
                me "I'm getting close Nora."
                "She nods and strokes you even faster from the chair beside you. Her hand is wet with your precum, spreading it along your shaft while she jerks you off. She moans as she fingers herself quickly too."
                "Your orgasm builds and you begin tensing up. Outside, the crowd starts getting quiet."
                nora "The speech must be starting, I have to get out there."
                me "Wait!"
                "You fire off your load forward onto the floor and Nora rubs your cock a few extra times until you're finished."
                show nora work at right
                "She lets go and grabs her pants. She wipes your cum onto the inside, then pulls them on and heads for the door."
                nora "Wait here, I'll be back in a few minutes."
                "Nora slips out the door and back to the party. In ten minutes she's back."
                nora "Okay, all done. We can head out."
                "The two of you head out and say goodbye. As she walks away you feel confident you made a [noraO.effect_string] impact on her tonight."
                $noraO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(party_event_object.get_resist_change(3))
                $party_event_object.inc_level(3)
            else:
                nora "Ugh, me too. The wine is definitely helping."
                "You slide your chair beside Nora's."
                me "I could use a hand, would you mind?"
                "You pull your pants down a little, slipping the tip of your hard cock out of your pants. Nora looks at you surprised."
                nora "Oh! I think I misunderstood! I just wanted to sit and have a nap."
                me "Well we've got the room all to ourselves, I'm excited. We should make the most of it."
                "Nora considers it for a while, looking at your swollen tip poking out above the waist of your pants."
                "Finally she shakes her head."
                nora "No, we can't do that here. I've got to head out soon, and if anyone walked in we'd both be fired."
                me "I'm sure we'll be fine. It'll just be a few minutes."
                nora "Sorry [inputName], you'll have to wait until you're home or something. I'll try and finish up here as quickly as I can."
                "She must have resisted the drug. Maybe you pushed her too far."
                me "Okay, sorry I brought it up."
                "You pull your pants back up and make small talk for a while. Eventually Nora goes out to make an appearance during the speech, then you head out. As you say goodbye you feel like you could have done more with the situation."
                $noraO.change_slut_failed()
                $noraO.change_resist(party_event_object.get_resist_change(0))
                $party_event_object.inc_level(0)

        "Have her give you a blowjob.":
            $ action_difficulty = 45
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            $noraO.set_action_freeuse()
            me "Right. I always enjoy our time alone together. In fact, I can think of something I'd really enjoy doing right now."
            nora "And what's that?"
            me "A blowjob, if you're up for it party girl."
            if noraO.check_willing(action_difficulty):
                nora "Is that the kind of thing that goes on at university parties these days?"
                me "Well, girls are a little more free spirited now."
                nora "Ha, I'm not that old you know!"
                "Nora drops to her knees at the base of your chair. You undo your pants for her and slide them down past your cock."
                show nora blow1 at right
                $ noraO.inc_blow()
                "She takes your shaft in her hand and rubs it slowly, then brings her mouth forward and runs her tongue along it slowly."
                "You moan quietly as she licks you base to tip a few times, getting your entire cock wet."
                nora "Ready?"
                me "Ready when you are."
                "Nora nods and wraps her head around your tip, then starts bobbing her head up and down. With each stroke she moves deeper, and licks you gently with her tongue inside her mouth."
                me "Ugh, that feels great."
                "She gives you a thumbs up and keeps going. Her mouth makes wet sucking sounds as she blows you."
                "For a few minutes you just enjoy the feeling of Nora around your cock. You can feel your orgasm start to build before long."
                me "I'm getting close Nora."
                "She pulls off your cock and looks up at you."
                if noraO.exhib:
                    nora "God this feels great. Do you want to cum on my face?"
                    "She strokes your wet shaft with her hand a few times."
                    me "Yeah, I do. I want to cover you with it."
                    "She smiles and slides you back into her mouth. She blows you quickly, touching the tip of your cock to the back of her throat with each stroke."
                    "You tap her on the top of the head just before you climax, giving her time to pull back and look up at you."
                    show nora blow25 at right
                    "You spray your load over her face, moving your cock left and right to spread it around as much as possible."
                    "Nora stays pauses, listening intenstly."
                    nora "Shit, the speech!"
                    hide nora
                    "She stands up quickly, doing her best to wipe your load off of her face as she rushes to the door."
                    $ noraO.inc_cum_over()
                    "You pull up your pants and sit down, waiting for a few minutes until Nora returns."
                    show nora work at right
                    nora "Sorry, the speech was starting and I had to make sure I was there."
                    me "No problem. You've got a little..."
                    "You motion to your lip, and Nora checks her own. She giggles a little and wipes away a little bit of cum she missed in her hurry."
                    nora "Oops. Hope nobody noticed."
                    me "I wouldn't worry about it. Nobody would care anyway."

                else:
                    nora "I've got to go out there soon, so you can't make a mess."
                    me "Okay, I'll cum in your mouth then."
                    if noraO.cumslut:
                        "She nods eagerly, stroking you with her hand while you talk."
                        nora "Good, I want you to really fill it up. Give me a nice big load, okay?"
                    else:
                        "She thinks about it for a moment, then nods."
                        nora "Okay, lets get to it then."
                    "She opens her mouth wide and goes back to blowing you. She moves her head quickly, touching your tip to the back of her throat with each downstroke. You're almost ready to cum when the crowd outside grows quiet."
                    me "Don't stop, I'm almost there."
                    "Nora nods and keeps going until you start releasing your load. She moves the tip into her mouth and lets you stroke yourself off until you're done."
                    show nora work at right
                    $ noraO.inc_cum_mouth()
                    "Then, without a word, she stands up and rushes out the door."
                    "You wait in the room for a few minutes until Nora returns."
                    nora "Sorry, the speech was starting and I had to make sure I was there."
                    me "Did you take care of..."
                    "She nods and blushes gently."
                    $ noraO.inc_cum_swallow()
                    nora "Yes, I had to swallow."
                    me "Well done then. A proper party girl after all."
                nora "Ya, right. We're all done here, we can head out."
                $noraO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(party_event_object.get_resist_change(4))
                $party_event_object.inc_level(4)
            else:
                nora "Right here? That seems a little risky [inputName]."
                me "I'm sure everyone else is busy kissing up to their bosses, nobody's going to come over."
                nora "I know, but if they did we'd both get fired. That seems like a big risk."
                me "I'll make it quick, and we'll actually get something good out of this whole evening."
                "Nora thinks about it for a few moments, then shakes her head."
                nora "No, I don't think so. Maybe sometime later."
                "Her eyes are more focused and her speech is more confident. She must have resisted the drug."
                me "Okay, maybe later."
                "You pull up a chair and make small talk with Nora until the speech. Afterwards the two of you head out. As you say goodbye you feel like you could have done more with the opportunity."
                $noraO.change_slut_failed()
                $noraO.change_resist(party_event_object.get_resist_change(0))
                $party_event_object.inc_level(0)

        "Fuck her in the conference room.":
            $ action_difficulty = 60
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            $noraO.set_action_freeuse()
            me "Ya, and I know just the way we should get this party started. How about you take off some of those clothes and take these chairs for a spin?"
            if noraO.check_willing(action_difficulty):
                nora "Oh, I think I know what you mean. That sounds way better than dealing with all the politics going on outside."
                "She pulls her labcoat off and her sweater up and over her head. Before long you've both ditched your clothes."
                "You sit down on a chair and stroke yourself slowly. Nora stands in front of you and spreads her legs around the chair so she can sit on your lap while facing you."
                show nora fuck6 at right
                $ noraO.inc_sex()
                "You hold your cock and guide it in as Nora lowers herself down. She gasps quietly as your tip touches her pussy, and you begin sliding into her wet slit."
                me "There you go, almost all in."
                "She moans as she slides along your full length, eventually coming to a stop at the bottom while she sits on your lap. Without a word she starts moving her hips up and down."
                nora "Is this the kind of party you like?"
                me "Oh ya, this is great."
                "Nora wraps her arms around you and gives you a hug. The chair swings left and right slightly with each stroke into Nora."
                "Her breasts rub against your bare chest while she fucks you, and her breath is warm on your ear."
                "You reach around and grab a handful of her ass with both hands, pulling it up and down to guide her. She speeds up her strokes and moans into your ear."
                nora "Oh ya, fuck me like that."
                if noraO.exhib:
                    "She lets out a loud moan, pumping her hips as fast as she can manage."
                    me "Easy there, someone might hear us."
                    nora "Ah, fine with me. Maybe we can see if they want to join in."
                    "You spend a few more minutes with Nora riding your cock, moaning and gasping. You can feel your core tense up as your orgasm builds."
                else:
                    "A few minutes pass with Nora riding your cock, and you can feel your orgasm building."
                menu:
                    "Cum inside her.":
                        me "I'm getting close Nora. Ride me until I cum."
                        if noraO.cumslut:
                            nora "Oh god yes! Pump it into me, try and make me a mother!"
                        else:
                            nora "Oh god. Okay!"
                        "Nora speeds up even more, her pussy making wet slapping sounds as it lands with each stroke. She moans loudly now, and you give her ass a hard slap."
                        show nora fuck7 at right
                        $ noraO.inc_cum_inside()
                        "You grip her butt hard as you begin cumming and use it to pull her down your full length. She yelps and shudders as you release deep inside her, shaking with her own orgasm."
                        "She holds onto you for a few minutes while you both pant and catch your breath."
                        nora "I think we missed the speech."
                        me "Oh well, I'm sure they didn't even notice we were gone."
                        "Nora kisses you and lifts herself up off your cock. She rushes to her underwear and uses it to wipe up a line of cum dripping down her leg."
                    "Cum on her face.":
                        me "I'm getting close Nora. I want to finish on your face, okay?"
                        "Nora nods and moans, then kisses you a few times on the neck while she pumps her hips up and down."
                        "You hold onto her butt and use it to push her up and down until you are right on the edge. Then you give her a hard slap and pull her up until she gets off."
                        show nora fuck8 at right
                        $ noraO.inc_cum_over()
                        "Nora drops to her knees and looks up at you. You stroke your shaft until you release your load, and spray it over Nora's entire face."
                        "You sit back panting when you're done."
                        nora "I think we missed the speech."
                        me "Oh well, I'm sure they didn't even notice we were gone."
                        if noraO.cumslut:
                            $ noraO.inc_cum_swallow()
                            "Nora uses her finger to scoop up your cum, scraping it off her cheeks towards her mouth. She slides it into her mouth, then licks her finger clean and sighs contently."
                            "Once she's got herself cleaned up she stands up and gets dressed."
                        else:
                            "Nora crawls over to her clothes and grabs her panties. She uses them to wipe your cum off her face, then puts them on."

                    "Cum in her mouth.":
                        me "I'm getting close Nora. I'm going to cum in your mouth."
                        "Nora nods and moans. She kisses your neck and pumps her hips faster."
                        "After a few good strokes you're right on the edge, and give her ass a hard slap to get her up."
                        show nora fuck10 at right
                        $ noraO.inc_cum_mouth()
                        "Nora gets on her knees and wraps her lips around your tip, then strokes you off with one hand."
                        "You unload yourself into her mouth while she moans and fingers her clit. When you're done she pulls off and pauses for a moment."
                        "You see her throat move and hear a swallowing sound."
                        $ noraO.inc_cum_swallow()
                        if noraO.cumslut:
                            nora "Mmm, thank you for that [inputName]."
                            "She licks her lips, and sighs contently."
                            nora "I think we missed the speech though."
                        else:
                            nora "There, all done. I think we missed the speech."
                        me "Oh well, I'm sure they didn't even notice we were gone."
                        "Nora stands up and heads over to her clothes."

                    "Cum on her tits.":
                        me "I'm almost there Nora. I'm going to cum on your tits."
                        "Nora nods and moans, then kisses you on the neck and pumps her hips faster."
                        "You knead her ass and guide her up and down, then give her a hard slap as you're almost ready."
                        "Nora wastes no time and drops to her knees, holding her tits forward to receive your load."
                        me "Here I cum!"
                        show nora fuck9 at right
                        $ noraO.inc_cum_over()
                        "You stroke yourself to completion and release all over her tits. Your cum splatters over her nipples and pools in her cleavage."
                        if noraO.cumslut:
                            nora "Wow, thank you [inputName]. This looks so delicious."
                            "She uses her finger to scoop up some of your semen, then licks her finger clean."
                        else:
                            nora "Wow, well done."
                            "She reaches over to her clothes and grabs her panties. She uses them to wipe up your cum, then puts them on."
                        nora "I think we missed the speech."
                        me "Oh well, I'm sure they didn't even notice we were gone."

                nora "We should get dressed and head out then. No reason to hang around any longer than we have to."
                "You and Nora leave the party and say goodnight. As you're watching her leave you feel you've had a [noraO.effect_string] impact on her tonight."
                $noraO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(party_event_object.get_resist_change(5))
                $party_event_object.inc_level(5)
            else:
                nora "You want to have sex, right here?"
                "Nora thinks about it for a while, then shakes her head."
                nora "No way, if someone walked in we'd both be fired. That's a huge risk."
                me "I doubt anyone is going to walk it, they're all busy at the party."
                nora "Even still, it's not worth it. Maybe some other time [inputName]."
                "Her eyes are more focused, she must be fighting off the drug."
                me "Yea, I guess you're right. Some other time then."
                "You and nora make small talk until the speech. Afterwards you both say goodbye and head your separate ways. As you say goodbye you feel like you could have done more with the opportunity."
                $noraO.change_slut_failed()
                $noraO.change_resist(party_event_object.get_resist_change(0))
                $party_event_object.inc_level(0)

    jump campusJumpTimeSkip

label maj_noraStudySpike:
    $ nora_study_event_object.happened = True
    $temp_slut_score = 0
    call serum_give(noraO) from _call_serum_give_18
    $ temp_slut_score = _return
    "You take a moment to pour some serum into her drink and stir it around with a spoon."
    "Glass of water in hand you return to your room."
    show nora casual at right
    nora "Thanks [inputName]."
    me "My sister got a water purifier that tints the water when it's done. Don't mind the colour."
    nora "Huh, I wonder how it works. Maybe a pH indicator of some sort."
    "She takes a drink of water, then turns her attention back to the work at hand."
    nora "So I was looking at this, and I'm thinking we have to hold this constant while we vary..."
    "She explains her idea, sipping water as she goes."
    me "That just might work. You should finish your drink before we keep going."
    nora "Do you need the glass for something?"
    me "Sort of, ya."
    "Nora gives you a strange look, but drains the rest of her glass."
    me "How are you feeling Nora?"
    nora "I'm feeling good, we've almost got this problem licked."
    me "Good, that's good. I think we need a little more time to relax though. Give our brains a break."
    nora "Do you think so?"
    me "I do. I think I know a good way to relax too."
    nora "And what's that?"
    menu:
        "Have her take off her top.":
            $ action_difficulty = 0
            $noraO.set_action_exhib()
            $noraO.check_willing(action_difficulty)
            me "I don't know about you, but I normally like to work without my shirt on. It's already warm in here, and it just feels so much more free."
            "Nora thinks about this for a few moments, then nods."
            nora "I don't normally do this at home, but if you think it's a good idea we might as well give it a try."
            "You pull your shirt off and throw it on the bed. Nora Pulls her sweater off, then unbuttons her shirt and drops that to the ground as well."
            show nora strip9 at right
            $ noraO.inc_naked()
            "She takes a deep breath and leans back in her chair. Her tits wobble as she breathes out."
            nora "This does feel nice, doesn't it. Are you ready to get back to work?"
            me "Right, ya. Lets get to it."
            "You and Nora work on the questions in the textbook some more. You're distracted the whole time, stealing glances at her boobs while she works."
            "After half an hour of work she sighs and sits back again."
            nora "I'm thinking this was just a printing error. It doesn't seem possible."
            me "Well, we tried our best. I learned a lot either way."
            nora "Good, that's the real point of this anyway."
            "She picks up her shirt and starts putting it on again."
            show nora casual at right
            nora "I had a good time, thanks for the invitation [inputName]."
            me "And thank you for taking the time to come and help."
            "When Nora is dressed you walk her to the door and say goodbye. As she drives away you feel like you made a [noraO.effect_string] impact on her."
            $ noraO.change_slut_rebalanced(action_difficulty)
            $noraO.change_resist(nora_study_event_object.get_resist_change(1))
            $ nora_study_event_object.inc_level(1)
        "Have her get naked.":
            $ action_difficulty = 15
            $noraO.set_action_exhib()
            me "Well it's a little warm in here and you're still wearing a sweater. Hell it's a little too hot for any clothes at all."
            if noraO.check_willing(action_difficulty):
                "Nora thinks about it for a few long moments, then shrugs."
                nora "If you don't mind. It is a little hot now that you mention it."
                me "No, go ahead. We can relax for a few minutes then get back to work."
                show nora strip9 at right
                "Nora nods and pulls her sweater off, then undoes her shirt and places it on the floor carefully."
                show nora strip10 at right
                "She pauses for a moment, then stands up and unzips her pants and slides them down as well."
                nora "Ahh, that's better."
                me "You've still got something left."
                nora "Do you think it should go?"
                me "I think so. So you can completely relax."
                show nora strip5 at right
                $ noraO.inc_naked()
                "Nora reaches behind her and undoes her bra. Then she slips her panties off quickly and kicks them onto her other clothes with a toe."
                nora "Ahh, that does feel really refreshing. I think I'm ready to get back to work already, how about you?"
                me "Lead the way, I'll help if I can."
                "Nora sits down and pulls the books close to her. For the next thirty minutes you steal what glances you can at her tits, ass, and pussy while she sits naked doing biology work."
                "Eventually Nora sits back and sighs."
                nora "I think there was just a printing error, this doesn't seem possible."
                me "Well we gave it a good try. I definitely learned a lot from you."
                nora "Good, that's the real point of problems like this."
                show nora strip11 at right
                "She picks up her panties and slides them on, then her pants."
                nora "Thank you for the invitation to come over [inputName], I had a good time."
                me "I'm glad you could make it, I've learned a lot."
                nora "Good, I'm sure it will help at work."
                show nora casual at right
                "When Nora is dressed you walk her to the door and say goodbye. As she drives away you feel like you made a [noraO.effect_string] impact on her."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(nora_study_event_object.get_resist_change(2))
                $ nora_study_event_object.inc_level(2)
            else:
                nora "No clothes at all? That sounds a little excessive. It feels pretty cool in here to me."
                me "That's just because you haven't tried it nude yet. Go on, give it a go."
                "Nora hesitates while she thinks about it. After a few moments she shakes her head."
                nora "I don't think I'm comfortable with that. Someone might walk in on us, and it would be hard to explain what's going on."
                me "I'm sure we'll be fine."
                nora "It's not worth the risk. I'm fine how I am anyway."
                "Nora seems more alert now. She must have resisted the drug."
                me "Alright, never mind then. Lets get back to work and see what we can do."
                "You and Nora work for another fifteen minutes, then give up and call it a day. You walk Nora to the door and wave goodbye, feeling like you could have done more with the opportunity."
                $ noraO.change_slut_failed()
                $noraO.change_resist(nora_study_event_object.get_resist_change(0))
                $ nora_study_event_object.inc_level(0)
        "Have her jerk you off.":
            $ action_difficulty = 30
            $noraO.set_action_cumslut()
            me "I've been horny since I saw you walk in, and it's making it hard to concentrate. If you could help me out, we could get back to work faster."
            "You rub the bulge in your pants suggestively."
            if noraO.check_willing(action_difficulty):
                "Nora sits for a moment, either stunned or thinking."
                "After a long while she reaches over and rubs you through your pants with one hand."
                nora "Well then, we should take care of that and get back to work as soon as we can. Pull it out for me."
                "You nod and unzip your pants. You slide them down and slip your cock out of your underwear."
                "Wasting no time, Nora grabs onto your shaft and begins rubbing it gently."
                "She jerks you off for a little while, then stops."
                $ noraO.inc_hand()
                nora "I think we could do this more effectively. Do you have any lotion?"
                me "Uh, ya. One moment."
                "You stuff yourself back in your pants and rush to the bathroom. You grab a small bottle of lotion from the counter, then hurry back."
                "You hand the bottle over and Nora squirts some onto her palm while you sit down and get ready again."
                nora "There we go. This should make things much faster."
                show nora hand3 at right
                "When you're ready she wraps her now slippery hand around your shaft and spreads the lotion around. She makes sure to rub her palm over the tip of your cock to get every inch covered."
                "Then she resumes stroking you, faster now. The combination of her warm hand and slippery lotion feels amazing."
                nora "And one more thing."
                show nora hand4 at right
                "With her free hand Nora unbuttons her sweater and shirt enough to pop her tits out. She pulls her bra up, letting her tits hang free in front of you."
                nora "Is this working for you?"
                me "Ya, you're doing great. Just keep going now."
                "Nora nods and keeps stroking your shaft quickly. After a few minutes you can feel your orgasm building."
                me "I'm almost there Nora."
                nora "Okay, just let it out. No need to hold back in your own room."
                "She rubs your cock even faster until you begin releasing. With a steady hand she points your tip away from her and jerks you off onto the floor."
                "When you're finished she lets go."
                nora "There you go, that should help you focus now."
                show nora casual at right
                "You breath deeply and nod. After taking a minute to recover you grab a tissue box and hand some to Nora. She wipes some cum off of her hand while you clean up the floor."
                me "Well thank you Nora. I'm feeling much better now. We should get back to work."
                nora "Excellent. While we were busy I had an idea I wanted to try out."
                "She pulls the books closer to her and scribbles away on a notepad. For the next thirty minutes you work together on the problems, until she leans back and sighs."
                nora "It must be a printing error, this just doesn't seem possible."
                me "Well we gave it a good try."
                nora "We did, and getting practice is the real purpose for this sort of thing. Thank you for having me over [inputName]."
                me "And thank you for coming over and helping me out. I've learned a lot."
                "You walk Nora to the door and wave goodbye. As you watch her drive away you feel like you've made a [noraO.effect_string] impact on her."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(nora_study_event_object.get_resist_change(3))
                $ nora_study_event_object.inc_level(3)
            else:
                "Nora sits for a minute, either stunned or thinking."
                nora "I'm sorry [inputName], but you're just going to have to deal with that some other way."
                me "If you helped me out we could be done in a few minutes."
                nora "If someone walked in we'd be in serious trouble. I'm your boss, that sort of thing can't happen."
                "She turns her attention back to the textbook. She seems more focused now, like she's resisted the drug."
                me "Forget I said anything then, lets just get back to work."
                "You and Nora work for another fifteen minutes, then give up and call it a day. You walk Nora to the door and wave goodbye, feeling like you could have done more with the opportunity."
                $ noraO.change_slut_failed()
                $noraO.change_resist(nora_study_event_object.get_resist_change(0))
                $ nora_study_event_object.inc_level(0)
        "Have her get under the desk while you work.":
            $ action_difficulty = 45
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            $noraO.set_action_freeuse()
            me "Your tits and ass got me all worked up as soon as you walked in. I think I know how to to solve the problem we're working on, but I can't focus while I'm this horny."
            "You rub the bulge in your pants."
            me "You should get under the desk and take care of it, I'll keep working and see if I can make any progress."
            if noraO.check_willing(action_difficulty):
                "Nora sits for a moment, either stunned or thinking. Finally she nods."
                nora "I didn't realise I would have such an effect, or that you would be so distracted."
                me "Well I am, and there's not much I can do about it."
                nora "If you can solve the problem I'll be impressed, and I did offer to help..."
                "She slides down onto her knees. You move your chair back from the desk a little bit to make room for her."
                me "I've got a few ideas I'll try out. If I need any help I'll let you know."
                show nora blow3 at right
                $ noraO.inc_blow()
                "You slip your pants down and slide your cock out. Nora grabs hold carefully and strokes you a few times until you are as hard as possible."
                "Then she licks your tip, running her tongue along the bottom of your shaft a few times before wrapping her mouth around it and beginning to slide down."
                "You moan, and Nora slides off and looks up at you."
                nora "Try to stay focused [inputName]."
                me "Right, sorry. I'll try to keep working at this while you take care of me."
                "You pull a notepad close and scribble down your best guess at how to solve the problem. You're almost certain it's the wrong way to do it, but you don't actually have a better idea."
                "Nora slides her mouth down the length of your cock slowly until you're nice and wet. Then she starts speeding up her blowjob, bobbing her head under your desk."
                "You do what work you can, but the feeling of Nora's warm mouth around your shaft is distracting to say the least. After a few minutes of service you can feel yourself getting close to finishing."
                menu:
                    "Warn her.":
                        me "I'm almost there Nora. You're doing a great job."
                        "She pulls off with a wet pop and peeks up at you from under the desk."
                        nora "Okay, tap me on the shoulder when you're going to finish."
                        "You nod, and she returns your cock to her throat. A few more quick wet strokes and you're ready."
                        if noraO.cumslut:
                            "You tap on her shoulder as you begin to tense up for the first pulse. She pulls back so your tip is resting on her lips and strokes your wet shaft with your hand as quickly as she can."
                            "You fire your load off into Nora's mouth, shooting it off in pulses over her tongue. She looks up at you and moans softly, obviously enjoying herself."
                            "When you're finished she legs go and pauses for a moment, drinking down your cum before she gets back into her seat."
                            $ noraO.inc_cum_swallow()
                            $ noraO.inc_cum_mouth()
                            nora "Thank you [inputName], that was great. I hope it helps you focus too."
                        else:
                            "You tap her on the shoulder as you begin to tense up for the first pulse. She pulls you from her mouth quickly and strokes your wet shaft with her hand as quickly as she can."
                            "She points the tip to the side and you fire your load over her shoulder. Some of your cum hits the bottom of your desk, the rest arcs away from Nora and onto the floor."
                            "When you're finished she lets go and crawls out from under the desk, sitting back in her seat."
                            nora "There, that should help you focus."
                        "You nod and take a moment to catch your breath, then you pull your pants up again."

                    "Let her keep going.":
                        "You lean back and abandon your work while Nora sucks you off. Another few minutes and you're ready to release."
                        "You moan as you start cumming in Nora's mouth. She yelps in surprise as you blast your first shot into her mouth."
                        show nora blow4 at right
                        $ noraO.inc_cum_mouth()
                        if noraO.cumslut:
                            "She keeps her lips wrapped around your shaft, letting you pump your load into her mouth. She moans softly, shivering with pleasure."
                            "When you're done she sits back and quickly drinks down your sperm, taking a deep breath at the end."
                            $ noraO.inc_cum_swallow()
                            nora "[inputName], I thought you were going to warn me."
                            "You take a moment to catch yoru breath, then look down at her."
                            me "Sorry, I got caught up in an idea and didn't realise I was so close."
                            nora "It's fine, it was a pleasant suprise. I was just a little startled."
                            show nora casual at right
                            "Nora crawls out from under the desk and gets back into her seat beside you."
                        else:
                            "She jerks back and pulls her mouth off, and your second pulse catches her square in the face. She ducks for the rest, which go arcing over her shoulder or onto her sweater."
                            nora "[inputName]! You should have warned me!"
                            "You take a moment to catch your breath, then look down at her."
                            me "Sorry, I got caught up in an idea and didn't realise I was so close."
                            "Nora wipes her face with the back of her hand and crawls out from under the desk."
                            show nora casual at right
                            "You hand her a box of tissues and she wipes off her face. You notice she didn't go and spit the cum you got in her mouth out; she must have swallowed it."
                            nora "It's okay, I was just surprised. It's a good thing I didn't hit my head on the desk."
                            "After she finishes cleaning up she sits down beside you again while you do up your pants."
                nora "So, did you make any progress?"
                me "Ah, I thought I had something, but it was just another dead end."
                "Nora looks over your work and nods."
                nora "Right. I thought of this earlier but didn't bother writing it down. A good attempt either way."
                "She grabs a pen and launches into another attempt. For the next thirty minutes you try and finish the problem together, but have no luck."
                nora "I think it's a printing error, this doesn't seem possible."
                me "Well, we gave it a good try."
                nora "We did, and the practice is the important part anyway. Thank you for having me over [inputName]."
                me "And thank you for coming over, it was a pleasure to work with you."
                "You walk Nora to the door and wave goodbye. As she drives away you feel like you've had a major effect on her today."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(nora_study_event_object.get_resist_change(4))
                $ nora_study_event_object.inc_level(4)
            else:
                "Nora sits for a moment, either stunned or thinking. Finally she shakes her head."
                nora "I don't see how this is my fault. I'm sure you can control your urges."
                me "With you around? It's hard to do sometimes."
                nora "Well, you're going to have to tough it out. I'll be gone soon, you can take care of it then."
                "She gives you a sharp look, and you can tell most of the drug has worn off already."
                me "Okay, forget I said anything then. Lets just get back to work and see if we can finish this."
                "You and Nora work for another fifteen minutes, then give up and call it a day. You walk Nora to the door and wave goodbye, feeling like you could have done more with the opportunity."
                $ noraO.change_slut_failed()
                $noraO.change_resist(nora_study_event_object.get_resist_change(0))
                $ nora_study_event_object.inc_level(0)
        "Fuck her on your bed.":
            $ action_difficulty = 60
            $noraO.set_action_cumslut()
            $noraO.set_action_freeuse()
            me "Well if you take your pants off and lay down on the bed I can take you for a quick fuck. After we both finish our heads will be a lot clearer. I'm sure we'll have the problem solved in minutes."
            if noraO.check_willing(action_difficulty):
                nora "Right now? Are you sure we'll be alone?"
                me "Positive. We've got plenty of time to ourselves."
                show nora strip11 at right
                "Nora thinks about it, then nods. She stands up and starts stripping out of her clothes."
                nora "A good fuck does sound nice right about now."
                show nora fuck11 at right
                "Her panties fall to the ground while you kick your own pants off. She lies down on your bed face down, placing her hands on her ass to spread it for you."
                "You walk over to the side of the bed, crotch level with Nora's head."
                me "Wait a moment though, you've got to get me wet and ready."
                show nora fuck12 at right
                "Nora nods and turns her head towards you, she opens her mouth up and sticks her tongue out, inviting you in."
                "You slide your shaft into her mouth slowly, and her tongue licks at the bottom. When you're nice and wet you slide back and forth a few times, gently fucking her mouth."
                "Nora moans softly while she blows you, hands still gripping her ass tightly."
                "Finally you pull off and get on top of Nora, you line your wet cock up with her pussy and begin pushing in."
                show nora fuck13 at right
                $ noraO.inc_sex()
                "Nora moans into your pillow while sink yourself all the way in. You roll your hips against her ass as you start to fuck her."
                me "Looks like I wasn't the only one who was getting wet. You feel great Nora."
                "She nods and pants. Her hands grip at the sheets tightly, gathering balls of fabric."
                "You speed up the pace, and Nora starts to grind her hips up at you with each thrust too."
                nora "Give it to me! Your dick feels great!"
                "Her pussy tightens around your shaft and her own thrusting speeds up."
                "Just to tease her, you pull out almost all the way, leaving just the tip inside, and stop moving."
                nora "What?"
                me "Well if you want it, you'll have to work for it."
                "Nora moans and starts thrusting her pussy up onto your cock from below. She rolls her ass back and forth to get your length sliding in and out again."
                nora "Please? I'm almost there."
                me "Alright, lets make you cum then."
                "You lean hard into Nora, planting your shoulders onto the back of hers to pin her to the bed. You pump your hips up and down, fucking her as fast as you can."
                if noraO.exhib:
                    "She squeals, arching her back and pressing herself against you with each thrust."
                    me "God Nora, you're going to let everyone in the house know what's going on."
                    nora "Fuck, I don't care. Just keep fucking me, please!"
                else:
                    "She sqeuals, then grabs a pillow and moans into it loudly. Her legs twitch and she does her best to keep thrusting herself onto you too."
                "A few more thrusts and you can feel her pussy convulse around you as she orgasms. She lets out one long continuous moan while you keep fucking her."
                "Finally she goes limp under you, breathing heavily."
                "Your own orgasm is fast approaching, and you fuck her faster while you think about how to finish."
                menu:
                    "Cum inside her.":
                        me "Get ready, I'm going to fill you up!"
                        "Nora moans and holds onto the fabric of your sheets."
                        "You fuck her a little while longer, bouncing your hips off her ass with each thrust until you're ready to climax."
                        "You keep fucking her while you cum, timing each thrust to a burst of cum. Nora gasps with each new addition to her pussy, moaning softly when you're finished."
                        show nora fuck14 at right
                        $ noraO.inc_cum_inside()
                        "You stay on top of her while you catch your breath, then pull out and roll off. Nora pants beside you, and your cum starts leaking down her thigh onto the bed."
                        me "Feeling relaxed now?"
                        "Nora nods but doesn't say anything."
                        "After a few minutes she rolls onto her back."
                        nora "I'm feeling more relaxed, but I definitely don't feel like working any more."
                        me "Me neither. Lets just call it a day then."
                        show nora casual at right
                        "She nods, and starts getting dressed slowly. When you're both ready you walk her to the door and wave goodbye. As she drives away you feel like you made a [noraO.effect_string] impact on her today."
                    "Cum on her ass.":
                        me "I'm almost there! I'm going to cover your hot ass!"
                        "Nora moans, lying still on the bed for you to use."
                        "You fuck her a little while longer, bouncing your hips off her ass with each thrust until you're ready to climax."
                        show nora fuck15 at right
                        $ noraO.inc_cum_over()
                        "You pull out and stroke your wet shaft, spraying your load onto her ass cheeks and lower back. She gasps as each fresh line of cum lands on her, then lies moaning quietly when you're finished."
                        "You sit on the edge of the bed and catch your breath while Nora pants beside you."
                        me "Good job Nora, that was great. Mind cleaning me up a little?"
                        "You stand up and walk beside Nora. She turns and looks at you with tired eyes, but opens up for you anyway."
                        "You slide into her mouth and use it to get the last few drops of cum off the tip. It feels amazing with your sensitive post-orgasm cock."
                        "When you're done you pull out and lie down beside her. A few minutes go by until she says anything."
                        nora "I may be more relaxed, but I definitely don't feel like doing any more work."
                        me "Me neither. Lets just call it a day."
                        show nora casual at right
                        "She nods and gets up slowly. She uses her underwear to wipe your cum off her ass, then puts the cum soaked panties on anyway. She gets the rest of her clothes on, then you walk her downstairs."
                        "You wave goodbye as she drives away, and you feel like you've made a [noraO.effect_string] impact on her today."
                    "Cum in her mouth.":
                        me "I'm almost there! You're going to swallow my load Nora!"
                        "Nora moans while you fuck her, but otherwise stays still for you to use as you wish."
                        "You fuck her a little while longer, bouncing your hips off her ass with each thrust until you're ready to climax."
                        show nora fuck12 at right
                        $ noraO.inc_cum_mouth()
                        $ noraO.inc_cum_swallow()
                        "You pull out suddenly, causing Nora to gasp, and get to your feet. You hurry to the side of the bed, and Nora opens her mouth for you."
                        "You slide in quickly, just as your first blast of cum leaves your cock. Nora gasps again, then moans as you fire off the rest of your load into her mouth."
                        "You wait until you're completely finished, then give Nora's mouth a few thrusts for good measure. You pull out slowly, and Nora quietly swallows it all."
                        me "Good girl Nora, you did great."
                        "She nods and pants loudly now that her mouth is free. It takes a few minutes before she's able to sit up on the bed with you."
                        nora "I may be feeling more relaxed, but I definitely don't feel like doing any more work."
                        me "Me neither. Lets just call it a day then."
                        show nora casual at right
                        "She nods and starts getting her clothes on. When you're both ready you walk her to the door and wave goodbye. As you watch her drive away you feel confident you've made a [noraO.effect_string] impact today."

                $ noraO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(nora_study_event_object.get_resist_change(5))
                $ nora_study_event_object.inc_level(5)
            else:
                nora "Right now? I came over to work on these problems in person, not to get distracted."
                me "We're just clearing away the distractions so we can focus. It won't be more than a few minutes, I promise."
                "Nora hesitates and thinks about it, then shakes her head."
                nora "No, I think we should just keep working. If you're... excited, I'll be gone soon. You can take care of yourself somehow then."
                "Her eyes seem more focused and her speech is clearer. She must have resisted the drug."
                me "Okay, if you're sure."
                nora "I am."
                me "Then lets get back to work."
                "You and Nora work for another fifteen minutes, then give up and call it a day. You walk Nora to the door and wave goodbye, feeling like you could have done more with the opportunity."
                $ noraO.change_slut_failed()
                $noraO.change_resist(nora_study_event_object.get_resist_change(0))
                $ nora_study_event_object.inc_level(0)
    jump jumpTimeSkip

label maj_nora_beach:
    $nora_beach_event_object.happened = True
    $temp_slut_score = 0
    call serum_give(noraO) from _call_serum_give_24
    $ temp_slut_score = _return
    #Move up to the changing rooms.
    "You pull out some serum and mix it into Nora's drink before balancing everything on a tray and taking it up to her."
    nora "Excellent, thank you [inputName]."
    me "No problem Nora, my treat. Lets dig in!"
    "You have lunch together, chatting between bites. You keep a careful eye on Nora's drink, waiting until she's finished most of it before you speak up."
    me "Hey Nora, I think I forgot something up by the change rooms earlier today. Would you mind comming with me while I check?"
    "Nora looks at you, eyes slightly unfocesed, and nods."
    nora "If you need me to. Lead the way."
    "You take Nora up to the change rooms. Most of them are empty this time of day, and you pick the stall the furthest away from the parking lot."
    "You open up the curtain, taking a brief glance inside to make sure it really is empty."
    me "Hmm, I guess I was wrong, it's not here. Since we're up here all alone though, I wanted to do something quickly."
    nora "Okay. How can I help?"
    menu:
        "Have her strip for you.":
            $ action_difficulty = 0
            $noraO.set_action_exhib()
            $noraO.check_willing(action_difficulty)
            me "Well, I've been taking looks at you all day and would really like a good long look at your body."
            "Nora thinks for a moment, then nods and steps into the changing room."
            nora "Come on, I'll give you a peek."
            "You follow her in, and she closes the curtain behind you. Once that's done she slides the straps of her swimsuit over her shoulders and pauses for a second."
            nora "Ready?"
            me "Ready."
            show nora strip34 at right
            $ noraO.inc_naked()
            "She pulls her swimsuit down entirely, letting it fall to the sand. She steps out of it and stands in front of you, completely naked."
            nora "Well, what do you think? Is this what you needed to see so badly?"
            show nora strip35 at right
            "Nora turns around, placing her hands on her hips and wiggling her butt at you."
            me "You look amazing Nora, this is exactly what I needed to see."
            show nora strip34 at right
            "She turns back."
            nora "Good. It's nice to know I'm still attractive enough to get this sort of rise out of a boy."
            "She reaches forward and runs her hand over the bulge in your swim trunks."
            nora "A very good rise, by the feel of it."
            "She gives you a wink and steps back, reaching for her swimsuit again."
            me "You're a good looking woman Nora, don't let anyone tell you differently. You've got a killer body and you should be proud of it."
            if slut_outfit:
                show nora swim2 at right
            else:
                show nora swim1 at right
            "Nora steps into her swimsuit again and pulls it back up, pausing to jiggle her tits back into place."
            nora "Thank you [inputName], it means a lot to hear you say that. If we're done here, should we head back to the table?"
            me "That seems like a good idea."
            "You both return to the picnic table. You chat with Nora for another half hour, giving the serum time to wear off completely. You feel confident you had a major effect on her here."
            $ noraO.change_slut_rebalanced(action_difficulty)
            $ noraO.change_resist(nora_beach_event_object.get_resist_change(1))
            $ nora_beach_event_object.inc_level(1)

        "Have her pose while you masturbate.":
            $ action_difficulty = 15
            $noraO.set_action_exhib()
            me "I've been looking at you all day, and your swimsuit has really got me excited. I wanted to duck in here and masturbate quickly, and I was hoping you could help me by posing for me."
            if noraO.check_willing(action_difficulty):
                "Nora thinks for a second, then steps past you into the changing room and motions for you to follow."
                nora "Come on then, I'm sure you've waited long enough to see this."
                "She waits for you to step in with her, then closes the curtain and steps back against the far wall. She slides the straps of her swimsuit over her shoulders and pauses for a second."
                nora "Ready?"
                "You slide your swim trunks down, letting your hard cock free. Nora watches while you take it in your hand and give it a few strokes."
                me "Ready."
                show nora strip34 at right
                $ noraO.inc_naked()
                "She pulls her swimsuit down entirely, letting it fall to the sand. She steps out of it and kicks it to the side, completely naked. You start to jerk yourself off while you watch her."
                nora "What do you think? Will this do it for you?"
                show nora strip35 at right
                "She turns around and puts her hands on her hips, wiggling her ass a little bit."
                me "I think that will get me there, I just need a minute or two."
                nora "Take your time. If you're going to do it, do it right."
                show nora strip36 at right
                "Nora gives you a little while to look at her butt, then turns around and holds her tits up for you."
                nora "Come on, you can cum for me [inputName]. I want you to cum for me."
                "You stroke yourself even faster, spreading your own precum around until you are nice and slippery."
                me "Fuck, that's really hot Nora."
                "She smiles and rolls her nipples between her fingers, moaning softly."
                nora "I know. I want you to climax while you look at me."
                "She licks her lips, eyeing up your dick while you pleasure yourself. You can feel your orgasm building quickly."
                me "I'm almost there... Ah..."
                "Nora spins around again, this time placing her palms flat on the wall when she bends forward. There isn't much space in the room, and her ass ends up right in front of you."
                nora "Do it [inputName], cum all over my ass! I know you want to!"
                show nora strip37 at right
                $ noraO.inc_cum_over()
                "You grunt in response and climax, suddenly pulsing your hot load onto Nora's butt cheeks."
                nora "Oh! There it is. Let it all out."
                "She waits until you've finished covering her, then stands up again."
                nora "There we go. Good job. If that's everything, should we head back to the table?"
                "You take a moment to catch your breath, then pull up your swim trunks."
                me "Sounds like a good idea."
                if slut_outfit:
                    show nora swim2 at right
                else:
                    show nora swim1 at right
                "Nora grabs her swimsuit and uses the inside to clean your semen off her ass. Then she slides it back on, jiggling her tits to get back into place."
                "That done, you return to the picnic table. You chat with Nora for another half hour, giving the serum time to wear off completely. You feel confident you had a major effect on her here."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ noraO.change_resist(nora_beach_event_object.get_resist_change(2))
                $ nora_beach_event_object.inc_level(2)

            else:
                #Getting here with Nora requires at least 30 influence, so this shouldn't happen. Adding just in case.
                "Nora thinks for a few seconds, then shakes her head."
                nora "No, I don't think that's a good idea. You can do whatever you want, I'll be back at the picnic table."
                "She must have resisted the serum, maybe you pushed her too far this time."
                me "It's fine Nora, lets just forget I said anything."
                "You head back to the picnic table and chat for another half hour while the serum wears off completely."
                $ noraO.change_slut_failed()
                $ noraO.change_resist(nora_beach_event_object.get_resist_change(0))
                $ nora_beach_event_object.inc_level(0)

        "Have her give you a handjob.":
            $ action_difficulty = 30
            $noraO.set_action_cumslut()
            me "I've been staring at you in your swimsuit all day and it's gotten me really exited. I wanted you to come in here with me and help get me off with your hands."
            nora "How, exactly, would you like me to do that?"
            if noraO.check_willing(action_difficulty):
                "Nora thinks for a second, then steps past you into the changing room and motions for you to follow."
                nora "I think I can do that. Come in here."
                "She waits for you to step in with her, then closes the curtain and gets onto her knees."
                nora "Lets see exactly what we're dealing with here..."
                if slut_outfit:
                    show nora hand12 at right
                else:
                    show nora hand11 at right
                $ noraO.inc_hand()
                "She pulls down your swim trunks, letting your hard cock spring free. She watches it bounce a few times, then wraps one of her hands around it gently."
                nora "Oh, I can see why you needed my help. You just relax and let me take care of you, okay?"
                "You nod, and Nora starts to stroke you off slowly. Soon after she raises her other hand up and gently massages your balls."
                me "Ah, that feels great Nora."
                nora "Good. I'm sure we'll be done here in no time. Maybe this will speed things along even more..."
                "She sits up a little and leans forward, then opens her mouth and lets a thin line of drool slide out onto your shaft. She moves her head, dragging it up and down the length of your cock."
                "With that done, she moves her second hand onto your shaft as well and starts to stroke your now slippery dick off two handed."
                me "Oh shit!"
                nora "Almost there? Just give me some warning before you cum, okay?"
                "It doesn't take much longer for Nora to bring you to the edge of your orgasm, wet hands sliding up and down along your cock."
                me "Here I cum!"
                "Nora jerks you off as fast as she can, leaning to one side as you cum."
                nora "That's it, let it all out for me [inputName]."
                "You fire your load over her shoulder, pulsing most of your cum into the sand behind her. Your last few drops of sperm land on her shoulder or dribble down onto her hand as she slows down."
                nora "Good boy, that's it."
                me "Oh wow..."
                if slut_outfit:
                    show nora swim2 at right
                else:
                    show nora swim1 at right
                "She lets go of your shaft and stands up, wiping her hands on her thighs."
                nora "I hope you're feeling a little better now. Should we head back to the table."
                "You take a moment to catch your breath, then pull up your swim trunks."
                me "Sounds like a good idea."
                "You return to the picnic table and chat with Nora for another half hour to give the serum time to wear off completely. You feel confident you had a major effect on her here."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ noraO.change_resist(nora_beach_event_object.get_resist_change(3))
                $ nora_beach_event_object.inc_level(3)

            else:
                "Nora thinks for a few seconds, then shakes her head."
                nora "No, I don't think that's a good idea. You can do whatever you want, I'll be back at the picnic table."
                "She must have resisted the serum, maybe you pushed her too far this time."
                me "It's fine Nora, lets just forget I said anything."
                "You head back to the picnic table and chat for another half hour while the serum wears off completely."
                $ noraO.change_slut_failed()
                $ noraO.change_resist(nora_beach_event_object.get_resist_change(0))
                $ nora_beach_event_object.inc_level(0)


        "Have her blow you.":
            $ action_difficulty = 45
            $noraO.set_action_cumslut()
            $noraO.set_action_freeuse()
            me "I've been staring at you in your swimsuit and it's gotten me really worked up. I wanted you to come in here and suck me off."
            if noraO.check_willing(action_difficulty):
                "Nora thinks for a second, then steps past you into the changing room and motions for you to follow."
                nora "If you need it that badly, I'll see what I can do."
                "She waits for you to step in with her, then closes the curtain and gets onto her knees."
                nora "First, we'll have to get these out of the way..."
                "She pulls down your swim trunks, letting your hard cock spring free. She watches it bounce a few times, then looks up at you."
                nora "Oh, I can see why you needed my help. I'll do my very best with it [inputName]."
                if slut_outfit:
                    show nora blow32 at right
                else:
                    show nora blow31 at right
                $ noraO.inc_blow()
                "With that she leans forward and sticks her tongue out, running it along the bottom of your shaft. When she reaches the top she tilts her head to the side, then slides herself back along the side of your cock."
                "She does the same with the other side, making sure you're wet from base to tip, before opening up her mouth and sliding you inside."
                me "Damn, you feel great Nora."
                "She mumbles something in response and starts to blow you, slowly at first but picking up speed with each thrust into her mouth."
                "After a few minutes she's taking you right down to the base, her warm tight throat sending shivers up your spine. She pulls off with a wet pop and looks up at you."
                nora "Would it speed things up if you took control of this? I can just keep my mouth open..."
                "She opens wide and sticks her tongue out, then takes your hands and rests them on the back of her head."
                me "I think it's worth a shot."
                "You thrust forward, sliding yourself all the way to the back of Nora's mouth and holding yourself there. She does her best to look up at you and maintain eye contact."
                me "Yeah, that feels pretty fucking good."
                if slut_outfit:
                    show nora blow34 at right
                else:
                    show nora blow33 at right
                "You hold her head in place and start to pump your hips back and forth, pushing your cock as deep down Nora's throat as you can manage."
                "As she gets comfortable Nora opens her mouth even wider and starts to make wet gagging noises each time you tap against the back of her mouth."
                "After a few moments you pull out, letting Nora gasp for air."
                me "Easy there Nora, if you keep that up the whole beach is going to know what we're doing."
                if noraO.exhib:
                    "Nora wipes some of the spit from her chin and looks up at you and smiling happily."
                    nora "I don't care, let them hear all they want! I just want to feel you at the back of my throat!"
                    "She lunges forward and slips herself onto your cock, giving you a few quick sucks before popping off again."
                    nora "Now, are you almost ready to cum?"
                    me "Yeah, just a little longer now."
                    nora "Good, get back to work then!"
                    "She opens her mouth, and you slide yourself all the way inside again. She pushes herself forward in time with each of your thrusts, slamming your tip against the back of her throat."
                    "The wet smacking noises only get louder as you go, her skullfucking drawing you to the edge of your orgasm."

                else:
                    "Nora wipes some of the spit from her chin and looks up at you."
                    nora "Sorry [inputName], I'll try and keep it down. Are you almost there?"
                    "You nod, and Nora smiles."
                    nora "Good, don't stop now then!"
                    "She opens her mouth up again, and you waste no time sliding yourself back in. She keeps the gagging noises to a minimum, and soon you've brought yourself to the edge of orgasm."

                menu:
                    "Cum in her mouth.":
                        me "Fuck, here we go Nora!"
                        "You give her a few more thrusts, then pull out of her mouth with a wet pop. She looks up at you while you rest your cock on her lower lip, stroking yourself off for the last few moments."
                        "You fire off your load, pulsing thick ropes of cum into Nora's waiting mouth. She maintains eye contact while you fill her up, then leans back on her knees."
                        $ noraO.inc_cum_mouth()
                        if noraO.slut_score > 70 or noraO.cumslut:
                            if slut_outfit:
                                show nora blow38 at right
                            else:
                                show nora blow37 at right
                            $ noraO.inc_cum_swallow()
                            "Nora lets you look for a moment, then closes her mouth and swallows loudly. It takes two or three gulps for her to get it all down."
                        else:
                            if slut_outfit:
                                show nora blow39 at right
                            else:
                                show nora blow37 at right
                            "Nora lets you look for a moment, then leans to the side and spits your cum onto the sand. When she's done she looks back at you."
                        nora "Ah... Thank you [inputName]. I hope you're feeling better now."

                    "Cum on her face.":
                        me "Fuck, here we go Nora!"
                        "You give her a few more thrusts, then pull out of her mouth with a wet pop. She looks up at you while you stroke yourself off, tip resting on her chin."
                        $ noraO.inc_cum_over()
                        if slut_outfit:
                            show nora blow36 at right
                        else:
                            show nora blow35 at right
                        "You fire off your load, pulsing thick ropes of cum over Nora's face. She gasps softly as the first one lands over her nose and forehead, then holds still until you're finished."
                        "You finally sigh and step back, admiring your work. Nora runs a finger under one of her eyes, cleaning away some of your semen."
                        if noraO.cumslut:
                            nora "Wow, thank you [inputName]. This looks delicious."
                            "She looks at her cum covered finger for a moment, then licks it clean. She scoops up some more from her cheeks and does the same, sighing contently after she swallows."
                            $ noraO.inc_cum_swallow()
                            "Soon she's cleaned off most of her face. She wipes the last few drops on her swimsuit."
                            nora "I hope you're feeling better now. I certainly am."
                        else:
                            nora "Wow, well done [inputName]..."
                            "She wipes the cum from her face with her hands, rubbing it on the back of her swimsuit."
                            nora "Nobody should notice that, right? Anyway, I'm hope you're feeling better now."
                if slut_outfit:
                    show nora swim2 at right
                else:
                    show nora swim1 at right
                "Nora gets up off knees and brushes away some of the sand."

                nora "If that's all done, should we head back to the table?"
                me "Sounds like a good idea."
                "You return to the picnic table and chat with Nora for another half hour to give the serum time to wear off completely. You feel confident you had a major effect on her here."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ noraO.change_resist(nora_beach_event_object.get_resist_change(4))
                $ nora_beach_event_object.inc_level(4)

            else:
                "Nora thinks for a few long seconds, staring off past your shoulder."
                nora "You would like me to give you a blowjob? In here?"
                me "That's right Nora. Could you do that for me?"
                nora "I... I don't think so [inputName]. Not here."
                "She's taken on a sharper tone, and seems more focused. She must be resisting the serum! Pushing her farther would do more harm than good."
                me "I'm sorry, just forget I asked Nora. Lets head back to the table."
                "You walk back to the picnic table and chat for another half hour, waiting for the serum to wear off completely."
                $ noraO.change_slut_failed()
                $ noraO.change_resist(nora_beach_event_object.get_resist_change(0))
                $ nora_beach_event_object.inc_level(0)

        "Fuck her.":
            $ action_difficulty = 60
            $noraO.set_action_cumslut()
            $noraO.set_action_freeuse()
            me "I've been staring at you in your swimsuit all day, and I just can't hold back any longer. I want to rip it off of you and fuck you."
            if noraO.check_willing(action_difficulty):
                #Include public section if applicable
                nora "Is that so? Well then, I'll just have to help you out."
                "She steps past you into the changing room, waiting until you follow to close the curtain."
                show nora strip34 at right
                "She slides the straps of her swimsuit over her shoulders, then pulls the whole thing down and off in one fluid motion. She kicks it to the side and faces you, completely naked."
                nora "Lets see just how bad the situation is..."
                "She reaches down to your waist and pulls your swim trunks low enough that your hard cock springs free."
                nora "Oh, you certainly need my help. Lean against the wall and leave everything to me."
                show nora fuck37 at right
                $ noraO.inc_sex()
                "You nod and follow her directions. Nora stands in front of you and leans forward, planing her palms on the far wall while thrust her ass against you. She grinds against you a few times, rubbing your shaft between her ass cheeks."
                nora "There we go. Just slip yourself in, please."
                me "My pleasure. Here we go!"
                "You hold onto the base of your cock and guide yourself in, easily sliding into Nora's wet pussy. She moans softly as you enter her, then presses her hips back against yours to get you as deep as possible."
                nora "Mmm, that feels so good."
                "She jiggles her ass against you while you're balls deep in her, then pulls forward and starts to work herself back and forth on your shaft."
                me "Fuck Nora, you're so wet."
                nora "I noticed your little problem earlier, I just wanted a chance to jump on you and now seemed like a good a time as any! It's a good thing I'm this wet, you feel so big!"
                show nora fuck38 at right
                "You lean back and relax, letting Nora do all the work as she rides your cock. You peek to the side and watch her breasts swing underneath her in time with her thrusts."
                "A few minutes go by with you enjoying Nora's tight, wet pussy when you feel your orgasm start to build, distant but closing fast."
                menu:
                    "Cum inside of her.":
                        me "Keep going like that Nora, I'm going to cum soon!"
                        nora "That's right, give it to me [inputName]! I want to feel your hot cum inside me! Ah!"
                        show nora fuck40 at right
                        $ noraO.inc_cum_inside()
                        "Nora speeds up, slamming her ass back against your hips with each thrust. You grab onto her hips as you climax, pulling her back against you and holding her there while you pump her full of your semen."
                        nora "Oh... That's it... Ah..."
                        "Nora quivers against you and takes a few sharp breaths. Once you're finished cumming she stumbles forward a step and leans against the far wall for support. You watch as your cum drips out of her pussy onto the sand."
                        if noraO.cumslut:
                            nora "[inputName]... That felt so good. I love being filled up with your semen. Maybe you'll get me pregnant if you keep this up. Ah..."
                        else:
                            nora "[inputName]... That felt so good. Ah..."
                            me "Yeah, it did. Thanks Nora."
                        if slut_outfit:
                            show nora swim2 at right
                        else:
                            show nora swim1 at right
                        "She takes a moment to regain her breath, then collects her swimsuit and puts it back on. She has to pause to jiggle her tits back into position."

                    "Cum on her ass.":
                        me "I'm almost there, pull out so I can cum on your hot ass!"
                        "Nora takes a half step forward, sliding you out of her wet pussy, then steps back so it's pressed against her ass cheeks again."
                        show nora fuck39 at right
                        $ noraO.inc_cum_over()
                        "You moan and start to cum, firing your load onto Nora's butt and lower back. She gasps quietly as each new pulse of hot sperm lands on her."
                        if noraO.cumslut:
                            nora "That's it, give it all to me! Cover me with your semen!"
                        else:
                            nora "That's it, Ah, that's a good boy!"
                        "When you're done you both stay still for a moment, catching your breath. Finally she stands up and grabs her swimsuit, using the inside to clean herself off."
                        nora "That was very sexy [inputName], thank you. I hope you enjoyed yourself too."
                        me "Yeah, I did. Thanks Nora."
                        if slut_outfit:
                            show nora swim2 at right
                        else:
                            show nora swim1 at right
                        "Once she's cleaned off most of your sperm she pulls her swimsuit back on, pausing to jiggle her tits back into position."

                nora "Now that that's done, should we get back to the table?"
                me "Sounds like a good idea."
                "You return to the picnic table and chat with Nora for another half hour to give the serum time to wear off completely. You feel confident you had a major effect on her here."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ noraO.change_resist(nora_beach_event_object.get_resist_change(5))
                $ nora_beach_event_object.inc_level(5)

            else:
                "Nora thinks for a few long seconds, staring off past your shoulder."
                nora "You want to have sex? In here?"
                me "That's right Nora. Could you do that for me?"
                nora "I... I don't think so [inputName]. Not here."
                "She's taken on a sharper tone, and seems more focused. She must be resisting the serum! Pushing her farther would do more harm than good."
                me "I'm sorry, just forget I asked Nora. Lets head back to the table."
                "You walk back to the picnic table and chat for another half hour, waiting for the serum to wear off completely."
                $ noraO.change_slut_failed()
                $ noraO.change_resist(nora_beach_event_object.get_resist_change(0))
                $ nora_beach_event_object.inc_level(0)


    return

############################
##Stephanie's Major Scenes##
############################

label maj_stephSpikeDrink:
    $ steph_drink_event_object.happened = True
    $temp_slut_score = 0
    call serum_give(stephO) from _call_serum_give_15
    $ temp_slut_score = _return
    "You mix in some serum, stiring it in with a straw. Then you get back to the lab, drinks in hand."
    show steph work at right
    steph "Perfect! You're a life saver [inputName]."
    me "The pleasure's all mine."
    "Stephanie takes a sip from her drink and leans against a counter."
    steph "So, what got you to come in so early today?"
    me "Well, I figured you or Nora might be in early today and I had nothing to do."
    "She'll need to drink more of the serum to be affected."
    me "So I just figured I'd hang around here and help out if I could. Your drink's getting warm."
    "She picks up the drink again and takes another sip."
    steph "Well it's been great to have you around the lab. The setup work goes so much faster with three sets of hands."
    me "I can imagine. You better keep drinking, that iced cap might melt before we're done chatting."
    "Stephanie nods and keeps sucking back mouthfuls of the frozen coffee drink. Her eyes slowly lose focus, as if looking into the distance."
    me "Can you hear me Stephanie?"
    "She nods."
    menu:
        "Have her take her shirt off":
            $ action_difficulty = 0
            $stephO.set_action_exhib()
            $stephO.check_willing(action_difficulty)
            me "You're such a good lab assistant here all the time Steph. You really should take some time to relax every once in a while."
            me "You should take your shirt off, like you're at a wild party."
            "Stephanie immediately grabs at her sweater and starts pulling it off."
            steph "Like a party? I can manage that, I've been to a few the last few years."
            show steph strip3 at right
            $ stephO.inc_naked()
            "Her sweater is over her head, revealing a startlingly pink and black lace bra."
            "She swings the sweater above her head a few times, then lets it go and chucks it into the corner of the room."
            steph "It's been a long time since I got to party like this though. We've been so busy here."
            "Stephanie starts dancing slightly to music you can't hear."
            steph "And Nora doesn't hang out with anyone fun. It's all tea and blackboards with that crowd. It's great to finally get to flash these girls for someone again!"
            me "That's a shame, a ton of guys must be missing out on seeing you in your bra then."
            "Stephanie looks down at her own tits and smiles."
            steph "At least you get to see them. It's not entirely a waste then."
            show steph strip4 at right
            "She puts her hands under the cups and slides them up until her hands are in the way."
            steph "Not today though, I don't give it up that easy."
            show steph strip3 at right
            "She slides the bra back into place and laughs."
            steph "That's enough for today I think. Wouldn't want Nora walking in on us and wondering what's happening."
            me "Definitely not."
            "You grab Stephanie's shirt and pass it to her."
            "The two of you head out to get some fresh air a few minutes later."
            $stephO.change_slut_rebalanced(action_difficulty)
            $stephO.change_resist(steph_drink_event_object.get_resist_change(1))
            $steph_drink_event_object.inc_level(1)

        "Have her get completely naked and dance for you":
            $ action_difficulty = 15
            $stephO.set_action_exhib()
            me "You like to party, right Stephanie?"
            steph "Ya, I've done some partying before."
            me "Did you do a lot of dancing at those parties? For guys I mean."
            "She nods and smiles."
            steph "I have, I like to think of my dancing skills as impressive."
            me "Would you dance for me then? I'm curious how good you actually are."
            if stephO.check_willing(action_difficulty):
                steph "A proper dance for men is what you want? I can make that happen."
                "Stephanie takes you by the hand and leads you over to a high lab stool."
                "Once you are firmly seated she struts two steps away, showing off her great ass in her jeans."
                "She turns around, as tapping one foot as if in time with some music. Her hands hold the two sides of her shirt and begin pulling them upwards."
                steph "I can definitely make it happen."
                show steph strip3 at right
                "She pulls her shirt up and off, revealing a bright pink and black bra. Then she turns around and you can hear the zipper of her jeans going down."
                show steph strip5 at right
                "Stephanie plants her hands on her waist and slides them down, keeping her legs straight as her pants drop to show her matching set of panties. Her ass ends high in the air towards you."
                show steph strip6 at right
                $ stephO.inc_naked()
                "Then, slowly, she draws her hands along her thighs, ending with them on her ass. She gives both cheeks a quick smack which echos around the room."
                steph "How's the show so far?"
                me "Great, you look amazing."
                "Stephanie walks towards you on your stool and grabs your hands in hers. She turns around and plants them on her tits, then holds her own high up in the air while you are left to fondle her breasts."
                "She grinds against you in time with music you can't hear."
                steph "That's right, grab a handful."
                "You oblige and knead her tits through her bra. Her ass rubs up against your cock as she grinds against you."
                show steph strip2 at right
                "Eventually she steps away and reaches behind herself to undo her bra. She lets it fall to the floor, then lowers her underwear as well."
                "Completely naked, she turns to face you with legs spread."
                steph "And that, [inputName], is how I used to dance."
                "You clap as she bows, dangling her perky tits for you."
                me "An incredible show. I hope this won't be the only showing."
                "Stephanie smiles and winks as she collects her clothing."
                "Afterwards you decide to get lunch together, and you're satisfied you made a [stephO.effect_string] impact today."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_drink_event_object.get_resist_change(2))
                $steph_drink_event_object.inc_level(2)
            else:
                steph "Sure thing, but I can't exactly do it the normal way here."
                me "Sure you can. Just lock the door and nobody will know."
                "Stephanie shakes her head."
                steph "A bunch of other people have the code. If we got caught they'd fire us both."
                steph "I can do a clothed dance though, how's that sound?"
                me "Seems like a reasonable compromise."
                "You sit on a lab bench while Stephanie spins and grinds to imaginary music. It's impressive, and she's having a good time, but it would definitely be sexier if she was naked."
                "Not wanting to risk the drug wearing off any faster, you let Stephanie finish her routine."
                me "Very nice."
                steph "I'm glad you liked it."
                me "I'm going to get some lunch, I'll be back in a little bit for my shift."
                "Stephanie nods and goes back to dancing slowly in her own world."
                "She must have resisted the drug, maybe you pushed her too far."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_drink_event_object.get_resist_change(0))
                $steph_drink_event_object.inc_level(0)

        "Ask her to suck you off":
            $ action_difficulty = 35
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            me "We're all alone down here, and thinking about the way you move when you work has got me all excited."
            "You rub your crotch, and Stephanie's eyes follow the movement."
            me "If you're up for it, I need some relief."
            if stephO.check_willing(action_difficulty):
                steph "You want a blowjob? No problem."
                "She takes you by the hand and leads you to a low lab bench. She pats for you to sit down on it, and you do."
                if stephO.freeuse:
                    steph "I've been getting a little practice lately. I'm sure you'll have a good time."
                else:
                    steph "It's been a little while, I might be a touch out of practice."
                    steph "But if it's for the greater good, how could I say no."
                "Stephanie grabs your pants and pulls them down, revealing your already hard cock."
                steph "Well I see you do need my help."
                me "Ya, pretty badly."
                "She gets down on her knees and runs her hand down your shaft. She cups your balls with the other hand and plays with them slowly."
                "She begins stroking your cock, then leans over it and lets a long line of spit fall over it. Her hand speeds up and spreads the spit around."
                "Next, she licks the shaft and tip quickly, making sure every last inch is wet and slipery. Finally, she brushes her hair out of the way, opens her mouth, and slides you inside."
                show steph blow1 at right
                $ stephO.inc_blow()
                "Stephanie's mouth is warm, wet, and the perfect combination of suction and friction. She takes you as deep as she can after a few trial runs, then slides her head back and forth at a moderate pace."
                me "That feels great Steph, don't stop."
                "In response, her hands reach up for yours. She guides them to the sides of her head and leaves them there. You gently guide her back and forth, encouraging her to greater speeds and depths."
                show steph blow5 at right
                "Her own hands drop to her waist and she lifts up her shirt and bra, exposing her tits for you. She then puts her hands behind her back, and continues entirely hands free."
                "Within a few minutes you're feeling ready to finish."
                menu:
                    "Cum in her mouth.":
                        me "I'm almost there. I want to cum in your mouth."
                        "Stephanie nods at the top of a stroke, then picks up the pace and begins flicking your tip with her tongue at the top of every pass."
                        if stephO.cumslut:
                            "You tense up as you reach orgasm. Stephanie holds your tip just inside her lips as you start to pulse your load out into her mouth. Her eyes flutter as your cum sprays across her tongue."
                        else:
                            "You tense up as you reach orgasm and Stephanie holds your tip in her mouth. Her eyes lock with yours, face turned up as you unload everything you can into her."
                        "After a long moment she lets go of your cock and kisses it on the tip."
                        show steph blow6 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "Then she opens her mouth to show you it's full of cum. She closes and swallows, then opens again. Then she moves her tongue around to show she's not hiding it anywhere."
                        me "Holy crap. Wow."
                        if stephO.freeuse or stephO.cumslut:
                            steph "Mmm, that was great [inputName]. Thanks for the fun."
                            me "Any time, you know where to find me."
                        else:
                            steph "Ya, wow. Like I said, it's been a long time since I got to do that."
                            me "Well, I'm glad to bring you out of retirement."
                        "Stephanie smiles and pulls her shirt back down into position."

                    "Cum on her face.":
                        me "I'm almost there. I want to cum all over your face."
                        "Stephanie shakes her head left and right at the top of a stroke, then picks up the pace. Her tongue works along your shaft as quickly as it can."
                        "You tense up as you reach orgasm and move to pull your cock out of her mouth."
                        "Stephanie grabs you from behind with both arms and pulls you in, refusing to let you out."
                        "It's too late, and you start to cum."
                        "She bobs happily up and down on your shaft as you spasm out your load, then slowly slides off and kisses the tip."
                        show steph blow6 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "She looks at you and opens her mouth to show that it's full of cum, then closes and swallows."
                        if stephO.cumslut:
                            steph "Sorry [inputName], I just needed to taste your cum so badly. I hope you don't mind."
                            "She smiles up at you and licks her lips."
                            me "I think I'll get over it."
                        else:
                            steph "If I'm the one giving the blowjob, I decide where you finish."
                            "She winks and pulls her shirt back into position."
                            me "I'm not about to argue with you."
                            steph "I use to run with a group of girls. We joked that we didn't want our hair ruined, so we always let them cum in our mouth."
                            steph "Truth is, after a while you start to like it."
                            me "Those sound like a wild group of girls. I'm available if you ever feel like you need a reminder of the good old days."
                            steph "I'll keep that in mind."

                    "Cum on her tits.":
                        me "I'm almost there. I want to cum all over your tits."
                        "Stephanie shakes her head left and right at the top of a stroke, then picks up the pace. Her tongue works along your shaft as quickly as it can."
                        "You tense up as you reach orgasm and move to pull your cock out of her mouth."
                        "Stephanie grabs you from behind with both arms and pulls you in, refusing to let you out."
                        "It's too late, and you start to cum."
                        show steph blow6 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "She bobs happily up and down on your shaft as you spasm out your load, then slowly slides off and kisses the tip."
                        "She looks at you and opens her mouth to show that it's full of cum, then closes and swallows."
                        if stephO.cumslut:
                            steph "Sorry [inputName], I just needed to taste your cum so badly. I hope you don't mind."
                            "She smiles up at you and licks her lips."
                            me "I think I'll get over it."
                        else:
                            steph "If I'm the one giving the blowjob, I decide where you finish."
                            "She winks and pulls her shirt back into position."
                            me "I'm not about to argue with you."
                            steph "I use to run with a group of girls. We joked that we didn't want our hair ruined, so we always let them cum in our mouth."
                            steph "Truth is, after a while you start to like it."
                            me "Those sound like a wild group of girls. I'm available if you ever feel like you need a reminder of the good old days."
                            steph "I'll keep that in mind."

                show steph work at right
                "After getting cleaned up you decide to split up and get some lunch. You feel satisfied that you've made a [stephO.effect_string] impact with todays performance."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_drink_event_object.get_resist_change(3))
                $steph_drink_event_object.inc_level(3)
            else:
                steph "You mean a blowjob?"
                "She thinks about it for a long time. Her hand drifts over to your crotch and rubs you through your pants."
                steph "I'm not sure that's a good idea actually. Not here."
                me "I'm sure it would be fine."
                "You pull your pants down and get your cock out for her. She stares at it a moment, transfixed."
                "Her hand drifts closer to it."
                steph "No. Wait. No."
                "She shakes her head and turns away. You put yourself back in your pants quickly."
                steph "We could be fired, someone could catch us, I'd never do something like that in the lab."
                me "Okay, forget I asked then. No big deal."
                steph "Right, no big deal."
                "You chat a little while longer, then head out for lunch. You must have pushed her too far all at once."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_drink_event_object.get_resist_change(0))
                $steph_drink_event_object.inc_level(0)

        "Fuck her on a lab bench":
            $ action_difficulty = 55
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            me "We've got the lab to ourselves, and a locked door. I don't know about you but just thinking about having you alone is making me horny."
            me "How about you hop up onto the bench and let me fuck you."
            if stephO.check_willing(action_difficulty):
                steph "Right here on the bench?"
                "She hops up onto it and scoots her butt back a little."
                steph "I've done it in worse places. Might as well help you release some of that sexual tension."
                show steph fuck2 at right
                "Stephanie lifts up her shirt and bra, throwing them to the side. Then she undoes her pants and slides them down. Left in only her sneakers and panties, she spreads her legs for you."
                me "Oh ya, you'll help me release something alright."
                "You step foward between Stephanie's legs and grind your crotch against hers. Her hands drop to your waist and undo your pants while she kisses you along your neck."
                "Your pants fall free, and she begins fondling your cock. She's already left a small wet spot on the bench where her soaked panties have touched."
                steph "I think I'm ready for you."
                me "Then lets do this."
                $ stephO.inc_sex()
                "Steph pulls your cock in closer and slips her panties to the side. You slide into her pussy easily, and she sighs as you enter."
                "You wrap your arms around her and pull her close, and her legs wrap around your waist to do the same."
                me "Oh god you're tight."
                "Her slit clamps down on you as she tenses up and sighs, and you have to fight to get moving again inside her."
                steph "Damn I'm horny. I'm going to cum soon."
                "You pump back and forth rhythmically while Stephanie pants and squirms in your arms. Finally you hear a sharp intake of breath, and her whole body shudders against yours."
                steph "Don't stop, this is the best part!"
                "You have no intention of stopping, and the feeling of Stephanie orgasming around you is incredible. You lower both your hands onto her ass and grab as hard as you can."
                steph "Oh, just like that. Just like that!"
                show steph fuck3 at right
                "With both hands under her, you start lifting Stephanie a little then letting her slide back down onto your cock. Before long you've abandoned the desk entirely, and the two of you stand in the middle of the room."
                me "Are you still cumming?"
                "Stephanie buries her head into your shoulder and nods repeatedly, then squeals as you pump faster. Her hips rock back and forth to get more movement along your shaft."
                me "Well we can't let you have all the fun. I'm going to cum soon too."
                "She pants heavily on your shoulder, trying to catch her breath."
                steph "Cum... cum where ever you... want."
                menu:
                    "Cum inside.":
                        me "I want cum inside you. I want to fill you up!"
                        if stephO.cumslut:
                            steph "Oh god yes! Please, please give me everything you can! I need it so badly!"
                        else:
                            steph "Do it! Ugh... Cum already!"
                        "You drop Stephanie down on your cock one last time and leave yourself as deep as gravity could get you. Her legs curl into your back and her ass tightens underneath your hands."
                        "You feel yourself spasm into her, and she spasms in response. After six long pulses you stumble back to the lab bench and place her down."
                        "As soon as you let go she relaxes and slumps back, legs limp off the edge."
                        steph "Oh wow, you really did fill me up."
                        show steph fuck4 at right
                        $ stephO.inc_cum_inside()
                        "As you watch a bubble of cum bursts and a stream of it runs around her panties, down her ass, and onto the lab bench."
                        me "Ya, I really did."
                        steph "I'm going to need a moment to catch my breath. And to stop my legs from shaking."
                        "You pull up a chair and collapse as well. Both of you take a few minutes to slow your breathing."

                    "Cum on her tits.":
                        me "I want to watch my cum drip down your tits!"
                        if stephO.cumslut:
                            steph "Okay, whatever, I just want your cum on me right now. Please!"
                        else:
                            steph "Okay! Hurry up and cum!"
                        "You pump a few last times into her wet pussy, then lift Stephanie off your cock and plant her on the ground. She reaches up for her tits and holds them while you stroke yourself towards her."
                        show steph fuck5 at right
                        $ stephO.inc_cum_over()
                        "You bring yourself to climax and spray your load over Stephanie's upper chest and tits. Thick streams of cum drape across her nipples and pool in her cleavage."
                        "When you finish she runs her hands over the splatter marks and rubs it into her skin, making her tits look shiny."
                        steph "That was one hell of a load."
                        "She takes a cum covered finger from her chest and licks it clean."
                        me "Wow. Ya, you took it well."
                        "You both pull up chairs and spend a few moments catching your breath."

                    "Cum on her face.":
                        me "I'm going to cum on your face while you look at me."
                        if stephO.cumslut:
                            steph "Oh yeah, I want to feel your hot cum all over me! Come on, give it to me!"
                        else:
                            steph "Classic. I can do that."
                        "She pants loudly as you pump a few more times into her, then you lift Stephanie up off your cock and lower her to the ground."
                        "As soon as she's down she falls to her knees, one hand rubbing her clit, the other one kneading a breast. She looks up at you with wide eyes, mouth open and tongue out."
                        me "Perfect, here I come!"
                        show steph fuck6 at right
                        $ stephO.inc_cum_over()
                        $ stephO.inc_cum_swallow()
                        "You stroke yourself to completion and unload yourself onto her face. You send at least two pulses of cum into her mouth, but she doesn't flinch. When you're done she quietly swallows."
                        if stephO.cumslut:
                            steph "Mmm, thank you [inputName]. You gave me such a big, tasty load."
                        else:
                            steph "Well done. That was a huge load."
                        "She wipes her face with her hands, then licks her fingers clean."
                        me "You earned it after that performance."
                        "You both pull up chairs and spend a few moments catching your breath."

                    "Cum in her mouth.":
                        me "Never waste a drop, right? I'm going to cum in your mouth!"
                        steph "Oh god, yes!"
                        "She shudders as you pump a few more times, then lift her off your cock and drop her to the ground."
                        "She immediately goes to her knees and lunges to get your shaft in her mouth."
                        show steph fuck7 at right
                        $ stephO.inc_cum_mouth()
                        "Almost immediately you're inside her again as she moves her head up and down, licking with her tongue as she goes."
                        me "Here it is!"
                        "Stephanie pulls you back to her mouth and places the tip underneath her tongue. You can feel your cum washing back over you as it tries to find more room to go, and Stephanie puffs out her cheeks."
                        "Several huge spasms later you've finished emptying your load and pull out."
                        $ stephO.inc_cum_swallow()
                        "Stephanie looks at you with big eyes, then swallows. Then again. Then a third time."
                        "Finally she opens her mouth and gasps for air, then shows you her cum free mouth."
                        me "Good girl, that was impressive."
                        "She nods, but doesn't say anything. Her legs still shake slightly, and she scoots back against the lab bench to wait for the orgasm convulsions to end."
                        "You also pull up a chair, and the two of you spend a few minutes catching your breath."

                "Finally, when you're both able to walk and talk again, you decide to head out and get lunch at separate places."
                #Fuck her like a rock star
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_drink_event_object.get_resist_change(4))
                $steph_drink_event_object.inc_level(4)
            else:
                "Stephanie nods slowly and moves to a lab bench. She sits down at the edge, legs spread."
                steph "Like this?"
                "You nod and move towards her."
                "She closes her legs and looks away."
                steph "Wait, nevermind."
                me "What's wrong?"
                steph "It doesn't feel right, and I always trust my gut. This isn't a good idea."
                "Stephanie stands up quickly and walks away from you."
                me "Are you sure?"
                steph "Positive."
                "She must have resisted the drug. Maybe you pushed her too far this time."
                me "Alright then, I trust you."
                "She nods. The two of you go out and get lunch, then split up."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_drink_event_object.get_resist_change(0))
                $steph_drink_event_object.inc_level(0)
    jump campusJumpTimeSkip

label maj_tennisSpike:
    $ steph_tennis_event_object.happened = True
    $temp_slut_score = stephO.slut_score
    call serum_give(stephO) from _call_serum_give_13
    $ temp_slut_score = _return
    "You pull some serum out from your pocket and slip it into Stephanie's water bottle. You shake it around to make sure it's well mixed, then put it back where you found it."
    show steph sport at right
    "After a few minutes Stephanie comes back and throws you a cold bottle of water."
    steph "Catch! Drink up then we can get back to it."
    "You crack open the bottle and take a much needed drink while Stephanie does the same with her own."
    me "Make sure to drink up, getting fluids is important."
    "Stephanie nods and drinks more of her water, until most of it is gone."
    steph "Ya, I think I was more dehydrated than I thought. I'm feeling a little light headed."
    me "I'm sure it will pass. Just give it a moment."
    "You wait and watch as Stephanie's eyes grow unfocused, staring at the tennis net."
    me "Feeling relaxed now?"
    steph "Ya, I am."
    menu:
        "Have her show off her tits.":
            $ action_difficulty = 0
            $stephO.set_action_exhib()
            $stephO.check_willing(action_difficulty)
            me "We've got the court to ourselves here, how about we take a few minutes to do something else and catch our breath."
            steph "What else would you like to do?"
            me "Well, if we're just standing around I might as well have something interesting to look at. How about you show off your tits to me?"
            "Stephanie thinks about it for a few moments, then nods."
            steph "Fine, I guess we don't really have anything to do anyway."
            show steph sportstrip1 at right
            $ stephO.inc_naked()
            "She checks behind her for people, then pulls her tanktop up and over her tits. She's not wearing a bra underneath, and they fall free of the garment easily."
            steph "What do you think?"
            me "You look great Stephanie, it's a shame I can't see them more often."
            steph "Well, I think you might get a little distracted at work if I had the girls out all the time."
            me "I'm distracted now, that's for sure. I didn't think tennis would turn into a show like this."
            show steph sportstrip2 at right
            "Stephanie laughs and smiles. She grabs her racket off of the bench beside her and uses it to lift her tits up from below."
            steph "Might as well make it a tennis themed show then."
            "She moves the tennis racket up and down, bouncing her tits for you."
            steph "Okay, ready to get started again?"
            me "One moment, just a few more looks."
            show steph sport at right
            "She turns to the left and right to show them off some more, then takes the racket away and pulls her shirt down again."
            steph "Alright, you've had plenty of rest time now. I came here to play some tennis, not just to show off."
            me "Alright, fair is fair. Lets get back to it then."
            "You and Stephanie play a few matches over the rest of the morning. When you're done you return your rental gear and say goodbye. As you watch her walk away you feel like you've made a [stephO.effect_string] impact on her."
            $stephO.change_slut_rebalanced(action_difficulty)
            $stephO.change_resist(steph_tennis_event_object.get_resist_change(1))
            $steph_tennis_event_object.inc_level(1)
        "Have her touch herself while you play.":
            $ action_difficulty = 15
            $stephO.set_action_exhib()
            me "You're crushing me out there, this feels completely unfair."
            steph "It's just a friendly game though."
            me "I know, but I'd like to at least feel like you're trying. How about a handicap, to make thing even."
            steph "What sort?"
            me "Well, it must be difficult to play while you're distracted. For the next match you'll have to keep one hand in your underwear, and then we'll see who the winner is."
            if stephO.check_willing(action_difficulty):
                steph "Ha, you think that would stop me?"
                me "If you're giving yourself a good time? Oh ya, I think that'll put us on even footing."
                steph "Alright, fine. Challenge accepted. Get on your side."
                show steph sportmast1 at right
                $ stephO.inc_naked()
                "You and Stephanie head to opposite sides of the tennis court. Before you serve Stephanie lifts up her skirt and slides her hand underneath her lacy red underwear."
                steph "Ready, lets do this."
                "You serve, and Stephanie runs to the side to return the shot. She's a little slower because her hand is in the way, but has no trouble beating you and winning the rally."
                steph "You'll have to try harder than that!"
                "You can see her fingers squirm underneath the thin fabric of her panties. She's obviously not taking it easy on you or herself."
                "Another serve, and another rally won by Stephanie. She takes her hand out to serve, then shoves it back before you can return it."
                "Her running seems to be getting slower, and for the first time in the match you're able to win the rally."
                me "Having some problems?"
                "Stephanie pants a little bit before responding. Her skin is flush and her knees are shaking a little bit."
                steph "Me, no way. I've got this."
                me "Okay, just make sure you don't finish yourself before we finish the match."
                "She serves, barely clearing the net with the ball, and goes back to fingering herself as quickly as she can."
                "After a tense rally you score another point, tying the game."
                steph "Damn it!"
                me "Keep those fingers going, no cheating!"
                "She speeds up her masturbation and lifts her skirt up so you can see."
                steph "I'm doing it. I just didn't think this would be so hard."
                "You serve again, and it's becoming increasingly obvious that Stephanie is distracted. The rally barely starts before she drops to her knees and misses the ball."
                me "So close! I think I've got you on the run!"
                show steph sportmast2 at right
                "Stephanie doesn't say anything, but drops her racket and shoves her second hand between her legs."
                me "Oh, are you surrendering?"
                steph "Wait, just one moment."
                "She pants loudly and spreads her legs a little. She's pulled her underwear completely out of the way and you can see one hand fingering herself while the other rubs her clit."
                me "That sounds like a forefeit to me."
                steph "Fine, you win! Just let me finish please."
                me "Go for it, you've earned it after all that."
                "She rubs herself as fast as she can, and within a minute is shuddering from her orgasm. When she's finished she stands up slowly and heads over to the bench."
                show steph sport at right
                steph "I think the competition made it more intense. We should do this more often."
                me "We should. Lets take a few minutes for you to catch your breath."
                "She nods, and you chat a little while she regains her strength. Afterwards you play a few more matches, and find that post-orgasm Stephanie is an easier opponent."
                "Eventually you're both tired and say goodbye. As you watch her head off you feel like you've had a major effect on her."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_tennis_event_object.get_resist_change(2))
                $steph_tennis_event_object.inc_level(2)
            else:
                steph "Right here? We're kind of out in the open."
                me "We're fenced in on three sides, and nobody is using the other court. Come on, it'll make it fair for both of us."
                "Stephanie thinks about it for a long moment, then shakes her head."
                steph "No, that seems strange. It's just a friendly match, it doesn't even matter if you aren't winning."
                "Her eyes are focusing more, and her speech is more determined. She must have resisted the drug."
                me "Okay, lets just play a normal match then. No going easy on me though."
                "You and Stephanie play a few more matches until you're both tired. As you head your separate ways you feel like you could have done something more with the situation."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_tennis_event_object.get_resist_change(0))
                $steph_tennis_event_object.inc_level(0)
        "Have her masturbate with her racket.":
            $ action_difficulty = 30
            $stephO.set_action_exhib()
            me "I'm going to need a few minutes to catch my breath before we start again. It's really unfair how much better you are than me, you aren't even winded."
            steph "Well, lots of practice helps with that."
            me "I bet it does. I think we need to make this even though, and get you out of breath too."
            "Stephanie looks at you confused."
            me "A good orgasm always leaves me exhausted, I'm assuming it's the same for you. You can use your racket to get off, and when you do we can play another match on even footing."
            if stephO.check_willing(action_difficulty):
                steph "Why not just use my fingers? They're normally good enough."
                me "Well we're playing tennis, it only feels right that you're still using a racket somehow."
                "Stephanie laughs a little and looks at the racket on the bench."
                steph "Fine, I'll give it a try. If it doesn't work I'll just get myself off normally."
                me "Sounds fair to me."
                show steph sportmast3 at right
                $ stephO.inc_naked()
                "Stephanie stands in front of you and lifts up her skirt. She places her racket between her legs, handle behind her, and holds it against her crotch."
                "Slowly at first, then gaining confidence, she begins rubbing her hips back and forth along the handle of the racket."
                me "How's it feel."
                steph "Interesting. I think this might work."
                "She holds the racket tight against her and rubs faster. She moans softly, then checks behind her to make sure nobody is around to notice."
                me "Don't worry, I'll keep an eye out. You can just enjoy yourself."
                "She nods and closes her eyes while she grinds against the leather wrapped handle."
                "After a few minutes she reaches down and pulls her underwear to the side. As she grinds against the handle her pussy lips spread, and she leaves wet streaks along it's length."
                steph "Oh that feels strange."
                me "Good though?"
                "A moan and a nod are your answer."
                show steph sportmast4 at right
                "A few more strokes and Stephanie sits down on the bench next to you. She holds the racket with one hand and uses it to rub against her slit while her other hand rubs her clit quickly."
                steph "I'm almost there."
                me "Keep it up girl."
                show steph sportmast5 at right
                "She arches her head back and moans loudly, dropping the racket to the ground and plunging three fingers into her pussy."
                "Stephanie shivers a few times and tightens her legs up suddenly. She moans, then relaxes."
                me "Perfect. Well done."
                steph "Glad you enjoyed the show."
                me "Come on, time for a match on even footing."
                show steph sport at right
                "Stephanie takes a deep breath, then picks her racket up and takes her place on the far side of the court. After a few minutes of playing it's clear post-orgasm Stephanie is a much easier opponent."
                "You have a few very close matches, even managing to win one, then decide you're too tired to continue."
                "As you watch Stephanie head out you feel like you've made a [stephO.effect_string] impact on her."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_tennis_event_object.get_resist_change(3))
                $steph_tennis_event_object.inc_level(3)
            else:
                steph "With my racket? It's not even clean though. What if someone saw me?"
                me "We haven't seen anyone all morning, I'm sure we'll be fine. Come on, this way it'll be fair for me when we play."
                "Stephanie holds her racket and looks at it for a few moments then shakes her head."
                steph "Sorry [inputName], I don't think I can do it. Besides, it's just a friendly game. I'll go easy on you for a few matches."
                "Her eyes are looking more focused, she must have resisted the drug. Maybe you pushed her too far at once."
                me "Alright, fine. Lets play a few more matches and see how we feel."
                "You and Stephanie play a few more matches until you're both tired. As you head your separate ways you feel like you could have done something more with the situation."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_tennis_event_object.get_resist_change(0))
                $steph_tennis_event_object.inc_level(0)

        "Have her give you a blowjob.":
            $ action_difficulty = 45
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            me "I think I'm going to need a few minutes before we can start again. Seeing you in your tennis outfit got me a little... excited."
            "Stephanie looks down at your crotch, which is bulging against your pants."
            steph "Right, take as long as you need."
            me "Well, if you were willing to give me a little bit of help we could get back to playing a lot quicker."
            if stephO.check_willing(action_difficulty):
                steph "How long would it take otherwise?"
                me "With you still wearing that short skirt? We might be here for a while."
                "Stephanie thinks for a few long moments, then nods."
                steph "Okay, might as well speed things up. Sit down on the bench."
                "You do as she says, and she wastes no time in getting your pants down past your cock."
                show steph sportblow1 at right
                $ stephO.inc_blow()
                "She holds your cock in her hand and strokes it a few times, then licks you from base to tip. She repeats this until she's licked every side, then licks the top, swirling you around like a lollipop."
                me "That feels great."
                steph "Just wait until I really get started."
                "She places her mouth on the tip and slides you into her throat quickly. Her nose bumps into your stomach, and she flexes her throat around your cock."
                "Then she pulls almost off and repeats, picking up speed each time. After a few minutes she's running your entire length in and out of her throat as fast as she can manage."
                "With a wet pop she comes off of your cock and looks up at you."
                if stephO.cumslut:
                    steph "I really want you to cum in my mouth. Could you do that for me [inputName]? Could you give me a nice hot load?"
                    me "Yeah, I think I can do that for you."
                else:
                    steph "I left my change of clothes at home, so you're going to have to cum in my mouth. Okay?"
                    me "Ya, that's fine with me."
                "She smiles, then goes back to work on your shaft. In a few minutes time you feel your orgasm approaching and get ready to release."
                menu:
                    "Cum down her throat.":
                        show steph sportblow2 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "When you're ready you place a firm hand on the back of Stephanie's head and push her down as far as you can. She moans and doesn't fight you, and you feel your tip reach the back of her throat."
                        "You thrust your hips back and forth a few times, then begin releasing right down her throat. Stephanie works her tongue along your shaft the entire time, making the feeling even better."
                        "When you're done you let go and lean back with a sigh. Stephanie slowly and carefully slides back off your cock, then takes a deep breath."
                        if stephO.cumslut:
                            steph "Fuck, you tasted so good!"
                            "Stephanie leans forward and starts to lick the sides of your shaft, cleaning up every last drop of semen she can find."
                            steph "Mmm, thank you so much [inputName]. You know exactly what I want."
                        else:
                            steph "Thank you for making sure my outfit didn't get dirty."
                        me "Thank you for helping me out."
                        show steph sport at right
                        "She stands up and straightens her clothing."
                        steph "Alright, lets get back to it then!"

                    "Warn her and cum in her mouth.":
                        me "I'm almost there, get ready."
                        "Stephanie nods and garbles something past your cock. She blows you as fast as she can, and holds your tip against her tongue as you begin to tense up."
                        "You fire your load into her mouth, and she slides off of it carefully when you're done."
                        show steph sportblow3 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "She looks up at you and opens her mouth so you can inspect your handiwork, giving you a thumbs up."
                        "After a few seconds of showing off she closes and swallows."
                        show steph sport at right
                        if stephO.cumslut:
                            steph "Oh wow [inputName], you taste so damn good. I definitely needed that."
                            me "Me too. Thanks Stephanie."
                        else:
                            steph "Wow, well done. You definitely needed that."
                            me "I did. Thanks."
                        steph "No problem. Now, lets get back to the game!"
                "You struggle to your feet and do your best to put up a fight, but Stephanie is a far better player than you in your exhausted state. After a few matches you call it a day."
                "As you say goodbye and head home you feel like you've had a major effect on Stephanie today."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_tennis_event_object.get_resist_change(4))
                $steph_tennis_event_object.inc_level(4)
            else:
                steph "But what if someone came by? I don't want to get kicked out."
                me "We haven't seen anyone out here all morning, I'm sure we'll be fine. Come on, we can get back to playing faster this way."
                "Stephanie thinks about it for a few moments, then shakes her head."
                steph "I don't think it's worth the risk. We can just sit around until you're, um, better."
                "Her eyes look more focused, and her speech more determined. She must have resisted the drug, maybe she was pushed too far."
                me "Alright, fine. I guess we can just sit and wait."
                "You and Stephanie wait around for a few minutes until you're ready to play again. You play a few more matches, then say goodbye and head your separate ways."
                "As you watch Stephanie head off you feel like you could have done more with the siutation."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_tennis_event_object.get_resist_change(0))
                $steph_tennis_event_object.inc_level(0)

        "Fuck her on the tennis net.":
            $ action_difficulty = 60
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            me "I've been having fun with our game Stephanie, but I think I need to take a break and do something else."
            steph "What else would you like to do?"
            me "We've got the court all to ourselves, and you're wearing a skimpy little skirt. How about you bend over the net and we have some fun?"
            if stephO.check_willing(action_difficulty):
                steph "Oh, did I get you all worked up? I can't imagine how."
                show steph sportfuck1 at right
                "Stephanie bends over slightly to show off her butt and giggles."
                "You give her a hard slap on the ass and she yelps quietly."
                me "Come on, don't just tease me here."
                show steph sportfuck2 at right
                "Stephanie nods and walks over to the middle of the court. She leans on the stretchy material and sticks her ass in the air for you."
                steph "I'm all yours."
                "You walk up behind Stephanie and pull your cock out of your pants. You push her skirt up and out of the way, then bounce your tip on her tight ass cheeks a few times."
                show steph sportfuck3 at right
                "Stephanie reaches behind with one hand and pulls her panties down past her knees. She lets them fall to the ground then kicks them to the side."
                steph "Oh come on now, don't keep me waiting."
                $ stephO.inc_sex()
                "You line your tip up with her pussy and run it up and down, getting yourself wet with her juices. When you're ready you press forward slowly, slipping easily into her wet tunnel."
                steph "Ugh yes!"
                me "Easy there Steph, we don't want other people to hear us."
                if stephO.exhib:
                    steph "Fuck it, let 'em watch. I just want you to give me a good fuck right now."
                "You hold onto her hips and pump yourself back and forth slowly. You speed up as time goes on, watching how her ass jiggles with each stroke."
                "Stephanie moans and pants as you fuck her, putting more and more of her weight on the net."
                show steph sportfuck4 at right
                "After a few minutes of fucking her Stephanie is almost entirely supported by the net and bouncing back and forth on it with each stroke. Her pussy shakes around your cock as she reaches her own orgasm."
                steph "Don't stop fucking me."
                me "I don't plan on it."
                "You put some force behind your thrusts as Stephanie cums, enjoying the feeling of her convulsing pussy and twitching legs. The sight is enough to drive you towards your own orgasm too."
                menu:
                    "Cum inside of her.":
                        me "I'm almost there. I'm going to cum inside of you."
                        if stephO.cumslut:
                            steph "Oh yes, pump me full of your hot load! I don't care if you get me pregnant, just give it to me!"
                        else:
                            steph "Do it, keep fucking me!"
                        "You hold onto Stephanie's hips and pump as hard as you can until you're ready. Then you hold on and pull her tight against you, filling her up with your load."
                        "Stephanie moans loudly while you finish, and her legs twitch with each pulse of cum. When you're done, you step back take a deep breath."
                        show steph sportfuck5 at right
                        $ stephO.inc_cum_inside()
                        "She stays leaning on the net for a while, panting heavily. You watch as a line of cum drips out from her pussy and runs down her inner thigh."
                        "You admire your handiwork while Stephanie tries to stand on shaky legs."
                        show steph sport at right
                        "You both take a few minutes to catch your breath, then Stephanie slides her panties on again."
                        steph "Well, I think I'm worn out for today. Lets call it a day."
                        "As you head to the front you see Stephanie run a finger along her thigh. She looks at you and smiles, sticking her finger in her mouth and licking off the cum."
                        "As you say goodbye and head home you feel like you've made a [stephO.effect_string] impact on her today."

                    "Cum on her ass.":
                        me "I'm almost there. I'm going to cum all over you."
                        if stephO.cumslut:
                            steph "Mmm, yes! Cover me as much as you can, spray it all over my ass!"
                        else:
                            steph "Fine, just fuck me until the very end!"
                        "You hold onto Stephanie's hips and pump as hard as you can until you're ready. Then you pull out and stroke yourself off until you begin releasing."
                        show steph sportfuck6 at right
                        $ stephO.inc_cum_over()
                        "You fire your load onto the back of her clothes, then aim closer to yourself and land a few spurts over each ass cheek. When you're done you drop your cock onto her ass and take a deep breath."
                        "You both take a few minutes to catch your breath, then Stephanie uses her panties to wipe up some of the cum on her ass and back."
                        "When she's finished she shoves them in her bag."
                        show steph sport at right
                        steph "Well, I think I'm worn out for today. Lets call it a day."
                        "As you head to the front stephanie makes a point of bending over to check her shoes. She flashes her naked and wet pussy at you, then stands up and walks on like nothing happened."
                        "As you say goodbye and head home you feel like you've made a [stephO.effect_string] impact on her today."

                    "Cum in her mouth.":
                        me "I'm almost ready. I want to cum in your mouth."
                        steph "Fuck ya! I want to swallow your entire load!"
                        "You give Stephanie a few more good thrusts, then pull out and hop over the net."
                        "Stephanie looks up and opens her mouth wide for you. You slide in and fuck her face for a few moments while you get ready to cum."
                        show steph sportfuck7 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "As you tense up and begin releasing, Stephanie holds you in her mouth and locks eyes with you. She doesn't move as she takes every drop in her mouth, then she opens to show it off."
                        me "Fuck you look good like that."
                        "Stephanie smiles and blows bubbles through the cum puddle as best she can. Then she closes her mouth and swallows loudly."
                        steph "I think I'm worn out, lets call it a day."
                        show steph sport at right
                        "Stephanie slips her panties back on and rearranges all her clothing."
                        "You and Stephanie walk to the front and say goodbye. As you're watching her leave you feel like you've made a [stephO.effect_string] impact on her."

                    "Cum on her face.":
                        me "I'm almost ready to cum. I want to finish on your face."
                        if stephO.exhib or stephO.cumslut:
                            steph "Fuck, okay! Hurry up and cover me then!"
                            "You pull out of her with a wet pop and hop over the net, standing in front of her while you stroke yourself off."
                            show steph sportfuck8 at right
                            $ stephO.inc_cum_over()
                            "Stephanie looks up at your cock, leaving her mouth open and tongue out as you start to empty your balls onto her. When you're done you take a deep breath and admire your work."
                            me "Fuck you look good like that."
                            "Stephanie smiles and stands up, her legs still shaky underneath her. She grabs her panties and pulls them back on, but doesn't move to clean off your load."
                            steph "Come on, we should probably get moving in case someone heard us going at it."
                            "You and Stephanie walk to the front of the building, stopping by the front desk for a quick goodbye. Stephanie doesn't wipe your sperm off until you're out the door."
                            "As she heads off you feel like you've had a [stephO.effect_string] impact on her today."
                        else:
                            steph "Fuck that! I want you in my mouth, I want to swallow your cum!"
                            "You think about it for a moment, but you don't exactly have time to negotiate."
                            me "Fine. Here I come!"
                            "You give Stephanie a few more good thrusts, then pull out and hop over the net."
                            "Stephanie looks up and opens her mouth wide for you. You slide in and fuck her face for a few moments while you get ready to cum."
                            show steph sportfuck7 at right
                            $ stephO.inc_cum_mouth()
                            $ stephO.inc_cum_swallow()
                            "As you tense up and begin releasing Stephanie holds you in her mouth and locks eyes with you. She doesn't move as she takes every drop in her mouth, then she opens to show it off."
                            me "Fuck you look good like that."
                            "Stephanie smiles and blows bubbles through the cum puddle as best she can. Then she closes her mouth and swallows loudly."
                            steph "I think I'm worn out, lets call it a day."
                            show steph sport at right
                            "Stephanie slips her panties back on and rearranges all her clothing."
                            "You and Stephanie walk to the front and say goodbye. As you're watching her leave you feel like you've made a [stephO.effect_string] impact on her."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_tennis_event_object.get_resist_change(5))
                $steph_tennis_event_object.inc_level(5)
            else:
                steph "Right in the middle of the court? But anyone could see us there!"
                me "I'm sure it'll be okay, we haven't seen anyone all morning. It'll be a lot of fun, I promise."
                steph "But I like my Sunday habits, I wouldn't want to get kicked out. I don't think it's worth the risk."
                "Stephanie shakes her head a few times, and her eyes seem more focused than before. She must be resisting the drug."
                me "Fine, never mind then. We can play a few more matches whenever you're ready, then we'll call it a day."
                steph "Fine, give me a few moments to clear my head."
                "You and Stephanie play for the rest of the morning, then head your separate ways. As you head off you feel like you could have done more with the situation."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_tennis_event_object.get_resist_change(0))
                $steph_tennis_event_object.inc_level(0)

    jump jumpTimeSkip

label maj_stephParty:
    $ steph_party_event_object.happened = True
    $temp_slut_score = stephO.slut_score
    call serum_give(stephO) from _call_serum_give_14
    $ temp_slut_score = _return
    "You stealthily mix some serum into Stephanie's drink. She gets back a few minutes later."
    show steph casual at right
    steph "Ah, much better. Now lets go, you're looking so lonely all by yourself!"
    "She downs the rest of her drink in one go, then grabs your hand and pulls you to the center of the room. She throws her arms up and starts to dance, singing along with the music."
    "You do your best to keep up, but it's clear she's a much better dancer than you are."
    me "How are you feeling Steph?"
    steph "Great! It's been so long since I got to do this!"
    "Her eyes are slightly unfocused as she sways to the music."
    #Dancing with groping, goes both ways
    menu:
        "Grope her on the dance floor.":
            $ action_difficulty = 0
            $stephO.set_action_exhib()
            $stephO.set_action_freeuse()
            $stephO.check_willing(action_difficulty)
            ##success
            me "Good, you deserve a good time out. We've been working hard this whole summer."
            steph "Right? It's good to get out and relax."
            "The music changes to something a little slower, and a few people move off to get fresh drinks."
            me "I should thank you for inviting me out tonight. Would you give me the honour of dancing with me?"
            "You hold out your hand to her."
            steph "Of course, [inputName], it would be my pleasure."
            show steph strip20 at right
            "Stephanie takes your hand and you pull in close. You wrap your other arm around her and the two of you start to slow dance."
            "As the dance goes on you drop your hands lower, sliding them over her waist and onto her ass."
            steph "Well hello there, like what you feel?"
            "You give her ass a good squeeze, and she pulls tighter against you."
            me "I do, you've got a great butt."
            "To emphasise the point you give one of her cheeks a good smack through her skirt."
            steph "Ah! Two can play at that game then!"
            show steph strip21 at right
            "Stephanie slides one of her hands off your shoulder and runs it down the front of your body. She ends with it cupping your crotch, rubbing up and down gently."
            "The two of you dance like this for a minute or two, rubbing each other as you spin around."
            "Eventually the song starts coming to an end. You pull Stephanie close one last time and give her a deep kiss, then let her go."
            me "Thank you for the dance Stephanie."
            steph "My pleasure, [inputName]. We should do it again some time."
            show steph casual at right
            "You spend the rest of the evening chatting with some of Stephanie's friends and drinking a little."
            "As the night wears on the party shows no signs of stopping but you're beginning to feel worn out. You find Stephanie to say your goodbyes, then head out and catch a bus home."
            $stephO.change_slut_rebalanced(action_difficulty)
            $stephO.change_resist(steph_party_event_object.get_resist_change(1))
            $steph_party_event_object.inc_level(1)


        "Have her strip for everyone.":
            $ action_difficulty = 15
            $stephO.set_action_exhib()
            #Gives everyone a show.
            me "Good, you deserve a good time out! Everyone is here to cut loose and relax anyway, right?"
            steph "Right! Now come on, you can't avoid this dance all night."
            me "How about you give everyone a show Stephanie? You're looking great today, and this party could really use a little R-rated action to liven it up."
            if stephO.check_willing(action_difficulty):
                "Stephanie bites her lip a little while she thinks, then nods."
                steph "The girls are going to go crazy! They use to throw parties like that all the time."
                "She steps into cleared area of the room that's become the dance floor and launches into an impressive dance routine."
                show steph strip22 at right
                "A little ways into it, stephanie pulls her shirt up and off, spinning it in the air a few times before launching it towards you."
                "The crowd takes a moment to notice Stephanie dancing without her shirt on in the middle of the room. Finally someone woops and starts to clap for her."
                $ stephO.inc_naked()
                "Stephanie smiles and keeps moving around with the music, keeping her arms high so her tits are in full view for everyone."
                show steph strip23 at right
                "Next, she spins around and undoes her skirt quickly. She lets it fall to the ground and bends over to give everyone a good view of her ass."
                "A few guys have gotten their phones out and are filming Stephanie as she dances around now. The rest are cheering her on, chanting \"tits, tits, tits!\"."
                "Stephanie reaches behind her back and undoes her bra, then slips her hands forward and holds it in place."
                show steph strip24 at right
                "Everyone seems to hold their breath, then she pulls her bra off completely and throws it into the crowd."
                "Guys cheer and woop while Stephanie moves back and forth, shaking her free tits left and right. A few girls who you recognize as Stephanie's friends are cheering for her too."
                "For a few minutes Stephanie is center stage dancing around with just her panties on. A few people call for her to take them off too, but she just ignores them."
                show steph casual at right
                "Finally the song draws to a close and Stephanie ends her dance. Her friends run forward and high five her, then help her get her skirt back on."
                "You pass her shirt back, but it seems like her bra has disapeared completely. Finally she shrugs and just goes braless for the rest of the night."
                "You stay at the party for another hour, but don't get much time with Stephanie again. When you're feeling tired you say your goodbyes and catch a bus home."
                "You feel confident you had a major effect on Stephanie tonight."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_party_event_object.get_resist_change(2))
                $steph_party_event_object.inc_level(2)
            else:
                #failure
                "Stephanie bites her lip a little while she thinks, then shakes her head."
                steph "The girls would go crazy if I did, but I stopped doing that a while ago with them."
                me "Oh come on, just a little show for us wouldn't hurt."
                steph "Maybe not, but I don't want the drama. Now come on, I want to have a dance with you!"
                "She must have resisted the serum. Trying to push her any farther might be a bad idea."
                "You and Stephanie share a dance together, but it's clear she's much better than you are."
                "Afterwards you hang around for another hour until you're feeling worn out, then say goodbye and catch a bus home. You feel like you could have accomplished more tonight."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_party_event_object.get_resist_change(0))
                $steph_party_event_object.inc_level(0)

        "Have her give you a handjob.":
            $ action_difficulty = 30
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            #Pulls you aside to give you a handjob
            me "There's actually something I'd like a little more than a dance with you."
            steph "And what would that be?"
            me "Your outfit got me hard, I'd like you to give me a hand taking care of it."
            if stephO.check_willing(action_difficulty):
                #success
                "Stephanie seems to think about it for a long while before responding."
                steph "It would be cruel for me to leave you like that all night. Follow me."
                "Stephanie leads you through the house and up some stairs to the second floor. The first room she tries is locked, but the second one is open."
                "She pulls you into a small bedroom, then locks the door behind the two of you."
                steph "Now, you have something you'd like me to take care of?"
                me "Indeed I do."
                "You sit on the bed and slide your pants down around your ankles, revealing your hard shaft."
                show steph hand4 at right
                "Stephanie sits beside you and runs a hand up your thigh, then along your cock. She rubs her thumb along the back of your tip a few times."
                $ stephO.inc_hand()
                steph "Well then, I'll do my best with it."
                "She wraps her hand around you and starts to stroke you off. Her hand is soft and warm, and she definitely knows what she's doing."
                me "Ahh, that feels great."
                steph "Good. Just relax and let me take care of you."
                "She pushes your shoulder with her other hand and makes you lie down while she gives you a handjob."
                "A little while later she stops for a moment, spits a few times into her hand, then rubs you a few times to get everything wet and slippery."
                me "Oh fuck."
                steph "Are you almost there?"
                me "Ya. Keep going."
                steph "You're going to cum in my mouth, okay?"
                "She speeds up, sliding her wet hand along the length of your shaft as fast as she can."
                me "Oh ya, that's fine. Get ready!"
                show steph hand5 at right
                "Stephanie leans over your cock while she strokes you to completion. She opens her mouth and places it above the tip of your cock."
                $ stephO.inc_cum_mouth()
                $ stephO.inc_cum_swallow()
                "You tense up and begin firing your load into her mouth. She moans a little as the first pulse lands inside, and keeps rubbing you until you've finished."
                me "Damn, that was amazing."
                "Stephanie closes her mouth and swallows quietly, then looks up and smiles."
                show steph casual at right
                steph "I'm glad you liked it. Now, we should get back before anyone notices we're gone."
                me "Right, of course."
                "You follow Stephanie back downstairs. You hang around for another hour, then say goodbye to Stephanie and catch a bus back home. You feel confident you had a major effect on her today."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_party_event_object.get_resist_change(3))
                $steph_party_event_object.inc_level(3)

            else:
                #failure
                "Stephanie seems to think for a long while before responding."
                steph "I don't think so. Not right now at least. I'm sure you can survive the night if you have to."
                me "Aw, come on, just a few minutes."
                "She shakes her head, then turns around and sticks her ass out towards you."
                steph "Sorry, you'll just have to deal with all my teasing. Now come on, lets dance!"
                "Stephanie must have resisted the serum. No point trying to push it any farther."
                me "Fine, lets dance then. Just try and contain your raw sexuality."
                "You and Stephanie share a dance together, and she shows off how much better she is than you."
                "Afterwards you hang around for another hour until you're feeling worn out, then say goodbye and catch a bus home. You feel like you could have accomplished more tonight."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_party_event_object.get_resist_change(0))
                $steph_party_event_object.inc_level(0)

        "Have her blow you on the couch":
            $ action_difficulty = 45
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            #Gives you a blowjob on the couch
            me "Actually, there's something I'd like more than a dance with you right now."
            steph "And what would that be?"
            "You wrap your arms around her waist and pull her close, so you can whisper in her ear."
            me "I'm rock hard. I want to feel your mouth around my cock."
            if stephO.check_willing(action_difficulty):
                #success
                "There's a short pause, then she whispers back."
                steph "You don't have a problem with crowds, do you?"
                "She reaches down with one hand and rubs your crotch."
                me "I think I'll be fine. I don't know anyone here anyway."
                "Stephanie pulls away and smiles, then grabs your hand and pulls you across the room to a couch."
                steph "Sit down, let me take care of everything."
                "You nod and do as she says. There are five or so other people in the room in small groups, talking to each other and having a few drinks."
                "Stephanie pushes your legs to the side and kneels down, then reaches up and pulls your pants down low enough to free your cock."
                show steph blow12 at right
                "She holds your shaft in one hand and runs her tongue along the bottom, gives the tip a little kiss, and finally slips it into her mouth and starts to blow you."
                $ stephO.inc_blow()
                "You lean back and enjoy the feeling of Stephanie's wet mouth and nimble tongue."
                "A few of the people in the room have noticed what's going on now. One points you out to his friend, then raises his drink in your direction in congratulations."
                "Stephanie keeps focused on her task, taking your cock deep into her throat with each pass."
                "She brushes her hair to the side and makes eye contact with you, then slides herself as deep as she can go and holds herself there."
                "Long seconds tick past with your dick firmly planted down Stephanie's throat. She tightens and relaxes a few times, and runs her tongue along the bottom."
                "A small crowd is watching you two now. A girl who you recognize as one of Stephanie's friends woo's for her as she holds herself down longer and longer."
                "Finally, Stephanie pulls up and takes gasps of air. The crowd erupts into applause and yelling. Stephanie wastes no time and goes back to blowing you quick and deep."
                "It doesn't take much more before you're feeling ready to finish. You tap Stephanie on the shoulder a few times to get her attention."
                "She pulls off and smiles at you."
                steph "Almost there?"
                me "Ya, almost."
                if stephO.cumslut:
                    steph "Good, I want to guzzle down that hot jiz. Give me as much as you can, I want it all."
                else:
                    steph "Good, I want you to cum in my mouth."
                "Without another word she puts you back in her mouth and slides up and down some more."
                "The crowd of people watching have formed a semicircle around the couch. A few people have their phones out and are filming Stephanie as she goes down on you." ##Appears somewhere on the internet?
                show steph blow13 at right
                "A moment later you can feel your orgasm building up. Stephanie pulls back and holds your tip just inside her lips, grabs your wet shaft with one hand, and starts to stroke you off."
                "You fire off your load into Stephanie's waiting mouth to the cheers of the people around you. Stephanie closes her eyes and moans softly while you unload, and keeps stroking you until you're completely finished."
                show steph blow14 at right
                "After that she pulls off and looks up at you, opening her mouth for you and moving her head left and right so you can get a good look."
                "Blonde Girl" "Stephanie, you huge slut!"
                $ stephO.inc_cum_mouth()
                $ stephO.inc_cum_swallow()
                show steph casual at right
                "The blonde who opened the door for you steps out of the crowd. Stephanie stands up and swallows, then turns to face her."
                "Blonde Girl" "I knew you had it in you."
                if stephO.cumslut:
                    steph "How could I resist, it just tasted so good."
                    "You pull up your pants again and smile at the two girls."
                    "Blonde Girl" "Oh? How good could it possibly be. Here, let me have a taste."
                    "The blonde steps up to Stephanie and kisses her. Stephanie doesn't hesitate, and you can see their tongues wrap around each others for a few seconds."
                    "Eventually they break, and the blonde turns back to you."
                    "Blonde Girl" "Alright, I think I see what she's getting at. Maybe you'll have to give me a proper taste one day."
                    "She looks down at your crotch and bites her lip."
                    "Blonde Girl" "I'm going to have to steal your girlfriend for a few minutes though, I think I owe her a drink after that."
                else:
                    steph "Well, just for my friend here."
                    "You pull up your pants again and smile at the two girls."
                    "Blonde Girl" "Oh, it must be serious if you're going to suck him off in public."
                    "The blonde smiles and winks at you."
                    "Blonde Girl" "I'm sure I can pull you away for a few minutes though. I owe you a drink after all that."
                hide steph
                "The blonde grabs Stephanie's hand and pulls her away. Stephanie turns around for a moment and waves, then is pulled into the crowd."
                "A few guys come up and clap you on the back. You also notice a few other couples getting a little handsy with each other after your show."
                "You hang around for a little while longer at the party, but Stephanie is nowhere to be seen for the rest of the night."
                "Eventually you slip out and catch a bus home, certain you've had a major effect on her tonight."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_party_event_object.get_resist_change(4))
                $steph_party_event_object.inc_level(4)

            else:
                #failure
                "Stephanie thinks about it for a long time, while you hold her close and dance slowly with her."
                steph "I don't think that would be a good idea. There are a bunch of people around here that I know."
                me "I doubt they would mind. It's just two people having fun, right?"
                "Stephanie rests her head on your shoulder."
                steph "Not today. How about we just enjoy a dance, okay?"
                "She must have resisted the drug, there's no point pushing it any farther."
                me "Alright, that sounds nice too."
                "You and Stephanie share a slow dance together. When you're finished she lets go and steps away to spend some time with her other friends."
                "You hang around for another hour until you're feeling worn out, then say goodbye and catch a bus home. You feel like you could have accomplished more if you didn't push her so far."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_party_event_object.get_resist_change(0))
                $steph_party_event_object.inc_level(0)

        "Fuck her on the couch.":
            #Fucks you (and other people?) on the dance floor.
            me "Actually, how about we do something other than dance."
            steph "I'm all ears."
            me "How about I bend you over that couch and give your pussy a good pounding?"
            $ action_difficulty = 75
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            if stephO.check_willing(action_difficulty):
                #success
                "Stephanie looks at you and smiles. She wraps her arms around your waist and pulls you close so she can whisper in your ear."
                steph "Do you think you can handle the pressure? All these people watching you as you fuck me?"
                show steph strip20 at right
                "You grab her head and kiss her. Your tongues meet and wrap around each other for a few moments until you break the kiss and pull back."
                me "I think I can manage."
                show steph fuck20 at right
                "She pulls away and walks over to the couch you pointed out. Without hesitating she bends over and pulls her skirt up, shaking her ass at you."
                "A few people glance over, and one guy whistles in appreciation."
                "You step up behind Stephanie and give her ass a good smack, then plant both hands on her cheeks and knead them for a moment."
                "Stephanie moans softly while you play with her ass. When you reach a hand between her legs her juices have soaked completely through her panties."
                show steph fuck21 at right
                "You pull her panties down and let them fall to the ground, then pull your cock out and let it bounce on one of her cheeks."
                "A small crowd of people have noticed what's going on and are watching you two now, calling loudly for their friends to come over."
                "You line your hard cock up with Stephanie's slit and run it up and down a few times, then press forward and slip into her."
                $ stephO.inc_sex()
                "She moans loudly, and the whole crowd cheers. There's applause as you settle into a steady rhythm pumping back and forth."
                "Stephanie places her head against the back of the couch as she gets rocked back and forth with each thrust. She's clearly making no attempt to stay quiet, and keeps moaning loudly as you fuck her."
                "After a few minutes you pull out of Stephanie's wet pussy. There are groans from the crowd, and Stephanie looks back with a confused look."
                "You sit down on the couch and spread your legs."
                me "Come on, come sit on my cock."
                "The crowd cheers again as Stephanie turns around and gets positioned above your lap. As a last thought, she pulls her shirt off, then drops her bra to the ground too."
                show steph fuck22 at right
                "You hold your shaft still while Stephanie lowers herself down. She gasps as you slip back into her, then sits down completely to push you as deep as possible."
                "After a pause she leans forward and starts to work her hips to slide you in and out of her."
                "Blonde Girl" "Stephanie, you huge slut!"
                "The blonde girl who let you into the house bursts through the crowd and stands in front of you while Stephanie rides your cock."
                show steph fuck23 at right
                "Stephanie doesn't stop, but looks up and pants out a reply."
                if stephO.exhib or stephO.cumslut:
                    steph "You know it! Fuck, he feels so big too!"
                    "The blonde steps closer and places her hands on Stephanie's hips, guiding them up and down even faster."
                    "Blonde Girl" "Come on, you can do better than that. You want to make him cum, right?"
                    steph "Oh ya! Ah!"
                    "Blonde Girl" "They you have to work for it! There we go!"
                else:
                    steph "What, a girl can't have some fun?"
                    "Blonde Girl" "Of course you can, I just didn't think you were so... forward any more."
                    "Blonde Girl" "Good on you! Ride em cowgirl!"
                "The blonde holds up her hand, and Stephanie gives her a high five while she fucks you."
                "Meanwhile, the rest of the crowd is cheering you on. A few couples have even started to play with each other too. At least two girls have their shirts off, and someone is on their knees on the far side of the room."
                "Stephanie's tight pussy has driven you to the edge though, and you can feel your orgasm start to build."
                menu:
                    "Cum inside her.":
                        me "Steph, I'm almost there. Don't stop!"
                        "You place your hands on her hips and guide her up and down as fast as she can manage. Her breath comes in gasps as you fuck her."
                        $ stephO.inc_cum_inside()
                        "Finally you start to cum inside of Stephanie. She keeps fucking you the whole time, mixing moans and gasps while your seed makes her even slipperier inside."
                        "The crowd cheers and drinks are chugged as Stephanie collapses backwards, pussy twitching around your shaft, and tries to catch her breath."
                        show steph fuck24 at right
                        "She lifts up just enough to let your cock slip out of her, then sits on your lap while she recovers."
                        "You reach a hand around her and play with her tits gently while your cum leaks out of her and onto the couch."
                        "Blonde Girl" "Wow, it looks like he really filled you up!"

                    "Cum in her mouth.":
                        me "Steph, I'm almost there. You're going to drink my cum!"
                        steph "Oh god, yes! I want it in my mouth!"
                        "The crowd cheers as you grab her hips and guide her up and down as fast as she can manage. When you're right on the edge you pull her up, and she spins and drops to her knees."
                        show steph fuck26 at right
                        "Stephanie slips your cock into her mouth and starts to blow you. Almost immediately you start to release your load in her mouth and down her throat."
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        show steph fuck27 at right
                        "When you're finally done, Stephanie sits back and pauses for a moment with a mouth full of cum."
                        "Blonde Girl" "Come on Stephanie, you know that all good girls swallow."
                        "Stephanie nods, and you can see her throat work up and down as she swallows your entire load."
                        "Blonde Girl" "There we go, that's the slut I know! A big hand for Stephanie everyone!"
                        "The crowd erupts in applause while Stephanie sits on the floor and catches her breath."

                    "Cum on her face.":
                        me "Steph, I'm almost there. I'm going to finish on your face and show everyone what a slut you are."
                        "Stephanie nods and moans. You grab her hips and start to guide her up and down as fast as she can manage."
                        "When you're right on the edge you pull up on her hips to get her to move. She pulls off of you with a wet pop and spins around, landing on her knees."
                        $ stephO.inc_cum_over()
                        me "Tilt your head back."
                        show steph fuck25 at right
                        "Stephanie looks up at you and opens her mouth, sticking her tongue out. You stroke yourself off and start to fire your load on her face."
                        "The crowd erupts into applause as your first blast of cum lands. You fire a few pulses onto her forehead, then work your way down to her nose, mouth, then dribble the last bit on her chin."
                        "Blonde Girl" "There we go girl, take his load all over your face!"
                        "When you're done you sit back on the couch and take a moment to appreciate Stephanie's glazed face."

                show steph casual at right
                "When Stephanie recovers her friends group around, seemingly to congratulate her. She's guided away to get cleaned up, and comes back to see you a few minutes later."
                "The party seems to be dying down now, as more and more people pair off and leave to find somewhere more private."
                if stephO.freeuse:
                    steph "Hey [inputName]. The girls seem to have something going on, so I'm going to head off with them. I think they've got some guys lined up for us at another party. I had a great time with you though."
                    me "Yeah, you were amazing. Have fun, I'll see you around."
                else:
                    steph "Hey [inputName]. I think I'm going to head off soon. I had fun, by the way."
                    me "Me too, you were amazing."
                "She smiles, gives you a hug, then waves goodbye as she heads back to her friends. You grab a bus afterwards and head home soon after, confident you've had a [stephO.effect_string] impact on her tonight."
                $stephO.change_slut_rebalanced(action_difficulty)
                $stephO.change_resist(steph_party_event_object.get_resist_change(5))
                $steph_party_event_object.inc_level(5)

            else:
                #failure
                "Stephanie looks at you and bites her lip a little while she thinks it over."
                me "Come on, it'll be fun."
                steph "Oh, I know it would. There are just a bunch of people here that I know, and that would make a big deal out of it."
                me "How bad could it be?"
                steph "Pretty bad."
                "She seems to make up her mind and shakes her head."
                steph "No, how about we just enjoy a dance together instead."
                "Stephanie must have resisted the drug. There's no point pushing her any farther right now."
                me "Okay, that sounds nice too."
                "You and Stephanie share a dance together, and she shows off how much better she is than you. When you're done she goes to spend some time with her other friends."
                "You hang around for another hour until you're feeling worn out, then say goodbye and catch a bus home. You feel like you could have accomplished more tonight though."
                $stephO.change_slut_failed()
                $stephO.change_resist(steph_party_event_object.get_resist_change(0))
                $steph_party_event_object.inc_level(0)
    jump jumpTimeSkip

label maj_stephConvinceAssistant:
    $ temp_slut_score = stephO.get_serum_result("blue")
    me "Yep, managed to drag myself out of bed. How's everything here?"
    steph "Actually [inputName], I was doing the inventory yesterday, and I noticed something strange."
    "You freeze, heart beating heavily in your chest."
    steph "Ya, we're low on a bunch of supplies that we haven't been using for months. I was wondering if you put them somewhere else or something."
    me "Uh, nope. Haven't seen them around."
    steph "Damn. I'll have to tell Nora then, and she'll have to do a full review of the security camera footage to be sure. It probably just got put into a different cabinet at some point."
    "If Nora checks the cameras she'll discover your little science experiment. You can't let that happen! Thinking fast, you come up with the best lie you can."
    if blueberry_event_object.happened == True:
        "Besides, it worked once already."
    me "Actually, I have a confession to make. I've been preparing a surprise for you and Nora, but it isn't ready yet."
    steph "Seriously? I've been panicking over this inventory for a week now!"
    me "I'm so sorry, I didn't realise you guys even kept an inventory of all this stuff."
    steph "Well we do. I'll need to know what you've been doing with it so I can write up a report."
    me "Okay, of course. I've been doing some side work with another professor looking at flavour composition. It's an interesting chemical engineering challenge to emulate taste exactly."
    steph "Sure, I guess. What were you doing here though?"
    me "Well, we finally figured out how to perfectly replicate blueberry. I've been working on a mixture for you and Nora to try with some of the leftover supplies here in the lab."
    steph "That's a nice thought, but it's screwed up the reports here pretty bad."
    me "Damn, I'm really sorry. I've almost finished though, there's just one last step I needed to do before it was ready for you two."
    me "Think we could finish it right now, that way I at least have something to give Nora as an apology?"
    "Stephanie glares at you, but eventually softens and nods."
    steph "Alright, we'll finish it up right now before Nora gets back. But you have to explain the shit show you've caused to her."
    me "Deal."
    "With Stephanie's help you're able to produce some blue serum in record time. Having her as a lab assistant right now gives you an idea."
    steph "So that's it?"
    "She motions to the little vial of blue you've made."
    me "Yep, that's it. Tastes so much like blueberry you can't tell it apart."
    me "Give it a try. I planned to make two batches anyway."
    "Stephanie takes the vial from you and thinks about it. She opens the top and smells it."
    steph "It doesn't smell like blueberry."
    me "Ya, we're still working on that though. Taste it, it's perfect."
    "She raises the vial to her lips and tips a small amount into her mouth."
    steph "Uh, I don't think that's blueberry at all."
    me "Are you sure? Try the rest."
    "Stephanie looks concerned, but the drug is already taking effect. She drinks the rest of the vial and puts it down on the counter."
    steph "Nope, still not tasting it."
    me "How do you feel though? Relaxed?"
    "Stephanie nods slowly."
    me "Good. There are a few things I wanted to talk to you about before Nora shows up."
    steph "What do you mean?"
    me "First, I don't think Nora needs to know about the inventory problems. Just tell her that some of the supplies went bad and had to be disposed of."
    "Stephanie nods, eyes unfocused."
    me "Second, I have a few lab projects I need help with. You know more about biology than I do, and I would appreciate some help."
    steph "What kind of help?"
    me "If I come in early to the lab and you're here, I want you to help me with whatever I ask, okay? I'll bring any extra supplies we need for it."
    "Stephanie nods again."
    steph "Okay, I can do that."
    me "Finally, I want you do one thing for me."
    menu:
        "Have her show off her tits.":
            $ action_difficulty = 0
            $stephO.set_action_exhib()
            $stephO.check_willing(action_difficulty)
            me "I want you to pull your shirt up for me. Can you do that for me Stephanie?"
            "She hesitates, then nods."
            steph "Okay, sure."
            show steph strip8 at right
            $ stephO.inc_naked()
            "Her hands grab the bottom of her shirt and pull it up. She catches her bra as she goes and pulls it up out of the way too."
            "Her tits fall out from the bottom of a bright pink bra and jiggle for a few seconds."
            "She looks away nervously while you stare, but makes no move to cover up again."
            me "That's great Stephanie. Give your nipple a pinch for me."
            show steph strip9 at right
            "She takes her hard nipple in-between her thumb and forefinger and rolls it gently. She gasps quietly."
            me "Perfect. Okay, you can put them back. We don't want Nora to catch us here."
            show steph work at right
            "Stephanie pulls her shirt down again and wiggles her tits back into their cups."
            "You make small talk for a few minutes like nothing happened, and eventually head out of the lab for a while, confident you made a [stephO.effect_string] impact and got yourself an assistant."
            $stephO.change_slut_rebalanced(action_difficulty)
        "Have her get naked.":
            me "I want you to take your clothes off for me. So I know I can trust you."
            $ action_difficulty = 15
            $stephO.set_action_exhib()
            if stephO.check_willing(action_difficulty):
                steph "You want me to get naked?"
                me "That's right. If you trust me that much I can trust you to keep quiet in front of Nora."
                show steph strip3 at right
                "Stephanie reaches for her sweater, pauses, then nods and pulls it up over her head. She throws the sweater onto a chair, then reaches for her pants."
                show steph strip1 at right
                "She unzips her pants and slips them down. She stands still for a moment in her bright pink underwear."
                me "Good work, keep going."
                steph "Okay. If you want me to."
                show steph strip2 at right
                $ stephO.inc_naked()
                "She reaches behind her back and undoes her bra. She slips it forward and off, and drops it too. Finally she drops her panties to past her thighs and onto the ground."
                steph "There, is this good?"
                me "Give me a little spin, show me your ass."
                show steph strip10 at right
                "Stephanie spins for you, pausing to wiggle her ass towards you."
                me "Perfect. You look perfect."
                show steph strip11 at right
                "Stephanie faces you and spreads her legs slightly so you can get a good look at her pussy."
                me "Alright, that's enough. You should get dressed before Nora shows up."
                steph "Okay. Trust me now?"
                me "I trust you, just keep this between us."
                show steph work at right
                "Stephanie collects her clothes and begins putting them on as you slip out of the lab. You feel confident you've had a major effect and secured yourself a lab assistant."
                $stephO.change_slut_rebalanced(action_difficulty)
            else:
                steph "You want me to get naked? How will that let you know you can trust me?"
                me "If you trust me enough to get naked, I can trust you not to tell Nora anything."
                steph "But if Nora walks in now, she'll see everything."
                me "We better hurry up then, right?"
                "Stephanie hesitates, then shakes her head."
                steph "No, we can't do that. I'll help you but I can't strip right now."
                "Damn, she must have resisted the drug now. Maybe this last step was too far."
                me "Okay, I'll just have to take your word for it."
                "You and Stephanie make small talk, then you slip out of the lab. You're confident that you could have done more with the situation, but at least you have an assistant now."
                $stephO.change_slut_failed()
        "Have her jerk you off.":
            me "I need to know I can trust you Stephanie, if you tell Nora we'd both be in a lot of trouble."
            steph "How can I make sure you trust me?"
            me "I want you to give me a handjob until I cum, okay?"
            $ action_difficulty = 30
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            if stephO.check_willing(action_difficulty):
                steph "A handjob?"
                "She pauses to consider, shifting her weight from foot to foot."
                me "Right, just a simple handjob. If I can trust you with my penis I can trust you with that inventory report."
                steph "Okay, I guess that makes sense."
                "You pull up a chair and stephanie kneels in front of you. She wastes no time and pulls your pants down, revealing your hard cock."
                show steph hand1 at right
                $ stephO.inc_hand()
                "She takes you up in one hand and begins stroking you gently."
                "You moan quietly as she rubs your shaft. You sit back and enjoy the feeling for a few minutes."
                "She clearly knows what she's doing, and within a few minutes she has you close to cumming already."
                me "I'm almost there Stephanie, you're doing a great job."
                steph "Good. Finish and then we can clean up before Nora shows up."
                "Her hand speeds up and your own precum lubricates her hand. A few more strokes and you begin to spasm and shoot your load."
                "Stephanie points your cock to her side and rubs you while you shoot spurts of cum past her shoulder onto the floor. When you're done, she lets go of you slowly and wipes her hand on her sweater."
                me "And there it is. That was great."
                show steph work at right
                "Stephanie stands up and nods. The two of you get the lab cleaned up and slip out before Nora shows up for the day. As you say goodbye you're confident you had a major effect and secured a lab partner."
                $stephO.change_slut_rebalanced(action_difficulty)
            else:
                steph "A handjob? Here in the lab?"
                me "Right. If I can trust you with that I can trust you to keep this from Nora."
                steph "But how can I trust you?"
                me "You've got the inventory logs, you don't need to trust me."
                steph "If Nora finds us we'd both get fired. I'm not going to take that risk for you. You'll just have to trust me."
                "Damn, she must have resisted the drug now. Maybe this last step was too far."
                me "Okay, I'll just have to take your word for it."
                "You and Stephanie make small talk, then you slip out of the lab. You're confident that you could have done more with the situation, but at least you have an assistant now."
                $stephO.change_slut_failed()
        "Have her give you a blowjob.":
            me "I need to know I can trust you Stephanie, if you tell Nora we'd both be in a lot of trouble."
            steph "How can I make sure you trust me?"
            me "I want you to give me a blowjob and make me cum."
            $ action_difficulty = 45
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            if stephO.check_willing(action_difficulty):
                "She thinks about it for a few moments, then nods."
                steph "Okay, but I get to swallow it."
                me "No argument here."
                "You pull up a chair and stephanie gets on her knees in front of you."
                show steph blow7 at right
                $ stephO.inc_blow()
                "With quick hands she undoes your pant's zipper and pulls them down to your ankles. She wastes no time and gives your hard shaft a lick from base to tip."
                "She slips her mouth over your tip and slides your wet cock down her throat. She starts stroking her head up and down your shaft at a steady pace, flicking your tip with her tongue at the top."
                me "That feels great. You're doing a great job."
                "Stephanie doesn't respond, but keeps blowing you. One of her hands gently massages your balls while she sucks you off."
                "After a few minutes you feel your orgasm building up."
                me "I'm getting close. You want to swallow it, right?"
                "Stephanie pulls off your cock with a wet pop."
                steph "Right. I want you to shoot it into my mouth, then I'll swallow it."
                "She goes back to sucking you, moving faster now."
                "A few more seconds of her wet throat around you and you're ready. You tense up, and Stephanie pulls your tip back into her mouth."
                me "Here we go, take it all!"
                "Your cock pulses out your load one spurt at a time. Stephanie doesn't move and waits until you're finished, then pulls off carefully from your tip."
                show steph blow8 at right
                "She tilts her head up and opens her mouth, then blows bubbles through your cum. After a few seconds she closes her mouth again and swallows."
                $ stephO.inc_cum_swallow()
                show steph work at right
                steph "Ah, that was a good one. Do you trust me to keep this from Nora now?"
                me "Completely. Now lets get cleaned up before she walks in the door."
                "You and Stephanie get cleaned up and slip out of the lab before Nora comes in for the day. As she's heading away you feel confident you've made a [stephO.effect_string] impact on her and secured yourself a lab assistant."
                $stephO.change_slut_rebalanced(action_difficulty)
            else:
                steph "A blowjob? If Nora caught us we'd both be fired"
                me "We better be quick then, before Nora gets into work."
                "Stephanie hesitates, but shakes her head."
                steph "No, that doesn't seem like a good idea. You're just going to have to trust me [inputName], I won't tell Nora anything."
                "Damn, she must have resisted the drug now. Maybe this last step was too far."
                me "Okay, I'll just have to take your word for it."
                "You and Stephanie make small talk, then you slip out of the lab. You're confident that you could have done more with the situation, but at least you have an assistant now."
                $stephO.change_slut_failed()
        "Have her fuck you on a chair.":
            me "If Nora finds out about this we're both in a huge amount of trouble. I want to make sure we're both invested in not getting caught."
            steph "How will you do that?"
            me "Get on the table and I'll show you."
            $ action_difficulty = 60
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            if stephO.check_willing(action_difficulty):
                steph "And then you'll trust me?"
                me "Absolutely, if I fuck you here we're both on the cameras so you won't want her checking those. Then we can work together and trust each other"
                show steph strip1 at right
                "Stephanie nods and strips off her sweater. She undoes her pants next, then sits on a table and spreads her legs."
                steph "Okay, come and take me then."
                "You slide your own pants off and throw your shirt to the floor. You step between Stephanie's legs and rub your hands along her warm thighs."
                show steph fuck10 at right
                $ stephO.inc_sex()
                "She shivers slightly under your touch, and you move your hands closer to her pussy. You rub her gently through her underwear, then pull them aside and rub her clit gently."
                steph "Oh, that feels good."
                "You grab your cock with one hand and begin running up and down the length of her slit, getting yourself wet with her juices."
                "Finally you line yourself up and thrust forward. Stephanie gasps loudly and wraps her legs around you while you begin pumping back and forth."
                show steph fuck11 at right
                "As you fuck her she brings her hands up to her tits and slides her bra up. She holds her tits and rolls her erect nipples between her fingers."
                steph "Fuck that feels good, fuck me harder!"
                me "Whatever you say!"
                "You pump harder and faster into Stephanie's pussy. She gasps and moans, her legs pulling against your back to try and get you even deeper inside."
                "After a few minutes of pumping you feel yourself building towards orgasm. Stephanie seems to be as well, and rolls her hips against yours with every thrust."
                "She begins to twitch, and her panting gets faster and louder."
                steph "I'm going to cum!"
                me "Me too!"
                menu:
                    "Cum inside her.":
                        "You pump as fast as you can, grabbing Stephanie's hips with your hands and pulling her into you. The table shakes loudly beneath her."
                        "Her pussy twitches and contracts around your cock, and she lets out a long continuous moan as she reaches her orgasm."
                        "Your cock begins to tighten and you push as deep as you can go while you unload yourself. After a few spurts you're finished, and you and Stephanie both try and regain your breath."
                        show steph fuck12 at right
                        $ stephO.inc_cum_inside()
                        "Without a word you pull your cock out, trailing cum behind it. There's a wet pop and a small trickle runs down Stephanie's leg."
                        steph "Oh god that felt good."
                        me "Ya, same. Now we should get cleaned up before Nora gets back."

                    "Cum in her mouth.":
                        me "I'm almost there. I want to finish in your mouth."
                        steph "Oh god that's so hot. Fuck me!"
                        "You pump a few more times and feel Stephanie's pussy tighten around your cock. She moans loudly as she cums."
                        show steph fuck13 at right
                        $ stephO.inc_cum_mouth()
                        "Your own orgasm approachs and you pull out with a wet plop. Stephanie drops to her knees as fast as she can and wraps her lips around your shaft."
                        "Her hand strokes you to completion, and she licks your tip while you cum into her mouth."
                        "When you're finished she slides you out gently, licking you to get every drop."
                        show steph fuck15 at right
                        $ stephO.inc_cum_swallow()
                        "She opens her mouth and shows off your load, then closes and swallows."
                        steph "Ahh, I love doing that!"
                        me "And I love doing it to you. We should get cleaned up before Nora gets back though."
                    "Cum on her tits.":
                        me "I'm almost there. I want to cum on your tits."
                        steph "Don't stop fucking me! Just pull out and cum from there!"
                        me "Okay, get ready!"
                        "Stephanie's pussy tightens around your cock as she orgasms, which pushes you over the edge."
                        show steph fuck14 at right
                        $ stephO.inc_cum_over()
                        "You pull your shaft out with a wet pop and start stroking it until you start cumming. Your first few shots arch up and land on Stephanie's tits, the rest land between her cleavage down to her pussy."
                        "You rub the last few drips off onto the lips of her pussy while you both pant heavily, trying to catch your breath."
                        steph "How was that?"
                        me "It was great. We should get cleaned up before Nora shows up though."
                show steph work at right
                "You and Stephanie get cleaned up and slip out of the lab before Nora comes in for the day. As she's heading away you feel confident you've made a [stephO.effect_string] impact on her and secured yourself a lab assistant."
                $stephO.change_slut_rebalanced(action_difficulty)
            else:
                steph "Here in the lab?"
                "She thinks about it for a long while, then shakes her head."
                me "It's so I can trust you Stephanie."
                steph "Well this would get us both fired, and Nora could come in any moment now."
                "She crosses her arms angrily."
                steph "You're just going to have to trust me, I won't tell Nora unless I have to."
                "Damn, she must have resisted the drug now. Maybe this last step was too far."
                me "Okay, I'll just have to take your word for it."
                "You and Stephanie make small talk, then you slip out of the lab. You're confident that you could have done more with the situation, but at least you have an assistant now."
                $stephO.change_slut_failed()
    $ has_lab_assistant = True
    jump campusJumpTimeSkip

label maj_steph_beach:
    $ steph_beach_event_object.happened = True
    $temp_slut_score = 0
    call serum_give(stephO) from _call_serum_give_25
    $ temp_slut_score = _return
    "You empty a small vial of serum into Stephanie's drink, then balance everything on your tray and head up the slope leading away from the beach. You find her sitting at a picnic table under an umbrella."
    me "I'm back. Glad you were able to find us some shade."
    steph "Thank you [inputName], the food looks great!"
    "You sit down next to Stephanie and start in on your lunch. You pay special attention to her as she finishes off her drink, waiting for the serum to take affect. After a few minutes you speak up."
    me "Hey Stephanie, I think I forgot something up by the change rooms earlier today. Would you mind comming with me while I check?"
    "Stephanie looks at you, eyes slightly unfocused."
    steph "Sure. What did you lose?"
    me "Nothing important, I just want to take a quick look."
    "You lead Stephanie up to the change rooms. Most of them are empty this time of day, and you pick a stall that's as far away from anyone else as possible."
    "You pull open the curtain leading to the stall and take a quick glance around, confirming there's nothing in it."
    me "Hmm, I guess I was rong, it's not here. But, if we're up here already, I wanted to ask you something."
    steph "Yeah? What's up?"
    menu:
        "Have her flash you her tits.":
            $ action_difficulty = 0
            $stephO.set_action_exhib()
            $stephO.check_willing(action_difficulty)
            me "I've been sneaking glances at you in your cute swimsuit all day, and I just can't stand it any more. I was hoping you would sneak in here with me and give me a quick peak of your tits."
            if stephO.exhib:
                steph "Oh, you should have just asked!"
                #Note that being public always means she's wearing her slut outfit.
                show steph strip41 at right
                "Stephanie grabs her bikini top and pulls it up, letting her breasts fall free. She shakes her shoulders, making them jiggle around. She seems completely unfazed having her tits out in public."
                me "Damn, those look great Stephanie."
                "She cups one of her boobs and hefts it a few times, then pinches the nipple and moans softly."
                steph "Thank you, I think they're pretty good too."
                if slut_outfit:
                    show steph swim2 at right
                else:
                    show steph swim1 at right
                "She gives you one last look, then pulls her top back down into position."
            else:
                steph "Oh, I didn't even realize."
                "She glances up and down the line of change rooms, then steps inside the one you opened and motions for you to follow. Once you're inside she closes the curtain behind you."
                steph "Okay, ready?"
                me "Ready when you are."
                if slut_outfit:
                    show steph strip41 at right
                    "She grabs her bikini top and pulls it up, letting her breasts fall free. She shakes her shoulders, making them jiggle around."
                else:
                    show steph strip40 at right
                    "She slides the straps of her swimsuit over her shoulders, then pulls it down around her waist. She shakes her shoulders, jiggling her breasts for you."
                me "Damn, those look really good Stephanie."
                steph "Thank you, I think so too."
                "She gives you one last look, then pulls her swimsuit back into position."
            if slut_outfit:
                show steph swim2 at right
            else:
                show steph swim1 at right
            $ stephO.inc_naked()
            steph "I hope that scratched your itch [inputName]."
            me "Yeah, I think that will do. Lets head back to the table and chill for a little bit."
            "She nods, and you return to the picnic table. You chat with each other for half an hour, waiting for the serum to wear off completely. You feel like you had a major effect on her today."
            $ stephO.change_slut_rebalanced(action_difficulty)
            $ stephO.change_resist(steph_beach_event_object.get_resist_change(1))
            $ steph_beach_event_object.inc_level(1)

        "Have her get naked for you.":
            me "You've been hanging around in your cute swimsuit, and I just haven't been able to take my eyes off of you. It would really help me if you would take it all off for me and let me have a good look."
            $ action_difficulty = 15
            $stephO.set_action_exhib()
            if stephO.check_willing(action_difficulty):
                steph "Oh, I didn't realize I had gotten you quite that worked up."
                "She glances down at the bulge in your swim trunks."
                steph "Come in here and I'll see how I can help."
                "You follow her into the change room, closing the curtain behind the two of you."
                steph "Ready?"
                me "Ready when you are."
                show steph strip43 at right
                $ stephO.inc_naked()
                if slut_outfit:
                    "She reaches behind her neck and undoes her bikini top, then pulls it up and off completely. She grabs the bottoms next, pulling them down past her thighs and letting gravity take over from there."
                else:
                    "She takes her swimsuit's straps and pulls them over her shoulders. Then she slides the whole outfit down, stepping out of it and kicking it to the side."
                steph "There, how's this?"
                "She poses in front of you, completely naked."
                me "You look amazing Stephanie. Wow."
                steph "What about from behind?"
                show steph strip44 at right
                "She spins around and places her hands on the far wall, sticking her ass out towards you."
                me "Yeah, that looks pretty great too."
                steph "Give it a squeeze."
                "She wiggles her butt, and you reach out with both hands to grab her cheeks. You press them together, then let them go and watch them bounce around."
                steph "Ah, that feels weird!"
                "You give her ass one last smack before she turns around."
                steph "There, I hope that helped you out [inputName]."
                me "It did. Thank you Stephanie."
                if slut_outfit:
                    show steph swim2 at right
                else:
                    show steph swim1 at right
                "She grabs her swimsuit and puts it back on before opening up the curtain again."
                steph "If we're all done here, should we head back to the table?"
                me "Sounds like a good iea, I feel like just chilling out for a few minutes."
                "You return to the picnic table and chat with each other for a half hour, waiting for the serum to wear off completely. You feel like you had a major effect on her today."
                $ stephO.change_slut_rebalanced(action_difficulty)
                $ stephO.change_resist(steph_beach_event_object.get_resist_change(2))
                $ steph_beach_event_object.inc_level(2)
            else:
                "Stephanie thinks for a long moment, looking to her side at the crowds on the beach."
                steph "I'm not so sure [inputName]..."
                me "There's nothing wrong with it, just a little fun between friends. Right?"
                steph "Maybe, but I just don't feel comfortable with it. Maybe some other time, okay?"
                "She's got a sharper look in her eye all of a sudden. She must have resisted the serum; pushing her farther is going to do more harm than good now."
                me "Alright, just forget I asked then. Lets head back to the table and chill out for a few minutes."
                "She nods, and you return to the picnic table. You chat with each other for a half hour, waiting for the serum to wear off completely."
                $ stephO.change_slut_failed()
                $ stephO.change_resist(steph_beach_event_object.get_resist_change(0))
                $ steph_beach_event_object.inc_level(0)

        "Have her give you a handjob.":
            me "You've been hanging around in that cute swimsuit, and it's gotten me all worked up. I could really use your help taking care of this, if you could lend a hand."
            "You rub the bulge in your swim trunks a little, showing off the shape of your erection."
            $ action_difficulty = 30
            $stephO.set_action_cumslut()
            if stephO.check_willing(action_difficulty):
                steph "Oh wow, all because of little old me?"
                "She reaches down and cups your bulge, rubbing it gently."
                steph "Alright, come in here and I'll see what I can do for you."
                "You follow her into the change room, and she closes the curtain behind you. She pushes you against one of the walls, then gets onto her knees in front of you."
                "Next she grabs your swim trunks and pulls them down to get your cock out."
                me "Yeah, I'm definitely going to need your help with this Stephanie."
                steph "My pleasure [inputName]. My pleasure."
                $ stephO.inc_hand()
                if slut_outfit:
                    show steph hand13 at right
                else:
                    show steph hand12 at right
                "She takes your shaft in one of her hands and starts to stroke you off slowly. Her gentle touch feels amazing, sending shivers up your spine."
                me "Fuck, that feels good."
                steph "Just relax and let me take care of this."
                "She speeds up, bringing her other hand up to massage your balls while she strokes you off. Soon you're dripping precum down onto her hand, and she spreads that around as well."
                "You enjoy Stephanie's handjob for a few minutes, but eventually you can feel your orgasm getting closer."
                me "I'm going to cum soon Steph."
                "She nods and speeds up even more, her hand gliding along your wet shaft."
                "When you tense up and start to cum she leans to the side, letting your load fire over her shoulder and into the sand."
                steph "There it is! Wow..."
                "She slows down, finally letting go of your cock when you've dribbled the last bit of semen onto her hand."
                me "Yeah, wow. Thanks Stephanie, that felt great."
                steph "I'm sure it did. Now that that's taken care of, should we head back to the table?"
                if slut_outfit:
                    show steph swim2 at right
                else:
                    show steph swim1 at right
                "She wipes her hand off on her thigh and stands up while you pull your swimsuit back up."
                me "Sounds like a good idea, I feel like just chilling out for a few minutes."
                "You return to the picnic table and chat with each other for a half hour, waiting for the serum to wear off completely. You feel like you had a major effect on her today."
                $ stephO.change_slut_rebalanced(action_difficulty)
                $ stephO.change_resist(steph_beach_event_object.get_resist_change(3))
                $ steph_beach_event_object.inc_level(3)

            else:
                "Stephanie thinks for a long moment, watching your hand slide along the outline of your shaft."
                steph "I'm not sure [inputName]. It doesn't feel like now is the right time for that."
                me "There's nothing wrong with it, you'd just be helping a friend out. Right?"
                steph "Maybe... But I don't feel comfortable with it. How about you do whatever you need to in there and meet me back at the table in a few minutes."
                "She's got a sharper look in her eye all of a sudden. She must have resisted the serum; pushing her farther is going to do more harm than good now."
                me "Alright, just forget I asked then. I'll just come back with you to the table and we can chill out for a few minutes."
                "She nods, and you return to the picnic table together. You chat with each other for a half hour, waiting for the serum to wear off ocmpletely."
                $ stephO.change_slut_failed()
                $ stephO.change_resist(steph_beach_event_object.get_resist_change(0))
                $ steph_beach_event_object.inc_level(0)

        "Have her blow you.":
            me "You've been walking around in that cute swimsuit, and it's gotten me pretty horny. I was hoping you'd come in here with me and take care of it with a quick blowjob."
            "You rub the bulge in your swim trunks, showing off the shape of your erection."
            $ action_difficulty = 45
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            if stephO.check_willing(action_difficulty):
                steph "Oh wow, all because of little old me?"
                "She reaches down and cups your bulge, rubbing it gently."
                steph "Alright, come in here and I'll see what I can do for you."
                "You follow her into the change room, and she closes the curtain behind you. She pushes you against one of the walls, then gets onto her knees in front of you."
                steph "First, lets get these out of the way."
                "She grabs your swim trunks and pulls them down. Your hard cock springs free, bouncing up and down a few times before comming to a stop."
                steph "Hmm, lets see..."
                $ stephO.inc_blow()
                if slut_outfit:
                    show steph blow42 at right
                else:
                    show steph blow41 at right
                "She leans forward and wraps her lips around the tip of your dick, swirling her tongue around it."
                me "Shit, that feels good."
                "She moves lower, using her tongue to get your shaft wet before sliding it farther into her mouth."
                "Soon she's gotten your full length dripping wet, and she starts to bob her head up and down. You lean back against the wall and close your eyes, losing yourself in the feeling."
                "Eventually Stephanie slides off with a wet pop and looks up at you, smiling broadly."
                steph "Well, having a good time?"
                me "Holy fuck, you're so good at that."
                steph "Damn right I am. Now, give me a little warning before you cum, okay?"
                me "Sure. Just keep doing what you were doing."
                steph "Gladly."
                if slut_outfit:
                    show steph blow44 at right
                else:
                    show steph blow43 at right
                "She slides you back down her throat, leaving her tongue flat against the bottom of her mouth to give you a clear path right to the back."
                "It doesn't take much longer for her to bring you to the edge of your orgasm."
                menu:
                    "Cum on her face.":
                        me "I'm going to cum, I want to finish on your face."
                        "She slides off for a brief moment."
                        steph "Oh no, I want to feel you cum in my mouth. Maybe next time though."

                    "Cum in her mouth.":
                        me "I'm going to cum, I want to finish in your mouth."
                        "She slides off for a brief moment to talk."
                        steph "Do it, fill it up with your hot cum!"
                $ stephO.inc_cum_mouth()
                $ stephO.inc_cum_swallow()
                "She goes back to blowing you as fast as she can manage, pulling back at the last moment as you start to climax. She keeps you inside of her lips as you cum, blowing your load across her tongue and filling up her mouth."
                if slut_outfit:
                    show steph blow46 at right
                else:
                    show steph blow45 at right
                "When you've let out the last drop she leans back and opens up, showing you the mess you've made."
                "After a few more seconds she closes her mouth, and you watch as she swallows down your cum. It takes two or three gulps before it's all gone."
                if stephO.cumslut:
                    steph "Ah... Thank you so much [inputName]. You tasted so good."
                    "She licks her lips, then leans forward and starts to suck on the tip of your cock again. She uses her tongue to clean up any semen still left."
                    "Eventually she's satisfied she's gotten it all and lets you slide back out of her mouth."
                else:
                    steph "Ah... That was so fucking hot. Thanks [inputName]."
                    me "No, thank you Stephanie. That was great."
                "You pull up your swimsuit while Stephanie catches her breath."
                me "When you're ready, want to head back to the table? I feel like just chilling out for a few minutes."
                steph "Yeah, lets do that."
                if slut_outfit:
                    show steph swim2 at right
                else:
                    show steph swim1 at right
                "You return to the picnic table together and chat with each other for half an hour until the serum has worn off completely. You feel like you've had a major effect on her today."
                $ stephO.change_slut_rebalanced(action_difficulty)
                $ stephO.change_resist(steph_beach_event_object.get_resist_change(4))
                $ steph_beach_event_object.inc_level(4)

            else:
                "Stephanie thinks for a long moment, watching your hand slide along the outline of your shaft and biting her lip a little."
                steph "We really shouldn't [inputName]. Not here."
                me "Come on, there's nothing wrong with it Stephanie. You'd just be helping a friend out. Right?"
                steph "Maybe, but I just don't feel comfortable with it. I'll go wait for you at the table, you go in there and do whatever you have to do to calm down a little."
                "She's got a sharper look in her eye all of a sudden. She must have resisted the serum; pushing her farther is going to do more harm than good now."
                me "Alright, just forget I asked then. I'll just come back with you to the table and we can chill out for a few minutes."
                "She nods, and you return to the picnic table together. You chat with each other for a half hour, waiting for the serum to wear off completely."
                $ stephO.change_slut_failed()
                $ stephO.change_resist(steph_beach_event_object.get_resist_change(0))
                $ steph_beach_event_object.inc_level(0)

        "Fuck her.":
            me "You've been walking around in that little swimsuit, and it's gotten me pretty horny. I was hoping you'd come in here and I could pull it off of you and take you for a ride."
            "You rub the bulge in your swim trunks, showing off the shape of your erection."
            $ action_difficulty = 60
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            if stephO.check_willing(action_difficulty):
                steph "Oh my... Come in here right now."
                "She grabs your arm and pulls you into the changing room, closing the curtain as soon as she can manage."
                "Before you can say another word she's bent forward and grabbed the rod that's holding up the privacy curtain. She wiggles her swimsuit covered ass at you."
                steph "Come on, just pull it to the side and slide in. I'm already really fucking wet."
                if slut_outfit:
                    show steph fuck54 at right
                else:
                    show steph fuck53 at right
                $ stephO.inc_sex()
                "You pull your swim trunks down and let your hard cock flop onto her ass cheek. You line yourself up with her pussy, taking a moment to pull her swimsuit to the side and drag your tip along the her wet slit."
                steph "Mmm, yeah I think I need this as badly as you do. Come on, you know you want to fuck me!"
                me "Alright, lets give you what you want then!"
                "You grab her hips and push forward, plunging your full length into her cunt. Stephanie lets out a loud moan, leaning heavily on the metal rod that's holding the curtain up for support."
                "Stephanie's pussy is tight and wet, and she rocks her hips back to meet yours with each thrust. Her moans only seem to get louder as you fuck her."
                me "Easy there Steph, half the beach is going to hear you at this rate."
                if stephO.exhib:
                    steph "Fuck it, I don't care. Just keep giving it to me like that. Fuck yes!"
                    "She moans even louder this time, her legs quivering against yours when you thrust in."
                else:
                    steph "Shit, sorry. I'll do my best, it just feels so good."
                    "She bites her lip and muffles a moan. You feel her legs quiver against yours when you thrust in."
                "It doesn't take much longer for her to push you right to the edge of your orgasm."
                menu:
                    "Cum inside of her.":
                        me "I'm going to cum Steph!"
                        "You grab her hips and pump in and out of her as fast as you can manage."
                        if stephO.cumslut:
                            steph "God yes, please! Fill me up with your hot cum, try and get me knocked up like a good slut!"
                        else:
                            steph "Do it, fill me up with your hot cum! Ah!"
                        $ stephO.inc_cum_inside()
                        "When you finally climax you pull her tight against you, emptying your balls as deep into her as possible. She takes a few shuddering gasps, and you feel her pussy twitch around your cock."
                        steph "Fuck, fuck fuck fuck..."
                        if slut_outfit:
                            show steph fuck58 at right
                        else:
                            show steph fuck57 at right
                        "When you've finished pumping out your load you take a step back. Your cock leaves her with a wet pop, and almost immediately a line of cum starts to trickle down her leg into the sand."
                        steph "Wow... That felt great [inputName]. Ah..."
                        "She takes a moment to catch her breath, then straightens up again."


                    "Cum on her ass.":
                        me "I'm going to cum Steph! Lets cover that hot ass of yours!"
                        "You grab her hips and pump in and out a few times as fast as you can manage. You pull out before you climax, leaving her pussy with a wet pop, and start to stroke yourself off."
                        if stephO.cumslut:
                            steph "Yes! give me that hot load! I want it so badly! Ah!"
                        else:
                            steph "Oh yeah, do it [inputName]!"
                        $ stephO.inc_cum_over()
                        if slut_outfit:
                            show steph fuck56 at right
                            "You pulse your load out onto Stephanie's ass, most of it landing on her bikini bottom."
                        else:
                            show steph fuck55 at right
                            "You pulse your load out onto Stephanie's ass. Most of it lands on her swimsuit bottom."
                        "She holds onto the metal bar for a few more seconds to catch her breath, then straightens up again."
                        steph "Wow... You really went to town, didn't you."
                        "She runs a finger along her ass cheek, then shrugs and starts to spread your sperm all over her butt."
                        steph "Nobody will notice if I rub it in, right?"
                        me "I'm sure it'll be fine."
                        "After a few moments she's spread your cum out into an even, shiny layer."
                if slut_outfit:
                    show steph swim2 at right
                else:
                    show steph swim1 at right
                me "Thanks for the help Stephanie. Lets head back to the table, I feel like just chilling out for a few minutes."
                steph "Sounds like a good idea."
                "You return to the picnic table together and chat for another half an hour while you wait for the serum to wear off completely. You feel like you've had a major effect on her today."
                $ stephO.change_slut_rebalanced(action_difficulty)
                $ stephO.change_resist(steph_beach_event_object.get_resist_change(5))
                $ steph_beach_event_object.inc_level(5)

            else:
                "Stephanie thinks for a long moment, watching your hand slide along the outline of your shaft."
                steph "I... I don't know [inputName]."
                me "There's nothing wrong with it, you'd just be helping a friend out. Right?"
                steph "Maybe, but I just would't feel comfortable with it here. Maybe some other time, some other place. If you need to rub one out, I can wait for you back at the table."
                "She's got a sharper look in her eye all of a sudden. She must have resisted the serum; pushing her farther is going to do more harm than good now."
                me "Alright, just forget I asked then. I'll just come back with you to the table and we can chill out for a few minutes."
                "She nods, and you return to the picnic table together. You chat with each other for a half hour, waiting for the serum to wear off ocmpletely."
                $ stephO.change_slut_failed()
                $ stephO.change_resist(steph_beach_event_object.get_resist_change(0))
                $ steph_beach_event_object.inc_level(0)


    return

#########################
##Alexia's Major Scenes##
#########################


label maj_spikeDrink:
    $ coffee_event_object.happened = True
    $temp_slut_score = 0
    call serum_give(alexO) from _call_serum_give_12
    $ temp_slut_score = _return
    "You pull out the vial of liquid and pour it into Alexia's drink. You swirl the cup to make sure it's mixed in properly."
    "A few minutes later Alexia comes back."
    show alex casual at right
    alex "Whew, some cold water definitely helped. I hope it's a more reasonable temperature now!"
    "She sits down and takes a long sip of the now cool coffee."
    me "How is it?"
    alex "The coffee? It tastes a little strange, I wonder if the milk was a little off."
    me "You should drink it all, it's good for you."
    "Alexia gives you a strange look, but the first sip must have contained a large enough dose to have an effect. She picks up the drink and begins drinking the rest without stopping."
    me "There you go, that's good."
    alex "Mmhm."
    "Her eyes are unfocused, looking into the indefinite distance. Now's the perfect time to reprogram her as much as you can."
    menu:
        "Have her make out with you.":
            $ action_difficulty = 0
            $alexO.check_willing(action_difficulty)
            me "Alexia, we've always had a lot of chemistry, right?"
            alex "I know we do, we're in the class together."
            "Even when she's completely out of it she's witty."
            me "Well, there's no use wasting time then. I want to make out with you right now."
            alex "I've always thought you were pretty hot."
            "Alexia leans forward over the table, and you lean towards her."
            "You meet in the middle, lips pressing against each other. You feel her tongue slip out from her mouth, and lick at your lips. You open your mouth to let your own tongue meet hers."
            "She moans softly as you bring up a hand to hold the back of her head, and press yourself against her with renewed vigor."
            "You can hear someone else on the patio comment, but neither you nor Alexia pay attention to them."
            show alex kiss1 at right
            "Alexia hops up and sits on the table, scooting towards you to reach you more easily. Her hands reach around you and hold you in a hug."
            "Your other hand drifts down her back, and ends up resting on the top of her ass."
            "You savour the moment, but the crowd around you starts making more noise, and you break the kiss."
            alex "That was nice."
            "She smiles, seemingly unbothered by the other people staring at you."
            me "It was, you're beautiful and I hope we can do it again some time."
            alex "I'm sure we will."
            show alex casual at right
            "Her eyes are focusing a little better, it looks like the drug is wearing off. You should head out before she starts asking questions."
            me "It's getting a little late, I should head out."
            alex "Oh, sure. Have a great day [inputName]."
            me "You too."
            "You're pretty sure you had a major effect on Alexia with that show."
            $ alexO.change_slut_rebalanced(action_difficulty)
            $alexO.change_resist(coffee_event_object.get_resist_change(1))
            $coffee_event_object.inc_level(1)

        "Have her flash her tits for you.":
            me "Alexia, I've always had a hard time bringing myself to talk to you because you're just so attractive."
            "Alexia blushes and looks at you."
            me "One thing I've always noticed is how great you manage to make your tits look in every outfit. I always wonder if it's a trick, or if they're just that amazing."
            me "Could you show them to me, just so I know it's not an illusion?"
            $ action_difficulty = 15
            $alexO.set_action_exhib()
            if alexO.check_willing(action_difficulty):
                #She does it
                "Alexia pauses to consider."
                alex "Sure, I guess. I don't know why you'd think I fake these girls though."
                show alex strip7 at right
                "Without checking the rest of the patio she reaches down to the bottom of her shirt, grabs it and pulls up. She catches her bra on the way up, and pulls that out of the way too."
                "Her tits bounce down from underneath her shirt, looking amazing in the sunlight."
                "Nobody else seems to have noticed yet."
                me "Wow, those do look amazing. Squeeze them together for me."
                show alex strip8 at right
                $ alexO.inc_naked()
                "Alexia nods, and takes both hands and squeezes her tits between them. They bulge slightly, and she smiles as she looks down at her own cleavage."
                "Someone nearby says something, and the patio starts going quiet."
                alex "Is this good?"
                me "Oh ya. That's perfect."
                me "Just lean forward a little bit and let them hang."
                show alex strip9 at right
                "She does so, and her tits dangle from her chest, nipples hardening in the air."
                "The patio is almost completely silent now. You better get out of here before anyone says anything."
                me "That was amazing Alexia. You should put them away for now, but I'd love to see them again later."
                show alex casual at right
                "Alexia smiles and pulls her shirt and bra back down, shuffling her tits back into place."
                alex "Sure, that sounds fun."
                me "But now we should be heading out, it's getting a little late."
                "You stand up and Alexia follows you. You say goodbye to her shortly after and head your separate ways."
                "You're certain you had a major effect on Alexia with that show."
                $ alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(coffee_event_object.get_resist_change(2))
                $coffee_event_object.inc_level(2)
            else:
                #She resists
                "Alexia pauses to consider."
                alex "Alright, but I don't think I can show you everything here. There are other people around."
                me "I'm sure they wouldn't mind, your tits must look great."
                alex "Well, I mind. And their my tits, so I decide who gets to see them."
                show alex strip10 at right
                "Alexia grabs the front of her shirt with one hand and lifts it up until her bra covered boobs slip out from underneath it. The bra is tight fitting, perhaps a size too small, and lacy around the edges."
                alex "Is that good?"
                me "Just a little bit longer. How about you pop them out of the cups."
                alex "Not here, there are other people."
                show alex casual at right
                "She leans over slightly to obsure her breasts from the other people on the patio. A few seconds later she glances around, then pulls her shirt back into place."
                alex "That was really risky, I hope nobody else noticed."
                me "I'm sure it's fine."
                alex "Ya, probably. I'm going to head out though, just in case. It was nice hanging out with you."
                "Alexia stands up and heads off, leaving you sitting by yourself. Eventually you head out too."
                "You probably had some effect, but maybe you pushed her too far with this."
                $ alexO.change_slut_failed()
                $alexO.change_resist(coffee_event_object.get_resist_change(0))
                $coffee_event_object.inc_level(0)

        "Have her masturbate right here.":
            me "Hey Alexia. There are so many people in this store who would die to have five minutes alone with you, and do really dirty things to you. Does thinking about that ever get you horny?"
            $ action_difficulty = 30
            $alexO.set_action_exhib()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                #She does it
                alex "It does a little bit. I wonder how many of them are turned on by me right now."
                me "I'm sure more than a few. I know I'm rock hard thinking about you, and a pair of guys behind you have been trying to get glances at your tits every time they walk past."
                alex "Really? Damn."
                me "Ya, really. Just thinking about what they'd do to you must get you horny enough to want to rub one out, right?"
                show alex mast1 at right
                "You see Alexia's hand drift below the table to her lap."
                alex "It kind of does. I wonder if they would take me one at a time, or all at once."
                "Her hand is rubbing against her crotch through her skirt."
                me "Which way would you like it?"
                alex "Both at once, definitely. One in my mouth and one in my pussy."
                "She sighs as she rubs herself through two layers of fabric."
                me "You should slip your hand under your skirt, to make things easier for you."
                show alex mast2 at right
                "Alexia doesn't say anything, but pulls her skirt up higher and sighs as she touches herself."
                me "So you like having two guys at the same time?"
                alex "More than two if I could. Imagine if I could seduce all the guys here. That would be hot."
                me "Thats a lot of guys, how would you take care of them all?"
                alex "They'd have to take turns, obviously. We could probably..."
                "She shudders and takes a moment to catch her breath."
                alex "We could fit four people around the table, and me on my back on top. One guy in my pussy, one in my mouth, one in each hand."
                me "And the rest would tag in?"
                alex "Exactly. When he cums down my throat..."
                "Another shudder interrupts her story."
                alex "...down my throat his friend would step up and slide right in. I'd barely have time to breath."
                me "What about the other three?"
                alex "Them? I'm pretty good with my hands, I'm sure I could get a guy off with each hand while I'm lying down."
                alex "And when they finish, they could..."
                show alex mast3 at right
                "shuddering again, this time coiling up slightly."
                alex "They could finish on my tits and my stomach and my face. By the end of the night I'd be plastered head to toe."
                me "All night? You think you could keep that up?"
                alex "It wouldn't matter, it would be out of my hands. They would just keep fucking my throat and cumming in my pussy. Some might even anal me and have me screaming."
                "Alexia leans one hand against the table and shivers, her core muscles twitching."
                me "And by the end of the night you'd be a mess. Covered in cum, pussy and ass stretched out, mouth completely filled with spunk."
                alex "Oh god yes."
                "She doubles over, knocking your coffee aside, and shudders violently. You can see her hand working as fast as possible underneath the table."
                "A few other patrons glance over, but discreetly look away."
                show alex mast1 at right
                "Alexia relaxes, and pulls her hand out slowly."
                alex "There it was, oh fuck."
                me "On a coffee shop patio, cumming near so many people. You dirty girl."
                "You wink at Alexia, who smiles back weakly."
                me "You should tell me more of your fantasies, they're interesting."
                alex "Sure, one day."
                me "It's getting late now though, lets head out."
                "You and Alexia head out of the shop, say goodbye, and head your own separate ways."
                $ alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(coffee_event_object.get_resist_change(3))
                $coffee_event_object.inc_level(3)
            else:
                #She resists
                alex "A little bit I guess. I don't even know these people though."
                me "The thought of all of them wanting you doesn't turn you on? You can tell me."
                alex "Well... Sometimes I have fantasies about a bunch of dudes taking me all at once. But being out here it just doesn't feel right."
                me "you should try getting off while thinking about that, right here."
                alex "Here? No way, I don't think I could do it."
                me "Give it a try, I think you'll surprise yourself."
                show alex mast1 at right
                "Alexia slips her hand between her legs and starts rubbing."
                me "That's right. Riding all the guys as they wait for their turns."
                alex "No, I'd want them taking me all at once."
                me "Sexy. You're a dirty girl."
                alex "Maybe just a little."
                "She brings her hand back up to the table."
                alex "But I'm not feeling it today. Maybe it's just not the right crowd."
                me "Well, it was still hot to watch you try."
                "Damn, you must have pushed her too far all at once. You got her to talk about her fantasies though, so that's something."
                me "We should head on out, it's getting late."
                "Alexia nods. The two of you leave together, then head your separate ways."
                $ alexO.change_slut_failed()
                $alexO.change_resist(coffee_event_object.get_resist_change(0))
                $coffee_event_object.inc_level(0)

        "Have her get under the table and give you a blowjob.":
            me "You know, I've always thought you looked like you gave pretty amazing head."
            alex "Oh ya?"
            me "Ya, you look like you'd know what to do, and not be afraid to do it anywhere. I bet you'd even blow me right here if I asked."
            $ action_difficulty = 45
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                #she does it
                alex "No maybes about that. I bet I could finish you off before anyone gets the staff."
                me "Think you could? I doubt it. You'd probably just get me hard then we'd have to run."
                alex "Is that a challenge? If so, challenge accepted."
                "Alexia slides underneath the metal table and quickly scoots up to you. You stretch one leg out to try and cover her from the rest of the patio."
                "With quick hands she slips your pants down, and frees your cock from your underwear."
                alex "Start the timer now."
                show alex blow3 at right
                $ alexO.inc_blow()
                "She doesn't waste any time, and immediately slips the tip into her mouth. Her tongue licks back and forth as she slides it in, getting your shaft wet for her throat."
                me "Damn, that feels good."
                "She nods, then begins bobbing her head up and down underneath the table. Her tongue flicks across your tip every time she's at the top."
                "Someone on the patio says something, but you can't pay attention to anything other than the hot chick devouring your cock under the table."
                "Her hands come up, one working the shaft as her mouth slips past and the other playing gently with your balls."
                "Alexia's mouth is warm and soft, her technique is perfect as she throats you quickly and deeply."
                "Another person has noticed, and they get up and start heading to the store."
                me "They noticed, we better get out of here!"
                "Alexia doesn't get up though. Instead, she begins furiously bobbing her head up and down your cock, gagging on you with each stroke."
                "The sudden change of pace, and the feeling of hitting the back of her throat, brings you right to the edge."
                me "Oh shit, I'm cumming!"
                "Alexia doesn't stop sliding down the full length until the first blast of cum hits her throat. Then she pulls back, opens her mouth, and places the tip firmly on her tongue as you pulse out your load."
                "A waitress is coming out of the building, heading towards you two."
                me "Come on, we've got to go!"
                "You grab Alexia's arm and pull her out from underneath the table. She mumbles something but you can't make it out past the cum."
                "You try to stuff your package back in your pants as you run onto the grass field. The waitress chases you to the edge of the patio and shouts after you, but doesn't go any farther."
                "Eventually you lose sight of the coffee shop and stop to catch your breath."
                me "Holy crap that was great."
                show alex blow4 at right
                $ alexO.inc_cum_mouth()
                $ alexO.inc_cum_swallow()
                "Alexia doesn't say anything, but looks at you, opens her mouth, and reveals a mouthful of cum."
                "She then closes her mouth, swallows loudly, and opens again."
                show alex casual at right
                if alexO.cumslut:
                    alex "All gone. You tasted delicious [inputName]."
                    me "Good to know, glad you liked it."
                    "You glance around, making sure nobody has followed you."
                else:
                    alex "Tada. And its gone."
                    me "That might be the hottest thing I've ever seen."
                    "Alexia bows."
                    alex "I aim to please. I believe that load also proved me right, I can make you cum before anyone could stop me."
                    me "You've got me, imagine my embarassment."
                me "They might come looking for us, we should probably split up just in case."
                alex "Right, sounds like a good idea. Stay in touch, and let me know if you have any other things you don't think I can do."
                "She winks, and the two of you head in opposite directions."
                "You definitely make a large impression on her, her behaviour will probably be different from now on."
                $ alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(coffee_event_object.get_resist_change(4))
                $coffee_event_object.inc_level(4)
            else:
                #She resists
                alex "Here? I don't think so."
                me "Why not, nothing wrong with it."
                alex "If anyone caught us they'd kick us out of class. You'd lose your research job. Not worth the risk."
                me "Not even for a mouthful of cum?"
                alex "Ooh, you make a good point."
                "Her hand reaches over and grabs you by the cock through your pants."
                alex "But I think we should take a rain check on this one. I'll find some other time to make it up to you, I promise."
                me "Alright, but I'm holding you to that."
                "Alexia lets go, and eats the last bit of her sandwich."
                alex "It's getting late, we probably should head out soon."
                "It looks like you rushed things too quickly and she resisted the drug. Maybe next time you'll have better luck."
                me "Right, ya."
                "The two of you leave the coffee shop together, then head your separate ways."
                $ alexO.change_slut_failed()
                $alexO.change_resist(coffee_event_object.get_resist_change(0))
                $coffee_event_object.inc_level(0)

        "Have her lie on the table and fuck her.":
            me "After everything we've done together, there's still one thing I want to do."
            alex "Oh ya, what's that."
            me "Well, I've never gotten the chance to fuck you on this table."
            $ action_difficulty = 75
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                #she does it
                alex "This table right here? That's strangely specific."
                "Alexia scoots her chair closer, and smiles mischieviously."
                me "What can I say, I'm a strange man. What do you say?"
                alex "If it's really something you can't live without we could give it a try. We'll need to finish before security gets here."
                me "Of course, I'll finish as quickly as I can."
                alex "Wait."
                "Alexia repositions her chair so it's looking towards the grass field, away from the rest of the patio. Then she slips one hand under her skirt and one down your pants."
                alex "Lets get us both nice and ready."
                show alex fuck6 at right
                "Alexia grabs you by the cock and strokes you slowly up and down. At the same time her own hand squirms around inside her panties."
                "After a few minutes you're rock hard and excited about what you're going to do."
                alex "I'm nice and wet, how do you want to take me?"
                me "I want to put you on your back and throat fuck you quick, then spin you around and fuck you till I cum in you."
                "Alexia nods."
                alex "I'll take off my skirt while you use my throat."
                me "Ready? 3. 2. 1. Go."
                "Alexia jumps up on the table, leans her head over the edge, and opens her mouth for you."
                show alex fuck7 at right
                $ alexO.inc_sex()
                "You pull your pants down past your cock and flop it out onto her face. A quick reposition gets you lined up with her mouth and you plunge in deep and fast."
                "A few people nearby are startled, but nobody moves to stop you."
                "Alexia's mouth is soft and wet, and she makes soft gagging noises every time you hit the back of her throat. Her hands and feet thrash as they push her skirt off and leave it crumpled on the ground."
                "She reaches up and tags you on the arm. You pull out and push on her shoulder, pivoting her around her ass. As she swings around you catch her legs, place them on either side of your hips, and line up to enter her."
                "Someone inside the shop is yelling, and a few people have pulled out phones to take pictures or video."
                show alex fuck8 at right
                alex "Fuck me!"
                "You line the tip up and thrust your wet cock inside Alexia. Her legs wrap around behind you, and she pulls you in with every thrust. Between her handjob and throat fuck, you're already right on the edge."
                "No more than a dozen thrusts in and you're right at the edge."
                me "I'm cumming!"
                if alexO.cumslut:
                    alex "Please! I want to feel you pump me full of cum!"
                else:
                    alex "Do it! Cum inside!"
                "You grab her by the hips and pull her into you, forcing yourself as deep as you can go while you release. Her hips rock against yours as you empty yourself, and you can feel her shudder with a mutual orgasm."
                show alex fuck9 at right
                $ alexO.inc_cum_inside()
                "Barely finished, you pull your dripping cock out of Alexia. She hops down from the table and the two of you begin running as fast as you can away from the coffee shop."
                "Alexia kicks off her skirt and picks it up as she runs, and you can see your cum dripping down the side of her leg as she speeds in front of you."
                "Somewhere behind you can hear a security cart, but a few quick turns past some buildings and you've lost them."
                "Alexia puts her skirt back on quickly and gives you a kiss."
                alex "That was amazing."
                me "It was, you felt so good."
                alex "So did you. Now we should split up so they can't catch us both."
                me "Right. Talk to you later coffee slut."
                "Alexia winks at you, then takes off between some buildings. Eventually you circle around back to campus and act like nothing happened."
                "You definitely had a [alexO.effect_string] impact, Alexia will probably be acting different now."
                $ alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(coffee_event_object.get_resist_change(5))
                $coffee_event_object.inc_level(5)
            else:
                #she resists
                "Alexia stands up, sits on the table in front of you, and wraps her legs around you."
                alex "Oh ya, you want to take me right here, right now?"
                me "Definitely. You should lean back and let me get started."
                "She seems to think about it for a moment, and one of her hands reaches under her skirt as she does."
                alex "That would be pretty hot. I bet you'd fuck me hard enough that I couldn't run when security got here."
                "She looks into the air and sighs."
                alex "I wonder what they'd do with me then, if I asked them to finish what you started."
                me "How about we find out. Warm me up with a blowjob and then I'll fuck you as hard as I can."
                "Some people near by must have overheard you, and are staring at you and Alexia."
                "Alexia looks around and seems to realize how many people there are."
                alex "It would be hot, but I don't think it's a good idea."
                "She pulls her hand out of her skirt, and goes back to her chair."
                me "No? I think we could pull it off."
                alex "But if we got caught, we'd both be kicked out of school for sure. No way I'm risking that."
                me "Nothing I could do?"
                "Alexia seems to be coming around, she must have resisted the drug. Maybe you pushed her too far at once."
                alex "Nothing, no chance. Thanks for the coffee, but I should probably be going."
                me "Sure, no problem. We should do this again."
                "You might have gotten her all warmed up, but you doubt you had much of an effect on her."
                alex "Ya, that would be fun."
                "You and Alexia both leave the coffee shop together, then head your own separate ways."
                $ alexO.change_slut_failed()
                $alexO.change_resist(coffee_event_object.get_resist_change(0))
                $coffee_event_object.inc_level(0)
    jump campusJumpTimeSkip

label maj_alexStudy:
    $ test_studying_object.happened = True
    $ temp_slut_score = alexO.slut_score
    "You grab separate bowls and divide the popcorn evenly between them."
    call serum_give(alexO) from _call_serum_give_10
    $ temp_slut_score = _return
    "You mix in the serum as well as you can, shaking the bowl back and forth to spread it around while you pour it over the popcorn. When you're done you head back up to your room, bowls in hand."
    show alex casual at right
    alex "Ah, great! Thanks!"
    me "No problem, my pleasure."
    "You hand Alexia her bowl, and sit back on your seat. You chat about your last school year while you both eat popcorn."
    me "Enjoying the snack?"
    alex "Ya, it's really good. Just what I needed to keep my energy up."
    me "Great. Make sure to eat it all."
    "She nods and keeps eating it by the handful."
    alex "I must have really needed this, I'm starting to feel a little tired."
    me "Maybe you're just getting relaxed. There's nothing left to worry about for this test, we can just hang out for a while."
    "The last few bites of popcorn disapear into her mouth while her eyes stare at the wall unfocused."
    menu:
        "Have her flash her tits for you.":
            $ action_difficulty = 0
            $alexO.set_action_exhib()
            $alexO.check_willing(action_difficulty)
            me "You've probably been stuck on this for a while now, right?"
            alex "Ya, this section of the course is killing me."
            me "It's a good thing I was here to help. I feel like I deserve some sort of reward."
            alex "I guess so, you really helped me out."
            me "Okay then, for a reward I want you to flash me your breasts. I've always wanted to get a good look at them."
            "Alexia considers it for a moment then nods."
            alex "Okay, I can do that. Thanks for all your help."
            show alex strip11 at right
            "She pulls her sweater up past her tits, then grabs her bright red bra and pulls it up too."
            "Her tits fall out the bottom and bounce to a stop. She puffs her chest out at you so they spring out as much as possible."
            me "That's perfect. Shake them around for me."
            "Alexia complies, shaking her tits so they jiggle back and forth."
            "While you watch her nipples harden and stand on end."
            alex "All done?"
            me "I suppose. I wish I could get a look at those more often."
            show alex casual at right
            "Alex pulls her bra down and gets her breasts back in the cups, then slides her sweater over them."
            alex "Play your cards right and maybe you will."
            "She winks and laughs."
            alex "Now there's another section we have to cover. We should get that done."
            me "Right, of course."
            "You and Alex spend some more time going over the other section. When you're done, you walk her to the door and watch as she drives away. You're certain you made a [alexO.effect_string] impact on her with your actions."
            $ alexO.change_slut_rebalanced(action_difficulty)
            $alexO.change_resist(test_studying_object.get_resist_change(1))
            $test_studying_object.inc_level(1)
        "Have her get naked and show off by your window.":
            me "You've been studying really hard for this test, haven't you?"
            "She nods slowly."
            alex "Ya, I haven't had time for anything else lately."
            me "Then you deserve to really cut loose and relax. How about you take your clothes off so they aren't getting in the way?"
            $ action_difficulty = 15
            $alexO.set_action_exhib()
            if alexO.check_willing(action_difficulty):
                alex "Huh, I guess that does sound nice."
                "Alexia stands up and reaches for her sweater."
                alex "When I'm at home I like to spend some of my time naked anyway."
                "She pulls the sweater up, her tits contained in a bright red bra."
                if alexO.exhib:
                    alex "I leave the window open too. I've got a neighbour who loves to peek in on me and see what I'm doing. I give him a little show whenever I can."
                    show alex strip3 at right
                    "She giggles and reaches for her skirt waist. She slides a zipper down and lets it fall to the floor, revealing a matching set of panties underneath."
                    me "I bet you love doing that, right? Showing off for him."
                    show alex strip12 at right
                    $ alexO.inc_naked()
                    "Alexia reaches behind her back and undoes the clasp of her bra. She pulls it forward nd drops it to the floor."
                    alex "God, I do. I can feel how badly he wants me. It's so damn hot."
                    show alex strip4 at right
                    "She slides her panties down to her knees and lets gravity carry them down from there. She stands in the middle of your room completely naked."
                    me "There are some people outside right now. Why don't you lean on the window and give them a show too."
                else:
                    alex "It just feels so naughty, but if I'm in private there's nothing wrong with it."
                    show alex strip3 at right
                    "She giggles and reaches for her skirt waist. She slides a zipper down and lets it fall to the floor, revealing a matching set of panties underneath."
                    me "Nothing wrong with that at all. Do you ever leave your windows open?"
                    show alex strip12 at right
                    $ alexO.inc_naked()
                    "Alexia reaches behind her back and undoes the clasp of her bra. She pulls it off forward and drops it to the floor."
                    alex "Well... Sometimes. I doubt anyone's noticed though."
                    show alex strip4 at right
                    "She slides her panties down to her knees and lets gravity carry them down from there. She stands in the middle of your room completely naked."
                    me "I'm sure some people have noticed you walking around naked, and I'm certain they liked what they saw."
                    "Alexia smiles and blushes, and you can see her nipples getting hard."
                    me "This is a completely different neighbourhood from yours you know, if someone saw you through my window it wouldn't even matter."
                    "Alexia bits her lower lip and cradles a breast in one hand."
                    alex "What are you suggesting?"
                    me "Just lean over and press your tits against the window and see if anyone notices."
                show alex strip13 at right
                "She hesitates, kneading a breast in her hand. Finally she nods and leans over the desk. You get a great look at her ass while she plants her tits on the glass and stares out."
                me "See anyone out there?"
                alex "There's a person walking their dog. A few cars. There's a person cutting the grass across the street."
                "Alexia slides her tits up and down on the glass. From your vantage point you can see that her pussy is getting wet."
                me "Try and get the grass guy's attention. I'm sure he'd appreciate the break too."
                "She waves with one hand while rubbing a tit up and down on the glass. It takes nearly a minute, but finally she yells in surprise."
                alex "He's looking up here!"
                "She places both hands on the top of the window and leans against the glass as hard as she can. She shakes them up and down, left and right."
                me "Alright, I think he's seen enough. You don't want to give him the wrong idea about you."
                "Alexia sighs and leans back from the glass."
                alex "Ya, you're right. We have studying to do anyway."
                me "Right. Maybe you should get dressed in case my mom or sister comes in while we're studying."
                show alex casual at right
                "Alexia nods and puts her clothes back on. You spend some time going over the next section of the textbook, and when you're done you walk her to the door. As she drives away you feel confident you had a [alexO.effect_string] impact on her."
                $ alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(test_studying_object.get_resist_change(2))
                $test_studying_object.inc_level(2)
            else:
                alex "You want me to get naked, in your room?"
                me "Sure, why not? It'll be freeing, I promise."
                "Alexia hesitates, and one hand rubs the inside of her thigh lightly. Finally she shakes her head."
                alex "No, that would feel too weird. If I was at home that would be different."
                "She must have resisted the drug. Better back off and hope she doesn't get suspicious."
                me "Okay, if you don't want to no problem. How about we finish that next section then."
                alex "Right, sure. I think I need some more water."
                "You and Alex go over the next section quickly. Afterwards she thanks you for all your help and drives home. While you watch her leave you're certain you could have made better use of the situation."
                $ alexO.change_slut_failed()
                $alexO.change_resist(test_studying_object.get_resist_change(0))
                $test_studying_object.inc_level(0)
        "Have her give you a handjob.":
            me "That was some serious studying, it's good to be done with it. I've been hard ever since you got here too, which has made things even more difficult."
            alex "You're hard?"
            me "Oh ya, the moment I saw you at the door. Since I helped you study for your test, it only seems fair you help me jerk off now too."
            $ action_difficulty = 30
            $alexO.set_action_cumslut()
            if alexO.check_willing(action_difficulty):
                alex "You did help me out, and I wouldn't want you dealing with that all day."
                "She places a hand on your crotch and rubs your bulge."
                me "Right. We'll take a few minutes to take care of this, then get back to the studying."
                show alex hand1 at right
                $ alexO.inc_hand()
                "You pull your pants down to your knees and free your cock from your underwear. Alexia takes it gently in her hand and rubs it slowly."
                alex "How's that?"
                me "Perfect. Just like that."
                "Her soft hand slides up and down your shaft, slowly picking up speed."
                "For a few minutes you don't say anything, you just sit back and enjoy feeling her jerk you off."
                "Your precum drips down your cock and gets her palm wet. She strokes you faster with her wet hand."
                me "Damn that feels good. I'm getting close."
                alex "Okay, just let it out."
                "Alexia strokes you as fast as she can, and you feel your orgasm building."
                me "Don't stop, keep going until I'm done!"
                "Your cock tenses and begins spasming. You shoot several spurts onto your desk, then dribble the rest down your shaft onto Alexia's hand."
                alex "There it is!"
                show alex casual at right
                "Alexia slows her stroking down, then removes her hand and wipes it off on the inside of her skirt. She uses a sleeve to wipe a blob of cum off her textbook."
                me "Sorry about that."
                alex "No, don't be sorry. That was kind of the point, wasn't it?"
                me "Right. I guess we should get back to studying now then."
                "You spend some time going over the next section of the textbook, and when you're done you walk her to the door. As she drives away you feel confident you had a [alexO.effect_string] impact on her."
                $ alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(test_studying_object.get_resist_change(3))
                $test_studying_object.inc_level(3)
            else:
                alex "So... a handjob?"
                me "Right."
                "You pull down your pants, letting your hard cock swing free."
                alex "In your room though? I was really just here to study..."
                me "It's fine. It's a way of thanking me for helping."
                "Alexia reaches forward and runs a finger along your shaft. You flex it and bump the tip into her palm."
                alex "Ah! Um, no. This doesn't feel right. Maybe later [inputName]. I'm really thankful for your help, but I'm not feeling great."
                "She must have resisted the drug. Better back off and hope she doesn't get suspicious."
                me "Okay, of course you don't have to. It was just a suggestion."
                "You stuff your cock back in your pants."
                me "How about we finish the next section then."
                "You and Alex go over the next section quickly. Afterwards she thanks you for all your help and drives home. While you watch her leave you're certain you could have made better use of the situation."
                $ alexO.change_slut_failed()
                $alexO.change_resist(test_studying_object.get_resist_change(0))
                $test_studying_object.inc_level(0)
        "Have her blow you.":
            me "That was some serious studying. Glad we're done with it. How about you give me a little reward and suck me off?"
            $ action_difficulty = 45
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                #TODO add extra sister/Alexia scene where you show off Alexia under the desk.
                alex "You have done a lot to help me. It's the least I could do."
                "Without a second thought she drops to her knees. You swivel your chair to face her and struggle to get your pants down past your cock quickly."
                me "Sounds great. We can get back to studying once we're done."
                show alex blow1 at right
                $ alexO.inc_blow()
                "Alexia takes your cock in her hand and rubs it gently for a few seconds. Then she licks it from base to tip, and gives the tip a little kiss."
                "Finally she spreads her lips around the top and slides it into her mouth. She takes the first few strokes slowly to get your shaft wet, then speeds up and sucks you off at a good pace."
                "For a few minutes you enjoy the feeling of Alexia's warm mouth wrapped around your cock. You watch as her head moves up and down rhythmically, and you can hear quiet wet noises coming from her mouth."
                "Alexia slides off the tip and licks up some extra spit. She takes you in her hand and strokes your wet cock while she talks to you."
                alex "How's that?"
                me "Fucking amazing. You're doing great."
                alex "Good, I'm glad you like it."
                "She puts you back in her mouth, and returns to sucking at a faster speed."
                "You're getting close to orgasming when there's a single knock at the door."
                sis "Hey [inputName], did you borrow my phone charger?"
                show alex blow5 at right
                "The doorknob begins to turn. Alexia puts her hands on your thighs and shuffles under the desk with her mouth still around your cock."
                show sis casual1 at left
                "Your chair swivels around, and by the time the door is opened fully you're pressing your waist against the edge of the desk with your back to the door."
                sis "Hey, did you hear me?"
                if alexO.exhib:
                    "Alexia keeps blowing you quickly, pushing herself down as deep as she can manage on your cock. You do your best to block her from sight, but there's nothing you can do about the wet sucking noises."
                    me "Uh no, I haven't seen it. Did you leave it downstairs or something?"
                    sis "I didn't think so, I thought it was in my room. If you borrowed it... Uh, do you hear that?"
                    "Alexia pushes her head down into your lap, your tip rubbing against the back of her throat. You can feel her throat spasm lightly as she tries not to gag."
                    if sisO.freeuse:
                        me "Oh, that? That's just Alexia."
                        "You slide your chair back a little, swiveling so she can see under your desk."
                        sis "Oh! Hey there Alexia. I didn't notice you when I came in."
                        show alex blow1 at right
                        if alexO.freeuse:
                            "Alexia slides off your cock and takes a deep breath before speaking. She strokes you off with her hand while she faces your sister."
                            alex "Hey Lily, good to see you. Me and your brother were just having a little fun, taking a break."
                            show alex blow5 at right
                            "She leans towards you and holds your cock close to her face, running her tongue from base to tip before slipping you back into her mouth."
                            sis "Mmm, looks like a good time. Give it to her good for me, okay [inputName]."
                            me "Sure thing Lily. I'll let you know if I see your charger."
                            hide sis
                            "Lily nods and closes the door as she leaves. Alexia keeps blowing you, taking you extra deep. After a few more minutes she comes up for air again, obviously enjoying herself as much as you are."
                        else:
                            "Alexia slides off your cock, and takes a deep breath. She's suddenly blushing intensly."
                            alex "Oh, hi! I didn't, uh... I..."
                            sis "Don't worry about it, you and [inputName] have fun. Let me know if you find that charger, okay?"
                            me "Sure thing Lily. Talk to you later."
                            hide sis
                            "Lily closes to door again and you turn your attention back to Alexia. Her face is flush and she's taking fast, shallow breaths."
                            me "Sorry about that, I didn't..."
                            show alex blow5 at right
                            "Alexia looks up at you, then down at your cock. She opens her mouth wide and slides you all the way to the back of her throat. You feel her shiver with pleasure as she starts to blow you as fast as she can."
                            me "Oh, did you like getting caught? Is that it?"
                            "Alexia moans and nods her head as best she can while sliding your throat in and out of her soft, warm mouth."
                    else:
                        me "I don't hear it now. No clue what it was."
                        "Lily pauses for a moment, listening intently. Alexia stays deep on your shaft, licking the bottom with her tongue. You feel a shiver of pleasure run down her body."
                        sis "Huh, never mind I guess. Anyway, if you see my charger let me know."
                        me "Will do. Maybe mom has it in her room."
                        hide sis
                        "Lily shrugs and closes the door. A second later Alexia comes off your cock for air. She gasps loudly, then takes a few slow deep breaths."
                else:
                    "Alexia sucks you slowly, but takes you as deep as she can. You do your best to block her from sight."
                    me "Uh no, I haven't seen it. Did you leave it downstairs or something?"
                    sis "I didn't think so, I thought it was in my room. If you borrowed it that's fine, I just need to know where it is."
                    "Alexia pushes her head down into your lap, your tip sliding against the back of her throat. You can feel her throat spasm lightly as she tries not to gag."
                    me "Nope, definitely didn't take it. Maybe it's in mom's room or something."
                    sis "Huh. Okay, thanks anyway."
                    hide sis
                    "Lily closes the door as she heads out, and a second after Alexia comes off your cock for air. She gasps loudly, then takes a few slow deep breaths."
                "Alexia's blowjob has gotten you right to the edge, and you can feel the first spasms of your orgasm arrive."
                menu:
                    "Cum in her mouth.":
                        me "Don't stop, I'm cumming!"
                        "You reach under the desk and grab Alexia's head. You pull her towards you, and she opens her mouth to slip onto your tip just as your first load of cum launches."
                        "You pump your cock back and forth in her mouth a little bit while you release the rest of your load. Finally you're finished and you let go of her head."
                        if alexO.cumslut:
                            "She cimbs out from under the desk and sits back down in her seat. She shivers with pleasure as she gulps down your load."
                        else:
                            "She climbs out from under the desk and sits back down in her seat. Without a word she swallows your load, then takes a few deep breaths."
                        $ alexO.inc_cum_mouth()
                        $ alexO.inc_cum_swallow()
                        me "All good?"
                        alex "Oh ya. Oh fuck that was hot."
                        me "Ya, I can't believe she didn't see you."
                        show alex mast3 at right
                        "Alexia leans back in her chair and pulls up her skirt. She rubs her pussy through her panties for a few seconds, then her thighs tense up and she moans."
                        me "Are you cumming right now?"
                        alex "Fuck yes!"
                        "A few more rubs and Alexia's own orgasm is upon her. She twitches slightly and breathes heavily for a while."
                        me "Well, I don't think we have time for that studying any more."
                        alex "That? Eh, screw it. How hard can the test be?"

                    "Cum on her face.":
                        "You reach down and grab your cock. You stroke yourself as quickly as you can, feeling your cock tense as it gets ready to shoot your load."
                        me "Here it comes, get ready!"
                        "Alexia looks up from under the desk, mouth open and panting loudly. Both her hands are between her legs and she's rubbing her own pussy as quickly as she can."
                        show alex blow6 at right
                        $ alexO.inc_cum_over()
                        "You begin releasing your load, and you send your streams of cum over her face onto her forehead, eyebrows, then nose and mouth."
                        "She moans while you plaster her with cum, twitching with her own orgasm."
                        "Finally you both finish, Alexia collapsed and leaning against the bottom of your chair."
                        alex "Oh fuck that was hot. She almost caught us."
                        me "Ya, I can't believe she didn't see you. And you just didn't stop going!"
                        alex "I got so turned on, I couldn't help myself."
                        me "Well, I don't think we're going to have time to get that studying done now."
                        alex "Eh screw it, how hard can the test be?"
                show alex casual at right
                "You and Alexia take some time getting cleaned up, then you walk her to the door. While you watch her drive away you feel like you've made a major change to her."
                $ alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(test_studying_object.get_resist_change(4))
                $test_studying_object.inc_level(4)

            else:
                alex "Right here, in your room?"
                me "You could get under the desk if it makes you feel more secure."
                alex "No, that's not what I meant. It feels like a strange way to say thank you."
                me "Think of it as making me feel good, which seems like a good reward for helping you out."
                "Alexia thinks for a long time, then shakes her head."
                alex "I'm sorry [inputName], it just doesn't feel right. I've got to trust my gut, you know?"
                "She must have resisted the drug. Better back off and hope she doesn't get suspicious."
                me "Of course, whatever you think is best. How about we finish off that next section then."
                "You and Alex go over the next section quickly. Afterwards she thanks you for all your help and drives home. While you watch her leave you're certain you could have made better use of the situation."
                $ alexO.change_slut_failed()
                $alexO.change_resist(test_studying_object.get_resist_change(0))
                $test_studying_object.inc_level(0)
        "Fuck her on the desk.":
            me "Man am I glad to be done with that. I've been staring at your ass this entire time."
            alex "I thought so, I saw you watching it when I sat down."
            me "How about we both relax and I get behind that ass and have some fun?"
            $ action_difficulty = 60
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                alex "Oh ya, you think you can handle my ass? I have my doubts."
                me "Well then put your assets where your mouth is."
                "Alexia leans forward and kicks her chair away. It slides across the room and bounces into the far wall."
                "She puts her hands against the window across the desk and plants her upper body onto the desk top. Her ass sticks out at you, and she shakes it seductively."
                alex "You're move."
                show alex fuck10 at right
                "You slide her skirt up and out of the way, then take a moment to enjoy her awesome butt. You grab a cheek with each hand and give them a squeeze."
                "Alexia moans and pushes her waist towards you. You give her ass a quick slap, and she yelps quietly."
                "You pull down your own pants and free your cock. You bounce it on one ass cheek a few times, then switch to the other."
                alex "Oh come on, I thought you were actually going to fuck me and not just tease me!"
                me "So you want me to fuck you?"
                alex "I'm bent over your desk and your cock is on my ass. Yes I want you to fuck me!"
                show alex fuck11 at right
                $ alexO.inc_sex()
                "You pull her panties down past her knees and let them fall off. You spread her legs wide and line your shaft up with her pussy."
                "With deliberate slowness you slide yourself inside of Alexia, her slit lubricating your cock as it goes in."
                alex "Ohhhh that feels good."
                "She moans quietly as you slide your full length in, then begin pumping in and out."
                me "You're nice and tight, you feel amazing."
                "In response Alexia grinds her hips against you when you thrust in, moaning more loudly now."
                me "Now, are you ready to really get fucked?"
                alex "Give me your best!"
                "You place your hands on her hips and begin pumping as fast as you can. You pull her into you with each stroke, getting yourself as deep as possible."
                alex "Oh fuck!"
                "She's moaning loudly now. You take a hand off her hip and reach around to her mouth to keep her quiet. You slip three fingers in, which she sucks on vigorously while you fuck her from behind."
                "Alexia tries to moan past your fingers, but you keep her quiet. You can feel her pussy starting to twitch and quiver around your cock, and the feeling of her orgasm drives you towards your own."
                menu:
                    "Cum inside her.":
                        me "I'm getting close, I'm going to cum."
                        "You take your fingers out of her mouth so she can speak."
                        if alexO.cumslut:
                            alex "Fill me up! Pump me full like you're trying to get me pregnant!"
                        else:
                            alex "Cum wherever you want! Fuck!"
                        "You hold her hips and fuck her as fast as you can. A couple more strokes and your cock tenses and begins releasing it's load. You push yourself as deep as you can and stay there until you're finished."
                        show alex fuck12 at right
                        $ alexO.inc_cum_inside()
                        "Finally you pull out, leaving a trail of cum between your tip and her pussy."
                        me "Damn that was good."
                        alex "Oh fuck ya it was."
                        me "We should get cleaned up now."
                        "Alexia stays slumped over your desk as cum starts trickling down her leg."
                        alex "Wait, one more thing."
                        "She grabs her phone from the desk and passes it back to you."
                        if alexO.slut_score > 85 or alexO.cumslut:
                            alex "Take a picture of me, I want to put it online."
                            show alex fuck13 at right
                            "She turns around so you can see her face and smiles, then reaches a hand back and spreads her pussy lips so you can see the entire load."
                            "You use her phone's camera to take a few pictures, then hand it back."
                            #TODO Let you find this on the computer's porn collection.
                        else:
                            alex "Take a picture of me so I can put it online. Just make sure my face isn't in it."
                            "She buries her face in her arms and spreads her legs a little bit more."
                            "You use her phone's camera to take a few pictures, then hand it back."

                    "Cum in her mouth.":
                        me "I'm getting close, I want to finish in your mouth."
                        "You take your fingers out of her mouth so she can speak."
                        if alexO.cumslut:
                            alex "Yes! I want to swallow your cum so badly!"
                        else:
                            alex "Okay! Fuck! I'm ready!"
                        "You hold her hips and fuck her quickly a few times, then pull out as your orgasm reaches it's peak."
                        "Alexia drops to the floor and spins around, quickly taking you in her mouth. She gives you three strokes of her throat before you begin unloading in her mouth."
                        "She reaches up and pumps your cock with her hand while you finish, then slides her mouth off of you slowly."
                        $ alexO.inc_cum_mouth()
                        $ alexO.inc_cum_swallow()
                        if alexO.slut_score > 85 or alexO.cumslut:
                            "Alexia turns around and grabs her phone off of the desk. She swipes it to camera mode, then hands it to you."
                            show alex fuck16 at right
                            "She opens her mouth and shows off your load while you take a few pictures. You even take a moment to caption one of them \"Cum Guzzler\"."
                            "After a few moments she closes her mouth and swallows, taking a deep breath after."
                            alex "How'd they turn out?"
                            me "Great, they look great."
                            alex "Awesome, I can't wait to put those online."
                        else:
                            show alex fuck16 at right
                            "Alexia opens her mouth and shows your load to you, then closes and swallows. She takes a few deep breaths after, and pulls herself back onto her chair."

                    "Cum on her ass.":
                        me "I'm almost there. I'm going to pull out!"
                        "You keep fucking Alexia from behind, and she sucks hard on your fingers while the rest of her body twitches. As you reach your own orgasm you pull out and rest your cock between her ass cheeks."
                        if alexO.cumslut:
                            alex "Yes, plaster me with your hot cum!"
                        else:
                            alex "Cover me [inputName]!"
                        show alex fuck14 at right
                        $ alexO.inc_cum_over()
                        "You pump your load over her back first, then her ass cheeks. When you're done you take a moment and spread it around with the tip of your cock."
                        if alexO.slut_score > 90 or alexO.exhib or alexO.cumslut:
                            "Alexia grabs her phone from the table and hands it back to you."
                            alex "Quick, take some pictures while it's warm."
                            show alex fuck15 at right
                            "She turns her head so you can see her face and smiles, then plants her hands on her cum covered ass and spreads the cheeks wider."
                            "You take a few pictures, then hand the phone back to Alexia."
                            alex "It's going to be so hot when I put these online."
                        else:
                            "Alexia grabs her phone from the table and hands it back to you."
                            alex "Take some pictures, I want to remember how this looks."
                            "She turns her head away from the camera so you can't see her face. You take some pictures of your cock sliding across her cum covered ass."

                    "Cum on her face.":
                        me "I'm almost ready. I want to finish on your face!"
                        "Alexia nods her head vigorously and sucks on your fingers hard."
                        "You pump as fast as you can and feel your orgasm building. You pull out and stroke yourself while Alexia drops to the ground and tilts her head back."
                        show alex fuck17 at right
                        $ alexO.inc_cum_over()
                        "You don't waste any time and unload yourself on her face. You drape your cum over her eyes, mouth and nose, then scrape the leftover drizzles onto her chin."
                        if alexO.slut_score > 90 or alexO.exhib:
                            alex "Quick, get my phone. I want you to take some pictures of me."
                            "You grab it and swipe it to camera mode. You snap a few pictures of Alexia plastered with your cum, and even take a moment to caption one of them \"Cum Dumpster\""
                            "You hand the phone back to her so she can look at the pictures."
                            alex "These are going to be so hot when I put them online."

                me "Well I don't think we're going to have time for that studying."
                alex "Eh fuck it. How hard can it be, right?"
                "You and Alexia take some time getting cleaned up, then you walk her to the door. While you watch her drive away you feel like you've made a major change to her."
                $ alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(test_studying_object.get_resist_change(5))
                $test_studying_object.inc_level(5)
            else:
                alex "Here? We're not even done studying yet."
                me "It'll be a great break, then we can finish later."
                alex "I'm not so sure. I've really got to get this done, and I need you to help me."
                me "Just a few minutes, we can make it quick."
                "Alexia thinks about it for a long time. One of her hands rubs along the inside of her thigh."
                alex "No, it just doesn't feel right. I've got to trust my gut on this one. Sorry [inputName]."
                "She must have resisted the drug. Better back off and hope she doesn't get suspicious."
                me "Of course, whatever you think is best. Maybe next time."
                alex "Right, maybe."
                me "Lets finish off that section then."
                "You and Alex go over the next section quickly. Afterwards she thanks you for all your help and drives home. While you watch her leave you're certain you could have made better use of the situation."
                $ alexO.change_slut_failed()
                $alexO.change_resist(test_studying_object.get_resist_change(0))
                $test_studying_object.inc_level(0)
    jump jumpTimeSkip



label maj_alexLabTest:
    $ lab_test_object.happened = True
    $ temp_slut_score = alexO.slut_score

    me "Well, we've been working on a few different drugs recently. Really experimental stuff."
    alex "Like what?"
    me "You wouldn't recognize the name, but it's a sort of anxiety medication. We think it'll change the way PTSD is treated."
    alex "Wow, how does it work?"
    me "We aren't entirely sure yet. We've tested it out a few times on people, but we need more data points before we can know for certain what it's doing. It's perfectly safe though, so it's only a matter of time."
    call serum_give(alexO) from _call_serum_give_11
    $ temp_slut_score = _return
    "You pull out a vial of colored serum and hand it over to Alexia."
    alex "This is it?"
    me "Yep, that's it. If you wanted to try it out, we can always use more test subjects."
    alex "It's safe, right?"
    me "Completely. We've tested it here in the lab. The effects should only last a few minutes. You may feel a little groggy afterwards, but it should fade within the hour."
    "Alex thinks about it for a moment, then nods."
    alex "Okay, sure. I don't mind giving it a try to help you out. Hell, it may even be fun."
    "You dig up a pad of paper and a pen to look professional and set up a pair of chairs facing each other. You sit down in one, and motion for Alexia to take the other one."
    "She sits down, holding the vial in one hand."
    me "Okay Alexia, when you're ready unstopper the vial and drink all of the substance. Afterwards I'll ask you to answer some questions and perform some tasks, and observe the results."
    alex "Okay. Here we go!"
    "She takes the top off the vial and tips it into her mouth. She swallows, and looks thoughtful for a moment."
    alex "Huh, tastes a little bitter."
    me "That's normal."
    "You scribble on the pad of paper for a few seconds to give the drug time to act."
    me "Alright. Can you hear me Alexia?"
    alex "Yep. Just fine."
    me "Okay. And how are you feeling? Relaxed?"
    alex "Yes, very relaxed, and a little bit nervous."
    me "Good, good. Just trust me and everything will be okay."
    menu:
        "Have her take her shirt off.":
            $ action_difficulty = 0
            $alexO.set_action_exhib()
            $alexO.check_willing(action_difficulty)
            me "Now Alexia, for the next part of this test I'm going to need you to take your shirt off for me."
            alex "My shirt, off?"
            me "That's right."
            show alex strip1 at right
            "She hesistates, then nods and reaches for the bottom of her shirt. She pulls it up and over her head and drops it to the side of her chair."
            alex "Okay, now what?"
            "She waits expectantly, sitting with only a stunningly bright red bra on."
            me "How do you feel right now? Excited, anxious, self concious?"
            alex "Um, maybe a little bit excited."
            me "Okay, and do you know why?"
            alex "Well, I'm trying a new drug, and I'm sitting here in my underwear."
            "You scribble nonsense down on the paper."
            me "Alright. Next, I want you to pull your bra up for me. You don't have to take it off, just pull it above your breasts."
            show alex strip2 at right
            $ alexO.inc_naked()
            "Alexia nods and grabs the middle of her bra and pulls it up. Her tits flop out the bottom, nipples erect."
            me "Perfect. You're looking great."
            alex "Thank you. Is there anything else."
            me "Do you feel any different now?"
            alex "A little more excited I think."
            me "Sexually excited or surprise party excited?"
            alex "Um... Sexually."
            "More random scribbling."
            me "Okay then, I think I have everything I need. You can put your shirt back on now."
            show alex casual at right
            "Alexia does so, and you slip the pad of paper onto a desk."
            me "You did great, this will really help us make quick progress."
            alex "I'm glad I could help."
            me "And I'm glad I could be here to help you help. Now how about I walk you up, so you don't get lost."
            "You guide Alexia back up to the ground floor and say goodbye. As she walks away you're confident you had a major effect on her."
            $alexO.change_slut_rebalanced(action_difficulty)
            $alexO.change_resist(lab_test_object.get_resist_change(1))
            $lab_test_object.inc_level(1)

        "Have her get naked for you.":
            me "Now Alexia, for this part of the test I need you to take off your clothes for me."
            $ action_difficulty = 15
            $alexO.set_action_exhib()
            if alexO.check_willing(action_difficulty):
                "Alexia nods and stands up. She pulls her shirt over her head, then reaches for the waist of her skirt."
                show alex strip3 at right
                "Without asking any questions she undoes a button on the side and slides her skirt off too. She's wearing a stunning red bra and panty set."
                alex "Is this good?"
                me "Keep going. You need to be completely naked."
                show alex strip4 at right
                "She nods and reaches behind her back. With a quick movement she pulls her bra off and drops it to the ground, then slides her panties down to join it."
                "She kicks her panties to the side and stands still for a moment, completely naked."
                me "Wow, you're looking good Alexia."
                alex "Thank you, now what's the next part of the test."
                me "Oh, just sit down and I'll ask you a few questions."
                show alex strip5 at right
                $ alexO.inc_naked()
                "She does so, and you make up a few quick interview questions to kill some time while you stare at her tits and pussy."
                me "Alexia, just grab your breasts for me, will you?"
                show alex strip6 at right
                "Without questioning she does."
                me "Excellent, we've found some types of contact help produce better answers."
                alex "Strange. I guess you're the scientist here though."
                "For a few more minutes you watch her and scribble meaningless things on your note pad. Finally you've had your fill and decide to end things for today."
                me "Okay Alexia, you've been a perfect test subject. You can go ahead and get dressed now."
                show alex casual at right
                "She puts her clothes on quickly, and you offer to take her up to the ground level."
                "As you watch Alexia walk away you feel confident you had a major effect on her."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(lab_test_object.get_resist_change(2))
                $lab_test_object.inc_level(2)
            else:
                "Alexia nods and stands up. She pulls her shirt over her head, then reaches for the waist of her skirt."
                show alex strip1 at right
                alex "What is this testing for exactly?"
                me "Um, a few different things. It's all very complicated."
                alex "I'd like to hear about it actually. It seems a little strange that I have to be naked."
                "She pauses, her skirt waist pulled just below her hips, resting on her ass and thighs."
                me "Well, it tests protein uptake and calorie retention across a wide range of applications."
                "You do your best to invent technobabble."
                alex "Uh huh. Why do I have to be naked though?"
                me "The tests work best with, uh, maximum skin contact."
                "She shakes her head and pulls her skirt back up."
                alex "I don't think I'm comfortable getting naked in front of you, even if it's for science. Sorry [inputName]."
                "She must be resisting the drug. Maybe you pushed her too far all at once."
                show alex casual at right
                me "That's no problem Alexia. Whatever you're comfortable with. You can put your clothes on, and I'll show you out when you're ready."
                "You lead Alexia back to the ground floor and say goodbye. You're certain you could have done something more with the opportunity though."
                $alexO.change_slut_failed()
                $alexO.change_resist(lab_test_object.get_resist_change(0))
                $lab_test_object.inc_level(0)

        "Have her give you a handjob.":
            me "Okay, for this test we will be testing your physical dexterity. I'll need you to come over to me and sit close."
            "Alexia nods and moves her chair over beside yours."
            me "Now, your task is to make me orgasm with your hands."
            $ action_difficulty = 30
            $alexO.set_action_cumslut()
            if alexO.check_willing(action_difficulty):
                alex "So, a handjob?"
                me "We try to avoid putting it in common slang, but yes."
                "She pauses, then nods and reaches for your pants. She undoes the zipper and slides them down."
                alex "That makes sense. It's suprisingly hard to give a good handjob, so if your medicine was affecting me somehow you might be able to notice."
                show alex hand1 at right
                $ alexO.inc_hand()
                "She wraps her hand around your shaft and begins stroking it quickly."
                alex "The penis does have plenty of nerve endings, so it would make a good measurement device for things like this."
                me "Exactly, you're a natural."
                "She smiles and keeps stroking you with one hand. After a few minutes you begin leaking precum down your cock. She pauses."
                alex "Is it okay if it's lubricated like that?"
                me "Oh, of course. In fact it's encouraged for better results."
                "Alex doesn't say anything, but brings her hand up to her mouth and licks it from palm to finger tip. She then returns it to your shaft and starts rubbing faster."
                alex "Well then that should make things easier."
                "You spend the next few minutes enjoying Alexia's soft slippery hand stroking you off and you feel your orgasm building."
                me "I'm getting close, keep going."
                alex "Great! Am I doing better than the other test subjects?"
                me "Much!"
                "You tense up and begin to release. Alexia keeps stroking you, and you fire off your load onto the lab floor."
                "She stops, and you spend a few moments catching your breath."
                show alex casual at right
                me "Well that was a great success I say."
                alex "Me too, glad I could help out with your research."
                me "Any time. Now, how about I walk you to the ground floor then get things cleaned up down here."
                alex "Sounds good."
                "You walk Alexia upstairs and say goodbye. You feel confident you've made a [alexO.effect_string] impact on her today."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(lab_test_object.get_resist_change(3))
                $lab_test_object.inc_level(3)

            else:
                alex "Finish you with a handjob? What does that even test?"
                me "Physical dexterity, hand softness, previous experience, a whole range of variables."
                "She strokes your thigh and thinks about it for a while."
                alex "I'm not sure..."
                me "It's fine Alexia, I'm a scientist."
                "She pauses her stroking and moves her hand back to her own lap."
                alex "I don't think I can do it. Is there any other sort of test?"
                "She must be resisting the drug. Maybe you pushed her too far."
                me "Uh, yes, of course."
                "You make up a quick questionaire and ask Alexia a few meaningless questions. She seems satisfied with the test and doesn't say anything about the initial plan."
                me "Okay, that's some useful data. How about I walk you back up to the ground floor so you don't get lost."
                alex "Thanks, that would be nice."
                "You walk Alexia up and say goodbye. You're pretty sure you could have done something more with the situation though."
                $alexO.change_slut_failed()
                $alexO.change_resist(lab_test_object.get_resist_change(0))
                $lab_test_object.inc_level(0)

        "Have her give you a blowjob.":
            me "Okay Alexia, for this test I need you to come kneel in front of me. You're going to use your mouth and make me cum."
            $ action_difficulty = 45
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                alex "So a blowjob?"
                me "Right. We try to avoid the common names if we can, for test purposes."
                "She hesitates, then gets onto her knees in front of you."
                alex "Okay, any special rules or do I just go at it?"
                me "Go at it however you would like to start with. I'll let you know if the test parameters change."
                "She nods and reaches for your pants. You unzip them for her and pull them down, revealing your hard cock."
                alex "Is this timed?"
                me "Not timed exactly, but speed is a factor. Just do whatever comes naturally."
                show alex blow1 at right
                $ alexO.inc_blow()
                "You hold the notepad above her head and scribble. She grabs your cock and brings it to her mouth, then starts licking it from all sides."
                "Once it's properly wet she slides her mouth over the tip, then moves down and takes the whole length into her mouth."
                me "Very good."
                "Alexia begins moving her head up and down at a steady speed while you make random meaningless notes on the note pad. You even take a moment to appreciate her hot ass over her shoulder."
                "As time goes on Alexia steadily speeds up her movements, until you can hear soft wet noises coming from her mouth with every stroke."
                "You feel your orgasm building, and you put the notepad to the side."
                me "Okay Alexia, you're doing great so far. You've almost got me to cum."
                show alex blow1 at right
                menu:
                    "Cum in her mouth.":
                        show alex blow1 at right
                        me "Test protocol says you will have to take my semen in your mouth, okay?"
                        "She nods gently on your cock, but doesn't stop blowing you."
                        "A few seconds later you begin tensing up as you release your load."
                        "Alexia places your tip in the middle of her mouth and strokes your shaft with a hand while you pulse out your cum."
                        $ alexO.inc_cum_mouth()
                        "After a few seconds she pulls back and looks at you."
                        me "That was great, you did great."
                        "Alexia doesn't say anything, but looks around quickly."
                        "She grabs a piece of paper from a nearby desk and snatches the pen out of your hand. She quickly scribbles onto the paper."
                        if alexO.cumslut:
                            "It reads: \"You taste so good! Want me to swallow?\""
                        else:
                            "It reads: \"Should I swallow?\""
                        show alex blow1 at right
                        menu:
                            "Make her swallow.":
                                show alex blow1 at right
                                me "Of course, it's very important for the test."
                                "Alexia nods and pauses for a moment, then makes a loud swallowing noise. When she's finished she takes a deep breath and pants for a few seconds."
                                me "Good job. I'll need to check to make sure you got it all."
                                if alexO.cumslut:
                                    alex "I'm not about to waste a single drop, don't worry. Take a look."
                                else:
                                    alex "Oh, okay."
                                $ alexO.inc_cum_swallow()
                                "She kneels back on the ground in front of you and opens her mouth wide. She tilts her head so the light shows everything, and you can see there isn't a drop left."
                                me "Excellent, looks like a perfect test."

                            "Let her spit it out.":
                                show alex blow1 at right
                                if alexO.cumslut:
                                    me "You can spit it out if you want."
                                    "She shakes her head and starts to swallow. She has to take a couple big gulps until it's all gone."
                                    alex "Ah... There was no way I was going to waste that delicious spunk [inputName]. I thought you knew me better than that."
                                    $ alexO.inc_cum_swallow()
                                else:
                                    me "You don't have to. You can spit it out into the sink if you wish."
                                    "Alexia speed walks to the sink and leans over, making a loud spitting noise. She takes a deep breath and pants for a few seconds."
                                    alex "Whew! I guess I should have asked that earlier, huh."
                                    me "Oh no, my mistake for not letting you know."

                    "Cum on her face.":
                        me "Test protocol states I have to finish on your face. It will test for potential skin irritation."
                        "Alexia nods and continues to blow you at an impressive speed."
                        "A few seconds later you begin tensing and tap her on the shoulder."
                        "Alexia pulls off your cock with a wet pop and sits back. She closes her eyes and mouth and waits for you to stroke yourself to completion."
                        show alex blow2 at right
                        $ alexO.inc_cum_over()
                        "Your cock spasms and begins covering her face with your load. After a few seconds you're finished, and wipe the last drop on her chin."
                        me "Perfect. All finished."
                        alex "Okay. Good. Glad I could help."
                        me "You're welcome to use the sink to clean up. Let me know if there is any redness in the next few minutes."
                        "Alexia uses one of the sinks to wash your cum off her face, then smiles at you."
                        alex "That was fun, it's cool I can help with real science here."

                show alex casual at right
                me "Thank you for your help Alexia. How about I walk you upstairs so you don't get lost."
                alex "That would be great, thanks."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(lab_test_object.get_resist_change(4))
                $lab_test_object.inc_level(4)
            else:
                alex "You want me to give you a blowjob?"
                me "For science, of course."
                "You point to the note pad, flashing her your scribbled notes quickly as proof."
                "Alex nods and walks over, then gets on her knees."
                alex "I don't think I've ever heard of an experiment that included a blowjob."
                me "Well, it's not exactly lab policy."
                alex "I can imagine."
                "She rubs your thighs, working up to your waist."
                alex "How can you even publish results like this then?"
                me "It's... Uh, it's difficult."
                "She stops and looks at you."
                alex "Maybe we should try a different test then. No point doing all this work if the data isn't useful."
                me "No, I'm sure we can make this work. Just keep going."
                alex "No, I think this is a little strange. Lets try something else."
                "She must be resisting the drug. Maybe you pushed her too far."
                me "Okay. I'm sure I can ask some questions and get some good information."
                "You make up a few interview questions to fill the time. Afterwards you offer to guide her back up to the ground floor."
                alex "Thanks, that would be helpful."
                "After you say goodbye and watch Alexia walk away you feel like you could have done more with the situation."
                $alexO.change_slut_failed()
                $alexO.change_resist(lab_test_object.get_resist_change(0))
                $lab_test_object.inc_level(0)

        "Fuck her.":
            me "For this test we're going to check the drug's affect on arousal. You're going to need to take off your clothes to get ready."
            $ action_difficulty = 60
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                alex "Okay, I can do that."
                show alex strip4 at right
                "She stands up and begins stripping down. First her sweater, then her skirt, then her bright red undies."
                alex "So how does this work? How do you measure arousal?"
                me "Well, we've found the most direct way is the best. You're going to bend over one of the tables, and I'll do whatever I can do to make you cum."
                alex "That doesn't sound very... scientific."
                show alex fuck1 at right
                "Despite this, she goes to the nearest table and bends over it, just like you asked."
                me "It's the best way we've found. Your subjective experience is more important than any time data we gather anyway. Make sure to let me know how you're feeling throughout the process."
                alex "Okay, I can do that."
                "You drop your own pants and peel off your shirt as you walk up behind Alexia."
                me "Are you ready?"
                alex "Yes. I'm feeling horny right now, and I'm pretty wet."
                "You hold your cock in your hand and get lined up, then start to slide into her pussy."
                "Alexia gasps as you slide your full length in, then you begin to pump."
                $ alexO.inc_sex()
                alex "Ahhh, that feels good. I think it felt better than normal when you entered me."
                me "Okay, noted."
                "You pump into Alexia from behind, enjoying the view of her ass. You give it a quick slap and watch it bounce around."
                alex "That felt good too. I'm getting more wet now."
                "You slap Alexia's butt a few more times, then grab both cheeks with your hands and use them to pull yourself into her faster."
                alex "Ahhh, ahhh, it's definitely more intense than I'm used to. I think you could make me orgasm like this."
                me "Good, keep telling me what works."
                "You keep fucking Alexia, moving faster or slower as she reports what feels the best."
                alex "I'm getting close, keep going and I'm going to cum!"
                me "That's the goal then! Get ready!"
                "You pump your cock into her pussy as fast as you can, and you feel her tighten up around your cock. She moans loudly, and her legs start to shake."
                "Her orgasm drives you quickly on to your own."
                menu:
                    "Cum inside her.":
                        me "I'm almost done as well. Get ready!"
                        "Alexia nods and pants, hips bucking and legs spasming as you fuck her orgasming pussy."
                        "A few more thrusts and you tense as you begin releasing your load. You grab her hips and pull her in tight against you."
                        show alex fuck2 at right
                        $ alexO.inc_cum_inside()
                        "She opens her mouth and lets out a silent scream as one big spasm wracks her body, and then she falls limp against the table panting quickly."
                        me "Test complete, I think."
                        alex "I think so. I came, probably the hardest I've cum in a while. I guess that's some good information for you."
                        me "It definitely is. Now lets get cleaned up."

                    "Cum in her mouth.":
                        me "I'm almost finished too. Test protocol states I have to finish in your mouth. Get ready!"
                        "Alexia nods and pants, hips bucking and legs spasming as she continues to orgasm."
                        "After a few thrusts you're ready to cum and you slap her on the ass to get her moving. You pull out with an audible pop and Alexia drops to the ground and spins around."
                        show alex fuck3 at right
                        $ alexO.inc_cum_mouth()
                        $ alexO.inc_cum_swallow()
                        "You push your cock into her mouth as the first pulse shoots out a line of cum. She holds you in while you finish releasing, then slides her mouth off slowly."
                        "She swallows loudly, then looks up at you."
                        alex "I hope I was suppose to swallow."
                        me "Oh, that's perfect. Good job."
                        alex "Glad I could help."
                        me "Now, we should get cleaned up."

                    "Cum on her ass.":
                        me "I'm almost finished. I'm going to pull out when I cum."
                        "Alexia nods and pants, hips bucking and legs spasming as she continues to orgasm."
                        "After a few more thrusts you're ready and you pull your cock out of her pussy. You slap it down between her ass cheeks and stroke yourself as you begin cumming."
                        show alex fuck4 at right
                        $ alexO.inc_cum_over()
                        "Your load shoots out across her back, and you move your tip around to get some on her ass cheeks as well."
                        "Afterwards you both pant loudly, trying to catch your breath."
                        alex "I came, so test complete."
                        me "Ya, that was some good data. Now we should get cleaned up quickly."

                    "Cum on her tits.":
                        me "I'm almost finished. I'm going to need to cum on your tits for the test."
                        "Alexia doesn't ask questions, just nods and pants. Her hips buck up and down and she continues to spasm in her orgasm."
                        "After a few more thrusts you're ready and pull out of her. You give her ass a slap to get her moving, and stroke yourself while she gets on her knees."
                        show alex fuck5 at right
                        $ alexO.inc_cum_over()
                        "She gets her tits in her hands just in time, and you begin letting your load out over them. A few seconds of gasping and cum shooting and you're finished."
                        "Alexia looks down at the strings of cum over her tits and smiles."
                        alex "Successful test I suppose."
                        me "Very. Now we should get you cleaned up."
                show alex casual at right
                "After a few minutes of tidying the lab up you walk Alexia upstairs so she doesn't get lost. As she's walking away you're confident you had a major effect on her today."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(lab_test_object.get_resist_change(5))
                $lab_test_object.inc_level(5)

            else:
                alex "How exactly are we checking the effects?"
                me "It's going to be a practical test. If I can make you orgasm the drug must be having some sort of effect."
                alex "But how do we know you couldn't make me orgasm before. You need some sort of control."
                me "Hmm, perhaps your right. We can set a follow up exam for the future."
                "Alexia laughs."
                alex "Good one [inputName]. But seriously, what is the test? It's not like you can just fuck every test subject you get in here."
                me "Of course not, that would be silly..."
                "She looks like she's resisting the drug. Maybe you pushed her too far."
                me "The real test is just a short interview."
                "You make up a few questions to fill the time. Afterwards you offer to guide her back up to the ground floor."
                alex "Thanks, that would be great."
                "After you say goodbye and watch Alexia walk away you feel like you could have done more with the situation."
                $alexO.change_slut_failed()
                $alexO.change_resist(lab_test_object.get_resist_change(0))
                $lab_test_object.inc_level(0)

    jump campusJumpTimeSkip

label maj_spikeMallDrink:
    $ mall_event_object.happened = True
    $ temp_slut_score = 0
    "You pop the top off her drink."
    call serum_give(alexO) from _call_serum_give_9
    $ temp_slut_score = _return
    "You mix the serum in quickly and stir it in with a straw. A quick glance around confirms nobody noticed you do anything."
    show alex casual at right
    "A minute later Alexia comes back out of the store. She grabs her drink and takes a sip."
    alex "Thanks. There was nothing in there, so I guess we're back on the hunt."
    me "I guess so. You should finish your bubble tea though, so I don't have to wait outside."
    alex "Right, sure."
    "She sucks back the rest of her drink in one go, then drops the empty cup into a garbage can."
    alex "Hmm, where next?"
    "Alexia thinks about it for a moment, then nods and sets off for a store across the hall."
    alex "Ah! Follow me, there's some good stuff in here."
    "As you enter the store Alexia starts to slow down. She looks around, eyes not quite focusing on the clothing."
    alex "Hmm, see anything you like?"
    menu:
        "Have her change outfits in front of you.":
            $ action_difficulty = 0
            $alexO.set_action_exhib()
            $alexO.check_willing(action_difficulty)
            "You take a quick look around the store. You find a skimpy little outfit for Alexia, a pair of jean short shorts and a blue tanktop. You even grab a pair of shoes to go with it."
            me "How about this? I'll come with you into the changing room and let you know what I think."
            "Alexia takes the outfit and looks at it for a moment."
            alex "It's a little small, don't you think?"
            me "No, I think it'll look great on you. Trust me, lets go try it on."
            "She nods and leads you to the back of the store. The changing rooms are small alcoves with a curtain to pull across the opening. Nobody is watching, so you slip into one and slide the curtain closed."
            "You take a seat on a bench on the wall while Alexia places the clothing beside you and starts taking her clothes off."
            "She pulls off her sweater and places it on the bench beside you, then drops her skirt to the floor as well."
            "She sits down and strips her socks off, then her shoes."
            me "Looking good Alexia."
            alex "I haven't even put it on yet."
            show alex sexy at right
            $ alexO.inc_naked()
            "She picks up the jean shorts and slides them on, then pulls the top on and buttons up the bottom few buttons. She puts the shoes on last, then stands and faces you."
            alex "Well, what do you think?"
            me "Give me a little turn."
            show alex sexystrip1 at right
            "She spins around slowly, giving you a great view of her ass. The shorts are so small you can see her underwear peeking out the edges."
            me "I think it looks great."
            alex "You think so? It seems so small."
            me "That's fine, it shows off your natural assets. You look beautiful and sexy in it."
            show alex sexy at right
            "Alexia smiles at you and checks herself out in the mirror."
            alex "Alright, I'm sold. Lets grab this and head out."
            show alex casual at right
            "Alexia strips out of her new outfit and puts on her old one. You head to the front together and buy the clothes, then head back out into the mall."
            "You shop for another hour, but she doesn't find anything else that interests her. You say goodbye at the bus stop and head home. You feel like you made a [alexO.effect_string] impact on Alexia today."
            $alexO.change_slut_rebalanced(action_difficulty)
            $alexO.change_resist(mall_event_object.get_resist_change(1))
            $mall_event_object.inc_level(1)
        "Have her try on different underwear in front of you.":
            "You point towards the underwear section of the store."
            me "Some of that stuff looks pretty nice. Think you would like to try some on?"
            alex "Well you wouldn't be able to see it though."
            me "I could if I came into the changing room with you."
            $ action_difficulty = 15
            $alexO.set_action_exhib()
            if alexO.check_willing(action_difficulty):
                "Alexia walks over to the racks of underwear and looks at it for a while."
                alex "What should I try?"
                me "Just pick whatever stands out. Go wild."
                "She takes a few minutes and picks out a couple of sets, then leads you to the back of the store."
                "The changing rooms are small alcoves with a curtain to pull across the opening. Nobody is watching, so you slip into one and slide the curtain closed."
                "You sit down on a bench at the side of the room while Alexia strips out of her clothes."
                show alex strip4 at right
                $ alexO.inc_naked()
                "She places her sweater and skirt to the side, then takes her bra and panties off too."
                alex "Okay, lets try this one first."
                show alex sexystrip2 at right
                "She pulls up a white pair and starts putting them on."
                "She gives you a spin to show off her ass, then checks herself out in the mirror."
                show alex sexystrip3 at right
                alex "This has potential. What do you think?"
                "The set is a fairly simple white panty set, form fitting but not extravagant."
                me "I'll wait until I've seen them all until I make any judgement."
                show alex strip4 at right
                "Alexia nods and pulls the white underwear off. She places it to the side and picks up a purple set."
                show alex sexystrip4 at right
                "A moment later and she's slipped them on. The bra covers most of her breasts, and the panties cling tight to her ass cheeks."
                show alex sexystrip5 at right
                "She turns around to show her ass off."
                alex "This is pretty nice too. Hmm. Hard choices."
                me "Lets see the last one, then we can decide."
                show alex strip4 at right
                "Once again she gets naked and picks up a tiny red set."
                show alex sexystrip6 at right
                "Alexia gives it a good try, squeezing her tits into the tiny seethrough bra and pulling the panties as high up as they'll go."
                alex "Wow, this barely covers everything."
                show alex sexystrip7 at right
                "The panties are a bare minimum g-string, and everything is made of translucent lace."
                alex "What do you think, which one do you like?"
                menu:
                    "Pick the white set.":
                        me "The white set. You looked gorgeous in it."
                        alex "I think so too. Alright, lets do it."
                    "Pick the purple set.":
                        me "The purple set. It complimented your body the most."
                        alex "It did make my tits look great. Okay, I'll get it."
                    "Pick the red set.":
                        me "This red set. You look super sexy in it."
                        alex "It feels so dirty too, worse than not wearing anything. I definitely want it."
                show alex casual at right
                "She puts her clothes back on and walks out with you to the front of the store. She pays for it, and the two of you get back to shopping for another hour."
                "Eventually you're both tired, and Alexia hasn't found anything else to interest her. You walk to the busses together, then head your separate ways. As you wave goodbye you feel like you've made a [alexO.effect_string] impact on her."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(mall_event_object.get_resist_change(2))
                $mall_event_object.inc_level(2)
            else:
                "Alexia walks over to the racks of underwear and looks at it for a while."
                alex "I think the employees would notice. We better not risk it."
                me "I'm sure they won't mind. It will just be a few minutes."
                "Alexia shakes her head, becoming more confident."
                alex "No, I don't think I like any of this stuff anyway. Lets just head out."
                "She must have been pushed too far and resisted the drug."
                me "Alright, I'll follow you then."
                "You and Alexia do some more shopping, and after an hour decide to head home. You walk to the busses together, then head your separate ways. As you wave goodbye you feel like you could have done more with the situation."
                $alexO.change_slut_failed()
                $alexO.change_resist(mall_event_object.get_resist_change(0))
                $mall_event_object.inc_level(0)
        "Have her tit fuck you in a changing room.":
            "You gaze down at her tits and nod."
            me "I see a pair of things I would like to try on. How about we slip into a changing room and give them a try?"
            $ action_difficulty = 30
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                "Alexia glances around the store."
                alex "But if we just go back there for no reason someone's going to notice."
                me "Alright, I'll find an outfit for you to try on. We can kill two birds with one stone."
                alex "Okay, that sounds good."
                "You take a quick walk around the store and pick out a skimpy little outfit for Alexia. You even grab shoes for her."
                "The changing rooms are small alcoves with a curtain to pull across the opening. Nobody is watching, so you slip into one and slide the curtain closed."
                me "Here, I think this would look great on you."
                "You hand the clothes to Alexia and take a seat on a small bench on the side of the room."
                show alex sexy at right
                "She nods and strips out of her own clothing. In another moment she's slid on the tight jean shorts and blue tanktop."
                alex "What do you think?"
                me "I want to see it in action before I make any decision."
                "You slide your pants down and pop your cock out."
                "Alexia pulls the blue tanktop up above her tits and kneels down on the floor."
                show alex sexytit1 at right
                $ alexO.inc_tit()
                "Without saying a word she pulls her bra forward a little and fits your cock between her cleavage. Then she lets go, and her bra holds you in place."
                "She looks up and smiles at you, then starts sliding her tits up and down along your shaft."
                alex "How does that feel?"
                me "It feels great, your tits are so soft."
                "Alexia speeds up, using her hands to push her tits in from the side and letting the bra hold you in from the front."
                "After a few minutes she stops and looks down. She opens her mouth and lets a large glob of spit fall between her tits."
                alex "How about now?"
                me "Oh god, even better."
                "Another minute of being fucked by her slippery breasts and you're getting ready to cum."
                me "I'm almost there Alexia."
                "She nods."
                alex "Cum between my tits."
                show alex sexytit2 at right
                "She keeps tit fucking you until you tense up. As you start cumming she sticks your tip in between her cleavage and lets you fire off all of your cum between her breasts."
                $ alexO.inc_cum_over()
                "She pulls up slowly when you're done, and your cum slides down from between her tits onto her stomach."
                me "Wow, that was great."
                alex "What about the outfit?"
                me "I love it too."
                alex "Good, then I don't have to worry about getting it dirty."
                show alex sexy at right
                "Alexia pulls the tanktop down over her cum covered front and smoothes it into place as best she can."
                alex "Come on, lets go pay for this."
                "You walk to the front of the store, and Alexia explains that she liked the outfit so much she wants to wear it out the door. They look up the codes and ring her up, and you two are able to leave."
                "You wander the mall for another hour before you're ready to leave. The whole time Alexia's shirt clings to the underside of her bra, but she tries not to pay attention to it."
                "You walk to the busses together and say goodbye. As you leave you feel like you've made a [alexO.effect_string] impact on her."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(mall_event_object.get_resist_change(3))
                $mall_event_object.inc_level(3)
            else:
                "Alexia takes a moment to respond, then shakes her head."
                alex "I like shopping here, if we got caught I'd be banned for life."
                me "I'm sure nobody will notice. Just a quick tit fuck."
                alex "I said no. Lets just get back to shopping, okay?"
                "Her eyes seem more focused, and she seems more aware of what is going on. She must have been pushed too far and resisted the drug."
                me "Alright, forget I said anything. I'll follow you."
                "You and Alexia do some more shopping, and after an hour decide to head home. You walk to the busses together, then head your separate ways. As you wave goodbye you feel like you could have done more with the situation."
                $alexO.change_slut_failed()
                $alexO.change_resist(mall_event_object.get_resist_change(0))
                $mall_event_object.inc_level(0)
        "Have her blow you in a changing room.":
            "You lean close and kiss her."
            me "I'd like to try these lips on. How about we slip into a changing room and you let me give them a try?"
            $ action_difficulty = 45
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                "Alexia glances around the store."
                alex "But if we just go back there for no reason someone's going to notice."
                me "Alright, I'll find an outfit for you to try on. We can kill two birds with one stone."
                alex "Okay, that sounds good."
                "You take a quick walk around the store and pick out a skimpy little outfit for Alexia. You even grab shoes for her."
                "The changing rooms are small alcoves with a curtain to pull across the opening. Nobody is watching, so you slip into one and slide the curtain closed."
                me "Here, I think this would look great on you."
                "You hand the clothes to Alexia and take a seat on a small bench on the side of the room."
                show alex sexy at right
                "She nods and strips out of her own clothing. In another moment she's slid on the tight jean shorts and blue tanktop."
                alex "What do you think?"
                me "I want to see it in action before I make any decision."
                "You slide your pants down and pop your cock out."
                show alex sexyblow1 at right
                $ alexO.inc_blow()
                "Alexia doesn't say anything, but drops to her knees in front of you. She takes your tip into her mouth and starts bobbing up and down, getting deeper with every pass."
                "You reach a hand down and play with a tit through her clothing while she blows you. She moans and speeds up, licking the bottom of your cock as she goes."
                me "That feels great."
                "She nods and keeps going."
                "After a few minutes you can feel your orgasm approaching."
                me "I'm almost ready!"
                "Alexia blows you as fast as she can, her throat making soft wet noises as you hit the back. You tense up and begin to climax."
                "A voice outside of the change room speaks up."
                "Stranger" "Excuse me, do you need any assistance in there?"
                menu:
                    "Let Alexia pull off and answer.":
                        "You lean back and Alexia pulls your cock from her mouth. She strokes you off with one hand while looking to the right where the curtain is."
                        alex "No, I'm just fine in here."
                        show alex sexyblow2 at right
                        $ alexO.inc_cum_over()
                        "You start cumming and have to hold back a moan. Alexia sprays your cum all over her tits."
                        alex "Thank you though, I'll let you know if I need anything."
                        "Stranger" "Okay then."
                        "Alexia puts the tip of your cock between her cleavage as you dribble out the last of your load."
                        if alexO.cumslut:
                            alex "Wow, thank you so much for this [inputName]."
                            "She runs a finger over the slope of her breasts, scooping up some of your cum before bringing it to her lips and licking it clean."
                            alex "I think I'm going to have to buy these now. I don't think many people other than me would want clothes covered in your spunk."
                        else:
                            alex "Wow, good job. I think I'm going to have to buy these now."

                    "Force Alexia to stay on and stay quiet.":
                        show alex sexyblow3 at right
                        "You put a hand on the back of Alexia's head and push her down on your cock as you cum. She braces her hands on the bench, but doesn't make a noise as you shoot your load down her throat."
                        "Stranger" "Hello? Anyone in there?"
                        "Alexia's throat tightens and sucks on your sensitive cock."
                        "Stranger" "Nobody? Huh..."
                        show alex sexy at right
                        $ alexO.inc_cum_mouth()
                        $ alexO.inc_cum_swallow()
                        "You hear footsteps walking away, and when you think you're safe you let Alexia up for air."
                        "She gasps when she's free and takes a moment to catch her breath."
                        me "Sorry, I needed to make sure you didn't make any noise."
                        alex "Fuck that was so hot. You made me cum."
                        "She sits down beside you while you stuff yourself back into your pants."
                        me "From almost getting caught?"
                        if alexO.cumslut:
                            alex "And your semen, it felt so nice and warm sliding down my throat. I think I've gotten the shorts a little wet, I'm just going to buy the whole outfit so they don't ask any questions."
                        else:
                            "Alexia nods."
                            alex "I've probably gotten these shorts a little wet, so I think I should just buy the whole outfit."
                show alex casual at right
                "Alexia gets changed into her normal outfit and the two of you head up to the front of the store. The cashier scans the clothes, and if they notice anything wrong with them they don't comment."
                "Afterwards you wander the mall for about an hour, but nothing interested Alexia. You walk to the bus stop together and say goodbye. As you're heading off you feel like you've made a [alexO.effect_string] impact on her."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(mall_event_object.get_resist_change(4))
                $mall_event_object.inc_level(4)
            else:
                "Alexia takes a moment, then shakes her head."
                alex "If they noticed we'd be kicked out of here for life. I like being able to shop here. I don't think it's worth the risk."
                me "Oh come on, I'm sure nobody will notice."
                "She shakes her head."
                alex "I said no, just drop it, okay?"
                "Her eyes seem more focused, and she's more aware of what she's doing. She must have been pushed too far and resisted the drug."
                me "Alright, forget I said anything. I'll just follow you."
                "You and Alexia do some more shopping, and after an hour decide to head home. You walk to the busses together, then head your separate ways. As you wave goodbye you feel like you could have done more with the situation."
                $alexO.change_slut_failed()
                $alexO.change_resist(mall_event_object.get_resist_change(0))
                $mall_event_object.inc_level(0)
        "Fuck her in a changing room.":
            "You step close and whisper into her ear."
            me "I don't see anything right now, but I'd like to see me wearing your pussy like a glove. Lets slip into that changing room."
            $ action_difficulty = 75
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                "Alexia glances around the store, biting her lower lip."
                alex "We'll need an excuse to be back there, in case someone asks."
                me "I'll find you a hot outfit to wear. This way we'll be killing two birds with one stone."
                alex "Okay, that sounds good."
                "You take a quick walk around the store and pick out a skimpy little outfit for Alexia. You even grab shoes for her."
                "The changing rooms are small alcoves with a curtain to pull across the opening. Nobody is watching, so you slip into one and slide the curtain closed."
                me "Here, put this on."
                show alex sexy at right
                "Alexia changes into the outfit you picked up. A set of jean hot pants, a blue tanktop, and red shoes."
                alex "What do you think?"
                me "I think I want to see you on my cock."
                "She smiles and motions for you to sit down on the bench to the side."
                show alex sexyblow1 at right
                "You do, and she gets on her knees. She slips your dick free of your pants and wastes no time in putting it in her mouth."
                "She blows you for a few minutes until you're both wet and hard, then she stands up."
                show alex sexyfuck1 at right
                $ alexO.inc_sex()
                "She takes the shorts off and pulls her panties to the side, then turns around and goes to sit on your lap."
                "You hold onto the base of your cock and guide your tip into Alexia's pussy as she decends."
                "You can hear her gasp slightly as you slide all the way into her tight slit. She pauses a moment, then starts fucking you while you're sitting."
                me "Fuck that feels good."
                if alexO.exhib:
                    alex "I know. Fuck, you feel so big."
                else:
                    alex "I know, oh god I know. Be quiet though, or someone will catch us."
                "She speeds up, and the only sound in the room is the soft noise of her ass against your thighs with each stroke."
                "Alexia seems to be going as fast as she can, but after a few minutes you desperately want more of her."
                show alex sexyfuck2 at right
                "You stand up suddenly, and Alexia gasps as she falls forward, planting her arms on the far wall to stop from stumbling completely."
                "Now upright, you grab her ass with both hands and start fucking her as fast as you want."
                if alexO.exhib:
                    "She moans loudly, obviously not worried about anyone outside the changeroom."
                    alex "Keep fucking me, I'm going to cum soon. Ah!"
                    "Stranger" "Hello? Is everything alright in there?"
                    me "Uh, yeah, everything is fine!"
                    "Alexia moans again and bucks her hips against you, pushing you deep inside of her. Her pussy is drenched and quivering around your hard cock."
                    "Stranger" "Are you sure? Who's in there?"
                    alex "Ah! Here I cum!"
                    "Alexia's legs shake and she lets out a loud yelp. You keep pumping into her from behind, driving yourself to your own climax as well."
                else:
                    "She moans lightly, but tries to stay quiet as you pound her pussy from behind."
                    "A few short minutes of doggy style and Alexia's legs start to shake. She starts to moan, then shoves her knuckles in her mouth and bites down to avoid making any noise. Her pussy twitches around you as she orgasms."
                    "Feeling her cum drives you close to your own climax."
                menu:
                    "Cum inside her.":
                        "You don't say anything, but keep fucking Alexia until you start to cum. You thrust in time with each pulse, and Alexia gasps a little with each new addition."
                        show alex sexyfuck3 at right
                        $ alexO.inc_cum_inside()
                        "When you're finished you pull out and watch as your load starts to leak out and run down her leg."
                        if alexO.cumslut:
                            alex "It's so nice and warm..."
                        "Alexia pulls her panties back in place to try and stop it, but stays bent over while she catches her breath."
                        if alexO.exhib:
                            "There are footsteps nearby, and the curtain to the change room is thrown open. Two staff members stare at you and Alexia, your sperm still leaking out of her despire her best attempts to stop it."
                            alex "Shit, run!"
                            "Alexia grabs her jean pants on the bench and the two of you take off, rushing past the two shocked staff. The detectors at the front of the store beep loudly as you run past them, and you're gone before anyone can chase you."
                            show alex sexy at right
                            "You slow down when you're outside, giving Alexia time to get dressed again."
                            alex "Wow. That was amazing."
                            "She wraps her arms around you and pulls you into a deep kiss. Her hips grind against you while you make out for a moment. Finally she pulls back again."
                            alex "We should do that again. Soon."
                            me "I'll make sure we do. For now we should get going."
                        else:
                            me "Come on, we should get going."
                            alex "Ya, right."
                            show alex sexy at right
                            "She pulls the jean shorts on quickly, and the two of you walk to the front of the store. She explains that she likes them so much she wants to wear them out, and after paying you both feel ready to head home."
                        "As you say goodbye you feel like you've made a [alexO.effect_string] impact on her today."

                    "Cum on her ass.":
                        show alex sexyfuck4 at right
                        $ alexO.inc_cum_over()
                        "You don't say anything, but keep fucking Alexia until you start to cum. You pull out at the last minute and spray your load over both her ass cheeks. You tap your tip on her to get the last few drops."
                        if alexO.cumslut:
                            alex "Mmm, you treat me so well [inputName]. I love feeling you sprayed over my ass."
                        "You sit down and start getting your pants back on while Alexia stays bent over, catching her breath."
                        if alexO.exhib:
                            "There are footsteps nearby, and the curtain to the change room is thrown open. Two staff members stare at you and Alexia, your sperm still covering her ass."
                            alex "Shit, run!"
                            "Alexia grabs her jean pants on the bench and the two of you take off, rushing past the two shocked staff. The detectors at the front of the store beep loudly as you run past them, and you're gone before anyone can chase you."
                            show alex sexy at right
                            "You slow down when you're outside, giving Alexia time to get dressed again."
                            alex "Wow. That was amazing."
                            "She wraps her arms around you and pulls you into a deep kiss. Her hips grind against you while you make out for a moment. Finally she pulls back again."
                            alex "We should do that again. Soon."
                            me "I'll make sure we do. For now we should get going."
                        else:
                            me "Come on, we should get going."
                            alex "Right, sure."
                            show alex sexy at right
                            "She pulls up her jean shorts, hiding your cum under them. You walk to the front of the store, and Alexia explains that she likes the outfit so much she wants to keep it on."
                        "You walk to the bus after and say goodbye. As you're heading off you feel like you've made a [alexO.effect_string] impact on her today."

                    "Cum in her mouth.":
                        me "I'm almost there, You're going to swallow it."
                        if alexO.cumslut:
                            alex "Yes, please! I'll take every drop you give me!"
                        else:
                            "Alexia nods but doesn't say anything, still trying not to make any noise."
                        show alex sexyfuck5 at right
                        "You fuck her until you start to cum, then pull out and push yourself into her mouth as soon as she's on the floor and ready."
                        "No sooner to you get inside than you start firing off your load. Alexia locks eyes with you while you fill up her mouth."
                        show alex sexyfuck6 at right
                        $ alexO.inc_cum_mouth()
                        $ alexO.inc_cum_swallow()
                        if alexO.exhib:
                            "There are footsteps nearby, and the curtain to the change room is thrown open. Two staff members stare at you and Alexia, your cock still firmly in her mouth."
                            "Alexia gurgles something through her mouthful of cum and jumps up, grabbing her jean shorts in one hand and your arm in the other."
                            "The two of you take off, rushing past the two shocked staff. The detectors at the front of the store beep loudly as you run past them, and you're gone before anyone can chase you."
                            show alex sexy at right
                            "You slow down when you're outside, giving Alexia time to get dressed. She has to take a moment and gulp down your cum before she can speak again."
                            alex "Wow. That was amazing."
                            "She wraps her arms around you and pulls you into a deep kiss. Her hips grind against you while you make out for a moment. Finally she pulls back again."
                            alex "We should do that again. Soon."
                            me "I'll make sure we do. For now we should get going."
                        else:
                            "She slides off and opens wide so you can look, the closes and swallows it all."
                            me "Good girl. Now we should get going."
                            alex "Right. I think I'm going to get the outfit."
                            show alex sexy at right
                            "She pulls on her shorts and you both head up the the front. Alexia explains that she wants to wear the outfit out the door, and once you're done paying you head to the bus stop and say goodbye."
                        "As you leave you feel like you made a [alexO.effect_string] impact on her today."

                    "Cum on her face.":
                        me "I'm almost there, I'm going to finish on your face."
                        if alexO.cumslut:
                            alex "Yes, please! Give me every last drop you can!"
                        else:
                            "Alexia nods but doesn't say anything, still trying not to make any noise."
                        "You fuck her until you start to cum, then pull out and stroke yourself as she gets into position."
                        show alex sexyfuck7 at right
                        $ alexO.inc_cum_over()
                        "No sooner does she get on her knees than you start blasting your load across her face. She keeps her eyes open as your cum lands over her glasses, and licks a little that landed on her lips."
                        if alexO.exhib:
                            "There are footsteps nearby, and the curtain to the change room is thrown open. Two staff members stare at you and Alexia, your cum plastered over her face."
                            alex "Shit, run!"
                            "Alexia grabs her jean pants on the bench and the two of you take off, rushing past the two shocked staff. The detectors at the front of the store beep loudly as you run past them, and you're gone before anyone can chase you."
                            show alex sexy at right
                            "You slow down when you're outside, giving Alexia time to get dressed and clean your sperm off her glasses."
                            alex "Wow. That was amazing."
                            "She wraps her arms around you and pulls you into a deep kiss. Her hips grind against you while you make out for a moment. Finally she pulls back again."
                            alex "We should do that again. Soon."
                            me "I'll make sure we do. For now we should get going."
                        else:
                            me "Good girl, you look great."
                            "Alexia pants and nods again, then starts wiping the cum off her face with her origional outfit."
                            alex "Fuck it, I'm just going to buy this so they don't ask questions."
                            show alex sexy at right
                            "You walk to the front of the store together and Alexia explains she wants to wear the outfit out the door. When you're done paying you walk to the bus stop together and say goodbye."
                        "As you leave you feel like you made a [alexO.effect_string] impact on her today."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(mall_event_object.get_resist_change(5))
                $mall_event_object.inc_level(5)
            else:
                "Alexia takes a moment and thinks. She bites her lower lip a little, but shakes her head."
                alex "If they noticed we'd get kicked out for life. I like this mall."
                me "I'm sure they won't notice, we'll be fine."
                alex "They'd be able to hear us."
                me "I'll be perfectly quiet."
                alex "I wouldn't be though. Now just drop it, okay?"
                me "Alright, forget I said anything. Lead the way, I'll follow you."
                "You and Alexia do some more shopping, and after an hour decide to head home. You walk to the busses together, then head your separate ways. As you wave goodbye you feel like you could have done more with the situation."
                $alexO.change_slut_failed()
                $alexO.change_resist(mall_event_object.get_resist_change(0))
                $mall_event_object.inc_level(0)

    jump jumpTimeSkip

label maj_alex_beach:
    $ alex_beach_event_object.happened = True
    $ temp_slut_score = 0
    call serum_give(alexO) from _call_serum_give_26
    $ temp_slut_score = _return
    #Move up to the changing rooms.
    "You mix the serum into Alexia's drink, then get everything balanced and head up the slope to meet up with her. You find her sitting at a picnic table, taking shelter in the shade of an umbrella."
    alex "There you are, I'm starving!"
    me "Good, because I've got food! Here you go."
    "You split up the food and dig in. You keep a careful eye on Alexia's drink, waiting until she's drunk most of it to speak up."
    me "Hey Alexia, I think I forgot something up by the change rooms earlier today. If you're finished with your lunch, could you come up and help me look for it?"
    alex "Sure. I guess we can head up right now."
    "You lead Alexia away from the beach to the change rooms. Most of them are empty this time of day, and you pick a stall as far away from other people as possible."
    me "Here we go, lets see..."
    "You pull open the curtain and check inside, confirming there's nothing inside."
    me "Nope, nothing here. I guess I was wrong."
    alex "Oh, I'm sorry. Is there anywhere else we should check?"
    me "No, I think I was just mistaken earlier. No big deal. But if we're anyways, there's something I'd like to do."
    alex "What would that be?"
    menu:
        "Have her flash you her tits.":
            $ action_difficulty = 0
            $alexO.set_action_exhib()
            $alexO.check_willing(action_difficulty)
            me "You've been looking so cute in your swimsuit, I'd love to get a look at your boobs before the end of the day. If we step in here, would you show them to me?"
            "Alexia thinks for a split second, then smiles and nods."
            alex "Of course [inputName]. Come on."
            $ alexO.inc_naked()
            if slut_outfit:
                show alex strip38 at right
            else:
                show alex strip37 at right
            "She steps inside of the change room, and you close the curtain behind the two of you. She doesn't waste any time pulling her bikini top up, letting her tits slip out of the bottom."
            alex "There you go. Take a good look."
            "She leans forward and jiggles them a few times."
            me "They look just as good as I thought they would. Thanks Alexia."
            if slut_outfit:
                show alex swim2 at right
            else:
                show alex swim1 at right
            "She smiles at you and pulls her top back down into place. It takes her a moment to get her breasts back into their cups properly."
            alex "Thank you, I think they're pretty nice too. If that's all for now, lets head back to the table. The sun's killing me, I want to spend some time in the shade."
            "You and Alexia return to the picnic table and chat for another half hour in the shade. You feel like you've had a major effect on her today."
            $alexO.change_slut_rebalanced(action_difficulty)
            $alexO.change_resist(alex_beach_event_object.get_resist_change(1))
            $alex_beach_event_object.inc_level(1)

        "Have her strip for you.":
            me "Well, you look so good in that cute swimsuit. I've been distracted all day thinking about what you would look like out of it."
            alex "And you'd like me to show you?"
            "You nod, and Alexia takes a moment to think."
            $ action_difficulty = 15
            $alexO.set_action_exhib()
            if alexO.check_willing(action_difficulty):
                alex "Alright, lets do this then. Come on."
                "She steps onto the change room, waiting until you've stepped in to close the curtain."
                alex "Lets see, I suppose I should start off with this..."
                $ alexO.inc_naked()
                if slut_outfit:
                    show alex strip40 at right
                else:
                    show alex strip39 at right
                "Alexia undoes her bikini top, pulling it up and over her head and throwing it towards you. You catch it, feeling how warm it is before hanging it on a peg on the wall."
                alex "Should I keep going?"
                "She fiddles with her swimsuit bottom, pulling it down a little, then back up."
                me "Yes, please."
                alex "It would be a little mean to leave you like this. Here you go."
                show alex strip45 at right
                "She turns around and bends forward, peeling her swimsuit down until it's past her thighs and she can let it drop to the ground. She wiggles her ass at you, letting you get a good look at her pussy from behind."
                me "Oh god, you look amazing Alexia."
                show alex strip46 at right
                "Alexia sways her hips for a few seconds, then turns back to face you."
                alex "I'm glad you think so. Mmm, this feels so nice to do."
                "She holds her breasts, squeezing them and sighing."
                alex "Have you gotten a good look?"
                me "More than just \"good\", I think."
                "She smiles and reaches past you, grabbing her top off of the peg beside you."
                alex "Then lets get back to the table, I want to hang out in the shade for a little bit."
                if slut_outfit:
                    show alex swim2 at right
                else:
                    show alex swim1 at right
                "Alexia pulls her swimsuit back on quickly, jiggling her tits to get them settled into her top again."
                "The two of you return to the picnic table and chat for another half hour while you wait for the serum to wear off completely. You feel like you've had a major effect on her today."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(alex_beach_event_object.get_resist_change(2))
                $alex_beach_event_object.inc_level(2)

            else:
                alex "I don't know [inputName]. It feels a little personal, you know?"
                me "There's nothing wrong with it, you'd just be helping a friend out. Right?"
                alex "Maybe..."
                "She makes patterns in the sand with one of her feet, staring down at it while she thinks."
                alex "But I just don't feel comfortable with it. Maybe some other time, okay?"
                "She looks up at you again, and you notice she's looking a little sharper now. She must have resisted the serum, and pushing her harder would only make things worse."
                me "Whatever you're comfortable with Alexia. How about we head back to the table and get into some shade, it's hot as balls out here."
                alex "Yeah, lets do that."
                "You and ALexia return to the picnic table and chat for another half hour in the shade while the serum wears off."
                $alexO.change_slut_failed()
                $alexO.change_resist(alex_beach_event_object.get_resist_change(0))
                $alex_beach_event_object.inc_level(0)

        "Have her give you a titjob.":
            me "You look so good in that little swimsuit, I keep wanting to slide myself between your top and have a little fun. What do you say?"
            $ action_difficulty = 30
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                alex "I say we take care of that right away. Come on."
                "She grabs your hand and pulls you into the changing room, closing the curtain behind you."
                alex "You just stand right there, and leave this all to me."
                $ alexO.inc_tit()
                if slut_outfit:
                    show alex tit13 at right
                else:
                    show alex tit12 at right
                "Alexia drops to her knees. She brushes her hands along your thighs, sliding them up until she reaches your swimsuit. Then she pulls it down, gasping softly when your hard cock springs free."
                me "Just slip me between your tits. They look so nice."
                "She nods and sits up a little, hooking her bikini around the top of your shaft then sliding back down."
                alex "Just like that? Mmm, you feel so warm between my boobs."
                "She holds her breasts in her hands and pushes them together, squeezing your dick between them."
                me "God, that feels perfect."
                "Alexia starts to work her tits up and down, massaging you with them. She picks up speed as she goes, eventually reaching a steady rhythm."
                alex "You're so hard... Fuck that's hot."
                "She gives you a few more fast strokes, then pauses and leans back to look up at you. Your shaft strains against the front of her bikini, threatening to pull it off entirely."
                alex "Give me some warning before you cum."
                me "Sure, just keep going, please."
                alex "Of course. How rude of me."
                "She looks back down and resumes her titfuck, going even faster than before. It doesn't take much more before you feel your orgasm approaching."
                me "Get ready!"
                alex "Go for it!"
                $ alexO.inc_cum_over()
                if slut_outfit:
                    show alex tit15 at right
                else:
                    show alex tit14 at right
                "She looks up at you and keeps working her breasts up and down. You tense up and grunt as you orgasm, spraying your load out the top of her clevage and onto her chest."
                "Your cum drips down between her tits, pooling where she has them pressed together. You're both silent for a moment while you catch your breath."
                alex "Wow... Good job, that was impressive."
                "She slides her boobs off of your shaft and sits back. Your semen starts to drip out of her clevage down onto her stomach."
                me "Thanks Alexia, that was great. Want to head back to the table?"
                alex "Yeah. Let me just stop by at the showers quickly and get this cleaned off."
                if slut_outfit:
                    show alex swim2 at right
                else:
                    show alex swim1 at right
                "She stands up and brushes some of the sand from her legs, then strides boldly out of the changing room. You walk with her to the public showers, where she cleans off your cum."
                "Once that's done you head back to the table and relax in the shade while the serum wears off completely. You feel like you've had a major effect on her today."
                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(alex_beach_event_object.get_resist_change(3))
                $alex_beach_event_object.inc_level(3)

            else:
                "Alexia pauses, eyes dropping to your crotch while she thinks."
                alex "I don't know [inputName]. It feels a little weird doing that here."
                me "It's just a little fun between friends, right? It won't take very long."
                "She makes patterns in the sand with one of her feet, tearing her eyes away from your obvious erection to look at them."
                alex "I know, but I just don't think I would be comfortable. Okay?"
                "She looks up at you again, and you notice she's got a sharper look in her eye. She must have resisted the serum, and pushing her harder would only make things worse."
                me "Whatever you're comfortable with Alexia. How about we head back to the table and get into some shade, it's hot as balls out here."
                alex "Yeah, lets do that."
                "You and Alexia return to the picnic table and chat for another half hour in the shade while the serum wears off."
                $alexO.change_slut_failed()
                $alexO.change_resist(alex_beach_event_object.get_resist_change(0))
                $alex_beach_event_object.inc_level(0)

        "Have her blow you.":
            me "Well you look amazing in that swimsuit, and it's gotten me a little worked up. I was hoping we could slip into the changing room and you could help me let off some steam with a quick blowjob."
            "You rub your crotch, tracing the shape of your obvious erection."
            $ action_difficulty = 45
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                alex "Oh you poor thing. Let me take care of that for you..."
                "She reaches forward and cups your crotch, rubbing your hard shaft a few times. She pulls you into the change room and closes the curtain behind you."
                $ alexO.inc_blow()
                if slut_outfit:
                    show alex blow28 at right
                else:
                    show alex blow27 at right
                "Without another word she drops to her knees and yanks your swimsuit down. Your hard cock bounces free, and she lets it rest on her cheek for a moment."
                alex "Lets get it wet first, I suppose..."
                "She holds your shaft gently with one hand and runs her tongue along the sides and bottom of your cock. Once you're dripping wet she strokes you off a few times."
                alex "Does that feel wet enough yet?"
                me "I think it'll do. Ah!"
                if slut_outfit:
                    show alex blow30 at right
                else:
                    show alex blow29 at right
                "Alexia slides the tip of your cock onto her mouth, then pushes herself down it slowly. She takes you down to your base in a single pass, pausing to look up at you while your full length is down her throat."
                me "Oh fuck!"
                "She wiggles her head a little, and you feel her throat spasm lightly around your dick. Then she slides back up and off, taking a deep breath once you're free of her mouth."
                alex "There, that seems wet enough now."
                "Alexia slips you back into her mouth and starts to suck you off. Her tight, wet throat sends shivers up your spine."
                "You lean back against the changing room wall, moaning softly as she throats you. Soon you can feel a growing tightness in your core as your orgasm approaches."
                menu:
                    "Cum in her mouth.":
                        me "I'm almost there Alexia, I want to cum in your mouth!"
                        "She pauses with your shaft half way down her throat and nods a few times, then starts to suck you off again."
                        "Alexia pulls back as you start to climax, leaving the tip of your cock resting on her lips while she looks up at you."
                        $ alexO.inc_cum_mouth()
                        if slut_outfit:
                            show alex blow32 at right
                        else:
                            show alex blow31 at right
                        "You grunt as you cum, emptying your balls into her mouth. She waits patiently until you've finished, then licks the last few drops from your tip and sits back."
                        "She keeps her sperm filled mouth open, swirling her tongue through the off-white liquid while you watch."
                        menu:
                            "Tell her to swallow.":
                                me "Good girl, now drink up for me."
                                "She nods and closes her mouth. You watch while she gulps down your load, then opens again to show you that it's all gone."
                                $ alexO.inc_cum_swallow()

                            "Let her decide.":
                                if temp_slut_score > 75 or alexO.cumslut:
                                    $ alexO.inc_cum_swallow()
                                    "You stay quiet and watch as Alexia closes her mouth and starts to gulp down your load. Once she's done she opens up again to show you that it's all gone."
                                else:
                                    "You stay quiet and watch as Alexia turns to the side and lets your cum out in a long stream. She spits out the last little bit, then looks up at you and smiles."
                        if slut_outfit:
                            show alex swim2 at right
                        else:
                            show alex swim1 at right

                        if alexO.cumslut:
                            alex "Thank you so much [inputName], you tasted delicious. I hope you're feeling better now too."
                        else:
                            alex "Ah, that was hot [inputName]. I hope you're feeling better now."
                        me "Much. Lets head back to the table and chill out for a little bit."
                        "You and Alexia return to the pincic table and chat for another half hour while you wait for the serum to wear off completely. You feel like you've had a major effect on her today."

                    "Cum on her tits.":
                        me "I'm almost there Alexia, I want to cum on your tits!"
                        "She pauses with your shaft half way down her throat and nods a few times, then starts to suck you off again."
                        "She pulls back as you start to climax, barely getting your tip free of her mouth before you start to shoot off your load. She grabs her tits and squeezes them together while you stroke yourself off."
                        if alexO.cumslut:
                            alex "Yes, give me that hot load of yours! Oh god, I want it so badly!"
                        else:
                            alex "Ah! That's it, let it all out!"
                        $ alexO.inc_cum_over()
                        if slut_outfit:
                            show alex tit15 at right
                        else:
                            show alex tit14 at right
                        "You guide your cock left and right, spreading your cum evenly over both tits. When you're done she wipes the last few drops off your tip with her finger, then brings it up to her mouth and licks it clean."
                        alex "Mmm, you really did try and cover me. I think you did a pretty good job of it too."
                        if alexO.cumslut:
                            "She runs a finger between her clevage, scooping up some of your semen before bringing it up to her lips and licking it clean."
                        else:
                            "She runs a finger between her clevage, dragging it through lines of your semen."
                        me "I think I did, yeah. Lets go get you cleaned up and head back to the table."
                        if slut_outfit:
                            show alex swim2 at right
                        else:
                            show alex swim1 at right
                        "You and Alexia head over to the public showers, where she cleans your semen off her chest."
                        "Once that's done, you head back to the picnic table and chat for a half hour in the shade while you wait for the serum to wear off completely. You feel like you've had a major effect on her today."


                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(alex_beach_event_object.get_resist_change(4))
                $alex_beach_event_object.inc_level(4)

            else:
                "Alexia pauses, eyes following your hand as it slides up and down the length of your shaft."
                alex "I... I don't know [inputName]. Right here? With everyone around?"
                me "There's nobody nearby, and we'll be inside the change room anyway. You'd really be helping out a friend."
                "She sighs and looks around, then turns back to you and shakes her head."
                alex "No, I don't think I'd be comfortable with that. If you want to... Take care of that, I can wait for you back at the table."
                "She's got a sharper look in her eye now. She must be resisting the serum, pushing her harder would only make things worse."
                me "It's okay, lets just forget I said anything in the first place. Getting back to the shade sounds like a great idea."
                alex "Yeah, lets do that."
                "You and ALexia return to the picnic table and chat for another half hour in the shade while the serum wears off."
                $alexO.change_slut_failed()
                $alexO.change_resist(alex_beach_event_object.get_resist_change(0))
                $alex_beach_event_object.inc_level(0)

        "Fuck her.":
            me "You look so great in that little swimsuit, I've gotten pretty horny. I wanted to pull you inside here and take you for a ride."
            "You rub your crotch, tracing the shape of your obvious erection."
            $ action_difficulty = 60
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $alexO.set_action_freeuse()
            if alexO.check_willing(action_difficulty):
                #Include public section if applicable
                alex "You poor thing. Here, lets go take care of this right away."
                "She grabs your hand and pulls you into the change room, pulling the curtain closed behind you."
                "Before you can say anything she wraps her arms around you and kisses you. Her tongue brushing playfully against your lips."
                "While you make out she slides her hands lower, eventually resting on them on the waistband of your swim trunks. She pulls them down slowly, until your cock springs free and rubs against her inner thigh."
                alex "Oh god, I think I need this just as badly as you do [inputName]. I don't want to wait any longer, please give it to me!"
                "She kisses you again, more forcefully this time, and grinds her hips against your cock. You respond by guiding her to one of the changing room walls, pressing her up against it."
                "You reach down and pull Alexia's swimsuit to the side, giving you clear access to her pussy. You rub your cock against her lips a few times and feel her tremble in response."
                alex "Ah! Yeah, that's it. Slide it into me nice and slow. Oh god..."
                $ alexO.inc_sex()
                if slut_outfit:
                    show alex fuck56 at right
                else:
                    show alex fuck55 at right
                "She gasps and shivers as you slip yourself into her wet cunt, pushing her against the wall. Her fingernails scrape across your back, and she lifts one leg up to wrap around your waist."
                me "There, is that what you want?"
                alex "Mmm, uhuh!"
                "Alexia arches her back and rolls her hips against you, pushing you even deeper. You start to thrust in and out of her and lean forward to kiss her at the same time."
                "Her tongue meets yours, and she moans softly while you fuck her."
                alex "Oh god, [inputName]... Fuck me harder! Fuck!"
                "She pulls away from your mouth to moan loudly, her whole body trembling against you."
                me "You want it harder? I'll see what I can do..."
                if slut_outfit:
                    show alex fuck58 at right
                else:
                    show alex fuck57 at right
                "You reach down and grab her by the ass with both hands. You then lift her up and press her against the wall, lifting her off her feet entirely."
                if alexO.exhib:
                    alex "Fuck, yes! Oh god!"
                else:
                    "Alexia leans forward and presses her head against your shoulder, using your neck to muffle her shouts and moans."
                "With Alexia pinned against the wall you are free to set your own pace. You alternate between pounding her as hard as you can, and sliding in and out slowly while you play with her ass."
                "After spending a few minutes enjoying her dripping wet pussy you feel your orgasm building up."
                menu:
                    "Cum inside of her.":
                        me "Here we go!"
                        "You pull Alexia tight against you, pushing your cock as deep as you can manage while you pump your load into her."
                        if alexO.cumslut:
                            alex "Fuck yes! Fill me up, pump me full!"
                        else:
                            alex "Fuck!"
                        $ alexO.inc_cum_inside()
                        if slut_outfit:
                            show alex fuck60 at right
                        else:
                            show alex fuck59 at right
                        "She writhes in your arms, quivering with pleasure and rolling her hips to keep you moving inside of her. A few seconds after you've finished filling her pussy up with cum she gasps, then relaxes."
                        me "That felt amazing Alexia."
                        "She buries her face in your shoulder and nods, panting loudly. You lower her gently to the ground, supporting her for an extra moment while her legs regain their strength."
                        alex "Wow... I... Just wow..."
                        "She leans against the wall, your cum trickling out of her cunt and onto the sand below."
                        me "When you're feeling up to it, lets head back to the table."
                        if slut_outfit:
                            show alex swim2 at right
                        else:
                            show alex swim1 at right
                        "She nods, and takes a minute or two to recover her strength. Then she pulls her swimsuit back into place, and follows you to the picnic table. You chat for another half hour while the serum wears off completely, and you feel like you've had a [alexO.effect_string] impact on her."

                    "Cum on her face.":
                        me "Get on your knees, I want to cum on your face!"
                        "You give Alexia's cunt one last deep thrust, then pull out and lower her to the ground. She's on her knees and ready for your load in a second."
                        alex "Come on, give it all to me [inputName]. Fuck, I want it so bad!"
                        $ alexO.inc_cum_over()
                        if slut_outfit:
                            show alex fuck62 at right
                        else:
                            show alex fuck61 at right
                        "You grunt as you climax, pumping your thick load over Alexia's face. She stays perfectly still for you, letting you cover her from forehead to chin."
                        "When you're done you lean against the far wall and take a few deep breaths. Alexia slumps onto the sand, your cum dripping off her chin onto her tits."
                        alex "Wow... It's so warm..."
                        me "You look good like that Alexia. We should do this more often."
                        "She smiles and nods."
                        alex "Yeah, I think we should."
                        "She licks a drop of semen off her lips as it trickles down."
                        if alexO.exhib or alexO.cumslut:
                            alex "When you're ready to go, lets head over to the showers so I can clean this off."
                            me "Sure, lets go."
                            "Alexia pulls her swimsuit back into place, then strides confidently out of the changing room. She heads over to the public showers with your load still plastered across her face."
                            if slut_outfit:
                                show alex swim2 at right
                            else:
                                show alex swim1 at right
                            "She draws a few curious glances whlie she walks, but says anything to the two of you as she washes herself clean."
                        else:
                            alex "Shit, I guess I need to clean this all up somehow. I can't exactly go outside like this."
                            $ alexO.inc_cum_swallow()
                            "She thinks for a moment, then shrugs and starts to wipe your sperm off with her finger. She licks her finger clean after each pass, and soon has herself looking presentable again."
                            alex "That'll have to do."
                            if slut_outfit:
                                show alex swim2 at right
                            else:
                                show alex swim1 at right
                            me "Yeah. Lets head back to the tables and chill out for a little while."
                        "You and Alexia head back to your picnic table and relax in the shade. You chat for another half hour while the serum wears off, and you feel confident you've had a [alexO.effect_string] impact on her."

                $alexO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(alex_beach_event_object.get_resist_change(5))
                $alex_beach_event_object.inc_level(5)

            else:
                "Alexia pauses, eyes following your hand as it slides up and down the length of your shaft."
                alex "I... I don't know [inputName]. Right here? With everyone around?"
                me "There's nobody nearby, and we'll be inside the change room anyway. It'll feel great, I promise."
                "She sighs and looks around, then turns back to you and shakes her head."
                alex "No, I don't think I'd be comfortable with that. If you want to... Take care of that, I can wait for you back at the table."
                "She's got a sharper look in her eye now. She must be resisting the serum, pushing her harder would only make things worse."
                me "It's okay, lets just forget I said anything in the first place. Getting back to the shade sounds like a great idea."
                alex "Yeah, lets do that."
                "You and ALexia return to the picnic table and chat for another half hour in the shade while the serum wears off."
                $alexO.change_slut_failed()
                $alexO.change_resist(alex_beach_event_object.get_resist_change(0))
                $alex_beach_event_object.inc_level(0)

    return

###########################
##Multi-girl Major Scenes##
###########################

label maj_noraMomThreesome:
    $ nora_mom_study_event_object.happened = True
    call serum_give(noraO) from _call_serum_give_16
    $ temp_nora = _return
    call serum_give(momO) from _call_serum_give_17
    $ temp_mom = _return
    "You mix the serums into the wine then head back to the girls in the dining room."
    show mom casual at left
    show nora casual at right
    me "Here you go ladies."
    mom "Thank you [inputName]."
    nora "Yes, thank you."
    mom "Now where were we?"
    "Mom and Nora chat back and forth, drinking their wine a few sips at a time. After a few minutes you decide they've had enough of a dose to push things further."
    me "You're both just letting your wine sit there. Drink up, I can always go get you more."
    mom "Nora has to drive, she should probably go easy."
    nora "Oh I'll be fine. One glass isn't that bad."
    "Nora takes a big gulp of her wine."
    mom "Oh fine, I don't want to be left out."
    "She joins in, and after a few more minutes of talking they've both finished their drinks."
    nora "Maybe I spoke too soon, the drink's hitting me a little harder than I'm used to."
    mom "Me too. I guess we got a little carried away."
    me "Do you both feel okay though? Relaxed?"
    "Nora and mom both nod, eyes losing focus as they stare into the indeterminate distance."
    me "Good. You should both just relax, it's been a hard day. I know something we could do to really relax."
    "Both of the girls look at you with quizzical looks."
    menu:
        "Have them compare tits.":
            $ action_difficulty = 0
            $momO.set_action_exhib()
            $momO.check_willing(action_difficulty)
            $noraO.set_action_exhib()
            $noraO.check_willing(action_difficulty)
            me "How about a friendly competition? I've spent a bunch of time with both of you, and I've always wondered something."
            mom "What's that?"
            me "Which one of you has the nicer breasts. I see them in various clothes every day, but I can never get a direct comparison."
            "Nora and mom glance at each other. Nora shrugs, and mom nods."
            nora "I can see why you might think that, your mother's a good looking woman."
            mom "Well thank you Nora, you are as well. Now I'm curious what [inputName] thinks about us."
            "Nora starts unbuttoning her shirt and sweater, while mom does the same."
            show mom strip9 at left
            show nora strip9 at right
            $ momO.inc_naked()
            $ noraO.inc_naked()
            "A moment later and they've both pulled their tops off, leaving them just in their bras."
            "Mom giggles when she looks at Nora."
            mom "What are the odds!"
            nora "Hmm?"
            mom "Our bras, we wear the same one."
            nora "I suppose you bought yours at the department store."
            "Mom nods."
            nora "Me as well. Great minds think alike I suppose."
            show mom strip10 at left
            "Mom reaches behind her back and undoes her bra, letting it fall to the ground."
            mom "There we go. What do you think?"
            nora "They look great Jennifer. How about me?"
            show nora strip11 at right
            "Nora undoes her bra and slides it off as well. The two women compare tits to each other."
            mom "Very nice too. I certainly wouldn't complain if we swapped."
            nora "[inputName], what do you think?"
            menu:
                "Mom is the winner.":
                    me "I've got to say my mom wins by a little bit. You've both got terrific breasts though, I'm glad I got a chance to take a look."
                    "Nora looks at mom's boobs and nods."
                    nora "I can see why you think that. I think you're right."
                    mom "You're both too kind, you're making me blush!"
                    nora "Well you deserve it. Now, we should get dressed so [inputName] and I can get back to work."
                    mom "Right, of course."
                "Nora is the winner.":
                    me "Sorry mom, but I think Nora's edged you out by a little bit. Don't get me wrong though, you've both got amazing breasts. I'm glad I got to take a peek and finally settle this."
                    "Mom smiles and nods."
                    mom "They are quite nice, aren't they. Perky, large. Very nice."
                    nora "Well thank you, both of you. I personally think you've got me beat Jennifer, but I won't argue."
                    mom "Thank you too then! Now I should let you two get back to work, I've distracted you for long enough."
            show mom casual at left
            show nora casual at right
            "The two girls get their shirts back on, and mom heads upstairs to her room."
            "After another half an hour of work Nora leans back and sighs."
            nora "I think there was a printing error, this doesn't seem possible."
            me "Well, it was the practice that was important anyway, right?"
            nora "Right. Well, thank you for having me over [inputName]. Make sure to thank your mom as well, she was a delightful host."
            "You walk Nora to the door and say goodbye. As she drives off you feel like you've had a [noraO.effect_string] impact on her today."
            $ noraO.change_slut_rebalanced(action_difficulty)
            $ momO.change_slut_rebalanced(action_difficulty)
            $noraO.change_resist(nora_mom_study_event_object.get_resist_change(1))
            $momO.change_resist(nora_mom_study_event_object.get_resist_change(1))
            $ nora_mom_study_event_object.inc_level(1)
        "Have them compare bodies.":
            me "You two are getting along so well, I'm wondering how much you have in common."
            nora "We do seem to share some interests."
            mom "It's interesting to hear about the lab. It seems like such a high stress job."
            me "Plus you're both drop dead gorgeous."
            $ action_difficulty = 15
            $momO.set_action_exhib()
            $noraO.set_action_exhib()
            if noraO.check_willing(action_difficulty) and momO.check_willing(action_difficulty):
                nora "And there is that."
                mom "Ha, you're going to make me blush!"
                nora "He's right though. You're a good looking woman, there's nothing wrong with admitting it. I hope I am too."
                mom "You certainly are, I just don't get complimented like that very often."
                me "You should show off to each other. I'm sure you both don't get many chances to compare yourselves like that."
                "The girls glance at each other, then nod."
                nora "That sounds like a great idea, if you're interested."
                mom "Sure, it sounds like fun."
                show mom strip10 at left
                show nora strip11 at right
                $ momO.inc_naked()
                $ noraO.inc_naked()
                "Mom and Nora begin stripping off clothes. First their shirts, then they slide off their bras as well."
                nora "Well, in terms of breasts we're almost evenly matched."
                mom "Yours are perkier than mine, which is nice."
                nora "Yours are larger though. I think that balances it out."
                show mom nightstrip3 at left
                show nora strip5 at right
                "Mom slides her pants down, and Nora does the same. Panties are dropped just as quickly."
                show nora strip12 at right
                "Nora turns around first, showing her ass to mom."
                nora "What do you think?"
                mom "Good size, looks nice and soft. A very nice butt if I may say so. And me?"
                show nora strip5 at right
                show mom nightstrip4 at left
                "Mom spins around and Nora takes a moment looking at her ass too."
                nora "Well shaped, perky, big and soft. I think we're evenly matched here too."
                show mom nightstrip3 at left
                "The girls turn back to each other and smile."
                mom "Lets call it a draw then. We can both be smoking hot, right."
                nora "Right. That seems the fairest way to call it."
                "They chat for a few minutes more, and you take the opportunity to ogle both of their bodies. Finally mom speaks up."
                mom "I should really let you two get back to work though, I've distracted you enough."
                nora "It was no problem at all. Thank you for being such a great host."
                mom "You're welcome over any time."
                show mom casual at left
                show nora casual at right
                "They get their clothes on quickly, and mom heads upstairs to her room."
                "After another half an hour of work Nora leans back and sighs."
                nora "I think there was a printing error, this doesn't seem possible."
                me "Well, it was the practice that was important anyway, right?"
                nora "Right. Well, thank you for having me over [inputName], let me know if you find any more interesting problems like that."
                "You walk Nora to the door and say goodbye. As she drives off you feel like you've had a [noraO.effect_string] impact on her and a [momO.effect_string] impact on mom today."

                $ noraO.change_slut_rebalanced(action_difficulty)
                $ momO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(nora_mom_study_event_object.get_resist_change(2))
                $momO.change_resist(nora_mom_study_event_object.get_resist_change(2))
                $ nora_mom_study_event_object.inc_level(2)
            else:
                if temp_nora <= 15:
                    nora "[inputName], that's really not appropriate."
                    mom "Come on Nora, it's just a compliment."
                    nora "But we have to work together. We might not be in the office, but we should keep it professional."
                    me "Oh come on, it's nothing serious."
                    "Nora shakes her head and seems to be getting her focus back. She must be resisting the drug."
                    nora "Come on, we need to get this work done. I've got to head out soon."
                    mom "I'll leave you two to it then. Good luck."
                else:
                    mom "[inputName]! That's no way to talk to your boss."
                    nora "Jennifer, it's fine. It was just a compliment."
                    me "Of course, nothing serious about it."
                    mom "Still, that isn't appropriate talk for someone you work with."
                    me "Alright, I'm sorry if I offended you Nora."
                    nora "It's quite alright."
                    "Mom looks at you sternly. She seems to be regaining her focus and must be resisting the drug."
                    mom "I'll let you two get back to work. Stay on topic [inputName]."
                    me "Right, of course."
                "Mom heads up to her room while you and Nora get back to work. After fifteen minutes you give up and Nora leaves. As you wave goodbye you feel like you could have done more with the situation."
                $ noraO.change_slut_failed()
                $ momO.change_slut_failed()
                $noraO.change_resist(nora_mom_study_event_object.get_resist_change(0))
                $momO.change_resist(nora_mom_study_event_object.get_resist_change(0))
                $ nora_mom_study_event_object.inc_level(0)
        "Have them jerk you off together.":
            me "Well, I know something that would help me relax. My brain is feeling pretty fried, and all I can think about now is you two."
            mom "Us?"
            me "Right, you're getting along so well together and I'm stuck here just watching. How about you two help me relax while you chat. Then Nora and I can get back to work."
            $ action_difficulty = 30
            $momO.set_action_exhib()
            $momO.set_action_cumslut()
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            if noraO.check_willing(action_difficulty) and momO.check_willing(action_difficulty):
                "Mom and Nora look at each other."
                nora "It is important he's as focused as possible. We're doing challenging work here."
                mom "Do you think it's necessary?"
                me "I think so, it's not going to go away with either of you here."
                "Nora runs her hand along your thigh."
                nora "Come join us Jennifer, with your help we'll be done with this much faster."
                "You pull up a chair on the other side of you for mom. She sits down, and Nora reaches for your zipper."
                hide mom
                hide nora
                show momNora hand1
                $ momO.inc_hand()
                $ noraO.inc_hand()
                "She slides your pants down past your cock, then holds you by the base of the shaft."
                nora "Here you go."
                "Mom doesn't say anything, but holds onto your shaft and starts rubbing it gently. Nora uses her hand to play with your balls."
                me "That feels great."
                mom "Good. Finish as soon as you can so you can get back to work."
                me "Okay mom, I'll do my best."
                "Mom speeds up her stroking, and you lean back in your chair while you enjoy yourself."
                "A few minutes pass in silence, with mom working your shaft and Nora rubbing your balls."
                nora "It may help if you get your palm wet."
                "Mom nods and pulls her hand off your cock. She runs her tongue along her own palm, spitting at the end to make sure it's nice and wet."
                "When she returns it to your shaft it's warm and slippery. She rubs you quickly, and the room is filled with quiet wet noises."
                me "Oh fuck, that feels great."
                nora "That's good, just let it out [inputName]."
                "A few more strokes and you're feeling ready to finish."
                me "I'm going to cum soon."
                mom "I don't want you to get anything dirty, okay?"
                nora "He might not have that much control over it."
                mom "Well, I'll hold my hands out, you can finish there."
                "You nod and breath heavily as you begin climaxing. Mom pulls her hands off your cock and lets Nora take over. She puts her hands together and cups them at the tip, ready to catch your load."
                "You begin releasing, firing your cum into your mom's waiting hands. Nora keeps stroking you until you're completely finished, then lets go of your cock and wipes her hand against her thigh."
                "Mom looks down at her handfuls of semen."
                mom "Well I think that worked."
                me "Oh ya, I feel much better now."
                mom "I'm going to go take care of this, you two should get back to work."
                nora "Thank you for your help Jennifer."
                mom "Any time. Good luck!"
                hide momNora
                show nora casual at right
                "Mom heads to the kitchen to wash her hands, then goes upstairs to let you concentrate."
                "After another half an hour of work Nora leans back and sighs."
                nora "I think there was a printing error, this doesn't seem possible."
                me "Well, it was the practice that was important anyway, right?"
                nora "Right. Well, thank you for having me over [inputName], let me know if you find any more interesting problems like that."
                "You walk Nora to the door and say goodbye. As she drives off you feel like you've had a [noraO.effect_string] impact on her and a [momO.effect_string] impact on mom today."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ momO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(nora_mom_study_event_object.get_resist_change(3))
                $momO.change_resist(nora_mom_study_event_object.get_resist_change(3))
                $ nora_mom_study_event_object.inc_level(3)
            else:
                if temp_nora <= 30:
                    nora "With your mother? I don't think so [inputName]."
                    mom "Well if he really can't focus..."
                    nora "Then he should go take a cold shower or something. We're in the middle of a project, he can't just drop things when he gets tired."
                    "Mom thinks about this for a while, then nods in agreement."
                    mom "You're right. I should let you two get back to work."
                    "Nora looks more alert, she must have resisted the drug."
                    me "Alright, a bad joke was all it was. Lets get back to work then."
                else:
                    mom "[inputName]! You can't say that when your boss is here."
                    nora "It's alright Jennifer. I'm sure it was just a bad joke."
                    mom "Joke or not, that's not appropriate!"
                    "Mom seems to be shaking off the effects of the drug."
                    me "Your right Nora, just a bad joke. I'm sorry if I offended you."
                    "Mom gives you a stern look, then nods."
                    mom "Good. Now, I'll let you two get back to work."
                "Mom heads up to her room while you and Nora get back to work. After fifteen minutes you give up and Nora leaves. As you wave goodbye you feel like you could have done more with the situation."
                $ noraO.change_slut_failed()
                $ momO.change_slut_failed()
                $noraO.change_resist(nora_mom_study_event_object.get_resist_change(0))
                $momO.change_resist(nora_mom_study_event_object.get_resist_change(0))
                $ nora_mom_study_event_object.inc_level(0)
        "Have them blow you together.":
            me "I know my brain is feeling fried after all that work. I could use some help relaxing."
            nora "You're tired already?"
            me "I don't do this as a job, it's a little bit harder. Plus I've been staring at your tits and ass all day, so I'm horny as hell."
            $ action_difficulty = 45
            $momO.set_action_exhib()
            $momO.set_action_cumslut()
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            if noraO.check_willing(action_difficulty) and momO.check_willing(action_difficulty):
                "Mom and Nora both hesitate and look at each other."
                mom "I suppose we could help him out. A quick handjob would get him back to work fast."
                me "I don't think a handjob would do it. I'm going to need some more... intimate service if we're going to do any work after this."
                nora "I don't have much more time to spend here. If we're going to finish the problem I'll need your son back as soon as possible."
                "You slide your chair back and slip your pants off. Nora drops to her knees and shuffles in front of you."
                "Mom seems to hesitate, then joins her on the ground."
                mom "If you think it's the best way I'll help however I can."
                me "Thanks you two, I'm sure we'll be done very soon."
                hide mom
                hide nora
                show momNora blow1
                "Nora takes your cock into her hand and rubs it slowly."
                nora "You should play with his balls Jennifer. Most men like that."
                "Mom nods and reaches forwards. She cups your balls in her hands and rubs them softly while Nora strokes your shaft."
                "Nora leans forwards and spits on your cock, rubbing it over your cock to get you slipery. Then she leans forward and wraps her lips around your tip, licking around the edges with her tongue."
                show momNora blow2
                $ momO.inc_blow()
                $ noraO.inc_blow()
                "She slides her head down slowly, bobbing up and down as she goes. Before long her nose bumps your waist and she's sliding along your entire length with each stroke of her mouth."
                mom "How does that feel sweetheart?"
                me "It feels great mom, you're both doing great work."
                mom "We'll help take care of you, just sit back and relax."
                "You lean back in your chair and spend a few minutes watching Nora's head bounce up and down while she blows you."
                "Finally she pops off the end and takes a few deep breaths."
                nora "Mind taking a turn Jennifer? I need to catch my breath."
                show momNora blow3
                "She slides to the side and mom moves up. She holds the base of your cock with one hand to keep it steady and leans in to lick the shaft a few times."
                show momNora blow4
                "Nora sits back on her ass and undoes her sweater and shirt. She pulls them open and pulls up her bra so her tits flop out of the bottom."
                nora "This should help."
                "Mom opens her mouth and slides you into her throat. Your cock is dripping wet already and she has no problems taking you all the way to the back of her throat."
                "Nora places a gentle hand on the back of your mom's head and helps guide her up and down. She rubs her own nipple with her other hand."
                "Mom's throat convulses a few times as she takes your cock as deep as she can, and her soft moans push you towards your orgasm quickly."
                menu:
                    "Cum in Mom's mouth.":
                        me "I'm almost there, keep going mom."
                        "Mom tries to pull off of your cock, but Nora holds her gently at the end of your cock, tip still in her mouth."
                        nora "Don't stop now Jennifer, you're almost done."
                        "Mom hesitates, then nods and goes back to blowing your cock."
                        "A few more strokes of her throat and you're ready to finish. You moan and begin firing your load into your mom's mouth."
                        "She moans and tries to say something, but Nora doesn't let her pull off your dick until you're finished cumming. When you're done, mom pulls off and looks at Nora."
                        nora "Great job, you were perfect."
                        "Mom reaches up for the table and grabs her wine glass. She spits your load into it, then places the glass back on the table."
                        mom "Thanks for the encouragement Nora. I'm just happy I could help."
                        me "You both were great, I'm feeling much better now."
                        $ momO.inc_cum_mouth()
                        hide momNora
                        show mom casual at left
                        show nora casual at right
                        "The girls stand up, and Nora gets her shirt back in position again."
                        nora "Good, we can get back to work then."
                        mom "I'm going to go get cleaned up, good luck to you two."

                    "Cum in Nora's mouth.":
                        me "I'm almost there. Nora, can you finish me off?"
                        "Mom pulls off your cock with a wet pop and slides out of the way."
                        nora "Of course, here we go."
                        show momNora blow5
                        $ noraO.inc_cum_mouth()
                        $ noraO.inc_cum_swallow()
                        "She opens her mouth and slides her mouth down your shaft until your tip hits the back of her throat. Mom sits back and watches as Nora blows you."
                        "A few more strokes and you're ready to finish. You moan loudly, then start cumming in Nora's mouth."
                        "She grunts as the first pulse hits her in the throat, then slides your tip onto her tongue and waits until you're finished."
                        "When you're done she opens her mouth and looks up at you so you can see how you've done."
                        mom "Well done Nora. You can use the sink if you want to..."
                        "Nora shakes her head and closes her mouth. There's the quiet sound of her swallowing, then she opens her mouth again and takes a deep breath."
                        nora "No need. I don't want to impose."
                        "Mom laughs and stands up."
                        mom "It wouldn't have been any problem at all!"
                        me "Well, I'm feeling a lot better after that."
                        nora "Excellent, we can get back to work then."
                        hide momNora
                        show mom casual at left
                        show nora casual at right
                        "Nora gets her shirt back in position and sits down in her chair again."
                        mom "Okay then, I'll leave you two to work. Try and stay focused, okay [inputName]?"

                    "Cum on both of their faces.":
                        me "I'm almost ready! I want to cum over both of you!"
                        "Mom slides you down her throat a few more times, then pulls off with a wet pop. She grabs your shaft with her hand and strokes you while she turns to Nora."
                        mom "Nora, are you okay with that?"
                        nora "I'm fine with it, lets finish him off."
                        "Mom strokes you quickly while they squeeze together, getting ready for your load. A few moments more and you moan as you climax."
                        show momNora blow6
                        $ noraO.inc_cum_over()
                        $ momO.inc_cum_over()
                        "Mom holds your cock steady as you spray her with cum, then she moves it and strokes you while you lay a few lines of cum over Nora's face as well. The rest drips onto her tits and dribbles onto mom's hand."
                        "You lean back and sigh while the girls look at each other, covered in cum."
                        nora "Good job, I think we did it."
                        mom "I think we did."
                        me "Thank you, both of you. I'm feeling much better now."
                        mom "Good. The bathroom is this way Nora, we can get cleaned up quickly."
                        hide momNora
                        show nora casual at right
                        "The girls leave the room, and Nora comes back a few moments later without your load on her."
                        nora "Lets get back to work then, shall we?"

                hide mom
                "After another half hour of work Nora slides her chair back and sighs."
                nora "After all that, and it's just a printing error."
                me "Well, it's the practice that's important, right?"
                nora "Right. I hope this at least taught you some techniques."
                me "A bunch, thanks for the help Nora."
                "You walk Nora to the door and say goodbye. As she's driving away you feel like you've made a [noraO.effect_string] impact on her and a [momO.effect_string] impact on mom."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ momO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(nora_mom_study_event_object.get_resist_change(4))
                $momO.change_resist(nora_mom_study_event_object.get_resist_change(4))
                $ nora_mom_study_event_object.inc_level(4)
            else:
                if temp_nora <= 45:
                    nora "[inputName], that doesn't seem like appropriate talk in front of your mother."
                    "Mom nods a little, but still seems distracted."
                    me "What, it was just a suggestion."
                    nora "Well I don't think it's reasonable. You've got to stay focused on our work."
                    mom "She's right. I'm sure you can keep focused for a little longer."
                    "Nora seems aware and alert now, she must have resisted the drug."
                    me "Alright, sorry. Forget I even said anything."
                    mom "I'll let you two get back to work, sorry for distracting you."
                else:
                    mom "Staring at our tits? [inputName], I raised you better than that!"
                    nora "Jennifer, I'm sure it was just a bad joke."
                    mom "Well no son of mine should be making jokes like that."
                    me "Sorry mom, I'm just a little distracted."
                    mom "I'm sure you can hold it together for a little longer. Nora went out of her way to meet with you today, and you're being incredibly rude."
                    "Mom seems aware and alert again, you must have pushed her too far and she's resisted the drug."
                    me "Sorry. Lets get back to work then."
                    "Mom scowls, then nods."
                    mom "Okay, I'll leave you to it. It was a pleasure meeting you Nora."
                    nora "You too Jennifer. Thank you for the drink."
                "Mom heads up to her room while you and Nora get back to work. After fifteen minutes you give up and Nora leaves. As you wave goodbye you feel like you could have done more with the situation."
                $ noraO.change_slut_failed()
                $ momO.change_slut_failed()
                $noraO.change_resist(nora_mom_study_event_object.get_resist_change(0))
                $momO.change_resist(nora_mom_study_event_object.get_resist_change(0))
                $ nora_mom_study_event_object.inc_level(0)

        "Fuck them both on the dining room table.":
            me "I'm starting to think these problems aren't solvable anyway, it's probably just a typo."
            "Nora nods slowly. Mom just watches the two of you."
            me "What I could really use is a pair of hot pussies to take for a ride to blow off some stress. You're both getting along so well, how about we take a few minutes to enjoy ourselves."
            $ action_difficulty = 75
            $momO.set_action_exhib()
            $momO.set_action_cumslut()
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            if noraO.check_willing(action_difficulty) and momO.check_willing(action_difficulty):
                "Mom looks at Nora and shrugs."
                mom "You've both been working really hard. I'm sure you could use a break."
                "Nora thinks about it, then nods."
                nora "You're right, you'll have to help us out though."
                "Mom blushes."
                mom "If you two don't mind."
                me "Not at all mom, I'd appreciate the company."
                show nora strip5 at right
                show mom nightstrip3 at left
                "Nora unbuttons her shirt and pulls it off. Her bra goes next, then she slides down her pants and panties. Mom joins her in stripping down, and soon they're both standing naked in the dining room."
                nora "It's your house Jennifer, you should go first."
                mom "You're the guest though, it's only polite."
                hide nora
                hide mom
                show momNora fuck1
                $ momO.inc_sex()
                $ noraO.inc_sex()
                "Nora shakes her head and pushes your mom over onto the table. She gives her ass a quick slap."
                nora "Don't even think about it."
                "You stand up, pull your shirt off, and drop your pants."
                show momNora fuck2
                "Nora slides her hand down between mom's legs and rubs her pussy, then slides a finger in and out a few times."
                nora "I think she's plenty wet for you already."
                me "Are you ready mom?"
                mom "Whenever you're ready sweetheart."
                show momNora fuck3
                "You step between her legs and line your shaft up with her pussy. Nora holds onto her ass cheeks and spreads them so you have a clear view of her while you slide in."
                "Mom gasps and moans as you enter her, sliding along her wet tunnel easily."
                nora "There you go. That's so hot."
                me "You're next Nora, so get ready."
                show momNora fuck4
                "You fuck mom from behind for a few minutes. She moans softly, holding onto the far side of the table while you thrust into her. Nora gives her ass one last smack, then sits on the edge and rubs her own pussy."
                nora "How does that feel?"
                mom "You feel so good! Don't stop honey!"
                me "Whatever you say!"
                "You grab onto your mom's hips and fuck her faster. Her ass bounces with each hit, and the table creaks and groans under the stress."
                mom "Fuck, I'm going to cum!"
                "Her pussy twitches around your cock and her legs go weak. She leans completely on the table and moans loudly while you pound her."
                nora "Damn that looks good. When is it my turn?"
                show momNora fuck5
                "Nora lies down on the table beside your mom, spreading her legs and presenting her dripping pussy to you."
                me "One moment, I'll be right with you!"
                show momNora fuck6
                "Mom pants and spasms a few more times until her orgasm is finished. She yelps as you pull out and step over in-between Nora's legs. With a smooth motion you slide balls deep into her."
                nora "Oh fuck!"
                me "Damn, you feel great!"
                "Nora wraps her legs around your hips, pulling you deep into her. Her pussy is dripping wet already, and your cock is lubricated with your mom's juices anyway."
                "Her tits bounce as she slides slightly on the table with each thrust, and she reaches behind her to grab the edge of the table to hold herself still."
                "After a few more minutes of fucking her she's moaning loudly and her pussy is twitching around you."
                nora "I'm cumming too! Please don't stop!"
                "You have no intention of stopping, and keep fucking her while her legs convulse and pull at your back."
                nora "Fuck!"
                "Her tightening pussy and bouncing tits drive you to the edge, and your orgasm builds rapidly."
                menu:
                    "Cum inside Nora.":
                        me "Here I cum!"
                        nora "Fuck! Fill me up!"
                        "You grab her hips and fuck Nora as fast as you can. When you're ready you hold yourself tight against her and moan while you fill her up with your cum."
                        "Nora tightens as you finish, letting out a tiny gasp with each new pulse of cum. When you're finished she moans and goes limp, legs dangling off the edge of the table."
                        show momNora fuck7
                        $ noraO.inc_cum_inside()
                        "You pull out, trailing a thin line of cum, and look at the two post orgasm girls on the table."
                        me "Damn, that felt amazing."
                        "Mom nods slowly, still face down on the table with her ass in the air. Nora just moans, cum dripping down her leg."
                        "You collapse down in a chair and catch your breath. Both the girls pant for a while, then drag themselves into chairs as well."

                    "Cum inside Mom.":
                        me "You've had your fill Nora, here I come mom!"
                        "You pull out as suddenly as you had entered Nora, then step over and grab ahold of your mom's ass. She yelps as you sqeeze her ass, then moans loud and long as you slide your cock into her."
                        mom "I thought you were done!"
                        me "Not quite yet, here I cum!"
                        "You fuck her fast and hard for a few strokes, then push yourself as deep as you can as you fire your load into her pussy."
                        "Nora turns her head and watches, panting heavily."
                        show momNora fuck8
                        $ momO.inc_cum_inside()
                        "When you're finished you pull out of your mom, trailing a thin line of cum. She pants and moans a little, but stays limp on the table. A line of cum starts running down her thigh."
                        "You enjoy the view of the two post orgasm girls collapsed on the table and sit down in a chair yourself. After a few minutes of heavy breathing they both get themselves into chairs as well."

                    "Cum on both of them.":
                        me "I'm almost there! Get ready you two!"
                        nora "Let it out! We want your cum!"
                        "You fuck Nora's tight pussy a few more times, then pull out and stroke yourself off until you start cumming."
                        show momNora fuck9
                        $ momO.inc_cum_over()
                        $ noraO.inc_cum_inside()
                        "You fire a line of cum over Nora's tits, then one onto her pussy. You step to the side and finish jerking yourself off onto your mom's ass."
                        "When you're done, you step back and enjoy the view of the two post orgasm girls on the table."
                        me "Fuck that felt great."
                        "You collapse into a chair while they pant heavily, trying to catch their breath. After a few minutes they slide off the table and into chairs beside you."

                me "You know, I don't think we're going to have time to finish that problem Nora."
                nora "I don't think so either. I'm going to have to save my energy just to drive home."
                mom "Well at least you tried. That's worth something."
                "When they're ready the girls get their clothes back on. Mom gives Nora a big hug before she leaves and you watch her drive away together. You feel like you had a [noraO.effect_string] impact on Nora and a [momO.effect_string] impact on Mom."
                $ noraO.change_slut_rebalanced(action_difficulty)
                $ momO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(nora_mom_study_event_object.get_resist_change(5))
                $momO.change_resist(nora_mom_study_event_object.get_resist_change(5))
                $ nora_mom_study_event_object.inc_level(5)

            else:
                if temp_nora < temp_mom:
                    nora "[inputName]! That is no way to talk to your mother or a guest!"
                    "Nora seems instantly alert and aware. She must have fought off the drug."
                    me "Oh I'm sorry Nora. It's an inside joke we have here, I guess it seems kind of vulgur if you don't know."
                    "Nora looks at you and then at your mom. Mom is still dazed, and just nods slowly when attention is turned to her."
                    nora "Well, you should warn me then. Someone else might have taken serious offense to that."
                    me "I'm sorry, it won't happen again."
                    nora "Good. How about we get back to work then. Thank you for the drink Jennifer, it was a pleasure meeting you."
                    mom "And a pleasure meeting you. Good luck."
                else:
                    mom "[inputName]! That's not okay to say, especially to a guest!"
                    "Mom seems instantly alert and aware. She must have fought off the drug."
                    me "Oh I'm sorry, it's kind of an inside joke we have at the lab. I guess it sounds vulgur if you don't know it."
                    "Mom scowls at you, but Nora nods slowly when you look at her."
                    mom "Well I still don't like you using language like that. You should make a better impression in front of your boss."
                    me "Sorry, it won't happen again."
                    nora "It's alright Jennifer. We should be getting back to work anyway. Thank you for the drink."
                    mom "You're welcome. It was a pleasure meeting you Nora."
                "Mom heads up to her room while you and Nora get back to work. After fifteen minutes you give up and Nora leaves. As you wave goodbye you feel like you could have done more with the situation."
                $ noraO.change_slut_failed()
                $ momO.change_slut_failed()
                $noraO.change_resist(nora_mom_study_event_object.get_resist_change(0))
                $momO.change_resist(nora_mom_study_event_object.get_resist_change(0))
                $ nora_mom_study_event_object.inc_level(0)

    jump jumpTimeSkip

label maj_spikeMovieDrinksThreesome:
    $movie_threesome_event_object.happened = True
    call serum_give(sisO) from _call_serum_give_2
    $ temp_sis = _return
    call serum_give(momO) from _call_serum_give_3
    $ temp_mom = _return
    "You pour some serum in each glass and swirl them quickly, then head back to the living room."
    show sis casual1 at left
    show mom casual at right
    sis "There he is!"
    mom "Thank you [inputName]."
    me "No problem mom. Here you go Lily."
    "You distribute the drinks and take a seat between the girls on the couch."
    "Mom picks up the remote and resumes the movie and the three of you relax. Lily and mom both take sips from their wine glasses."
    "You'll have to make sure they drink it all to have the full effect. Maybe the small sips have had some effect already."
    me "You two should drink up, there's plenty of wine if you want more."
    mom "We don't want to drink too much, I've got stuff to do in the morning."
    sis "Oh come on mom, it'll be fine. We barely drink anyways."
    "Lily lifts her drink up and takes a large gulp."
    mom "Lily, you're terrible!"
    "Mom reaches across you and slaps Lily on the leg, then takes her own glass and drinks some more."
    me "You should finish the glass, I can get more if you want."
    "The girls don't say anything, but both of them down their entire glass of wine."
    "They put their glasses down on the coffee table and lean back heavily into the couch. Both of them stare at the TV with blank eyes, not laughing at the jokes."
    me "Can you two both hear me?"
    mom "Of course [inputName]."
    sis "Ya. What's up bro?"
    menu:
        "Have them take off their shirts.":
            $ action_difficulty = 0
            $momO.set_action_exhib()
            $momO.check_willing(action_difficulty)
            $sisO.set_action_exhib()
            $sisO.check_willing(action_difficulty)
            me "You've both had such a long hard week. You really earned a relaxing night in."
            "Your mom and sister listen and nod."
            me "I think we'd all be even more relaxed without our shirts. We're all family here."
            sis "Do you think so?"
            me "Definitely."
            mom "If you two are comfortable with it I'll play along."
            me "Sure. I'll go first."
            "You pull your t-shirt over your head and drop it to the floor."
            me "Your turn Lily."
            sis "Well, my dress kind of is my shirt."
            show sis strip1 at left
            "She stands up and shrugs her dresses straps off and lets it fall to the ground. She isn't wearing a bra underneath."
            sis "So I guess I don't get to wear any of it."
            "She giggles, and sits back down on the couch in just her panties."
            me "Mom?"
            show mom strip9 at right
            $ momO.inc_naked()
            $ sisO.inc_naked()
            "Mom unbuttons her blouse and pulls it off. She folds her shirt carefully and puts it on the coffee table."
            "The three of you sit on the couch for a few minutes, your mom in her beige bra and your sister in just her panties."
            "You aren't sure how much longer the drug will last though, so you take a few last looks and then speak up."
            me "It's getting a little chilly in here. Maybe we should put our shirts on after all."
            sis "I didn't notice, but ya it is."
            mom "Good idea. We don't want to catch a cold playing around the house like this."
            show sis casual1 at left
            show mom casual at right
            "You all put on your clothes again and watch the rest of the movie."
            "As you say goodnight, you feel confident you made a major effect on both of them tonight."
            $ sisO.change_slut_rebalanced(action_difficulty)
            $ momO.change_slut_rebalanced(action_difficulty)
            $sisO.change_resist(movie_threesome_event_object.get_resist_change(1))
            $momO.change_resist(movie_threesome_event_object.get_resist_change(1))
            $ movie_threesome_event_object.inc_level(1)

        "Have them both get naked.":
            me "We've all had such long hard weeks, I think we all need to relax as much as possible."
            "Your mom and sister listen and nod."
            me "I know I'm always more relaxed when I'm naked, so I'm going to take off my clothes. I think you two should join me."
            $ action_difficulty = 15
            $momO.set_action_exhib()
            $sisO.set_action_exhib()
            if sisO.check_willing(action_difficulty) and momO.check_willing(action_difficulty):
                #Do it
                sis "Do you think so?"
                me "Definitely. No tight bras, no fluffy dresses. Way more relaxing."
                "You stand up and pull your shirt off, throwing it on the back of the couch."
                mom "That's an interesting idea honey. I think we should give it a try."
                sis "Jokes on you, I'm already not wearing a bra."
                show mom strip9 at right
                show sis strip1 at left
                "Mom and Lily stand up and start taking off their clothes. Lily drops her dress to the floor while mom folds her shirt up and places it onto the coffee table."
                show mom nightstrip2 at right
                show sis strip2 at left
                "Mom's pants slip off next, then her bra. Lily slides her panties down and gives a little dance in the nude."
                sis "You're right bro, this is relaxing."
                show mom nightstrip3 at right
                $ sisO.inc_naked()
                $ momO.inc_naked()
                "You pull your pants and underwear down. Mom pulls her panties down past her thighs then lets it drop."
                me "What do you think mom? Feeling relaxed?"
                mom "It's a little strange to be doing this with you two, but I suppose it's a good way to get to know each other."
                me "Exactly. Now lets sit down and enjoy the movie."
                "The three of you sit down. You're excited, and your cock stands hard and ready. You see Lily sneaking glances at you from the corner of her eye."
                me "Getting an eyeful Lily?"
                "She blushes and looks away quickly."
                sis "Just taking a look. Sorry."
                me "Don't be sorry, we don't see each other naked very often. Stare away."
                mom "Quiet you two, we're missing the movie."
                "You both stay quiet, but Lily now doesn't hide her staring and looks at your impressive package directly. You flex your cock for her a few times, and see her blush some more."
                "You aren't sure how long the drug will last though, so you have to cut the fun short."
                me "It's getting a little cold in here, isn't it?"
                mom "Is it?"
                me "Ya, I think so. I'm going to get dressed again."
                sis "Me too, it's definitely chilly."
                show mom casual at right
                show sis casual1 at left
                "Mom follows your lead, and a few minutes later you're all dressed."
                "When the movie ends you all say goodnight. You feel like you had a major effect on the two of them tonight."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ momO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(movie_threesome_event_object.get_resist_change(2))
                $momO.change_resist(movie_threesome_event_object.get_resist_change(2))
                $ movie_threesome_event_object.inc_level(2)
            else:
                "You grab the bottom of your t-shirt and pull it over your head."
                if temp_sis < temp_mom:
                    #sis resists first
                    sis "You're going to get naked here? In the living room?"
                    me "Ya. It'll be nice, trust me."
                    sis "Ew, we sit here and eat sometimes! Mom, you can't let him do that."
                    "Mom shakes her head, as if waking up from a nap."
                    mom "What?"
                    sis "[inputName] is taking his clothes off to relax, on the couch."
                    me "Sorry, sorry. If you two don't think I should I'll stop."
                    mom "Maybe that's a good idea. Lets just watch the movie."
                    "Damn, Lily must have resisted the drug, and she's warned mom now."
                    "The three of you watch the rest of the movie, then head to bed. You're sure you could have done more with the situation."
                else:
                    mom "In front of your sister?"
                    me "Ya. We're family, it's nothing we haven't seen by accident."
                    "Mom hesitates, then shakes her head."
                    mom "I don't think so, you should be setting a better example for her."
                    "Lily nods slowly, appearing to be waking up from her stupor slowly."
                    sis "I think we should just finish watching the movie."
                    me "Okay, if you aren't comfortable with it."
                    "You put your shirt back on. Mom must have resisted and has warned Lily now."
                    "After the movie the three of you say goodnight and head to bed. You're sure you could have done more with the situation."
                    #mom resists first
                $ sisO.change_slut_failed()
                $ momO.change_slut_failed()
                $sisO.change_resist(movie_threesome_event_object.get_resist_change(0))
                $momO.change_resist(movie_threesome_event_object.get_resist_change(0))
                $ movie_threesome_event_object.inc_level(0)

        "Have them use their tits and hands to jerk you off.":
            me "We've all had a really busy week I think. It's good that we can all sit back and relax."
            "Lily and mom nod slowly."
            me "I know I've been really horny lately though. It would help me relax if you two could help me get off."
            $ action_difficulty = 30
            $momO.set_action_exhib()
            $momO.set_action_cumslut()
            $sisO.set_action_exhib()
            $sisO.set_action_cumslut()
            if sisO.check_willing(action_difficulty) and momO.check_willing(action_difficulty):
                sis "Is that really the only way you could relax?"
                mom "Well if he's that horny, probably. When a boy gets excited it can be really distracting."
                "You pull your pants down past your waist and free your cock for emphasis."
                me "Mom's right. You two would really be helping me out."
                "Mom stands up and begins unbuttoning her shirt."
                mom "Okay Lily, lets help your brother out with his little problem, then we can finish the movie."
                sis "Okay, what should I do?"
                me "Come a little closer and rub it for me while mom gets ready."
                show sis hand1 at left
                "Lily slides closer on the couch and reaches a hand out, brushing it against your shaft."
                me "That's right. Grab it and give it a rub."
                show mom strip9 at right
                "She does so, while mom drops her shirt on the coffee table and reaches behind herself to undo her bra."
                sis "Like this?"
                me "Just like that. Keep stroking it for me."
                show mom strip10 at right
                "Mom strips off her bra, revealing her large tits. She lets the bra fall to the ground, and joins you on the couch on the other side."
                mom "Here, let me show you Lily."
                "She reaches forward and takes your cock from Lily's hand. Mom begins stroking you quickly and softly."
                hide mom
                hide sis
                show momSis hand1
                "You reach up and pull the top of Lily's dress down past her tits. She blushes but keeps looking at you."
                me "You have really great tits sis. Would you like mom to show you how to use them?"
                show momSis tit1
                "Mom leans over your lap and drapes her breasts across your shaft. She slides them across you a few times before taking them up in her hands and nestling you inside her cleavage."
                mom "You've got to make sure you keep him right in the middle, between both your tits. A little bit of pressure helps, then slide him up and down."
                "She demonstrates, and Lily gets on her knees in front of you to watch."
                mom "Sometimes it's a little dry. Some spit helps keep everything moving."
                "Mom stops for a moment and sits up, then spits between her tits. When she leans over again you're treated to a nice slippery tit fuck."
                sis "I think I get it. Can I try?"
                show momSis tit2 at right
                $ momO.inc_tit()
                $ sisO.inc_tit()
                "Mom nods and stops. She sits up and watches as Lily spits between her own tits and rubs them together, then she sits up on her knees and wraps her tits around your shaft."
                "Slowly at first, she begins to slide herself up and down your length, holding your cock deep in her cleavage with a little pressure from her hands."
                "Seeing your sister rub your cock, while your topless mom watches beside you, is enough to bring you right to the edge."
                me "I'm going to finish soon."
                menu:
                    "Cum on Lily.":
                        mom "Okay, let me take over then."
                        me "I think Lily can handle it, she's doing a great job so far."
                        sis "I don't mind."
                        "Mom nods and sits back, watching as Lily strokes your cock to completion with her tits."
                        "You moan and lean back as you finish. Lily keeps her tits sliding as you cum between them, making them even more slippery."
                        show momSis tit3
                        $ sisO.inc_cum_over()
                        "As you finish your last pulse she lets your cock slide out the bottom and stands up. Your cum drips down her chest and runs into the front of her dress."
                        mom "Good job sweetheart."
                        "Lily smiles proudly."
                        sis "Thanks mom."
                        me "And thank you both. That really helped."
                        mom "Glad we could help. Now, lets finish the movie."
                        "Lily sits back on the couch and you finish the last twenty minutes of the movie. Neither Lily nor mom bother to cover their tits again, and Lily doesn't even bother wiping your cum away."
                    "Cum on mom.":
                        mom "Okay, let me take over then."
                        "Lily strokes you with her breasts a few more times, then lets go and sits on the couch again."
                        "Mom gets on the floor where Lily had been and wraps her tits around your wet cock. Immediately she presses them tight around you and begins sliding them up and down."
                        "A minute later you're ready and begin tensing."
                        mom "There we go, let it out."
                        show momSis tit4
                        $ momO.inc_cum_over()
                        "She holds your tip at the top of her cleavage as you pulse out your load. Your cum pools around your cock, kept in place by the valley her cleavage forms."
                        "Finally she slides her tits up, and your load begins trickling between her breasts."
                        sis "Wow, that looked impressive."
                        me "Thanks. It was you girls who did all the work though."
                        mom "Just glad I could help. Now, how about we finish up the movie and head to bed."
                        "Mom joins you two on the couch, keeping a hand on her stomach to catch the trickles of cum. Neither her nor Lily bother putting their shirts on while you finish the movie."
                "Afterwards you head up to bed, feeling confident you made a [sisO.effect_string] impact on Lily and a [momO.effect_string] impact on mom."

                $ sisO.change_slut_rebalanced(action_difficulty)
                $ momO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(movie_threesome_event_object.get_resist_change(3))
                $momO.change_resist(movie_threesome_event_object.get_resist_change(3))
                $ movie_threesome_event_object.inc_level(3)
            else:
                "The two girls look at each other for a moment."
                if temp_sis < temp_mom:
                    sis "Get you off... you mean give you a handjob?"
                    me "That would be one way, ya."
                    sis "I would have to touch you... in front of mom?"
                    mom "Well..."
                    sis "I don't think I could do that. It would be too weird."
                    me "There's nothing strange about it. We're just family helping each other out, right?"
                    mom "I think your sister is right, that would be going too far [inputName]."
                    "Damn, Lily must have resisted and warned off mom. Nothing to do now but damage control."
                    #sis resists first
                else:
                    #mom resists first
                    mom "You want a handjob?"
                    me "If that's what you're comfortable with, sure."
                    sis "Both of us?"
                    mom "With your little sister here? I don't think so."
                    sis "Ya, that doesn't seem right."
                    "Damn, mom must have resisted and warned off Lily. Nothing to do now but damage control."
                me "Ah, I'm sorry. You're right I guess. Forget I brought it up."
                "The three of you return to watching the movie. Afterwards you say goodnight and head to bed, knowing you could have had more of an effect on them tonight."
                $ sisO.change_slut_failed()
                $ momO.change_slut_failed()
                $sisO.change_resist(movie_threesome_event_object.get_resist_change(0))
                $momO.change_resist(movie_threesome_event_object.get_resist_change(0))
                $ movie_threesome_event_object.inc_level(0)

        "Have them blow you.":
            me "I've had a really busy week, and it's nice to have you two here to help me de-stress."
            "Lily and mom nod slowly."
            me "It would help me even more though if you could use your mouths to help me relax."
            $ action_difficulty = 45
            $momO.set_action_exhib()
            $momO.set_action_cumslut()
            $sisO.set_action_exhib()
            $sisO.set_action_cumslut()
            if sisO.check_willing(action_difficulty) and momO.check_willing(action_difficulty):
                #Do it
                mom "You have been working hard all week..."
                sis "He has been really busy. I think we should help."
                "Lily slides down to the floor on her knees. You spread your legs and undo the zipper on your pants for her."
                mom "Okay, we'll help you take care of this, then we can get back to watching the movie."
                me "Sounds great. Thanks you two."
                "Lily nods and reaches for your pants, sliding them down to the floor. Your cock pops out of your underwear, hard and ready for the girls."
                "Mom reaches over to your lap and starts stroking your cock. Lily leans forward and kisses the base of your shaft."
                hide mom
                hide sis
                show momSis blow1
                "Mom stops her stroking so Lily can lick up the bottom of your cock, circling her tongue around your tip to get it nice and wet."
                sis "That should feel better."
                "Lily leans back to let mom start stroking again, and you shiver slightly as her wet hand slides up and down your cock."
                mom "Does that feel good?"
                me "Yes, it feels great."
                show momSis blow2
                "She strokes you quickly for a few seconds, then leans over and wraps her mouth around your tip. She brushes her hair out of the way and begins sliding you into her throat."
                "As mom reaches the bottom she shakes her head left and right slightly, clenching down on your cock with her throat. Finally she pulls back and begins blowing you at a slow regular pace."
                "Lily watches fron the ground on her knees, eyes following mom's mouth up and down. As she watches she pulls the straps of her dress over her shoulders and pulls it below her tits. She kneads a breast slowly."
                sis "Can I give it a try?"
                "Mom pulls off your cock."
                mom "Sorry, of course sweetheart."
                "She sits up and straightens her hair. While Lily slides forward between your legs mom unbuttons her shirt and begins pulling it off."
                mom "Here you go, you can play with my tits [inputName]."
                show momSis blow3
                $ sisO.inc_blow()
                $ momO.inc_blow()
                "Lily holds your shaft lightly in one hand and brings her face close. She licks you quickly, then places her mouth over the tip and starts sucking on it."
                "Mom lifts her breasts up with both hands, offering them to you."
                "You take a nipple in your mouth and suck lightly, grabbing the other tit with a hand."
                "Lily slides your shaft deeper into her warm mouth, licking with her tongue."
                me "That's good sis. See if you can go as deep as mom."
                "She nods and starts going deeper with every stroke over her mouth. As she reaches the bottom you can hear wet gagging sounds as your tip hits the back of her throat."
                mom "You're doing great Lily. Keep it up."
                me "She really is a great slut mom, she knows exactly what to do."
                mom "[inputName]! You shouldn't say that about your sister."
                "Lily coughs with your cock in her throat, then pushes herself deeper onto it."
                me "It's a compliment, she's really good at this. It's making me feel great."
                "Mom gives you a look, then nods."
                mom "I suppose she is trying really hard."
                "You reach down and hold Lily's head from either side, then pump your waist up and down to slide your cock in and out of her throat."
                "Spit runs down her mouth, dripping off her chin. Her mouth makes satisfing wet slapping sounds, but she holds her mouth as wide open as possible for you. She twists her own nipples between her fingers."
                mom "It looks like she might need some help down there."
                "You relax your thrusts and let Lily take over again while mom gets on her knees and joins her on the ground."
                "Lily pulls your cock out of her mouth, dripping spit down onto her tits. She pants loudly as she moves out of the way for mom."
                sis "Thanks mom."
                show momSis blow4
                "Mom returns your cock to her mouth, sliding you up and down quickly."
                "You feel your orgasm building up inside you while the girls stare at your cock on their knees."
                menu:
                    "Cum on both of them.":
                        me "I'm about to finish! Get together!"
                        "Mom throats you deep one last time, then pulls off with a wet sigh and slides back. She throws an arm around Lily and pulls her close, pressing the side of their tits together."
                        sis "We're ready [inputName]!"
                        mom "Give it to us!"
                        show momSis blow5
                        $ sisO.inc_cum_over()
                        $ momO.inc_cum_over()
                        "You sit forward on the couch and stroke your wet cock quickly. You tense and begin releasing your load, shooting thick streams of cum over first mom, then Lily."
                        "The girls stay still and wait while you finish, and you rub the last few drops of cum onto Lily's nipple. Finally you sigh and sit back, looking at your cum covered mother and sister."
                        mom "There we go. Feeling better?"
                        me "Much better. Thank you two."
                        sis "No problem. It was fun."
                        "Lily and mom look at each other and help wipe the strings of cum out from around their eyes."
                        mom "Now, we should finish that movie."
                    "Cum in mom's mouth.":
                        me "I'm about to finish. Keep going mom, I want you to take my load."
                        "Mom nods slightly while blowing you and speeds up her pace."
                        "She takes you deep in her throat, tongue licking quickly. Before long you tense up and begin to release."
                        "Mom slides your tip into her mouth and places it on her tongue. She grabs your wet cock with her hand and strokes you off as you spasm and shoot your load into her mouth."
                        "After a few pulses you're finished, and she pulls you out of her mouth slowly."
                        show momSis blow6
                        $ momO.inc_cum_mouth()
                        "She opens her mouth to show you, then reaches for her wine glass and spits it out inside. She places the glass on the coffee table and smiles at you."
                        mom "Good job sweetheart. You let out a lot. Feeling better?"
                        me "Much better, thank you."
                        if temp_sis > 80:
                            "While mom is talking Lily grabs the wine glass and tilts it back, drinking up the cum your mom had spit out."
                            mom "Lily, what are you doing?"
                            $ sisO.inc_cum_swallow()
                            "Lily swallows your load and turns back to you two."
                            sis "What? We can't go wasting that."
                            "Mom thinks for a moment, then shrugs."
                            mom "If that's what you think dear."
                        mom "Now how about we finish the movie and get to bed."
                    "Cum in Lily's mouth.":
                        me "I'm about to finish. Take over Lily, I want you to take my load."
                        "Mom pulls off your cock with a wet sigh."
                        mom "Can you handle that honey?"
                        show momSis blow7
                        $ sisO.inc_cum_mouth()
                        $ sisO.inc_cum_swallow()
                        "Lily nods and grabs the base of your shaft. She slips your tip into her mouth and begins blowing you quickly."
                        "A few deep strokes of her throat you feel yourself tense up and begin to release."
                        "Lily keeps blowing you until the first pulse hits. She pulls your tip back into her mouth and lets the rest of your spasms shoot your load into her mouth."
                        "When you're finished she slides off slowly, careful not to let anything slip out."
                        mom "Good job sweetheart. Now you can go to the bathroom and spit it out if you want."
                        "Lily shakes her head and swallows loudly. She smiles at both of you after."
                        sis "No need. I took care of it."
                        me "Well done sis, that was great."
                        sis "Mom helped too. Now lets finish the movie."

                "They rejoin you on the couch, both still topless, and you watch the last few minutes of the film. When you head to bed you're satisfied you had a major effect on both of them."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ momO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(movie_threesome_event_object.get_resist_change(4))
                $momO.change_resist(movie_threesome_event_object.get_resist_change(4))
                $ movie_threesome_event_object.inc_level(4)
            else:
                if temp_sis < temp_mom:
                    #sis resists first
                    sis "You want us to kiss you?"
                    me "Not exactly, no."
                    mom "Do you mean a blowjob?"
                    "You nod. Mom's hand rests on your thigh and starts rubbing it."
                    sis "A blowjob? Here!"
                    me "What's wrong? We're all family, just helping each other out."
                    sis "Ew, no. Not here with mom. Not at all!"
                    "Mom moves her hand back."
                    mom "Your sister is right. That's not appropriate talk young man."
                    "Damn, Lily must have resisted the drug and has warned mom. Nothing to do now but damage control."
                    me "You're right. I'm sorry you two."
                    mom "Apology accepted. Lets watch the rest of the movie and get to bed."
                    "You finish the movie, then head up to bed. You can't help thinking that you could have done more to take advantage of the situation tonight."

                else:
                    #mom resists first
                    mom "You want us to give you a blowjob?"
                    sis "I thought he just meant kisses."
                    me "No, mom is right. A blowjob would be perfect."
                    mom "Perfect isn't the word I'd use. We're having a very nice time watching the movie right now."
                    me "It's no big deal, we can pause the movie."
                    mom "That still doesn't make it alright in front of your sister."
                    sis "Ya, that sounds a little weird."
                    "Damn, Mom must have resisted the drug."
                    me "Sorry, you're right. Lets just finish the movie then."
                    "The three of you watch the rest of the movie. You head to bed after, and feel that you could have done something more to take advantage of the situation."
                $ sisO.change_slut_failed()
                $ momO.change_slut_failed()
                $sisO.change_resist(movie_threesome_event_object.get_resist_change(0))
                $momO.change_resist(movie_threesome_event_object.get_resist_change(0))
                $ movie_threesome_event_object.inc_level(0)

        "Fuck them both.":
            me "It's been a busy week for all of us, and if you're like me you've been horny for most of it. We've got some time together to just relax. How about we pause the movie and take advantage of it."
            $ action_difficulty = 75
            $momO.set_action_exhib()
            $momO.set_action_cumslut()
            $sisO.set_action_exhib()
            $sisO.set_action_cumslut()
            if sisO.check_willing(action_difficulty) and momO.check_willing(action_difficulty):
                #Do it
                "Lily grabs the remote and pauses the movie right away."
                mom "Well, it would be a good way to relax."
                sis "Come on mom, it'll be fun."
                show sis strip1 at left
                "Lily stands up and slides the straps of her dress off. Mom hesitates for a moment, then shrugs and stands up as well."
                show sis strip2 at left
                "Lily slides her pink panties down next, and mom begins unbuttoning her shirt."
                me "How about you get me warmed up while mom strips down sis?"
                "She nods and kneels between your legs while you unzip your pants and slide your cock out."
                show sis blow4 at left
                show mom strip10 at right
                "As mom undoes her bra and places it on the back of the couch she puts your tip into her mouth and starts gently sucking on it."
                mom "Don't get too carried away you two."
                "Lily licks the shaft a few time to get it wet, then slides the whole length into her mouth. Mom slides her pants down and begins folding them up."
                show mom nightstrip2 at right
                "While mom gets her panties off Lily blows you quickly, making wet gagging sounds quietly as you hit the back of her throat."
                hide mom
                hide sis
                show momSis fuck1
                "Mom kneels down and watches Lily blow you for a while, then reaches around and rubs her breasts."
                "Lily pulls off your cock with a wet pop."
                sis "There we go, all wet and ready."
                mom "Me too."
                "Mom stands up and turns around, spreading her lips with one hand and leaning back towards your cock."
                show momSis fuck2
                "You hold onto your shaft and guide it towards her pussy as she eases herself down onto the tip. Lily sits back and puts a hand between her own legs, rubbing herself gently."
                "Mom gently lowers herself until your entire length is inside her. She sighs loudly and pauses at the bottom for a moment."
                "Then she begins raising and lowering herself, making sure to stroke every inch of your cock with her body."
                "Lily sighs and sits back, legs spread, and rubs her clit quickly while watching the two of you."
                sis "That looks great mom."
                "Mom sighs and nods, speeding up her movement."
                mom "I'll make sure not to finish him off so you can have a turn."
                "Lily nods and slips two fingers into herself while she waits."
                "Eventually mom gives one last deep stroke and stands up, your cock popping out with a wet squelch."
                mom "Okay, your turn."
                "She sits down beside you and begins fingering herself while Lily stands up and gets on top of you."
                "Lily kneels on the couch, legs on either side of yours, and looks at you while you line up your shaft with her slit."
                me "Okay, ready."
                show momSis fuck3
                $ sisO.inc_sex()
                $ momO.inc_sex()
                "She nods and lowers herself down. She doesn't waste any time and begins riding you as quickly as she can. Her pony tail bounces around on her shoulders and her tits shake up and down."
                mom "That's a good girl, make sure to get it all."
                "Lily does, and moans loudly as she goes. A few minutes later you can feel her legs start to quiver, only partly from exertion."
                sis "Oh fuck. I think you're going to make me cum."
                "You're starting to get close to your own orgasm too."
                menu:
                    "Cum inside Lily.":
                        me "I'm getting close too."
                        mom "Keep going Lily!"
                        "She slides up and down as quickly as she can, panting loudly and moaning. Mom rubs her own clit quickly with one hand, watching her daughter get fucked."
                        "Lily quivers and gasps, throwing herself onto your cock as hard as she can. Her thighs clench around your legs and she holds onto your shoulders as she shudders."
                        "Mom reaches over and grabs her by the hips, pulling her up and pushing her down."
                        sis "Ah! Mom!"
                        "Lily screams in pleasure as she's guided up and down your cock. She shakes and spasms as she's forced to keep riding you while she orgasms."
                        mom "Trust me sweetie, keep going!"
                        sis "Ah! Ah! Ahhhhh!"
                        "Your orgasm builds up to the limit and you tense in preparation for your release."
                        "Finally she can take no more. She leans forward and wraps her arms around your neck and collapses completely. Her weight pushes her completely down onto your cock."
                        "You can feel her pussy tense and untense as she is wracked by her orgasm, and you begin unloading yourself inside of her."
                        show momSis fuck4
                        $ sisO.inc_cum_inside()
                        "You hold her down on you for a little while while you finish, then you both sit and pant loudly."
                        "Mom gives her a kiss on the cheek."
                        mom "Good girl, good girl."
                        "Lily gets up slowly, dripping cum from her pussy as she does. She flops onto the couch beside you."
                        "Mom rubs her clit until she spasms from her own orgasm, and the three of you rest together until you're able to get up and go to bed."
                    "Cum inside mom.":
                        me "I'm getting close, it's your turn mom!"
                        "Lily bounces up and down on your cock a few more times and you feel her legs start to flutter from her orgasm. She collapses beside you and begins fingering herself, gasping loudly."
                        mom "Okay, take me!"
                        "Mom bends over the couch and waits for you to get set up behind her. You waste no time and thrust into her while Lily moans and gasps beside you both."
                        "Within a few strokes you're ready to finish and you pull mom's ass tight against your waist. You spasm a few times, unloading deep inside her, and feel her pussy tighten in response."
                        mom "Yes, there it is!"
                        "She shakes and moans, and reaches her own orgasm."
                        show momSis fuck5
                        $ momO.inc_cum_inside()
                        "You give your mom a few more strokes while she finishes, then pull your wet cock out and watch as a little bit of cum trickles down her thigh."
                        "Lily screams loudly and collapses completely, and you two join her on the couch. You sit still for a long while catching your breath."
                    "Cum in their mouths.":
                        me "I'm almost there, I want to cum in your mouths!"
                        sis "Ahh! Okay!"
                        mom "I'm ready!"
                        "You pump a few more times and feel Lily start to shake from her own orgasm. You tense up and get ready to release, and smack her ass up to get her moving."
                        "Lily slumps to the floor at your feet and throws her mouth over your tip as you pulse out a heavy load of cum."
                        "She moans and fingers herself while you release into her."
                        show momSis fuck6
                        "After a while she sits back and opens her mouth, showing you her mouthful of hard earned cum."
                        show momSis fuck7
                        "Mom joins her on the floor leans over her. She pulls Lily into a deep kiss."
                        show momSis fuck8
                        $ sisO.inc_cum_mouth()
                        $ momO.inc_cum_mouth()
                        $ sisO.inc_cum_swallow()
                        $ momO.inc_cum_swallow()
                        "They make out for a long moment, then mom looks up and opens her mouth to show it full of cum as well now."
                        "Both of them swallow and display their empty mouths to you after."
                        mom "There we go, all taken care of."
                        "Lily just pants, shaking from exertion."
                        "The two get up and join you on the couch, recovering from the night's activities."
                    "Cum on both of them.":
                        me "I'm almost there. I want to finish on top of both of you."
                        "Lily moans and nods her head quickly. Mom drops onto the floor and plays with her tits."
                        mom "Okay, I'm ready."
                        "Lily bounces up and down a few times until she reaches her own orgasm. Her tightening pussy sets off your own, and you lift her up quickly."
                        "She slumps to the ground and mom pulls her close, holding her tits up to present them to you."
                        show momSis fuck9
                        $ sisO.inc_cum_over()
                        $ momO.inc_cum_over()
                        "You stroke yourself to completion, letting your load out first onto mom's face, then Lily's face and tits."
                        me "There we go, take it all!"
                        mom "Let it out sweetheart!"
                        "After you finish you sit back on the couch and look at your mom and sister covered in your load. Lily is still panting, body limp from cumming."
                        "Eventually she and mom join you on the couch, and you spend a few minutes catching your breath."

                "Later that night you head to your room, confident you had a huge effect on both of them tonight."
                $ sisO.change_slut_rebalanced(action_difficulty)
                $ momO.change_slut_rebalanced(action_difficulty)
                $sisO.change_resist(movie_threesome_event_object.get_resist_change(5))
                $momO.change_resist(movie_threesome_event_object.get_resist_change(5))
                $ movie_threesome_event_object.inc_level(5)
            else:
                if temp_sis < temp_mom:
                    #sis resists first
                    sis "What did you have in mind?"
                    me "Well, I was thinking that you and mom could lean over the couch, and I take you from behind."
                    sis "Me and mom together? Here in the living room. That doesn't sound okay. Are you okay with this mom?"
                    mom "Hmm? Oh, I guess you're right. That doesn't sound okay."
                    me "It'll be fine. A great way to blow off stress in fact."
                    sis "I don't think so. I just want to watch the movie."
                    mom "Don't bother your sister [inputName]. Lets just watch the movie."
                    "Lily must have resisted the drug. No use pushing it now."
                    me "Alright, never mind. Forget I brought it up."
                    "The three of you finish the movie and head up to bed. You feel like you could have done more to take advantage of the situation."
                else:
                    #mom resists first
                    sis "Right here in the living room? That sounds really naughty."
                    me "And you're a naughty girl, right Lily?"
                    mom "[inputName]! Don't talk about your sister like that."
                    me "I was just saying, if she's into it she's a dirty girl."
                    mom "And I'm saying to stop it. This is the family living room, I'm not allowing it."
                    me "But it's just a way of relaxing, it'll be good for all of us."
                    mom "I said no and that's final. Now lets just watch the rest of the movie."
                    "Mom must have resisted the drug. No point pushing it now."
                    me "Alright, forget I said anything. A bad joke was all it was."
                    "The three of you watch the rest of the movie and head to bed. You feel like you could have done more to take advantage of the situation."
                $ sisO.change_slut_failed()
                $ momO.change_slut_failed()
                $sisO.change_resist(movie_threesome_event_object.get_resist_change(0))
                $momO.change_resist(movie_threesome_event_object.get_resist_change(0))
                $ movie_threesome_event_object.inc_level(0)
    jump jumpTimeSkip

label maj_labThreesome:
    $lab_threesome_event_object.happened = True
    call serum_give(noraO) from _call_serum_give
    $ temp_nora = _return
    call serum_give(stephO) from _call_serum_give_1
    $ temp_steph = _return
    "You mix the serums in thoroughly, then head back to the girls."
    show steph work at right
    show nora work at left
    me "And I'm back. Here are our drinks ladies."
    "You place the smoothies on the table and grab a seat."
    nora "Perfect, thanks [inputName]!"
    steph "Great. Here's to you!"
    "Nora holds her drink up in a toast. You bump the plastic cups together, then start drinking."
    steph "So [inputName], what are your plans after work today? Got anything special going on?"
    me "Oh, I've got a few things planned. Nothing set in stone yet."
    "Stephanie nods and takes a few more sips. Both the girls look a little zoned out suddenly."
    me "You should both finish your smoothies. You don't want that to go to waste."
    "They both nod and pick up their drinks, sucking back gulps until they're finished."
    "You'll have to be careful, if either one of them resists the drug it's likely they'll warn the other."
    me "Are you both feeling nice and relaxed?"
    steph "Mmhm."
    nora "Yes. Very relaxed actually."
    menu:
        "Have them make out with each other.":
            $ action_difficulty = 0
            $noraO.check_willing(action_difficulty)
            $stephO.check_willing(action_difficulty)
            me "Have you two worked with each other very long here?"
            "The girls look at each other with unfocused eyes."
            nora "Yes. I hired Stephanie a few years ago."
            steph "I'm a perpetual graduate student I guess."
            me "And have you ever done anything with each other? You must spend a lot of time down here in the lab alone."
            nora "Done anything?"
            steph "He means like making out."
            nora "Oh. No we haven't."
            me "You should give it a try. Just for fun. I'm sure you'd both enjoy it."
            hide nora
            hide steph
            "Nora looks uncertain, but Stephanie leans over the table and grabs her head. She pulls Nora into a long french kiss."
            show noraSteph kiss1
            "Nora looks shocked for a moment, then relaxes and leans into the kiss as well. The two girls slide their chairs together and wrap their arms around each other."
            "After a few moments Stephanie breaks the kiss for a moment."
            hide noraSteph
            show nora work at left
            show steph work at right
            steph "You're right, I do enjoy it."
            "Nora is blushing, but Stephanie pulls her back into a kiss. Her hand runs over Nora's shoulder and ends up on a breast, rubbing it lightly through her sweater."
            "Nora moans softly and returns the kiss."
            "You watch the two make out for minutes, but eventually become worried that the drug will wear off too soon."
            me "Okay you too, break it up."
            "They separate, panting slightly. A silver line of spit trails between them, then breaks and drops to their shirts."
            nora "Wow. I was not expecting all that."
            "Stephanie nods and giggles."
            me "It's getting to the end of the day anyway. I think I'm going to head out."
            "The two nod, but stay sitting with each other. They've started chatting about other things by the time you've gathered your belongings and headed out."
            "You're satisfied you had some sort of lasting effect on the two of them."
            $noraO.change_slut_rebalanced(action_difficulty)
            $stephO.change_slut_rebalanced(action_difficulty)
            $noraO.change_resist(lab_threesome_event_object.get_resist_change(1))
            $stephO.change_resist(lab_threesome_event_object.get_resist_change(1))
            $lab_threesome_event_object.inc_level(1)

        "Have them strip each other down.":
            me "You've both worked together for a while, right?"
            "The girls nod and look at each other."
            me "Have you ever seen each other naked?"
            "Stephanie nods, Nora looks at her surprised."
            steph "You were getting changed in here one day for a meeting. You didn't hear me come in, and when I saw you I left right away."
            nora "Well then! It seems I'm at a disadvantage here! I've never seen you naked!"
            me "You could fix that right now."
            $ action_difficulty = 15
            $noraO.set_action_exhib()
            $stephO.set_action_exhib()
            if stephO.check_willing(action_difficulty) and noraO.check_willing(action_difficulty):
                nora "It only seems fair that if you got to see me naked, I get to see you naked Stephanie."
                "Stephanie sighs dramatically."
                steph "Fine, fine. The punishment I get for not changing in a public place."
                "She stands up from her chair and starts pulling off her sweater."
                "Before long she's kicked off her pants too, and is standing in a matching set of pink underwear."
                show steph strip1 at right
                me "Keep going, she said naked."
                "Steph turns around and undoes her bra, laying it carefully on her chair. Finally she slides her panties down to her ankles and turns back around."
                steph "There, completely naked for you. To be fair, this is more than I saw of you."
                show steph strip2 at right
                nora "What?"
                steph "You had already put your pants on, I just saw your tits."
                me "Well that doesn't seem fair that Stephanie had to get naked for you and she only saw your tits. You should join her to balance it out Nora."
                "Nora hesitates, then stands up and pulls off her labcoat as well."
                show nora strip1 at left
                nora "Fine, this way there's nothing unusual about it all."
                "Her pants go next, and then she undoes her bra and lets it fall to the ground. Her tits are larger than Stephanie's, but both are perky with hard nipples."
                show nora strip6 at left
                steph "Come on girl, panties too."
                "She spanks Nora on the ass, who yells and hops away."
                nora "I'm getting there! Give a woman some time!"
                "Nora slides her underwear down and steps out of it, standing naked side by side with Stephanie."
                show nora strip5 at left
                $ stephO.inc_naked()
                $ noraO.inc_naked()
                me "There we go, perfectly fair."
                "Stephanie looks at Nora, sliding her eyes up and down her body."
                steph "You look even better than I remember. I guess I didn't get a good enough look."
                "Nora blushes."
                nora "Stop that, I can't hold a candle to you. I wish I had breasts that perky."
                steph "What do you think [inputName]? Who looks better?"
                "Stephanie turns and bends over a little to show off her butt. Nora moves to do the same, holding her tits in her hands."
                hide nora
                hide steph
                show noraSteph strip1
                menu:
                    "Choose Stephanie.":
                        me "Stephanie wins by a little bit. Nora, you're a very close second but your ass just isn't as great."
                        "Stephanie smiles and crosses her arms while Nora pouts."

                    "Choose Nora.":
                        me "Nora, you win by a hair. Stephanie just doesn't have the tits to keep up."
                        "Nora smiles while Stephanie pouts."

                hide noraSteph
                show nora strip5 at left
                show steph strip2 at right
                me "It's getting late, you two should get your clothes back on so we can get out of here. Unless you want to head outside naked with each other."
                "Stephanie looks at Nora, but she shakes her head."
                nora "Oh no, I'm not letting you talk me into that."
                steph "Fine, lets just get dressed then."
                "After a few minutes the girls are back in their clothes and you all head out from the lab."
                "You're confident you had a major effect on both girls with their show."
                $noraO.change_slut_rebalanced(action_difficulty)
                $stephO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(lab_threesome_event_object.get_resist_change(2))
                $stephO.change_resist(lab_threesome_event_object.get_resist_change(2))
                $lab_threesome_event_object.inc_level(2)
            else:
                if temp_nora <=15:
                    "Stephanie nods and stands up."
                    nora "You don't have to do that Stephanie, it was an accident anyway."
                    steph "Are you sure?"
                    nora "Of course! We can't just go stripping in the lab whenever we want now."
                    me "Well, Nora did."
                    "Nora shoots you a sharp look. She must have resisted the drug."
                    me "Nevermind, forget I said anything."
                elif temp_steph <=15:
                    nora "Well, it does only seem fair if you saw me naked."
                    steph "Barely naked. Tits only."
                    nora "Oh?"
                    steph "Ya, you had already gotten mostly dressed. I don't think it counts honestly."
                    "The girls look at each other for a moment, then nod in agreement."
                    nora "You're right. No big deal."
                    "Stephanie must have resisted the drug."
                "Having lost the moment, the three of you chat a little more then head out. As you head in different directions you're certain you didn't have much of an effect on either of them."
                $noraO.change_slut_failed()
                $stephO.change_slut_failed()
                $noraO.change_resist(lab_threesome_event_object.get_resist_change(0))
                $stephO.change_resist(lab_threesome_event_object.get_resist_change(0))
                $lab_threesome_event_object.inc_level(0)


        "Have them tit fuck you together.":
            me "Have you two ever compared your tits to each other?"
            "Both girls look at each other's chest."
            steph "No contest there, Nora's got me beat."
            nora "You're perkier than I am. Lots of guys like that."
            me "I'm sure they both feel great. How about you use me as a test subject and see who has the better tits for fucking."
            $ action_difficulty = 30
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            if stephO.check_willing(action_difficulty) and noraO.check_willing(action_difficulty):
                steph "I think I've got an edge for that. Perkier tits means better control."
                "Stephanie stands up from her chair and pulls her shirt over her head."
                nora "You think so? Larger and softer just sounds better to me."
                "Nora does the same. Soon they've both thrown off their shirts and bras and are comparing tit size."
                "You slide your chair back from the table to give them room, then pull your pants down to reveal your cock."
                me "Alright girls, lets settle this once and for all then, shall we?"
                "Stephanie kneels down in front of you first, then Nora on the other side."
                nora "So who should go first?"
                me "I think you should do it at the same time, one on each side. That way I have a direct comparison."
                "The girls look at each other and nod, then take their tits up in their hands and press them against each other around your shaft."
                hide nora
                hide steph
                show noraSteph tit1
                $ stephO.inc_tit()
                $ noraO.inc_tit()
                steph "There we go, lets see who's better at this then."
                "Stephanie begins sliding her breasts up and down, and Nora matches her speed so they stay pressed together."
                "Their four tits squeeze your cock from all sides as they move."
                nora "Initial results?"
                me "Too close to call. You both feel great."
                "For a few minutes the girls are silent as they service your cock."
                steph "You know what he needs?"
                "She leans her head forward and spits loudly onto your cock and between the tits."
                steph "Some lube to get things moving faster."
                "Nora leans forward and spits as well, and before long your cock is gliding between two well lubricated pairs of tits."
                "The spit also works it's way between the girls breasts, and occasionally one slips above or below the other. Both of them have rock hard nipples, and are panting from exertion."
                "The slippery tits are doing a great job of getting you close, and you feel your orgasm building."
                menu:
                    "Declare Stephanie the winner.":
                        me "I'm getting close. I think Stephanie's tits were the best today. Sorry Nora, but the prize is hers."
                        steph "Haha! I knew it!"
                        "Nora pouts and sits back on her ass while Stephanie moves over to take sole possession of your cock."
                        "A few more quick strokes of her tits and you begin tensing up."
                        "You begin releasing your load as Stephanie moves her tits up and down."
                        steph "There we go, let it out."
                        "After a few seconds you've finished and she slides her tits off of you. Your thick load is draped over her breasts and erect nipples."
                        $ stephO.inc_cum_over()
                        hide noraSteph
                        show steph tit1 at right
                        "Stephanie runs a finger through the thickest part, then looks at Nora and licks it."
                        steph "That's what victory tastes like."
                        "Nora scoffs, but looks jealous as Stephanie begins wiping herself off."
                    "Declare Nora the winner.":
                        me "I'm getting close. Nora, your tits are the ones that are responsible. I want to cum on your tits."
                        steph "What? Ridiculous!"
                        nora "Sorry girl, but you heard the man."
                        "Nora shuffles over and pushes Stephanie out of the way. She wraps her tits around your cock and claims sole possession of it."
                        nora "Time to give me my prize."
                        "She slides you between her tits quickly, and you begin cumming."
                        "Your cum lands on her neck and tops of her tits, then runs down towards her hard nipples."
                        hide noraSteph
                        show nora tit1 at left
                        $ noraO.inc_cum_over()
                        "Nora sighs as it lands, and runs her fingers through it slowly when you're done."
                        steph "Well, you only won because I was there to help."
                        nora "Of course, of course."
                    "Call it a tie.":
                        me "Yep, it's too close to call. I'm just going to have to call it a tie and cum on both of your tits."
                        "The girls lock eyes over your shaft while they rub."
                        steph "Can he do that?"
                        nora "Nothing in the rules says he can't."
                        "As they talk you start to orgasm."
                        "Your cum shoots straight up, then falls back down between their tits."
                        show noraSteph tit2
                        $ noraO.inc_cum_over()
                        $ stephO.inc_cum_over()
                        me "Don't stop moving yet."
                        "They keep sliding along your shaft, rubbing their cum covered breasts against each other. Finally you're completely finished, and they let you go."
                        me "Well, I guess we didn't exactly learn a lot."
                        nora "We'll have to repeat the experiment some day and see if we get different results."
                        steph "Of course we will, I'd obviously win."
                "The three of you get your clothes back on and head your separate ways. You're satisfied you made a [noraO.effect_string] impact on Nora and a [stephO.effect_string] impact on Steph with todays performance."
                $noraO.change_slut_rebalanced(action_difficulty)
                $stephO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(lab_threesome_event_object.get_resist_change(3))
                $stephO.change_resist(lab_threesome_event_object.get_resist_change(3))
                $lab_threesome_event_object.inc_level(3)
            else:
                if temp_nora <=30:
                    steph "Well, there's where I might have an edge."
                    nora "In the lab? I don't think so you two."
                    me "Are you sure Nora? You're not curious what Stephanie's breasts feel like pressed up against yours?"
                    "Nora looks at you sharply."
                    nora "No, and that's the last of it. Drop it you two."
                    "She must have resisted the drug. Maybe you pushed her too far."
                    nora "Alright, we should be getting out of here before things go too far."
                    "You all leave the lab and head your separate ways. You definitely could have done better than that."
                elif temp_steph <=30:
                    nora "Here in the lab? Sounds naughty."
                    steph "Really Nora? I didn't think that was your kind of thing."
                    "Nora shrugs."
                    nora "Normally it isn't, but it sounds like fun. You're right though, it's a little out of character."
                    steph "Ya, I think it may be a bad idea. If someone walked in on us we'd lose the lab."
                    nora "Right, ya. Of course."
                    "Stephanie must have resisted the drug. Maybe you pushed her too far all at once."
                    me "Well then, we should finish up here and head out, it's getting late."
                    "You gather your things and the three of you head your separate ways. You're certain you could have done better here."
                $noraO.change_slut_failed()
                $stephO.change_slut_failed()
                $noraO.change_resist(lab_threesome_event_object.get_resist_change(0))
                $stephO.change_resist(lab_threesome_event_object.get_resist_change(0))
                $lab_threesome_event_object.inc_level(0)

        "Have them suck you off together.":
            me "I wish I could relax like that. Every day at work I'm holding myself back when I look at you two."
            me "Surrounded by beautiful tits and asses, it's hard keeping your composure."
            "Both the girls look at you with unfocused eyes."
            me "And that's not the only thing that's hard. I could really use a blowjob to release some of this pressure."
            $ action_difficulty = 45
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            if stephO.check_willing(action_difficulty) and noraO.check_willing(action_difficulty):
                "The two girls look at each other."
                steph "If he's really that horny we could help him out."
                nora "I doubt he's been working as hard as he could if he's always distracted by us."
                "They stand up from their chairs, and you slide yours back from the table."
                nora "But nobody can know anything about this, okay?"
                me "Of course. My lips are sealed."
                "Nora and Stephanie kneel down in front of your chair as you unzip your pants and pull them down."
                steph "Wow, someone's ready."
                nora "Don't worry, we're here to help."
                "Stephanie rubs your shaft gently, then wraps a hand around it and begins stroking it."
                show steph blow1 at right
                $ stephO.inc_blow()
                $ noraO.inc_blow()
                steph "Spit on it and get it all wet for me Nora."
                "Nora leans over and lets out a long line of spit, which Stephanie quickly spreads over your cock."
                steph "That's better. Now for the main event."
                "She leans forward, using a hand on your chair to steady herself, and places her lips gently on your tip."
                "With painful slowness she slides her head down your shaft, running her tongue along the top and sides."
                "Nora reaches forwards and brushes her hair to the side and holds it there."
                "Stephanie stops, then slides herself back up and off your cock. She takes a deep breath at the top."
                steph "There we go, your turn."
                "Nora nods and shuffles closer. Then she licks you from the base of your penis up to the tip and places her mouth around it."
                "Then she slides her head forward down your already wet length. Her mouth is warm and soft as she begins to glide back and forth at a good pace."
                show nora blow1 at left
                me "That feels great, keep going."
                "Stephanie pulls her shirt and bra up over her tits, then goes back to watching Nora move up and down."
                show steph blow2 at right
                steph "Oooh that's hot. You're doing great Nora."
                "Nora slides off the end of your cock, and Stephanie immediately grabs it with one hand and strokes it."
                nora "Just need to catch my breath."
                steph "When you're ready I want to try getting us both around him. If you put your mouth on one side, and I put mine on the other we could do it."
                "Stephanie strokes you faster as she and Nora position themselves to the left and right of you."
                "They put their heads on both sides of your cock and spread their lips over it, meeting on either side like a kiss."
                hide nora
                hide steph
                show noraSteph blow1
                "Then they begin sliding up and down. You feel and see their tongues moving out around their mouths."
                "Seeing both girls on their knees in front of you gets you right to the edge, and you're almost ready to cum."
                menu:
                    "Cum in Nora's mouth.":
                        me "I want to cum in your mouth Nora. Get ready!"
                        "Stephanie sits back and leaves your cock all to Nora. Nora sits up straight and positions herself over your shaft, then goes back to giving you a normal blowjob."
                        hide noraSteph
                        show nora blow2 at left
                        $ noraO.inc_cum_mouth()
                        "After a few trips down her throat you feel yourself tensing up."
                        me "Here it is!"
                        "Stephanie cradles Nora's head from behind as you cum, holding her in place as you fill up her mouth."
                        steph "That's a good girl. Catch it all."
                        "Nora tries to pull away, but Stephanie keeps her there until you are all finished."
                        steph "Here, give it to me. I'll take care of it."
                        "Stephanie lets Nora's head back off your cock and quickly slides her own mouth over Nora's."
                        "The two kiss intensely for a long moment, then break away leaving a long line of cum strung between them."
                        show steph blow3 at right
                        "Stephanie looks at you and opens her mouth, revealing the cum that you unloaded into Nora."
                        $ stephO.inc_cum_swallow()
                        "Then she closes and swallows, smiling widely after."
                        nora "I didn't think I'd be able to keep it all in."
                        steph "You did great. The two of us were able to manage it. That's what friends are for, right?"

                    "Cum in Stephanie's mouth.":
                        me "I want to cum in your mouth Stephanie. Get ready!"
                        "Stephanie slides her mouth to the very top of your cock on their next rise. She opens her mouth and slides it over your tip, quickly taking you down her throat. Nora sits back while Stephanie takes over."
                        "Stephanie moves her head up and down quickly, licking and sucking as fast as she can. A few seconds later you tense up and begin to release."
                        "She takes your tip into her mouth and holds it there, sucking lightly, while you unload yourself into her mouth. When you finish she keeps you in her mouth for a few seconds, then sits back and lets you out."
                        nora "That was impressive Stephanie. I doubt I could have managed that."
                        hide noraSteph
                        show steph blow3 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "Stephanie looks over and opens her mouth to show a load of cum. She closes and swallows."
                        steph "It takes some practice, but you learn to like it."
                        nora "Well, I'm glad we could help [inputName]."
                        me "The pleasure was all mine."

                    "Cum over both their faces.":
                        me "I'm almost ready ladies, I want to cum on both your faces."
                        "Nora mumbles something but doesn't stop sliding her mouth over your cock. Stephanie nods her head slightly."
                        "A few more seconds of them servicing you and you're ready to cum."
                        me "Here we go, get ready!"
                        hide nora
                        hide steph
                        show noraSteph blow2
                        "The girls move back and sit down on their asses. Stephanie pulls Nora close and holds their heads close together. Stephanie then opens her mouth and sticks out her tongue for you."
                        "You stroke yourself as you cum, blasting a hot line across Stephanie's face, then move your aim over to Nora and land a pair of shots onto her. You move closer as your orgasm finishes and let the rest dribble onto them as well."
                        show noraSteph blow3
                        $ stephO.inc_cum_over()
                        $ noraO.inc_cum_over()
                        me "Wow, perfect."
                        "Stephanie wipes the cum off her face and licks her hands clean while Nora uses the end of her lab coat."
                        steph "A pleasure to help."
                        nora "Any time [inputName]. We're here to help."

                "The girls get up and start getting dressed. You chat for a little bit, then head your separate ways."
                "You feel confident you've made a [noraO.effect_string] impact on Nora and a [stephO.effect_string] impact on Steph."
                $noraO.change_slut_rebalanced(action_difficulty)
                $stephO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(lab_threesome_event_object.get_resist_change(4))
                $stephO.change_resist(lab_threesome_event_object.get_resist_change(4))
                $lab_threesome_event_object.inc_level(4)


            else:
                if temp_nora <=45:
                    steph "I can see why, we're both pretty good looking."
                    "Stephanie cups her breasts in her hands."
                    steph "What do you say Nora, should we help him out?"
                    "Nora looks at you for a moment, then looks at Stephanie."
                    nora "I'm not sure. I don't think it's a good idea here in the lab."
                    steph "Maybe you're right. We don't want to get caught and get the lab in trouble."
                    "Nora nods. Stephanie straightens out her sweater."
                    nora "I think I'm going to head out, it's getting a little late."
                    steph "Me too."
                    "The three of you head out from the lab and split up. Nora must have resisted the drug, maybe you pushed her too far all at once."

                elif temp_steph <=45:
                    nora "We've both gotten you that turned on? Well, you aren't going to be doing your best work when you're horny."
                    "Nora stands up from her chair and moves over to you."
                    steph "Wow Nora, are you actually up for that?"
                    nora "Well, if it's our fault."
                    steph "Sure, but you're normally so proper. I didn't expect you'd start blowing people just because they asked."
                    nora "Hmm, maybe you're right. I'm sorry [inputName] but you're going to have to take care of yourself some other way."
                    "She returns to her seat."
                    me "In that case I think I should be heading home then."
                    "You gather your things quickly and head out before the drug wears off and they start asking questions."
                    "You're certain you could have done something more with that opportunity."
                $noraO.change_slut_failed()
                $stephO.change_slut_failed()
                $noraO.change_resist(lab_threesome_event_object.get_resist_change(0))
                $stephO.change_resist(lab_threesome_event_object.get_resist_change(0))
                $lab_threesome_event_object.inc_level(0)

        "Fuck them both.":
            me "I know a way we can relax even more. You both look like you've been excited all day, how about we fuck each other until we all cum."
            $ action_difficulty = 75
            $noraO.set_action_exhib()
            $noraO.set_action_cumslut()
            $noraO.set_action_freeuse()
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            $stephO.set_action_freeuse()
            if stephO.check_willing(action_difficulty) and noraO.check_willing(action_difficulty):
                "Stephanie immediately stands up and pulls her shirt over her head."
                steph "Oh fuck ya. I've been horny all day. How about you Nora?"
                "Nora stands up too and nods, and begins taking off her labcoat."
                "You join the girls in disrobing and drop your pants. You stroke yourself while Nora and Steph take off their pants, then their underwear."
                show nora strip5 at left
                show steph strip2 at right
                "Stephanie drops to her knees in front of you and begins licking your cock while Nora places all her clothes on a chair."
                nora "How should we do this?"
                me "Get up onto the table here. Stephanie can suck me off while I lick you Nora. That should get us all warmed up."
                "Nora sits on the edge of the table, legs up and to the side of her. Stephanie repositions so her head is under the table."
                hide nora
                hide steph
                show noraSteph fuck1
                "Stephanie sucks you slowly while you lower your head to Nora's pussy. She spreads herself open for you with a hand, and you begin licking her."
                "Nora moans loudly, and Stephanie sucks faster in response."
                "After a few minutes Nora is twitching slightly every time you flick your tongue over her clit and Stephanie is fingering herself under the table while she takes you as deep as she can in her throat."
                me "Okay, I'm ready to fuck one of you."
                steph "Me first! I've been stuck under this table this whole time!"
                "Nora lowers a hand to her pussy when you move your head and starts fingering herself."
                nora "Okay, hurry up and finish her off so you can take care of me."
                "Stephanie gets up on the table beside Nora. You step between her legs and line your tip up with her slit."
                hide noraSteph
                show steph fuck1
                steph "That's right, come here and fuck me."
                me "Here I come, get ready."
                "You slide yourself into Stephanie and she shudders. She's already dripping wet from sucking you off."
                nora "Oh ya [inputName], look how badly she wants it."
                "Stephanie nods and moans as you start pumping back and forth."
                "Nora grabs a breast with one hand while rubbing her clit with the other. Her eyes are locked on your cock sliding in and out of her lab assistant."
                steph "Fuck that's good. Kiss me Nora!"
                "Stephanie leans over and grabs Nora, then pulls her into a deep kiss. The two continue to make out as you fuck Stephanie."
                "You pull out of Stephanie suddenly, step over, and slide into Nora without warning."
                "Distracted by her makeout session, Nora yells in surprise then gasps in pleasure as you slide into her."
                steph "Your turn now."
                nora "Yes! Oh fuck me!"
                "Nora leans back and lies down on the table as you fuck her. Stephanie seizes the opportunity and swings a leg over, lying on top of Nora."
                hide steph
                show noraSteph fuck2
                "You continue to fuck Nora while Stephanie positions her pussy directly above hers, and resumes making out with Nora."
                "Unable to limit yourself to just one, you begin thrusting four or five times into one girl, then pulling out and slipping into the other."
                "Both begin shaking with orgasms, yelping as you enter them and moaning as you pull out."
                "After a long satisfying while you feel your orgasm building."
                $ stephO.inc_sex()
                $ noraO.inc_sex()
                menu:
                    "Cum inside Stephanie.":
                        "You time your strokes and build up to your orgasm right as you enter Stephanie."
                        me "I'm going to cum. Get ready!"
                        steph "In me? Fill me up!"
                        nora "Give it to her!"
                        "You tense and hold Stephanie tight against your hips while you pulse your cum into her."
                        "She shudders and twitches, moaning loudly while holding onto Nora underneath her."
                        "Finally you finish and pull out, leaving a trail of cum that falls onto Nora's wet pussy underneath."
                        "Stephanie slumps, and a stream of cum leaks out. It drops onto Nora below."
                        show noraSteph fuck3
                        $ stephO.inc_cum_inside()
                        nora "That's a good girl. You took his whole load."
                        "Stephanie nods, and rolls off of Nora. Both girls are panting, and take a few minutes to catch their breath."
                    "Cum inside Nora.":
                        "You time your strokes and build up to your orgasm right as you enter Nora."
                        me "I'm about to cum. Get ready!"
                        nora "Fire away stud!"
                        "She grinds against your hips as best she can underneath Stephanie. Stephanie grabs her tits and starts sucking on them."
                        "You pull Nora close and release as deep inside her as you can. You both moan loudly and you can feel her pussy tighten around you."
                        "After a few moments you pull out, leaving a line of cum on the table."
                        "Nora relaxs her belly, and a small stream of cum begins leaking from between her legs."
                        show noraSteph fuck4
                        $ noraO.inc_cum_inside()
                        steph "Not about to waste all that, are you?"
                        "She hops down from the table and gets on her knees. She begins licking up the cum leaking out of Nora, and then begins licking Nora herself."
                        $ stephO.inc_cum_swallow()
                        nora "Oh god, not so soon. Oh god!"
                        "Nora writhes on the table while Stephanie eats her out for a few minutes. Eventually Stephanie sits back and wipes her mouth."
                        "All three of you take a moment to catch your breath."

                    "Cum on their faces.":
                        me "I'm going to cum, I want you two to share it on your faces."
                        "You pull out of Nora and step back from the table to give them room."
                        "Both girls slide off the table and turn around, presenting their faces for you."
                        steph "Squeeze together so he can't miss us. Open up!"
                        "She pulls Nora's head closer and they both open their mouths. Stephanie even sticks out her tongue for you."
                        "Stroking your shaft you begin unloading on them. You try and pump an equal amount onto both of them, and when you're finished they both have lines of cum draped across their forehead, nose, and mouth."
                        show noraSteph fuck5
                        $ stephO.inc_cum_over()
                        $ noraO.inc_cum_over()
                        me "That's great. You two look great together."
                        "Stephanie turns and pulls Nora into a long deep kiss."
                        "You watch the two make out, covered in your cum, until the girls break up their makeout session."
                "Eventually you all get dressed and head your separate ways. You're confident you've had a huge effect on both of them today."
                $noraO.change_slut_rebalanced(action_difficulty)
                $stephO.change_slut_rebalanced(action_difficulty)
                $noraO.change_resist(lab_threesome_event_object.get_resist_change(5))
                $stephO.change_resist(lab_threesome_event_object.get_resist_change(5))
                $lab_threesome_event_object.inc_level(5)

            else:
                if temp_nora < temp_steph:
                    nora "Here in the lab? I don't think so."
                    steph "You think it's a bad idea Nora?"
                    "She nods, slowly at first, then gaining confidence."
                    nora "I know it is. If we get caught we're all out of jobs."
                    steph "Right, I didn't think about that."
                    nora "We should just head out right now before this goes any farther."
                    "The three of you gather your things and head out the door. Nora must have resisted the drug."
                    "You're certain you could have gotten more out of the situation than that."

                else:
                    steph "I don't think Nora would be up for that. You know how she is."
                    "Nora looks around slowly, then nods."
                    nora "Right, of course not. It's inappropriate for you to even joke about that [inputName]."
                    "Stephanie must have resisted the drug and has warned Nora. Nothing to do now but back off."
                    me "Of course, you're both right. A bad joke on my part."
                    "You talk for a few more minutes, but eventually you all decide it's getting late and head home."
                    "Maybe you tried to push them too far all at once. You definitely didn't make full use of the situation."
                $noraO.change_slut_failed()
                $stephO.change_slut_failed()
                $noraO.change_resist(lab_threesome_event_object.get_resist_change(0))
                $stephO.change_resist(lab_threesome_event_object.get_resist_change(0))
                $lab_threesome_event_object.inc_level(0)

    jump campusJumpTimeSkip

label maj_stephalexthreesome:
    #Intro stuff:
    me "You drive a hard bargain Steph. Fine, I'll treat you both to some ice cream. What do you want."
    steph "Strawberry, and get me some of those colourful sprinkles while you're at it."
    alex "Chocolate for me, if you're buying."
    me "Alright, I'll be back in a few minutes. Don't get into too much trouble."
    steph "Since [inputName] is going to be busy, I'll show you around Alexia. Come on."
    hide alex
    hide steph
    show bg campus_day
    "You leave the lab and head upstairs. You walk briskly towards the food court at the center of campus and wait in line at the ice cream place."
    "After a few minutes you have your order and you start to travel back to the lab. You pause at a bench out of sight from anyone and set the ice cream down."

    $lab_alex_steph_event_object.happened = True
    call serum_give(alexO) from _call_serum_give_27
    $ temp_alex = _return
    call serum_give(stephO) from _call_serum_give_28
    $ temp_steph = _return
    #Post-serum intro stuff:
    "You pour the serum over the ice cream, then mix it in. After a second or two of work it's impossible to tell that anything is different."
    show bg lab_day
    show alex casual at right
    show steph work at left
    "You return to the lab and push the door open. Alexia is watching while Stephanie explains one of the machines in the lab."
    steph "...And then this spins, pulling everything apart so that we can just grab the product that we want and throw away the rest. Ah, here's the ice cream man."
    me "Yep, I'm back. Did you have a good look around Alexia?"
    "You hand the girls their ice cream. Stephanie starts to eat hers immediately."
    alex "Yeah, this place is insane! I can't believe you actually work with all of this stuff every day."
    "She takes a scoop of her ice cream and starts to eat it as well."
    alex "Didn't you want anything for yourself [inputName]?"
    me "I'm not feeling hungry at the moment, you two enjoy though. Make sure to eat it all."
    "You lean on your desk and watch while Alexia and Stephanie eat. After a minute you're able to notice the first signs of the serum taking effect: dilated pupils and an unfocused gaze."
    me "How's the ice cream ladies?"
    steph "It's nice."
    alex "It's great, thank you [inputName]."
    menu:
        "Have them make out with each other.":
            $ action_difficulty = 0
            $stephO.check_willing(action_difficulty)
            $alexO.check_willing(action_difficulty)
            #Scene
            me "I'm glad you two are getting along so well. You don't mind that I brought a guest, right Stephanie?"
            steph "It's fine, Alexia seems like a great person."
            alex "Aw, thanks Steph. You seem pretty nice too."
            me "Alexia, maybe you should give Stephanie a kiss to say thank you."
            "Stephanie and Alexia look at each other. After a few seconds Stephanie shrugs, and Alexia steps closer to her."
            hide steph
            hide alex
            show alexSteph kiss1 at center
            "Alexia throws her hands onto Stephanie's shoulders and stands up on the tips of her toes. They kiss for a brief moment."
            me "Come on, you can do better than that. Show her how to do it Stephanie."
            "Stephanie leans in and returns the kiss, holding Alexia's head in place. You hear Alexia moan, and the two of them make out for a long moment."
            show alexSteph kiss2 at center
            "They finally break apart, leaving a trail of saliva strung between them for a split second. Alexia takes a deep breath."
            alex "Wow, I certainly wasn't expecting that. That was impressive."
            steph "Heh, yeah. You could say I have some experience."
            alex "Hmm, you'll have to teach me your secrets then."
            hide alexSteph
            show alex casual at right
            show steph work at left
            steph "For a cute girl like you, I'd be glad to. How about I finish that tour I was giving you though."
            alex "Sounds cool, lead the way."
            "Stephanie leads Alexia around the lab, pointing to various machines and giving a brief description. After a few minutes it's time for Alexia to head off to her class."
            alex "This was really cool, thanks for bringing me here [inputName]. And thank you Stephanie for letting me stay."
            steph "As long as our boss doesn't find out it's no problem at all."
            me "It was nice to hang out. I'll walk you upstairs."
            hide steph
            "You guide Alexia through the twisting basement tunnels and back to the surface. She waves goodbye and heads towards the center of campus."
            hide alex
            "As you watch her leave you feel like you've made a [alexO.effect_string] impact on Alex and a [stephO.effect_string] impact on Stephanie with your actions today."

            $alexO.change_slut_rebalanced(action_difficulty)
            $stephO.change_slut_rebalanced(action_difficulty)
            $alexO.change_resist(lab_alex_steph_event_object.get_resist_change(1))
            $stephO.change_resist(lab_alex_steph_event_object.get_resist_change(1))
            $lab_alex_steph_event_object.inc_level(1)

        "Have them both strip for you.":
            #Intro:
            me "I'm glad you two are getting along so well, it's always nice to see two hot girls together."
            "Stephanie and Alexia look at each other for a second. Alexia giggles softly while admiring Stephanie."
            alex "Well, he's not wrong. I think we qualify as \"hot\"."
            me "I've got an idea for you two. Why don't you strip down a little and show off for each other."

            $ action_difficulty = 15
            $alexO.set_action_exhib()
            $stephO.set_action_exhib()
            if stephO.check_willing(action_difficulty) and alexO.check_willing(action_difficulty):
                #Scene
                alex "That might be fun. I don't know, what do you think Steph?"
                "Stephanie bites her lip and looks Alexia up and down."
                steph "Fuck it, lets do it!"
                "Alexia claps her hands. Before you can say another word they start to strip off their clothes."
                show alex strip17 at right
                show steph strip3 at left
                "Stephanie pulls her shirt off and drops it onto the chair by her desk. Alexia does the same, letting her shirt just fall to the ground."
                alex "Oh, nice tits."
                steph "Oh these? Well thank you, I made them myself."
                show alex strip3 at right
                show steph strip1 at left
                "Stephanie unzips her pants and pulls them down past her knees. Alexia undoes her skirt and pulls it off too. Soon both girls are standing and looking at you in their underwear."
                steph "Well, what do you think [inputName]?"
                me "You both look amazing. It seems cruel to keep your underwear on after all this though."
                alex "Hmm, maybe he's right Steph. I kind of want to see those puppies too."
                show alex strip12 at right
                show steph strip7 at left
                "Alexia reaches behind her back and undoes her bra. Stephanie pauses for a moment, then follows suit and undoes her. They both shrug off their bras and let them fall to the ground."
                steph "Alexia, would you help me with my panties please?"
                "Stephanie turns around and wiggles her butt at you and Alexia."
                alex "Jesus, go easy on the man. He looks like he's going to have a stroke if you keep doing that. Now, lets see what we can do..."
                hide alex
                hide steph
                show alexSteph strip1 at center
                "Alexia kneels down beside Stephanie and grabs her panties at her waist. Alexia pulls them down slowly, letting you watch as they peel off of Stephanie's pussy."
                $ stephO.inc_naked()
                $ alexO.inc_naked()
                "Once they're past Stephanie's knees Alexia lets go of the panties and lets them fall to the ground. She stands up and pulls her own down too, kicking them to the other side of the room and giggling."
                hide alexSteph
                show alex strip4 at right
                show steph strip2 at left
                "The girls turn back to face you, both of them blushing a little and smiling broadly."
                alex "God, this feels so naughty. Take a good look [inputName], enjoy it."
                "Alexia turns around and bends over a little to show off her ass. Stephanie gives it a quick spank to make it jiggle for you."
                steph "Isn't that a great sight?"
                me "It's damn near perfect."
                steph "Near? How about this?"
                hide alex
                hide steph
                show alexSteph strip2 at center
                "Stephanie turns around and bends forward with Alexia. They wiggle their naked butts at you, giving you a good look at their cute little pussies at the same time."
                me "Yeah, that would do it."
                steph "Ha, I thought so!"
                "Stephanie stands up and turns back to you. Alexia does the same, putting her arm around Stephanie's waist."
                steph "Well this was a lot of fun, but our boss might actually be getting in any minute now. We should get dressed before we're all in trouble."
                alex "Right, sounds like a good idea then. I've got a class to get to anyway."
                hide alexSteph
                "You watch while the girls collect their clothing and begin getting dressed. Once they're finished you walk Alexia up to ground level again and wave goodbye."
                "You feel like you've had a major effect on both of them today."

                $alexO.change_slut_rebalanced(action_difficulty)
                $stephO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(lab_alex_steph_event_object.get_resist_change(1))
                $stephO.change_resist(lab_alex_steph_event_object.get_resist_change(1))
                $lab_alex_steph_event_object.inc_level(2)

            else:
                #reject scene
                if temp_alex < temp_steph:
                    #alex resists first
                    steph "Hmm, I don't know. What do you think Alexia?"
                    alex "I... I'm not sure. I mean, you seem nice. I just hardly know you, you know?"
                    "Alexia turns away from you and Stephanie, slowly turning red."
                    alex "I'm sorry, I just don't think I'm up for it."
                    steph "Hey, it's fine. We're all friends here, you don't have to do anything you don't want to do."
                    me "Yeah, of course Alexia. It was just an idea."
                    "Alexia turns back to face you. She's got a sharper look in her eye now; she must have resisted the serum."
                    alex "Okay, thanks for understanding. How about we finish that tour Stephanie, I was having a good time with that."
                    steph "Sure thing. Now, where were we..."


                else:
                    #steph resists first
                    alex "That might be fun. I don't know, what do you think Steph?"
                    steph "Well... Honestly [inputName], if Nora found out she'd have us both fired."
                    me "Nora won't be here for another hour or two though, we've got time."
                    steph "No, I think we should just hang out a little. Alexia, how about I finish that tour for you?"
                    alex "Sure, that sounds fun too. I wouldn't want either of you getting fired just because of me."
                    "Stephanie has a sharper look in her eye; she must have resisted the serum. No point pushing her any farther now."
                    me "Alright, forget I mentioned anything then. There's a ton of cool stuff here in the lab."

                "Stephanie shows Alexia around the rest of the lab. When it's time for her next class you walk Alexia back up to ground level."
                "You say goodbye, and she starts walking towards the center of campus. You feel like you could have accomplished more here if you hadn't pushed the girls so far."

                $alexO.change_slut_failed()
                $stephO.change_slut_failed()
                $alexO.change_resist(lab_alex_steph_event_object.get_resist_change(0))
                $stephO.change_resist(lab_alex_steph_event_object.get_resist_change(0))
                $lab_alex_steph_event_object.inc_level(0)


        "Have them titfuck you.":
            #Intro:
            me "I'm glad you two are getting along so well, I can think of something you two can do together that we'd all enjoy."
            alex "Hmm? What would that be?"
            me "You've both have great sets of tits, you should pull them out and we can have some fun with them."

            $ action_difficulty = 30
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            if stephO.check_willing(action_difficulty) and alexO.check_willing(action_difficulty):
                #Scene
                alex "You know, that doesn't sound like such a bad idea. What do you say Stephanie? I'm in if you are."
                "Alexia grabs the bottom of her shirt and starts to pull it up."
                steph "Alright, if you're going to do it then I feel like I have to keep up. Lets go."
                "Stephanie and Alexia both pull their shirts up and off, throwing them to the side of the room. Wheile they're getting undressed you unzip your pants and let your hard cock spring free."
                alex "Well hello there. It looks like we have an admirer. We better help him out pretty soon Steph, he looks like he's ready to burst already."
                steph "I think you're right. Help me get my bra, if you don't mind."
                show steph strip27 at left
                show alex strip53 at right
                "Stephanie turns her back to Alexia, and she unhooks her bra. They switch places, and within a moment both girls have their tits out for you."
                steph "How about you sit down right here [inputName] and let us take over."
                me "Well, you girls seem to know what you want to do."
                hide steph
                hide alex
                show alexSteph tit1 at center
                "You sit down in one of the office chairs. Stephanie and Alexia get onto their knees on either side of your legs and lean forward."
                steph "Alright, lets see if we can do this together."
                alex "I'm sure we can figure it out. It's not rocket surgery, right?"
                $ stephO.inc_tit()
                $ alexO.inc_tit()
                "They both take their tits in their hands and lean towards each other. They catch your hard shaft inbetween their cleavage, sandwiching you between their soft, warm breasts."
                me "Fuck, that feels great you two."
                steph "Mmm, good."
                "Stephanie starts moving her tits up and down, and Alexia follows her lead. You lean back and moan softly as they start to tit fuck you together."
                alex "He's so cute when he's having fun. Can you go a little faster?"
                steph "Yeah, I think so. Ah..."
                "They speed up, using their tight cleavage to pleasure you. You enjoy it for as long as you can, but soon you feel your orgasm approaching."
                menu:
                    "Cum on their faces.":
                        me "Fuck, I'm almost there. I want to cum on your faces."
                        alex "I like the sounds of that too. Come on Steph, we're in the home stretch now!"
                        "Alexia speeds up even more, and with Stephanie's help they push you over the edge of your orgasm. You grunt and pull your cock out from between their tits while they sit back together and look up at you."
                        if stephO.cumslut:
                            steph "Come on, give it to us [inputName]! We want it so badly!"
                        if alexO.cumslut:
                            alex "Oh god yes, give it to us!"
                        $ stephO.inc_cum_over()
                        $ alexO.inc_cum_over()
                        show alexSteph tit5 at center
                        "You grab your shaft and stroke yourself off as you cum, spraying your load over Alexia and Stephanie. They pull each other close, giving you a nice big target to aim for."
                        "When you've finished emptying your balls you sit back with a sigh. The girls look at each other and giggle."
                        steph "God, he really did give it to you, didn't he."
                        alex "It looks like I got just as much as you."
                        if stephO.cumslut:
                            "Stephanie leans forward and starts to lick your sperm off of Alexia's cheeks."
                        else:
                            "Stephanie runs a finger over Alexia's face, cleaning some of your sperm off of her cheek."
                        if alexO.cumslut:
                            alex "Here, let me help you with that too."
                            "Alexia sticks her tongue out and starts to lick at Stephanie's neck and chin, catching drops of your cum before they can fall to the floor."
                        else:
                            "Alexia uses her finger to catch some drops of your cum before they can fall onto Stephanie's pants."
                        "After a few seconds the girls both sit back and take a few deep breaths."
                        me "That was amazing girls, thank you."
                        alex "Glad you had a good time too [inputName]."
                        steph "Yeah. Now Nora may be getting here soon, we should really get cleaned up."
                        me "That sounds like a good idea. I'm going to take a walk and stretch my legs, you two can get cleaned up in here."
                        alex "Alright, thanks for showing me around [inputName], I'll see you later!"


                    "Tell them to kiss while you cum.":
                        me "Fuck, I'm almost there. Make out with each other while I cum!"
                        show alexSteph tit2 at center
                        "Alexia doesn't waist any time and leans forward to press her lips against Stephanie's. Stephanie takes a moment to respond, then moans and closes her eyes while she returns the kiss."
                        "The two girls keep their tits pressed tightly around your hard shaft as they make out, and the visuals alone are enough to push you right over the edge. You grunt a little as you start to climax."
                        $ stephO.inc_cum_over()
                        $ alexO.inc_cum_over()
                        show alexSteph tit3 at center
                        "Stephanie and Alexia mumble to each other and moan as they kiss. You spasm out your cum up between their cleavage, spraying it over their necks. It collects in a puddle where their tits squeeze around your cock."
                        if stephO.cumslut:
                            "Stephanie shivers with pleasure as your cum spurts out onto her. She breaks the kiss just long enough to moan loudly."
                        if alexO.cumslut:
                            "Alexia has a quiver run through her entire body as she makes out with Stephanie with your cum dripping down her breasts. She moans loudly while she makes out."
                        show alexSteph tit4 at center
                        "After a few moments the two girls break their kiss and sit back. Your semen starts to run down between their tits and onto their stomachs."
                        steph "Wow, that was amazing Alexia."
                        alex "Yeah. I think [inputName] had a good time too."
                        "Stephanie runs a finger between her tits and scrapes up some of your cum. She brings it to her lips and licks it clean."
                        steph "Yeah, I think he did."
                        me "That was amazing, thank you girls."
                        steph "Hey, Nora may be getting here soon. We should probably be getting cleaned up."
                        me "That sounds like a good idea. I'm going to take a walk and stretch my legs. You two can get cleaned up in here."
                        alex "Alright, thanks for showing me around [inputName], I'll se you later!"

                hide alexSteph
                "You leave the lab while Stephanie and Alexia start looking around for tissue to clean themselves off with. You feel like you've had a major effect on them tonight."
                $alexO.change_slut_rebalanced(action_difficulty)
                $stephO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(lab_alex_steph_event_object.get_resist_change(3))
                $stephO.change_resist(lab_alex_steph_event_object.get_resist_change(3))
                $lab_alex_steph_event_object.inc_level(3)

            else:
                #reject scene
                if temp_alex < temp_steph:
                    #alex resists first
                    "Alexia and Stephanie glance at each other for a long moment."
                    steph "Well? It could be fun..."
                    alex "Yeah, but won't you guys get in trouble? Do you have a boss around or something?"
                    me "It's fine, our boss won't be here for an hour or two."
                    steph "Usually, at least."
                    alex "That seems a little risky, doesn't it? Come on [inputName], this doesn't seem worth risking your job over."
                    steph "But... Uh... I don't know, maybe she's right [inputName]."
                    "Stephanie and Alexia both look at you. Alexia seems to have her wits about her again; she must have resisted the serum. You won't achieve anything by pushing them farther now."


                else:
                    #steph resists first
                    "Alexia and Stephanie glance at each other for a long moment."
                    alex "Well? I might be up for it if you are..."
                    steph "I... I don't know. Our boss could come in early today and me and [inputName] would be in some pretty deep shit if she did."
                    me "I'm sure it'll be fine Stephanie. We've got plenty of time."
                    alex "Come on [inputName], I don't know if this is worth risking your job over."
                    "Stephanie turns to you and nods."
                    steph "I think she's right. Maybe we should just do something else instead."
                    "Stephanie seems to have a sharp look in her eye already; she must have resisted the serum. You won't achieve anything by pushing them farther now."

                me "I guess you're right. Just forget I said anything about it."
                alex "How about you finish that tour you were giving me Steph?"
                steph "Sure. Come back over here."
                "Stephanie shows Alexia around the rest of the lab. When it's time for her next class you walk Alexia back up to ground level."
                "You say goodbye, and she starts walking towards the center of campus. You feel like you could have accomplished more here if you hadn't pushed the girls so far."
                $alexO.change_slut_failed()
                $stephO.change_slut_failed()
                $alexO.change_resist(lab_alex_steph_event_object.get_resist_change(0))
                $stephO.change_resist(lab_alex_steph_event_object.get_resist_change(0))
                $lab_alex_steph_event_object.inc_level(0)

        "Have them both blow you.":
            #Intro:
            me "It's good to see you two are getting along. Since you're such good friends already, how about we do something togethter?"
            steph "What did you have in mind [inputName]?"
            "You rub your crotch, emphasising the outline of your hard shaft for the girls."
            me "I happen to know Stephanie loves sucking cock. Why don't you give Alexia a demonstration?"

            $ action_difficulty = 45
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            if stephO.check_willing(action_difficulty) and alexO.check_willing(action_difficulty):
                #Scene
                alex "[inputName]! That's a little rude, isn't it?"
                "Stephanie winks at you, then drops to her knees at your feet."
                steph "It's fine Alexia, he's right. The size, the shape, mmm."
                show steph strip46 at left
                "She undoes the zipper on your pants and pulls them down, letting your cock spring free. She leans forward and lets it rest against her cheek."
                steph "I really do love it. He's just calling a spade a spade."
                alex "Oh... Well I guess that's okay then. How hard can it be though?"
                steph "Sucking cock? Oh girl, there's a whole world of oral techniques out there for you to master. It's not just a matter of sticking it down your throat and calling it a day."
                "Stephanie sticks her tongue out and runs it along the bottom of your shaft. She pauses at the top and gives the tip a kiss."
                steph "Come a little closer, I'll show you what I mean."
                $ stephO.inc_blow()
                hide steph
                hide alex
                show alexSteph blow1 at center
                "Alexia hesitates for a split second, then gets onto her knees opposite Stephanie. She watches as Stephanie licks at the sides and bottom of your dick."
                steph "Ah... There, first you have to get it nice and wet. Guys love a sloppy blowjob, isn't that right [inputName]."
                me "Fuck that feels good. Yeah, you know what I like Stephanie."
                steph "Then, when you've got him nice and ready, you can just slide him in."
                "Stephanie slips you into her mouth, then keeps going until she has your whole cock down her throat. She bobs her head back and forth a little, rubbing the tip of your dick against the back of her mouth."
                alex "Holy shit, she really is good at that."
                "Stephanie slides back, letting go of your cock with a wet pop. She takes a deep breath and looks at Alexia."
                steph "Just like that. How about you give it a try now."
                $ alexO.inc_blow()
                show alexSteph blow2 at center
                "She plants a finger on your shaft and points your dick towards Alexia. Alexia takes a second to prepare herself, then opens her mouth wide and slips you in."
                steph "Perfect. Now slide him all the way to the back. Your nose should be bumping up against his stomach when you're deep enough."
                "Alexia nods as best she can and pushes herself deeper onto your dick. She has to pause and reposition once, but finally succeeds in going all the way down on you."
                steph "Good girl. How does that feel [inputName]?"
                me "It feels amazing. Your throat feels amazing Alexia."
                "Stephanie brushes Alexia's hair out of her face."
                steph "Make sure to look up at him, right into his eyes as you suck on his cock."
                "Alexia looks up, pressing your shaft against the top of her mouth. The feeling sends shivers of pleasure up your spine, and she looks pretty damn sexy while she looks up at you, balls deep on your dick."
                "After a few moments Alexia pulls back. She coughs a few times, then takes a deep breath."
                alex "Fuck, that's going to take some practice."
                steph "I'm sure you won't have any trouble finding someone to help you out with that. Alright, we should stop teasing poor [inputName] and help finish him off."
                show alexSteph blow1 at center
                "Stephanie slides you back into her mouth and starts to throat you again. Her tongue keeps licking at hte bottom of your dick, and the feeling sends shivers up your spine."
                "Alexia watches for a minute or two, then leans farther down and starts to lick at your balls. Stephanie puts her arm around her and keeps sucking you off."
                me "Yeah, keep that up girls, I'm almost there!"
                menu:
                    "Cum on Stephanie.":
                        "You feel your core tense up as you're pushed over the edge."
                        me "Here you go Stephanie!"
                        $ stephO.inc_cum_over()
                        show alexSteph blow4 at center
                        "She slides back off of your cock and looks up at you, mouth open wide and tongue out. You stroke yourself off, spraying your load over her face while Alexia keeps sucking on your balls."
                        "When you're finally done you step back and grab a chair to sit down on. Alexia takes a look at Stephanie's cum covered face and smiles."
                        alex "Wow, he really gave it to you, didn't he."
                        steph "Damn right he did."
                        if alexO.cumslut:
                            "Alexia leans forward, placing a hand on Stephanie's chin to hold her in place. She sticks out her tongue and runs it along Stephanie's cheek, cleaning off a line of your sperm."
                            alex "Mmm, god that tastes good. Sorry, I hope you don't mind."
                            steph "No, of course not. I know exactly what you mean."
                        "After catching their breath they girls stand up. Stephanie starts to wipe your semen off of her face."


                    "Cum on Alexia.":
                        "You feel your core tense up as you're pushed over the edge."
                        me "Here we go! Get ready for it Alexia!"
                        "Stephanie slides back off of your cock and grabs it with one of her hands. She uses her other hand to guide Alexia in front of you while stroking you off."
                        steph "That's it, give it to her [inputName]! She wants every last drop of that hot cum on her!"
                        $ alexO.inc_cum_over()
                        show alexSteph blow3 at center
                        "Alexia barely manages to make it in front of you before you cum. Stephanie guides your cock left and right, spraying your load over Alexia's waiting face."
                        "When you're done Stephanie leans forward and licks the last few drops of semen off your tip, then lets go of you completely."
                        alex "Fuck, that felt like a lot. Was it a lot?"
                        steph "Yeah, it was a lot. Here, let me get some of that for you."
                        if stephO.cumslut:
                            "Stephanie tilts Alexia's face towards her and starts to lick your sperm off of her cheeks and chin. After a few moments Alexia is almost completely cleaned up."
                        else:
                            "Stephanie tilts Alexia's face towards her and starts to clean your sperm off with her finger. She licks it clean after each pass, and soon Alexia is almost completely cleaned up."
                        steph "Mmm, I never get tired of that."
                        alex "I'm glad to share, it was a team effort to get it out of him."

                steph "Nora's going to be in for work soon, so we should probably get cleaned up."
                me "Yeah, that sounds like a good idea. I'm going to go for a walk, I'll be back in a little bit for work."
                alex "Thanks for showing me around [inputName], I had a great time. See you around!"
                hide alexSteph
                "You leave the lab while Stephanie and Alexia look for some tissues to get cleaned up with. As you walk towards the center of campus you feel like you've had a major effect on them today."
                $alexO.change_slut_rebalanced(action_difficulty)
                $stephO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(lab_alex_steph_event_object.get_resist_change(4))
                $stephO.change_resist(lab_alex_steph_event_object.get_resist_change(4))
                $lab_alex_steph_event_object.inc_level(4)

            else:
                #reject scene
                if temp_alex < temp_steph:
                    #alex resists first
                    alex "[inputName]! You can't just say that about people!"
                    steph "No, it's okay Alexia. I... Well, he's kind of right."
                    alex "Okay, but it's still rude as fuck."
                    "Alexia seems completely in control of herself already. Her anger must have helped her resist the serum. Pushing her farther now would only undo what progress you've made."
                    me "Shit, I'm sorry Alexia. Lets just forget I said anything, it was inappropriate."
                    alex "Don't appologize to me, appologize to her."
                    steph "Really, it's no big deal."
                    me "I'm sorry Stephanie, I stepped out of line."
                    steph "Uh, thank you. I guess."
                    alex "There, thank you for doing that [inputName]. Now how about we put this behind us, we should finish that tour of the lab if you have time Steph."
                    steph "Yeah, sure. Follow me over here..."

                else:
                    #steph resists first
                    steph "[inputName]! There's someone else here, remember?"
                    me "Oh come on, Alexia doesn't mind, right?"
                    alex "I... I mean, it's a little rude, isn't it [inputName]."
                    steph "Exactly."
                    "Stephanie seems completely in control of herself already. She must have been upset by your comment, and it's helped her resist the serum. Pushing her farther now would only undo what progress you've made."
                    me "I'm sorry Stephanie, that was inappropriate of me to bring up."
                    steph "Thank you. Now how about we do something normal; I was going to show you around the lab, right Alexia?"
                    alex "Yeah, lets give that a try."
                    steph "Cool. Follow me back here..."

                "Stephanie shows Alexia around the rest of the lab. When it's time for her next class you walk Alexia back up to ground level."
                "You say goodbye, and she starts walking towards the center of campus. You feel like you could have accomplished more here if you hadn't pushed the girls so far."
                $alexO.change_slut_failed()
                $stephO.change_slut_failed()
                $alexO.change_resist(lab_alex_steph_event_object.get_resist_change(0))
                $stephO.change_resist(lab_alex_steph_event_object.get_resist_change(0))
                $lab_alex_steph_event_object.inc_level(0)



        "Fuck them both.":
            #Intro:
            me "It's good to see you two are both getting along so well."
            "You rub your crotch, emphasising the outline of your hard shaft."
            me "What do you girls think about me pulling my cock out so we can have some fun together?"

            $ action_difficulty = 60
            $alexO.set_action_exhib()
            $alexO.set_action_cumslut()
            $stephO.set_action_exhib()
            $stephO.set_action_cumslut()
            if stephO.check_willing(action_difficulty) and alexO.check_willing(action_difficulty):
                #Scene
                alex "Can you two just do that here?"
                steph "Well, our boss won't be around for a few hours. So yeah, if you're up for it."
                "Alexia smiles and nods. Before you can say another word she's pulling her shirt up and over her head."
                alex "Fuck yes I'm up for it. It's so hard to find a nice, quiet place around here where you won't be interupted half way through, right [inputName]?"
                show steph strip27 at left
                show alex strip53 at right
                "Stephanie pulls her shirt off too, then starts to undo her bra in front of you. Alexia does the same, and soon both of them have their tits out for you."
                show alex strip4 at right
                show steph strip2 at left
                "Alexia pulls her skirt down and kicks it to the side, then does the same for her panties. She turns around and wiggles her butt at you while Stephanie finishes stripping as well."
                alex "Come on [inputName], can't you see that I need you? I've barely been keeping it together all day."
                "Alexia bends over one of the lab benches and spreads her legs. You have a perfect look at her dripping wet pussy."
                steph "Wow, it looks like she really needs it. Hmm, lets see what I can do first."
                hide alex
                hide steph
                show alexSteph fuck1 at center
                "You start to pull down your pants and get your cock out while Stephanie knees down between Alexia's legs."
                alex "Wait, what are... Oh... Oh never mind... Ah... I see what you're... Ah... doing!"
                "Stephanie runs her tongue along Alexia's cunt, pausing at her clit to play with it for a few seconds. Alexia doesn't hold anything back and moans as loudly as she can."
                alex "Oh fuck, oh fuck that's nice! Ah!"
                me "Alright Stephanie, I think I can take over from here."
                "Stephanie leans back and wipes her lips, then stands up and moves to the side."
                steph "Go for it [inputName], she's nice and ready now."
                $ alexO.inc_sex()
                show alexSteph fuck2 at center
                "You press the tip of your cock against Alexia's pussy. You're able to slide in with barely any pressure, fitting your full lenth inside of her on the first stroke."
                alex "Ooooh..."
                "Alexia moans helplessly into the lab bench as you start to fuck her, working your hips back and forth slowly. Stephanie wraps her arms around your torso, stroking your chest and nibbling on your neck."
                steph "God that looks good. Do you think I could have a turn soon Alexia?"
                alex "Yeah... Ah! Fuck! I need... I need a break..."
                "You pull out of Alexia's tight cunt. Stephanie leans over the lab bench beside Alexia, and you take a step over to line up with her pussy now."
                steph "Thanks for getting him all wet for me. Ah!"
                $ stephO.inc_sex()
                show alexSteph fuck3 at center
                "Stephanie gasps as you spread her tight slit and slide yourself in. Alexia's juices have you nicely lubricated, and you start to pump in and out right away."
                alex "Yeah, give it to her [inputName]! Look how badly she wants it!"
                steph "I do want it! Fuck me [inputName]! Fuck me!"
                "Stephanie rolls her hips back to meet yours with each thrust. Her cunt is warm and wet, and seems to clamp down tighter on your shaft with each pump. It isn't long before you feel your orgasm building up."
                menu:
                    "Cum inside of Stephanie.":
                        me "Fuck, here I cum Steph!"
                        if stephO.cumslut:
                            steph "Do it! Fill me up, get me pregnant, I don't care! Just give me that hot cum!"
                        else:
                            steph "Do it! Finish wherever you want!"
                        $ stephO.inc_cum_inside()
                        "You give Stephanie one last stroke of your cock, then hold yourself as deep inside of her as you can manage. You both shiver with pleasure as you start to empty your balls deep inside of her."
                        alex "Fuck, that's so damn hot."
                        steph "Ah! Ah..."
                        "Stephanie goes limp against the lab bench, legs twitching occasionally. You wait until you're completely done climaxing, then step back and slide out of her."
                        me "That felt amazing girls."
                        alex "Yeah. I think you might have broken her though."
                        steph "I'll... I'll be fine. That was just really intense."
                        show alexSteph fuck4 at center
                        "You and Alexia watch as your cum starts to dribble out of Stephanie's pussy and down her leg."
                        me "Nora's going to be in for work soon. You two should probably get cleaned up. I'm going to go for a walk and stretch my legs."
                        steph "Yeah... Right. Alexia, can you find us some tissue or something."
                        alex "Sure. Thanks for showing me around the lab [inputName], I had a lot of fun."
                        hide alexSteph
                        "You wave goodbye to the girls and leave them as they start to get dressed again. As you head upstairs you feel like you've had a [alexO.effect_string] impact on Alex and a [stephO.effect_string] impact on Steph today."

                    "Cum inside of Alexia.":
                        me "Lets fill you up a bit Alexia!"
                        "You pull out of Stephanie, causing her to shiver with pleasure, and take a step to the side. Alexia yells and twitches as you slam your cock back inside of her dripping wet cunt."
                        if alexO.cumslut:
                            alex "Yes, do it! I want that hot cum! I want every last drop deep in my pussy! Get me pregnant, fill me up, just give it to me now!"
                        else:
                            alex "Oh fuck! Oooooh fuck!"
                        $ alexO.inc_cum_inside()
                        "You give her a few quick thrusts, then hold yourself as deep inside of her as you can manage. You both twitch a little as you empty your balls inside of her."
                        steph "That's a good girl. Does it feel warm inside you?"
                        alex "Ah... Yeah, it does..."
                        show alexSteph fuck5 at center
                        "Alexia pants loudly, gasping when you step back and pull your shaft out of her. Stephanie stands up and watches as your cum starts to dribble down her leg."
                        if stephO.cumslut:
                            steph "Mmm, I wish that was me. It looks so nice and thick..."
                            "She leans down and runs a finger up Alexia's thigh, collecting your sperm on the end. She brings it up to her mouth and licks it clean."
                        me "That felt amazing girls, thanks."
                        steph "It was our pleasure, really."
                        me "Nora's going to be in for work soon. You two should probably get cleaned up. I'm going to go for a walk and stretch my legs."
                        steph "Sure. I'll make sure Alexia is cleaned up and out of here by the time Nora shows up."
                        alex "Talk to you later [inputName]. This tour was really fun..."
                        hide alexSteph
                        "You wave goodbye to the girls and leave them as they start to get dressed again. As you head upstairs you feel like you've had a [alexO.effect_string] impact on Alex and a [stephO.effect_string] impact on Steph today."

                    "Cum on both of them.":
                        me "I want to cum on both of you, get on your knees!"
                        steph "Oh yes, give it to us!"
                        "You step back and pull out of Stephanie's tight pussy. She turns around and drops to her knees in front of you, quickly joined by Alexia."
                        "Stephanie pulls Alexia close to her as you stroke yourself off, pushing yourself over the edge."
                        $ stephO.inc_cum_over()
                        $ alexO.inc_cum_over()
                        show alexSteph fuck6 at center
                        "The girls both keep their mouthes open and tongues out as you climax, pulsing your loads out over their waiting faces. You do your best to spread your sperm around, spraying it over Stephanie first, then Alexia."
                        "When you're done you step back and admire your work. Alexia and Stephanie look at each other and smile."
                        steph "Mmm, you look good like that."
                        alex "You do too, it definitely suits you."
                        me "That felt amazing girls, thanks."
                        steph "It was our pleasure."
                        alex "Definitly our pleasure."
                        "They both take a deep breath and lean against each other for support."
                        me "Nora's going to be in for work soon, so you two should probably get cleaned up. I'm going to go for a walk and stretch my legs."
                        steph "Sure. Sounds good."
                        alex "Thanks for showing me around your lab [inputName], I had a lot of fun."
                        "You wave goodbye to the girls and leave them as they start to get dressed again. As you head upstairs you feel like you've had a [alexO.effect_string] impact on Alex and a [stephO.effect_string] impact on Steph today."

                $alexO.change_slut_rebalanced(action_difficulty)
                $stephO.change_slut_rebalanced(action_difficulty)
                $alexO.change_resist(lab_alex_steph_event_object.get_resist_change(5))
                $stephO.change_resist(lab_alex_steph_event_object.get_resist_change(5))
                $lab_alex_steph_event_object.inc_level(5)

            else:
                #reject scene
                if temp_alex < temp_steph:
                    #alex resists first
                    alex "Jesus [inputName], you're suppose to be at work, right?"
                    me "It's no big deal, right Steph?"
                    steph "Well... I mean, if Nora came in early we'd be pretty screwed."
                    alex "Yeah, I can't imagine your boss would be happy with us suddenly screwing each other in here."
                    "Alexia seems to be completely in control of herself again. You must have pushed her too far, and she's resisted the serum. Pushing her any further would only undo what progress you've made."
                    me "You know what, you're right. Forget I said anything, I don't know what I was thinking."
                    alex "Right... Can we just do something normal instead? Stephanie, how about you finish that tour for me?"
                    steph "I'd love to. Follow me..."

                else:
                    #steph resists first
                    steph "[inputName], I don't know if that woudld be a great idea. Nora could come in early today and we'd both be pretty screwed then."
                    alex "Oh, I didn't even think about that. Maybe we should do this some other time. I mean, it sounds fun, but not if you two are going to get fired."
                    me "Nora won't be in for hours, we'd be fine."
                    steph "It just doesn't feel worth the risk for me. Maybe some other time. How about I finish that tour for you instead Alexia?"
                    alex "That sounds great."
                    steph "Alright. Follow me then..."

                "Stephanie shows Alexia around the rest of the lab. When it's time for her next class you walk Alexia back up to ground level."
                "You say goodbye, and she starts walking towards the center of campus. You feel like you could have accomplished more here if you hadn't pushed the girls so far."
                $alexO.change_slut_failed()
                $stephO.change_slut_failed()
                $alexO.change_resist(lab_alex_steph_event_object.get_resist_change(0))
                $stephO.change_resist(lab_alex_steph_event_object.get_resist_change(0))
                $lab_alex_steph_event_object.inc_level(0)




    jump campusJumpTimeSkip
