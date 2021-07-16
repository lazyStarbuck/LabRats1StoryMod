##This file holds all of the minor scenes, sorted by the girl.


#######################
##Lily's Minor Scenes##
#######################

label min_sis_mast_1:
    "Lily bucks slightly as she hits something particularly sensitive."
    "She squeaks, then grabs a pillow and bites down on it. Her whole body is trembling from the effort of rubbing herself."
    "Your cock is wet with pre-cum, and you can feel an orgasm building quickly."
    show sis mast5 at right
    "Lily has both hands between her legs working as fast as they can, rubbing her clit and plunging inside her."
    show sis mast4 at right
    "Suddenly she tenses and lets out a little shriek through the pillow. Her thighs clamp down on her hands, and her whole body shakes. Then she slumps to the bed, spread out completely."
    "The sight suddenly brings you to the edge, and you put your hand over the tip and cum into it. Better that than leaving a stain on her door."
    "You step away from Lily's door slowly as her panting begins to slow down."
    $ sis_mast.inc_level(0)
    $ sisO.change_resist(-sis_mast.use_red(0,sisO.resist_score))
    return

label min_sis_mast_2:
    me "Hey sis. Need some help?"
    if sisO.slut_score > 35:
        #pics
        if sisO.exhib:
            sis "Oh, hey [inputName]. I thought I locked the door."
            "Lily moans again, fingers sliding in and out of her cunt slowly."
            me "I saw what was going on and thought I'd see if you needed some help."
            sis "Yeah, ah. That would be really nice. Thank you."
        else:
            sis "Oh, I thought I locked the door!"
            "Lily yells and goes to sit up."
            me "Don't worry, I'm just here to help if you'd like me to."
            "She pauses, on her knees and up on one hand. Her ass is still pointed towards you."
            sis "You'd do that for me? It's hard for me to get myself off sometimes without help."
        show sis mast3 at right
        "She bites her lower lip, then lowers her shoulders to the bed and looks away."
        me "No problem at all."
        "You step forward to the edge of the bed and take in the view."
        "She's dripping wet, you can see wet marks down her thighs where she's dripped."
        sis "Just a little bit, to help me finish."
        "You rub two fingers up and down her slit, getting them wet in her juices. She twitches slightly when you first touch her."
        "Next, you slide your two fingers inside slowly, curling and uncurling them gently."
        "Lily moans softly and presses her head into a pillow."
        "You slide in and out a few more times, then pull your fingers out and run them along the length of her vagina again."
        "Her breath is coming in ragged gasps. Her hands grasp at the sheets, pulling them up in bunches."
        "You run your two fingers to her clit, swollen and desperate for attention. She moans as you touch it, and leans into your hand."
        sis "Oh wow."
        "You rub your fingers rapidly over her clit."
        me "Does that feel good?"
        if sisO.anal:
            sis "So good, I just need a little more..."
            "You keep fingering your sister with one hand while you slide the other towards her ass. She gasps and shivers as you slip your thump inside of her tight butthole."
        else:
            sis "Oh wow. I'm getting close."
            "You speed up even more, thrashing your hand back and forth across the small bump."
            sis "Oh, oh, I'm close, I'm close!"
        "Lily leans heavily into your hand, and you have to place your other on her ass cheek to hold her up."
        sis "Yes, oh, yes yes yesyesyes!"
        show sis mast4 at right
        "She twitches violently, bucking against your hand once and then clamping down on it with her thighs. Her muscles quiver rapidly, and you have to pull a little to take your hand out."
        if sisO.slut_score > 60 or sisO.exhib:
            sis "Wow. Oh wow. We need to do this again [inputName]."
            "Lily slumps onto the bed, panting heavily. You get up and head out of the room, leaving her to her rapture."
        else:
            sis "Wow. oh wow."
            "Lily slumps onto the bed, panting heavily."
            sis "Thank you so much. We can't let anyone know what we did though."
            me "I promise my lips are sealed. That was fun sis."
            "She nods and rolls over."
            sis "Now get out of here before mom wonders what you're up to."
        $ sis_mast.inc_level(1)
        $ sisO.change_resist(-sis_mast.use_red(1,sisO.resist_score))

    else:
        sis "Oh, I thought I locked the door!"
        "Lily rolls off the bed suddenly."
        me "It's okay sis, I thought I could..."
        sis "Get out of here! I can't believe you saw that!"
        "She runs at you and pushes you out the door. You hear the lock click behind you."
        "That could have gone better."
    return

label min_sisPeep:
    "You crack your sister's door open and are about to say something..."
    $ tempInt = -1
    show sis bend1 at right
    with fade
    sis "Damn it, where did it go?"
    "She's searching under her desk for something."
    sis "How far could it roll?"
    "You've got a great look at her thighs and ass as she leans over. Just a little bit more and you could tell what kind of underwear she's wearing."
    if sisO.slut_score > 15:
        $ tempInt = 0
        sis "Just a little farther..."
        "Lily leans over farther, digging for something behind the desk."
        show sis bend2 at right
        menu:
            "You've seen enough. Retreat before you get caught.":
                "Alright, it's time to get out of here."
            "Knock on the doorframe.":
                if sisO.slut_score > 25:
                    $ tempInt = 1
                    "She turns her head around to look at you, but stays bent over reaching for something."
                    sis "Hey, what's up."
                    me "Not much, enjoying the view."
                    "Lily smiles slyly. Her left hand brushes against her thigh, then up to her ass, bringing her skirt with it."
                    show sis bend3 at right
                    sis "How about now?"
                    me "Perfect."
                    if sisO.slut_score > 80 or sisO.freeuse:
                        sis "Perfect? Wouldn't it look better covered in cum?"
                        show sis bend4 at right
                        "She reaches down and pulls her panties to the side and wiggles her ass at you."
                        menu:
                            "Fuck her.":
                                $ tempInt = 2
                                me "That's a good point, we'll have to do something about that."
                                show sis fuck6 at right
                                $ sisO.inc_sex()
                                "Lily smiles and braces herself with her hands on her thighs. You step up behind her and slip your pants down, flopping your cock onto her ass."
                                sis "Oh, it's already so big."
                                me "That's because you were teasing me. Now it's my turn."
                                "You grip your shaft and slide the tip along Lily's pussy a few times. She twitches a little as you flick past her clit, and before long she's dripping wet."
                                sis "Please [inputName]? Can you fuck me now?"
                                "You give her ass a slap, grab ahold of her hips, and thrust into her pussy as deep as you can."
                                me "If that's what you want, slut."
                                sis "Fuck! Oh fuck!"
                                "You waste no time, pumping your hard cock into your sister. You have to hold onto her hips hard with each thrust to stop her from falling forward."
                                me "Give me your arms Lily."
                                show sis fuck7 at right
                                "You pause for a moment so Lily can get her footing back and move her arms behind her. You let go of her waist and grab her by the wrists, pulling on them to arch her back up a little."
                                "Then you resume fucking her, pulling her back onto your cock with each thrust so you can get a little deeper."
                                "The sound of your hips hitting her ass and her loud moaning echoes around the room."
                                me "You feel great sis, are you ready for your reward?"
                                if sisO.cumslut:
                                    sis "Yes, please! Give me your cum [inputName], I want it so badly!"
                                else:
                                    sis "Uh huh! I'm ready!"
                                "You pump into her a few more times, then pull out and stroke your shaft."
                                show sis fuck8 at right
                                $ sisO.inc_cum_over()
                                "Lily leans forward and plants her hands on her desk, ass high in the air while you cover her cheeks with cum."
                                me "There it is!"
                                "Lily pants while you flick the few last drops onto her. You step back and enjoy the view for a moment."
                                me "Now that's perfect. A perfect house slut, covered in my cum."
                                if sisO.cumslut:
                                    sis "It's so warm... It feels so nice."
                                    "She stumbles forwards a few steps and collapses onto her own bed, ass up."
                                else:
                                    "Your sister doesn't say anything, but stumbles forward a few steps and collapses onto her bed ass up."
                                    sis "Oh fuck."
                                "You pull your pants back up and head out of the room, leaving Lily to clean herself up."
                                return True

                            "Leave her alone.":
                                me "It definitely would. I've got some stuff to do though, I'll have to take a rain check."
                                "Lily pouts but nods."
                                sis "Don't keep me waiting too long, okay?"
                                "You nod and head off."
                    else:
                        "She laughs and goes back to reaching behind her desk. You spend a few minutes watching her, enjoying the way her tits dangle and ass bounces when she reaches farther."
                        "Eventually she finds what she's looking for, and you head out of the room."
                else:
                    sis "What? Ow!"
                    show sis casual1 at right
                    "She jerks her head up, hitting it on the bottom of the desk."
                    sis "Son of a bitch!"
                    "She doesn't look happy now, and you don't have anything to say to her."
                    me "You okay?"
                    "Lily sits down on her bed, hand cradling her head."
                    sis "Ya, I'll be fine. Give me a few minutes, would you?"
                    me "Sure."

    else:
        sis "Aha! There it is!"
        "Having found her prize, Lily begins standing up and you beat a hasty retreat."
    if tempInt == 0:
        $ sis_peek.inc_level(0)
        $ sisO.change_resist(-sis_peek.use_red(0,sisO.resist_score))
    elif tempInt == 1:
        $ sis_peek.inc_level(1)
        $ sisO.change_resist(-sis_peek.use_red(1,sisO.resist_score))
    elif tempInt == 2:
        $ sis_peek.inc_level(2)
        $ sisO.change_resist(-sis_peek.use_red(2,sisO.resist_score))
    return False

label min_sisinterruptPorn:
    show sis casual1 at right
    sis "Hey [inputName], do you have a USB Cab..."
    "You spin your chair around as the door is opened suddenly. You lock eyes with Lily. Your dick is still in your hand and some girl is getting pounded on the screen behind you."
    if sisO.slut_score < 10: #Is startled
        me "Hey, ah!"
        sis "Oh shit!"
        "Lily turns around and pulls the door shut. It slams closed suddenly."
        me "Crap, sorry Lily!"
        "She talks through the door, her voice muffled."
        sis "Ugh, some things you can't unsee!"
        me "Well you should have knocked then!"
        sis "Can't you remember to lock your door or something when you're... having some me time?"
        "Having lost all interest in jerking off, you close everything down and wipe your hand off."
        me "I forgot, alright? Just, knock next time."
        sis "Hopefully there won't be a next time. Now do you have a USB cable?"
        "You rummage around your room for a while before finding the cable. You open the door a crack and slide it out."
        me "Here."
        sis "Thanks. Have fun I guess."
        "She heads off back to her room. Your heart is still beating fast, and you definitely don't feel like finishing up now."
        $ sis_porn_catch.inc_level(0)
        $ sisO.change_resist(-sis_porn_catch.use_red(0,sisO.resist_score))

    elif sisO.slut_score < 40: #Does nothing, not surprised
        me "Oh, hey."
        sis "I didn't realise you were busy. Want me to come back later?"
        me "No, it's fine. What's up?"
        "You keep stroking yourself while you look at Lily in the doorway."
        sis "I need a USB cable, do you have a spare one hanging around?"
        me "I think so. Come on in, I think it's beside my bed. I'm a little busy though."
        sis "Don't worry about it, I can grab it myself."
        "Lily closes the door behind her and walks over to your bed. You turn back to your monitor as the girl is fucked doggy style."
        sis "Here it is!"
        "She glances over your shoulder at your monitor too."
        sis "Wow, nice."
        me "I know, right?"
        sis "Thanks for the cable, have fun."
        me "No problem. Close the door on your way out."
        "Lily does so, and you finish yourself off a little while later."
        $ sis_porn_catch.inc_level(1)
        $ sisO.change_resist(-sis_porn_catch.use_red(1,sisO.resist_score))

    elif sisO.slut_score < 70: #Gives you a blowjob
        me "Oh, hey Lily."
        sis "Hey, do you have a moment?"
        "You keep stroking yourself while you look at Lily."
        me "Well I'm a little busy. What do you need?"
        sis "I need a USB cable. Do you have one lying around?"
        me "I might, but I'm not sure where I left it."
        sis "Could you take a break? I kind of need it quickly."
        me "I just got settled in though. If I stop now I have to start all over. Just come over here and help me finish."
        "Lily steps into the room and closes the door."
        sis "Fine, what do you need me to do?"
        me "Just get on your knees and suck me off."
        show sis blow1 at right
        $ sisO.inc_blow()
        "She nods and kneels in front of you. She takes your cock in her hand and licks the tip a few times. Then she slips you into her warm mouth."
        me "Perfect, just like that."
        "Lily bobs her head up and down, taking your shaft as deep as she can."
        "Before long you're ready to cum."
        me "I'm almost there Lily!"
        if sisO.slut_score > 60 or sisO.cumslut:
            "Lily speeds up her blowjob for a few strokes, then pulls off and rubs you as fast as she can. She strokes your wet shaft while you cum, blowing your load over her face."
            show sis blow2 at right
            $ sisO.inc_cum_over()
            if sisO.cumslut:
                sis "Mmm, thank you [inputName]."
                "She rubs your semen around a little, spreading it over her cheeks."
            else:
                sis "Wow."
            me "Damn, good job."
        else:
            "Lily speeds up her blowjob for a few strokes, then pulls you off and rubs you until you start cumming. She points your tip to the side so you fire your load past her onto the floor."
            me "Damn that felt good."
            sis "Good, glad I could help."
        "She smiles and stands up."
        sis "Now, where's the cable?"
        "You get up and pull the USB cable out from a drawer and hand it over."
        sis "Thanks, I'll bring it back later."
        "She ducks out the door while you take a moment to get cleaned up."
        $ sis_porn_catch.inc_level(2)
        $ sisO.change_resist(-sis_porn_catch.use_red(2,sisO.resist_score))

    else: #Fucks you like the video
        me "Hey Lily, what's up?"
        sis "Hey, have a moment?"
        "You keep stroking yourself."
        me "I'm kind of in the middle of something. Come in."
        "Lily steps into your room and closes the door."
        sis "I need a USB cable, do you have one lying around?"
        me "I might. I'm going to need to get off before I have time to look for it though."
        sis "Well, I need that cable soon. How about I help you out with that?"
        show sis fuck1 at right
        $ sisO.inc_sex()
        "She walks to your desk beside you and bends over, pulling her dress up and panties to the side."
        me "Wow, someone knows what I like."
        sis "Don't just sit there then, come fuck me!"
        "You stand up and get behind Lily. She grips the far side of the desk as you press your tip against her already wet pussy."
        "She moans softly as you rub your tip against her clit, then gasps as you thrust inside. You settle into a regular rhythm pumping her pussy from behind."
        me "Do you like that sis?"
        "Lily nods and gasps a little as you fuck her harder."
        me "Good. I like keeping my slut of a sister happy."
        sis "I'm so happy right now! I love being your slut."
        "You give her ass a resounding slap and her pussy tightens up around your shaft."
        sis "Ah! Fuck!"
        me "That's a good little whore. I'm almost ready to cum."
        if sisO.slut_score > 85 or sisO.freeuse:
            sis "Hurry! I want your load inside me!"
            me "Ya? You want to be my cum dumpster?"
            if sisO.cumslut:
                if sisO.preg_response_ok():
                    sis "God yes, that's all I want. Please [inputName]? Please cum inside me. I want you to try and get me pregnant!"
                else:
                    sis "God yes, I just... I hope today is a safe day!"
            else:
                sis "God yes, I'll be whatever you want me to be if you just keep going like that!"
            "You lean into her as you start to release and press your tip as far up her pussy as it will go. She moans and twitches as you fill her up, then goes limp over your desk."
            me "Fuck that felt good!"
            show sis fuck2 at right
            $ sisO.inc_cum_inside()
            "You pull out and watch as your cum leaks out and starts to run down her leg. Lily just pants, bent over your desk for awhile. Finally she stands up."

        else:
            sis "Good! I want you to cum over my ass. Cover me with your load!"
            me "Do you like being covered in my cum? Does that turn you on?"
            if sisO.cumslut:
                sis "I love it so, so much [inputName]!"
                "Lily moans loudly as you fuck her, pussy quivering around your shaft. When you're ready you pull out and stroke your cock while you fire your load onto her ass. She gasps and twitches as each warm pulse lands on her."
            else:
                "Lily nods and moans while you fuck her. When you're ready you pull out and stroke your cock while you fire your load onto her ass. Lily gasps and twitches as each warm pulse lands on her."
            show sis fuck3 at right
            $ sisO.inc_cum_over()
            "When you're done you step back and admire your handiwork. Lily just pants for awhile, bent over your desk. Finally she stands up."

        sis "Do you have that cable?"
        me "Right. Here."
        "You grab the USB cable from a drawer and throw it to her. Lily smiles and heads for the door."
        sis "Thanks, I owe you one."
        $ sis_porn_catch.inc_level(3)
        $ sisO.change_resist(-sis_porn_catch.use_red(3,sisO.resist_score))
    return

label min_sis_search_room:
    if sisO.slut_score < 10: #Just her underwear, nothing fancy
        "You dig through Lily's drawers, careful to memorize where everything was so you can put it back."
        "After a few minutes of searching the only things you've turned up are a few extra pairs of underwear, all either white or pink and conservatively cut."
        "With nowhere else to search you carefully refold it and put it back. You leave the room and close the door behind you again."
        $ sis_search_room.inc_level(0)
        $ sisO.change_resist(-sis_search_room.use_red(0,sisO.resist_score))

    elif sisO.slut_score < 30: #Some sexy lingerie.
        "You dig through Lily's drawers, careful to memorize where everything was so you can put it back."
        "After a few minutes all you've found are a few extra pairs of underwear, all either white or pink and conservatively cut."
        "You search her closet next, and find a box placed on the shelf above. When you pull it down and open it up, you find it's full of lacy lingerie."
        "Two sets stand out to you. One is a thin black lacy bra and panty set. The edges are a little worn from being washed, so she must have worn it a few times already."
        "The other is a white corset and matching panties. They look completely untouched, but are folded neatly at the bottom."
        "You don't find anything else of interest in the room, so you put everything back where you found it and close the door behind you as you leave your sister's room."
        $ sis_search_room.inc_level(1)
        $ sisO.change_resist(-sis_search_room.use_red(1,sisO.resist_score))

    elif sisO.slut_score < 60: #A vibrator, plus all of the above.
        "You dig through Lily's drawers, but only find her normal underwear. You search the closet next, and find a box placed on the shelf above. When you pull it down and open it up, you find it's full of lacy lingerie."
        "Two sets stand out to you. One is a thin black lacy bra and panty set. The edges are a little worn from being washed, so she must have worn it a few times already."
        "The other is a white corset and matching panties. They look completely untouched, but are folded neatly at the bottom."
        "Beside the white corset, tucked along the side of the box, is a pink penis shaped vibrator. You pick it up and find a small battery indicator, which shows that it's half full."
        if sisO.freeuse and not sisO.cumslut:
            "At the very bottom of the box there are a few strips of condoms. A quick count reveals that a few of them are missing."
        "You search the rest of the room but don't find anything of interest. You place everything back where you found it and close the door behind you as you leave your sister's room."
        $ sis_search_room.inc_level(2)
        $ sisO.change_resist(-sis_search_room.use_red(2,sisO.resist_score))
    else: #Vibrating panties, partly low on batteries.
        "You dig through Lily's drawers, but only find her normal underwear. You search the closet next, and find a box placed on the shelf above. When you pull it down and open it up, you find it's full of lacy lingerie."
        "Three sets stand out to you. One is a thin black lacy bra and panty set. The edges are a little worn from being washed, so she must have worn it a few times already."
        "The other is a white corset and matching panties. They look completely untouched, but are folded neatly at the bottom."
        "Beside the white corset, tucked along the side of the box, is a pink penis shaped vibrator. You pick it up and find a small battery indicator, which shows that it's half full."
        "The last set is a plain black set with a bulge in the middle. You pick it up, unfold it, and find a small remote. Using the remote brings a sharp buzz from the panties in your hand."
        if sisO.freeuse:
            if sisO.cumslut and not sisO.anal:
                "At the very bottom of the box you find a small cardboard container, a five pack of pregnancy tests with a single test remaining. If this is all of Lily's sex stuff, there's a conspicuous lack of condoms."
            else:
                "At the very bottom of the box you find a cardboard box, filled with condoms. Lily seems to have a bunch of different kinds: ribbed, flavoured, extra-thin."
        "You do a quick search of the rest of the room but don't find anything of interest. You place everything back where you found it and close the door behind you as you leave."
        $ sis_search_room.inc_level(3)
        $ sisO.change_resist(-sis_search_room.use_red(3,sisO.resist_score))
    return

label min_sis_search_computer:
    "Lily should really leave her computer locked. You spend a few minutes searching her computer."
    if sisO.slut_score < 10: #Just talking to a boy
        "She's spent the last few days having a facebook conversation with a guy. Looks like they met on campus and have been hanging out."
        "Everything's pretty tame, and it doesn't look like he's had the courage to ask her out yet on a proper date."
        "Unable to find anything else interesting you head out."
        $ sis_search_comp.inc_level(0)
        $ sisO.change_resist(-sis_search_comp.use_red(0,sisO.resist_score))

    elif sisO.slut_score < 30: #Sent a nude to a boy
        "Lily's been talking a lot with a guy on facebook. By the looks of it she got a little frisky last night."
        show sis strip4 at right
        "She sent him a picture of herself naked, hiding her tits in her hands."
        "You browse around, but don't find anything else that's interesting. You close everything and leave her room as you found it."
        $ sis_search_comp.inc_level(1)
        $ sisO.change_resist(-sis_search_comp.use_red(1,sisO.resist_score))

    elif sisO.slut_score < 50 or not sisO.freeuse: #Pics of herself masturbating, for the boy. Any higher requires public
        "You find a few interesting things in her search history. It looks like she's either started watching porn or stopped clearing her history after."
        if sisO.slut_score > 80 and not sisO.freeuse:
            "Checking her facebook page you find she's been talking to a guy for a while. They had a date planned soon, but Lily called it off."
            "Lily just sent him a message last night: \"I'm sorry I have to say this. There's someone else in my life I love very much, and I don't think we should see each other any more. I hope you are able to understand.\""

        else:
            "You find a few interesting things in her search history. It looks like she's either started watching porn or stopped clearing her history after."
            "Checking her facebook page you find she's been talking to a guy for a while. He mentioned feeling lonely last night, so Lily sent him a picture to help out."
            show sis mast1 at right
            "You spend a while enjoying the picture yourself too. It looks like your sister was really having a good time."
        "When you're ready you close up everything and leave her room as you found it."
        $ sis_search_comp.inc_level(2)
        $ sisO.change_resist(-sis_search_comp.use_red(2,sisO.resist_score))

    elif sisO.slut_score < 70: #Blows the boy and swallows for him
        "You find some interesting searches in her history. On a few porn sites she's been looking for \"Deepthroat\" and \"Dominated\", almost every night."
        "Her facebook page is logged in, and you find a few messages waiting for her from a guy."
        show sis blow3 at right
        "He writes \"Here's the picture you wanted from last night.\", and has an image attached. It's Lily on her knees looking up at the camera with a mouth full of cum."
        if sisO.cumslut:
            "Then he continues: \"It was super cute the way you begged for it. I'll save up plenty of cum for you next time sweety.\"."
        else:
            "Then he continues: \"And it was super hot when you swallowed. Lets do this again some time.\"."
        "When you're done staring at the picture you close everything and leave her room as you found it."
        $ sis_search_comp.inc_level(3)
        $ sisO.change_resist(-sis_search_comp.use_red(3,sisO.resist_score))

    else: #Fucks the boy and his friends, lets them finish all over her.
        "It doesn't take long to find some interesting search terms in Lily's browser, like \"Facefuck\" and \"Brother Fuck\". She's even favorited a few porn sites and pinned them to her startup page."
        "Her facebook profile is logged in, and there are some new private messages from a few different guys. One reads \"Thanks for helping out last night Lily, you should come over for poker night more often.\""
        show sis fuck5 at right
        "Then a picture. Lily's on her back on a poker table, cards and chips swept aside, and covered in cum. She's smiling at the camera while cum drips off her tongue and leaks out of her pussy."
        "The other messages all seem to be from other guys, telling her what a great time they had last night during the poker game."
        "You read through them for a while and enjoy the picture, then close everything and leave the room as you found it."
        $ sis_search_comp.inc_level(4)
        $ sisO.change_resist(-sis_search_comp.use_red(4,sisO.resist_score))
    return

label min_sis_sleep:
    me "Okay, I don't mind as long as you aren't keeping me up all night. It's a small bed though, we're going to have to be close."
    sis "That's okay. Thank you so much."
    "Lily closes the door behind you and slips under the covers next to you."
    "After a few minutes of tossing and turning it's clear there isn't enough space for both of you to sleep separately."
    show sis sleep1 at right
    "You roll onto your side and put your arm around Lily, pulling her close so you can spoon."
    if sisO.slut_score < 45: #Light cuddling
        sis "Hey!"
        me "There isn't much room on the bed Lily. If you want to sleep in here we're going to have to be close to each other."
        "Lily thinks for a moment, then nods and pulls closer to you. You wrap an arm around her torso, ending up with one hand cupping a boob."
        sis "Comfortable?"
        me "Ya, that feels good. Goodnight Lily."
        sis "Goodnight [inputName]."
        "You both drift off to sleep cuddling with each other. Early in the morning Lily wakes up and slips out of your arms to head back to her own room."
        $ sis_sleep.inc_level(0)
        $ sisO.change_resist(-sis_sleep.use_red(0,sisO.resist_score))

    elif sisO.slut_score < 85: #Heavy fondling and getting her off.
        sis "Oh, hey there."
        me "There isn't much room on the bed, so we're going to have to get nice and close."
        sis "You're right. In that case..."
        show sis strip1 at right
        "Lily slips out of your arms and stands up, pulling her pajamas off and leaving them in a pile. When she's down to just her panties she slips back in and slides against you."
        sis "I don't want to get too hot, if we're right next to each other."
        show sis sleep2 at right
        "She pulls your arm around her again, planting your hand firmly on one of her naked tits. While she's getting comfortable she also rubs her ass up and down against your hard cock."
        me "Easy there Lily, or I'm going to have to repay the favour."
        "You pinch her nipple between a finger and thumb and she gasps."
        me "Or maybe that's what you want, right? To be played with?"
        "You slip your other hand down her legs, rubbing the inside of her thighs."
        sis "No, I just couldn't sleep and want to be comfortable."
        "Lily moans while you play with her tits, then gasps again when you rub a finger between her legs along the length of her pussy."
        me "You're already wet though. You aren't fooling me, you want to be used like a good little slut."
        show sis sleep3 at right
        "You pull her panties to the side and slip two fingers inside her, causing her to moan and arch her back a little bit."
        sis "No, I just... ah..."
        me "Don't say a word, I'll take care of you."
        "You knead your sister's breast with one hand while you finger her with the other. She was already wet when you slid your hand down, and now she's completely soaked."
        "Lily pants and moans, gasping any time your fingers brush against her clit. After a few minutes you feel her thighs start to tighten up around your hand."
        me "Are you getting close?"
        sis "Lily whimpers and nods, legs clenching up."
        "You finger her faster for a while, then pull out and rub her clit as fast as you can with two fingers."
        "Lily tenses up, curling into a ball and moaning loudly. Her breathing comes in short gasps for a few moments while you keep playing with her through her orgasm."
        show sis sleep2 at right
        "Finally you stop and let her recover. She straightens out on the bed again and pushes herself back against you."
        me "Was that good?"
        sis "Mmhm. Thank you."
        me "Good. Now lets get to sleep."
        "You hold Lily next to you as you both drift off to sleep. Early in the morning Lily wakes up and slips out of your arms to head back to her own room."
        $ sis_sleep.inc_level(1)
        $ sisO.change_resist(-sis_sleep.use_red(1,sisO.resist_score))
    else: #Fuck her spoon style.
        "Lily sighs and snuggles closer to you."
        me "You're going to get really hot in all that if we're both sharing the bed Lily."
        show sis sleep4 at right
        $ sisO.inc_sex()
        "Lily nods and slips out of your arms. She quickly strips out of everything, including her panties, then slides back into bed."
        sis "Is this better?"
        me "Much."
        "You slip an arm around her chest and grab hold of a tit, then grind your hips against her ass a little bit."
        "Lily just lays next to you and moans softly while you play with her."
        "After a few minutes you slide your pants down and pull your cock out."
        me "You've got me all worked up Lily. We're going to have to take care of this before I can get to sleep."
        sis "I'm sorry. Do whatever you want, It's my fault anyway."
        "You slip your cock between her legs and run the tip along her pussy. Lily moans softly, but stays perfectly still for you."
        me "That's a good girl, stay just like that until I'm finished."
        "Once you've gotten your tip wet from her juices you slide all the way into your sister."
        if sisO.exhib:
            "Lily gasps the first few times you pump into her, then starts to let out some loud moans. You pinch her nipple and roll it between your fingers while you fuck her."
            me "Easy there sis, you're going to wake mom up if you keep that up."
            sis "Ah, fuck! I don't care, we'll deal with that later. Just keep going!"
        else:
            "Lily gasps the first few times you pump into her, but before long the only noise she's making are soft moans. You pinch her nipple and roll it between your fingers while you fuck her."
        "With her legs together Lily's pussy is incredibly tight, and within a few minutes you're ready to finish."
        "You pump faster, bumping your hips into her ass each time, then begin to fire your load inside of her."
        $ sisO.inc_cum_inside()
        if sisO.cumslut:
            sis "Oh god, yes! Fill me up!"
            "Lily quivers with pleasure, suddenly climaxing at the same time as you."
        else:
            "Lily gasps in surprise, but still doesn't move."
        show sis sleep5 at right
        "You hold yourself tight against her, then give a few final thrusts before pulling out. Lily sighs as you slip out of her, going limp against you."
        me "Good job Lily. Now we can get to bed."
        if sisO.preg_response_ok():
            "Lily nods and cuddles closer to you. You fall asleep together, your cum dripping slowly out of her pussy."
        else:
            sis "We have to be more careful in the future [inputName], that or I need to start taking my birth control again. Eventually you're going to get me pregnant like this..."
            "Lily cuddles closer to you. You fall aslep together, your cum dripping slowly out of her pussy."
        "Lily wakes up early in the morning and slips out of your arms to head back to her own room and get cleaned up."
        $ sis_sleep.inc_level(2)
        $ sisO.change_resist(-sis_sleep.use_red(2,sisO.resist_score))
    return

label min_sis_video_game:
    sis "Hey, aren't you suppose to be at work?"
    if sisO.slut_score < 30:
        show sis casual1 at right
        "You turn around, startled by your sister. She's standing by your door, leaning against the door frame."
        me "I'm taking the day off."
        sis "You're going to waste the whole summer playing games. Why don't you take up a hobby, play a sport? Something."
        me "You just want me out of the house, don't you. Annoyed that your stuck spending time with your brother?"
        sis "Pfh, as if. Have fun blasting aliens or terrorists or whatever it is you're doing."
        "She slips back into the hallway, closing the door behind her."

    elif sisO.slut_score < 60:
        # Watched what you're playing, makes a bet that you win. Jerks you off as a reward. (different cum spots depending on relative high or low score)
        show sis casual1 at right
        "You turn around, startled by your sister. She's standing by your door, leaning against the door frame."
        me "I'm taking the day off."
        sis "You're going to end up wasting the whole summer playing games. You'd think you'd at least be better by now."
        "She comes over and leans on the back of your chair while you play, watching over your shoulder."
        me "And I'm sure you could do better. Games like this take years of practice, Lily. Years."
        sis "Uh, huh. Riiiight."
        me "Fine, I'll make you a bet then."
        "You back out to the menu of the game you're playing and kick the difficulty up to it's max."
        me "I'll clear the level in five minutes. Par is normally nine."
        "Lily thinks for a moment, then nods."
        sis "Fine. When you lose I want fifty bucks, so I can get some new makeup."
        me "And when I win, I want you to give me a handjob."
        "Lily thinks about it for a moment."
        sis "Deal. Hope you've got the cash on you."
        "You get comfortable in your chair, hands ready on your keyboard and mouse, and start the level. Lily peers over your shoulder watching closesly while you play."
        "You're a little out of practice, but this game made up the formative years of your childhood. You know it forwards and backwards, and could beat it in the dark."
        sis "Shit. Yes! Get him! Wait, fuck!"
        "You clear the level, a few seconds to spare. Lily groans behind you, planting her forehead on the back of your chair."
        me "And there we go. I'll be holding onto my cash for today, and you'll be holding onto this."
        "You pull your pants down and let your cock spring free."
        sis "Yeah, yeah. Lets get this over with."
        show sis hand10 at right
        $sisO.inc_hand()
        "You spin your chair around and lean back while Lily gets onto her knees in front of you. She takes a hold of your shaft and strokes it gently a few times, getting a feel for it."
        me "Oh yeah, that feels great."
        "Lily is silent for a few minutes while she jerks you off. She picks up speed as she gets more comfortable, and your precum has your shaft lubricated relatively soon."
        sis "Oh, I feel yo twitching. Are you going to cum soon?"
        me "Yeah, keep going!"
        if sisO.slut_score < 45 and not sisO.cumslut:
            "Lily keep stroking you off, shuffling to the side so she's clear of your firing arc. You tense up and grip the edge of your chair as you climax."
            sis "Wow..."
            "Your load sprays out in pulses past Lily's shoulder and onto the floor. The last few drops dribble down onto her hand."
            me "Ah... thanks sis. If you want to take that bet again let me know."
            show sis casual1 at right
            "Lily carefully lets go of your shaft and wipes her hand on her dress."
            sis "We'll see. You can't get lucky all the time, right?"
            me "Only one way to find out."
            "Lily gets up and leaves your room, closing the door behind her. You turn back to your game, feeling much more relaxed."
        else:
            "Lily keeps stroking you off, angling your tip down so it's pointing towards her cleavage. You tense up and grip the edge of your chair as you climax."
            sis "Ah!"
            show sis hand11 at right
            $ sisO.inc_cum_over()
            "Your load sprays out in pulses onto Lily's tits and chest, running down between her breasts and soaking into her dress. The last few drops dribble down onto her hand."
            me "Ah... thanks sis. If you want to make another bet and get another coating just let me know."
            "Lily lets go of your shaft and wipes her hand on her dress."
            sis "We'll see. You can't get lucky all the time, right?"
            me "Perfect record so far."
            "Lily gets up and leaves your room, closing the door behind her. You turn back to your game, feeling much more relaxed."
        $ sis_videogame.inc_level(0)
        $ sisO.change_resist(-sis_videogame.use_red(0,sisO.resist_score))

    elif sisO.slut_score < 85:
        # whatched what you're playing, bets you can't play while she blows you. Success you cum on her face, fail you cum down her throat.
        show sis strip19 at right
        "You turn around, startled by your sister. She's standing by your door, leaning against the frame. She's only wearing a white dress shirt and a small set of black panties."
        me "I'm taking the day off. Just walking around half dressed now?"
        sis "You and Mom are normally both gone by now. It's comfortable. Sue me."
        "She comes over and leans on the back of your chair while you play, watching over your shoulder."
        sis "Oh come on, you can do better than that. I hope I'm not distracting you."
        me "You'd have to be doing a lot more than just standing there to distract me."
        sis "Oh yeah? Alright then, lets test that. Slide back a little bit."
        "Lily drops to her knees and positions herself in front of you, partly under your desk. She rests her hands on your thighs, rubbing them slowly."
        sis "You just do your best to finish that level. I'll try and finish you."
        show sis blow20 at right
        $sisO.inc_blow()
        "She giggles and pulls your pants down a little, far enough for your hard cock to spring up. Without waiting a second she leans foward and licks it from base to tip, sending shivers up your spine."
        me "Oh shit..."
        sis "Already having trouble? This is going to be easier than I thought."
        "She kisses the tip of your cock, then slides down onto it. Her tongue works up and down your shaft while she blows you."
        "You keep your focus, clearing your way through the level you're on. Lily's blowjob is certainly doing it's job though, and you feel your orgasm building."
        menu:
            "Focus! You can do this!":
                me "Fuck, ah..."
                "You tighten up your core, trying to hold off your climax. Lily moans something and blows you faster, sensing how close you are."
                "You're almost done, and for a few desperate seconds you maintain control of yourself. When the last enemy falls you let go of your keyboard and mouse and grab Lily's head."
                me "Done! Come here!"
                "You slide your chair back, pulling your cock out from her throat with a wet pop."
                if sisO.cumslut:
                    sis "That's it, give me that hot cum!"
                else:
                    sis "Ah! Give it to me!"
                show sis blow22 at right
                $sisO.inc_cum_over()
                "You hold her head in place with one hand, fingers wrapped in her hair, while you stroke your shaft with the other. She gasps loudly as you pulse your hot load onto her face."
                "When you're done you let go of her hair and sit back, exhausted. Lily waits on the floor for a few more moments, then stands up and wipes some of your cum away from her eyes."
                if sisO.cumslut:
                    "She licks her fingers clean, savouring the tast of your sperm."
                me "See, told you I could do it."
                sis "I guess you were right. Good job."
                "She takes a few more deep breaths."
                sis "I'm going to go get cleaned up. I'll see you later."

            "Fuck it, give up and cum down her throat!":
                me "Oh fuck!"
                show sis blow21 at right
                $sisO.inc_cum_mouth()
                $sisO.inc_cum_swallow()
                "You lean back, letting go of your mouse and keyboard, and start to climax. Lily gasps in suprise as you fire your load with your cock still half way down her throat."
                "Lily pulls back a little bit, but waits until you've emptied your balls into her stomach before she comes off your shaft entirely."
                sis "Ah... Ah..."
                me "Sorry Lily. I guess you were right."
                if sisO.cumslut:
                    sis "Whatever, I just wanted to drink down your cum. I think there's still a little left here..."
                    "Lily leans back towards you and starts to run her tongue along the sides of your cock until she's satisfied she's gotten every last drop."
                else:
                    sis "Yeah, I guess I was. Wow, that was really... thick."
                show sis strip19 at right
                "She swallows, then takes a few deep breaths. Once she's recovered she climbs out from under your desk and stands up."
                sis "I'm going to go get a drink. I'll see you later."

        "Lily leaves your room, closing the door behind her. You turn back to your game, feeling much more relaxed."
        $ sis_videogame.inc_level(1)
        $ sisO.change_resist(-sis_videogame.use_red(1,sisO.resist_score))

    else:
        # whatches you play, bets you can't play while she fucks you. Success you cum in her mouth, fail you cum inside of her.
        show sis strip20 at right
        "You turn around, startled by your sister. She's standing by your door, leaning against the frame. She's not wearing anything at all."
        me "I'm taking the day off. Just walking around naked now?"
        sis "You and Mom are normally both gone by now. What's the harm?"
        "She comes over and leans on the back of your chair while you play. You can feel her breasts press up against your back."
        sis "I hope I'm not distracting you."
        me "I don't mind. You can try and distract me as much as you want."
        sis "Oh, is that so?"
        show sis fuck34 at right
        $ sisO.inc_sex()
        "She swings herself around your chair, straddling you. Her naked pussy grinds up against your hard cock through your pants."
        me "Go on, give it your best shot. I'm finishing this level no matter what you do."
        "She bites her lip and reaches down to your pants, pulling your zipper down. Soon she has your cock out, tip rubbing against her cunt."
        "She gasps into your ear when she finally slides on, taking your full shaft inside her. She's tight and wet, the feeling sending shivers up your spine."
        sis "[inputName]... Ah..."
        show sis fuck35 at right
        "Lily works her hips up and down, wrapping her arms around your back while she rides you. You do your best to stay focused on the task at hand, but her pussy is hard to ignore."
        "A few minutes later you've almost finished your level, and Lily almost has you climaxing."
        menu:
            "Focus! Just a little longer!":
                me "Ah! Fuck..."
                "You tighten your core, trying to hold off your climax. Lily moans and pumps her hips faster, sensing how close you are."
                if sisO.anal:
                    sis "I bet... this will do it..."
                    "Lily pulls off your cock for a split second, reaching between her legs to reposition it while she pants madly."
                    "You're taken by suprise when she sits down again, plunging your cock deep inside of her ass."
                    me "Oh fuck me Lily! Wait!"
                    "Lily half moans, half screams as she works her hips up and down, sliding you in and out of her impossibly tight butt. The feeling is amazing, and you're driven over the edge before you can finish the level."
                    "You abandon the game, wrapping your arms around your sister and pulling her close to you as you climax."
                    if sisO.cumslut:
                        sis "I win! Ah, give me my reward! Fill me up with your thick cum! Ah!"
                    else:
                        sis "Yes! Ah... I... Win!"
                    $ sisO.inc_cum_inside_ass()
                    show sis fuck36 at right
                    "You both stay still for a few minutes, long after you've finished dumping your load into your sister. When she finally has the strength Lily stands up, letting your flacid dick slip out of her."
                    me "Damn, that felt amazing."
                    "Lily nods weakly, cum smeared over her pussy and dripping down her leg."
                    sis "I knew you couldn't do it."
                    me "I guess you were right. Well done Lily."
                    sis "I'm going to go get cleaned up, I'll see you later."
                else:
                    "A few desperate seconds later and you've finished the level. You grab Lily's hips and lift her up, your cock slipping out of her drenched cunt."
                    me "Done! Now it's my turn, I want you to swallow it all for me."
                    "Lily moans and drops to her knees in front of you, looking up at you with her mouth open. You place the tip of your cock on her lips and stroke yourself off."
                    "You finally orgasm, pumping your load into your little sisters waiting mouth."
                    me "There we go, good girl. Very good."
                    show sis fuck37 at right
                    $sisO.inc_cum_mouth()
                    $sisO.inc_cum_swallow()
                    "When you're done you sit back, cock still resting on Lily's chin. She looks up at you with her mouth open, show you your own cum."
                    me "Good, now drink it all down for me."
                    "She nods and closes her mouth. She swallows a few times, then opens up again to show that it's all gone."
                    sis "Wow... It was so thick..."
                    show sis strip20 at right
                    "She takes a few deep breaths, then slides out from under your desk and stands up."
                    sis "I'm going to go get a drink. I'll see you later."

            "Fuck it, give up and cum inside her!":
                me "Fuck it!"
                "You let go of your keyboard and mouse, wrapping your arms around Lily's hips and pulling them close to your own. She gasps loudly as you push yourself as deep into her as you can manage."
                me "Here I come!"
                "You hold her against you, buried balls deep in her tight pussy, as you orgasm. She buries her face in your neck as you pump her full of cum."
                if sisO.cumslut:
                    sis "Yes, please give it to me! I want you to get me pregnant, fill me up! Ah!"
                else:
                    sis "Oh god... There's so much..."
                show sis fuck36 at right
                "You both stay still for a few minutes, long after you've finished cumming. When she finally has the strength Lily stands up, letting your flacid dick slip out of her."
                me "Damn, that felt amazing."
                "Lily nods weakly, cum trickling down her leg."
                sis "I knew you couldn't do it."
                me "I guess you were right. Well done Lily."
                sis "I'm going to go get cleaned up, I'll see you later."

        "Lily leaves your room, closing the door behind her. You turn back to your game, feeling much more relaxed."
        $ sis_videogame.inc_level(2)
        $ sisO.change_resist(-sis_videogame.use_red(2,sisO.resist_score))

    return

label min_sis_beach_walk:
    me "Lets go for a walk along the beach; see what else is going on here."
    sis "Alright. Lead the way."
    "You pick one direction along the beach and walk along the waters edge. You pass by the volleyball courts, taking a moment to watch a set between to pairs."
    "Past that, the beach gets narrower and narrower, the water comming closer to a small cliff on one side."
    "Soon you've left the crowds behind, with only the occasional stranger passing by. Lily steps closer to you and takes your hand in hers."
    sis "Thank you for inviting me out here [inputName]."
    me "No problem at all Lily. It's my pleasure."
    sis "I'm sure it is, you've been staring at me in this swimsuit all day."
    me "Guilty as charged. You look great in it."
    "Lily giggles and pulls closer to you, pressing up against your arm while you walk."
    "Eventually you come to a rocky outcropping that runs from the cliff down to the water, blocking your path."
    me "I guess this is the end of the road. Come on, lets head back."
    if sisO.slut_score < 40:
        "Lily nods, and the two of you begin the slow stroll back to the center of the beach."
    elif sisO.slut_score < 70:
        #gives you a handjob behind the rocks.
        "Lily lets go of your hand and heads over to the rocks, climbing the first few to get a better view."
        sis "Oh cool, there's a little cove back here. Come on, we can just swim around the side."
        me "Fine, just be a little careful."
        "You follow Lily and wade through the chest high water until you can clear the rocks, then head up the beach onto the other side. You find a small cove; twenty feet of private beach with a short cliff blocking the far side."
        sis "This is great! It's so private back here. In fact..."
        "Lily looks around, then bites her lip and motions for you to come closer."
        sis "I know you've gotten yourself a little worked up. Your swimsuit doesn't exactly leave much to the imagination. Just sit down here and let me take care of it for you, as a way of saying thanks."
        "You sit down on a mostly flat rock next to Lily. She gets down onto her knees and gives you a wink, running her hand over the bulge in your swim trunks."
        me "Here, let me get those out of the way for you."
        if slut_outfit:
            show sis hand13 at right
        else:
            show sis hand12 at right
        $ sisO.inc_hand()
        "You pull your swimsuit down, letting your hard cock free. Lily looks at it for a moment, then reaches out and takes it in her hand."
        sis "It's so warm..."
        "Your sister starts to stroke you off, running her hand up and down the length of your cock. You lean back and relax, enjoying the feeling for a few minutes."
        me "That feels great Lily, keep doing that."
        "She smiles and speeds up, playing idly with a breast while she jerks you off."
        "Not long after you feel yourself tensing up as your orgasm approaches."
        me "Shit, I'm going to cum!"
        sis "Good, do it for me [inputName]!"
        "She speeds up even more and shuffles to the side, clearing the line of fire."
        "Lily gasps as you climax, pulsing your load onto the sand beside her. The last few drops of cum run down your shaft onto her hand before she lets go."
        sis "Wow, that was hot."
        me "Ah, yeah. Thanks Lily."
        if slut_outfit:
            show sis swim2 at right
        else:
            show sis swim1 at right
        "She stands up and heads back to the waters edge, washing your semen off."
        sis "No problem. We should probably start heading back if we want to have time to do something else."
        "You get up and join your sister, wading back out and around the rock outcropping. From there the two of you take a slow stroll back to the center of the beach."
        $ sis_beach_walk.inc_level(0)
        $ sisO.change_resist(-sis_beach_walk.use_red(0,sisO.resist_score))

    elif sisO.slut_score < 90:
        #gives you a blowjob behind the rocks. At this score she's always wearing the slutty version of her swimsuit
        "Lily lets go of your hand and heads over to the rocks, climbing the first few to get a better view."
        sis "Oh cool, there's a little cove back here. Come on, we can just swim around the side."
        me "Fine, just be a little careful."
        "You follow Lily and wade through the chest high water until you can clear the rocks, then head up the beach onto the otherside. You find a small cove; twenty feet of private beach with a short cliff blocking the far side."
        sis "This is great! It's so private back here. In fact..."
        "Lily turns back to you and drops to her knees; the water laps up against her thighs with each little wave."
        sis "Pull down your swimsuit and let me give you a proper thank you for inviting me out here."
        "She licks her lips and winks at you, then watches while you pull your cock out for her."
        me "Here you go, is this what you wanted?"
        "She nods and runs a finger along your hard shaft, tracing it's shape."
        sis "That's exactly what I wanted [inputName]."
        show sis blow23 at right
        $ sisO.inc_blow()
        "Lily leans forward and kisses the tip of your dick, then runs her tongue in circles around it. After getting it wet she bobs her head forward, slipping you into her mouth."
        me "Oh fuck..."
        "Your sister moans something in response, slowly sliding your cock in and out of her mouth."
        "You run your hand through her hair and end up holding on by a handfull, guiding her head as she speeds up her blowjob."
        me "God, keep that up and you're going to make me cum."
        "Lily presses herself down onto your cock, tip sliding along the back of her throat. She looks up at you, holding herself there for a few seconds before pulling back."
        me "I guess that's what you want then, is it?"
        "She moans and nods, blowing you even faster. You tighten your grip on her hair and guide her even faster."
        me "Good girl, just like that. Just a little bit more."
        "Her tight, warm throat draws you closer to orgasm with each thrust."
        me "Fuck, here we go!"
        show sis blow24 at right
        $ sisO.inc_cum_mouth()
        $ sisO.inc_cum_swallow()
        "You pull your sisters head forward as you climax, pushing your cock as far down her throat as you can manage. She moans loudly, making her throat vibrate pleasantly around your shaft as you start to pump your cum right into her stomach."
        "After a few seconds you let go of Lily's hair, and she slides back and off of your dick with a wet pop. She takes a few short breaths, then looks up at you and smiles."
        if sisO.cumslut:
            sis "Thank you [inputName], I love feeling you cum in my mouth like that. You taste so good too."
        else:
            sis "I hope you had a good time. That was... a little intense."
        me "It felt great sis. You've gotten really good at that. Must be all the practice you're getting."
        if sisO.freeuse:
            sis "Every chance I get!"
        else:
            sis "Oh shut up. It's not that often."
        show sis swim2 at right
        "She gets up off her knees and looks around the cove."
        sis "This place is nice, but we should probably head back soon if we want to do anything else today."
        me "I suppose you're right. Come on, I'll lead."
        "You and Lily wade around the rock outcropping again, joining up on the other side. She takes your hand in hers, and the two of you take a slow stroll back to the center of the beach."
        $ sis_beach_walk.inc_level(1)
        $ sisO.change_resist(-sis_beach_walk.use_red(1,sisO.resist_score))

    else: #sisO.slut_score > 90
        #fucks you behind the rocks.
        "Lily lets go of your hand and heads over to the rocks, climbing the first few to get a better view."
        sis "Oh cool, there's a little cove back here. Come on, we can just swim around the side."
        me "Fine, just be a little careful."
        "You follow Lily and wade through the chest high water until you can clear the rocks, then head up the beach onto the otherside. You find a small cove; twenty feet of private beach with a short cliff blocking the far side."
        sis "This is great! It's so private back here. In fact..."
        "Lily presses herself against you before you can even get clear of the water, wrapping her arms around your waist and grinding her hips against yours."
        sis "Mmm, I can feel how hard you are already. I'm sorry I've been teasing you all day with this swimsuit."
        "You wrap your arms around your sister, hands on her ass. You give her a quick spank, making her gasp."
        me "You aren't sorry, and I know it."
        "She giggles and nods, pressing her tits against your chest."
        sis "I'm not, but I want to do something about it now that we have the chance."
        "Lily reaches for your swimsuit and pulls it down, your hard cock springing free to rub against her stomach."
        "She gasps and runs a finger along it's length."
        sis "Oh, it's so big... Here, I know exactly what you want."
        "She spins around in your grip and bends forward, grinding her ass against you now."
        show sis fuck38 at right
        $ sisO.inc_sex()
        "You hook a finger under Lily's tiny swimsuit and pull it to the side. She moans softly when you rub the tip of your cock against her pussy."
        me "I think you want this just as badly as me, right? You're dripping wet already."
        "Lily moans louder and nods."
        sis "Go ahead, please. I want you to fuck me."
        "You plunge inside of her, sliding your full length in on the first stroke."
        sis "Oh fuck! Ah!"
        me "God that feels good!"
        show sis fuck39 at right
        "You grab her arms and pull them back, letting her lean farther forward while you fuck her."
        sis "Yes! Ah, yes!"
        if sisO.anal:
            "After fucking Lily from behind for a few minutes you pull out, moving your cock higher so it's tip rubs against her cute butthole."
            sis "Oh, did you want to try that out too?"
            "Lily wiggles her ass at you, pressing her hips back a little so your wet tip starts to slide inside."
            me "Yeah, I think I do."
            show sis fuck60 at right
            "You pull back on your sisters arms while you push forward, plunging your cock balls deep into her ass."
            sis "Fuck! Ah!"
            "Lily's ass is incredibly tight, gripping your shaft as you slide in and out of her. She pants loudly with each stroke."
            sis "It's so big! I feel like it's tearing me apart and I love it!"
            "You fuck Lily's ass until it's red, then pull out and move lower again."
            me "That's enough for now, I don't want to stretch you out too badly."
            show sis fuck39 at right
            "You slide your dick back into your sister's cunt, letting out a moan of your own as you go. Soon you're fucking her as fast as you can manage again."
        "Lily's pussy is dripping wet around your shaft, and the feeling quickly draws you close to your orgasm."
        menu:
            "Cum inside of her.":
                me "I'm going to cum!"
                "Lily just moans in response as you push yourself as deep inside of her as you can manage. You pull back hard on her arms while you pump her cunt full of your sperm."
                show sis fuck41 at right
                $ sisO.inc_cum_inside()
                "You both stand still in the moments after, panting. When you let go of Lily's arms she takes a step forward, sliding your cock out of her."
                if sisO.preg_response_ok():
                    sis "Wow... It feels so warm..."
                else:
                    sis "Wow... Shit, you really shouldn't cum in me like that [inputName]. Be more careful next time, okay?"
                "She reaches a hand between her legs, wiping up a drip of cum and pulling her swimsuit back into place."


            "Cum on her ass.":
                me "I'm going to cum!"
                show sis fuck40 at right
                $ sisO.inc_cum_over()
                "Lily just moans in response as you pull your cock out of her cunt. You let go her arms and stroke yourself off, spraying your hot load over her ass and lower back."
                "You both stand still in the moments after, panting."
                sis "Wow... It feels so warm... You really covered me."
                "She straightens up and takes a deep breath to steady herself. Eventually she reaches down and pulls her swimsuit back into place too."

        show sis swim2 at right
        me "That felt great Lily. Thanks."
        sis "It really did. Ah..."
        "You hang around in the cove for a few minutes while you both catch your breath, then wade back around the rock outcropping again."
        "Lily takes your hand in hers while you take a slow stroll back to the center of the beach."
        $ sis_beach_walk.inc_level(2)
        $ sisO.change_resist(-sis_beach_walk.use_red(2,sisO.resist_score))

    return

label min_sis_shower:
    if sisO.slut_score < 20:
        # Knocks on door and asks you to hurry.
        "You've just gotten the water to the perfect temperature when there's a knock at the door."
        sis "Hey [inputName], is that you in there?"
        "You lean out of the shower and shout back to your sister on the other side of the door."
        me "Yeah, it's me, why?"
        sis "Can you hurry it up? I need to get ready and you're going to use up all the hot water."
        me "Calm down, I won't be that long."
        sis "Really? You take for-ev-er in there most of the time. I know what you're doing in there, and it's disgusting. We all use that shower you know."
        me "Lily, seriously just calm down. I'll be out in two minutes."
        sis "Fine. Thank you."
        "You enjoy another couple of minutes under the warm water, then step out and grab a towel. You call out to your sister as you head back to your room to get dressed."
        me "Lily, shower's free!"
        sis "Thanks!"
        "Lily hurries into the bathroom and closes the door behind her."

    elif sisO.slut_score < 40:
        # Opens door and asks you to hurry, undresses as you finish your shower.
        "You've just gotten the water to the perfect temperature when the door to the bathroom opens up."
        show sis casual_night at right
        sis "Hey [inputName], are you going to be much longer in here? I need to grab a quick shower then get going for the day."
        me "I'll be done in a few minutes if you don't mind waiting."
        sis "Alright, just don't take forever, okay?"
        show sis showerstrip3 at right
        "Lily starts to undo her pajama top and pull it off. You watch from the other side of the shower glass as she drops it to the ground, then pulls her sweatpants down as well."
        "Once she's stripped down to just her panties she turns to the bathroom sink and grabs her toothbrush. You get a good look at her ass as she brushes her teeth."
        "You enjoy another minute or two under the warm water while your half naked sister get ready in front of the mirror."
        sis "Done yet?"
        me "Yeah, I'm done. The shower is all yours."
        $ sisO.inc_naked()
        show sis shower at right
        "You step out of the shower and grab a towel, drying off your hair first. Lily pulls down her panties and adds them to her pile of discarded clothes."
        sis "Thanks [inputName]. Nice morning wood by the way, maybe you should go take care of that."
        "Lily takes a good long look at your hard cock, then gets into the shower and adjusts the water."
        me "Maybe I will. Talk to you later."
        hide sis
        "You close the door to the bathroom behind you and head to your room to get dressed again."
        $ sis_shower.inc_level(0)
        $ sisO.change_resist(-sis_shower.use_red(0, sisO.resist_score))

    elif sisO.slut_score < 65:
        # Opens door and comes in, asks to share the shower with you so there's still hot water. Gives you a soapy handjob.
        "You've just gotten the water to the perfect temperature when the door to the bathroom opens up."
        show sis casual_night at right
        sis "Hey [inputName], I need to grab a quick shower before I get going for the day. Mind if I join you?"
        me "No, come on in. The water's great."
        show sis showerstrip3 at right
        "Lily steps into the bathroom and begins undoing her pajama top. She strips it off, then pulls the bottoms down as well."
        show sis shower at right
        "You watch as your sister bends over to pull her panties down, then kicks them onto the top of the pile. You open the door to the shower and make room for her."
        sis "Thanks for sharing. I figured you'd use up all the hot water by the time you were done."
        me "Well I'm glad you came in then."
        "Lily turns her back to you and lets the water run over her body. She gasps softly as your growing erection rubs up against her ass."
        sis "Hey, what's that? Getting a little worked up, eh?"
        "Lily giggles and leans forward, rubbing her butt against your crotch."
        sis "Isn't that just a little fucked up [inputName]? I mean, I'm your sister for gods sake. You shouldn't be rubbing your dick against me in the shower..."
        show sis showerstrip6 at right
        "You grab her hips and grind up against her. Lily moans softly and presses herself eagerly against you."
        me "You can't blame me for this, you're the one who came in here and interupted my shower. This is your fault Lily."
        sis "Is it? Well, let me help you out then. It'll be our little secret."
        $ sisO.inc_hand()
        show sis showerhand2 at right
        "Lily takes a half step to the side, then reaches down and wraps her hand around your cock. She starts to stroke you off, still pressing her back against your chest."
        "You slide your hands up from Lily's hips to cup her breasts. She moans louder when you gently roll her nipples between your fingers."
        sis "Does that feel good? Mmm..."
        "Lily speeds up her handjob as you fondle her tits."
        me "Yeah, keep doing that Lily. You're going to make me cum soon."
        if sisO.cumslut:
            sis "Oh god yes... [inputName], I want you to cum for me! I don't care how wrong it is, I want it!"
        else:
            sis "Ah... Whenever you're ready..."
        "You relax and enjoy your sisters wet, slippery hand wrapped around your shaft and her warm, soft tits in your hands. After a minute or two you feel your orgasm approach quickly."
        me "Fuck, here I cum Lily!"
        $ sisO.inc_cum_over()
        show sis showerhand3 at right
        "Lily bends forward, throwing one arm against the far side of the shower to support, and keeps stroking you off. She rests the tip of your cock on her ass and gasps when you start to spray your load over her cheeks."
        me "That's it, fuck that feels good!"
        "Lily keeps stroking you until you're finished, then lets go of your cock. She stays bent over for a few seconds while the shower water runs over her, washing away your cum."
        sis "Ah... That was pretty intense."
        me "You did a great job Lily. Thanks."
        sis "Any time. We just can't let anyone know about this, right?"
        me "Of course. I think I'm done in here for now, I'll see you around."
        "You give your sister a light smack on the ass as you step out of the shower and grab a towel. You head back to your room and get dressed."

        $ sis_shower.inc_level(1)
        $ sisO.change_resist(-sis_shower.use_red(1, sisO.resist_score))
    elif sisO.slut_score < 100:
        # Opens door and joins you in the shower, grinds up against you until you cum.
        "You've just gotten the water to the perfect temperature when the door to the bathroom opens up."
        show sis casual_night at right
        sis "Hey [inputName], I need to grab a quick shower before I get going for the day. Mind if I join you?"
        me "No, come on in. The water's great."
        show sis showerstrip3 at right
        "Lily steps into the bathroom and begins undoing her pajama top. She strips it off, then pulls the bottoms down as well."
        show sis shower at right
        "You watch as your sister bends over to pull her panties down, then kicks them onto the top of the pile. You open the door to the shower and make room for her."
        sis "Thanks for sharing,"
        "Your sisters gaze drifts down to your erection. She smiles and turns around, brushing her ass against your tip."
        sis "But I guess you enjoy the company."
        show sis showerstrip6 at right
        "She giggles and grabs the shampoo from the shower rack. She leans forward just a little and wiggles her ass so your cock keeps rubbing against it."
        me "Maybe you could help me enjoy it even more."
        "You reach around and grab Lily's tits. She moans softly as you squeeze them together."
        if sisO.exhib:
            sis "Mmm, maybe I could. Could you imagine if Mom saw us like this? I wonder if she'd think it's as hot as I do."
        else:
            sis "Mmm, maybe I could. Mom can't know anything though, okay?"
            me "Yeah, of course."
        "Lily grinds her hips against yours, rubbing your cock between her wet ass cheeks. Her nipples have gotten rock hard under your hands as you fondle her tits."
        sis "Ah... Wait a sec."
        "Lily takes the shampoo bottle and twists around. She squirts some of the shampoo on her lower back and over her ass, then puts the bottle back and presses herself back against you."
        "She works her hips up and down, stroking you off with her ass cheeks. The shampoo makes her feel impossibly smooth and slick, and the feeling makes you moan a little as well."
        me "Oh god Lily, that feels great."
        sis "Yeah? Just relax and have fun, I'll take care of you."
        show sis showerhand4 at right
        "Lily keeps rubbing herself against you, pausing a few times to squeeze out some more shampoo onto your hard cock."
        sis "How are you doing? Ah... Are you going to cum soon?"
        me "Yeah, I think so. Just keep going!"
        "You hold onto Lily's hips and thrust up and down against her, moving in time with her strokes as your orgasm approaches quickly."
        me "Fuck, here I go!"
        if sisO.cumslut:
            sis "Wait, I want you to cum in me!"
            if sisO.anal:
                "Lily takes grabs her ass and spreads her cheeks, leaning her shoulders against the wall of the shower."
                sis "Come on, cum inside my ass!"
                $ sisO.inc_cum_inside_ass()
                "You struggle to hold back your climax as you grab your shaft and line it up with your sister's butthole. She feels impossibly tight, but the lubrication from the water and shampoo is just enough to let you slide the tip in."
                show sis showerhand6 at right
                "Lily shivers with pleasure as you finally cum, pumping your load right into her ass. You give her a few quick strokes when you're done, then pull out and step back."
                sis "Wow... Ah... It feels so nice and warm inside me."
                me "That was great Lily, really great."
                sis "Yeah, it was. Ah..."
                "Lily stays leaning up against the wall, still catching her breath while your semen drips out of her tight little asshole."

            else:
                "Lily leans her shoulders against the wall of the shower and spreads her legs, giving you a clear shot at her tight pussy."
                if sisO.preg_response_ok():
                    sis "Come on, cum inside me!"
                else:
                    sis "Give it to me, I think I'm safe today!"
                $ sisO.inc_cum_inside()
                "You struggle to hold back your climax as you grab your shaft and line it up with your sister's cunt. She's dripping wet and amazingly tight as you slide into her, just barely before you cum."
                show sis showerhand5 at right
                "Lily shivers with pleasure as you start to pump your load deep inside of her. You give her pussy a few strokes once you're done, then pull out and step back."
                sis "Wow... Ah... It feels so nice and warm inside me."
                me "That was great Lily, really great."
                sis "Yeah, it was. Ah..."
                "Lily stays leaning up against the wall, still catching her breath while your semen drips out of her pretty little pussy."

            "You spend a few more seconds in the warm shower water, then step out and grab a towel."
            me "I think I'm done in here, enjoy the rest of your shower."
            hide sis
            "You leave Lily alone in the bathroom and head to your room to get dressed."

        else:
            $ sisO.inc_cum_over()
            show sis showerhand3 at right
            "You grunt as you climax and start to pulse your load out over Lily's lower back. She keeps stroking you with her ass cheeks until you're completely finished."
            me "Ah, that was great Lily. You're really good at that you know."
            sis "Thanks. That was pretty hot, wasn't it."
            "She stands up and turns around, letting the shower water wash your cum off of her back."
            me "It definitely was. I think I'm done in here, have a good shower."
            hide sis
            "You step out, grab a towel, and head to your room to get dressed."

        $ sis_shower.inc_level(2)
        $ sisO.change_resist(-sis_shower.use_red(2, sisO.resist_score))
    else:
        # Comes in for a shower quicky.
        # Opens door and joins you in the shower, grinds up against you until you cum.
        "You've just gotten the water to the perfect temperature when the door to the bathroom opens up."
        show sis casual_night at right
        sis "Hey [inputName], I noticed you were in here and was wondering if you'd like some company?"
        "Lily steps into the bathroom and closes the door behind her. She undoes the top few buttons on her pajama's while she waits for you to answer."
        me "Sure Lily, there's plenty of room in here."
        show sis shower at right
        "Lily smiles and pulls off her shirt. It doesn't take long before she's finished stripping completely and steps into the shower with you."
        sis "Thanks. You know, I was thinking..."
        "Your sister glances down at your erection, then reaches out and runs a finger along it."
        sis "That if we're both in here we could have a little fun. What do you say?"
        me "What kind of fun would that be?"
        "She wraps her hand around your shaft and strokes it slowly."
        sis "Come on, you know what I mean. Just a quickie, before I have to get going."
        me "I want you to say it then. What do you want?"
        "Lily steps right up againt you, pressing her breasts against your chest. She rubs your cock right againt her pussy."
        sis "I... I want you to fuck me [inputName]. I want you to fuck me right now."
        show sis showerfuck8 at right
        "You guide Lily a few steps backwards, until her back is pressed against the shower wall."
        me "That's what I wanted to hear."
        $ sisO.inc_sex()
        "Lily keeps your shaft in line her pussy as you push forward, sliding yourself into her. She leans her head forward and rests it on your shoulder."
        sis "Oh fuck... It always feels so big..."
        "You give Lily a few seconds, then start to work your hips back and forth. She moans and pants into your ear as you fuck her against the side of the shower."
        sis "That's... ah, right there... Yeah, that's it!"
        me "Mmm, you're such a dirty little slut Lily, I love it!"
        if sisO.freeuse:
            sis "I'm your dirty little slut [inputName], I'm your filthy fuck toy! Give me exactly what I deserve! Ah!"
        else:
            sis "It feels so good, I just... Ah... I just don't care anymore!"
        "You grab Lily's hands and lift them up, pinning them against the wall. She moans and kisses you, wrapping her tongue around yours as you fuck her."
        "After a few minutes you can feel your orgasm starting to build. You break the kiss and focus on fucking her as fast as you can manage."
        me "I'm going to cum soon."
        if sisO.cumslut:
            sis "Mmm yeah, give it to me [inputName]! Give me a nice big load!"
        else:
            sis "Ah! Finish wherever you want!"
        menu:
            "Cum inside of her.":
                "You take a few more quick pumps, then push yourself as deep into your sister's cunt as you can manage. She shivers and twitches against you as you climax and start to fill her up with hot cum."
                sis "Ah! Oh god [inputName]!"
                $ sisO.inc_cum_inside()
                "She wraps her hands around your back and holds on tight until you've finished. The two of you stand together for a few seconds, panting for breath."
                show sis showerfuck9 at right
                "Eventually you take a step back and let your cock slide free. Your cum starts to trickle down her leg almost immediatley."
                me "That was great Lily, it felt great."
                if sisO.preg_response_ok():
                    sis "It did for me too. Whew..."
                else:
                    sis "It did, but you really shouldn't cum inside me any more. What would we do if I got pregnant?"

            "Cum on her face.":
                "You take a few more quick pumps, then pull out of your sister's wet cunt and step back."
                me "Get on your knees for me!"
                "Lily doesn't waste any time. She drops to her knees and looks up at you, holding herself right under the tip of your cock as you stroke yourself to completion."
                $ sisO.inc_cum_over()
                show sis showerhead5 at right
                "She gasps softly as your first blast of cum shoots over her face, covering her nose and forehead. You pulse out the rest of your hot load all over her, wiping the last few drops onto her chin."
                sis "Fuck, you really covered me..."
                if sisO.cumslut:
                    "Lily runs a finger along her cheek, scooping up your cum and then licking it clean. She closes her eyes and sighs happily. After a few seconds she stands up and gets under the showerhead."
                else:
                    "Lily wipes some of your cum away from her eyes, then gets up and stands under the showerhead."
                me "That was great Lily, you felt amazing."
                sis "So did you. Whew..."

        "You and Lily spend a few more minutes in the shower together getting cleaned off. When you're done you step out and grab a towel, then pass one to her."
        sis "That was fun, we should do it again some time."
        me "Sounds good to me. See you later Lily."
        hide sis
        "You split up and head back to your seperate rooms to get dressed."
        $ sis_shower.inc_level(3)
        $ sisO.change_resist(-sis_shower.use_red(3, sisO.resist_score))
    return

######################
##Mom's Minor Scenes##
######################

label min_mom_wakeup:
    if momO.slut_score < 50: #Handjob
        me "Well... I normally wait a little while to let \"things\" calm down."
        "Mom thinks for a moment, then walks over and sits on the edge of your bed."
        mom "Then I'll help you take care of that right now. It's important to get an early start to the day, or you'll waste it all in bed."
        "She pulls the sheets of the bed off of you, then reaches for your pants. You help her slide them down enough to free your already hard dick."
        mom "We'll have to make it quick though. I don't have much time or I'll be late."
        show mom hand7 at right
        $ momO.inc_hand()
        "She takes your shaft in her hand, rubbing it gently while you lie down and relax."
        me "Okay mom, I'll try and finish as quickly as possible."
        "Mom smiles at you and nods. For a few minutes she jerks you off in silence."
        mom "Would it help if I showed you something?"
        me "I think it would, ya."
        "Mom pauses her handjob for a moment to undo her jacket and pull it wide. Then she pulls her beige bra up and out of the way to let her tits out."
        mom "There, how's that?"
        me "Great. You look great mom."
        "She smiles and takes hold of your cock again. She rubs your precum around, then jerks you off with her slippery hand."
        "A short while later you're ready to finish."
        me "Mom, I'm almost there."
        mom "Good, just let it out."
        show mom hand8 at right
        "She speeds up slightly as you start to orgasm. You fire your load almost straight up, landing most of it over your stomach and shirt."
        "The rest dribbles down your shaft and onto Mom's hand. She slows her stroking until you're completely finished, then lets go. With her clean hand she pulls her bra back down and gets her shirt sorted out."
        mom "There you go honey. Now, I've got to get to work. Try and make the most of the morning, okay?"
        me "Uh, ya. Of course mom. Have a good day at work."
        "She leaves your room and closes the door behind her."
        $ mom_wakeup.inc_level(0)
        $ momO.change_resist(-mom_wakeup.use_red(0,momO.resist_score))

    elif momO.slut_score < 70: #Titfuck
        me "Well... I normally wait a little while to let \"things\" calm down."
        "Mom nods and walks over to your bed."
        mom "I think I know something that can help with that. Pull down your pants for me sweetheart."
        "You kick the sheets away and pull your pants down while mom sits on the edge of the bed. She undoes her jacket and pulls it out of the way, then pulls her bra up and lets her tits flop out."
        mom "Just lie down and leave it to me, okay?"
        me "Okay mom."
        show mom tit3 at right
        $ momO.inc_tit()
        "Mom climbs onto the bed, on all fours near your crotch. She holds her tits in her hands and wraps them around your cock, putting just enough pressure on them to hold you in place."
        "She starts to slide her tits up and down along your shaft, occasionally using a finger to guide you back in-between her cleavage."
        mom "How's that?"
        me "Fantastic mom. Your tits feel great."
        "Mom smiles and leans forward a little to get a better grip on her tits. Her ass is thrust high into the air behind her, her work skirt riding high while she moves back and forth."
        "After a few minutes she stops and spits into her hand. Then she grabs your cock and strokes you off a few times to get you wet, then wraps your slippery dick with her tits again."
        me "Oh fuck."
        mom "Language. I'm glad you like it though."
        "It doesn't take long before the warm, soft, and slippery feeling of your mom's breasts has you ready to cum."
        me "Mom, I'm almost there. Don't stop."
        mom "Let it all out for me sweetheart. Just let it go."
        show mom tit4 at right
        $ momO.inc_cum_over()
        "She speeds up a little, gasping when your first burst of cum shoots out and lands just under her neck. She keeps you sliding between her tits until you're completely done."
        "Finally she pulls her tits back and looks down at them."
        if momO.cumslut:
            mom "Wow, thank you [inputName]. Just what I was looking for."
            "She runs a hand over the slope of her breasts, spreading your cum around."
            mom "Oh, I think there's still a little left here."
            "She leans back down and licks along the sides of your cock, making sure she's cleaned up every last drop."
            mom "There, that's better. I hope you had a good time too sweety."
        else:
            mom "Wow. Good job."
        "She glances at the clock beside your bed."
        mom "And look at the time! I've got to get going, I'll be home later tonight, okay?"
        me "Okay mom, thank you!"
        "Mom pulls her bra back into position then does up her jacket. She uses her hand to wipe all the cum on the top of her breasts towards her cleavage where it'll be hidden."
        mom "Can you see any of it?"
        me "No, you look great mom."
        "She hurries from your room and leaves for work with your cum still in-between her tits."
        $ mom_wakeup.inc_level(1)
        $ momO.change_resist(-mom_wakeup.use_red(1,momO.resist_score))

    elif momO.slut_score < 85: #Blowjob
        "Mom walks over to the bed and sits down. She reaches for the bed sheets and starts pulling them away."
        mom "Actually, I think I know what would get you up. Pull down your pants for me sweetie."
        "You nod and pull your pants down, as soon as your cock is free mom takes it in her hand and starts rubbing it."
        mom "Would you like me to take care of this for you? So you can focus on the rest of your day?"
        me "That would really help mom, ya."
        show mom blow5 at right
        $ momO.inc_blow()
        "She smiles and nods. Mom brushes her hair behind one ear and leans over, licking the bottom of your cock just under the tip. You lie back down and sigh."
        "Mom licks around your cock a few times until it's wet, then slips her mouth over it and starts bobbing her head up and down, going a little lower each time."
        "Finally she reaches the base, her nose gently bumping your stomach while she takes you as deep as she can."
        me "Wow, that's amazing. Don't stop mom."
        "Mom mumbles something that you can't understand past your cock and speeds up a little. Before long her warm, wet throat has you ready to cum."
        me "I'm about to cum!"
        "Your mom pulls your cock back a little so the tip is just inside her mouth and takes in her hand. She rubs your wet shaft as fast as she can while you start to unload into her waiting mouth."
        show mom work at right
        $ momO.inc_cum_mouth()
        $ momO.inc_cum_swallow()
        "She slows down once you are done and pulls off. Without saying anything she stands up, then takes a moment to swallow."
        if momO.cumslut:
            mom "Mmm, thank you [inputName]. Your cum just tastes so good, I'm glad I could have a little snack before work."
            me "No problem Mom. Don't you have to get off to work now?"
        else:
            mom "Wow. Well done sweetheart. I hope that helped."
            me "A ton. Thanks mom. Don't you have to get off to work now?"
        "Mom glances at the time on your clock."
        mom "Oh shit, you're right. I'll be home later today sweetheart, make sure to get to work on time!"
        "She hurries out the door before you can respond, going straight to her car and pulling out of the driveway."
        $ mom_wakeup.inc_level(2)
        $ momO.change_resist(-mom_wakeup.use_red(2,momO.resist_score))

    else: #Fuck her
        "Mom walks over to the bed and sits down on the side."
        mom "How about a quickie? That should wake you up, and as long as you don't get my outfit dirty we should have enough time."
        me "Uh, that sounds great mom."
        show mom fuck16 at right
        $ momO.inc_sex()
        "She smiles and pulls her skirt up, then slips her panties off. She climbs on top of you with her ass towards you and head away."
        mom "Like the view?"
        "She wiggles her butt at you, and you give it a light spank."
        me "It looks great mom. You have a fantastic ass."
        mom "I'm glad you like it. Pull your pants down sweetheart."
        if momO.anal:
            "You do so, and rub your hard cock against her sli. She moans when you flick your tip past her clit, then reaches back and pulls one of her ass cheeks to the side."
            mom "Wouldn't you like to slip it in somewhere else? I promise this will feel great for both of us."
            "Mom rubs her ass along your shaft. You hold your cock still while she gets lined up over it."
            mom "I don't have much time, so cum as soon as you can, okay?"
            me "I'll do my best."
            "Your mom sighs as she sits back down on your dick, using her body weight to push it deeper and deeper into her ass."
            mom "Oh wow... That's a little, ah, bigger than I remembered..."
            "She takes a deep breath, then starts to work her hips up and down."
            me "You feel amazing Mom. I would be done even faster if you talked dirty to me."
            if not (momO.freeuse or momO.slut_score > 105):
                mom "Oh ya? I think I can do that for you. Remember this is all just to help you get off."
                me "Of course mom."
            "She holds her ass down on your cock and shakes her waist left and right a few times, then goes back to riding you."
            mom "Just lie there and let me take care of you. Let me ride your cock like a good slut should."
            me "Do you like me fucking you?"
            mom "God yes. I love feeling you deep inside of me, I just want your cock so bad."
            "Mom moans and speeds up, slamming her ass up and down on your dick."
            mom "Can you cum for me now? Can you cum inside your slutty mom's ass? Please, please don't make me beg for it..."
            $ momO.inc_cum_inside_ass()
            "Hearing your mom talking like that drives you to the edge. You grab a handful of each ass cheek and guide her up and down. Finally you pull her down on you and start unloading inside of her."
            if momO.cumslut:
                mom "Oh god! There we go, fill me up sweetheart. Give your cumslut what she wants and pump my ass full of that hot cum!"
            else:
                mom "Oh god, There we go, give it all to me. I want you to cum your little brain out."
        else:
            "You do so, and rub your hard cock against her slit. She moans when you flick your tip past her clit and starts to lower herself onto you."
            "She's already dripping wet, and you're able to slide all the way into her without stopping. Mom moans a little and pauses at the bottom before she starts to ride you."
            "You lie back on the bed and enjoy the view of mom's ass bouncing up and down on you, your cock slipping all the way into her pussy."
            mom "I don't have much time, so cum as soon as you can, okay?"
            me "I'll do my best."
            "She you gives a few more strokes of her pussy."
            me "It would help if you could talk dirty to me. That always gets me off faster."
            if not (momO.freeuse or momO.slut_score > 105):
                mom "Oh ya? I think I can do that for you. Remember this is all just to help you get off."
                me "Of course mom."
            "She holds her ass down on your cock and shakes her waist left and right a few times, then goes back to riding you."
            mom "Just lie there and let me take care of you. Let me ride your cock like a good slut should."
            me "Do you like me fucking you?"
            mom "God yes. I love feeling you deep inside of me, I just want your cock so bad."
            "Mom moans and speeds up, slamming her ass up and down on your cock. Her pussy is drenched and quivering."
            mom "Can you cum for me now? Can you cum inside your slutty mom? Please, please don't make me beg for it..."
            $ momO.inc_cum_inside()
            "Hearing your mom talking like that drives you to the edge. You grab a handful of each ass cheek and guide her up and down. Finally you pull her down on you and start unloading inside of her."
            if momO.preg_response_ok():
                if momO.cumslut:
                    mom "Oh god! There we go, fill me up sweetheart. Give your cumslut what she wants and get her pregnant again!"
                else:
                    mom "Oh god, There we go, give it all to me. I want you to cum your little brain out."
            else:
                mom "I think today is a safe day, so just fill me up!"
        "You grunt as you finish cumming inside of her. Mom spends a few moments panting to catch her breath."
        mom "Did I say the right things? I hope you liked it."
        me "That was amazing. You did great."
        mom "Good."
        show mom work at right
        "Mom pulls off of your cock and stands up. Her legs are shaking a little."
        mom "Oh god, look at the time. I've got to go! I'll be home later sweetheart, make sure to get to work on time!"
        if momO.anal:
            "Mom rushes out of your room and leaves for work before you can say anything. Her panties are still on the ground, and you imagine she's going to spend the whole day at work with your cum dripping out of her ass."
        else:
            "Mom rushes out of your room and leaves for work before you can say anything. Her panties are still on the ground, and you imagine she's going to spend the whole day at work with your cum dripping out of her pussy."
        $ mom_wakeup.inc_level(3)
        $ momO.change_resist(-mom_wakeup.use_red(3,momO.resist_score))
    # "Instead of waking you up, your orgasm has left you feeling exhausted. You lie back down for a few minutes, and before you realize it the whole morning has passed anyway with you lounging in bed."

    if wake_up_recover.check_event():
        "Satisfied, you decide it's time to wake up before the morning gets away from you."
        return False
    else:
        "Instead of waking you up, your orgasm has left you feeling exhausted. You lie back down for a few minutes, and before you realize it the whole morning has passed anyway with you lounging in bed."
        return True

label min_mom_sleep:
    me "I don't mind as long as you don't. It's a small bed though."
    mom "Thank you sweetheart. I'll do my best to let you get your rest."
    "Mom comes into the room and closes the door behind her. You slide over to make room and she slips under the covers beside you."
    me "Comfortable?"
    mom "Thank you for this again [inputName]."
    me "Any time."
    "You and mom try to share the same small bed separately, but after a few minutes of tossing and turning it's clear there isn't enough space."
    mom "I don't think this is going to work unless we're a little closer. Here, put your arm around me."
    show mom sleep1 at right
    "Mom rolls onto her side and slides closer to you, nesting her body against yours like a spoon. You put your arm around her chest and pull her closer."
    me "That seems better."
    mom "Ya, it does."
    "You shuffle around slightly, and end up with your hand lightly cupping mom's breast. You go to move it, but she stops you."
    mom "Don't worry about it. It's going to be impossible to sleep this close without touching something. Just relax and get some rest."
    if momO.slut_score < 45: #nothing extra
        "You hold mom close for the rest of the night, crotch pressed against her ass and hand cupping her breast. You both fall asleep after a few minutes, warm and comfortable."
        "Mom wakes up first and slips out of your arms."
        mom "Thank you for helping me out, I'm going to go get ready for the day."
        "She slips out of your room and heads towards her own."
        $ mom_sleep.inc_level(0)
        $ momO.change_resist(-mom_sleep.use_red(0,momO.resist_score))
    elif momO.slut_score < 85: #She teases you on purpose
        "You hold mom close, crotch pressed against her ass and hand cupping her breast. After a few minutes she starts to shuffle around a little."
        me "Anything wrong mom?"
        mom "No, just trying to get comfortable."
        "She presses her ass into your crotch, then rubs it up and down a few times."
        mom "You'll have to hold me tight so I don't fall off."
        "She takes your arm and places your hand firmly on one of her tits. You can feel that her nipple is hard through her thin tanktop."
        "Mom grinds against your cock a few more times, then settles down against you."
        "Eventually you both fall asleep cuddling with each other."
        "Mom wakes up first and slips out of your arms."
        mom "Thank you for helping me out. I'm going to go get ready for the day."
        "She slips out of your room and heads towards her own."
        $ mom_sleep.inc_level(1)
        $ momO.change_resist(-mom_sleep.use_red(1,momO.resist_score))
    else: #Spoon fucking
        "You hold mom close, crotch pressed against her ass and hand cupping her breast. After a few minutes she starts to shuffle around a little."
        me "Anything wrong mom?"
        mom "No, I just feel something pressed up against me."
        "She rubs her ass up and down on your cock through both of your pants."
        me "Oh, that would be me."
        mom "I thought so. Well that isn't going to help you get to sleep any time soon."
        show mom sleep2 at right
        $ momO.inc_sex()
        "Mom slips her pants off and kicks them to the bottom of the bed, then pulls her panties to the side."
        mom "Just slip in and take care of it however you want."
        "You pull your pants down low enough to get your cock out and rub it against her butt a few times. Then you slip it between her legs and run your tip along her pussy."
        me "Ready?"
        "Mom nods and leans forwards a little to help you slip your dick inside of her. She moans a little as you slide in all the way."
        "You pull her tanktop up and fondle her tits with your free hand and start to pump into her rhythmically."
        if momO.exhib:
            "Mom rolls her hips against you while you fuck her, moaning loudly as you go. She clearly isn't worried about waking up Lily."
        else:
            "Mom lays still for you while you fuck her, moaning softly into a pillow. It isn't long until you're ready to cum."
        me "I'm almost there mom."
        if momO.preg_response_ok():
            if momO.cumslut:
                mom "Keep going, I want you to cum deep inside me. Can you do that for me?"
            else:
                mom "Keep going, you can finish inside."
        else:
            mom "I don't know if today is a safe day, we should be careful that you don't get me pregnant... Oh, are you already..."
        $ momO.inc_cum_inside()
        "You pump into her a few more times, then hold your cock as deep as you can while you cum inside her pussy. Mom holds her breath until you're finished, then lets it out in a deep sigh."
        me "That felt great mom."
        show mom sleep3 at right
        "You pull out and collapse against your mom. She turns and kisses you, then presses against you again and wraps your arm around her."
        mom "Good. We should both get a good nights sleep after that."
        "You fall asleep cuddling together, your mom's pussy still filled with your load."
        "Mom wakes up first and slips out of your arms."
        mom "Thank you for last night. It really helped. I'm going to go get ready."
        "Mom slips out of the room and heads towards her own."
        $ mom_sleep.inc_level(2)
        $ momO.change_resist(-mom_sleep.use_red(2,momO.resist_score))
    return

label min_mominterruptPorn:
    show mom casual at right
    mom "I'm going to make some food, would you..."
    "You spin your chair around as the door is opened suddenly. You lock eyes with mom. Your dick is still in your hand and some girl is getting pounded on the screen behind you."
    if momO.slut_score < 10: #Is startled
        me "Ah!"
        mom "Ah, I'm sorry!"
        "Mom turns around and grabs the door handle."
        me "No, it's okay, I was just..."
        mom "Sorry! I should have knocked!"
        hide mom
        "She pulls the door almost entirely closed and talks through the crack."
        mom "When you're, uh, done, I'm making some food."
        me "Okay, that sounds good. I'll come down soon."
        "Mom closes the door completely, and you can hear her footsteps down the hallway. Your heart is beating like a jackhammer in your chest from being startled."
        "Suddenly uninterested in jerking off, you close everything down and get cleaned up. You grab a bowl downstairs, making awkward small talk with Mom, then retreat back up to your room to eat."
        $ mom_porn_catch.inc_level(0)
        $ momO.change_resist(-mom_porn_catch.use_red(0,momO.resist_score))

    elif momO.slut_score < 40: #Does nothing, not surprised
        me "Oh, hey!"
        mom "I'm sorry honey, I didn't realise you were busy."
        "You keep rubbing yourself slowly."
        me "No problem, I should have locked the door or something."
        mom "Don't worry about it, it's no big deal. I'm making food for the three of us, when you're ready it'll be downstairs."
        me "Sure, thanks mom."
        mom "Have fun."
        "She smiles and closes the door. You turn back to your porn and finish yourself off a short while later. You grab your food from downstairs, then return to your room to eat."
        $ mom_porn_catch.inc_level(1)
        $ momO.change_resist(-mom_porn_catch.use_red(1,momO.resist_score))

    elif momO.slut_score < 70: #Gives you a blowjob
        me "Oh, hey mom."
        mom "Sorry I'm interrupting sweetheart. I'm making food downstairs, if you want some."
        me "Sure, I'm just trying to take care of something quickly."
        "You keep stroking your cock while you look at mom."
        mom "Well hurry down, it'll be cold otherwise."
        me "I'm going as fast as I can, but I can only do so much."
        "Mom pauses for a moment, then steps into the room and closes the door behind her."
        mom "How about I help out then. I can spare a few minutes."
        me "That would be great mom."
        show mom blow1 at right
        $ momO.inc_blow()
        "She comes forward and kneels down in front of you. She takes your cock from you and gives it a few rubs, then leans towards it and slips the tip into her mouth."
        me "Fuck that feels good."
        "Mom nods and starts bobbing her head up and down on your cock, gliding easily on your already slippery shaft."
        "It doesn't take long before you're feeling ready to finish."
        me "I'm almost there mom."
        "She mumbles something past your dick and keeps blowing you."
        if momO.slut_score >60 or momO.cumslut:
            "You tense up and begin to cum. Mom slides off your cock and strokes you off while you unload onto her face."
            me "Fuck!"
            show mom blow3 at right
            $ momO.inc_cum_over()
            if momO.cumslut:
                mom "That's it, let it all out. Cover me with your dirty cum."
            "When you're finished she lets go of you and takes a moment to catch her breath."
        else:
            "You tense up and begin to cum. Mom slides off your cock and strokes you off to her side."
            me "Fuck!"
            "You fire your load past her onto the floor. She rubs your sensitive shaft a few more times before letting go."
        mom "There you go sweetheart. All done."
        me "Wow, thanks mom."
        mom "I'm just glad I could help. Now get cleaned up and come downstairs when you're hungry."
        "You nod and mom stands up. She smiles at you as she closes the door behind her."
        $ mom_porn_catch.inc_level(2)
        $ momO.change_resist(-mom_porn_catch.use_red(2,momO.resist_score))

    else: #Fucks you like the video
        me "Oh, hey there mom."
        mom "Well hello. I guess someone got themselves worked up. You should have let me know."
        me "You seemed busy, I didn't want to bother you."
        "Mom walks in and closes the door behind her."
        mom "It's fine, I've got a few minutes. If you want, we could give that a try."
        "She nods at your monitor, where a girl is being plowed doggy style over a desk."
        me "Sounds like fun."
        "Mom smiles and starts stripping down. You do the same, and after a moment she's bent over your desk in front of you."
        me "Ready."
        mom "Go for it sweetheart."
        show mom fuck13 at right
        $ momO.inc_sex()
        "You press yourself against her pussy and find it already wet. You slip in easily while mom moans with pleasure."
        me "Shit, you feel great."
        "Mom nods and presses her hips against yours while you fuck her."
        "You hold onto her hips and plow your mom for a few minutes until you're feeling ready to cum."
        me "I'm almost there mom."
        if momO.slut_score > 85 or momO.cumslut:
            mom "Fuck! Finish inside me sweetie!"
            "You fuck her hard, slamming your hips into her ass with each pump. When you start to cum you hold yourself deep, moving a little with each pulse."
            me "There it is! Fuck!"
            $ momO.inc_cum_inside()
            show mom fuck14 at right
            "Mom moans and grips the table hard. When you're finished you pull out and admire your handiwork."
            if momO.preg_response_ok():
                mom "That was great. How are you feeling?"
            else:
                mom "I'm sorry sweetheart, I got a little carried away. I shouldn't be letting you cum like that if I'm not on the pill. How are you feeling?"

        else:
            mom "Great! Finish over my ass for me honey!"
            show mom fuck15 at right
            $ momO.inc_cum_over()
            "You fuck her hard, then pull out and stroke yourself to completion. You unload onto her ass cheeks, then rest your tired cock in-between them."
            "You both take a few moments to catch your breath before saying anything."
            mom "That was great. How are you feeling?"
        me "Much better, thanks mom."
        mom "Good. There's food downstairs if you want some."
        me "Okay, I'll be down in a little bit."
        "Mom stands up and gets her clothes back on, then slips out into the hall."
        $ mom_porn_catch.inc_level(3)
        $ momO.change_resist(-mom_porn_catch.use_red(3,momO.resist_score))
    return

label min_morningPay:
    "Mom looks around the kitchen quickly to make sure nobody else is around."
    mom "But it's really getting difficult to make ends meet. I know I shouldn't ask, but is there anything I could do for you for a little bit extra?"
    me "Hmm, there might be. What kind of things were you thinking?"
    "Mom pauses for a second, then grabs a piece of note paper and a pen from the table. She looks at you sternly."
    mom "No telling anybody about this, okay? Prices are non-negotiable."
    "She scribbles some notes onto the paper and hands it to you nervously."
    $mom_public_pay = 30
    if momO.exhib:
        $mom_public_pay = 10
    if momO.slut_score > 80: #61 and up bracket
        menu:
            "I'll flash my tits for $5." if player_money >= 5:
                me "Alright, I could use something nice to start the morning. Flash me your tits."
                "Mom doesn't hesitate, and undoes the top few buttons of her shirt. Once it's wide enough, she spreads it open to squeeze her tits out."
                show mom flash_1 at right
                "Then she grabs her bra and lifts it up out of the way, revealing her beautiful tits framed by her shirt on three sides and bra on one."
                "She grabs her right nipple and pinches it, pulling it left and right."
                show mom casual at right
                $ momO.inc_naked()
                "Finally, she squeezes both of her boobs together, before pulling her shirt back over both of them."
                mom "There you go, a morning flash."
                "You nod, and hand over $5."
                $ mom_favours.inc_level(0)
                $ momO.change_resist(-mom_favours.use_red(0,momO.resist_score))
                $ player_money += -5

            "I'll bend over so you can stare at my ass for $10." if player_money >= 10:
                me "I would love to see more of your sweet ass mom. How about you bend over."
                "Mom nods and turns around. She undoes her jeans and pulls them down, then bends over with her hands on the counter."
                show mom strip7 at right
                "She wiggles her butt, still in her panties, at you."
                show mom strip8 at right
                $ momO.inc_naked()
                "Then she reaches back with one hand and pulls them down and off, so you get a clear view."
                "Mom stretchs forwards, putting her butt as high as possible for you."
                mom "That's all you get for today!"
                show mom casual at right
                "She stands up quickly, and pulls her panties and jeans back up."
                "You nod, and hand over $10."
                $ mom_favours.inc_level(1)
                $ momO.change_resist(-mom_favours.use_red(1,momO.resist_score))
                $ player_money += -10

            "I'll let you use my breasts for $20." if player_money >= 20:
                me "I think I'd like to fuck your tits mom."
                "Mom nods, and starts undoing her shirt."
                show mom tit1 at right
                $ momO.inc_tit()
                "She sits you down on a chair and opens her shirt wide, then opens your pants up for you too."
                "She kneels down in front of you, leans forward, and slips the tip of your penis between her cleavage and under her bra."
                "Next, she looks down and lets a long fat line of spit drop between her tits, then lowers them down your cock."
                "You slide in between her heavy boobs, lubricated by her spit."
                me "Ooh, that feels nice."
                mom "Good, when you're ready cum between my tits."
                "It isn't very long before you're ready to cum as she lifts her tits up and down, your cock held in place by her bra."
                me "I'm cumming, get ready!"
                "Mom grabs her tits with her hands and starts rubbing them up and down as quickly as possible."
                show mom tit2 at right
                "You climax and shoot a few streams of cum up onto her neck and release the rest in between her tits."
                "Mom slides you up and down her tits, freshly lubricated by your sperm."
                $ momO.inc_cum_over()
                mom "That's a good boy, let it out."
                show mom casual at right
                "When you're completely finished, she lifts up, cum trailing from her cleavage. She does her shirt back up and smiles at you."
                if momO.cumslut:
                    mom "Ooh, thank you sweetheart. I almost feel like I should be paying you for this."
                else:
                    mom "Time to pay up."
                "You gladly hand over $20 to her, and go about your day."
                $ mom_favours.inc_level(2)
                $ momO.change_resist(-mom_favours.use_red(2,momO.resist_score))
                $ player_money += -20

            "I'll blow you for $25." if player_money >= 25:
                me "I want you to blow me, and take my load in your mouth."
                "Mom thinks about it briefly, then nods."
                mom "It's for the household, after all."
                "She kneels down in front of you and undoes your pants. She slips your cock out of your underwear and strokes it gently a few times."
                show mom blow1 at right
                $ momO.inc_blow()
                "Then she puts her lips on the tip, and you can feel her tongue playing gently across the top."
                "With painful slowness she slides her mouth down your shaft, tongue lubricating as she goes."
                "When she reaches the bottom she holds for a moment, then slides back up just as slowly."
                "At the top she takes a deep breath, then returns your dick to her mouth."
                "She begins bobbing her head up and down, working your full length."
                "Soon you're feeling ready to cum, brought to the edge by your mom's slutty mouth."
                me "I'm ready mom, I'm going to cum!"
                "Mom doesn't say anything, but looks up and locks eyes with you. She pulls your cock to the front of her mouth, tip resting inside on her tongue."
                "Then she takes a hand and begins stroking you quickly."
                "You begin cumming, and you feel your mom's tongue move up to catch the liquid as it comes out. She pumps your cock quickly, and doesn't stop until you're completely finished."
                me "Wow!"
                show mom blow4 at right
                $ momO.inc_cum_mouth()
                "Mom opens her mouth and shows that it's full of your cum."
                if momO.cumslut:
                    "Once you've had a good look she closes her mouth and swallows, gulping down your thick load."
                    mom "Ah... Thank you sweetheart, that was declicious."
                    "She stands up and gives you a quick hug once you've pulled up your pants."
                else:
                    "Then she stands up, goes to the sink, and spits it out."
                    show mom casual at right
                    mom "Swallowing is extra."
                    "She winks at you, and you smile as you do up your pants."
                "You hand over $25 to her, and you both go about your day."
                $ mom_favours.inc_level(3)
                $ momO.change_resist(-mom_favours.use_red(3,momO.resist_score))
                $ player_money += -25

            "I'll wear something slutty to work for $[mom_public_pay]." if player_money >= mom_public_pay:
                me "Hmm, I want you to put something extra special on for work today. Mondays are hard and I'm sure some of the guys could use some eye candy."
                if momO.exhib:
                    mom "Okay, I can do that. I've got an outfit I've been wanting to use for a while now."
                    $ momO.report_number = 3
                else:
                    "Mom thinks for a few moments, then nods."
                    mom "Okay. I think I've got something for that. Give me a few minutes to dig it out."
                    $ momO.report_number = 2
                "She heads off down the hall towards her room. Soon you hear her comming back, heels clicking on the wooden floor."
                show mom strip30 at right
                "She's wearing a very short skirt this time, riding just low enough to hide the garter belt she's got on. The belt is holding up a set of wide fishnet stockings."
                "Instead of a blazer or formal shirt she's just wearing a black tank top. It's clear that she's not wearing any sort of bra underneath it, and her breasts bounce and jiggle with each step."
                mom "Well, what do you think?"
                me "That's exactly what I was looking for. Turn around and bend over so I can take a look at your panties."
                show mom strip31 at right
                "Mom turns around and bends over, placing her hands on the kitchen table. It's immediately obvious that she's not wearing any underwear at all."
                if momO.exhib:
                    mom "I didn't put any on. I thought I should just show it all off."
                    me "And I'm sure there are plenty of guys at work who would appreciate a quick peek under that skirt now."
                    if momO.freeuse:
                        mom "They can have more than a peek if they want, as long as they ask nicely."
                    show mom strip30 at right
                    "Mom laughs a little bit, blushing. She stands up and faces you."
                else:
                    mom "Oh... I didn't put any on. I can go get some if you'd like."
                    me "No, no. This is great. I bet there are plenty of guys at work who would appreciate a quick peek under that skirt."
                    show mom strip30 at right
                    "Mom blushes a little and stands up again."
                "You count out the cash you promised Mom and hand it over. She takes it and tucks it between her breasts."
                mom "I've got to go get some other stuff ready. Come find me later tonight and I'll tell you how things went."
                me "Sure thing, I'll see you around Mom."
                "She smiles and heads back to her room."
                $ mom_favours.inc_level(9)
                $ momO.change_resist(-mom_favours.use_red(9,momO.resist_score))
                $ player_money += -mom_public_pay


            "I'll ride your cock for $50." if player_money >= 50:
                me "I want to feel your pussy around me. I want you to ride me in this chair."
                "Mom hesitates for a moment, then nods."
                mom "That's $50 for groceries. I can't say no to that."
                "She unbuttons the top of her shirt and lets her boobs slip out of the top. Then she undoes her jeans and slides them off."
                $ momO.inc_sex()
                if momO.anal:
                    "You do as she asks. Mom turns around and pulls her panties to the side, then grips her ass cheeks and spreads them to reveal her asshole."
                    mom "If I'm going to do this for you, we're going to put it in here. Okay?"
                    me "Whatever you say Mom."
                    show mom fuck11 at right
                    "She shuffles backwards, then lowers her hips down until the tip of your penis is pressing against her tight butt."
                    mom "Ready?"
                    me "Yeah, I'm ready."
                    "Your mom sits down slowly, letting her weight push your cock inside of her. She gasps lightly as it finally slips in."
                    mom "There we go. That's... Wow..."
                    "She raises herself up, then lowers herself again. Her ass feels incredibly tight, squeezeing down on your shaft with each stroke."
                    "You reach a hand around and grab one of Mom's tits, fondling it while she rides you."
                    "Mom's moans start to get louder as she speeds up. It's not much longer before you feel your orgasm building up."
                else:
                    "You do as she asks. Mom turns around and pulls her panties to the side, revealing her wet pussy."
                    show mom fuck10 at right
                    "She shuffles backwards, then lowers her slit onto your cock. She guides you right outside her with one hand, while playing with a tit with the other."
                    mom "Ready?"
                    me "Yeah, I'm ready."
                    "Your mom sits down slowly on your cock, letting it slide inside of her. She sighs lightly as it slips in."
                    mom "There we go. That's nice."
                    me "Oh yeah, very nice."
                    "She raises herself up, then lowers herself again. Her thighs being held together makes her incredibly tight, and every movement gets you closer to cumming."
                    "You reach a hand around her, and grab at a tit. You fondle her tits, then find a nipple and pinch it."
                    "Mom sighs louder this time, and speeds up."
                    show mom fuck11 at right
                    "She leans forward, bracing one hand on your leg, and slides up and down faster and faster."
                me "I'm going to cum soon Mom."
                if momO.cumslut:
                    mom "Okay, I want you to cum in my mouth sweetheart. I want to feel you fill my mouth up."
                else:
                    mom "Well I'm not about to spend my morning cleaning that up. Cum in my mouth so I can swallow."
                "Your mom pants loudly as she rides you, and you begin clenching as you orgasm."
                me "Here I cum!"
                show mom fuck12 at right
                $ momO.inc_cum_mouth()
                $ momO.inc_cum_swallow()
                "She stands up off your cock, turns around, and kneels down. Immediately she places your tip in her mouth and strokes your shaft."
                "You cum into her mouth, pulsing five times in time with her strokes."
                "Finally she tilts her head back, and you can hear as she swallows."
                if momO.cumslut:
                    mom "Ah... That tastes so good. Thank you so much."
                else:
                    mom "There, no mess."
                show mom casual at right
                "She stands up and pulls her clothing back into position."
                mom "That will be $50, darling."
                me "Gladly."
                "You count out the cash and hand it over, then go about your morning like normal."
                $ mom_favours.inc_level(4)
                $ momO.change_resist(-mom_favours.use_red(4,momO.resist_score))
                $ player_money += -50

            "Ask for her to give some serum to Lily instead, for $100." if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0) and player_money >= 100:
                call resistance_gain_report(sis_morning_event_object,sisO) from _call_resistance_gain_report_14
                jump maj_spikeLilyMorning

            "Give back the note and keep your money":
                "Sorry mom, I really need all the money I have right now. Maybe next week."


    else: #20 to 60 bracket.
        menu:
            "I'll show you my breasts for $30." if player_money >= 30:
                me "Okay mom, if it'll help the house out. I'd like for you to show me your tits."
                "Mom pauses for a moment, then nods."
                "She begins unbuttoning her shirt, glancing over her shoulder to make sure nobody is coming."
                mom "Ready?"
                "You nod, and she undoes the last button. She pulls her shirt open, and pulls her bra up and out of the way with one hand."
                "Her tits flop out of her bra and jiggle until they come to a stop."
                show mom flash_1 at right
                $ momO.inc_naked()
                "Her nipples are hard, and she's blushing intensely."
                mom "Got a good look?"
                me "One moment. Shake them a little."
                mom "That wasn't the deal."
                me "Just one little shake, to make them bounce."
                "Mom sighs, then shakes a little, bouncing her boobs left and right."
                mom "Okay, there."
                "She pulls her bra back down and uses her hand to scoop her tits back into their cups."
                show mom casual at right
                me "Thank you mom."
                mom "It's only fair, if you're helping out the house."
                "You get your wallet out and hand over $30, then go about your day as normal."
                $ mom_favours.inc_level(5)
                $ momO.change_resist(-mom_favours.use_red(5,momO.resist_score))
                $player_money += -30
            "I'll show you my underwear for $40." if player_money >= 40:
                "Okay mom, if it'll help the house out. I'd like to see what you look like in your underwear."
                "Mom pauses for a moment, then nods."
                "She quickly unbuttons her shirt, then undoes the top button on her jeans. She checks over her shoulder one last time to make sure Lily isn't there."
                mom "Ready?"
                "You nod, and she pulls her shirt off quickly. Next she shuffles her jeans down and steps out of them. Finally she stands still in the middle of the kitchen, wearing nothing but her underwear."
                show mom flash_2 at right
                $ momO.inc_naked()
                "She looks away shyly as you stare at her. Her panties and bra are a matching set, beige and functional."
                mom "Is that enough?"
                me "Turn around."
                mom "That wasn't the deal though."
                me "I haven't seen all of you, that was the deal. Turn around."
                "Mom does, and you get a great look at her ass. You definitely know where Lily got such an amazing ass from."
                me "Okay, get dressed before someone walks in."
                "Mom gets dressed as quickly as possible, then asks for her cash. You pay her and go about your day as normal."
                $ mom_favours.inc_level(6)
                $ momO.change_resist(-mom_favours.use_red(6,momO.resist_score))
                $player_money += -40
            "I'll wear something sexy to work for $50" if player_money >= 50:
                me "Okay Mom, I'll chip in a little something to help out. In exchange, I want you to put something a little nicer on for work. Something that shows you really care about the job."
                "Mom thinks for a moment, then nods."
                mom "I've got to get ready, so I'll put something on I think you would like. Back in a moment."
                "She ducks out of the kitchen, leaving you alone for a few minutes. You hear her heels clicking on the wood floors when she comes back."
                show mom strip28 at right
                "Your mom is wearing a shorter, tighter skirt than she normally does. Instead of her normal set of pantyhose she's got a set of fishnet stockings on, held up by a black garterbelt."
                "She's also wearing a short sleeved dress shirt instead of her normal blazer. She's left most of the buttons undone, so you can see a colourful bra underneath and an impressive amount of cleavage."
                mom "Well? What do you think?"
                me "I think that looks great Mom. Turn around and pull up your skirt so I can take a look at your underwear."
                show mom strip29 at right
                "She blushes a little, but turns around for you anyway. When she pull up her skirt you can see that she's got a bright pink set of panties on, matching her bra."
                me "Yeah, that looks perfect. I think you'll be a real hit at the office today."
                mom "Oh god, that's making me a little nervous."
                me "Don't worry about it, just relax and do your job. You go ahead and get ready for the day, I'll find you later tonight and you can tell me about your day."
                "You count out the cash and hand it over to your mom before she heads back to her room. Her heels click on the floor as she leaves."
                $ momO.report_number = 1
                $ player_money += -50
                $ mom_favours.inc_level(8)
                $ momO.change_resist(-mom_favours.use_red(8,momO.resist_score))

            "I'll give you a handjob for $100." if player_money >= 100:
                me "If it'll help the house out, I'll take the most expensive thing on the menu."
                "Mom hesitates, then nods."
                mom "Okay, hurry up and sit down. We don't want your sister finding out."
                "You sit down on a chair and mom kneels down in front of you."
                mom "Take it out, lets do this quick."
                "You undo your pants and slip them down past your penis. It's already hard, and mom stares at it for a moment."
                "Finally she takes a hand and wraps it around your shaft, and begins rubbing it slowly."
                show mom hand_1 at right
                $ momO.inc_hand()
                me "Thats good mom."
                "She doesn't say anything, but speeds up and makes sure to get the full length."
                "You begin leaking pre-cum, and she spreads it over your shaft. Her hands feel soft and warm, stroking you up and down."
                mom "Almost there?"
                "You wish you weren't, but she's suprisingly good at this."
                me "Ya, you're doing great."
                mom "Okay, I'm going to point you at the floor when you finish."
                menu:
                    "Nod in agreement.":
                        "Mom rubs you faster and faster, then moves her other hand up and takes you in both."
                        "The image of your mom, on her knees with your cock in both hands, puts you over the edge."
                        me "I'm cumming!"
                        "Mom quickly points your cock to the side, away from her. You shoot three powerful bursts onto the floor, then dripple several more onto her hands which stay locked in place."
                        "Without a word mom lets go, stands up, and walks over to the sink to wash her hands."
                        mom "You should wipe that up quickly."
                        "You nod, and get some paper towels for the floor. Afterwards you hand over $100 to her, and you both go about your day."
                        $ player_money += -100

                    "Offer her $50 to finish on her chest." if player_money >= 150:
                        me "I'll give you fifty dollars to finish on your chest mom!"
                        "Mom looks at you in surprise, but nods quickly."
                        mom "Okay, but just the chest."
                        "She takes your cock up in both hands and strokes you as quickly as possible. The feeling of her soft hands gliding up and down your wet shaft puts you at the edge right away."
                        me "Here I come!"
                        "Mom points your cock just below her neck and turns away. You blast three powerful loads onto her neck and above her cleavage, then shuffle closer and let the next few spurts land on her shirt over her tits."
                        show mom hand_1_chest at right
                        $ momO.inc_cum_over()
                        "You finish cumming and sit back, panting."
                        "Mom releases your cock and stands up right away, going to the sink to wipe off your cum."
                        mom "That will be $150 young man."
                        "You pull out your wallet and grab the cash, and hand it to her at the sink."
                        "She doesn't say anything, and you decide to go about your morning like normal."
                        $ player_money += -150

                    "Offer her $100 to finish on her face." if player_money >= 200 :
                        me "I'll give you a hundred if I can finish on your face!"
                        "The thought of cumming on your mom's face almost gets you to finish before she says anything, but your moms hands stop for a moment."
                        mom "Two hundred total?"
                        "You nod quickly."
                        mom "Promise you have that much?"
                        "You nod again, anything to get her to start stroking you again."
                        me "Of course, two hundred total mom."
                        "She nods and then starts stroking you, bringing up her second hand to help."
                        "With both of her hands wet from your precum working as fast as they can, you're quickly brought to the edge."
                        me "Here I come mom!"
                        "Mom looks up and plants your cock just above her chin. She closes here eyes and mouth, and strokes you quickly."
                        "You explode, pumping hot lines of cum across her face. She flinches with each one, but you shuffle forward in your seat to keep your tip resting against her face."
                        show mom hand_1_face at right
                        $ momO.inc_cum_over()
                        "Finally you finish, drippling your last few drops of cum onto her lips."
                        me "I'm done, you can let go."
                        "Mom releases your cock and brings her hands up to her face, to try and wipe the cum out of her eyes."
                        mom "Get me some paper towels dear, I can't see."
                        "You hesitate, enjoying the view of your mom blind and cum covered on her knees, but then get up and do as you're asked."
                        "She wipes her face, then stands up and goes to the sink to wash her hands."
                        mom "That's $200."
                        "You get out the cash, which she takes without making eye contact."
                        me "All for the good of the house, right?"
                        "Mom doesn't say anything, and you decide to go about your day as normal."
                        $ player_money += -200
                $ mom_favours.inc_level(7)
                $ momO.change_resist(-mom_favours.use_red(7,momO.resist_score))
            "Give back the note and keep your money":
                "Sorry mom, I really need all the money I have right now. Maybe next week."
    return

label min_mom_report:
    if momO.report_number == 1:
        # low slut score, sexy office outfit.
        # Lots of people commented on her outfit. A few guys tried to get a look up her skirt. On ~45 slut she let them take a peek.
        mom "Oh, it was okay. Plenty of people seemed to like my outfit."
        me "I thought they would."
        if momO.slut_score < 45:
            mom "I think a few people liked it a bit too much. They kept sending me to get some files from the top shelves."
            me "So?"
            mom "I think it was so they could get a peek up my skirt."
            "Mom blushes a little and shrugs."
            mom "Boys will be boys I suppose."
            me "I suppose. Good to hear you had a good day."
            "You leave the room and let your Mom watch TV."
        else:
            mom "I think they liked it a bit too much."
            me "You think so?"
            mom "The guys kept getting distracted and sending me to fetch files they didn't need, just so they could get a peek up my skirt."
            me "Did you do anything about that?"
            mom "Eventually I just pulled my skirt up and let them have a good look. That seemed to help."
            "She blushes a little and shrugs."
            me "I'm sure that was great for morale. You'll be the talk of the office."
            mom "Oh god I hope not. The other girls can get so catty about things like that."
            me "Well I'm glad you had a good day."
            "You leave the room and let your mom watch TV."

    elif momO.report_number == 2:
        # high slut score, slutty office outfit, not public.
        # Tons of comments about her outfit, some of the other girls were catty.
        # She let the guys look but not touch, but her boss got a little handsy when she was at his desk and bending over. She kind of liked it.
        mom "Oh, it was okay. Plenty of people noticed my outfit, that's for sure."
        me "That's good to hear, it's a good looking outfit."
        mom "Well, not according to the other girls in the office. They can get so catty about stuff like this."
        me "I'm sure their just jealous of you Mom, you've got a great body and aren't afraid to show it off."
        mom "They wouldn't stop going on about how I wasn't wearing any panties. None of the men seemed to be complaining though."
        me "I can't imagine they would."
        mom "My boss even said something about changing the dress code. The other girls were certainly not happy with that."
        "She laughs and shrugs."
        mom "I bet the guys don't want to see those hags like that anyway."
        me "Your boss liked it? That sounds good."
        mom "He had me over to his desk to help him with some work. I think he just wanted a chance to stare at my ass, but I don't mind the extra attention. I drew the line at touching though."
        me "Well I'm glad you had a good day then."
        "You leave the room and let your mom watch TV."

    elif momO.report_number == 3:
        # High slut score, slutty office outfit, public.
        # Tons of comments, same as above.
        # Same as above if slut ~75. Above that, she blows the boss in the bathroom when he gets handsy. Higher than that she fucks him in his office. At very high slut they run a train on her in the conference room.
        mom "It was good. Everyone seemed to love the outfit."
        me "That's good to hear, it's a good looking outfit."
        mom "That's what I thought, and all the guys seemed to agree."
        if momO.slut_score < 75:
            mom "My boss even said something about changing the dress code. Maybe we'll end up with a super-casual friday."
            me "It's nice to hear your boss in on board with all of this."
            mom "Yeah, he had me over to his desk to help him with some work. I think he just wanted a chance to stare at my ass, but I really don't mind the extra attention. I have him a good look at whatever he wanted."
            "Mom giggles a little and blushes."
            me "Well I'm glad you had a good day then."
            "You leave the room and let your mom watch TV."
        elif momO.slut_score < 90:
            mom "My boss certainly did. He called me into his office to get some work done, but couldn't stop looking up my skirt. We had to take some time so I could help him relax and focus."
            me "And how did you do that?"
            mom "Just a quick blowjob. I had been teasing him all morning, so he was finished after a few minutes."
            me "That would certainly do it."
            if momO.cumslut:
                mom "Mmm, his cum tasted so good too. Not as good as yours, but still very nice."
            else:
                mom "Don't worry sweetheart, he wasn't nearly as impressive as you."
            "She giggles a little, glancing down at your crotch."
            me "Well I'm glad you had a good day then."
            "You leave the room and let your mom watch TV."
        elif momO.slut_score < 115 or not momO.freeuse:
            mom "My boss certainly did. He called me into his office to get some work done, but couldn't stop looking up my skirt. We had to take some time so I could help him relax and focus."
            me "And how did you do that?"
            mom "Just a quicky over his desk. With no panties all I had to do was bend over and let him go to town."
            "She sighs and bites her lower lip."
            if momO.cumslut:
                mom "He's not as good as you, but It was so nice to get some cum to swallow in the middle of the day."
            else:
                mom "He's not as good as you, but it felt so good to do that in the middle of the day."
            me "I can imagine. I'm glad you had a good day Mom."
            "You leave the room and let your mom watch TV."
        else:
            mom "Oh, they certainly did. They were staring at me all morning, trying to get a peek up my skirt. That wasn't hard to do, to be fair."
            "She sighs and bits her lower lip."
            mom "So after lunch I called a few of them together for a team building exercise. I had them all so distracted I thought they needed some relief."
            me "And?"
            mom "Well, I laid down on the table and let them have as much fun as they wanted. Once they had cum a few times they were able to get back to work."
            me "How about you, did you have a good time?"
            "She sighs again and nods. She shuffles a little, rubbing her legs together."
            if momO.cumslut:
                mom "I really did. They were nice and gave me exactly what I needed. Oh god, their semen was so warm too..."
            else:
                mom "I really did. They were nice and gave me exactly what I wanted, as for as long as I asked."
            "Mom stares off, lost in thought for a moment."
            me "I'm glad you had a good day then Mom. You'll have to do this again for them some time."
            mom "Oh, I definitely will."
            "You leave the room and let your mom watch TV, her hand idly rubbing her crotch through her pants."

    else:
        "This shouldn't ever be called. Please let me (Vren) know that you ran into this error. Code 332."

    return

label min_mom_catch:
    "Suddenly, a hand wraps around your mouth and waist."
    "You try to yell out, but a voice shushes you into your ear."
    mom "It's alright sweetheart, it's just me."
    show mom casual at left
    "You're so stunned you couldn't say anything, even if she moved her hand away from your mouth."
    "Your mom slides one hand along your belly and peers over your shoulder into Lily's room."
    mom "Wow, she's really going at it."
    "Lily bucks slightly as she hits something particularly sensitive."
    mom "It's not right for you to be peeking on your sister, but I understand that you've got needs."
    "Mom's hand is still over your mouth, her other reaches down past you're belly and runs a finger down your shaft."
    mom "And it's not your fault your sister is a slut. You've done a great job keeping away from her when I'm not around."
    "Mom grabs your cock, and begins to slide along it gently."
    mom "So I'm just going to stroke you off while we watch your sister, so that you don't get any funny ideas about her. Okay?"
    "You nod in agreement, and her hand drifts from your mouth down to your waist. She cups your balls with one hand while stroking you with the other."
    mom "Just relax and enjoy yourself."
    "She strokes you faster, and her hand starts getting slippery with pre-cum."
    "Lily's masturbatation has reached a new height, and you can hear her moaning through the pillow she's biting down on. Your eyes are fixed on her as your mom strokes you."
    mom "One moment."
    "Mom's hand lets go of your cock for a moment, and you hear a wet sound over your shoulder."
    "When the hand goes back, it's slick with her spit. It feels so good you twitch as she starts rubbing you again."
    mom "That's right. Look at your sister and cum for me."
    show sis mast5 at right
    $ momO.inc_hand()
    "You're getting close, and so is Lily. Both hands are working as fast as they can rubbing her clit and plunging inside her."
    me "Mom, I..."
    mom "Just let it go into my hand. Just let it out sweetheart."
    "Your Mom keeps stroking you with her right hand, and cups the tip of your penis with her left. With a shuddering sigh you climax, and release your load into her waiting hand."
    show sis mast4 at right
    "Lily tenses suddenly and lets out a little shriek. Her thighs clamp down on her hands, and her whole body shakes. Then she slumps on the bed, spread out completely."
    "Mom lets go of you, and as you turn around to say something you see her already walking down the hall towards the bathroom."
    $ mom_catch.inc_level(0)
    $ momO.change_resist(-mom_catch.use_red(0,momO.resist_score))
    $ sis_mast.inc_level(0)
    $ sisO.change_resist(-sis_mast.use_red(0,sisO.resist_score))
    return

label min_mom_beach_swim:
    me "How about we go for a swim, the weather seems perfect for it."
    mom "That sounds like a great idea [inputName], lead the way!"
    "You and Mom wade out into the lake, walking along the sandy bottom until it is up to your waist. At that point the two of you lunge forward and begin swimming out farther."
    if slut_outfit:
        show mom strip33 at right
    else:
        show mom strip32 at right
    "Mom keeps pace with you easily, carving through the water with strong, steady, strokes."
    "Soon you slow down, a fair distance from the shore, and tread water while you catch your breath."
    me "You don't even look tired... How do you do it?"
    mom "Practice, sweety. Back in highschool I was on the swim team, it all comes back pretty quickly."
    if momO.slut_score < 35:
        #Just talks about the old days.
        if slut_outfit:
            show mom strip35 at right
        else:
            show mom strip34 at right
        "She lies on her back, taking a deep breath."
        mom "Ah, it's so nice to be out here. I had forgotten how much I liked this. I use to go swimming every day, but after I had you and Lily there just wasn't any time."
        me "We'll have to do this more often then. I'm sure there are a lot of things you could teach me."
        mom "I'd like that. Here, let me start with this."
        "Mom straightens up in the water and floats close to you."
        if slut_outfit:
            show mom strip33 at right
        else:
            show mom strip32 at right
        mom "You'll tire yourself out if you keep flailing your arms around like that. Just take a deep breath and relax, move your legs slowly and let the water support you."
        "You inhale and slow your arms a little. You slip lower down in the water, but nowhere close to sinking below the surface."
        mom "There you go. You could keep that up for hours if you had to."
        "Mom lies back down again in the water, and the two of you just float for an hour. When you're done you race back to shore, and Mom beats you by a mile."
        me "Next time, ah... I'll beat you next time..."
        mom "I'm sure you will sweetheart."
    elif momO.slut_score < 50:
        if slut_outfit:
            show mom strip35 at right
        else:
            show mom strip34 at right
        "She lies on her back, taking a deep breath."
        mom "It's so nice to be out here. I use to go swimming every day, but after I had you and Lily there just wasn't any time."
        me "We'll have to do this more often then. I'm sure there are a lot of things you could teach me."
        mom "I'd like that. I certainly learned a lot back in highschool, but I'm not sure it would be all that useful to you."
        me "Oh? Like what?"
        mom "The swim team use to practice every morning, and us being teenagers we were swimming in hormones just as much as water."
        mom "The guys couldn't keep their hands off us in our little swimsuits, and some of the girls were more than happy for the attention."
        mom "So some of the team got pretty good at sneaking in a little fun while the rest of us were practicing. We'd be swimming laps while some couple had a quicky in the deep end."
        me "What about you, did you ever get up to that kind of stuff?"
        mom "Me? Oh, nothing serious. I never worked up the courage to go all the way in the pool, the most I ever did was jerk a guy off in the water."
        me "Lucky guy."
        mom "Oh stop. Come on, lets just relax for a little bit."
        if slut_outfit:
            show mom strip33 at right
        else:
            show mom strip32 at right
        "You and Mom float in the water next to each other for an hour. When you're done you race back to shore, and Mom beats you by a mile."
        me "Next time, ah... I'll beat you next time..."
        mom "I'm sure you will sweetheart."
        $ mom_beach_swim.inc_level(0)
        $ momO.change_resist(-mom_beach_swim.use_red(0,momO.resist_score))
        #Talks about the old days, and how the other girls use to do guys in the pool.
    elif momO.slut_score < 80:
        #Jerks you off in the water
        "Mom floats close to you and wraps her arms around your chest from behind."
        mom "I learned a few things back then; you can do almost anything in the water."
        "Her hands rub along your chest for a few moments, then one slips below the water and towards your crotch."
        mom "I wanted to thank you for inviting me out here [inputName]. It's so nice to get some time to spend with my son, and to get to go swimming again."
        me "It's no problem at all Mom. My pleasure."
        "Her hand slides into your swimsuit, brushing against your already hard cock."
        if slut_outfit:
            show mom hand17 at right
        else:
            show mom hand16 at right
        $ momO.inc_hand()
        mom "Just relax and let me thank you properly. I know my swimsuit got you excited. Those trunks really don't hide it very well."
        "She pulls the waist of your swimsuit down, then wraps her hand around your shaft and strokes it gently. The water is a little chilly, but her hand is warm and soft."
        "You and Mom tread water while she holds onto you from behind, hand sliding up and down your cock."
        me "That feels great Mom."
        mom "Good. Cum whenever you're ready."
        "She pulls you a little closer, breasts pressing into your back. You relax and just float, enjoying the feeling until your orgasm approaches."
        me "Fuck, here I cum!"
        "Mom speeds up her strokes and whispers into your ear."
        mom "That's right, cum for me sweetheart. Just let it all out for me."
        "She strokes you off as you climax, pulsing your load out into the water. When you're done lets go and pulls your swimsuit back into place."
        mom "There we go, all done."
        if slut_outfit:
            show mom strip33 at right
        else:
            show mom strip32 at right
        "Mom pushes away from you and lies down, floating on her back. You do the same, floating next to your mom for an hour."
        "When you're ready to head back to shore you make it a race, and Mom beats you by a mile."
        me "Next time, ah... I'l beat you next time..."
        mom "I'm sure you will sweetheart. I'll try not to tire you out so much next time."
        $ mom_beach_swim.inc_level(1)
        $ momO.change_resist(-mom_beach_swim.use_red(1,momO.resist_score))
    else: #slut_score > 80
        #Fucks you in the water
        "Mom floats close to you and wraps her arms around your chest from behind."
        mom "There were a few things I never got to try back then though. Would you like to try something with me?"
        "One of her hands slides below the water, feeling the bulge in your swim suit."
        me "I think I would. What did you have in mind?"
        mom "Back in highschool the other girls had worked out a way of having sex in the pool, but I never got to try it."
        "Her hand slides inside the waist of your swimsuit, wrapping around your hard shaft."
        me "Only one way to solve that then. Let me know what to do."
        "Mom pulls your cock out of your swimsuit, then lets go. She lies on her back and spreads her legs, pausing for a moment to pull her tiny swimsuit to the side."
        mom "Pull yourself close to me, and push my hips under the water a little bit. If you just pull my bikini to the side, you should be able to slip right in."
        show mom fuck42 at right
        $ momO.inc_sex()
        "You nod and grab her by the hips. It doesn't take much force to move Mom around in the water, and soon you've got her positioned on front of you, with the tip of your penis lined up with her pussy."
        mom "That's right. Now we'll have to take it slow. The water isn't as lubricating as you might think."
        "You pull her hips towards you slowly, sinking into her cunt inch by inch. Mom arches her back and moans as you enter her."
        me "Damn, you feel so tight like this. It feels great."
        mom "Oh [inputName], you feel so big. Ah..."
        "You pause when you've gotten your full length inside of your mom. The waves on the lake bounce you both up and down, and the coolness of the water contrasted with the warmth of her pussy sends shivers up your spine."
        mom "Okay, I think I'm wet enough for you to keep going. Oh lord..."
        me "Just relax and let me take care of you Mom."
        show mom fuck43 at right
        "You start to thrust in and out of your mom, supporting yourself in the water by holding onto her hips."
        mom "Ah... that's it. Give it to me right there. Nice and slow. Ah..."
        "The water makes you feel weightless, with each pump pushing your Mom away from you. You tighten your grip on her to stop her from floating away."
        "For a few minutes you are both silent, enjoying the strange sensations."
        if momO.cumslut:
            mom "Are you almost there? I want you to give me your big load sweetheart! Ah!"
        else:
            mom "When you're ready, just let it out for me sweetheart. Wherever you want."
        "You pick up the pace, sliding in and out of your mom as fast as your position will allow."
        menu:
            "Cum inside of her.":
                me "Here I come!"
                show mom fuck44 at right
                $ momO.inc_cum_inside()
                "You pull on her hips, pushing yourself as deep inside her tight pussy as you can manage while you orgasm."
                "Mom moans loudly while you fill her cunt up with your hot cum. When you're done you let go of her, and the two of you float free of each other."
                if momO.preg_response_ok():
                    mom "[inputName]... That was... Amazing..."
                    me "Yeah, it was."
                else:
                    mom "Oh [inputName], I should have warned you not to finish inside. I don't know if today is safe or not..."
                    me "I'm sure it'll be fine."
                "Mom takes a moment to just float, then straightens up in the water."



            "Cum on her body.":
                me "Here I come!"
                show mom fuck45 at right
                $ momO.inc_cum_over()
                "You pull yourself free of your mom's tight pussy as you orgasm, leaning back in the water so your cock is above water."
                "You fire your load onto her body, landing your hot cum onto her chest, tits, and stomach. Mom gasps a little as each pulse of semen lands on her, laying spread out on the water."
                mom "[inputName]... That was... Amazing..."
                me "Yeah, it was."
                "Mom takes a moment to just float, then straightens up in the water and washes your cum off of her."

        mom "Lets head back to shore, I'm feeling a little tired out by all of that."
        "You swim back and return to firmer ground. You notice Mom's legs still shaking a little when she walks ashore."
        $ mom_beach_swim.inc_level(2)
        $ momO.change_resist(-mom_beach_swim.use_red(2,momO.resist_score))

    if slut_outfit:
        show mom swim2 at right
    else:
        show mom swim1 at right

    return

label min_mom_shower:
    if momO.slut_score < 20:
        # Knocks on door and asks you to hurry.
        "You've just gotten the water to the perfect temperature when there's a knock at the door."
        mom "Hello? Is that you Lily, or [inputName]?"
        "You lean out of the shower and shout back to your mom on the other side of the door."
        me "It's me Mom. What's up?"
        mom "I've got an early meeting to get ready for, could you finish up as quickly as you can for me?"
        me "I guess, I'll be out in a few minutes."
        mom "Thank you sweetheart!"
        "You go back to your shower and enjoy it for another minute or two, then sigh and step out and dry yourself off. When you leave the bathroom Mom hurries in right away."

    elif momO.slut_score < 40:
        # Opens door and asks you to hurry, undresses as you finish your shower.
        "You've just gotten the water to the perfect temperature when the door to the bathroom opens up."
        show mom night at right
        mom "Hey sweetheart, are you going to be long? I've got an early meeting that I need to get ready for."
        me "Just give me a few seconds to wash my hair and I'll be out of your way."
        mom "Thank you so much, I thought I was going to end up being late."
        show mom nightstrip1 at right
        "Mom grabs her tanktop and pulls it up and off."
        mom "You finish up in there, I'll step in once you're done."
        show mom nightstrip2 at right
        "She hooks her thumbs into the waistband of her sweatpants next and pulls them down. She kicks them to the side as well."
        "You grab the shampoo from the little shelf in your shower and squirt some into your hand, then begin lathering your hair. The whole time you're able to watch your mom undress through the glass shower walls."
        $ momO.inc_naked()
        show mom nightstrip3 at right
        "Mom finally pulls her panties down and off and adds them to the pile of discarded clothing. She turns back to you and her eyes go immediately to your now-hard cock."
        mom "Oh I'm sorry about that sweetheart, I should have waited until you were finished to get undressed I suppose."
        me "No, it's fine Mom. Don't worry about it. Just two seconds while I rinse my hair and I'll be out of your way."
        "Mom waits patiently outside the shower while you finish rinsing off. When you're done you step out and she passes you a towel."
        mom "Thank you again for giving up the shower for me sweety."
        "She leans forward and kisses you on the cheek. The tip of your cock brushes against her thigh."
        mom "Maybe you should go to your room and take care of that, I'd hate for you to walk around like that all day."
        me "Yeah, maybe that's a good idea. Have a nice shower Mom."
        hide mom
        "You take one last glance at your mother as she steps past you into the shower, then you close the bathroom door and head back to your room and get dressed."
        $ mom_shower.inc_level(0)
        $ momO.change_resist(-mom_shower.use_red(0, momO.resist_score))

    elif momO.slut_score < 75:
        # Opens door and comes in, asks to share the shower with you so you aren't late. Gives you soapy titfuck
        "You've just gotten the water to the perfect temperature when the door to the bathroom opens up."
        show mom night at right
        mom "Hey sweetheart, sorry to bother you. I've got an early meeting and I was wondering if I could join you."
        show mom nightstrip1 at right
        "Mom steps into the bathroom and closes the door behind her. She starts to pull her tanktop over her head, letting her breasts fall free."
        me "Sure, there's plenty of room. Come on in."
        show mom nightstrip3 at right
        "You watch as your mom pulls down her sweatpants, then her panties. She kicks her clothes into a pile and steps into the shower with you."
        mom "Thank you sweetheart, you're always so considerate."
        "She leans in and gives you a quick kiss on the cheek, then grabs the shampoo from the shower rack."
        mom "I hope I wasn't interrupting some alone time here..."
        "Mom begins lathering the shampoo into her hair while she looks down at your crotch. Your cock is rock hard."
        me "No, you weren't interrupting anything. You're just a good looking woman, that's all."
        mom "Aw, you're too sweet. I'm glad you think so though."
        show mom showerstrip1 at right
        "Mom pauses for a moment and turns around, showing off her legs and ass to you."
        mom "You know, I feel really bad about barging in here and stealing half the shower from you. How about I give you a reward for being such a good son."
        #TODO: shower titfuck scene
        "Mom gets onto her knees in front of you and holds her breasts up in each hand."
        mom "You just stay right there and I'll take care of everything, okay?"
        me "Okay mom."
        $ momO.inc_tit()
        "Mom takes the shampoo bottle, turns it upside down over her breasts, and squeezes out a long line of shampoo. Once that's done she drops the bottle and grabs her tits again, jiggling them up and down a bit so the shampoo foams in between."
        "Your mom leans forward and wraps her breasts around your hard shaft. They feel warm, soft, and impossibly slippery as she starts to move them up and down along your cock."
        mom "How does that feel, is it good?"
        me "Yeah, it feels amazing Mom. Just keep going like that."
        "Mom pushes her tits together even harder and speeds up."
        mom "I don't have a lot of time before I'm late, so I need you to finish as soon as you can. Can you do that for me?"
        me "Keep that up and I'll be done real soon Mom."
        "Mom keeps titfucking you with her soapy tits. True to your word, it isn't much longer before you feel your orgasm starting to build."
        me "I'm about to cum Mom."
        if momO.cumslut:
            mom "That's it, give your cum to mommy! I want every last drop on my tits!"
        else:
            mom "Just let it all out, we're in the shower so you don't have to worry about where it goes."
        "She keeps sliding her tits up and down, up and down. You finally gasp and tense up as you climax."
        $ momO.inc_cum_over()
        show mom showerhead5 at right
        "You spray your load out of the top of Mom's cleavage, covering her upper chest and the slope of her breasts. She slows down once you're done, then finally sits back and sighs."
        mom "There we go, all done sweety. Did you have a good time?"
        me "Yeah, I did. That was amazing Mom."
        "Mom stands up and moves in front of the shower head, washing your cum off of her chest."
        mom "Excellent. Would you mind washing my back for me now?"
        "You finish your shower with Mom, then head off to your room to get dressed."

        $ mom_shower.inc_level(1)
        $ momO.change_resist(-mom_shower.use_red(1, momO.resist_score))

    elif momO.slut_score < 100:
        # Opens door and joins you in the shower, gives you sloppy blowjob.
        "You've just gotten the water to the perfect temperature when the door to the bathroom opens up."
        show mom night at right
        mom "Hey sweetheart, sorry to bother you. I've got an early meeting and I was wondering if I could join you."
        show mom nightstrip1 at right
        "Mom steps into the bathroom and closes the door behind her. She starts to pull her tanktop over her head, letting her breasts fall free."
        me "Sure, there's plenty of room. Come on in."
        show mom nightstrip3 at right
        "You watch as your mom pulls down her sweatpants, then her panties. She kicks her clothes into a pile and steps into the shower with you."
        mom "Thank you sweetheart, you're always so considerate. Oh, and I see we have a little visitor with us too."
        "Mom looks down at your crotch, where your cock is standing rock hard. She reaches down, wraps her hand around it, and begins to stroke it slowly."
        mom "You've been nice enough to share the shower with me, I feel like it's only right I help you take care of this... Don't you agree?"
        me "I think you're right Mom. What did you have in mind?"
        $ momO.inc_blow()
        "Mom strokes your shaft for a few more seconds, then drops to her knees in front of you. She holds the tip of your penis up and licks the bottom of your shaft, sending shivers up your spine."
        mom "Something like this..."
        show mom showerhead1 at right
        "She slides the tip of your cock into her mouth and sucks on it, then starts to slip it farther back. Her tongue keeps licking at the bottom and sides of your dick as she pushes it all the way down her throat."
        "Mom pauses when her nose taps your stomach, holding herself in place for a few long seconds. You feel her throat spasm lightly around your cock a few times."
        "She finally slides back and takes a couple of deep breaths."
        me "Damn, that felt amazing Mom."
        if momO.freeuse:
            mom "I knew you'd like it. Now how about I just open my mouth and let you use it however you want? Does using my mouth like a fuck toy sound nice?"
        else:
            mom "I thought you'd like it. Since we're in the shower I don't mind if you get a little more rough with my mouth, if you'd like that."
        me "Yeah, I think I'd like that."
        show mom showerhead2 at right
        "Mom opens her mouth wide and places her hands on her thighs. You slide your cock back into her mouth, then start to pump in and out."
        "You place a hand on the back of Mom's head to hold her in place and start to speed up. She gags softly as you tap the head of your penis against the back of her throat, but otherwise keeps still for you."
        me "God that feels nice Mom. I think you're going to have me cumming soon."
        if momO.cumslut:
            "She moans and her eyes roll up slightly, unfocused. You feel her shiver with pleasure at the thought."
        else:
            "She looks up at you, staring you in the eyes while you fuck her mouth."
        "You place another hand on your mom's head and pick up the pace. Her drool mixes with the shower water and flows down her chest as you fuck her face."
        me "Yeah, I'm going to cum!"
        "Mom tries to moan something, but keeps getting interupted by your cock slamming into the back of her throat. All she gets out are a series of wet gagging noises."
        menu:
            "Cum on her face.":
                 "You keep thrusting in and out of your mom's mouth right up until you start to cum. Then you pull out and rest the tip of your cock on her chin while you stroke yourself off."
                 $ momO.inc_cum_over()
                 show mom showerhead4 at right
                 "Mom closes her eyes and waits patiently as you pulse your thick load across her face. When you're finally finished you wipe the last few drops off on her lips and let go."
                 mom "Wow, thank you sweetheart. I didn't expect you to give me so much..."
                 me "That felt great Mom. We really need to do this again some time."
                 show mom nightstrip3 at right
                 "Mom stays on her knees for a few seconds so you can have a good look, then stands up and turns towards the shower head to wash your cum off."
                 mom "Well you're always welcome to share the shower with me, and I'll take care of you as best I can."
                 me "Same goes for you, you can join me any time. I think I'm done for now though, I'll talk to you later."
                 hide mom
                 "You step out of the shower and grab a towel. You leave and head towards your room while Mom is washing her hair."

            "Cum down her throat.":
                "You keep thrusting in and out of your mom's mouth right up until you start to cum. Then you pull hard on the back of her head, forcing her deeper onto your shaft."
                $ momO.inc_cum_mouth()
                $ momO.inc_cum_swallow()
                show mom showerhead3 at right
                "Mom closes her eyes and trembles as you start to empty your balls right into her stomach. You hold her in place until you're completely done, then let her pull off slowly."
                "Once she's clear of your cock she takes a deep breath and turns to the side."
                mom "I... Wow... I didn't... Ah..."
                me "That was great Mom, you knew exactly what I needed."
                "She runs the back of her hand along her lips and takes another deep breath."
                mom "I'm just glad you had a good time sweetheart."
                show mom nightstrip3 at right
                "You step out of the shower and grab a towel while your mom stands up."
                me "That was a nice shower Mom, you're welcome to join me any time you want."
                mom "The same goes for you, of course. I'm going to take a few more minutes in here, I'll talk to you later."
                hide mom
                "You wrap the towel around yourself and head to your room to get dressed."

        $ mom_shower.inc_level(2)
        $ momO.change_resist(-mom_shower.use_red(2, momO.resist_score))
    else:
        # Comes in for a shower quicky.
        "You've just gotten the water to the perfect temperature when the door to the bathroom opens up."
        show mom night at right
        mom "Hey sweetheart, mind if I join you?"
        show mom nightstrip1 at right
        "Your mom steps into the bathroom and closes the door. She starts stripping off her clothes before you even answer."
        me "Sure Mom, there's plenty of room in here."
        show mom nightstrip3 at right
        "You watch as your mom pulls down her sweatpants, then her panties. She kicks her clothes into a pile and steps into the shower with you."
        mom "Thank you, you're always so sweet to me."
        "Mom gets under the showerhead and starts to wash her hair. It doesn't take Mom very long to notice your rock hard erection as it brushes against her ass."
        mom "Oh my, what do we have here..."
        "She turns around and takes a good long look at your cock."
        me "Sorry Mom, you're just looking really good today."
        mom "No need to apologize sweety. I mean, if we're both going to be in here at the same time we might as well take care of this, right?"
        "Your mom wraps her hand around your shaft and strokes it a few times."
        mom "How about I just bend over like this..."
        show mom showerfuck1 at right
        "She lets go of your cock and turns around, bending over and placing her hands against the wall of the shower."
        mom "And you just slip inside of me? Would you like that?"
        $ momO.inc_sex()
        "You rub the tip of your cock against her pussy, feeling how wet she is already. She shivers a little when you finally push forward and slide into her."
        mom "Ah... I'll take that as a yes."
        "You grab onto your mom's hips and start to pump back and forth."
        me "Fuck, you feel amazing Mom."
        if momO.freeuse:
            mom "Use me however you want, I just want to help take care of you. Ah..."
        else:
            mom "Just have a good time sweetheart. Ah..."
        "Mom pants and moans as you speed up. The combination of the warm shower water running over your back and Mom's warm pussy wrapped around your shaft feels incredible."
        mom "I can feel you twitching, are you going to cum soon?"
        me "Yeah, I'm almost there."
        if momO.cumslut:
            mom "Give it to me then! I want you to give me a nice thick load!"
        else:
            mom "Finish wherever you want, I can get cleaned up after."
        menu:
            "Cum inside of her.":
                me "Fuck, here I cum!"
                $ momO.inc_cum_inside()
                "You pull back hard on your mom's hips, pushing yourself deep inside of her. She gasps as you start to pulse out your load."
                if momO.preg_response_ok():
                    if momO.cumslut:
                        mom "That's it, fill me up! I want every last drop!"
                    else:
                        mom "Oh god, that's it... Ah..."
                else:
                    mom "I hope you don't get me pregnant like this one day..."
                show mom showerfuck3 at right
                "When you're done you pull out and step back, watching as a few drops of your semen drip out and are washed down her leg."
                me "Damn, that was great Mom."
                "Mom stands up and turns to you with a smile on her face."


            "Cum on her ass.":
                me "Fuck, here I cum!"
                $ momO.inc_cum_over()
                show mom showerfuck2 at right
                "You give her one last thrust, then pull out rest the tip of your cock on her ass cheek. She gasps slightly when the first pulse of cum shoots out over her butt."
                mom "There it is, ah..."
                "You keep stroking yourself off until you're finished. Then you wipe the tip of your cock off on her and step back to admire the view."
                me "Damn, that was great Mom."
                "Mom stands up and turns to you with a smile on her face. She gets under the showerhead and starts to wash your sperm off of her."

            "Cum on her face.":
                me "Fuck, here I cum! Get on your knees for me!"
                "You pull out of your mom's cunt and step back, giving her room to turn around. She drops to her knees in front of you and looks up."
                if momO.cumslut:
                    mom "Come on, cover me with it. I want it [inputName], I want every last drop!"
                else:
                    mom "Okay, I'm ready."
                $ momO.inc_cum_over()
                show mom showerhead4 at right
                "You stroke your shaft a few times and push yourself over the edge. You grunt as you climax, pumping your load out over your mom's waiting face. She holds still as you cover her with your sperm, eyes locked on yours."
                "When you're done you wipe the last few drops off on her chin and step back to admire the view."
                me "Damn, that was great Mom."
                "Mom stands up and smiles at you. She gets under the showerhead and starts to wash your cum off her face."

        mom "It was good for me too. Now I should really be getting ready for work or I'm going to be late."
        "You spend another minute in the shower cleaning yourself off, then step out and grab a towel. You leave Mom in the bathroom and head back to your room to get ready."



        $ mom_shower.inc_level(3)
        $ momO.change_resist(-mom_shower.use_red(3, momO.resist_score))
    return

#######################
##Nora's Minor Scenes##
#######################

label min_nora_walk_in:
    if noraO.slut_score < 50: #Just shirtless.
        show nora strip1 at right
        nora "Hello [inputName], need anything?"
        "Before you respond, Nora looks down at herself."
        nora "Oh, right! Sorry, I was doing some paperwork and was feeling a little warm. I should get my labcoat."
        me "No, don't worry about it Nora, it doesn't bother me."
        nora "Okay, good. It's a good thing you stopped by actually, there's some paperwork that needs to get done. Do you mind?"
        me "Sure, I guess that's no problem."
        "You pull a chair up to a desk and Nora comes over with a stack of papers. She dangles her tits in front of you as she puts them down, then heads back to her desk."
        "You chat about nothing in particular for the rest of the evening while you help her with her paperwork. As it gets late you walk up to ground level together and say goodbye."
        $ nora_walk_in.inc_level(0)
        $ noraO.change_resist(-nora_walk_in.use_red(0,noraO.resist_score))

    elif noraO.slut_score < 70 and not noraO.exhib: #Just Panties.
        show nora strip6 at right
        nora "Hello [inputName], need anything"
        "Nora's standing near her desk with a stack of papers in her hands, wearing nothing other than her panties."
        me "No, I had some free time though so I thought I'd come by and see if I could help out. I see you've been getting comfortable while you work."
        $ noraO.inc_naked()
        "She looks down, as if realising she's almost completely naked."
        nora "Oh, right. It was getting a little warm, and nobody else was around. I hope you don't mind."
        me "Not at all, I think I like it actually."
        nora "Good, I find it really helps with concentration. Anyway, it's good you came by. I've got some paperwork that needs to be done. Do you mind helping?"
        me "Sure, no problem at all."
        "You grab a chair and sit down at a desk. Nora comes over with a stack of papers and lowers them onto your desk, dangling her tits in front of you while she bends over."
        "You and Nora chat with each other for the rest of the evening while you help her with paperwork. You also spend your time enjoying looking at her naked tits whenever you can."
        "When it gets late Nora gets dressed again and you walk up to the ground floor together, then say goodbye."
        $ nora_walk_in.inc_level(1)
        $ noraO.change_resist(-nora_walk_in.use_red(1,noraO.resist_score))

    else: #Touching herself, wants your help.
        show nora strip5 at right
        nora "Oh, hey [inputName]. I didn't expect you here so late. Do you need something?"
        "Nora's sitting at her desk with some papers scattered in front of her. You can see all of her clothes folded neatly beside the desk, including her bra and panties."
        me "Nothing in particular. I had some free time so I figured I'd come down and see if you needed anything. I hope I'm not interrupting anything."
        if noraO.exhib:
            nora "No, you're not interupting. I was just... I thought I should get comfortable. I suppose I'm lucky it was you who walked in though, if it was my boss..."
            "Nora bites her lip and sighs."
            nora "Anyways, if you're already here would you like to sit down and help me with some paperwork? There's plenty here."
        else:
            nora "No, no. I'm just doing some paperwork and figured I might as well be comfortable. There's plenty here, if you'd like to join me."
        me "Sure, sounds fun."
        "You pull up a chair and sit down at the desk beside Nora. She slides over a pile of papers and you both get to work."
        "You and Nora chat a little as the evening goes on, but you notice she's talking less and less. instead of talking, you spend your time taking glances at her amazing tits and legs."
        show nora mast1 at right
        $ noraO.inc_naked()
        "When you look over one time, you see her hand has moved from the desk to her thigh. She's rubbing herself gently."
        "After a few minutes the hand drifts down her inner thigh, then slides up to her crotch."
        me "Having fun there Nora?"
        nora "Hmm?"
        "Nora looks down at her own lap."
        nora "Oh, I didn't even realise. My mind must have been drifting."
        me "Something else must be on your mind,. Is there something distracting you."
        "Nora doesn't say anything, but her hand keeps moving between her legs."
        nora "Okay, maybe something is distracting me."
        "She spreads her legs and rubs a finger over her clit, moaning slightly."
        if noraO.freeuse:
            nora "Could you play with me [inputName]? I want you to touch me so badly..."
        else:
            nora "Could you help me out? We really need to get this work done, and it'll go faster if I'm focused."
        menu:
            "Finger her.":
                "You nod and slide your chair over beside Nora. You rub her thigh a little, then slide your hand over her pussy."
                "She lets out a long breath, then gasps as you slide two fingers inside her. Her slit is warm and already dripping wet."
                me "You're really wet, you definitely need this."
                "Nora nods and breaths deeply as you slide your fingers in and out."
                show nora mast2 at right
                "She lowers one hand to her crotch and rubs her clit while massaging a breast with the other."
                "You pleasure her for a few minutes, the only sound her quiet moans and gasps."
                nora "I'm almost there, keep going."
                me "Good, cum for me Nora."
                "You slide a third finger inside and finger her faster. She leans hard against your hand, core muscles twitching."
                nora "Oh fuck."
                "She tenses up and you can feel her pussy convulse around your fingers. She stays tight for a moment, then relaxes suddenly."
                "You slide your fingers out, wet with her juices, as she leans back and takes a deep breath."

            "Eat her out.":
                "You nod and walk over to Nora, then get on your knees in front of her."
                nora "Ooh, full service. How nice."
                "You smile and raise a hand to her pussy. You rub your fingers along slowly, then spread her lips and lean your head in."
                show nora head1 at right
                "You press your lips to her slit and slip your tongue inside. Nora gasps and places a hand on the top of your head."
                nora "Oh fuck, that feels great."
                "You keep licking her, tasting her salty juices as you plunge your tongue inside. Flicking your tongue over her clit causes her to moan and hold onto your hair tight."
                "After a few minutes Nora is breathing loudly and pressing her hips into you. One hand is massaging a breast while the other is grasping at your hair and pulling you towards her."
                nora "I'm almost there, please don't stop!"
                "You run your tongue around a few more times, then nibble her clit a little bit. She twitches with each movement, moaning loudly."
                "Finally you feel her whole pussy convulse and she arches her back on the chair. She presses your head into her slit and you lick her as fast and hard as you can."
                "Nora finally relaxes and lets go of your head. You pull back and smile up at her."
        me "How was that?"
        nora "Amazing. I feel so much better."
        me "Good. Think you'll be able to focus?"
        "She nods and turns back to her paperwork. You finish off as much work as you can together, then she gets dressed and you walk to ground level together and say goodbye."
        $ nora_walk_in.inc_level(2)
        $ noraO.change_resist(-nora_walk_in.use_red(2,noraO.resist_score))
    return

label min_nora_panty_play_1:
    "You find one of the drawers on Nora's desk locked. A quick pull up and to the side slips the flimsy desk latch out of the way and lets you pull it open."
    "There are a few small notebooks at the bottom with some unimportant banking information, and a small black cardboard box. The box is empty, except for a small remote with a slider going from 0 to 10 that fits in the palm of your hand."
    "You slide the slider up and down, but don't notice any effect."
    "Down the hallway you hear the voices of Nora and Stephanie."
    "You close the drawer, which locks properly when closed. You keep the remote as you rush to your desk."
    "You try to look busy while the door lock beeps and unlocks."
    show steph work at right
    show nora work at left
    steph "Oh hey [inputName], glad you made it."
    nora "We got you a smoothie."
    me "Thanks girls. Much appreciated."
    steph "We've got some reports to get done, so we thought we'd grab some drinks before getting started."
    "The three of you settle down at your desks and Nora spreads the work around evenly. For a while it's silent in the lab while you're all focused."
    "As boredom grows you begin playing with the remote, turning it over in your hand and investigating it."
    "You slide it up to 10, still wondering what it does, when Nora yells in surprise."
    "Startled, you slide it down again."
    steph "Everything okay Nora?"
    nora "Uh, ya. Sorry, just sat on something. Just, ah, go back to your work."
    "Nora does a few minutes of paperwork, then glances around and pulls out a key from her pocket. She unlocks the bottom drawer and searches around."
    menu:
        "Play with Nora.":
            "Realising what the remote is, you slide the slider up slowly. Nora speeds up her search of the drawer, throwing her papers onto the desk."
            "You spike the remote up to 10 and Nora slams the drawer closed suddenly."
            steph "Ah!"
            nora "Sorry! Just slipped."
            "Stephanie gives Nora a strange look, but turns back to her work. Nora looks around the room with a mix of panic and pleasure."
            "As her gaze sweeps the room you slide up the slider on the remote, ending on 10 when she locks eyes with you."
            "You smile and hold up the remote in your hand."
            "Nora looks shocked for a moment, then shudders a little and turns back to her desk."
            "For the next hour or so you toy around with Nora by turning up the remote when she's most focused on her work."
            "You hear her moan a few times, and at least twice she has to stop and take a moment to regain her composure as she orgasms."
            "As the shift comes to an end you stand up to go to the bathroom and lay the remote gently on Nora's desk."
            $ nora_panty_play.inc_level(0)
            $ noraO.change_resist(-nora_panty_play.use_red(0,noraO.resist_score))
        "Return the remote.":
            "Worried about getting in any trouble with your boss, you stand up and go to walk out of the room. As you pass Nora's desk you drop the remote on a pile of paper."
            me "Going to the bathroom, back in a moment."
            "When you get back the remote is gone."
    return

label min_nora_panty_play_2:
    "You find one of the drawers on Nora's desk locked. A quick pull up and to the side slips the flimsy desk latch out of the way and lets you pull it open."
    "There are a few small notebooks at the bottom with some unimportant banking information, and a small black cardboard box. The box is empty, except for a small remote with a slider going from 0 to 10 that fits in the palm of your hand."
    "You slide the slider up and down, but don't notice any effect."
    "Down the hallway you hear the voices of Nora and Stephanie."
    "You close the drawer, which locks properly when closed. You keep the remote as you rush to your desk."
    "You try to look busy while the door lock beeps and unlocks."
    show steph work at right
    show nora work at left
    steph "Oh hey [inputName], glad you made it."
    nora "We got you a smoothie."
    me "Thanks girls. Much appreciated."
    steph "We've got some reports to get done, so we thought we'd grab some drinks before getting started."
    "The three of you settle down at your desks and Nora spreads the work around evenly. For a while it's silent in the lab while you're all focused."
    "As boredom grows you begin playing with the remote, turning it over in your hand and investigating it."
    "You slide it up to 10, still wondering what it does, when Nora yells in surprise."
    "Startled, you slide it down again."
    steph "Everything okay Nora?"
    nora "Uh, ya. Sorry, just sat on something weird. Just, ah, go back to your work."
    "Nora does a few minutes of paperwork, then glances around and pulls out a key from her pocket. She unlocks the bottom drawer and searches around."
    menu:
        "Play with Nora.":
            "Realising what the remote is, you slide the slider up slowly. Nora speeds up her search of the drawer, throwing her papers onto the desk."
            "You spike the remote up to 10 and Nora slams the drawer closed suddenly."
            steph "Ah!"
            nora "Sorry! Just slipped."
            "Stephanie gives Nora a strange look, but turns back to her work. Nora looks around the room with a mix of panic and pleasure."
            "As her gaze sweeps the room you slide up the slider on the remote, ending on 10 when she locks eyes with you."
            "You smile and hold up the remote in your hand."
            "Nora looks shocked for a moment, nods and smiles."
            nora "Stephanie, could you go check the supply room for a stapler? I think mine is on it's way out."
            steph "Uh, ya. Sure. Back in a moment."
            hide steph
            show nora mast3 at right
            $ noraO.inc_naked()
            "Stephanie leaves the room, and Nora wastes no time in pulling her pants off."
            if noraO.freeuse:
                nora "You don't have to stop, play with me as long as you want."
            else:
                nora "Don't stop."
            "You increase the slider and watch as Nora's unusual black panties vibrate slightly. She leans back in her chair and moans."
            "For a few minutes you pulse the remote up and down, playing with Nora's pleasure. As time goes on she looks at you desperately."
            "Knowing Stephanie will be back soon you slide the remote all the way up to 10 and leave it there while Nora gasps and leans hard on her table."
            "She hits the table with her palm a few time as she orgasms."
            "You ease the slider down to 0 and leave Nora panting and sweating."
            show nora work at left
            show steph work at right
            "When she's able she gets her pants on again, only a minute or two before Stephanie comes back in."
            steph "Here you go, took awhile to find."
            if noraO.freeuse:
                nora "Thank you Stephanie. [inputName] did some really great work while you were gone. I think we're nearly done for the day after everything he did..."
            else:
                nora "Thank you Stephanie."
            "A few minutes later you get up to go to the bathroom and place the remote to Nora's panties gently on her desk."
            $ nora_panty_play.inc_level(1)
            $ noraO.change_resist(-nora_panty_play.use_red(1,noraO.resist_score))

        "Return the remote.":
            "Worried about getting in any trouble with your boss, you stand up and go to walk out of the room. As you pass Nora's desk you drop the remote on a pile of paper."
            me "Going to the bathroom, back in a moment."
            "When you get back the remote is gone."
    return

label min_nora_nudes:
    if noraO.slut_score < 40: #Driving, can't talk now
        nora "Can't talk. Driving. 5 minutes."
        "You sit around and wait, and Nora eventually responds again."
        nora "Hi [inputName], sorry about that. I had to make a trip to pick something up after work, so I've been driving around all night."
        me "No problem. I just thought I'd check in and say hi."
        nora "It's good to hear from you. I've had an exhausting day though. I think I'm just going to go straight to bed."
        me "Alright. Goodnight Nora."
        nora "Goodnight [inputName]."
    elif noraO.slut_score < 70: #Shows off her new lingerie
        nora "Driving. 5 minutes. Something to show you."
        "You sit around and wait, wondering what Nora has to show you when she's done driving."
        nora "Ah, there we go! Home safe and sound."
        me "Good to hear! Out late I see."
        nora "Yes, I had to go pick something up. Want to see what it is?"
        me "You've got me curious now. I'd love to."
        "There's a long pause, then a picture is sent to your phone from Nora."
        show nora strip13 at truecenter
        $ noraO.inc_naked()
        "She's posing for you, wearing a black translucent baby doll and fishnet stockings. She's even taken her glasses off for the picture."
        nora "What do you think?"
        me "Wow! You look great!"
        nora "Thanks. I think it makes my butt look nice too."
        show nora strip14 at truecenter
        "Another picture, this time from behind with Nora bending over just a little."
        me "I have to agree. You look stunning."
        nora "Now you're just sucking up to the boss."
        me "Hey, I'm just telling the truth. Objective observations are the basis of good science, after all."
        nora "Of course. Now It's getting late, so I'm off to bed. Have a good night [inputName]."
        me "You too Nora."
        $ nora_nudes.inc_level(0)
        $ noraO.change_resist(-nora_nudes.use_red(0,noraO.resist_score))
    else: #Video of her riding her new dildo, in her new lingerie. Change if you've already seen the lingerie before? Just mention the dildo?
        nora "Driving. Wait 5 minutes. Promise you'll like it."
        "You sit around and wait, wondering what Nora has to show you."
        nora "There we go, home at last. Curious what I was out doing?"
        me "Very, now that you mention it."
        nora "Well, there's a little shop on the other side of town that sells lingerie. I've had my eye on something for awhile."
        "You get a picture from Nora."
        show nora strip13 at truecenter
        $ noraO.inc_naked()
        "She's posing for the camera in a translucent black baby doll and fishnet stockings."
        nora "Do you like it?"
        me "Like it? You look amazing."
        nora "That's not all though. They also sell toys there, and I just couldn't resist it on my way out."
        nora "One moment, I think I can take video with this thing."
        "There's a long pause, then you get a short video clip sent to your phone. You open it up immediately."
        show nora mast4 at truecenter
        "Nora's on her bed with her legs spread and a large pink dildo inside her. She's rocking her hips up and down, sending her tits bouncing with each stroke."
        if noraO.exhib:
            nora "Hello [inputName], do you like what you see? I want you to watch me ride this and cum, then save it for later and use it so you can cum too. Ah!"
        "She rides the dildo for a while, then takes a sudden deep breath and leans forward."
        show nora mast5 at truecenter
        "Her legs tremble as she orgasms, and she lets out a soft moan. The video ends with her collapsed on the bed with the toy still inside her."
        me "Wow."
        nora "Ya. I'm a little tired after that. Talk to you later?"
        me "Sure thing. Goodnight."
        nora "Goodnight."
        $ nora_nudes.inc_level(1)
        $ noraO.change_resist(-nora_nudes.use_red(1,noraO.resist_score))
    return

label min_nora_housework_1:
    me "Sure Nora, I think I could spare the time. I'll check the bus schedules and come over."
    nora "Sounds good."
    "You check online and find the right busses, and an hour later you're walking up to the door of Nora's bungalow."
    "A few seconds after ringing the bell the door is opened."
    show nora casual
    nora "Ah, glad you found the place okay."
    me "No problems. So, there's some furniture to move?"
    "You come inside, and Nora shows you to a wardrobe sitting in her bedroom."
    nora "I need to move it to the other side. If you get one end it should be easy enough."
    "The two of you take up positions on either end and lift. You manage to get it a few inches off the ground, then both decide it's too heavy."
    me "Wow. What do you have in there?"
    nora "My clothes. I figured I could save some time and not empty it if you were coming over. No such luck I suppose. Give me one moment."
    "Nora pulls open the doors and takes a pile of dresses out, then goes through the drawers and drops everything on her bed."
    "She empties her underwear drawer last. You spot a few different sets of silk and lace panties mixed in with the pile, along with matching bras."
    nora "There, that should be better."
    "You try again, and this time the two of you are able to walk the wardrobe over to the other side of the room to it's new position."
    nora "Excellent. Well, how about I order us that pizza then. Thanks again for your help [inputName]."
    "You spend another hour or so at Nora's house enjoying a pizza with her, then catch a bus home."
    return

label min_nora_housework_2:
    me "Alright, you've got me curious now. I'll be over in a little bit."
    nora "See you soon."
    "You check online and find the right busses. Within an hour you're walking up to the door of Nora's bungalow."
    "A few seconds after ringing the bell the door is opened"
    show nora casual at right
    nora "[inputName]! It's good to see you."
    me "Hey Nora. Good to see you too. So what do you need help with?"
    nora "I'm trying to move my wardrobe, but it's a little heavy. Follow me."
    "Nora leads you into her bedroom and motions to a large wood wardrobe against one wall."
    nora "I think we can move it if we work together."
    me "Worth a shot."
    "The two of you get on either side and lift, but after lifting it up a few inches you both decide it's too heavy."
    nora "Hmm. I was hoping to avoid this, but I'll have to empty it out. One moment."
    "Nora opens it up and starts pulling out her clothes. The last drawer is where she keeps her underwear."
    "She lifts out a few sets of lace and silk panties with matching bras and places them on the bed. Finally she pulls out something silky, black and translucent."
    nora "Oh ya, I almost forgot about this."
    me "Hmm? What is it?"
    if noraO.exhib:
        nora "Just a little something I like to wear when I want some attention. Let's hurry up and get this moved."
    else:
        nora "Oh, nothing. Let's move this quickly."
    "She puts the piece of lingerie on the bed and gets on the other side of the wardrobe again. This time you have no trouble lifting it and moving it to the other side of the room."
    me "There, all done?"
    nora "Almost. I promised you a reward. Can you go get my purse from the kitchen?"
    me "Sure thing. Back in a moment."
    "You walk around Nora's house for a while, find the kitchen, then search around. After a few minutes of searching you haven't found her purse and give up."
    me "Sorry Nora, I couldn't find it."
    show nora lingerie2 at right
    "You open the door to Nora's bedroom again, and find her sitting on the edge of her bed. She's wearing a black transparent baby doll, with fishnet stockings and lacy gloves."
    nora "Don't worry about that, I think I've thought of a better way."
    "She motions with her finger for you to come forward. When you're a few steps from her she slides off the bed onto her knees, and unzips your pants."
    if noraO.freeuse:
        nora "You've been so nice to me, I thought a nice, long, blowjob would be a good way to pay you back."
    else:
        nora "This is my way of thanking you for taking the time to come out here."
    show nora lingerie3 at right
    $ noraO.inc_blow()
    "She slides your pants down, freeing your already hard cock. She holds it in one hand and licks it on one side, then moves her head over and licks it along the other."
    me "Damn, that feels good."
    nora "Just relax and enjoy it."
    "She takes your tip into her mouth and swirls her tongue around, then starts to slide her head back and forth rhythmically."
    "Leaning over her you can get a great look at her ass while she blows you. Her tits bump into your thighs with each stroke of her throat."
    "Within a few minutes you're ready to finish."
    me "Nora, I'm almost there! Don't stop!"
    "Nora speeds up her blowjob, making a point of running her tongue down the bottom of your shaft on each pass."
    if noraO.cumslut:
        "You moan softly as you start to cum. Nora keeps the tip of your cock on her lips as you start to pulse out your load into her mouth. She closes her eyes and shivers with pleasure."
        show nora lingerie13 at right
        $ noraO.inc_cum_mouth()
        $ noraO.inc_cum_swallow()
        "When you've finished cumming Nora leans back and opens up her mouth, showing off the pool of off-white semen in side. You take a good look, then sit down on her bed to catch your breath."
        "Nora plays with your cum a little longer before gulping it down."
        nora "Mmm, thank you [inputName]. You've been a huge help today."
        me "My pleasure."
        show nora lingerie1 at right
        "Nora sees you to the door and says goodbye a few minutes later."
    else:
        show nora lingerie4 at right
        $ noraO.inc_cum_over()
        "You moan softly as you start to cum, and Nora pulls you out of her mouth. She strokes your wet cock as you fire your load all over her tits."
        "When you're done you sit down on Nora's bed to catch your breath."
        nora "Well, thank you very much for the help [inputName]."
        me "My pleasure."
        show nora lingerie5 at right
        "Nora sees you to the door and says goodbye with her tits still covered in your cum."
    $ nora_housework.inc_level(0)
    $ noraO.change_resist(-nora_housework.use_red(0,noraO.resist_score))
    return

label min_nora_housework_3:
    me "Alright, I'll be over as soon as I can."
    nora "See you soon!"
    "You check the bus schedules and head out. Within an hour you're ringing the doorbell on Nora's small bungalow."
    show nora lingerie1 at right
    "The door opens quickly, and Nora is standing inside wearing a black translucent baby doll, fish net stockings, lace panties, and lace gloves."
    nora "Hello there [inputName], thanks so much for coming over."
    if noraO.exhib:
        "Nora stays at the door in her lingerie while she talks to you, in clear view of the street and her neighbours."
        me "You're looking very nice. What's the occasion?"
        nora "Well, I was clearing out a wardrobe so we would be able to move it, and I found this. I hope you like it."
        me "I love it, and I'm sure everyone else does too."
        "Nora glances past you and bites her lip. She closes her eyes and sighs softly, trembling just a little bit."
        nora "I wonder if anyone's watching us right now... I shouldn't make you wait though, you've been so nice comming out here all this way. Come with me."
        "Nora grabs your hand and pulls you into the house, then closes the door. She leads you through her house and to her bedroom."
    else:
        "Nora steps back from the door so you can come in, then closes it behind you."
        me "You're looking very nice. What's the occasion?"
        "Nora guides you through her house, eventually opening the door to her bedroom."
        nora "Well, I was clearing out a wardrobe so we would be able to move it, and found this. I hope you like it."
        me "I love it, you look fantastic."
        nora "And I was thinking that you've been so nice, coming out here just to help me. It would be rude to make you wait for your reward."
    show nora lingerie6 at right
    "Nora lies down on the bed with her ass towards you and turns to look at you."
    nora "What do you think? Would you like your reward right now?"
    me "I think I would."
    "You pull off your shirt and pants, then climb onto the bed with Nora. She takes you in her arms and pulls you into a deep kiss."
    "After a few minutes of making out, you roll on top of her. You rub the tip of your cock along her pussy through her thin, lacy underwear."
    nora "Oh wow, you're just teasing me now."
    me "Maybe. Do you like it?"
    nora "I'm dripping wet, hurry up and take me!"
    show nora lingerie7 at right
    $ noraO.inc_sex()
    me "You reach down and pull her panties to the side, then slide yourself in. Nora moans as you sink yourself balls deep."
    "Nora wraps her arms around you and pulls you close while you start to pump in and out of her."
    nora "Oh god, you feel so big."
    "After a few minutes of fucking Nora missionary, you slip out of her with a wet pop."
    me "Slide over to the edge of the bed."
    "Nora nods and does what you want. You stand up and guide her so her waist it on the edge. You reach down and grab her ankles, then pull her legs high up above her to form a V."
    if noraO.anal:
        nora "Wait, I want you to slip it into my ass. Just for a little while."
        show nora lingerie14 at right
        "You lower Nora's legs a little and aim your cock lower, pressing your tip against her tight asshole. She gasps as you push forward and slide yourself inside."
        nora "Oh fuck! You're so big, It feels so... Ah!"
        me "That's a good girl, your ass feels amazing. So nice and tight."
        "You hold onto her legs and fuck her asshole as fast as you can manage. She twitches and pants on the bed beneath you."
        "After you've fucked her ass for a few minutes you pull out again and line yourself up with her pussy."
        me "That was great, but I think I want some more of this too."
        nora "Whatever you want [inputName], thank you..."
    else:
        nora "Ah, don't make me wait. Please?"
    show nora lingerie8 at right
    "You guide your cock back into Nora's dripping pussy. Your new position lets you drive yourself especially deep into her."
    nora "Oh fuck, oh fuck. I think I'm going to cum."
    me "Good girl, you deserve it."
    "You pull hard on her legs to give yourself more leverage and fuck her as fast as you can. After a few moments Nora starts to twitch on the bed beneath you as she lets out a loud, passionate moan."
    me "It's my turn now. Ready to give me my reward?"
    "Nora looks up and nods weakly, still trembling from her orgasm. With each thrust her pussy tightens up around you a little."
    menu:
        "Cum inside her.":
            "You keep fucking Nora until you're ready to finish. Then you spread her legs wide and hold yourself deep inside her, moaning softly as you pump her full of your cum."
            show nora lingerie9 at right
            $ noraO.inc_cum_inside()
            "Nora takes a long shuttering breath as you finish, gasping a little with each new pulse. When you're finished you pull out, keeping her legs spread so you can appreciate your handiwork."
            me "Well that was certainly an amazing reward Nora."
            if noraO.preg_response_ok():
                nora "I'm glad... Ah... Glad you liked it."
            else:
                nora "I'm glad... We need to be more careful though or I'll end up pregnant."
            "You let her legs go, and they slump back over the edge of the bed. Nora just lays still, panting softly, while you get your clothes back on."

        "Cum all over her.":
            "You keep fucking Nora until you're ready to finish. Then you pull out and stroke yourself off, firing your load over the length of Nora's body."
            show nora lingerie10 at right
            $ noraO.inc_cum_over()
            "Nora gasps softly as each new pulse of cum lands on her, first her face, then tits, then stomach and pussy. When you're done you hold her legs up and wide a little longer to admire your handiwork."
            me "Well, that was certainly an amazing reward Nora."
            if noraO.cumslut:
                nora "I think I should be thanking you. All this... It feels so nice..."
                "Nora runs a finger over her cheek, scooping up some of your cum, then slides it into her mouth and licks it clean. She shivers a little, obviously still turned on."
                nora "Mmm, it tastes so good... Just give me a moment, I want to stay like this for a little longer."
                "You let go of her legs, and they slump back over the edge of the bed. Nora stays still for a few minutes, lazily playing with your cum."
                "Eventually you've got your clothes back on, and Nora heads off to the bathroom to clean off any of the semen she hasn't already licked off of herself."
            else:
                nora "I'm glad. Ah... Glad you liked it. I think I might have to get cleaned up."
                "You let go of her legs, and they slump back over the edge of the bed. Nora stays still for a few minutes, panting softly, while you get your clothes back on."
                "Finally, she gets up and ducks into the bathroom to clean herself off. A few minutes later she comes back out with all of your sperm wiped off."

        "Cum in her mouth.":
            "You keep fucking Nora until you're ready to finish. Then you pull out and let Nora's legs fall back over the edge of the bed."
            me "Get down on the floor."
            "Nora slides off the bed, taking most of the sheets with her. She ends up on her ass, leaning against the edge of the bed."
            show nora lingerie11 at right
            $ noraO.inc_cum_mouth()
            if noraO.cumslut:
                nora "Cum right in my mouth [inputName]! I want to taste you so badly!"
                "She leans forwards and takes the tip of your cock in her mouth. She bobs her head back and forth a few times, then pulls back so your cock is just inside her lips as you cum."
                "Nora shivers with pleasure as you pump your load across her tongue, filling up her mouth."
            else:
                "She's still panting hard, but you're ready to finish and don't have time to wait. You place your cock against her mouth and slide yourself in, interrupting Nora's attempts to catch her breath."
                "She looks up at you with half closed eyes while you slide yourself in and out of her mouth a few times."
                "You keep the tip of your cock just past her lips as you start to cum, firing your entire load into Nora's mouth."
            "Without being able to open her mouth her moans sound like a kittens purr, and she's breathing heavily through her nose."
            menu:
                "Make her spit.":
                    me "Good, you can spit it out now."
                    show nora lingerie12 at right
                    $ noraO.inc_cum_over()
                    "Nora opens her mouth a little and lets your cum leak out in a thin curtain. She stays leaning against the bed, trying to catch her breath through just her nose."
                    "Finally the last bit has dribbled out and she looks up at you."
                    nora "Did you have a good time?"
                    me "Oh ya, I did Nora. That made the trip out here well worth it."
                    "She smiles and takes a deep breath."
                    nora "Good. I should go get cleaned up."
                    "Nora pulls her self to her feet and slips into the bathroom. A few minutes later she comes out, having wiped off most of your load."

                "Make her show you then swallow.":
                    me "Now show it to me."
                    show nora lingerie13 at right
                    $ noraO.inc_cum_swallow()
                    "Nora looks up at you and opens her mouth. It's filled with the off white liquid of your cum, and as you watch she sticks her tongue out to lick her lips, spreading it around."
                    me "Good, and now swallow."
                    "She closes her mouth and swallows loudly. She immediately takes a deep breath and starts panting to catch her breath."
                    me "All gone."
                    nora "All. Ah. Ah. Gone."
                    me "I think that's everything I wanted for my reward then. Thank you Nora."
                    nora "You're welcome."
                    "After a few moments she pulls her self up onto the edge of the bed."
    show nora lingerie1 at right
    me "So, wasn't there something I was going to help with?"
    nora "Oh, that? It's a little late. How about you come back some other day, okay?"
    me "Sure thing Nora."
    if noraO.exhib:
        "Nora walks you to the door and down her driveway, still dressed in her lingerie. She waves goodbye while standing half naked in front of her house."
    else:
        "Nora walks you to the door, still dressed in her lingerie."
    $ nora_housework.inc_level(1)
    $ noraO.change_resist(-nora_housework.use_red(1,noraO.resist_score))
    return

label min_nora_pull_over:
    "Your phone rings, Nora is video calling you. You head up to your room and get comfortable on your bed before you answer."
    show nora strip30 at truecenter
    "She's in her car, illuminated by the glow of her phone and the passing street lights. Her phone is attached to her visor, positioned above her and pointing down."
    me "Hey Nora."
    nora "Hey [inputName]. I'm driving and can't text, so I figured we could just do this instead."
    me "Yeah, this is fine. How are you doing?"
    nora "I'm doing well. I finished up at the lab and I'm on my way home. I'm thinking about stopping off and doing some shopping."
    me "What for?"
    if noraO.slut_score < 70:
        nora "A new outfit, maybe. I haven't gotten anything new in a while, and I feel like a I need a pretty back dress."
        me "Sounds cute, you'll have to show it off to me one day."
    elif noraO.slut_score < 110:
        nora "Some new lingerie, maybe. I picked up some new panties and need a garter belt and stockings to go with it. I'll have to show it to you some time."
        me "Sounds sexy, I look forward to seeing it."
    else:
        nora "A few new toys, maybe. My vibrator right now is a little weak. Something small and portable would be nice around the office."
        me "Sounds dirty, maybe I can help you out with that instead."
    nora "Yeah. Uh, wait one moment."
    "Nora stops talking, and you can hear a sudden burst of sirens behind her."
    nora "Oh damn, I'm getting pulled over. Sorry [inputName], I'll be with you in just a second."
    me "No problem, I'll be here."
    "She guides her car to the side of the road and brings it to a stop. Once that's done she reaches up to her phone and fiddles with it, probably turning off the volumn on her end."
    "Nora winds down her window and waits while the police officer gets out of his car and comes up beside hers."
    nora "Evening officer. What seems to be the problem?"
    "Officer" "Good evening. You've got a burned out tail light. Can I see your license and registration."
    "Nora digs through her glove compartment until she has the documents in hand."
    nora "I hadn't noticed, it must have just happened."
    "The police officer grunts and nods, looking at her papers briefly before handing them back."
    "Officer" "Well, you're responsible for checking your vehicle every time you get in. I'm going to have to write you a ticket and you'll need to get this sorted out as soon as possible."
    if noraO.slut_score < 65:
        # Takes the ticket, end of scene
        nora "Isn't there anything you can do? Maybe you could just give me a warning so I have a chance to get this fixed up?"
        "Officer" "Sorry, the law is the law. Here you go, have a good night and drive safe."
        "He punches some numbers into a handheld terminal, which spits out a ticket that he hands to Nora. She takes it and pouts, shoving it in her glove compartment along with her other papers."
        "The police officer returns to his car and drives off, and Nora turns the volumn on her phone back on so she can hear you again."
        nora "Hey [inputName]."
        me "Hey Nora. That really sucks."
        "She shrugs and pulls back out into traffic."
        nora "Nothing I could do I suppose. I'm going to have a quiet drive home if you don't mind. We can talk later."
        me "Okay, talk to you later Nora."
        hide nora
        "You end the call and put your phone away."
    elif noraO.slut_score < 85:
        # Blows him to get out of the ticket.
        nora "Really? Isn't there anything you could do for me? Maybe you could just give me a warning and I'll get this fixed up as soon as I can."
        "Her eyes run up and down the police officers body, pausing a moment when she reaches the bulge in his pants."
        "Officer" "Sorry, the law is the law."
        nora "There's nothing I could do to convince you?"
        "She licks her lips and puffs out her chest, large tits straining against her sweater. You hear the police officer take a deep breath and hesitate."
        "Officer" "Ma'm, I really shouldn't."
        "Nora undoes her seatbelt and opens the door, swiveling to face the police offier."
        nora "It's late, there's nobody else around. Let me make you a heart felt promise I'll get that tail light fixed first thing in the morning."
        show nora blow26 at truecenter
        "She slides off her seat and onto her knees. She's just barely inside the field of view of her phone's camera."
        "The police officer hesitates a few more seconds, during which Nora runs her hands along his legs up towards his waist."
        "Officer" "I want that light fixed as soon as you can manage. If you do that I can let you off with a warning."
        "Nora smiles and grips the zipper on his pants, pulling it down. She reaches inside and caresses his penis, making him moan softly."
        nora "Of course officer, you have my word. Now let me thank you for your civic duty."
        "She pulls his cock out and strokes it slowly with her hand. After a little while she leans in and starts to lick his shaft to get it wet."
        "You watch on your phone as Nora opens her mouth and slips the officers large dick into her mouth. He grunts as she starts to bob her head up and down."
        "For a few minutes everything is silent, other than the sound of traffic near by and the occasional wet pop."
        "Officer" "Ah, ma'm..."
        "Nora pulls off his cock and strokes him off with her hand. She keeps his tip pointed as her face while he climaxes."
        if noraO.cumslut:
            nora "Come on, give it to me. I want to feel your cum all over me!"
            "Nora closes her eyes and waits until he's done covering her face with cum. She runs a finger over her cheek, scooping up some of his sperm then licking it off."
            "Nora shivers with pleasure as she plays with the officers semen, taking a long while before she stands up and gets back into her car, closing the door behind her."
        else:
            "Nora closes her eyes and waits until he is done covering her face with cum. With that done she stands up and gets back into her car, closing the door behind her."
        nora "Thank you for letting me know about the problem officer. I'll get that looked at right away."
        "Officer" "Any time. Have a good night."
        show nora blow27 at truecenter
        "Nora drives off, leaving the police officer to pull up his pants on the side of the road. She reaches up to her phone and turns the volumn back on again."
        nora "Sorry for the interuption [inputName]."
        "She uses one of her hands to wipe his semen away from her eyes."
        me "No problem. Glad you dodged the ticket."
        nora "me too. I think I'm going to just have a quiet drive home if you don't mind. We can talk later."
        me "Okay, talk to you later Nora."
        hide nora
        "You end the call and put your phone away."
        $ nora_copcar.inc_level(0)
        $ noraO.change_resist(-nora_copcar.use_red(0,noraO.resist_score))
    else:
        # Fucks him to get out of the ticket. Condom or not depending on score.
        nora "Really? Isn't there anything you could do for me? Maybe you could just give me a warning and I'll get this fixed up as soon as I can."
        "Her eyes run up and down the police officers body, pausing a moment when she reaches the bulge in his pants."
        "Officer" "Sorry, the law is the law."
        nora "There's nothing I could do to convince you?"
        "She licks her lips and puffs out her chest, large tits straining against her sweater. You hear the police officer take a deep breath and hesitate."
        "Officer" "Ma'm, I really shouldn't."
        "Nora undoes her seatbelt and opens the door, swiveling to face the police offier."
        nora "It's late, there's nobody else around. Just relax and blow off some stress."
        "She stands up and undoes the zipper on her pants, pulling them down a little bit and teasing the officer with a glance at her panties."
        "Officer" "I want that light fixed as soon as you can manage. If you do that I think I can see you off with just a warning."
        show nora fuck35 at truecenter
        "Nora pulls her pants down completely and steps out of them, then turns and bends over the drivers seat of the car. She looks up at her phone and gives you a wink."
        nora "I think there's something other than a warning you could give me."
        "You see the police officer step forward and pull down his zipper. Soon he's got his cock free and resting on Nora's ass cheek."
        $condom = True
        if noraO.slut_score > 110 or noraO.cumslut or noraO.anal:
            $condom = False
            "Next the officer pulls Nora's panties down around her knees and lines his cock up with her pussy."
        else:
            nora "Wait just one moment there."
            "Nora stretches across the car and opens up her glove compartment again, then pull out a small colourful wrapper. She hands the condom package back behind her."
            "The officer pulls it open and slips the condom on. Next he pulls Nora's panties down around her knees and lines his cock up with her pussy."
        if noraO.anal:
            nora "Wait, aim a little higher and slip it into my butt. It's nice and tight and just dying for a good fuck."
            "The police officer holds his cock with one hand, spreading Nora's ass cheeks with the other. Nora gasps loudly as he slides his dick into her ass."
        else:
            nora "Oh yeah, there you go. Give it to me nice and hard."
            "The police officer holds her by the hips and slides himself in, grunting quietly as he goes. Once he's all the way in he pauses, then starts to fuck her."
        "Nora moans softly while he takes her from behind, arching her back and rolling her hips to meet his."
        show nora fuck36 at truecenter
        "You watch on your phone while Nora is fucked doggy style, bent over her seat. Eventually the officer speeds up and squeezes Nora's ass."
        "Officer" "Fuck, here we go!"
        if noraO.cumslut:
            nora "Let it all out! I want you to empty your balls in me!"
        else:
            nora "Just let it all out! Ah!"
        if condom:
            "The officer pushes himself deep into Nora's cunt, trembling while he orgasms. Nora pants heavily while he pumps his cum into the condom."
            "After a few moments he pulls out, pausing for a moment to peel the condom off and drop it to the ground."
        else:
            if noraO.anal:
                "The officer pushes himself deep into Nora's ass, trembling while he orgasms. Nora pants heavily while he fills her up with cum."
            else:
                "The officer pushes himself deep into Nora's cunt, trembling while he orgasms. Nora pants heavily while he pumps her full of cum."
            "After a few moments he pulls out, pausing for a moment to watch his cum drip out of her."
        nora "Ah... Thank you for letting me go with a warning officer. I'll get everything fixed up in the morning."
        "Officer" "Any time, have a good evening m'am."
        show nora strip30 at truecenter
        "He pulls up his pants and heads back to his squad car while Nora collects herself and closes the door to her car. She reaches up to her phone and turns the volume on again."
        nora "Sorry for the interuption [inputName]."
        me "No problem. Glad you were able to dodge the ticket."
        nora "Oh, it's no big deal. I leave that light out just so I have a chance to do this. It works most of the time."
        me "Clever. You certainly gave him a good time."
        nora "He gave me one too. I think I'm going to just have a quiet drive home if you don't mind. We can talk later."
        me "Okay, talk to you later Nora."
        hide nora
        "You end the call and put your phone away."
        $ nora_copcar.inc_level(1)
        $ noraO.change_resist(-nora_copcar.use_red(1,noraO.resist_score))
    return

label min_nora_beach_tan:
    me "I'm thinking we should find a nice sunny spot and just relax."
    nora "That sounds nice. Lead the way."
    "You and Nora head down the beach, looking for a nice sandy spot without many people around."
    "After a few minutes of walking you find an ideal spot. You and Nora lay out your towels next to each other, facing towards the lake."
    "Nora lies back on her towel, closing her eyes and soaking in the sun."
    nora "Excellent spot [inputName]. Oh, before I forget..."
    "Nora sits up again and digs through the small bag she's brought with her. After a quick search she's got a bottle of sunscreen in hand."
    nora "Do you need any?"
    me "Sure, thanks."
    if noraO.slut_score < 45:
        #Asks you to put sunscreen on her back. Gives you a good feel of her ass.
        "Nora gives you a squirt of sunscreen, then plops some into her own hand and starts to spread it around."
        show nora strip31 at right
        "Once she's covered her front she lies down on her towel, face down this time."
        nora "Could you do me a favour and get my back [inputName]?"
        me "No problem. It would suck to end up with a sunburn after a great day like this."
        "You take another squirt of sunscreen and kneel next to Nora. You run your hands along her back, lifting up the straps on her swimsuit to get all of her shoulder blades."
        nora "Thank you. If you could get the back of my legs too, it would be a huge help."
        "You move down, give yourself another squirt of sunscreen, and start to rub her legs."
        nora "Perfect. Just a little higher."
        "You move your hands up, spreading the sunscreen over her thighs. She spreads her legs a little, letting you reach her inner thighs."
        nora "Ah... A little more, please."
        "You move higher still, now rubbing the lower part of Nora's butt. She seems totally relaxed."
        nora "Just pull the swimsuit up a little if you have to, make sure you get some sunscreen all around the edge."
        me "Whatever you say Nora."
        "You work your hands around the periphery of her swimsuit, fingers slipping under the edge. Nora sighs softly as you run your hands over her ass."
        if slut_outfit:
            show nora swim2
        else:
            show nora swim1
        "Nora gives no sign that you should stop. For another minute you play with her ass, making sure every inch is covered with sunscreen. Eventually she rolls over onto her back again."
        nora "Thank you [inputName]. That was a huge help."
        me "Any time Nora."
        "You lie down on your own towel next to her. You pass an hour and a half in the sun, just enjoying the warm summer day."
    elif noraO.slut_score < 75:
        #Strips naked, then asks for you to put some sunscreen on her.
        "Nora gives you a squirt of sunscreen, then plops some into her own hand and starts to spread it around."
        "Nora lifts up the straps of her swimsuit a few times, then sighs and stands up. She pulls the straps over her shoulders, then pulls the entire thing off."
        nora "This is just going to give me some terrible tan lines anyway."
        show nora strip32 at right
        $ noraO.inc_naked()
        "She kicks the swimsuit to the side, then sits back down. She rubs some sunscreen over the front of her body, paying special attention to her breasts. That done, she lies face down on her towel."
        nora "[inputName], could you do me a favour and get my back for me?"
        me "No problem. It would suck to end up with a sunburn after a great day like this."
        "You take another squirt of sunscreen and kneel behing Nora. You run your hands along her back, starting with her shoulder blades and working down to her waist."
        nora "And my legs, if you don't mind."
        me "Of course not."
        "She spreads her legs a little, letting you run your hands along the inside and outside of her thighs."
        nora "A little higher too. I don't want a burned butt, after all."
        "You take another squirt of sunscreen and move up to her ass, rubbing it in gently. Nora sighs softly while you kneed her butt cheeks."
        show nora strip33 at right
        "Nora gives you plenty of time to play with her ass, then rolls onto her back again."
        nora "Thank you [inputName]. That was a huge help."
        me "My pleasure Nora."
        "You lie down on your own towel next to her. You pass an hour and a half in the sun, enjoying the warm summer day whhile you stare at Nora's tits."
        if slut_outfit:
            show nora swim2
        else:
            show nora swim1
        $ nora_beach_tan.inc_level(0)
        $ noraO.change_resist(-nora_beach_tan.use_red(0,noraO.resist_score))
    elif noraO.slut_score < 100 or (noraO.slut_score <85 and noraO.exhib):
        #Strips naked, asks for sunscreen and lets you play with her pussy.
        "Nora gives you a squirt of sunscreen, then puts the bottle down and stands up. She pulls the straps of her swimsuit over her shoulders, then pulls the whole thing down and off."
        show nora strip32 at right
        $ noraO.inc_naked()
        "She she kicks the swimsuit to the side and sits back down, taking a squirt of sunscreen for herself. She rubs it over the front of her body, paying special attention to her breasts. That done, she lies face down on her towel."
        nora "[inputName], could you get my back for me please?"
        me "No problem at all."
        nora "Thank you. Take as long as you need with my butt, I would hate to get a burn there."
        "You take the bottle of sunscreen and lay a long line out over Nora's back, stretching from her shoulder blades down to her ass. Then you start to spread it around and rub it in, working your way from top to bottom."
        "Heading her advice, you take a good long time on her ass. Nora sighs softly while you play with her."
        nora "That feels really good. Keep doing that, please."
        "You kneed her butt a little harder, enjoying how it feels in your hands. Nora seems to be having just as much fun, sighing occasionaly."
        nora "Mmm, I think I've gotten a little wet. Could you check and make sure?"
        me "Lets see..."
        "You reach a hand between Nora's legs and run a finger along her pussy. She gasps when you brush past her clit."
        nora "Oh, do that again."
        "You make little circles around Nora's clit with your finger. She responds by arching her and moaning quietly, her pussy now dripping wet."
        me "Yes, you seem to be a little wet Nora."
        nora "Keep touching me... Ah..."
        "She moans again, louder this time. You slide a pair of fingers into her cunt and start to finger her."
        "Nora grabs handfuls of her towel and gasps, her hips twitching against your hand."
        nora "Keep going! Ah!"
        "Nora's pussy convulses around your fingers, her thighs clamping down on your hand and holding it in place while she climaxes."
        show nora strip33 at right
        "After a few shuddering breaths she relaxes and you're able to remove your hand. Nora rolls onto her front and sits up, nipples rock hard."
        nora "Thank you [inputName]. Ah..."
        "You lie down on your own towel next to her. You pass an hour and a half in the sun, enjoying the warm summer day while you stare at Nora's tits."
        if slut_outfit:
            show nora swim2
        else:
            show nora swim1
        $ nora_beach_tan.inc_level(1)
        $ noraO.change_resist(-nora_beach_tan.use_red(1,noraO.resist_score))
    else:
        #Strips naked, gets oiled up, then blows you as thankyou.
        "Nora gives you a squirt of sunscreen, then puts the bottle down and stands up. She pulls the straps of her swimsuit over her shoulders, then pulls the whole thing down and off."
        show nora strip32 at right
        "She she kicks the swimsuit to the side and sits back down, taking a squirt of sunscreen for herself. She rubs it over the front of her body, paying special attention to her breasts. That done, she lies face down on her towel."
        nora "[inputName], could you get my back for me please?"
        me "No problem at all."
        nora "Thank you. Once you're finished with me I'll make sure to repay the favour."
        "You take the bottle of sunscreen and lay a long line out over Nora's back, stretching from her shoulder blades down to her ass. Then you start to spread it around and rub it in, working your way from top to bottom."
        "You spend a while playing with her butt when you reach it, kneeding her cheeks with your hands as you rub the suncreen in."
        show nora strip33 at right
        "Eventually she rolls over and sits up."
        nora "Thank you [inputName]. Now you lie down and I'll make sure to take care of everything for you."
        "You lie down on your own towel, face down, and wait. Nora kneels beside you, squirts some suncreen into her hand, and begins to rub your back."
        "She works her way down to your waist, then down to your legs."
        nora "Roll over for me."
        show nora blow28 at right
        "When you roll over Nora swings one leg across your body, straddling you. She rubs her hands down your chest, pausing for a brief moment to brush her thumbs over your nipples. Your erection rubs against her crotch, seperated only by your swimsuit."
        "Nora works her way lower, shuffling back as she goes. When she reaches your waist she pauses, hand resting on your hard shaft."
        nora "Oh my. I'll have to take care of this while I'm at it I suppose."
        show nora blow29 at right
        $ noraO.inc_blow()
        "She pulls your swimsuit down, letting your cock spring free. She leans forward and licks your shaft from balls to tip. When she reaches the top she opens her mouth and slides you in, quickly sliding you to the back of her throat."
        me "Oh god that feels good."
        "Nora places her hands on your thighs while she blows you, taking every inch of your hard cock down her throat with each pass."
        "After a few minutes of Nora servicing you, you feel your orgasm approach."
        menu:
            "Cum down her throat.":
                me "Ah, I'm going to cum soon Nora!"
                "She moans something back to you and speeds up, tongue licking the bottom of your shaft while she goes. You rest a hand on the back of her head and press her down as you climax."
                me "Here you go!"
                if noraO.cumslut:
                    "You fire your load down Nora's throat, right into her stomach. Her eyes flutter and her whole body shivers with pleasure while you fill her up with your sperm."
                    "When you're done you let go of her head, and she slides off your cock with a wet pop."
                    nora "Ah... You taste so damn good [inputName]."
                    "She leans back down and licks your sensitive shaft a few more times, getting every last drop of cum off of it."
                    me "Glad you like it Nora, that was great."
                else:
                    "You fire your load down Nora's throat, right into her stomach. She keeps her eyes locked on yours while you pump her full of your sperm."
                    "When you're done you let go of her head, and she slides off your cock with a wet pop."
                    nora "Ah... very good job [inputName]."
                    me "You too Nora, that was great."
                show nora strip33 at right
                $ noraO.inc_cum_mouth()
                "She takes a few deep breaths, then lies down on her towel next to you. Feeling completely relaxed, you spend an hour dozing in the warm summer sun."

            "Cum on her face.":
                me "Ah, I'm going to cum soon Nora. I want to cover your pretty face!"
                "She moans something back to you and speeds up, tongue licking the bottom of your shaft while she goes. She pulls off just before you orgasm, keeping your cock pointed squarely at her face."
                show nora blow30 at right
                "You fire your load up into Nora's face, spraying your cum across her forehead and cheeks."
                if noraO.cumslut:
                    nora "Yes, give it to me [inputName]! Ah!"
                    "Nora trembles with pleasure as you pump out your load. When you're done she leans down and eagerly licks the last few drops from your tip, sending shivers up your spine."
                    nora "Mmm, thank you for giving me so much. It feels so good..."
                    "Nora closes her eyes and takes a deep, shuddering breath."
                    me "Any time, I'm glad you liked it."
                else:
                    "She closes her eyes and waits until you're done, then leans down and licks the last few drops from your tip. The feeling sends shivers up your spine."
                    nora "Wow... very good job [inputName]. You really did cover me."
                show nora strip33 at right
                $ noraO.inc_cum_over()
                "She reaches for her own towel and uses it to clean her face off, then lays it out again and lies down next to you. Feeling completely relaxed, you spend an hour dozing in the warm sun."
        if slut_outfit:
            show nora swim2
        else:
            show nora swim1
        $ nora_beach_tan.inc_level(2)
        $ noraO.change_resist(-nora_beach_tan.use_red(2,noraO.resist_score))
    return

label min_nora_schoolgirl:
    show nora strip38 at right
    nora "Hello sir, may I come in?"
    "Nora crosses one leg behind the other, standing at your door in a schoolgirl's outfit. She's got her shirt tied up to show off her cleavage, and her skirt rolled at the hem so it ends at her mid thigh."
    me "Of course, come on in. I like the outfit."
    "Nora steps past you, and you close the door behind her."
    nora "Thank you, I thought you might. If we're going to be working on your homework I wanted to look the part. Now, lead the way."
    show nora strip39 at right
    "You lead Nora towards your room, trailing behind her on the stairs so you can peek up her skirt."
    nora "Enjoying the view?"
    me "Yeah, I am."
    "She slows down, taking her time with each step so you can watch her legs and ass."
    show nora strip38 at right
    "You close the door to your room once you and Nora are inside, locking it to make sure you aren't interupted."
    nora "Sir, I have to be honest with you. I've been a very bad girl."
    show nora strip40 at right
    "Nora sits on the edge of your desk and crosses her legs. She seems to be taking her schoolgirl roleplaying seriously now."
    nora "You so nicely invited me to your house, and I haven't done a single bit of my homework. Before we do anything else, I think I need to be punished."
    me "Hmm, I think you're right Nora. What do you think a naughty girl like you deserves?"
    show nora strip41 at right
    "Nora bites her lip and stands up, then turns around and bends over your desk. She wiggles her ass at you."
    nora "I think a spanking would be appropriate, sir."
    show nora strip42 at right
    "You nod and step forward, running a hand down her back towards the bottom of her skirt. You pull it up, revealing her bare ass."
    me "No panties either. I'm sorry, but that's in clear violation of our dress code."
    "You place a hand on her tight ass cheek, giving it a good squeeze."
    nora "I'm sorry sir, I accept whatever punishment you need to give to me."
    "You bring your hand back and smack Nora hard on the ass. She gasps softly in response."
    me "No homework, dress code violations. I'm very disapointed in you Nora."
    "You give her another hard spank, making her ass cheeks jiggle."
    nora "Ah... It won't happen again sir. Is there anything I can do to make it up to you?"
    "Another hard smack and Nora moans."
    me "Hmm, there may be something you could take care of for me. An extra credit assignment."
    show nora strip43 at right
    "Nora's ass has started to turn red as you spank her."
    nora "Anything sir, ah! Anything at all."
    "You reach a hand between Nora's legs, feeling her pussy."
    me "Well, since this already seems nice and wet I think I'll use it to relieve some stress."
    nora "Of course sir, whatever you want."
    show nora fuck46 at right
    "You hold onto Nora's hips and roll her over onto her back. She pulls her legs up and moves them to the side, presenting her wet cunt to you while you pull your pants down."
    nora "Oh sir... It looks so big. Are you sure it will fit?"
    "You rest your hard cock on Nora's slit, rubbing it back and forth to get it wet with her juices."
    me "I'm sure it will. Just relax and enjoy."
    $ noraO.inc_sex()
    if noraO.anal:
        nora "Wait, you can't put it there sir, I'm still an innocent young virgin. You'll have to put it somewhere else..."
        "Nora wraps her soft hand around your shaft and guides it lower, pressing your tip against her butthole."
        me "Of course, it's the only proper way to do it."
        show nora fuck56 at right
        "You hold onto her hips and push forward. Nora gasps as you stretch her ass open and fit full length inside."
        nora "Oh sir... Fuck me that's big..."
        "You give her a moment to get use to your cock, then start to pump back and forth."
        nora "Ah... Yes sir, thank you so much... Ah! For this...!"
        "Nora's ass is incredibly tight and seems to clamp down on your shaft with each stroke."
        me "You have a very nice butt Nora, but I think I'm going to need more than just this to finish."
        "You pull out of Nora's ass with a pop. She shivers with pleasure and looks up at you between her legs."
        nora "I give in sir, I'm all yours. Do whatever you want with me!"
        show nora fuck46 at right
        "You rest your cock on her slit again and get ready to fuck her."
    "She moans as you guide the tip of your penis into her pussy, slowly slipping yourself all the way into her."
    nora "Ah... do I feel good sir? How does it feel to fuck one of your students?"
    "You start to pump in and out of Nora. She's ridiculously wet, and her pussy seems tighter than normal."
    me "You feel amazing Nora. I don't think it'll be very long until I finish."
    nora "Good, I really want you to cum for me sir. I want you to cum wherever you want. Ah..."
    show nora fuck47 at right
    "She arches her back and trembles with pleasure, her hips moving to meet yours with each thrust."
    "After fucking Nora for a few more minutes you feel yourself approaching your climax."
    menu:
        "Cum inside her.":
            me "I'm almost there! Are you ready Nora?"
            if noraO.cumslut:
                nora "Yes! I want every last drop of your hot semen, please give it to me sir!"
            else:
                "Nora pants louder and nods in response."
            me "And you promise to be a good girl from now on?"
            nora "Of course sir! Ah! I'll be the best student in the whole class!"
            $ noraO.inc_cum_inside()
            "You give Nora's cunt a few quick thrusts, then slam yourself as deep inside of her as you can manage as you start to orgasm. She gasps loudly as you pump your load into her."
            "When you're finished you lean forward, resting your head on Nora's chest while you catch your breath."
            if noraO.preg_response_ok():
                if noraO.cumslut:
                    nora "Thank you sir, you feel so warm inside me. I wonder what people would think if you got a student pregnant though..."
                else:
                    nora "Wow, well done sir. Thank you."
            else:
                nora "Mmm, that was nice. We should be more careful though, I'm not on the pill right now. I think we both got a little carried away."
            show nora fuck48 at right
            "Once you've recovered a little you take a step back, letting your cock slip out of Nora's cum soaked pussy. She stays on your desk a little while longer, semen dripping out of her onto the floor."

        "Cum over her.":
            me "I'm almost there! Are you ready Nora?"
            if noraO.cumslut:
                nora "Yes! I want every last drop of your hot semen, please give it to me sir!"
            else:
                "Nora pants louder and nods in response."
            me "And you promise to be a good girl from now on?"
            nora "Of course sir! Ah! I'll be the best student in the whole class!"
            "You give Nora's cunt a few quick thrusts, then pull out with a wet pop and start to stroke yourself off."
            if noraO.cumslut:
                nora "Oh god sir, give it to me! I just want you to cover me with it!"
            else:
                nora "Ahh... Go ahead and finsi for me, sir."
            $ noraO.inc_cum_over()
            show nora fuck49 at right
            "You finally orgasm, pulsing out your load in thick lines across Nora's body. You step back and admire the view, with your cum covering Nora from her tits down to her stomach."

    me "Whew, I think you wore me out with that Nora."
    "She sits up and nods."
    nora "Me too. I'm going to go use your bathroom to get cleaned up, if you don't mind."
    show nora strip39 at right
    "Nora slips out of the room and is gone for a few minutes. When she gets back she's cleaned up all of your cum."
    nora "Thank you for playing along [inputName], I thought a bit of roleplay would be fun."
    me "I definitly had fun. Did you want to take a look at the problems I was working on?"
    nora "Oh, right. I think I figured it out while I was in the car. Sit down and I'll be the teacher for a little bit."
    "Nora walks you through the solutions to the different problems, pointing out the mistakes you were making before. After an hour you walk her to the door and say goodbye, watching her ass as she heads down the driveway."
    $ nora_schoolgirl.inc_level(0)
    $ noraO.change_resist(-nora_schoolgirl.use_red(0,noraO.resist_score))
    return




############################
##Stephanie's Minor Scenes##
############################

label min_steph_nudes:
    if stephO.slut_score < 10: #nothing special
        steph "Aww, that's sweet. It's nice to be friends with the people I work with."

    elif stephO.slut_score < 30: #tit flash
        steph "Oh, I know I can. I always have the nuclear option after all."
        me "The nuclear option?"
        "There's a pause, then Stephanie sends you a picture."
        show steph strip15 at truecenter
        "She's lifted up her shirt and bra, taking a close in shot of her tits."
        steph "If these girls don't make you smile you don't have a pulse."
        me "Wow, looking good. I'll admit that it worked."
        steph ":)"
        $ steph_nudes.inc_level(0)
        $ stephO.change_resist(-steph_nudes.use_red(0,stephO.resist_score))

    elif stephO.slut_score < 50 or (stephO.slut_score >= 50 and not stephO.exhib): #Completely naked.
        steph "Well thank you. I suppose I always have a secret weapon if you're really down."
        me "And what would that be?"
        "There's a pause, then you get a picture from Stephanie."
        steph "Me. A guy can't be sad when he's looking at a naked girl, right?"
        show steph strip14 at truecenter
        $ stephO.inc_naked()
        "Stephanie is naked and posing for the camera. She's not holding it herself, so you aren't sure how she got the shot."
        me "Not when she's as hot as you."
        steph "You're too sweet :P"
        $ steph_nudes.inc_level(1)
        $ stephO.change_resist(-steph_nudes.use_red(1,stephO.resist_score))

    elif stephO.slut_score < 70: #Giving a dude a titjob at a party. Can only trigger if she has public
        steph "Thank you, I pride myself on making guys smile."
        me "Oh ya? How do you normally do it?"
        steph "Well... I was at a party with some friends..."
        show steph tit2 at truecenter
        $ stephO.inc_naked()
        "Stephanie sends you a picture. She's on her knees in front of a dude on a couch, rubbing his cock between her tits."
        steph "And he seemed a little down. He was definitely smiling after this though."
        show steph tit3 at truecenter
        "Another picture. Stephanie's leaned back, tits covered in fresh cum."
        me "Ha, wow. That's one way to make a guy smile!"
        steph "I do my best ;)"
        $ steph_nudes.inc_level(2)
        $ stephO.change_resist(-steph_nudes.use_red(2,stephO.resist_score))

    else: #Having sex with a dude at a party.
        steph "Thank you [inputName], I pride myself on making guys smile ;)"
        me "Oh ya? How do you normally help them out?"
        steph "Well... I was at a party with some friends a few days ago..."
        show steph fuck8 at truecenter
        $ stephO.inc_naked()
        "Stephanie sends you a picture taken from someone's phone. She's riding a guy cowgirl style on an old couch, hands locked behind her head."
        if stephO.anal:
            steph "and he seemed a little down, so I did what any good girl would. He really went to town on my ass and seemed a lot happier when he finished."
        else:
            steph "and he seemed a little down, so I did what any good girl would. He seemed a lot happier after he finished."
        show steph fuck9 at truecenter
        "Another picture. Stephanie's on her knees and looking up at the camera now. There's a splash of cum across her cheek and a whole lot in her mouth."
        me "Ha, wow. That certainly would have made me smile!"
        if stephO.cumslut:
            steph "Promise to fill my mouth up like that and I'll do anything you want ;)"
        else:
            steph "I'll do my best ;)"
        $ steph_nudes.inc_level(3)
        $ stephO.change_resist(-steph_nudes.use_red(3,stephO.resist_score))
    "You and Stephanie flirt back and forth for a while longer until she has to go."
    return

label min_steph_walk_in:
    if stephO.slut_score < 40:
        show steph strip1 at right
        steph "Hey [inputName]."
        "Stephanie's just wearing her underwear; a bright pink set."
        $ stephO.inc_naked()
        me "Wow, hey Stephanie."
        steph "Wow? Oh! Ya, it was getting hot in there. Come on in."
        "Stephanie closes the door behind you and heads back to her seat at a desk."
        steph "If you get warm feel free to take your shirt off or something."
        me "Sure, will do."
        steph "So what brings you by this early in the morning?"
        me "Well, nothing in particular. I just thought I'd come by and see if you were around to hang out."
        steph "Well here I am, pull up a chair!"
        "You grab a chair and sit down opposite Stephanie's desk."
        me "So what are you up to?"
        "You and Stephanie make small talk for a while, and you take every opportunity to oggle her body."
        "Eventually Stephanie catches you and smiles."
        steph "Enjoying the view?"
        me "Honestly? Ya, you're looking really good today Steph."
        steph "You think so? What about my butt?"
        show steph strip6 at right
        "She stands up and turns around, bending over with her hands on her ass."
        me "Amazing, it looks amazing."
        steph "Give it a slap."
        "You lean over her desk and give her ass cheek a good spank. She gasps a little, then turns and smiles."
        steph "Thank you. Now I should get back to work, I can't have you distracting me all day."
        me "Right, of course. I wouldn't be able to stop spanking you."
        show steph strip1 at right
        steph "Exactly."
        "You go back to your small talk, making no efforts to hide your gaze now. Stephanie even holds her tits up for you a few times and makes a point of bending over with her legs straight when she has to get something low down."
        "Finally the afternoon aproaches and she gets dressed before Nora arrives."
        $ steph_walk_in.inc_level(0)
        $ stephO.change_resist(-steph_walk_in.use_red(0,stephO.resist_score))
    elif stephO.slut_score < 50:
        show steph strip7 at right
        steph "Hey [inputName], how's it going?"
        me "Wow, much better now, thanks!"
        "Stephanie's just in her pink panties, tits free to bounce around. She steps aside to let you in."
        steph "Good, I'm glad you like it. It was getting a little warm, and I figured nobody would mind if I was here by myself. I'm certain you won't mind."
        me "Not at all, as long as I can take a good look."
        show steph strip12 at right
        "Stephanie cradles tits in her hands and smiles at you."
        steph "Look as much as you want. Actually, I have an idea..."
        me "Oh ya?"
        show steph strip7 at right
        steph "Ya. Nora stuck me with a pile of paperwork. If you don't mind helping me out I can make sure we both have a good time"
        me "I'm not doing anything for the rest of the morning, sure."
        "Stephanie pulls a chair up beside hers for you, then sits down at her desk."
        steph "Here, we're filling out request forms. Simple stuff."
        "You sit down next to Stephanie and start to work on the paperwork, letting your gaze stray to her tits whenever you feel like it. Her nipples have gotten hard and she's blushing slightly now."
        "A few minutes later her hand runs along your thigh towards your waist."
        "You look over, but she pulls her hand back and keeps looking at her own work."
        "Unsure of what to do, you return to your work, and a few minutes later her hand returns to your thigh, rubbing gently."
        me "Uh, Steph?"
        steph "Shhh. Just keep working."
        "You keep your eyes on your paperwork this time, filling in the various blanks with the appropriate information."
        show steph hand2 at right
        "Stephanie's hand drifts up your thigh to your waist, then slips under your pants and rubs your cock over your underwear."
        me "Ooh, that feels good."
        show steph strip7 at right
        "Her hand pulls out and goes back to her lap. She wistles a short toon, pretending not to notice anything happening."
        show steph hand2 at right
        "Catching on to her game, you get back to work. You aren't surprised when her hand rubs your thigh, and you're eagerly ready for when her hand slips under your pants again, rubbing your hard shaft."
        "You stay quiet, eyes focused and pencil working while Stephanie rubs you. Her hand comes up again, works your fly down, then pulls your cock out."
        "She takes your dick in her hand and rubs you, slowly at first, while you both keep doing paperwork."
        "After a few minutes you have an idea. With the same absentminded slowness as Stephanie you move your free hand down to your lap, then over to her leg. She gasps as you touch her thigh, but spreads her legs slightly."
        "As Stephanie jerks you off you slide your own hand up her leg and over her crotch. Her panties are already wet and clinging to her slit. You peel them to the side slowly, then run a finger along her pussy."
        show steph hand3 at right
        $ stephO.inc_hand()
        "Stephanie shudders as you slip a finger into her and rubs you faster. Before long you're both masturbating each other, breathing hard and pretending not to notice."
        "Finally you reach your limit and begin to tense. Stephanie moans and goes even faster."
        "You fire your load into the bottom of the table, then Stephanie gasps and takes a deep breath. You can feel her pussy twitch around your fingers and her core muscles go tight."
        "After a moment she relaxes, pencil dropping from her hand onto the desk."
        steph "So how's that work going?"
        me "I think I'm all finished. You."
        steph "Ya, all done."
        show steph strip7 at right
        "You both take a while to catch your breath. Stephanie pulls her panties back into place and hands you some tissue to clean up."
        steph "Thanks for the help [inputName]. Stop by any time."
        me "Will do, glad to help out."
        "As it gets close to lunch time you head up to see what else is going on on campus."
        $ steph_walk_in.inc_level(1)
        $ stephO.change_resist(-steph_walk_in.use_red(1,stephO.resist_score))
    elif stephO.slut_score < 80:
        show steph strip2 at right
        steph "Oh, hey [inputName]."
        me "Hey Stephanie. Feeling relaxed I see."
        "Stephanie moves aside so you can come in, then closes the door behind her."
        steph "Well it was a little warm, and if I'm taking some clothes off I might as well take them all off."
        me "Seems reasonable to me. I hope I'm not interrupting anything."
        steph "Nothing important. Nora stuck me with a pile of paperwork to get done. It's all simple stuff, but it's going to take hours."
        "Stephanie pouts and leans against her desk and slides some of the papers towards you."
        "You walk over and take a look at her work. It's a simple procedure of calculating the total amount of materials used for each chemical stocked in the lab."
        me "You know, I could probably write a program to do this. It's all information on our computers anyway, you just have to calculate it and print it out."
        steph "Really? You could do that?"
        me "Easy."
        "You sit down at Stephanie's computer and open up excel. It doesn't take long to get all the data imported."
        "You're absorbed in your work for a while, and very surprised when you feel a pair of hands running along your inner thighs."
        "You slide your chair back and look under the desk. Stephanie has crawled under from the other side and is on her knees, completely naked, rubbing your legs."
        steph "Don't worry, just keep up the good work [inputName]."
        "She pulls your chair back and slides herself closer, working her hands up to your waist where she undoes your fly and pulls your pants down."
        show steph blow9 at right
        $ stephO.inc_blow()
        $ stephO.inc_cum_mouth()
        $ stephO.inc_cum_swallow()
        "You do some typing in excel, creating a formula to calculate all of the values Nora wanted. Stephanie plants her hands on your waist and leans her head in, licking the bottom of your cock from base to tip."
        me "Wow, that feels great."
        "Stephanie smiles up at you from under the desk and opens her mouth wide, then slides your cock into it until your tip hits the back."
        "You test your excel formula, find a bug, and fix it. Stephanie works her head back and forth, tongue soft and wet on the bottom of your shaft."
        "She looks up and makes little gurgling noises as you tap the back of her throat."
        "You set a print area, do a little bit of formating, and hit ctrl-p. Stephanie's working her head as quickly as she can, and you're almost ready to finish."
        me "Printing. I'm almost there Steph."
        if stephO.cumslut:
            "Stephanie pulls off for a quick second."
            steph "Good, fill up my mouth with your hot load! I want to taste it all!"
            "She slides you back into her mouth and resumes blowing you."
        else:
            "Stephanie nods and keeps blowing you."
        "You lean back in the chair and moan softly while you finish. At the last moment Stephanie pulls back a little bit so your tip is in her mouth and grabs your shaft. She jerks you off as you fire your load into her throat."
        show steph blow10 at right
        "When you're completely finished you slide your chair back, pulling your cock away from her lips. Stephanie stays under the desk for a moment and looks up at you. She smiles, then opens her mouth to show you your load."
        me "Good girl. That was amazing."
        if stephO.cumslut:
            "Stephanie plays with your cum for a little while, moving it around with her tongue and gargling it. Eventually she gulps it down, quivering with pleasure while she does."
            steph "You taste so, so good [inputName]. Did I get it all?"
            "She leans forward and licks along the sides of your cock, making sure to get every last drop of cum. When that's done, she loops back up at you."
            steph "So, how did the work go?"
        else:
            "Stephanie closes her mouth and you can see her throat work up and down for a moment. She sighs, then opens and shows you a now empty mouth."
            steph "Good, I'm glad. How did the work go?"
        me "All done, it's at the printer."
        steph "Thank's [inputName], you're a life saver."
        show steph strip2 at right
        "You pull your pants up while Stephanie gets your printout and adds it to the rest of her work. It's close to lunch, so you say goodbye and head back up to the campus proper."
        $ steph_walk_in.inc_level(2)
        $ stephO.change_resist(-steph_walk_in.use_red(2,stephO.resist_score))
    else:
        show steph strip2 at right
        steph "Hey [inputName], glad you're here. Come in."
        "Stephanie's standing at the door completely naked. Her skin is flush and her nipples are hard."
        me "I see you're in early and taking advantage of the empty lab."
        "Stephanie steps aside to let you in, then closes the door behind you."
        steph "Ya, well Nora stuck me with a pile of paperwork. I wanted to get it done early, but I couldn't focus."
        me "Too hot?"
        steph "Horny as fuck."
        show steph strip13 at right
        "She collapses in her chair and spreads her legs, running a finger along her pussy."
        menu:
            "Offer to help.":
                me "Well there may be a way I can help."
                "You walk towards Stephanie on the chair, slipping your pants down and revealing your already hard cock."
                steph "Oh god, please? Just a little bit to help me focus."
                show steph fuck16 at right
                $ stephO.inc_sex()
                "Stephanie sits at the edge of the chair and holds her legs wide for you. You step between them and guide your cock between her lips, rubbing slowly."
                "Finally you lean forward and slip into her. Stephanie moans and grips the edge of the office chair."
                "Her pussy is warm and soft, already wet and eager for you."
                steph "Oh yes, that's great!"
                "You hold onto Stephanie's hips and pump into her while she moans."
                show steph fuck17 at right
                "After a few minutes you grab her legs and pull them up and together. You feel her pussy tighten around your cock, driving you to fuck her even faster."
                me "You feel great Steph. I'm almost ready."
                steph "Can I swallow it? I want your cum in my mouth, please!"
                menu:
                    "Cum inside her.":
                        me "Too late, here I come!"
                        "You give her tight pussy a few more pumps, then hold yourself tight against it as you unload inside. Stephanie gasps as your seed fills her up, legs quivering against your shoulder."
                        show steph fuck18 at right
                        $ stephO.inc_cum_inside()
                        "When you're done you pull out, keeping a hand on Stephanie's ankles to keep her legs together for a little while."
                        "Your cum trickles out of her pussy and down her ass."
                        if stephO.preg_response_ok():
                            if stephO.cumslut:
                                steph "Oh wow... your cum feels so good inside me [inputName]. Did it feel good to pump me full of it?"
                                me "Damn right it did!"
                            else:
                                steph "Oh wow. That was... great."
                                me "It was. Hope it helps you focus."
                        else:
                            steph "Oh fuck... That was great, but we really need to be more careful when I'm not on my birth control..."
                        "You let go of Stephanie's legs and let them fall to the sides while she pants."
                        "Stephanie eventually gets back on her feet and starts cleaning up. You head up to ground level on campus to see what else is going on."

                    "Cum in her mouth.":
                        me "Okay, get ready!"
                        "You let go of Stephanie's legs and pull out of her pussy with a wet pop."
                        "She drops to her knees, letting the chair roll back into a desk, and opens her mouth wide."
                        "You place your tip on her tongue and rub your cock until you start cumming."
                        "Stephanie moans as you fill her mouth up, eyelids half closed in pleasure."
                        show steph fuck19 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "Her legs shudder a little, but she keeps her head steady until you're completely finished. Then she pulls off and looks up at you, blowing bubbles through your load."
                        me "Good job Stephanie. Very good job."
                        "She closes her mouth and swallows."
                        if stephO.cumslut:
                            steph "Mmm, your cum always tastes so good [inputName]. Lets make sure I got it all."
                            "She leans forward and starts to lick the sides of your cock, cleaning up every last trace of semen."
                            me "Glad I could help, I hope you're able to focus now."
                            "Stephanie finishes drinking up the last little bit of sperm and sits back."
                        else:
                            steph "Fuck. Thank you so much [inputName]."
                            me "No problem. I hope it helps you focus."
                        me "I've got to head out. Good luck with your work."
                        "You leave the lab and head up to ground level on campus."
                $ steph_walk_in.inc_level(3)
                $ stephO.change_resist(-steph_walk_in.use_red(3,stephO.resist_score))
            "Do nothing.":
                me "I can see how that would be distracting."
                "Stephanie nods and slips two fingers into her slit, rubbing them in and out slowly."
                steph "I thought if I just, ah, took care of it myself I would be okay."
                "She rubs herself faster and leans back in the chair."
                steph "But it's not that easy. I want someone's load in my mouth."
                "She looks straight at you."
                steph "Couldn't it be yours?"
                menu:
                    "Offer to help.":
                        me "Fine, I can help. It will have to be fast though, okay?"
                        "Stephanie smiles brightly and jumps up from her chair. She runs over to where you're standing by the door and drops to her knees."
                        steph "I'll be as fast as I can. Promise."
                        "She pulls your pants down and grabs your cock with her already wet hand. She gives it a few quick strokes, spits on it, then spreads the spit around with her palm."
                        show steph blow11 at right
                        $ stephO.inc_blow()
                        "Then she leans in, licks your tip once, and dives onto your shaft. She presses your tip into the back of her throat and looks up at you, holding herself there for a long while with her hands behind her back."
                        "Eventually she pulls off, takes a deep breath, then sets you back in her mouth and starts blowing you."
                        "Stephanie takes your full length with each stroke of her throat, gurgling a little each time you hit the back and drooling spit down her front each time she pulls off a little."
                        "Her eyes stay locked on yours the whole time, lids half closed in pleasure."
                        "After a few minutes of service by your lab partner you're feeling ready to finish."
                        me "You've done a great job Stephanie, ready for your reward?"
                        "Stephanie moans and nods as best she can with your dick in her mouth. A few more strokes of her throat and you begin to tense up."
                        "She pulls back and opens her mouth with her tongue out. She leaves your tip resting on her tongue, pointed directly in."
                        "You groan and begin firing your load across her tongue and into her eager mouth. Stephanie moans loudly, eyes fluttering up. Her thighs shiver, but she keeps her head still until you're completely finished."
                        "Finally you're done and Stephanie collapses backwards onto her ass, catching herself with her hands. Her pussy is drenched and her thighs still quiver a little bit."
                        show steph fuck19 at right
                        $ stephO.inc_cum_mouth()
                        $ stephO.inc_cum_swallow()
                        "Stephanie looks right at you and opens wide. She blows a few bubbles through her mouthful of cum, then closes her mouth and swallows. When she opens again her mouth is completely empty."
                        me "Good job Stephanie. Very good job."
                        if stephO.slut_score > 100:
                            steph "Do you think you could do it again?"
                            me "Again? I don't think so, I'll need some time to recharge."
                            "Stephanie frowns, still on the ground."
                        else:
                            steph "Thank you. Thank you so much."
                        me "I've got to head out. Good luck with your work."
                        "You leave the lab and head up to ground level on campus."
                        $ steph_walk_in.inc_level(4)
                        $ stephO.change_resist(-steph_walk_in.use_red(4,stephO.resist_score))
                    "Leave the lab.":
                        me "Sorry Steph, I've got some other stuff I need to take care of. I was just checking in."
                        "Stephanie frowns but nods."
                        "When you leave the lab Stephanie has three fingers deep in her pussy, moaning quietly while spread out on the chair."
    return

label min_steph_nap:
    if stephO.slut_score < 20: # Just startles you.
        show steph work at right
        "A small nudge to your side wakes you up. You're staring right up at Stephanie."
        me "Uh, hey there Stephanie."
        steph "Hey [inputName]. Having a good time?"
        me "Ya, actually. What's up?"
        steph "Nothing. I was heading to the lab and saw you here. I guess I just wanted to say hi."
        me "Oh. Hi."
        steph "Sorry I woke you up, that was stupid."
        "You rub your eyes and sit up."
        me "No, it's okay. I should probably get moving anyway, Nora will want us at the lab soon."
        "Stephanie looks embarassed, but nods."
        steph "Right. See you there."
        "She waves and heads off."
    elif stephO.slut_score < 40: # Sweater to the face.
        "You're woken up suddenly by the feeling of something soft and fabric covered against your face. You open your eyes, but all you see is black."
        "You try and turn your head, but the object turns with you. You can hear someone laughing, a girls voice."
        show steph strip16 at right
        "Finally the object moves and you're able to breath. Stephanie is kneeling, legs spread over yours, tits held in her hands through her shirt, and laughing hard."
        steph "Good morning there! I hope you enjoyed your wakeup."
        me "Oh god Steph, you nearly suffocated me."
        steph "I'll have to be more careful next time then. Anyway, I thought I'd wake you up, it's almost time for us to head into work."
        me "Right. Thanks."
        "Stephanie stands up and waves as she heads off."
        $ steph_nap.inc_level(0)
        $ stephO.change_resist(-steph_nap.use_red(0,stephO.resist_score))
    elif stephO.slut_score < 80 or (stephO.slut_score >= 80 and not stephO.exhib): # Naked tits to the face, licked nipples.
        "You're woken up by the sudden feeling of something soft and warm against your face. you open your eyes, but all you can see is black."
        "You try and turn your head, but the object turns with you. You can hear someone laughing, a girls voice, right in front of you."
        show steph strip17 at right
        $ stephO.inc_naked()
        "Finally they move and you're able to breath a little easier. Stephanie is kneeling, legs spread over yours, naked tits held in her hands, and laughing hard."
        steph "Good morning! I hope you enjoyed your little wakeup."
        "She jiggles her tits left and right."
        "You lean forward quickly and lick her left nipple, sucking it into your mouth and playing your tongue over it a few times."
        steph "Oh! I guess that's a yes!"
        "She holds her tits out for you. You suck on one for a while, leaving it hard and a little red."
        steph "That feels great. Wow."
        "Finally you pull off."
        me "Ya, it was a good way to wake up."
        steph "Glad you like it. Anyway, I noticed you napping and thought I should wake you up, Nora's going to be expecting us soon."
        me "Okay, I'll meet you guys at the lab in a few."
        "Stephanie pulls her shirt down and gets up. She waves as she heads off."
        $ steph_nap.inc_level(1)
        $ stephO.change_resist(-steph_nap.use_red(1,stephO.resist_score))
    else: # Quick titjob
        "You're woken up by the sudden feeling of something soft and warm against your face. you open your eyes, but all you can see is black."
        "You try and turn your head, but the object turns with you. You can hear someone laughing, a girls voice, right in front of you."
        show steph strip17 at right
        $ stephO.inc_tit()
        "Finally they move and you're able to breath a little easier. Stephanie is kneeling, legs spread over yours, naked tits held in her hands, and laughing hard."
        steph "Good morning! I hope you enjoyed your little wakeup."
        "She jiggles her tits left and right."
        "You lean forward quickly and lick her left nipple, sucking it into your mouth and playing your tongue over it a few times."
        steph "Oh! I guess that's a yes!"
        "She holds her tits out for you. You suck on one for a while, leaving it hard and a little red."
        steph "That feels great. Wow."
        "Finally you pull off."
        steph "Well I can't just let that go unanswered."
        "She looks around, confirming you're the only people nearby right now."
        steph "Slip your pants down."
        "You slip your pants down low enough to get your cock out, then lean back and leave it to Stephanie."
        me "Okay, what's your plan?"
        show steph strip18 at right
        "She leans down, slips your cock between her cleavage, and holds it in place by pinching her tits together with her hands."
        steph "This."
        "She starts sliding her breasts up and down along your shaft. You sigh a little as you enjoy how warm and soft they are."
        me "That's great. Keep going."
        "Stephanie smiles at you, then looks down and turns her full attention to tit fucking you. Over a few minutes she speeds up, stopping only to spit between her cleavage to make it more slippery."
        "Finally you're starting to feel ready to finish."
        me "I'm close Steph, don't stop."
        if stephO.cumslut:
            steph "Fill my mouth up, I want to taste your cum again!"
        else:
            steph "Finish in my mouth for me."
        "You nod, and she presses her tits together hard. A few more fast, wet strokes and you're tensing up as you orgasm."
        "Stephanie lets her breasts fall to the side and slips her mouth over your tip while you start to cum."
        show steph strip19 at right
        $ stephO.inc_cum_mouth()
        $ stephO.inc_cum_swallow()
        "She moans a little while you finish cumming, then pulls off carefully and sits up. When she looks up she opens her mouth and tilts her head around to show off your load."
        "Then she closes and swallows, opening after to prove it's all gone."
        me "Well done Stephanie, that was great."
        steph "Good. You taste amazing."
        show steph work at right
        "You both catch your breath for a few moments, then Stephanie stands up."
        steph "It's almost time for work, Nora's going to be expecting us. Meet you there?"
        me "Sure, see you soon."
        "Stephanie waves and heads off. She goes a dozen steps before realizing her shirt is still pulled up over her tits."
        $ steph_nap.inc_level(2)
        $ stephO.change_resist(-steph_nap.use_red(2,stephO.resist_score))
    return

label min_steph_stockroom:
    nora "Stephanie, [inputName], can I have a moment?"
    steph "Sure. What's up."
    me "Yeah, I'm here."
    nora "I need you two to go into the back and take inventory of what we have. Note whatever we're running low on and I'll pick some up on our next purchasing cycle."
    steph "Will do. [inputName], can you grab a pen and the stock notebook?"
    me "Got it, meet you in the back."
    hide nora
    show steph work at right
    "You grab everything you need and head to the stock room, a small closed in room at the back of the lab. It's cramped back here, especially with two people."
    if stephO.slut_score < 30:
        #Just some awkward squeezing.
        steph "Alright, ready to get started? Call stuff off the list, I'll count off what we have, you mark it down."
        me "Got it."
        "Stephanie gets to work, calling off numbers for you to record. The room isn't very large, so she's constantly squeezing past you as she moves around."
        steph "Okay, peroxides next. Excuse me."
        "She pushes past you, her ass rubs against your crotch."
        steph "Oh, sorry about that."
        me "No problem Stephanie. It's going to happen to matter what we do."
        steph "Three bottles of peroxide. I suppose you're right, it's no big deal."
        "She slides past you again. She doesn't say anything this time as your now hard shaft rubs against her ass as she moves past."
        show nora work at left
        "It takes a few hours, but you and Stephanie are able to get the inventory for the lab done."
        $ steph_stockroom.inc_level(0)
        $ stephO.change_resist(-steph_stockroom.use_red(0,stephO.resist_score))
    elif stephO.slut_score < 50:
        # Strips down a little so it's easier for you to move around.
        steph "Alright, ready to get started? Call stuff off the list, I'll count off what we have, you mark it down."
        me "Got it."
        "Stephanie gets to work, calling off numbers for you to record. The room isn't very large, so she's constantly squeezing past you as she moves around."
        steph "Okay, peroxides next. Excuse me."
        "She pushes past you, her ass rubs against your crotch."
        steph "There really isn't much room in here, is there? One moment."
        show steph strip1 at right
        $stephO.inc_naked()
        "She pulls her sweater up and off, then undoes her zipper and pulls her pants down."
        steph "Much better. If you strip down a little too we might have an easier time getting past each other."
        me "Uh, right."
        "You pull off your shirt and pants to match Stephanie's state of dress. She takes a peek at the obvious bulge in your pants, then gets focused again."
        steph "Perfect. Now, where were we?"
        me "Uh, peroxide bottles."
        steph "Right. Peroxide bottles. There are three."
        "She slides past again, your now hard cock rubbing against her ass with only your underwear in the way."
        "You spend another hour working on the inventory. It's hard to tell, but you think Stephanie might be pressing her ass against you on purpose each time she moves past you."
        show steph work at right
        show nora work at left
        "Eventually you're finished and get dressed again. Stephanie gives the report back to Nora."
        $ steph_stockroom.inc_level(1)
        $ stephO.change_resist(-steph_stockroom.use_red(1,stephO.resist_score))
    elif stephO.slut_score < 80:
        # Strips down, then gives you a blowjob since you're horny.
        steph "Alright, ready to get started? Call stuff off the list, I'll count off what we have, you mark it down."
        "Stephanie starts to pull her shirt up and off."
        steph "I'm just going to take some of this off. It's pretty cramped in here, it may help if you took something off too."
        me "Sure."
        show steph strip1 at right
        "She pulls off her sweater, then unzips her pants and takes them off too. You follow suit, and soon you're both in your underwear."
        steph "Good, lets get to work then. What's first on the list?"
        "You read off a few items from the inventory list and Stephanie moves around the room, giving you a count of each."
        steph "Peroxide? Lets see, it's on this side..."
        "Stephanie slides past you, pressing her ass against your crotch. She pauses as your hardon lands between her ass cheeks."
        steph "Oh, I hope I'm not getting you too excited like this?"
        "She rubs her ass left and right a little, leaning forward to put even more pressure against you."
        me "Well you aren't going to make it better like that."
        "Stephanie turns around in the crampt room, tits almost pressed up against you. She runs her hand down your chest, over your waist, and down to cup the bulge in your underwear."
        steph "I think I know what would make it better then. Lets finish this up quickly, then get back to work."
        show steph blow35 at right
        "She squats down, legs spread out to the side, and grabs the waistband of your underwear."
        if stephO.freeuse:
            steph "Lets get these off of you, shall we?"
        else:
            steph "Just be a little quiet, so Nora doesn't hear."
        "Stephanie slides your underwear down, leaving it around your knees. Your hard cock springs out, and she lets it rest against her cheek for a moment before taking it in her hand and licking it slowly."
        "After a few passes she lines it up with her mouth and slips you in. She starts to blow you slowly, bobbing her head up and down."
        me "That feels great Steph."
        "She nods and mumbles something. Over the next few minutes she picks up speed and starts going deeper, until her nose is pumping against your stomach on each pass."
        "She leans into you, pressing you deep down her throat and holding you there for a few seconds. You feel her throat spasm around your shaft, drawing you closer and closer to your orgasm."
        me "Fuck, I'm going to cum soon."
        "She pulls off with a wet pop and takes a few panting breaths."
        if stephO.cumslut:
            steph "Cum in my mouth, I need to taste it so badly. Please?"
        else:
            steph "Good, I want you to cum right in my mouth, okay?"
        "You nod, and she slips you back into her mouth and starts to blow you again. When you start to cum she keeps the tip of your cock in her mouth and strokes you off with your hand."
        "You pump your load into Stephanie's mouth, leaning against the shelf behind you for support. Stephanie moans softly below you, stroking you off until you are completely finished."
        show steph blow36 at right
        $stephO.inc_blow()
        $stephO.inc_cum_mouth()
        $stephO.inc_cum_swallow()
        "When you're completly finished she lets go of your cock and looks up at you, opening her mouth so you can see your load inside."
        "She gives you some time to take a good look, then closes back up and swallows. She has to take a few gulps to drink it all down."
        me "God, that felt great Stephanie."
        if stephO.cumslut:
            steph "It did, thank you so much [inputName]. Let me make sure I got it all."
            "She leans forward and licks along the sides of your cock, cleaning up every last drop of semen left. Eventually she's satisfied and leans back."
            steph "We should get back to work before Nora starts to wonder what's going on."
        else:
            steph "Ah, yeah. It did. We should get back to work and finish that inventory now."
        show steph work at right
        show nora work at left
        "She stands up and waits until you've got the inventory sheet ready again. Eventually you finish taking stock and get dressed again. Stephanie gives the report back to Nora."
        $ steph_stockroom.inc_level(2)
        $ stephO.change_resist(-steph_stockroom.use_red(2,stephO.resist_score))
    else:
        # Gets naked and lets you fuck her against the shelves.
        steph "Okay, lets get started. You know the drill by now. I'm going to ditch some of this so we aren't running into each other all the time. It would help if you did the same."
        show steph strip1 at right
        "Stephane starts to pull her shirt up and off. You do the same, and soon you're standing in your underwear."
        steph "This bra is really only going to get stuck on stuff, isn't it?"
        show steph strip7 at right
        "She unclips her bra next, throwing it ontop of the rest of her clothes."
        steph "And these panties too, really."
        show steph strip2 at right
        "She pulls down her panties as well, kicking them to the side when they fall to the ground."
        steph "Right, lets get to work."
        "Stephanie starts to move around the tight room, counting off items as you list them. She pauses as she slides past you, feeling your hard cock pressed up against her ass."
        steph "Oh, this again? Is someone getting a little excited?"
        show steph fuck49 at right
        "She rubs her bare ass against your hard cock, leaning forward and placing her hands on the shelf on the other side of the room."
        me "Maybe you'll have to take care of it for me. We've got some time before Nora expects us to be done, right?"
        "Stephanie looks over her shoulder at you, biting her lower lip. She nods, then reaches a hand back and pulls her ass cheek to the side to show off her wet pussy."
        steph "Go ahead and just slip it in there for me."
        "You pull your underwear down low enough to let your hard cock spring free, then line it up with Stephanie's cunt. She moans softly as you run the tip up and down the length of her slit."
        "After teasing her for a few seconds you slide in, her drenched pussy letting you go balls deep on the first stroke."
        steph "Oh [inputName], give it to me!"
        "You pump your hips, fucking Stephanie from behind. The shelf she's leaning on shakes and rattles."
        if stephO.exhib:
            steph "Just like that, yes! Fuck!"
        else:
            steph "Fuck, that's nice. Easy, we don't want Nora to hear what we're up to."
        show steph fuck50 at right
        $stephO.inc_sex()
        "You give Stephanie's ass a smack, then kneed her cheeks with your hands while you glide in and out of her. She moans louder and starts to bounce her hips against yours, helping you fuck her."
        me "God, you're nice and wet Stephanie. I think you needed this as badly as I did."
        if stephO.anal:
            steph "Ah, I really did! Could you slip it into my butt, just for a little bit? I love that so much..."
            "You pull out of Stephanie's cunt, then use your hands to spread her ass cheeks. She gasps when you start to push your tip inside of her."
            steph "Oh... That feel so nice. I'm glad I got you wet already..."
            show steph fuck64 at right
            "Soon you've got your entire cock buried in her ass. She moans and clamps her hands down on the shelf."
            me "Damn you're tight. Lets see if I can even move."
            steph "Be as rough as you need to be, I'm sure you'll stretch me out soon enough. Ah..."
            "You start to pump in and out of Stephanie's asshole, using her pussy juices as lube."
            "After a few minutes you pull out, leaving Stephanie's asshole stretched out and red."
            steph "Is everything alright? Ah..."
            me "Yeah, I just wanted to get back to the main event."
            show steph fuck50 at right
            "She moans when you slide your cock back into her pussy. The contrast between her tight ass and drentched pussy feels incredible and sends shivers up your spine."
            me "Are you having a good time? Do you like me using your ass and cunt like this?"
        else:
            steph "Ah, I really did! I needed to feel you inside me, I was just waiting for a chance. Ah!"
        "You reach around and grab Stephanie's tits, squeezing them tight. Stephanie's legs quiver against yours, her breath comming in faster and faster gasps."
        steph "Oh god yes! Ah!"
        "You feel her pussy twitch around your cock, and she suddenly leans heavily on the shelf. You feel your own orgasm quickly approaching."
        menu:
            "Cum inside of her.":
                me "Here I come Steph!"
                if stephO.cumslut:
                    steph "Yes! Hurry up and pump that load into me!"
                "You give her a few more quick thrusts, then press yourself deep inside of her as you climax. She gives a long, low moan as you pump her cunt full of cum."
                show steph fuck51 at right
                $stephO.inc_cum_inside()
                "You stay together for a few seconds after you're done, both breathing heavily. When you finally step back and pull your cock out a trickle of semen starts to run down her leg."
                steph "Ah... Oh wow..."
                me "That felt great Stephanie. Just what we both needed."
                if stephO.preg_response_ok():
                    "She nods and stands up, legs shaking a little."
                else:
                    steph "Fuck, I forgot to make you pull out... It's probably fine this time, but we shouldn't risk it when I'm not on my birth control."
                    "She stands up, legs shaking a little."
                steph "Okay, we need go get this inventory done quick before Nora notices we're running late."
                "The two of you get back to work, Stephanie's dripping pussy leaving little drops of your cum on the floor every few seconds."
                show steph work at right
                show nora work at left
                "When you're finally finished you both get dressed again and head back into the main lab room. Stephanie presents the report to Nora, then goes to get cleaned up."

            "Cum in her mouth.":
                me "I'm going to cum Steph! I want to cum right in your mouth!"
                steph "Oh fuck yes, please!"
                "You pull out and squeeze back as well as you can, rattling the shelf behind you. Stephanie spins around and squats down, looking up with her mouth open wide for you."
                "You plant the tip of your cock onto her lips and stroke yourself off until you climax, spraying your load inside of her mouth and down the back of her throat."
                "Stephanie moans loudly again and shivers with pleasure, holding still until you've completely finished cumming."
                show steph fuck52 at right
                $stephO.inc_cum_mouth()
                $stephO.inc_cum_swallow()
                "Once you're done she leans back on the shelf and fingers herself, her mouth still wide open and filled with your semen."
                "You watch as she shivers again, then relaxes. She closes her mouth and swallows loudly, taking a few seconds to drink down all of your cum."
                me "Damn Stephanie, that was amazing. Just what we both needed."
                show steph strip2 at right
                "She nods and stands up, legs shaking a little."
                if stephO.cumslut:
                    steph "You taste so fucking good. I need to make sure I didn't miss any."
                    "She leans forward and starts to lick the sides of your cock, cleaning up the last few drops of your semen along with her own pussy juices. Once she's satisfied she sits back again."
                    steph "I think that's everything. We should get this inventory done quick before Nora notices we're running late."
                else:
                    steph "You tasted so good. Thank's for the treat [inputName]."
                    me "Any time, it was my pleasure."
                    steph "We should get this inventory done quick before Nora notices we're running late."
                show steph work at right
                show nora work at left
                "The two of you get back to work, and soon you've finished your task. You both get dressed and head back into the lab room; Stephanie presents the report to Nora."
        $ steph_stockroom.inc_level(3)
        $ stephO.change_resist(-steph_stockroom.use_red(3,stephO.resist_score))

    return

label min_steph_beach_volley:
    me "There are the volleyball nets set up, lets go take a look at those."
    steph "Me versus you? Sounds like fun, lets go!"
    "You head off to the volleyball nets and take one of the empty sections of sand."
    steph "Is there anywhere for us to get a ball? I didn't even think about bringing one."
    me "Me neither. I didn't see anywhere that might have them."
    steph "Oh well, we'll remember next time I guess."
    "Stranger" "Hey, I don't mean to eavesdrop, but we've got an extra ball if you need one."
    "The team on the court beside you takes has taken a break, and one of the players has a volleyball in one hand."
    steph "That would be great, actually! Thanks!"
    "Stranger" "No problem at all. Just send it back over when you're done."
    "He throws Stephanie the ball and turns back to his friends."
    steph "Alright [inputName], lets do this! Ready?"
    me "Ready, serve whenever you're ready."
    "Stephanie serves the ball to you, and you return it with a bump on your forearms. You rally it back and forth for a few minutes, one or the other ocacsionally scoring a point."
    "The game beside you ends, with two of the four players heading off down the beach. The two remaining players watch you and Stephanie play until you reach a natural breaking point."
    "Stranger" "You two are looking pretty good! What do you say to a team game, us vs you two."
    steph "Sure, lets do it. Come on [inputName]. Get over here and lets do this!"
    if stephO.slut_score < 45:
        #Just play
        me "Alright, you serve and I'll play up front Stephanie."
        "You get set up across from the other team. Stephanie serves, and they return the ball to you. After a short rally you jump and block the ball, scoring a point."
        "Stranger" "Damn! Nice one!"
        steph "Nice [inputName]!"
        "The four of you play for half an hour with the points suprisingly close."
        "Stranger" "Ah, that was fun you two. We've got to head out, but we're up for a game if you're ever around again."
        "You and Stephanie give them high fives and pass their ball back before they leave."
        steph "Whew, that really got the blood flowing. Come on, lets head back."
    elif stephO.slut_score < 70:
        #Play and give them a quick flash them if they win.
        me "Alright, you serve and I'll play up front Stephanie."
        "You get set up across from the other team. Stephanie serves, and they return the ball to you. After a short rally you jump and block the ball, scoring a point."
        "Stranger" "Damn! Nice one!"
        steph "Nice [inputName]!"
        "The four of you play for half an hour with the points suprisingly close."
        "Stranger" "Okay, this will have to be the last play for us guys. Ready?"
        steph "I haven't been keeping count, so lets just make this winner takes all for all the bragging rights."
        "Stranger" "Deal. Lets go!"
        "You play out a short rally, with the game ending when your opponent spikes the ball down past your block."
        steph "No!"
        me "Good game guys."
        "Stranger" "Yeah, that was fun. If we see you around some other time we'll have to do this again."
        steph "Definitely. Would you two like your prize now?"
        "Stranger" "What prize?"
        $ stephO.inc_naked()
        if slut_outfit:
            show steph strip41 at right
            "Stephanie pulls up her bikini top, letting her tits fall free."
            "She gives them a quick shake, then pulls the top down again."
            show steph swim2 at right
        else:
            show steph strip40 at right
            "Stephanie slips her arms out of the top of her swimsuit, then pulls it down past her tits."
            "She gives them a quick shake, then pulls it back up again."
            show steph swim1 at right
        steph "That prize. See you next time."
        "She winks and passes the ball back to them."
        steph "Come on [inputName], lets head back towards the center of the beach."
        $ steph_beach_volley.inc_level(0)
        $ stephO.change_resist(-steph_beach_volley.use_red(0,stephO.resist_score))

    elif stephO.slut_score < 100 or not stephO.exhib:
        #Play and give them a good look at everything if they win.
        me "Alright, you serve and I'll play up front Stephanie."
        "You get set up across from the other team. Stephanie serves, and they return the ball to you. After a short rally you jump and block the ball, scoring a point."
        "Stranger" "Damn! Nice one!"
        steph "Nice [inputName]!"
        "The four of you play for half an hour with the points suprisingly close."
        "Stranger" "Okay, this will have to be the last play for us guys. Ready?"
        steph "I haven't been keeping count, so lets just make this winner takes all."
        "Stranger" "And what's the prize?"
        steph "Well..."
        "Stephanie cups her breasts and bounces them around a little."
        steph "How about I give the winner a good look at me. Sound good to you [inputName]?"
        me "Sounds fine to me, I'm sure we're going to win."
        steph "I like the confidence. Lets do this then!"
        "You play out the rally, barely saving the ball when it's spiked down past your guard. You pass it to Stephanie, who's able to bump it over the net. The other team scrambles to return it, bumping it high in the air."
        steph "Oh boys!"
        show steph strip41 at right
        $ stephO.inc_naked()
        "Stephanie yells to get their attention, then pulls the top of her bikini up and lets her tits free."
        "Stranger" "Oh shit! Fuck!"
        "The two players on the other team stumble into each other, both missing the ball entirely. It falls to the sand, making you and Stephanie the winners."
        steph "Yes! Woo!"
        "Stranger" "Damn! You cheated!"
        steph "Me? No, I just used my natural charms."
        "Stephanie smiles innocently, her tits still out in the open."
        "Stranger" "I suppose. Well, good game, we've got to get going."
        show steph swim2 at right
        "Stephanie pulls down her bikini top and passes them their volleyball. They take it and head off, looking over their shoulders at Stephanie."
        steph "Now, I think this was the deal if we won..."
        show steph strip41 at right
        "She pulls her top up, letting her tits out. She gives them a quick shake for you, bouncing them left and right."
        steph "Hmm, maybe you want a look at my pussy too, right? Here."
        show steph strip42 at right
        "She turns around and bends over, pulling her swimsuit to the side."
        me "Wow, you're looking really good today Stephanie."
        steph "Thanks, all that activity got me worked up. Watching you play like that helped too, I'm a little bit wet actually."
        "She runs a finger along her pussy, pausing to play with her clit for a moment."
        show steph swim2 at right
        "Stephanie gives her ass a quick smack, then stands up and pulls her swimsuit back into position."
        steph "Alright, we should get moving before someone comes along to get us in trouble."
        me "Yeah, you're right."
        "The two of you head back towards the center of the beach."
        $ steph_beach_volley.inc_level(1)
        $ stephO.change_resist(-steph_beach_volley.use_red(1,stephO.resist_score))

    else:
        me "Alright, you serve and I'll play up front Stephanie."
        "You get set up across from the other team. Stephanie serves, and they return the ball to you. After a short rally you jump and block the ball, scoring a point."
        "Stranger" "Damn! Nice one!"
        steph "Nice [inputName]!"
        "The four of you play for half an hour with the points suprisingly close."
        "Stranger" "Okay, this will have to be the last play for us guys. Ready?"
        steph "I haven't been keeping count, so lets just make this winner takes all."
        "Stranger" "And what's the prize?"
        steph "Well..."
        "Stephanie cups her breasts and bounces them around a little."
        steph "I don't have much in the way of cash that I could offer, but I'm sure there's something else I could do for you."
        "She runs a finger along her lips, sucking on it seductively at the end."
        steph "What do you say [inputName]?"
        me "Well it's hard to say no to that. Lets just make sure we win, okay?"
        "Stephanie gives you a wink, then faces the other team."
        steph "Okay, lets do this then!"
        "You play out the rally, barely saving the ball when it's spiked down past your guard. You pass it to Stephanie, who's able to bump it over the net. The other team scrambles to return it, bumping it high in the air."
        steph "Oh boys!"
        show steph strip41 at right
        "Stephanie yells to get their attention, then pulls the top of her bikini up and lets her tits free."
        "Stranger" "Oh shit! Fuck!"
        "The two players on the other team stumble into each other, both missing the ball entirely. It falls to the sand, making you and Stephanie the winners."
        steph "Yes! Woo!"
        "Stranger" "Damn! You cheated!"
        steph "Me? No, I just used my natural charms."
        "Stephanie smiles innocently, her tits still out in the open."
        "Stranger" "I suppose. Well, good game, we've got to get going."
        steph "Oh, you two aren't going to stay and watch me give our winner his prize?"
        "She steps up next to you and cups your package, rubbing it through your swimsuit."
        "Stranger" "Well, we weren't planning on it..."
        steph "Come on, stay just a few minutes. It would mean a lot to me."
        show steph blow38 at right
        $ stephO.inc_blow()
        "She drops to her knees and pulls your swimsuit down, letting your hard cock flop down onto her cheek."
        "Stranger" "Oh shit, this girls a freak!"
        "Stephanie opens her mouth wide and slides you in, looking up as takes your cock down her throat. She pauses for a few seconds when her nose bumps against your stomach, her throat constricting and relaxing rythmically around your shaft."
        me "Yeah she is. Look at her take that down. You love it, don't you Steph."
        "Stephanie nods as well as she can manage, then starts to bob her head up and down along your wet dick."
        "The two volleyball players watch while Stephanie sucks you off, right in the middle of the beach. Eventually some other people notice too, either turning to watch or turning away and pretending not to see anything."
        me "Fuck that feels good. Keep it up Steph, I want you to make me cum."
        "Another half hearted nod, and she sucks you off even faster. She makes soft gagging noises each time the tip of your penis bumps against the back of her throat."
        "Stranger" "Shit, look at her go!"
        "Not much later you feel your orgasm start to build, building quickly as Stephanie works her way up and down your shaft."
        menu:
            "Cum down her throat.":
                me "Alright, here I cum Stephanie!"
                show steph blow39 at right
                $ stephO.inc_cum_mouth()
                $ stephO.inc_cum_swallow()
                "You place a hand on the back of her head and push her down on your cock. She slides down easily, looking up at you as grunt and start to empty your balls down her throat."
                "When you've finished you give her mouth a few quick thrusts, then pull out with a pop. Stephanie takes a deep breath and smiles at you."
                steph "Thank you [inputName], Ah... That felt great!"
                "She turns to her side and winks at the two volleyball players."
                steph "Maybe you'll get lucky next time guys!"
                me "Come on, we should probably go for a quick walk before someone shows up to throw us out of here."
                show steph swim2 at right
                "Stephanie pulls her bikini top back on, wiggling her tits into place, and follows you as you walk down the beach. You head inland a little bit and wait a few minutes in the shade under some trees before heading back."

            "Cum on her face.":
                me "Alright, here I cum Stephanie!"
                "You place a hand on the back of her head and guide her up and off, tilting it back so she's looking up at you while you stroke yourself off for the last few moments."
                show steph blow40 at right
                $ stephO.inc_cum_over()
                "You climax, blowing your hot load over Stephanie's eager face. She gasps softly as each pulse of warm semen lands on her."
                "When you're done you let your arms fall limp at your sides. Stephanie slides the tip of your cock back into her mouth and sucks off the last few drops of cum."
                "After that, she pulls off again and turns towards the volleyball players, cleaning some of your semen off her face while she looks at them."
                steph "Maybe you'll get lucky next time guys!"
                me "Come on, we should probably go for a quick walk before someone shows up to throw us out of here."
                show steph swim2 at right
                "Stephanie pulls her bikini top back on, wiggling her tits into place, and follows you as you walk down the beach. You head inland a little bit and wait a few minutes in the shade under some trees before heading back."
        $ steph_beach_volley.inc_level(2)
        $ stephO.change_resist(-steph_beach_volley.use_red(2,stephO.resist_score))
    return


#########################
##Alexia's Minor Scenes##
#########################

label min_alex_nudes:
    if alexO.slut_score < 30: #Sends pictures of problems.
        "There's a pause in the coversation, then you get a bunch of pictures of Alexia's textbook."
        alex "Alright, here's where I'm stuck. I've got the conversion coefficent, but I don't understand why we need it."
        "You spend a while sending equations and hints to Alexia, careful not to make them too easy. When you're done she's feeling more prepared for the test."
        alex "Thanks [inputName]. I owe you one. I've got to go, have a good day!"
    elif alexO.slut_score < 50: #Send pictures of her tits. Plus the problem.
        "There's a pause, then you get a few pictures from Alexia. The first few are of her textbook with different problems highlighted."
        show alex phone1 at truecenter
        $ alexO.inc_naked()
        "The last one is a close up of her tits pulled out from her sweater and bra. Her nipples are hard."
        alex "I hope that's enough for you, I really need your help on this."
        me "Lets see what we can do about the problems then. ps. your tits look great."
        alex ";)"
        "You spend a while sending equations and hints to Alexia. You do your best not to make them too easy so she's mostly solving them herself. When you're done she's feeling more prepared for the test."
        alex "Thanks [inputName]. You really saved my..."
        show alex phone2 at truecenter
        "You get another picture. It's Alexia's ass while she bends over."
        alex "on this one."
        me "Clever. It was my pleasure. Let me know if you need any more help."
        alex "Will do. Have a great day!"
        $ alex_nudes.inc_level(0)
        $ alexO.change_resist(-alex_nudes.use_red(0,alexO.resist_score))
    elif alexO.slut_score < 70: #Send you a few nudes.
        "There's a pause, then you get a couple of pictures."
        alex "Hope these are good enough to convince you to help me."
        show alex phone3 at truecenter
        $ alexO.inc_naked()
        "The first is a picture of Alexia naked. She's smiling at you and posing for the camera, which she's propped up on something."
        "You enjoy it for a moment, then check out the second."
        show alex phone4 at truecenter
        "Now she is lying naked on her bed, legs spread so you can see her pussy."
        me "I just meant pictures of the problems, but this certainly helps."
        alex "Well consider that a bonus then."
        "A pause, then another picture."
        show alex phone5 at truecenter
        "Alexia's in a skimpy red set of lingerie now." #TODO make it dependent on the mall lingerie option.
        alex "There, now I've got some clothes on so I won't get distracted."
        "You get a few more pictures of her textbook with problems highlighted."
        "You spend a while sending equations and hints to Alexia. You do your best not to make them too easy and she does a good job solving them herself. When you're done she's feeling more prepared for the test."
        alex "Thanks [inputName]. You saved me on this one."
        me "No problem. Let me know if you need anything else."
        alex "Will do, I'm sure there's plenty more you'd like to see ;)"
        alex "Talk to you later!"
        $ alex_nudes.inc_level(1)
        $ alexO.change_resist(-alex_nudes.use_red(1,alexO.resist_score))
    else: #Fuck the problem, she's horny now.
        alex "Just as I start trying to work you want pics of me :P I guess we'll have to take care of this then."
        me "I meant pictures of the problems silly."
        "There's a pause, then you get a picture of Alexia."
        show alex phone4 at truecenter
        $ alexO.inc_naked()
        "She's naked, and she propped up her phone so you can see her on her bed."
        alex "Too late, my clothes are already off."
        "Another picture, now she's mounted her phone somewhere and is lying on her back with her legs spread."
        alex "What do you think? Vibrator or dildo?"
        menu:
            "Vibrator.":
                me "Get that vibrator going."
                alex "Mmm, it always makes me cum super hard too, how did you know?"
                me "Lucky guess I suppose."
                "A few moments later you get another picture."
                show alex phone6 at truecenter
                "Alexia's still on her back, black vibrator held tight against her clit with one hand while the other holds a tit. Her back is arched, a silent moan on her face."
                me "Wow, you're really getting into it."

            "Dildo.":
                me "I'm thinking your dildo."
                alex "A classic. Nothing like a little manual pleasure."
                "A few moments, then another picture."
                show alex phone7 at truecenter
                "Alexia's kneeling on her bed, pink dildo buried in her pussy and one hand rubbing her clit."
                me "Damn that's hot."

        "A long pause, then she messages back."
        if alexO.exhib:
            alex "Whew, just finished. I hope you enjoyed the show. I know the other guys did."
            me "Other guys?"
            alex "Yeah, I sent out those pictures to a group I'm part of. They love watching me get off like that."
            me "Glad I got to be a part of that. Feeling ready to focus now?"
        else:
            alex "Whew, just finished. Hope you enjoyed the show ;)"
            me "I definitely did. Feeling ready to focus now?"
        alex "I'll do my best."
        "You get a few pictures with highlighted problems from her textbook. You do your best to give her advice and hints, and when you're done she's feeling more prepared for her test."
        alex "Thanks [inputName]. If I need any more help I'll let you know. Talk to you later!"
        $ alex_nudes.inc_level(2)
        $ alexO.change_resist(-alex_nudes.use_red(2,alexO.resist_score))
    return

label min_alex_porn_start:
    if alexO.slut_score < 30: # Just flirt a little
        alex "Aww, that's sweet. I'll do what I can to keep you company then :)"
        "You and Alexia talk for an hour or two, flirting playfully with each other."
        alex "I've got to go, talk to you later, okay?"
        me "Sure thing. Later."
    elif alexO.slut_score < 50 or (alexO.slut_score >= 50 and not alexO.exhib): # A tit flash for you, any higher requires public tag
        alex "Aww, feeling \"lonely\"? I can definitely help you out with that."
        show alex phone8 at truecenter
        $ alexO.inc_naked()
        "There's a pause, then you get a picture. Alexia has her shirt and bra pulled up and she's pinching a nipple with one hand."
        alex "How's that? Helping?"
        me "Wow, you're looking good. Ya, helping a lot."
        alex ":) So what are you up to? Anything cool?"
        "You and Alexia talk for another hour or two, but she doesn't send you any more pictures."
        alex "I've got to go, talk to you later [inputName]."
        me "Sure thing, bye!"
        $ alex_porn_start.inc_level(0)
        $ alexO.change_resist(-alex_porn_start.use_red(0,alexO.resist_score))
    else: # She tells you about her porn site.
        alex "Aww, feeling \"lonely\"? I can definitely help you out with that."
        show alex phone8 at truecenter
        $ alexO.inc_naked()
        "There's a pause, then you get a picture. Alexia has her shirt and bra pulled up and she's pinching a nipple with one hand."
        alex "How's that? Helping?"
        me "Wow, you're looking good. Ya, helping a lot."
        if not alex_porn_site:
            alex "Well if you like that, I've got some other stuff you can look at."
            alex "Promise not to tell anyone else?"
            me "Promise. What is it?"
            alex "Well, I've been posting some stuff online. If you're curious you can look me up. My screen name is publicAlex."
            "She sends you a link to a porn site."
            me "Wow, I'll definitely check this out later. Should be interesting ;)"
            alex "Haha, have fun. I've got to go, talk to you later, okay?"
            me "Okay, talk to you later."
            $ alex_porn_site = True
        else:
            alex "Well if you like that you should check out my page online. There's plenty more that you might like ;)"
            me "I'll make sure to do that then. It's so nice of you to make that all available for little old me."
            alex "Hehe, you're welcome!"
            "You and Alexia flirt back and forth for another hour or two."
            alex "I've got to run, talk to you later, okay?"
            me "Okay, talk to you later."
        $ alex_porn_start.inc_level(1)
        $ alexO.change_resist(-alex_porn_start.use_red(1,alexO.resist_score))
    return

label min_alex_porn_visit:
    if alexO.slut_score < 50: #Should require at least 50
        "Something's gone wrong here. I must have tweaked some values and made her unlock her porn site eariler. Send me a message on patreon and let me know you found this so I can fix it!"
    elif alexO.slut_score < 60: #Shows off her underwear, a few bend over pictures, ect. Face covered or not in the picture.
        "Alexia has a small gallery going where she's showing off her underwear collection. She's got her face covered or cropped out of all the pictures, but you would recognise that ass and those tits anywhere."
        $ randChance = renpy.random.randint(0,2)
        if (randChance == 0):
            show alex phone10 at truecenter
            "Her most popular at the moment is her bending over her bed, camera propped up on a table behind her. Her ass is a little red, like it was just slapped."
        elif (randChance == 1):
            show alex phone9 at truecenter
            "Her most recent post is a close up of her tits in a thin lacy bra."
        else:
            "You find a picture that you like and open the full res version."
            show alex phone11 at truecenter
            "She's on her bed with the phone propped up in front of her. Her legs spread, like she's inviting you in."
        $ alex_porn_visit.inc_level(0)
        $ alexO.change_resist(-alex_porn_visit.use_red(0,alexO.resist_score))

    elif alexO.slut_score < 70: #masturbates on video, only a black bar over her eyes. Blowjob pictures if you've taken them.
        "Alexia's been taking pictures of herself while she masturbates. She's covered her eyes with a single black bar, but it's not hard to figure out who it is if you know her."
        "You pick one of the pictures that looks interesting and open up the full res image."
        $ randChance = 0
        if not alex_has_blow:
            $ randChance = renpy.random.randint(0,1)
        else:
            $ randChance = renpy.random.randint(0,2)

        if (randChance == 0): #Naked and showing off
            show alex phone12 at truecenter
            "Alexia's naked in front of her mirror, one hand between her legs, the other holding a tit tight. It's hard to tell, but her pussy looks like it's wet and dripping down her leg."
        elif (randChance == 1):
            show alex phone13 at truecenter
            "Alexia's propped her phone on a table to free up both her hands. One is running a vibrator over her clit while the other slips a couple of fingers into her pussy. She looks like she's in a silent orgasm."
            #Using a vibrator on her bed.
        else:
            "It seems Alexia's put your blowjob pictures up."
            show alex phone17 at truecenter
            "The first is her going balls deep on your shaft."
            show alex phone16 at truecenter
            "Then she's leaning back and you've sprayed your load over her face."
            #Your blowjob picture from earlier.
        $ alex_porn_visit.inc_level(1)
        $ alexO.change_resist(-alex_porn_visit.use_red(1,alexO.resist_score))

    else: #masturbates in public, nothing to hide her identity. Fuck pictures if you've taken them.
        "Alexia's porn channel seems to be all about public sex and masturbation. You recognise the thumbnails on a few of them as places on campus."
        $ randChance = 0
        if not alex_has_fuck:
            $ randChance = renpy.random.randint(0,1)
        else: #ie. has a chance to show you pictures of you fucking her.
            $ randChance = renpy.random.randint(0,2)

        if (randChance == 0):
            "You pull up one picture and recognise the library on campus."
            show alex phone14 at truecenter
            "Alexia is at an individual study desk with her chair slid back a little. She's got her shirt and bra pulled up past her tits to show them off, and her legs spread so she can slip a pair of fingers inside her pussy."
            #Rubbing herself in a library
        elif (randChance == 1):
            "You pull up a picture and recognise one of the lecture halls on campus."
            "The first picture is a wide shot of the room, showing a hundred or so students focused on the lecture."
            show alex phone15 at truecenter
            "The next is a shot up her skirt where a dildo is slipped deep into her pussy and covered in her juices already."
            #Dildo in her pussy in class.
        else:
            "You notice a familiar scene and open up a set of images."
            "You recognise your own cock in Alexia's mouth while she was blowing you beside one of the buildings on campus."
            show alex phone18 at truecenter
            "The next image is her bent over against a wall, skirt gathered around her waist and underwear pulled to the side. You're just starting to slide your cock into her pussy."
            show alex phone19 at truecenter
            "The last picture in the set is her leaning against the wall, panting hard while your cum leaks out of her and runs down her leg."
            #You fucking her on campus.
        $ alex_porn_visit.inc_level(2)
        $ alexO.change_resist(-alex_porn_visit.use_red(2,alexO.resist_score))
    "You spend a good long while enjoying yourself on the site, and tidy up when you're finished."
    return

label min_alex_porn_help:
    me "I think I could do that, ya."
    "Alexia smiles brightly and looks around."
    alex "Okay, follow me."
    "She grabs your hand and pulls you through the crowd, leading you outside the building."
    alex "We're going to have to find somewhere quiet."
    "You spend a few minutes following Alexia, who seems to have a pretty good idea of where to go."
    "Finally she pulls you into a small walkway between two of the administration buildings at the edge of campus."
    alex "This should work. Are you ready?"
    me "I think so, what do you want me to do?"
    if alexO.slut_score < 70: #She blows you, and you cum on her face
        "Alexia pushes you gently against the wall and drops to her knees."
        alex "First I want you to get your cock out for me. Then I want you to take this and make sure you get plenty of pictures."
        "She hands her phone up to you, already in camera mode."
        alex "I'll take care of everything else."
        show alex blow8 at right
        $ alexO.inc_blow()
        "She takes your already hard cock in her hand and wraps her mouth around your tip. She looks up at you as she starts to move her head deeper, placing her hands behind you to pull you closer to her."
        "Before long she's sliding your full length into her throat, nose tapping your stomach with each pass."
        me "Take it as deep as you can and look up at me."
        "Alexia slides down deep, pressing your tip against her throat. She looks up as much as she can, staring into the camera. You take a few pictures, then she pulls off and takes a deep breath."
        alex "Whew. Nice. How are you doing?"
        "She rubs your shaft while you talk."
        me "I'm getting close, your throat feels great."
        alex "Good, enjoy it. When you're ready I want you to cum on my face. The guys online love that."
        "You nod, and Alexia slides you back into her mouth. She blows you fast and deep, and it's not long before you're ready to cum."
        me "Here it is Alexia!"
        show alex blow9 at right
        $ alexO.inc_cum_over()
        "She pulls her head back and looks up at you, stroking you as quickly as she can. You moan and fire your load over her face while she drags your tip around to make sure you get everything."
        "You take a few pictures, doing your best to keep the phone pointed at her while you orgasm."
        if alexO.cumslut:
            "Alexia takes a deep breath, quivering a little while your cum drips down her face."
            alex "God that feels so good. How do the pictures look?"
        else:
            "When the last bit of cum has dripped off she lets go and sits back."
            alex "Good job, did you get some good pictures."
        me "Uh huh. Take a look."
        "Alexia wipes some cum out of her eye so she can open it and takes her phone back."
        alex "Ooh, that's hot. Thanks [inputName], this should be perfect."
        "She stands up and smiles at you, face still covered in cum."
        me "Good, I'm glad I could help. Let me know if there's anything else you would like."
        alex "Will do. See you around!"
        $ alex_has_blow = True
        "She heads off down the pathway while you get your pants back up."
        $ alex_porn_help.inc_level(0)
        $ alexO.change_resist(-alex_porn_help.use_red(0,alexO.resist_score))
    else: #She bends over and you fuck her, then cum inside
        alex "First, take this. Make sure to get some good pictures."
        "She hands you her phone, already in camera mode."
        alex "Second, I'm going to get you nice and wet."
        show alex blow3 at right
        $ alexO.inc_sex()
        "She drops to her knees and pulls your pants down. Without a moment's hesitation she takes your tip into her mouth and starts giving you a blowjob."
        "You snap a few pics of her while she blows you, then she pulls off."
        alex "And third, you're going to fuck me until you finish deep inside me."
        "Then she leans over against the wall and pulls up her skirt for you."
        me "Oh, is that all? I think I can manage that."
        show alex fuck20 at right
        "You step up behind her and pull her panties to the side. You rub your wet tip along her slit, then push your way into her pussy slowly."
        "Alexia moans as you get all the way inside, but turns and smiles at you."
        if alexO.anal:
            alex "Ah, there we go. Can you stick your thumb in my ass? I wish it was your cock, but I've got to give the people what they want..."
            "You try to keep the phone steady with one hand while you slip your thumb into Alexia's tight butthole. She moans loudly and pushes her hips against you while you pump into her from behind. You make sure to take plenty of pictures as you go."
        else:
            alex "There we go, just like that."
            "You hold onto her ass cheek with one hand while you try and keep the phone steady with the other. You pump into her from behind for a while, taking pictures as you go."
        "Between the blowjob and her tight pussy it doesn't take long before you're ready to finish. You squeeze her ass and pump harder."
        me "I'm almost there. You're sure about this?"
        if alexO.preg_response_ok():
            if alexO.cumslut:
                alex "Yes, I want you to feel your cum inside me [inputName]. Please fill me up!"
            else:
                alex "Oh ya, they love creampies online. Fill me up!"
        else:
            alex "Yeah, I think today is safe and they love creampies online. This might be your only chance, so fill me up!"
        "She gasps as you fuck her as hard as you can then start to cum inside of her. She moans and pants as you fire off your load, leaning hard against the wall."
        show alex fuck21 at right
        $ alexO.inc_cum_inside()
        "When you're done you pull out and take some pictures of your cum as it leaks out and runs down her leg."
        if alexO.cumslut:
            alex "Mmm, it's so warm..."
            "Alexia takes a deep breath, quivering with pleasure."
            alex "Right, the pictures. How do they look?"
        else:
            alex "How does it look?"
        me "Fantastic. They're going to love this."
        "Alexia takes a few moments to catch her breath, then stands up and does her best to get her panties back in place and her skirt smooth."
        alex "Let me see what we've got then."
        "You hand her phone back and she flips through the pictures."
        alex "Wow, that's super hot. Good job [inputName]."
        me "No problem, glad I could help. Let me know if there's anything else you would like to do."
        alex "Will do. Now I've got to run, I've got a class to get to. Hope nobody minds if my pussy's a little wet."
        "She smiles at you and starts heading down the path."
        me "Have fun, see you around!"
        $ alex_has_fuck = True
        $ alex_porn_help.inc_level(1)
        $ alexO.change_resist(-alex_porn_help.use_red(1,alexO.resist_score))
    return

label min_alex_nap:
    if alexO.slut_score < 20: # Just startles you.
        alex "Well hello there sleepy head."
        "You jerk awake, startled by the voice rignt next to you."
        show alex casual at right
        alex "Funny running into you here."
        "Alexia is lying next to you on her side, head propped on an arm. You're still groggy from the nap and a little confused."
        me "Ah, what?"
        "Alexia laughs as you try and figure out what's going on."
        alex "It's just me. Relax."
        me "Right. Hey Alexia."
        alex "Hello. Having a good nap?"
        me "I was actually, thank you very much."
        "Alexia slides closer."
        alex "Good. Make a little room on your backpack for me, would you?"
        "You slide over and Alexia lies down completely, head next to yours."
        me "So, what are you up to?"
        alex "Killing time before class. You looked like you were just so comfortable."
        me "Can't have that, better wake him up!"
        alex "Ha-ha. No, I wanted to come over and join you."
        "She looks you in the eyes and smiles."
        alex "Do you mind?"
        me "Not at all."
        "You and Alexia spend an hour having a nap together. By the time her class rolls around you've got an arm around her and she's snoring gently on your chest."
        "Her phone beeps softly, and she wakes up with a snort."
        alex "Aw shit."
        me "Time to go?"
        alex "Time to go. Thanks for sharing with me [inputName]. See you around."
        "Alexia gets up and waves as she walks away."

    elif alexO.slut_score < 40: # Grabs you by the crotch to wake you up.
        "You're woken up from your nap suddenly by a tight pressure on your crotch, not quite painful but certainly unexpected."
        alex "That certainly woke you up!"
        me "Ah, what?"
        show alex hand2 at right
        "Alexia is lying on her side next to you, one hand propping her head up while the other holds onto your penis through your pants."
        "You're still groggy from the nap, and take a moment to process it all."
        alex "Aww, you're so cute when you're sleepy."
        "She leans forward and kisses you, then releases your crotch."
        alex "I've got some time to kill before my class. Mind if I join you?"
        me "Uh, sure. Here."
        "You slide over to make room on your pillow/backpack. Alexia rests her head next to yours."
        alex "Having any good dreams?"
        me "Nothing that I remember."
        alex "Well I think one part of you remembers."
        "She nods down to your waist, where you realize you have a sizable erection."
        me "Oh, ya. I suppose so."
        show alex hand3 at right
        "Alexia laughs and leans against you, putting an arm across your chest."
        "For an hour you two have a nap together. When her phone starts to beep you've got your arm around her, and her head is resting on your chest."
        alex "Damn. Time to go."
        me "Okay. Have a good time in class."
        alex "Thanks. I'll see you around."
        "Alexia gets up and waves goodbye as she walks away."
        $ alex_nap.inc_level(0)
        $ alexO.change_resist(-alex_nap.use_red(0,alexO.resist_score))
    elif alexO.slut_score < 80 or (alexO.slut_score >= 80 and not alexO.exhib): # Wakes you up with her hand down your pants already.
        "You're slowly woken up by a strange sensation around your waist."
        show alex hand1 at right
        $ alexO.inc_hand()
        "You rub your eyes, and come face to face with Alexia beside you. She's lying on her side, head propped up on a hand."
        alex "Good morning sleepy head. Have a good nap?"
        "Looking down, you realize she's got her hand slipped under your pants and underwear and is stroking your already hard cock."
        alex "I noticed this guy was excited. I hope you don't mind."
        me "Ah, no, not at all."
        alex "Good. Make a little room for me."
        "You slide over on your pillow/backpack so Alexia can put her head down on it. You glance around, but this part of campus is nice and quiet and nobody else is nearby."
        "Her hand slides up and down one side of your shaft, pressing her warm palm against it."
        alex "How's that feel?"
        me "Really good."
        "She smiles and wraps her hand completely around you, rubbing faster."
        alex "I thought it would be rude to wake you up from a nap and not give you anything in return."
        "Alexia pulls her hand out of your pants and runs her tongue along it from the base of the palm to the tip of her fingers. She slides it back down and strokes you a few times to get you wet and slippery."
        me "Fuck, that's great."
        alex "Just lean back and enjoy."
        "You do so, and Alexia rubs you for a long ten minutes. Every so often she pulls her hand out and licks it again to keep it nice and wet."
        "Finally she drives you to the edge of orgasm."
        me "I'm almost there, keep going."
        "Alexia speeds up some more and holds on tight as you begin cumming in your pants."
        "When you're done she pulls her hand out slowly, bringing as much of your load with her as possible. She glances at her sticky hand then smiles at you."
        alex "Good job. Feeling like getting back to that nap now?"
        show alex hand3 at right
        "You nod, and Alexia snuggles close to you. She places her head on your chest, and within a few minutes you're both asleep."
        "Half an hour later Alexia's phone beeps."
        me "Time to go?"
        alex "Time to go. That was fun, see you around!"
        "She heads off, waving goodbye as she goes."
        $ alex_nap.inc_level(1)
        $ alexO.change_resist(-alex_nap.use_red(1,alexO.resist_score))
    else: # Wakes you up by blowing you in public
        "You're slowly woken up by a strange sensation around your crotch."
        show alex blow10 at right
        $ alexO.inc_blow()
        "You open your eyes, and look down. All you can see is the top of Alexia's head and her ass a little above that."
        me "Alexia? What?"
        "You rub your eyes, still waking up. Alexia's head slides up and down and you realize you were feeling her tongue on your cock."
        "She finally pulls off with a wet pop and looks up smiling."
        alex "Good morning sleepy head. I noticed you were a little hard, so I thought I'd help you out."
        me "Oh, that's very nice of you."
        "You look around, but there's nobody else nearby on this part of campus."
        "Alexia goes back to sucking on your cock."
        "For a few minutes you enjoy the feeling of her warm mouth and the sight of her ass bobbing behind her. Eventually you feel your orgasm building up."
        me "You're doing great, I'm almost there Alexia."
        $ alexO.inc_cum_mouth()
        $ alexO.inc_cum_swallow()
        "She mumbles something past your cock and speeds up. You hold onto her head and guide her as you cum in her mouth and down her throat."
        "When you're done Alexia pulls off and takes a moment to swallow, then takes a deep breath."
        if alexO.cumslut:
            alex "Fuck, you taste so good [inputName]."
            "She leans forward and slides your cock back into her mouth. She runs her tongue along the sides of your shaft, cleaning up every last drop of sperm before pulling off again."
            alex "Mmm, delicious. Now, can I join you for a nap now?"
        else:
            alex "Wow. So, can I join you for a nap now?"
        me "Of course, come on up."
        show alex hand3 at right
        "You slide over on your pillow/backpack and make room for Alexia. She cuddles next to you, resting her head on your chest, and soon you've both fallen asleep."
        "A few minutes later her phone beeps, but she turns it off."
        me "Time to go?"
        alex "Just a little while longer."
        "You hold her close, and drift back to sleep. It's another hour before you're both ready to get up. Alexia gives you a quick kiss, then heads off to catch a bus."
        $ alex_nap.inc_level(2)
        $ alexO.change_resist(-alex_nap.use_red(2,alexO.resist_score))
    return

label min_alex_bus:
    "You jump on a bus right before it pulls away from the bus stop. It's late at night, and there are only a handful of people on it."
    show alex casual at right
    "One of them waves at you from near the back. You head to the back to talk to Alexia."
    alex "Hey [inputName]!"
    me "Hey Alexia, heading home?"
    "She nods and stands up."
    alex "Here, you can have the window seat. I prefer the aisle."
    me "Sure. Thanks."
    "You slip past Alexia and you both sit down. The bus lurches into motion, working it's way along it's route. You and Alexia make small talk for a few minutes."
    if alexO.slut_score < 15: #Normal talk
        "With no traffic you're at your stop soon after. You wave goodbye to Alexia and walk the rest of the way home."
    elif alexO.slut_score < 50: #Sexy talk
        alex "I'm always surprised how few people there are here at this time of day."
        "You look around. It's just you, Alexia, and two other people at the front of the bus waiting to get off."
        me "You're right. How can they be making any money?"
        "Alexia shrugs."
        alex "I don't know, but it's a good opportunity to get up to some trouble."
        me "What kind of trouble would that be?"
        alex "Oh, you know. You hear stories about people fucking on busses, things like that."
        me "Do you think you'd ever do something like that?"
        alex "Me? Hmm."
        "She looks you up and down, nodding a little."
        alex "Play your cards right and maybe you'll get to see."
        me "I hope so."
        "Alexia laughs a little. You chat about the logistics of bus sex for the rest of the ride. When your stop comes up you wave goodbye and walk the rest of the way home."
        $ alex_bus.inc_level(0)
        $ alexO.change_resist(-alex_bus.use_red(0,alexO.resist_score))
    elif alexO.slut_score < 70 or (alexO.slut_score >= 70 and not alexO.exhib): #Gives you a handjob, any higher requires the public tag.
        alex "I'm always surprised how few people there are here at this time of day."
        "You look around. It's just you, Alexia, and two other people at the front of the bus waiting to get off."
        me "You're right. How can they be making any money?"
        "Alexia shrugs."
        alex "I don't know, but it's a good opportunity to get up to some trouble."
        me "What kind of trouble would that be?"
        "Alexia looks you up and down, then reaches over and rubs your crotch."
        alex "This kind. I doubt anyone would notice if I jerked you off right here."
        show alex hand1 at right
        $ alexO.inc_hand()
        "She rubs you through your pants for a few seconds, then slips her hand under your pants and underwear to grip your shaft."
        me "Right, that kind of trouble. Let me help you out with that."
        "You undo your pants and slide them down low enough for Alexia to pull your cock out. She gives it a few good strokes and smiles at you."
        "For a few minutes you sit back and enjoy Alexia jerking you off. Because you've got the window seat, it would be almost impossible for anyone to notice what's going on."
        "Finally her warm soft hand drives you to the edge."
        me "I'm almost there."
        "Alexia nods and keeps jerking you off until you start to orgasm. She uses her other hand to pull your underwear up and over your tip while you cum."
        "When you're done she pulls her hand out and looks at the few lines of cum that ended up splashing over it."
        alex "How was that?"
        me "Great. I'll have to get cleaned up when I get home. You too I suppose."
        "Alexia licks your cum off of her hand and winks at you."
        alex "I think I can take care of myself somehow."
        "You pull your pants back up and wait a few minutes until your stop. You wave goodbye to Alexia and walk the rest of the way home."
        $ alex_bus.inc_level(1)
        $ alexO.change_resist(-alex_bus.use_red(1,alexO.resist_score))

    elif alexO.slut_score < 85: #Blows you
        alex "I'm always surprised how few people there are here at this time of day."
        "You look around. It's just you, Alexia, and two other people at the front of the bus waiting to get off."
        me "You're right. How can they be making any money?"
        "Alexia shrugs."
        alex "I don't know, but it's a good opportunity to get up to some trouble."
        me "What kind of trouble would that be?"
        "Alexia checks the rest of the bus quickly, then reaches over for your waist. With quick fingers she undoes your pants and tries to pull them down a little."
        alex "Let me show you."
        show alex blow7 at right
        $ alexO.inc_blow()
        "You help her slip your pants down until your cock is free. Then she holds it by the base and slips her mouth around the tip. You sit back and sigh while she starts to blow you."
        "Her mouth is warm and wet. She uses her tongue to get your shaft wet and slides herself lower with each pass."
        me "My stop is in a few minutes, you don't have much time."
        "Alexia gives you a thumbs up and speeds up. You can feel the tip of your penis tapping the back of her throat."
        "You reach a hand around and grab onto her ass while she sucks you off. Alexia wiggles her ass a little for you and keeps going."
        "A few stops before you've got to get off you feel your orgasm building up."
        me "Don't stop, you're almost there."
        $ alexO.inc_cum_mouth()
        $ alexO.inc_cum_swallow()
        "Alexia moans a little and seems to be going as fast as she can. When you start to cum she keeps her head on your cock, letting you fire your load right down her throat and into her stomach."
        "When you're finished she pulls off and takes a deep breath."
        me "That was amazing Alexia. This is my stop though."
        if alexO.cumslut:
            alex "Mmm, your cum tastes great [inputName]. Lets do this again some time."
        else:
            alex "Lets do it again some time. Goodnight!"
        "You slip past Alexia and rush off the bus. You wave goodbye as it pulls away again, then walk the rest of the way home."
        $ alex_bus.inc_level(2)
        $ alexO.change_resist(-alex_bus.use_red(2,alexO.resist_score))

    else: #Fuck on the bus
        alex "You know, there aren't many people on the bus tonight."
        "You look around. She's right, it's just you and two people at the front waiting to get off."
        me "What did you have in mind?"
        "Alexia smiles and slides over onto your lap. She pulls up her skirt and rubs your cock through your pants."
        alex "How about you just slip it in. I'm sure nobody will notice."
        "She pulls her panties to the side and touches her pussy a little, then stands up and undoes your zipper so you can pull your pants down."
        "Once you've got your cock free she presses it against her pussy, rubbing it along the length of the slit."
        me "That sounds like a good idea."
        show alex fuck18 at right
        $ alexO.inc_sex()
        if alexO.anal:
            "Alexia smiles and stands up. She moves your cock back a bit, just far enough so the tip is rubbing against her tight butthole."
            alex "Lets do it like this, I've been wanting it so badly lately..."
            "She lowers herself down, gasping as your cock stretches out her ass. Once she's gotten us to it she starts to ride you slowly, moaning under her breath."
            me "Don't make too much noice. We don't want to get caught."
            if alexO.exhib:
                alex "Fuck it, let them hear. God, you feel so big inside me..."
                "She leans forward, holding onto the seat infront of you to keep herself steady."
            else:
                "Alexia nods and speeds up, biting her lip to keep quiet. She leans forward and holds onto the seat infront of you to keep herself steady."
            "You sit back and enjoy the feeling of Alexia's incredible ass around your shaft for a few minutes. After a few minutes the bus comes to a stop and a few more people get on."
            show alex fuck19 at right
            "She pauses and pulls her skirt down when two people come to the back and take the seats one row in front of you."
            me "Maybe we should stop."
            "Alexia shakes her head and starts sliding herself up and down again while the two newcomers chat less than a yard away."
            "You can feel her ass tighten up around your dick each time she lowers herself down, and she seems to be trying to ride you even faster since the other passangers showed up."
            "A few more minutes of quiet anal and she's gotten you ready to finish."
            me "Alexia. I'm going to cum."
            $ alexO.inc_cum_inside_ass()
            if alexO.cumslut:
                alex "Come on, cum for me [inputName]. Pump that hot cum deep in my ass."
                "She speeds up a little bit, riding you fast as you start to cum inside of her. She lets out a small gasp as the first pulse hits her, then moans softly for the rest."
            else:
                "She nods and speeds up a little bit, riding you fast as you start to cum inside of her. She lets out a small gasp as the furst pusle hits her, then moans softly for the rest."
        else:
            "Alexia smiles and stands up just enough to line your shaft up with her. Then she lowers herself slowly, slipping your full length into her."
            "When you're in all the way to the base she grinds her ass against your hips and moans softly."
            me "Don't make too much noise. We don't want to get caught."
            "Alexia nods, then starts to work her hips up and down so your cock slides in and out of her. She holds onto the seat in front of you to keep herself steady."
            "Alexia rides you for a few minutes, then the bus comes to a stop and a few more people get on."
            show alex fuck19 at right
            "She pauses and pulls her skirt down when two people come to the back and take the seats one row in front of you."
            me "Maybe we should stop."
            "Alexia shakes her head and starts sliding herself up and down again while the two newcomers chat less than a yard away."
            "You can feel her pussy quiver around your dick each time she lowers herself down, and she seems to have gotten tighter since the other passangers showed up."
            "A few more minutes of quiet sex and she's gotten you ready to finish."
            me "Alexia. I'm gonna cum."
            $ alexO.inc_cum_inside()
            if alexO.preg_response_ok():
                if alexO.cumslut:
                    alex "Come on, cum for me. Get me fucking pregnant."
                    "She speeds up a little bit, riding you fast while you unload into her pussy. She lets out a small gasp as the first pulse hits her, then moans softly for the rest."
                else:
                    "She nods and speeds up a little bit, riding you fast while you unload into her pussy. She lets out a small gasp as the first pulse hits her, then moans softly for the rest."
            else:
                alex "Fuck, I hope today is safe..."
                "She speeds up anyways, riding you fast as you unload into her pussy. She lets out a small gasp as the first pulse hits her, then moans softly for the rest."
        "One of the people one row forward turns around."
        "Stranger" "Everything alright back there?"
        "Alexia is trembling on your cock as she orgasms hard. Her skin is flush and she doesn't seem capable of talking right now."
        me "Uh, ya. Everything is fine. She's scared of cars is all. Isn't that right?"
        "Alexia nods, her whole body shaking with pleasure."
        "Stranger" "You poor thing, you're trembling! I promise you we're perfectly safe. We're in the biggest thing on the road right now."
        alex "Ya, I'm happy with this big thing. Ah..."
        "The stranger seems a little confused, but nods anyway. She turns around and goes back to talking with her friend."
        "Alexia pulls off of your cock slowly and collapses into her seat. You look out the window, and realise you've already missed your stop."
        alex "That was amazing."
        me "It was, I've got to get off though."
        alex "I thought that's what we just did?"
        "You ring the bell to request a stop."
        me "I'll see you around, have a good night!"
        "You rush off the bus and wave goodbye as it leaves. Luckily you didn't go too far, and it's not a terribly long walk to get back home."
        $ alex_bus.inc_level(3)
        $ alexO.change_resist(-alex_bus.use_red(3,alexO.resist_score))
    return

label min_alex_beach_walk:
    me "Lets go for a walk and do some exploring, see what there is to see."
    alex "Sounds good to me, lead the way!"
    "You pick a direction along the beach and start walking along the waters edge."
    if alexO.slut_score < 35:
        #Just walk and talk for a while.
        alex "It's such a nice day out, we really got lucky."
        me "Yeah, we did. I couldn't think of a better person to spend it with, either."
        alex "Oh, very smooth. If I swoon will you catch me?"
        "She laughs and walks closer to you, taking wrapping one of her arms around yours."
        "You walk along the beach for fourty minutes, until you've left the crowds behind and the strip of sand has shrunk to a narrow sliver."
        alex "Well, I think that's all there is to see this way. Lets head back and see if we have time to do something else."
        "You turn around and stroll back, chatting with each other as you go."
    elif alexO.slut_score < 55:
        #Walk for a while, flash some guys who are staring at her.
        alex "It's such a nice day out, we really got lucky."
        me "Yeah, we did. I couldn't think of a better person to spend it with, either."
        alex "Oh, very smooth. If I swoon will you catch me?"
        "She laughs and walks closer to you, taking wrapping one of her arms around yours."
        "You walk along the beach for a few minutes, passing by groups of people with umbrellas and tents set up."
        alex "Hey, you see those guys over there?"
        "You follow Alexia's gaze up the beach, to a group of four guys standing around a cooler. They're not-so-subtly staring at Alexia as she walks."
        me "I'm not suprised they're interested, you're a good looking girl in a hot little bikini."
        alex "I suppose you're right. Maybe I should give them a little peek, just to be nice."
        $ alexO.inc_naked()
        if slut_outfit:
            show alex strip38 at right
        else:
            show alex strip37 at right
        "She winks at you, then lets go of your arm and turns towards the group of men. With one quick movement Alexia pulls her bra up over her tits, then gives them a little shake."
        "There's a pause, then the group erupts in wolf whistles and cheers."
        if slut_outfit:
            show alex swim2 at right
        else:
            show alex swim1 at right
        "Alexia turns away and pulls her top back down, grabbing onto your arm again. You can feel her shaking a little against you."
        alex "Come on, lets keep going."
        "You keep walking until you've left the crowds behind and the strip of sand has shrunk to a snarrow sliver."
        alex "Well, I guess that's all there is to see this way. Lets head back and see if we have time to do something else."
        me "Sure. Plan on flashing those guys again?"
        alex "I'm not sure I could take that much excitement all in one day. They'll have to be satisfied with what they got."
        "She grabs your arm and pulls you along."
        alex "Now come on, lets get going!"
        "You stroll back, chatting with each other as you go."
        $ alex_beach_walk.inc_level(0)
        $ alexO.change_resist(-alex_beach_walk.use_red(0,alexO.resist_score))
    elif alexO.slut_score < 70:
        #Walk topless
        alex "It's such a nice day out, we really got lucky."
        me "Yeah, we did. I couldn't think of a better person to spend it with, either."
        alex "Oh, very smooth. If I swoon will you catch me?"
        "She laughs and walks closer to you, taking wrapping one of her arms around yours."
        "After a few minutes of walking Alexia slows down and lets go of your arm."
        me "Everything alright?"
        alex "Yeah, I just need you to do me a favour. Pull on the knot for me, would you?"
        $ alexO.inc_naked()
        if slut_outfit:
            show alex strip40 at right
        else:
            show alex strip39 at right
        "Alexia spins around and presents the back of her swimsuit to you. You pull on the knot, and she proceeds to take the top off entirely."
        alex "There we go. If we're going to be spending a lot of time walking around in the sun I don't want to end up with tan lines. Mind keeping this in a pocket or something?"
        "She hands you the top, then holds onto your arm again. You resume your walk down the beach, now with Alexia's tits out in the open."
        "Not long after a group of guys further up the beach notices her, and begin whistling and cheering as she passes. You feel Alexia shiver, as if cold."
        me "We can turn around if you want."
        alex "No, it's fine. I'm sure it's nothing they haven't seen before."
        "You notice her nipples are rock hard, and she's carefully sliding her thighs together with each step."
        "Once you're past the group of men she takes a deep breath and relaxes her grip on your arm. Half an hour of walking passes, and the beach has become a thin strip of sand against the water."
        alex "Well, I guess that's all there is to see this way. Lets head back and see if we have time to do something else."
        me "Sure. Want to put your top back on?"
        "Alexia shakes her head and takes your arm again, leading you back the way you came."
        alex "No, I... I like the way it feels when people watch me like that."
        "You stroll back, chatting with each other as you go. Alexia eagerly points out all of the men trying to take subtle glances at her tits, pressing up against your side tightly as you walk."
        if slut_outfit:
            show alex swim2 at right
        else:
            show alex swim1 at right
        "She finally puts her top back on when you get back to the heavily populated area of the beach, to avoid getting you both in trouble."
        $ alex_beach_walk.inc_level(1)
        $ alexO.change_resist(-alex_beach_walk.use_red(1,alexO.resist_score))

    elif alexO.slut_score < 90 or not alexO.exhib:
        #Walk completely naked and touch herself.
        alex "It's such a nice day out, we really got lucky."
        me "Yeah, we did. I couldn't think of a better person to spend it with, either."
        alex "Oh, very smooth. If I swoon will you catch me?"
        "She laughs and walks closer to you, taking wrapping one of her arms around yours."
        "After a few minutes of walking Alexia slows down and lets go of your arm."
        me "Everything alright?"
        alex "Yeah, I just need you to do me a favour. Pull on the knot for me, would you?"
        "Alexia spins around and presents the back of her swimsuit to you. You pull on the knot, and she proceeds to take the top off entirely."
        show alex strip41 at right
        $ alexO.inc_naked()
        "Next she pulls bottom down and steps out of it. She turns back to you, completely naked."
        alex "There we go. If we're going to be walking around in the sun I don't want to end up with some ugly tan lines. Mind keeping these in your pocket?"
        "Alexia hands over her bikini, then holds onto your arm again. You resume your walk down the beach with Alexia's tits and pussy out in the open."
        "Not long after a group of guys further up the beach notices her and begin whistling and cheering as she passes."
        alex "Oh, I bet they want a piece of me. Just look at them."
        show alex strip42 at right
        "She raises one arm and waves to them, bouncing her tits around a little bit while she's at it."
        me "So that's why you wanted to take all that off, just so people could get a better look."
        alex "Are you complaining? You get the best view in the house."
        "She cups a breast and pinches the hard nipple, rolling it between her thumb and forefinger."
        alex "Ah... God I've gotten myself so wet..."
        show alex strip41 at right
        "Alexia keeps walking, thighs held tightly together. After another ten minutes you've left most of the crowds behind, and she lowers her free hand to her pussy."
        "She runs a finger along her slit a few times, then slips it in. She fingers herself as you walk, holding onto your arm tightly."
        alex "Do you think those guys wanted to fuck me?"
        me "Back there? Oh ya, they would have done it in a heart beat if you asked them."
        "Alexia shivers against you, stumbling half a step as you walk."
        me "They would have bent you over that beer cooler and fucked you raw."
        alex "Oh god..."
        show alex strip43 at right
        "She shivers again, and this time comes to a complete stop. You lean in close and whisper into her ear while she pumps a couple of fingers in and out of her cunt."
        me "Then they would have cum over you and left you there, so the whole world could see what a dirty slut you are."
        alex "Ah!"
        "Alexia shouts out and wraps her free arm around you. Her hips buck a few times as she orgasms."
        "When she's done she slides her fingers out of her pussy and straightens up, taking a few deep breaths to compose herself."
        alex "That was... really intense."
        me "It sure looked like it."
        alex "Come on, lets keep walking for a little bit."
        show alex strip41 at right
        "You walk together until the beach is just a sliver of sand running along the waters edge. With nothing more to see, you turn around and stroll back towards the center of the beach."
        if slut_outfit:
            show alex swim2 at right
        else:
            show alex swim1 at right
        "Alexia gets redressed before you get to the most populated sections, to avoid getting you both in trouble."
        $ alex_beach_walk.inc_level(2)
        $ alexO.change_resist(-alex_beach_walk.use_red(2,alexO.resist_score))


    else:
        #Walk completely naked, gives you a public blowjob.
        alex "It's such a nice day out, we really got lucky."
        me "Yeah, we did. I couldn't think of a better person to spend it with, either."
        alex "Oh, very smooth. If I swoon will you catch me?"
        "She laughs and walks closer to you, taking wrapping one of her arms around yours."
        "After a few minutes of walking Alexia slows down and lets go of your arm."
        me "Everything alright?"
        alex "Yeah, I just need you to do me a favour. Pull on the knot for me, would you?"
        "Alexia spins around and presents the back of her swimsuit to you. You pull on the knot, and she proceeds to take the top off entirely."
        show alex strip41 at right
        "Next she pulls bottom down and steps out of it. She turns back to you, completely naked."
        alex "There we go. If we're going to be walking around in the sun I don't want to end up with some ugly tan lines. Mind keeping these in your pocket?"
        "Alexia hands over her bikini, then holds onto your arm again. You resume your walk down the beach with Alexia's tits and pussy out in the open."
        "Not long after a group of guys further up the beach notices her and begin whistling and cheering as she passes."
        alex "Oh, I bet they want a piece of me. Just look at them."
        if alexO.exhib:
            show alex strip44 at right
            "Alexia stops and turns towards them, cupping her breasts in her hands and playing with her nipples."
            alex "Is this what you want boys? Oh, I know it is!"
            "They cheer louder, thrusting beers into the air in celebration."
            "Alexia turns back to you and runs a finger down your chest. When she reaches the waistband of your swimsuit she hooks it and pulls it down a little."
            alex "I think we should give them a show they won't forget. Any objections?"
            me "I think that's a great idea Alexia."
        else:
            "Alexia stops and turns to you."
            alex "God, this got me so fucking horny. Can I suck you off, please?"
            "She reaches down and cups the bulge in your swimsuit, rubbing it slowly."
            me "I'd love that Alexia."

        "She drops to her knees and pulls your swimsuit down low enough to free your hard cock."
        alex "Oh, that looks nice. Lets have a taste."
        show alex blow24 at right
        $ alexO.inc_blow()
        "Alexia leans in and kisses the tip of your dick, then looks up at you while she slides it into her mouth."
        me "Damn, that feels great Alexia."
        "She starts to blow you, bobbing her head up and down along your cock while she kneels in the sand. Up the beach the cheering gets even louder."
        show alex blow23 at right
        "You rest a hand on the back of Alexia's head and run your fingers though her hair. She speeds up with each pass, her warm throat drawing you quickly towards your orgasm."
        me "Keep it up, you've almost got me there Alexia."
        "She moans and nods, eyes turned up to make eye contact with you."
        $covered = False
        menu:
            "Cum in her mouth.":
                "You grab onto Alexia's hair and pull her back just a little bit, leaving the tip of your cock resting on her lips as you climax."
                me "Shit, here we go!"
                "You hold onto your cock with your other hand and stroke yourself off, pulsing your load into Alexia's mouth. She stares up at you the entire time while she breaths heavily through her nose."
                show alex blow25 at right
                $ alexO.inc_cum_mouth()
                $ alexO.inc_cum_swallow()
                "When you're done you and let her go she opens wide and lets you take a good look at your own cum."
                me "That's a good girl. That felt amazing."
                "She closes and swallows, taking a few seconds to drink down all of your sperm."
                if alexO.cumslut:
                    alex "God, you taste so good [inputName]. Lets make sure I got it all."
                    "She leans forward and starts licking your shaft again, eagerly cleaning off every last drop of semen. After a few seconds she's satisfied and sits back again."
                else:
                    alex "Ah, oh god that was so hot..."


            "Cum on her face.":
                "You grab onto Alexia's hair and pull her back. She leaves your cock with a wet pop, looking up at you while you stroke yourself off with your other hand."
                alex "That's right, cum on me [inputName]! Give it to me!"
                show alex blow26 at right
                $ alexO.inc_cum_over()
                "You grunt softly as you climax, spraying your load over Alexia's face. She holds still until you're finished, then gives the tip of your penis a kiss, licking off the last drip of sperm in the process."
                me "Damn, that felt amazing."
                if alexO.cumslut:
                    alex "Mmm, it's so nice and warm. I fucking love being covered in your cum [inputName]."
                else:
                    alex "Wow, you really covered me... That was so hot..."
                $covered = True

        "You pull up your swimsuit and look around. The group of guys are cheering louder than ever, phones out while they take pictures of you and Alexia. Other small groups of people have noticed as well, and are watching the two of you."
        me "Come on, we should get going before someone comes along and gets us in any trouble."
        alex "Right. Lets go."
        "She gets back onto her feet and takes your hand. You hurry up the beach until you've left the crowds behind."
        if covered:
            show alex strip41 at right
            "Alexia takes a quick trip down to the water, washing your cum off of her face before you keep going."
        "Soon you come to the end of the beach, where the sand is just a narrow strip next to the water."
        alex "I guess that's all there is to see this way. I'm going to get dressed again, and then we can head back and do something else."
        if slut_outfit:
            show alex swim2 at right
        else:
            show alex swim1 at right
        $ alex_beach_walk.inc_level(3)
        $ alexO.change_resist(-alex_beach_walk.use_red(3,alexO.resist_score))

    return


###########################
##Multi Girl Minor Scenes##
###########################

label min_nora_steph_work_undress:
    "Nora and Stephanie have a number of the machines working at once, and the room is going from warm to stifling."
    $temp_slut_score = 0
    if (stephO.slut_score < noraO.slut_score):
        $temp_slut_score = stephO.slut_score
    else:
        $temp_slut_score = noraO.slut_score #ie. Use the lowest score only.

    if temp_slut_score < 10: #Work normally
        steph "Hey Nora, it's getting a little warm in here."
        nora "Whew, you're right. I'll give custodial services a call and see if they can up the AC in here while we're working."
        "Nora makes a quick phone call, and a few minutes later the lab is back at a comfortable temperature. The rest of your shift passes uneventfully while you help out with the lab work."

    elif temp_slut_score < 30: #Work without shirts on
        steph "Whew, it's getting a little warm in here, isn't it Nora."
        "Stephanie pulls at her collar and fans herself with her hand dramatically."
        nora "I suppose it is. There's been an email about cutting down on AC use in the department though, so we'll just have to make do."
        show steph strip3 at right
        "Stephanie nods, then reaches down and pulls her sweater up and off."
        steph "Well in that case, I'm not wearing this all day."
        show nora strip1 at left
        $ noraO.inc_naked()
        $ stephO.inc_naked()
        "Nora hesitates, then starts shrugging off her own lab coat and pulling her shirt off too."
        nora "Good idea, the lab is private and we might as well be comfortable. [inputName], if it gets too warm feel free to take off your shirt as well. We aren't working with anything dangerous today."
        me "Sure thing, thanks Nora."
        "The girls spend the rest of the afternoon without their shirts on, checking on different machines and taking inventory of supplies in their bras."
        $ nora_steph_work_undress.inc_level(0)
        $ noraO.change_resist(-nora_steph_work_undress.use_free_red(0,noraO.resist_score))
        $ stephO.change_resist(-nora_steph_work_undress.use_red(0,stephO.resist_score))
    elif temp_slut_score < 50: #Work in just panties.
        steph "Damn, it's getting hot in here. I'm getting underboob sweat and it's not fun."
        nora "We've been getting pressure to keep AC use down. We'll just have to get used to it. Do whatever you have to to get comfortable."
        show steph strip3 at right
        "Stephanie nods and pulls her shirt off."
        steph "We aren't working with anything corrosive today, right? I'm stripping down until this heat is more reasonable."
        show nora strip1 at left
        "Nora nods and pulls her own labcoat off, followed by her shirt."
        nora "Good idea. [inputName], feel free to take off whatever you need to be comfortable."
        show steph strip7 at right
        show nora strip6 at left
        $ noraO.inc_naked()
        $ stephO.inc_naked()
        "You nod and watch as both Nora and Stephanie take their pants and bra's off."
        steph "Ahh, much better. How's that calibration coming Nora?"
        nora "It's getting there, but there's a little vibration in the plate."
        "The girls spend the rest of the afternoon working in just their panties. You do a little bit of work to help out, but spend most of your time watching their tits bounce and jiggle."
        $ nora_steph_work_undress.inc_level(1)
        $ noraO.change_resist(-nora_steph_work_undress.use_free_red(1,noraO.resist_score))
        $ stephO.change_resist(-nora_steph_work_undress.use_red(1,stephO.resist_score))
    elif (not(stephO.freeuse and noraO.freeuse) or temp_slut_score < 80): #Work naked and get a little handsy with themselves.
        steph "Damn it's getting hot in here. Is there anything we can do about it Nora?"
        nora "We've been told to keep AC use to a minimum. We'll just have to figure some other way to take care of it."
        steph "Well then, I'm losing all of this. We're not working with anything dangerous today, right?"
        show steph strip3 at right
        "Stephanie pulls her sweater up and off, then starts to unzip her pants."
        nora "No, nothing today. That's a good idea, we might as well be as comfortable as we can."
        show steph strip2 at right
        show nora strip5 at left
        $ noraO.inc_naked()
        $ stephO.inc_naked()
        "Nora pulls her labcoat off and starts stripping down as well. Before long they're both bending over and pulling their panties off."
        steph "Ahh, much better. We might finally be able to concentrate now."
        nora "Agreed. Now let's get to that calibration. The plate's been wobbling the last few runs."
        "The girls get to work in the lab, keeping the machines running and checking on the inventory, all while completely naked."
        "As the afternoon wears on you notice both Nora and Steph occasionally running a hand over a breast, or slipping a finger between their legs."
        "You try to do a little bit of work, but the copious amounts of tits, ass, and pussy make it hard to focus."
        $ nora_steph_work_undress.inc_level(2)
        $ noraO.change_resist(-nora_steph_work_undress.use_free_red(2,noraO.resist_score))
        $ stephO.change_resist(-nora_steph_work_undress.use_red(2,stephO.resist_score))
    else: #They have high slut and are both public. Office takes a break while they mastrabate to relax.
        steph "Damn, it's getting hot in here. Is there anything we can do about it Nora?"
        nora "We've been told to keep the AC use to a minimum. We'll just have to strip down and make do."
        show steph strip3 at right
        "Stephanie pulls her sweater up and off, then starts to unzip her pants. Nora starts to do the same."
        show steph strip2 at right
        show nora strip5 at left
        $ noraO.inc_naked()
        $ stephO.inc_naked()
        "Soon both of the girls have pulled off clothes and have them collected in piles."
        steph "That's a little better."
        nora "I suppose. I'm not sure about you guys, but I'm a little horny too."
        steph "Ah, same here. Maybe we need to take a break and take care of that."
        nora "That's a good idea. Lets all take ten minutes, then we'll get back to work."
        show steph mast1 at right
        show nora mast9 at left
        "Nora and Stephanie both sit down in their chairs, spreading their legs wide open."
        steph "[inputName], grab a chair and rub one out. You can come sit next to me, if you want."
        "She smiles and slides a finger along her pussy, playing with her clit a little."
        me "Sounds like fun."
        "You pull down your pants and sit down in a chair next to Stephanie. She takes a good long look at your shaft, while she touches herself."
        "You start to stroke yourself off while Stephanie and Nora finger themselves. The lab is filled with wet sounds and soft moans for a few minutes."
        "Eventually Nora lets out a gasp and arches her back on her chair."
        steph "I'm almost there too. How are you doing [inputName]?"
        me "Getting really close."
        "Stephanie watches while you stroke yourself off, rubbing her clit as quickly as she can. You feel your orgasm approacing quickly."
        nora "Stephanie, get him something so he doesn't make a mess please."
        if stephO.slut_score > 85:
            "Stephanie slides off her chair suddenly, landing on her knees in front of you. She opens up her mouth and leans close to you, her warm breath on your cock making you cum instantly."
            me "Oh fuck!"
            "You keep jerking yourself off and empty your balls into Stephanie's mouth. A shiver runs down her body as the first pulse lands on her tongue, and she moans loudly."
            show steph blow37 at right
            "Once you're completely finished she looks up and blows a few bubbles through the puddle of cum."
            nora "I suppose that works. When you're done showing off Stephaie we've got some work to get back to."
            "Stephanie closes her mouth and swallows loudly."
            $ stephO.inc_cum_swallow()
            steph "Of course, right. Glad I could help you get cleaned up [inputName]."
            "She winks and stands up. The three of you get back to work, completely naked for the rest of the day."
        else:
            "Stepahnie grabs some tissue from her desk and hands it to you, just as you climax. You grunt and fire your load into the tissue balled up around your tip."
            steph "Ah! Oh god!"
            "Stephanie shout out, arching her back while she pumps a couple of fingers in and out of herself. After a brief moment she collapses and takes a deep breath, pulling her wet fingers out of her cunt."
            nora "Excellent. Now how about we get back to work, we need to calibrate the number two plate before we can get anything else done."
            "The three of you get back to work, completely naked for the rest of the day."
        $ nora_steph_work_undress.inc_level(3)
        $ noraO.change_resist(-nora_steph_work_undress.use_free_red(3,noraO.resist_score))
        $ stephO.change_resist(-nora_steph_work_undress.use_red(3,stephO.resist_score))
    return

label min_nora_steph_caught:
    "You key in the door code and unlock the door."
    if temp_slut_score < 65: #Making out
        show noraSteph kiss2
        "Nora is leaning on a table on the far side of the room with Stephanie standing in front of her. They're holding onto each other and making out."
        "The door makes noise at it opens, and Stephanie pulls back in surprise. Nora locks eyes with you and pushes Stephanie away, blushing and straightening out her shirt."
        hide noraSteph
        show nora work at left
        show steph work at right
        nora "[inputName]! You startled us!"
        me "I'm sorry, but you guys didn't answer the door and it was unlocked."
        steph "We were, uh, just working on some stuff."
        nora "Right. And we're all done, so it's time to head out."
        "Stephanie and Nora exchange a look, then grab their stuff and head out."
        nora "Make sure to lock the door this time Stephanie, Okay? [inputName], I hope you didn't see anything you weren't supposed to."
        me "Just two girls hard at work, nothing more."
        nora "Good."
        "The three of you walk up to ground level and say an awkward goodbye."
        $ nora_steph_caught.inc_level(0)
        $ noraO.change_resist(-nora_steph_caught.use_free_red(0,noraO.resist_score))
        $ stephO.change_resist(-nora_steph_caught.use_red(0,stephO.resist_score))

    elif temp_slut_score < 80: #Licking each other
        show noraSteph head1
        $ noraO.inc_naked()
        $ stephO.inc_naked()
        "Nora is sitting on a table at the far end of the room with her legs spread open. She's not wearing any pants, and her panties are pulled to the side. Stephanie is on the floor in front of her, head pressed between her legs."
        "Nora notices you come in and looks up in surprise."
        nora "Oh, [inputName]! I thought we locked the door!"
        "Stephanie lifts her head and turns around too."
        me "It was unlocked. Sorry if I interrupted anything ladies."
        steph "Nora was feeling a little stressed, so I offered to help her out."
        "Nora moves to stand up, but Stephanie plants her arms on her legs and keeps her on the table."
        steph "Don't worry about it Nora. [inputName] won't tell anyone. Right?"
        me "Of course. I just needed to, uh, check for something that I left here."
        "Stephanie smiles and nods, then turns her head back to Nora."
        nora "I'm not so sure about this Steph, maybe we should Ah..."
        "Nora gasps a little as Stephanie flicks her tongue along her clit. Any further protests are abandoned, and she leans back a little on the table and moans softly."
        "You walk slowly around the lab, pretending to look for something while Stephanie eats Nora out in the middle of the lab. The only noise is the soft wet sounds of her mouth against Nora's pussy."
        "After a few minutes Nora's breathing becomes heavier. She grips the edge of the table with one hand, and plants the other on the back of Stephanie's head."
        nora "Oh god. Don't stop."
        "Stephanie shows no intention of slowing down and wraps her arms around Nora's waist. Nora moans loudly, then lets out a shuddering breath."
        "Finally she lets go of Stephanie's head and lays down on the table completely, panting. Stephanie looks up and smiles."
        steph "How was that?"
        nora "So, so good."
        "Stephanie stands up and turns around to look at you."
        steph "Find what you were looking for [inputName]?"
        "She gives you a wink while she wipes off some of Nora's juices from her lips."
        me "Ya, I think I did. I'll be heading out, you two girls have a good night."
        "Stephanie waves goodbye while Nora recovers on the table. You head upstairs, surprised at how much time has passed already."
        $ nora_steph_caught.inc_level(1)
        $ noraO.change_resist(-nora_steph_caught.use_free_red(1,noraO.resist_score))
        $ stephO.change_resist(-nora_steph_caught.use_red(1,stephO.resist_score))

    else: #Scissoring
        show noraSteph fuck6
        "Nora and Stephanie are lying on the floor, right in the middle of the lab. They're both already naked and have their legs wrapped around each other, pussies rubbing in the middle."
        "Stephanie is holding onto Nora's leg and rocking her hips back and forth, causing them both to moan in pleasure."
        "You step inside the lab and close the door. The noise of it clicking shut alerts the girls, who pause and look over."
        nora "On, [inputName]. I thought I locked the door."
        "Stephanie just smiles and starts grinding against Nora again."
        me "It was unlocked. I hope I'm not interrupting."
        nora "No, no. We were, just, ah... relieving some stress, ah..."
        "Stephanie holds onto Nora's leg tight to pull her close."
        me "Okay then, don't let me stop you."
        steph "You sure you don't want to play around a little? I'm sure you aren't that busy."
        "She turns her head towards you and opens her mouth, sticking her tongue out."
        me "Well, if you're offering..."
        show noraSteph fuck7
        $ stephO.inc_blow()
        "She nods, and you slip your pants off and step up next to her. Stephanie leans towards you a little and licks the your shaft from base to tip, then slips it into her mouth and starts to blow you."
        "Nora lays on the ground, moaning and playing with her own breasts while she watches you."
        "Stephanie blows you in time with her own thrusts against Nora, slowly speeding up. Her tongue flicks against your tip at the top of each movement, then slides against the bottom as you fit yourself into her throat."
        "After a few minutes of service you're feeling ready to finish."
        menu:
            "Cum in Stephanie's mouth.":
                me "I'm almost there Stephanie. Are you ready?"
                "Stephanie rubs against Nora harder, causing her to moan and twitch. She looks up at you and keeps blowing you, nodding slightly."
                "A few seconds later you tense up and she pulls your tip back to rest on her tongue, still held inside her warm mouth. You rub yourself while you release your load over her tongue."
                "Stephanie pulls off and turns her attention back to Nora. They're both covered in sweat and grinding hard against each other. Stephanie grips Nora's leg tighter and leans into her."
                "Nora gasps and moans, squeezing her own breast tightly. You can see her legs start to spasm, and she lets out a loud suddering moan."
                "Stephanie starts to shake too and rubs herself against Nora as quickly as she can. She's still got her mouth closed, holding your cum inside."
                "Stephanie pauses and quivers while Nora finishes her own orgasm. After a few seconds Stephanie helps Nora sit up a little bit and leans over her."
                nora "Oh god that was amazing."
                "Stephanie tilts Nora's head up and uses a finger to gently pull her mouth open. Nora looks confused for a moment, but does as she's asked."
                show noraSteph fuck9
                $ stephO.inc_cum_mouth()
                $ noraO.inc_cum_swallow()
                $ stephO.inc_cum_swallow()
                "Stephanie opens her mouth, letting your cum drip in a long fat line into Nora's mouth. Nora closes her eyes, but keeps her mouth open until all of your cum has been given to her."
                "Finally Stephanie takes a big deep breath, followed by a few heavy pants."
                steph "I thought I should share. Here, give me some back."
                "She leans in and kisses Nora, holding her by the back of the head. The two girls embrace for a few moments while you watch, then they separate and look up at you."
                show noraSteph fuck10
                "Stephanie opens up her mouth and looks at Nora to remind her to do the same. Their mouths are both filled with a mixture of each other's spit and your cum."
                "After a long while Stephanie closes and swallows, then watches Nora do the same."
                steph "Wow. That was intense."
                "Nora just nods and tries to catch her breath."
                me "Well thank you both, I'll be sure to visit you guys next time I need to relax."
                "Stephanie smiles."
                steph "Be sure you do."

            "Cum over Nora.":
                me "I'm almost there Steph. I think Nora deserves some of this."
                "Stephanie rubs against Nora harder, causing her to moan and twitch. She looks up at you and keeps blowing, nodding slightly."
                "A few seconds later you start to tense up and pull out of Stephanie's mouth with a wet pop. You stroke your shaft and point it towards Nora, who is spread out on the ground below you."
                "Nora looks up at you and watches as you fire your load over her whole body. Stephanie moans loudly as you cum beside her, begining to twitch from her own orgasm."
                show noraSteph fuck8
                $ noraO.inc_cum_over()
                $ stephO.inc_cum_swallow()
                "A short moment later you're done, and Nora is covered with drops of your cum from head to toe. Her mouth was open as she panted, and you're sure some of it landed inside too."
                nora "Oh god, here I come!"
                "Nora lets out a long shuddering gasp while Stephanie grinds against her. When she's done she goes limp, and Stephanie lets her fall completely on her back."
                "Then Stephanie crawls over her, running her tongue up from her pussy all the way to her neck, licking your cum off of Nora."
                "Nora just lays still and pants heavily while Stephanie cleans her body off."
                "When she's done Stephanie sits down and smiles up at you."
                steph "Good job [inputName]. That was hot."
                me "Any time. I'll be sure to visit you guys next time I need to relax."
                steph "Be sure you do."
        "You pull your pants up and leave the lab while Nora and Stephanie start to get dressed. You're surprised at how much time has passed when you get to ground level."
        $ nora_steph_caught.inc_level(2)
        $ noraO.change_resist(-nora_steph_caught.use_free_red(2,noraO.resist_score))
        $ stephO.change_resist(-nora_steph_caught.use_red(2,stephO.resist_score))
    return

label min_mom_lily_movie:
    $ lowest_score = 0
    if (momO.slut_score < sisO.slut_score):
        $ lowest_score = momO.slut_score
    else:
        $ lowest_score = sisO.slut_score

    if lowest_score < 30: #Nothing
        show sis casual1 at right
        show mom casual at left
        "You return with the glasses of wine balanced carefully. The movie is put back on, and you all enjoy the evening relaxing with family."
        "As midnight rolls around the movie ends, and the three of you retire to your beds."
    elif lowest_score < 60: #Skimpy outfits, mature movie
        show mom nightstrip2 at left
        show sis strip1 at right
        "You come back with the glasses of wine carefully balanced. Lily has just finished pulling her dress off and chucks it into the corner of the room, while Mom is sitting down on the couch in just her panties."
        sis "Hey. We were just getting comfortable. Ready to start?"
        $ momO.inc_naked()
        $ sisO.inc_naked()
        me "Uh, ya. Sure."
        "You hand out the drinks and sit down on the couch between the girls."
        mom "Me and Lily were talking. Do you mind if we changed the movie to something more exciting? This is kind of.."
        sis "Terrible, this movie is terrible."
        me "No problem there. Put on whatever you would like."
        "Mom and Lily talk with each other while they scroll through your list of movies. Finally they agree on one titled \"Rock Hard: Precinct 131\", which looks like some sort of action movie."
        "The movie follows the story of Rock Hard, loose cannon cop who doesn't play by the rules."
        "The girls gasp and turn away during the gunfights, but neither bat an eye when Rock takes a girl back to his squad car and shows her that his name isn't just for show."
        "As midnight rolls around the movie ends, Rock Hard victorious over the criminals and loved by all. Lily and Mom get their clothes back on, then head upstairs."
        $ mom_lily_movie.inc_level(0)
        $ momO.change_resist(-mom_lily_movie.use_free_red(0,momO.resist_score))
        $ sisO.change_resist(-mom_lily_movie.use_red(0,sisO.resist_score))
    elif lowest_score < 90: #Handjob while they masturbate
        show mom nightstrip2 at left
        show sis strip1 at right
        "You come back with the glasses of wine carefully balanced. Lily has just finished pulling her dress off and chucks it into the corner of the room, while mom is sitting down on the couch in just her panties."
        sis "Hey. Ready to start?"
        mom "We were talking, what do you think about a different movie?"
        sis "This one is kind of boring, to be honest."
        "You distribute the drinks and sit down between the girls."
        me "Sure, whatever you two want."
        sis "And come on, there's no way you're comfortable wearing all that. It's the weekend, releax a little!"
        "Lily pulls at your shirt while Mom brings up the movie list and starts scrolling through it."
        me "Fine, fine. Here."
        "You pull your shirt off, then stand up and drop your pants too. Your hard cock presses against your underwear, and you see Lily notice it."
        me "Happy?"
        sis "Very."
        mom "What do you guys want to watch?"
        sis "Ooh, what about that? \"Rock Hard\". I think we saw the first one already."
        "You sit back down while Mom starts the movie."
        "The movie seems to follow a police officer, Rock Hard, through his daily life. Your memory is a little foggy about the original, but you're certain it had a higher production budget than this."
        "It's only when Rock arrests a girl and she pouts at him and asks \"Isn't there anything I could do to get out of this, officer?\" that you reaize this isn't the sequel to the cop movie you watched before."
        "Lily gasps a little when Rock pulls his cock out of his pants and flops it over the girls face."
        mom "Well! That took a sudden turn!"
        sis "Are they allowed to show that?"
        mom "It did say rated R..."
        "The girl in the back of the squad car opens her mouth wide and slips Rock's cock inside. She looks up at the camera with big eyes as she slides it back and forth."
        "You think about saying something, but decide to just watch how this plays out."
        "After a few minutes of deepthroating the girl, Rock turns her around and bends her over in the back of the car. Lily and Mom are both watching, eyes fixed on the screen while they pant softly."
        "Lily's hand slides in between her legs, a single finger rubbing up and down her slit."
        "You reach a hand over and rub Lily's leg, causing her to sigh a little. When your hand slides up her inner thigh she spreads her legs a little and pulls her own hand back."
        "Mom glances over and watches as you start to rub Lily's pussy through her panties."
        mom "Lily, don't be selfish."
        hide mom
        hide sis
        show momSis hand2
        $ momO.inc_naked()
        $ sisO.inc_hand()
        "Lily nods and reaches over to your waist to pull your underwear down. With that out of the way she takes a hold of your cock and starts to jerk you off. You pull her panties out of the way and slip a finger inside of her."
        sis "Of course. Sorry mom."
        "Mom leans back on the couch and sighs, her own hand rubbing her inner thighs. Rock Hard pulls out of the girl and puts her on her knees to suck off his cock some more."
        "Lily pants softly beside you, and mom pulls her panties down and off. After a few minutes Rock is back inside the girl, this time spread on the front of the squad car, and mom is fingering herself."
        "For a few more minutes the three of you sit in silence, broken only by soft panting and the occasional gasp of pleasure from Lily. Finally you're feeling ready to finish."
        me "Keep going Lily, you're doing great."
        "Lily nods and speeds up her handjob. Your cock is wet and slippery from your own precum."
        "Rock pulls out of the girl for the last time, putting her on her knees and spraying his cum over her face. She opens her mouth, letting his load drip over her lips and inside her mouth."
        "The scene triggers your own orgasm, and you start to finish. Lily holds on tight, rubbing gently, until you've finished firing your cum onto the floor in front of you. The last bit drips down on Lily's hand."
        "Mom takes a few shuttering breaths beside you, then seems to relax too."
        "For a few minutes you all just sit and catch your breath, watching the credits roll on a movie you now notice is called \"Rock Hard: Precinct 69\"."
        mom "I'll get this cleaned up. You two should get to bed."
        me "Sure mom. Thanks."
        "Lily stays on the couch for a while longer after you head upstairs, still breathing heavily."
        $ mom_lily_movie.inc_level(1)
        $ momO.change_resist(-mom_lily_movie.use_free_red(1,momO.resist_score))
        $ sisO.change_resist(-mom_lily_movie.use_red(1,sisO.resist_score))

    else: #Sex with them while you watch the movie.
        show sis strip2 at right
        show mom nightstrip3 at left
        sis "Hey [inputName], we were getting a little bored of the movie. Mind if we change it?"
        "Mom and Lily have both stripped down while you were getting the drinks. You pass out the glasses of wine, then sit down in the middle of the couch."
        me "Sure, put on whatever you two want."
        mom "We'll make sure it's something you'll enjoy."
        sis "Now come on, we can't be here naked with you all bundled up like that. Relax, we're at home!"
        "Lily pulls at your shirt, encouraging you to take it off. You stand up and take off not only your shirt, but your pants and underwear too. Lily smiles when your hard cock comes out."
        sis "There we go. Feeling better now?"
        me "Ya. I think so."
        "You sit back down and watch while Mom scrolls through the different movies. She's gone straight to the adult film section and picks a parody porn film called \"Rock Hard: Deep Undercover\"."
        sis "Ooh, that looks good. I think I've seen the first one."
        "The three of you sit back on the couch, completely naked, while the movie goes through the motions of introducing a plot. It doesn't take long before the main character, Rock Hard, is fucking a biker chick to earn her trust."
        "Lily moans softly while she watches another girl get railed, and rubs her pussy a little bit. Mom keeps her composure, but you can tell she's enjoying it."
        me "You know girls, I'm feeling a little left out here..."
        "Mom looks over and stares at your erect penis."
        mom "Oh, I'm sorry dear. How about we help you take care of that. Okay Lily?"
        "Lily nods, her attention still on the girl getting railed in the movie."
        hide mom
        hide sis
        show momSis fuck10
        $ momO.inc_blow()
        $ sisO.inc_sex()
        "Mom gets down on her knees in front of you, taking your cock into her hand and rubbing it gently. After a few moments, she licks you from base to tip, then slides you into her mouth and starts blowing you."
        me "Wow, that feels great."
        "Mom nods a little and keeps going, while Lily fingers herself beside you."
        me "Come on Lily. You're going to have to pull your weight around here!"
        show momSis fuck11
        "You reach over and grab her by the waist, pulling her around and on top of you. Mom lets go of your cock and watches as you get Lily positioned above your lap, kneeling on the couch with her legs spread around you."
        me "Ready?"
        "Lily looks down at your cock, already rubbing against her lips. She moans and nods."
        sis "I'm all ready."
        "You hold onto her waist as she lowers herself onto you. her pussy is already dripping wet, and you have no trouble sliding all the way in on the first stroke."
        mom "That's a good girl Lily. You're doing great."
        "Lily grinds on your cock a little, trembles for a moment, then pulls up and settles into a steady rhythm."
        "You watch the movie over her shoulder while she rides on your cock."
        "Mom watches from the floor, rubbing herself while she watches you fuck her daughter."
        "After a few minutes of fucking your sisters tight, wet pussy you're ready to finish."
        menu:
            "Cum inside.":
                me "I'm almost there Lily. Think you can handle taking my load like a good little slut?"
                if sisO.preg_response_ok():
                    "Lily whimpers and nods, riding up and down on your cock."
                else:
                    sis "Wait... what if you get me..."
                    me "It's fine, don't worry about that right now!"
                "You pull hard on her hips when you're ready, pushing her down while you fire your load inside her. Lily gasps and leans forward, wrapping her arms around your head."
                show momSis fuck13
                $ sisO.inc_cum_inside()
                "She rocks her hips up and down a little until you're completely finished, then pulls up just enough to let you slip out and collapses sideways onto the couch."
                mom "Wow, good job, both of you!"
                me "Thanks Mom. You did a great job taking that load sis."
                "Lily nods and smiles at you two while your cum leaks out of her pussy."
                if momO.preg_response_ok():
                    mom "Now, you two should both be getting to bed. Lily, try not to get anything on the couch please."
                    "Lily sits up carefully and cups a hand between her legs."
                    sis "Sorry Mom."
                else:
                    mom "Lily, you remember that talk we had about protection, right?"
                    "Lily sits up carefully and cups a hand between her legs, catching your semen before it can drip onto the couch."
                    sis "Of course Mom, I'm being careful."
                    mom "I know, I just worry sometimes. Anyways, it's getting late. You should go get yourselves cleaned up."
                "The three of you say goodnight and head upstairs."
            "Pull out.":
                me "Almost there, keep going!"
                "You give Lily a few more good strokes, then pull up on her ass to slip your cock out. She gasps loudly when you pull out, leaning onto your shoulder and twitching while she has her own orgasm."
                show momSis fuck12
                $ momO.inc_cum_over()
                "You grab your cock and stroke yourself as you cum, blowing your load over your mom's face and tits while she sits on the ground rubbing herself."
                "Mom looks up at you and smiles as you drip the last of your sperm onto her nipples."
                mom "How was that sweetheart? Feeling good?"
                me "Oh ya. You both were amazing."
                mom "Well, I better get all of this cleaned up, and you two should be heading to bed."
                me "Right. Goodnight then you two."
                "You head upstairs, leaving Lily collapsed on the couch and Mom wiping your cum off her tits."
        $ mom_lily_movie.inc_level(2)
        $ momO.change_resist(-mom_lily_movie.use_free_red(2,momO.resist_score))
        $ sisO.change_resist(-mom_lily_movie.use_red(2,sisO.resist_score))
    return
