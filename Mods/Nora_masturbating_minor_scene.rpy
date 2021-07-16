label min_nora_masturbating:
    show nora mast6 at right
    "As you step into the lab, the faint sound of feminine moans stops you. Peaking around the corner, you see Nora in her underwear, touching herself."
    "At first, it looks like she spots you, but when she doesn't respond, you realize her eyes are glazed over as she touches herself."
    nora "Oh god, [inputName]... that's it."
    "She said your name while she is masturbating!"
    if noraO.slut_score < 70: #Just watch.
        "Nora is really going at it. She appears to be almost done."
        nora "Yes... Yes!"
        "Her body quakes as she cums. You touch yourself a little bit at the sight, but there's no time to do anything but watch the finale."
        "When she finishes, she grabs a paper towel from a nearby desk and wipes her hands off. She quickly dresses then walks out of the room, leaving you alone in the lab."
        "You wonder if she sometimes comes in early to the lab to masturbate?"
        $ nora_masturbating.inc_level(0)
        $ noraO.change_resist(-nora_masturbating.use_red(0,noraO.resist_score))
        jump labAlone

    else: #You can interrupt or just watch..
        "Nora is really going at it, her moaning is getting more intense."
        nora "Yes [inputName], oh fuck me you naughty lab boy!"
        "You wonder if you should make your presence known and do what she is fantasizing about."
        menu:
            "Just Watch":
                "You decide for now to just enjoy the show."
                if noraO.cumslut:
                    nora "Oh god yes! Cum inside me! I'm cumming too!"
                    "Her fantasy clearly involves getting creampied."
                else:
                    nora "That's it [inputName]. I'm cumming!"
                    "Nora's fantasy version of her is making her cum."
                "Her body quakes as she cums. You touch yourself a little bit at the sight, but there's no time to do anything but watch the finale."
                "When she finishes, she grabs a paper towel from a nearby desk and wipes her hands off. She quickly dresses then walks out of the room, leaving you alone in the lab."
                $ nora_masturbating.inc_level(1)
                $ noraO.change_resist(-nora_masturbating.use_red(1,noraO.resist_score))
                jump labAlone
            "Fuck Her":
                me "If you insist."
                show nora mast7 at right
                "Nora stops, her panties pulled to the side mide session when she hears you."
                nora "[inputName]? I didn't hear you..."
                me "That's okay. Get naked and turn around, I'll finish you off."
                "Nora hesitates for a moment, then slides off her bra and panties and does as you instruct."
                show nora fuck31 at right
                "You quickly pull out your cock and step behind Nora as she presents her ass to you. Her cunt is soaked from her previous masturbation."
                nora "You aren't going to keep me waiting, are you?"
                "She wiggles her ass at you."
                me "Of course not!"
                "You grab her hip with your left hand while you guide your erection with your right."
                "Nora gasps when she feels your cock slide inside of her."
                $ noraO.inc_sex()
                $ noraO.inc_naked()
                "She moans into the desk as you begin to fuck her hard and fast. No reason to try and prolong it, she is going to cum fast."
                me "Is this what you were imagining, you fucking slut?"
                nora "Yes! Oh fuck yes give it to me!"
                "You shove it in deep then push forward, pinning her to the desk. You roll your hips a bit to stir her pussy with your cock."
                "You can feel her pussy start to twitch as she begins to orgasm."
                nora "I'm cumming! Oh [inputName] I'm cumming!"
                "You can feel your orgasm building as you fuck Nora from behind. You're almost there."
                menu:
                    "Cum inside.":
                        me "Here I come Nora!"
                        if noraO.cumslut:
                            nora "Yes, please give it to me! Fill me up and get me pregnant!"
                        else:
                            nora "Give it to me. Fill me up!"
                        "You pump one last time into her sweet pussy, then hold yourself deep as you release. Your thighs spasm, and you feel Nora tense up against you as you cum into her."
                        show nora fuc33 at right
                        $ noraO.inc_cum_inside()
                        "The two of you stay coupled for a moment, panting and covered in sweat."
                        me "Okay, you should go get cleaned up."
                        "Nora nods slowly, face resting sideways on the bench as she pants loudly."
                        "You pull out. She pulls her panties back in place to catch any drips."
                        "Nora stands slowly on shaking legs as you pull your own pants up."
                    "Cum on her ass.":
                        "Without a word you pump faster and faster, then pull out at the last moment and plant the tip of your cock against Nora's left ass cheek."
                        me "Ugh!"
                        if noraO.cumslut:
                            nora "Oh yes! That's right, cover me with your load!"
                        "You pump a stream onto her left cheek, then shift to the right and stroke yourself a few times as you tense and shoot more onto her."
                        show nora fuck34 at right
                        $ noraO.inc_cum_over()
                        "Nora stays slumped on the desk breathing heavily."
                        me "Ya. Wow."
                        me "You should get cleaned up quickly before anyone comes."
                        nora "Right. Ya."
                        "Nora stands up carefully on shaky legs and pulls up her panties to wipe away your cum."
                $ nora_masturbating.inc_level(1)
                $ noraO.change_resist(-nora_masturbating.use_red(1,noraO.resist_score))
                "You decide to leave the lab to allow Nora time to clean up."
                jump campusAfternoon
            "Reveal Yourself" if noraO.exhib:
                "You step around the corner, Nora looks up and notices you immediately."
                show nora mast7 at right
                "She stops masturbating for a second, surprised by the sudden intrusion. However, when she realizes it is you, she keeps going."
                "Nora bites her lip as she maintains eye contact with you. Her fingers start working faster, clearly enjoying that you are watching her."
                "Gasps turn to whimpers, which turn to moans. Nora is REALLY getting off on having you watch her!"
                show nora mast8 at right
                "Her moans get desperate. You watch as her body tenses up and she clearly begins to orgasm. Nora finally get the release she is lookign for, looking right into your eyes."
                "When she finishes, she grabs a paper towel from a nearby desk and wipes her hands off. She quickly dresses then walks out of the room, leaving you alone in the lab."
                $ nora_masturbating.inc_level(1)
                $ noraO.change_resist(-nora_masturbating.use_red(1,noraO.resist_score))
                jump labAlone

    return
