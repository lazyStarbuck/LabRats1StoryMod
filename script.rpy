#Hello! And welcome to the script for Lab Rats!
#I"m glad you've taken the time to delve a little deeper into the game! I welcome you to make whatever changes you'd like to the script below.
#Add scenes, take away ones you don't like, change random chances, or increase your influence with all the girls!
#
#There are only three things I ask of you if you want to share your work around:
#1) You don't ever sell your creation. This includes timed Patreon releases. Please pay it forward and keep everything free!
#2) You keep the patron link on the main page in place, or substitute it with something similar.
#3) If you make something cool, let me know! I always want to see what awesome stuff is being made by the community!
#Now that's enough talk from me, go forth and enjoy!

#Tokens taken with area select, use select, threshold 15, AA on, select transparant, Feathered edges 16

init python:
    ##GAME OBJECTS##
    class Girl(renpy.store.object):
        def __init__(self,name,slut_score = 0, resist_score = 0, temp_resist_modifier = 1):
            self.name = name
            self.effect_string = "crazy"
            self.slut_score = slut_score
            self.resist_score = resist_score
            self.temp_resist_modifier = temp_resist_modifier
            self.difficulty_shift = 0

            self.temp_cumslut_red = 0
            self.temp_anal_red = 0
            self.temp_freeuse_red = 0
            self.temp_exhib_red = 0

            self.naked_count = 0
            self.hand_count = 0
            self.tit_count = 0
            self.blow_count = 0
            self.sex_count = 0

            self.bc = True # The girl is on birth control. Creampies have little impact on her preg_score.
            self.preg_score = 0 #If this is 100 by the end of the game, the girl got pregnant.

            self.cum_inside_count = 0
            self.cum_inside_ass_count = 0
            self.cum_over_count = 0
            self.cum_mouth_count = 0
            self.cum_swallow_count = 0

            self.beach_count = 0

            self.report_number = 0 #Report 0 is no report, all other numbers must code to an entry when you talk to them.

            self.training_threshold = 45 #The point at which you can start to train a girl.
            self.training_increase = 15 #The increase to the training_threshold each time you train a girl.

            #Tags. These always start as false and must be trained.
            self.cumslut = False #The cumslut tag is used for events where cum is involved. This is almost all of them, towards the end.
            self.anal = False #The anal tag is used for scenes that involve, you guessed it, anal. Unlocks some options, or has the girl choose anal herself rather than vaginal sex.
            self.freeuse = False #The free use tag is used for events where the girl is having sex with other people in some way.
            self.exhib = False #The exhibitionist tag is used for events where the girl is having sex with the main character in a public space.

        def set_tag_cumslut(self):
            self.cumslut = True
            self.training_threshold += self.training_increase

        def set_action_cumslut(self):
            if self.cumslut:
                self.temp_cumslut_red = 15

        def set_action_anal(self):
            if self.anal:
                self.temp_anal_red = 15

        def set_action_freeuse(self):
            if self.freeuse:
                self.temp_freeuse_red = 15

        def set_action_exhib(self):
            if self.exhib:
                self.temp_exhib_red = 15

        def set_tag_anal(self):
            self.anal = True
            self.training_threshold += self.training_increase

        def set_tag_freeuse(self):
            self.freeuse = True
            self.training_threshold += self.training_increase

        def set_tag_exhib(self):
            self.exhib = True
            self.training_threshold += self.training_increase

        def slut_delta(self, difficulty):
            delta = self.slut_score-difficulty
            if delta < 0:
                self.effect_string = "major"
                return high_influence_raise
            elif delta < 15:
                self.effect_string = "big"
                return mid_influence_raise
            else:
                self.effect_string = "meaningful"
                return low_influence_raise

        def check_willing(self, difficulty):
            difficulty -= self.temp_cumslut_red
            difficulty -= self.temp_anal_red
            difficulty -= self.temp_freeuse_red
            difficulty -= self.temp_exhib_red
            delta = self.slut_delta(difficulty)
            # return False
            if delta == low_influence_raise:
                return True
            elif delta == mid_influence_raise and self.difficulty_shift < 1:
                return True
            elif delta == high_influence_raise and self.difficulty_shift < 0:
                return True
            return False

        def change_slut_rebalanced(self, difficulty):
            difficulty -= self.temp_cumslut_red
            difficulty -= self.temp_anal_red
            difficulty -= self.temp_freeuse_red
            difficulty -= self.temp_exhib_red
            delta = self.slut_delta(difficulty)
            self.change_slut(delta)

        def change_slut(self, amount):
            self.temp_cumslut_red = 0
            self.temp_anal_red = 0
            self.temp_freeuse_red = 0
            self.temp_exhib_red = 0
            self.slut_score += (amount * 0.01 * (100-self.resist_score)) ##ie. modify the amount gained inversly proportional to reluctance.
            if self.slut_score < 0:
                self.slut_score = 0

        def change_slut_failed(self):
            self.change_slut(min_influence_raise)

        def change_slut_no_resist(self, amount): #Reduces slut score by set amount, ignoring resistance. Used when training tags and influence is reduced.
            self.slut_score += amount
            if self.slut_score < 0:
                self.slut_score = 0

        def get_slut_description(self):
            description = "This is a bug, please let me (Vren) know on Patreon."
            if self.slut_score <= 15:
                description = "Barely affected."
            elif self.slut_score <= 30:
                description = "Unusually horny."
            elif self.slut_score <= 45:
                description = "Perceptibly lewd."
            elif self.slut_score <= 60:
                description = "A very dirty girl."
            elif self.slut_score <= 75:
                description = "A good little slut."
            elif self.slut_score <= 100:
                description = "Completely whorish."
            else:
                description = "A mindless fuck toy."
            return description

        def daily_change_resist(self):
            x = 1
            x += self.resist_score//25
            self.change_resist_quietly(-x)

        def change_resist_quietly(self, amount):
            real_amount = amount*self.temp_resist_modifier
            self.resist_score += real_amount
            self.temp_resist_modifier = 1
            if self.resist_score < 0:
                self.resist_score = 0
            if self.resist_score > 100: ##ie. max resist is 100. Let it rise above 100 to allow for negative influence gain with many repeated events.
                self.resist_score = 100

        def change_resist(self, amount):
            real_amount = amount*self.temp_resist_modifier
            self.resist_score += real_amount
            self.temp_resist_modifier = 1

            if real_amount < -1:
                the_string = self.name
                the_string += "'s resistance score dropped by "
                the_string += str(abs(real_amount))
                the_string += " due to this event."
                renpy.say("",the_string)

            if self.resist_score < 0:
                self.resist_score = 0
            if self.resist_score > 100: ##ie. max resist is 100. Let it rise above 100 to allow for negative influence gain with many repeated events.
                self.resist_score = 100

        def get_resist_description(self):
            description = "This is a bug, please let me (Vren) know on Patreon."
            if self.resist_score <= 15:
                description = "No resistance."
            elif self.resist_score <= 40:
                description = "Slightly resistance."
            elif self.resist_score <= 60:
                description = "Moderate resistance."
            elif self.resist_score <= 80:
                description = "Major resistance."
            else:
                description = "Almost complete resistance."
            return description

        def get_serum_result(self, type): #could use more testing to make sure temp_resist_modifier is working properly
            if type == "blue": ##Normal.
                self.difficulty_shift = 0
                return self.slut_score
            elif type == "purple": ##Lowers Resistance Hit, but lowers slut for this event.
                self.temp_resist_modifier = 0.25
                self.difficulty_shift = 1
                return self.slut_score - purple_serum_debuff
            else: ##type == "red"
                self.temp_resist_modifier = 1.75
                self.difficulty_shift = -1
                return self.slut_score + red_serum_buff ##Raises slut for this event, but has a larger resistance hit.

        def preg_response_ok(self):
            if self.bc:
                return True
            elif self.slut_score > 125 or (self.slut_score > 90 and self.cumslut):
                return True
            else:
                return False

        def is_pregnant(self): #Returns true if the girl is pregnant at this point, false otherwise.
            if self.preg_score >= 100:
                return True
            else:
                return False

        def inc_naked(self):
            self.naked_count += 1

        def inc_hand(self):
            self.hand_count += 1

        def inc_tit(self):
            self.tit_count += 1

        def inc_blow(self):
            self.blow_count += 1

        def inc_sex(self):
            self.sex_count += 1

        def inc_cum_inside(self): #Note, is now only for vaginal creampies, not anal.
            self.cum_inside_count += 1
            if not self.bc:
                self.preg_score += 7
            else:
                self.preg_score += 1

        def inc_cum_inside_ass(self):
            self.cum_inside_ass_count += 1

        def inc_cum_over(self):
            self.cum_over_count += 1

        def inc_cum_mouth(self):
            self.cum_mouth_count += 1

        def inc_cum_swallow(self):
            self.cum_swallow_count += 1

        def inc_cum_repeat(self, count): #Used for the end of game skipping code to add multiple creampies at once
            self.sex_count += count
            self.cum_inside_count += count

    class Major_Scene(renpy.store.object):

        def __init__(self,name,levels,inc_amount): ##level is the level of the interaction. 0 is all the failure states, 1 is the auto-success, 2 is strip, ect.
            self.name = name
            self.levels = levels
            self.levelArray = [0]*levels
            self.happened = False
            self.count = 0
            self.inc_amount = inc_amount

        def get_resist_change(self, level):
            return (self.get_level_count())*self.inc_amount ##ie. the resist factor is 10. Level should no longer be needed.

        def inc_level(self,level):
            self.levelArray[level] += 1 ##should record how often each choice was taken. Might be bugged, and isn't used anyways.
            self.count += 1

        def get_level_count(self):
            return self.count
            #value = 0
            #for counter in self.levelArray:
            #    value += self.levelArray[counter]
            #return value

    class Minor_Scene(renpy.store.object):
        def __init__(self,name,levels,reduction_available):
            self.name = name
            self.levels = levels
            self.levelArray = [0]*levels
            self.redArray = [reduction_available]*levels
            self.baseRed = reduction_available

        def inc_level(self,level):
            self.levelArray[level] += 1

        def use_red(self,level,amount_needed): #Use Reduction.
            max_red = self.redArray[level]//2 ##ie. use integer division.
            if max_red >= amount_needed:
                self.redArray[level] += -(amount_needed//2)
                return amount_needed
            else:
                self.redArray[level] += -(max_red//2)
                return max_red

        def use_free_red(self,level,amount_needed): #For use with threesome scenes, gets the red count without changing it for the next person (ie. use for the first person, then use use_red() for the second. Refactor this soon.
            max_red = self.redArray[level]//2 ##ie. use integer division.
            if max_red < self.baseRed/4:
                max_red = self.baseRed/4
            if max_red >= amount_needed:
                return amount_needed
            else:
                return max_red

    class Growth_Event(renpy.store.object):
        def __init__(self, min, max, start, inc, growth, growthLimit):
            self.min = min
            self.max = max
            self.current = start
            self.inc = inc
            self.growth = growth
            self.growthLimit = min + growthLimit
            if self.growthLimit > 100:
                self.growthLimit = 100

        def check_event(self):
            if renpy.random.randint(0,100) < self.current:
                #success, return true and reset the chance
                self.current = self.min
                self.min += self.growth
                if self.min > self.growthLimit:
                    self.min = self.growthLimit
                else:
                    self.max += self.growth
                    if self.max > 100:
                        self.max = 100
                return True
            else:
                #failure, return false and increment the chance up
                self.inc_chance()
                return False

        def inc_chance(self):
            self.current += self.inc
            if self.current > self.max:
                self.current = self.max
            if self.current < self.min:
                self.current = self.min

    class Random_Event(renpy.store.object):
        def __init__(self,min,max,start,inc):
            self.min = min
            self.max = max
            self.current = start
            self.inc = inc

        def check_event(self):
            #renpy.block_rollback()
            if renpy.random.randint(0,100) < self.current:
                #success, return true and reset the chance
                self.current = self.min
                return True
            else:
                #failure, return false and increment the chance up
                self.inc_chance()
                return False

        def inc_chance(self):
            self.current += self.inc
            if self.current > self.max:
                self.current = self.max
            if self.current < self.min:
                self.current = self.min



label serum_give(girl):
    $return_score = 0
    menu:
        "Give [girl.name] some blue serum." if player_blue_serum > 0:
            $player_blue_serum += -1
            $return_score = girl.get_serum_result("blue")
        "Give [girl.name] some purple serum.\n-75\% Resistance Gain, Weak effect (only actions she's already comfortable with)." if player_purple_serum > 0:
            $player_purple_serum += -1
            $return_score = girl.get_serum_result("purple")
        "Give [girl.name] some red serum.\n+75\% Resistance Gain, Strong effect (she'll do anything)." if player_red_serum > 0:
            $player_red_serum += -1
            $return_score = girl.get_serum_result("red")
    return return_score

label resistance_gain_report(the_scene, the_girl, the_second_girl = None):
    $ resist_change = the_scene.get_resist_change(0)
    $ number_of_times = the_scene.get_level_count()
    if number_of_times == 0:
        "You've never been in this situation before, so there will be no increase in resistance."
    elif number_of_times == 1:
        "You've been in this situation once before, and expect an increase of [resist_change] to their resistance after."
    else:
        "You've been in this situation [number_of_times] times before, and expect an increase of [resist_change] to their resistance after."

    if the_girl.resist_score > 60 and resist_tutorial:
        python:
            high_girl = the_girl
            if (the_second_girl is not None):
                if the_second_girl.resist_score > the_girl.resist_score:
                    high_girl = the_second_girl
            resist_fraction = 100 - high_girl.resist_score
        "[high_girl.name]'s resistance score is high, and you are unlikely to make much progress with her until it has been reduced. Influence gain is currently reduced to [resist_fraction]\% of it's normal value."

        menu:
            "Learn about resistance and how it can be lowered.":
                "Each girl has two important statistics associated with them. Influence represents your current amount of control over them. The higher their influence score, the less inhibited they will be."
                "Influence is increased through the use of serum to make a girl more malleable and a sexual act to solidify the change you wish to make."
                "If you dose a girl in the same situation more than once they will begin to notice something strange going on though, and their resistance score will rise. The higher their resistance score, the less influence they gain from each action."
                "Resistance is lowered by giving the girl time to become use to their new temperament. This is speeded along greatly if they are given a chance to take action in a way they wouldn't before, like stripping down or giving sexual favours."
                "One action will only lower a girls resistance by a certain amount before she becomes completely use to it and no longer gains a benefit from it."
                "If a girls resistance is high, it's probably a good idea to avoid giving her any more serum until it's dropped back down to reasonable levels."
                return

            "Continue.":
                return

            "Continue and disable this notification in the future.":
                $resist_tutorial = False
                return

    return

label start:
    scene bg bedroom
    "This is the start of the game. Welcome!"
    "Inside you will find a great many topics, most of them sexual. All characters depicted are over 18."
    menu:
        "I am over 18 or my countries equivalent.":
            jump overCont

        "I am under 18 or my countries equivalent.":
            jump underQuit

label underQuit:
    "You're not allowed to view this content."
    return

label overCont:
    python:
        inputName = renpy.input("What is your first name?")
        inputName = inputName.strip()
        if not inputName:
            inputName = "Derik"

    "Very well, you will be known as [inputName]."

    call screen diff_screen
    ## Values modified by difficulty. Established here so they are in scope everywhere else ##

    $ difficulty = "Normal"
    $ default_red_avail = 5
    $ min_influence_raise = 1 #Amount influence is raised by a failed event. Others are for success of different levels
    $ low_influence_raise = 4
    $ mid_influence_raise = 6
    $ high_influence_raise = 10
    $ player_money = 50 #used to buy things.
    $ game_length = 120 #default length of the game
    $ default_resistance_gain = 5 # resistance gain, multiplied by the number of times an event has been triggered before.

    # if _return == 0: #Normal mode
        #Do nothing, we have established the normal level variables already.

    if _return == 1: #Easy mode
        $ difficulty = "Easy"
        $ default_red_avail = 8
        $ min_influence_raise = 2 #Amount influence is raised by a failed event. Others are for success of different levels
        $ low_influence_raise = 5
        $ mid_influence_raise = 7
        $ high_influence_raise = 12
        $ player_money = 300 #used to buy things.
        $ game_length = 120
        $ default_resistance_gain = 3

    elif _return == 2: #Sandbox mode
        $ difficulty = "Sandbox"
        $ default_red_avail = 5
        $ min_influence_raise = 1 #Amount influence is raised by a failed event. Others are for success of different levels
        $ low_influence_raise = 4
        $ mid_influence_raise = 6
        $ high_influence_raise = 10
        $ player_money = 1000 #used to buy things.
        $ game_length = 360
        $ default_resistance_gain = 5

    $ resist_tutorial = True # Warn the player if Resistance is too high, and offer to tell them how to fix it.

    $ sharing_wage = False # Share with your mother.

    $ has_lab_code = False #Get into the lab after hours.

    $ knows_blue_serum = False # Knows blue

    $ has_online_code = False #Set the player on the path to learning about blue

    $ has_research_papers = False #Set the player on the path to learning about advanced

    $ knows_advanced_info = False #Knows enough to learn more about purp and red.

    $ has_lab_assistant = False #You'll need help for the more advanced serums.

    $ has_advanced_papers = False #Unlocks the lore dump for purples

    $ knows_purple_serum = False #Low resistance, low slut

    $ knows_red_serum = False ##High resistance, high slut

    $ has_alex_number = False
    $ has_steph_number = False
    $ has_nora_number = False

    $ off_Work = False
    $ went_Work = False
    $ days_Off_Work = 0

    $ default_Wage = 200
    $ current_Wage = 200
    $ missed_Day_Deduction = 40

    $ mom_Split_Wage_Amount = 50

    # mod variables
    $ phone_call_made = False
    $ skip_nobody_home_lab_event = False
    $ skip_find_alex = False
    $ steph_in_lab = False
    $ steph_not_in_lab = False
    $ nora_in_lab = False
    $ nora_not_in_lab = False
    $ sis_in_room = False
    $ sis_not_in_room = False
    $ sis_date_checked = False
    $ lab_cleaned_up = False
    $ maj_night_event_triggered = False
    $ sleep_in_missed = False
    $ serum_xp = 0
    $ practiced_serum_skill = False
    $ expert_serum_skill = False

    #######################
    ##Major Scene Objects##
    #######################

    #Nora events
    $ blueberry_event_object = Major_Scene("Nora Blueberry",5, default_resistance_gain) #
    $ party_event_object = Major_Scene("Nora Party", 6, default_resistance_gain) #
    $ nora_study_event_object = Major_Scene("Nora Study", 6, default_resistance_gain) #
    $ nora_beach_event_object = Major_Scene("Nora Beach", 6, default_resistance_gain) #

    #Steph events
    $ steph_drink_event_object = Major_Scene("Steph Drink", 5, default_resistance_gain) #
    $ steph_tennis_event_object = Major_Scene("Steph Tennis", 6, default_resistance_gain) #
    $ steph_party_event_object = Major_Scene("Steph Party", 6, default_resistance_gain) #
    #Plus red_serum events. Only ever called once so it doesn't have an object for tracking repeats. #
    $ steph_beach_event_object = Major_Scene("Steph Beach", 6, default_resistance_gain) #

    #Mom events
    $ mom_movie_event_object = Major_Scene("Mom Movie", 6, default_resistance_gain) #
    $ mom_night_event_object = Major_Scene("Mom Night",6, default_resistance_gain) #
    $ mom_bathroom_event_object = Major_Scene("Mom Bathroom", 6, default_resistance_gain) #
    $ mom_beach_event_object = Major_Scene("Mom Beach", 6, default_resistance_gain) #

    #Alexia events
    $ coffee_event_object = Major_Scene("Alex Coffee", 6, default_resistance_gain)  #
    $ lab_test_object = Major_Scene("Alex Labtest", 6, default_resistance_gain) #
    $ test_studying_object = Major_Scene("Alex Study", 6, default_resistance_gain)  #
    $ mall_event_object = Major_Scene("Alex Mall", 6, default_resistance_gain) #
    $ alex_beach_event_object = Major_Scene("Alex Beach", 6, default_resistance_gain) #

    #Sister events
    $ sis_night_event_object = Major_Scene("Lily Night", 6, default_resistance_gain)  #
    $ sis_morning_event_object = Major_Scene("Lily Morning", 5, default_resistance_gain) #
    $ sis_movie_event_object = Major_Scene("Lily Movie", 6, default_resistance_gain) #
    $ sis_bathroom_event_object = Major_Scene("Lily Bathroom", 6, default_resistance_gain) #
    $ sis_beach_event_object = Major_Scene("Lily Beach", 6, default_resistance_gain) #

    #Special events
    $ lab_threesome_event_object = Major_Scene("Nora Steph Lab", 6, default_resistance_gain) #
    $ movie_threesome_event_object = Major_Scene("Mom Lily Movie", 6, default_resistance_gain)  #
    $ nora_mom_study_event_object = Major_Scene("Mom Nora Study", 6, default_resistance_gain)  #
    $ lab_alex_steph_event_object = Major_Scene("Alex Steph Lab",6, default_resistance_gain) #

    #######################
    ##Minor Scene Objects##
    #######################

    #Nora events
    $ nora_hub = Minor_Scene("Nora Hub", 6, default_red_avail*2) #

    $ nora_walk_in = Minor_Scene("Nora Walk In", 3, default_red_avail) # new exhib and freeuse added, faster if exhib
    $ nora_panty_play = Minor_Scene("Nora Panty Play", 2, default_red_avail) # faster if freeuse. Small free use section
    $ nora_nudes = Minor_Scene("Nora Nudes", 2, default_red_avail) # Small exhib section
    $ nora_housework = Minor_Scene("Nora Housework", 2, default_red_avail) # new exhib section
    $ nora_copcar = Minor_Scene("Nora Copcar", 3, default_red_avail) #  nothing needed.
    $ nora_beach_tan = Minor_Scene("Nora Beach Tan", 3, default_red_avail) # nothing needed.
    $ nora_schoolgirl = Minor_Scene("Nora Schoolgirl", 1, default_red_avail) # nothing needed.
    $ nora_masturbating = Minor_Scene("Nora Masturbating", 2, default_red_avail) #Test masturbating scene

    #Steph events
    $ steph_hub = Minor_Scene("Steph Hub", 6, default_red_avail*2) #

    $ steph_nudes = Minor_Scene("Steph Nudes", 4, default_red_avail) #
    $ steph_walk_in = Minor_Scene("Steph Walk In", 5, default_red_avail) #
    $ steph_nap = Minor_Scene("Steph Nap", 3, default_red_avail) #
    $ steph_stockroom = Minor_Scene("Steph Stockroom", 4, default_red_avail) #
    $ steph_beach_volley = Minor_Scene("Steph Beach Volley", 3, default_red_avail) #

    #Mom events
    $ mom_hub = Minor_Scene("Mom Hub", 6, default_red_avail*2) #

    $ mom_catch = Minor_Scene("Mom Catch", 1, default_red_avail) #
    $ mom_favours = Minor_Scene("Mom Favours", 10, default_red_avail) #
    $ mom_porn_catch = Minor_Scene("Mom Porn Catch", 4, default_red_avail) #
    $ mom_sleep = Minor_Scene("Mom Sleep", 3, default_red_avail)  #
    $ mom_wakeup = Minor_Scene("Mom Wakeup", 4, default_red_avail) #
    $ mom_beach_swim = Minor_Scene("Mom Beach Swim", 3, default_red_avail) #
    $ mom_shower = Minor_Scene("Mom Shower", 4, default_red_avail) #  TODO: image

    #Alex events
    $ alex_hub = Minor_Scene("Alex Hub", 6, default_red_avail*2) #

    $ alex_nudes = Minor_Scene("Alex Nudes", 3, default_red_avail) #
    $ alex_porn_start = Minor_Scene("Alex Porn Start", 2, default_red_avail) #
    $ alex_porn_visit = Minor_Scene("Alex Porn Visit", 3, 0) #
    $ alex_porn_help = Minor_Scene ("Alex Porn Help", 2, default_red_avail) #
    $ alex_nap = Minor_Scene ("Alex Nap", 3, default_red_avail) #
    $ alex_bus = Minor_Scene ("Alex Bus", 4, default_red_avail) #
    $ alex_beach_walk = Minor_Scene ("Alex Beach Walk", 4, default_red_avail) #

    #Lily events
    $ sis_hub = Minor_Scene("Lily Hub", 6, default_red_avail*2) #

    $ sis_mast = Minor_Scene("Lily Mast", 2, default_red_avail) #
    $ sis_peek = Minor_Scene("Lily Peek", 3, default_red_avail) #
    $ sis_porn_catch = Minor_Scene("Lily Porn Catch", 4, default_red_avail) #
    $ sis_search_room = Minor_Scene("Lily Search Room", 4, 0) #
    $ sis_search_comp = Minor_Scene("Lily Search Comp", 5, 0) #
    $ sis_sleep = Minor_Scene("Lily Sleep", 3, default_red_avail) #
    $ sis_videogame = Minor_Scene("Lily Videogame", 3, default_red_avail) #
    $ sis_beach_walk = Minor_Scene("Lily Beach Walk", 3, default_red_avail) #
    $ sis_shower = Minor_Scene("Lily Shower", 4, default_red_avail) # TODO: image

    #Special events
    $ nora_steph_work_undress = Minor_Scene("Nora Steph Work Undress", 4, default_red_avail) #
    $ nora_steph_caught = Minor_Scene("Nora Steph Caught", 3, default_red_avail) #
    $ mom_lily_movie = Minor_Scene ("Mom Lily Movie", 3, default_red_avail) #

    ##Minor Scene Triggers##
    $ alex_porn_site = False
    $ alex_has_blow = False
    $ alex_has_fuck = False

    $ beach_unlocked = False
    $ beach_girl = None
    $ alex_beach_busy = False #She goes to the beach without you sometimes, stop her from being accessable in other events.

    $ player_serum_supplies = 0 #Used by purple and red to make. Costs cash to buy.
    $ player_blue_serum = 0 #Easiest to make, but has no extra effect on their slut score when used. +0 temp
    $ player_purple_serum = 0 #Requires access to the lab alone to make and some money for supplies, but raises the targets slut score temperarily when used. +15 temp
    $ player_red_serum = 0 #Requires assistance in the lab to make, money, and special supplies, but raises the targets slut score a lot when used. +30 temp

    $ steph_knows_alex = False

    ##Random Event Objects##

    ####How random events work, for you curious code monkeys:####
    #Test_Event = Random_Event(min,max,start,inc)
    #Test_Event.check_event() returns a boolean, True if the event has triggered, false otherwise.
    #Each time the event fails to trigger, the current chance of the event happening is increases by "inc" amount, until it hits "max".
    #When an event is triggered (ie. check_event returns True) the current chance of the event happening is reset to "min" amount.
    #"start" is the chance used by the event when the object is first created, which may be higher than min (or higher than max, if you want it to be!)
    #So our test event with min = 10, max = 50, start = 30, and inc = 5 would start off with a 30% chance of happening each time check_event() is called. Each time it fails to trigger, that's increased by 5%.
    #When it does trigger, the chance it will trigger next time is 10%.

    # $ night_chance = Random_Event(10,40,0,5) ##Min, Max, Start, Inc
    $ night_sis_drink_chance = Random_Event(10,25,0,3)
    $ night_mom_drink_chance = Random_Event(10,25,0,3)
    $ night_sis_sleepover_chance = Growth_Event(0,100,0,3,10,50)
    $ night_mom_sleepover_chance = Growth_Event(0,100,0,3,10,50)
    $ sister_chance = Random_Event(70,70,70,0)
    # $ wake_up = Random_Event(10,30,10,3)
    $ wake_up = Growth_Event(10,80,80,10,10,90)
    $ wake_up_recover = Random_Event(70,70,70,0)
    $ date_chance = Random_Event(30,75,45,15)
    $ peep_chance = Random_Event(20,50,30,10)
    # $ mast_chance = Random_Event(10,35,5,5)
    $ mast_chance = Growth_Event(20,40,5,5,5,30)
    # $ mom_mast_chance = Random_Event(10,20,5,5)
    $ mom_mast_chance = Growth_Event(10,40,10,10,10,70)
    # $ interrupt_chance = Random_Event(20,40,30,5)
    $ mom_interrupt_chance = Growth_Event(20,40,30,5,10,80)
    $ sis_interrupt_chance = Growth_Event(20,40,30,5,10,80)
    $ alex_bus_chance = Random_Event(10,50,0,2)
    # $ nap_interrupt_chance = Random_Event(10,40,20,5)
    $ alex_nap_interrupt_chance = Growth_Event(10,40,30,5,5,80)
    $ steph_nap_interrupt_chance = Growth_Event(10,40,30,5,5,80)
    $ test_chance = Random_Event(20,40,20,5)
    # $ moving_chance = Random_Event(20,40,20,10)
    $ moving_chance = Growth_Event(20,50,0,10,10,80)
    # $ study_chance = Random_Event(25,45,30,5)
    $ study_chance = Growth_Event(25,45,0,5,5,50)
    $ mom_join_chance = Random_Event(75,100,100,5)
    # $ steph_stripped_chance = Random_Event(10,30,20,5)
    $ steph_stripped_chance = Growth_Event(10,30,10,5,2,20)
    # $ nora_stripped_chance = Random_Event(10,30,20,5)
    $ nora_stripped_chance = Growth_Event(10,30,10,5,2,20)
    $ nora_party_chance = Random_Event(30,70,0,5)
    $ steph_lab_chance = Random_Event(40,80,40,10)
    $ nora_steph_lab_chance = Random_Event(0,50,0,5)
    # $ lab_strip_chance = Random_Event(10,30,10,5)
    $ lab_strip_chance = Growth_Event(10,30,10,5,5,50)
    $ blueberry_caught = Random_Event(0,30,0,5)
    $ panty_find_chance = Growth_Event(20,80,0,10,20,80)
    $ lab_code_chance = Random_Event(50,100,50,20)
    $ nora_lab_chance = Random_Event(60,90,60,5)
    # $ nora_steph_les_chance = Random_Event(20,40,20,5)
    $ nora_steph_les_chance = Growth_Event(20,40,20,5,2,10)
    $ chance_red = Random_Event(40,100,40,20)
    $ snacks_chance = Random_Event(20,90,0,5)
    # $ steph_party = Random_Event(30,60,30,5)
    $ steph_party = Growth_Event(30,60,30,5,5,70)
    # $ alex_gangbang = Random_Event(25,75,50,25)
    $ alex_gangbang = Growth_Event(25,75,50,25,5,20)
    # $ nora_pull_over = Random_Event(20,60,20,10)
    $ nora_pull_over = Growth_Event(20,60,20,10,5,50)
    $ stockroom_check = Growth_Event(0,80,0,5,2,10)
    # $ nora_schoolgirl_check = Random_Event(30,70,30,5)
    $ nora_schoolgirl_check = Growth_Event(30,70,30,5,10,30)
    $ alex_steph_lab_check = Random_Event(60,30,70,10)
    # $ shower_interupt_check = Random_Event(30,80,60,15)
    $ shower_interupt_check = Growth_Event(30,80,60,15,5,70)

    #TODO mod scene checks
    # Growth_Event Args ==  (min, max, start, inc, growth, growthLimit)
    $ nora_masturbating_chance = Growth_Event(10,25,10,5,5,60)

    $ purple_serum_debuff = 15 #Amount it lowers influence by
    $ red_serum_buff = 15 #Amount it raises influence by

    #0-5 not slutty at all.
    #6-15 slightly slutty. Says lewd things but won't follow through. Might forget that some things shouldn't be shown off. (Leans over too far, grabs own tits, ect)
    #16-25 minor slut. Likes being watched and feels like it's normal. (Leans over for you, doesn't mind being seen naked sometimes, talks about sex freely, masturbates in private at night)
    #26-40 moderate slut. masturbates in private during the day, comfortable seeing you naked and being naked in front of you most of the time. Might ask to be touched by you or give you a handjob
    #41-65 major slut. masturbates in public if they think they can get away with it. Starts wearing skimpier clothing around the house, teasing you on purpose, or engaging in mutual masturbation, handjobs, or boobjobs.
    #66-80 Huge slut. Wears slutty clothing when they can, willing to have give handjobs, titjobs, or blowjobs.
    #81-95 Massive slut. Loves sex, servicing, and being a slut. Will let you fuck her whenever you want.
    #96-100 Collosal slut. Will present for sex without asking, suck you off unless you tell them no, and do anything if you promise to fuck them later.

    $ momO = Girl("Mom")
    $ sisO = Girl("Lily")
    $ noraO = Girl("Nora")
    $ stephO = Girl("Stephanie")
    $ alexO = Girl("Alexia")

    $ day = 0 #goes for 4 months, so 120 days in the game.
    $ dayTime = 0 #where 0 is morning, 1 is afternoon, 2 is night.
    $ slept_early = False #Did the player sleep early last night. Enables some morning actions.
    jump introRoom

style hudStyle is text:
    bold True
    color Color("#dadada")
    outlines [(3, "#000", 0,0)]


style notebookStyle is text:
    ##font "Viner_Hand_ITC.ttf"
    font gui.default_font
    color Color("#444444")

style notebookStyle_Small is text:
    ##font "Viner_Hand_ITC.ttf"
    font gui.default_font
    color Color("#444444")
    size 22

screen diff_screen:
    hbox:
        xalign 0.5
        yalign 0.3
        spacing 120
        vbox:
            imagebutton auto "Diff_Background_Sandbox_%s.png" action Return(2)
        vbox:
            imagebutton auto "Diff_Background_Easy_%s.png" action Return(1)
        vbox:
            imagebutton auto "Diff_Background_Normal_%s.png" action Return(0)

screen infoButton: ##For bringing up info_screen
    vbox xalign 1.0 yalign 0:
        imagebutton:
            idle "Menu_Info_Tab.png"
            hover "Menu_Info_Tab_Hover.png"
            action ui.callsinnewcontext ("toggleInfoButton")

screen infoScreen: ##Displays information about all of the girls and yourself.
    frame:
        background "Menu_Notebook.png"
        xalign 0.5
        yalign 0.15
        xsize 620 ysize 800
        #Girl Select
        vbox: ##Left Aligned vbox
            xalign 0.04
            yalign 0.65
            spacing 20
            imagebutton:
                idle "Mom_Menu_Note.png"
                hover "Mom_Menu_Note_Hover.png"
                action Jump("momInfo")
            imagebutton:
                idle "Lily_Menu_Note.png"
                hover "Lily_Menu_Note_Hover.png"
                action Jump("sisInfo")
            imagebutton:
                idle "Nora_Menu_Note.png"
                hover "Nora_Menu_Note_Hover.png"
                action Jump("noraInfo")
            imagebutton:
                idle "Steph_Menu_Note.png"
                hover "Steph_Menu_Note_Hover.png"
                action Jump("stephInfo")
            imagebutton:
                idle "Alexia_Menu_Note.png"
                hover "Alexia_Menu_Note_Hover.png"
                action Jump("alexInfo")

        vbox: #Right Aligned vbox
            xalign 1.1425
            yalign 0.08
            spacing 20
            imagebutton:
                idle "Return_Menu_Note.png"
                hover "Return_Menu_Note_Up.png"
                action Return()
            imagebutton:
                idle "Help_Menu_Note.png"
                hover "Help_Menu_Note_Hover.png"
                action Jump ("helpInfo")

        #Center aligned vbox
        vbox:
            xpos 100
            ypos 100
            xsize 600
            ysize 200
            spacing 20
            text "Inventory" style "notebookStyle" bold True underline True
            text "Serum Supplies: %i" %(player_serum_supplies) style "notebookStyle"
            text "Blue Serum: %i" %(player_blue_serum) style "notebookStyle"
            text "Purple Serum: %i" %(player_purple_serum) style "notebookStyle"
            text "Red Serum: %i" %(player_red_serum) style "notebookStyle"

        imagebutton auto "Ending_Skip_%s.png" action Jump("skip_end_confirm"):
            xalign 1.55
            yalign 0.95



screen momInfoScreen:
    frame:
        background "Menu_Notebook.png"
        xalign 0.5
        yalign 0.15
        xsize 620 ysize 800
        #Girl Select
        vbox: ##Left Aligned vbox
            xalign 0.04
            yalign 0.65
            spacing 20
            imagebutton:
                idle "Mom_Menu_Note.png"
                hover "Mom_Menu_Note_Hover.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Lily_Menu_Note.png"
                hover "Lily_Menu_Note_Hover.png"
                action Jump("sisInfo")
            imagebutton:
                idle "Nora_Menu_Note.png"
                hover "Nora_Menu_Note_Hover.png"
                action Jump("noraInfo")
            imagebutton:
                idle "Steph_Menu_Note.png"
                hover "Steph_Menu_Note_Hover.png"
                action Jump("stephInfo")
            imagebutton:
                idle "Alexia_Menu_Note.png"
                hover "Alexia_Menu_Note_Hover.png"
                action Jump("alexInfo")

        vbox: #Right Aligned vbox
            xalign 1.1425
            yalign 0.08
            spacing 20
            imagebutton:
                idle "Return_Menu_Note.png"
                hover "Return_Menu_Note_Up.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Help_Menu_Note.png"
                hover "Help_Menu_Note_Hover.png"
                action Jump ("helpInfo")
        vbox:
            xpos 100
            ypos 100
            xsize 600
            ysize 400
            text "Mom's Stats" style "notebookStyle" bold True underline True
            text "Influence: %i" %(momO.slut_score) style "notebookStyle"
            text "      %s" %(momO.get_slut_description()) style "notebookStyle" italic True size 22
            null height 5
            text "Resistance: %i" %(momO.resist_score) style "notebookStyle"
            text "      %s" %(momO.get_resist_description()) style "notebookStyle" italic True size 22
            null height 15
            text "Stripped %i times" %(momO.naked_count) style "notebookStyle"
            text "Gave handjob %i times" %(momO.hand_count) style "notebookStyle"
            text "Titfucked %i times" %(momO.tit_count) style "notebookStyle"
            text "Gave blowjob %i times" %(momO.blow_count) style "notebookStyle"
            text "Had sex %i times" %(momO.sex_count) style "notebookStyle"
            null height 15
            if momO.bc:
                text "Currently on birth control: Yes" style "notebookStyle"
            else:
                text "Currently on birth control: No" style "notebookStyle"
            text "Came onto her %i times" %(momO.cum_over_count) style "notebookStyle"
            text "Came inside her pussy %i times" %(momO.cum_inside_count) style "notebookStyle"
            text "      Pregnancy Score: [momO.preg_score]/100" style "notebookStyle" italic True size 22
            text "Came inside her ass %i times" %(momO.cum_inside_ass_count) style "notebookStyle"
            text "Came in her mouth %i times" %(momO.cum_mouth_count) style "notebookStyle"
            text "Swallowed your cum %i times" %(momO.cum_swallow_count) style "notebookStyle"
        vbox:
            xpos 400
            ypos 135
            xsize 300
            spacing 0
            text "Training:" style "notebookStyle"
            if momO.cumslut:
                text "      Cumslut" style "notebookStyle" italic True size 22
            if momO.anal:
                text "      Anal Lover" style "notebookStyle" italic True size 22
            if momO.freeuse:
                text "      Free Use Slut" style "notebookStyle" italic True size 22
            if momO.exhib:
                text "      Exhibitionist" style "notebookStyle" italic True size 22
            if not (momO.cumslut or momO.anal or momO.freeuse or momO.exhib):
                text "      None" style "notebookStyle" italic True size 22

screen sisInfoScreen:
    frame:
        background "Menu_Notebook.png"
        xalign 0.5
        yalign 0.15
        xsize 620 ysize 800
        #Girl Select
        vbox: ##Left Aligned vbox
            xalign 0.04
            yalign 0.65
            spacing 20
            imagebutton:
                idle "Mom_Menu_Note.png"
                hover "Mom_Menu_Note_Hover.png"
                action Jump("momInfo")
            imagebutton:
                idle "Lily_Menu_Note.png"
                hover "Lily_Menu_Note_Hover.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Nora_Menu_Note.png"
                hover "Nora_Menu_Note_Hover.png"
                action Jump("noraInfo")
            imagebutton:
                idle "Steph_Menu_Note.png"
                hover "Steph_Menu_Note_Hover.png"
                action Jump("stephInfo")
            imagebutton:
                idle "Alexia_Menu_Note.png"
                hover "Alexia_Menu_Note_Hover.png"
                action Jump("alexInfo")

        vbox: #Right Aligned vbox
            xalign 1.1425
            yalign 0.08
            spacing 20
            imagebutton:
                idle "Return_Menu_Note.png"
                hover "Return_Menu_Note_Up.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Help_Menu_Note.png"
                hover "Help_Menu_Note_Hover.png"
                action Jump ("helpInfo")
        vbox:
            xpos 100
            ypos 100
            xsize 600
            ysize 400
            text "Lily's Stats" style "notebookStyle" bold True underline True
            text "Influence: %i" %(sisO.slut_score) style "notebookStyle"
            text "      %s" %(sisO.get_slut_description()) style "notebookStyle" italic True size 22
            null height 5
            text "Resistance: %i" %(sisO.resist_score) style "notebookStyle"
            text "      %s" %(sisO.get_resist_description()) style "notebookStyle" italic True size 22
            null height 15
            text "Stripped %i times" %(sisO.naked_count) style "notebookStyle"
            text "Gave handjob %i times" %(sisO.hand_count) style "notebookStyle"
            text "Titfucked %i times" %(sisO.tit_count) style "notebookStyle"
            text "Gave blowjob %i times" %(sisO.blow_count) style "notebookStyle"
            text "Had sex %i times" %(sisO.sex_count) style "notebookStyle"
            null height 15
            if sisO.bc:
                text "Currently on birth control: Yes" style "notebookStyle"
            else:
                text "Currently on birth control: No" style "notebookStyle"
            text "Came onto her %i times" %(sisO.cum_over_count) style "notebookStyle"
            text "Came inside her pussy %i times" %(sisO.cum_inside_count) style "notebookStyle"
            text "      Pregnancy Score: [sisO.preg_score]/100" style "notebookStyle" italic True size 22
            text "Came inside her ass %i times" %(sisO.cum_inside_ass_count) style "notebookStyle"
            text "Came in her mouth %i times" %(sisO.cum_mouth_count) style "notebookStyle"
            text "Swallowed your cum %i times" %(sisO.cum_swallow_count) style "notebookStyle"
        vbox:
            xpos 400
            ypos 135
            xsize 300
            spacing 0
            text "Training:" style "notebookStyle"
            if sisO.cumslut:
                text "      Cumslut" style "notebookStyle" italic True size 22
            if sisO.anal:
                text "      Anal Lover" style "notebookStyle" italic True size 22
            if sisO.freeuse:
                text "      Free Use Slut" style "notebookStyle" italic True size 22
            if sisO.exhib:
                text "      Exhibitionist" style "notebookStyle" italic True size 22
            if not (sisO.cumslut or sisO.anal or sisO.freeuse or sisO.exhib):
                text "      None" style "notebookStyle" italic True size 22


screen noraInfoScreen:
    frame:
        background "Menu_Notebook.png"
        xalign 0.5
        yalign 0.15
        xsize 620 ysize 800
        #Girl Select
        vbox: ##Left Aligned vbox
            xalign 0.04
            yalign 0.65
            spacing 20
            imagebutton:
                idle "Mom_Menu_Note.png"
                hover "Mom_Menu_Note_Hover.png"
                action Jump("momInfo")
            imagebutton:
                idle "Lily_Menu_Note.png"
                hover "Lily_Menu_Note_Hover.png"
                action Jump("sisInfo")
            imagebutton:
                idle "Nora_Menu_Note.png"
                hover "Nora_Menu_Note_Hover.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Steph_Menu_Note.png"
                hover "Steph_Menu_Note_Hover.png"
                action Jump("stephInfo")
            imagebutton:
                idle "Alexia_Menu_Note.png"
                hover "Alexia_Menu_Note_Hover.png"
                action Jump("alexInfo")

        vbox: #Right Aligned vbox
            xalign 1.1425
            yalign 0.08
            spacing 20
            imagebutton:
                idle "Return_Menu_Note.png"
                hover "Return_Menu_Note_Up.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Help_Menu_Note.png"
                hover "Help_Menu_Note_Hover.png"
                action Jump ("helpInfo")
        vbox:
            xpos 100
            ypos 100
            xsize 600
            ysize 400
            text "Nora's Stats" style "notebookStyle" bold True underline True
            text "Influence: %i" %(noraO.slut_score) style "notebookStyle"
            text "      %s" %(noraO.get_slut_description()) style "notebookStyle" italic True size 22
            null height 5
            text "Resistance: %i" %(noraO.resist_score) style "notebookStyle"
            text "      %s" %(noraO.get_resist_description()) style "notebookStyle" italic True size 22
            null height 15
            text "Stripped %i times" %(noraO.naked_count) style "notebookStyle"
            text "Gave handjob %i times" %(noraO.hand_count) style "notebookStyle"
            text "Titfucked %i times" %(noraO.tit_count) style "notebookStyle"
            text "Gave blowjob %i times" %(noraO.blow_count) style "notebookStyle"
            text "Had sex %i times" %(noraO.sex_count) style "notebookStyle"
            null height 15
            if noraO.bc:
                text "Currently on birth control: Yes" style "notebookStyle"
            else:
                text "Currently on birth control: No" style "notebookStyle"
            text "Came onto her %i times" %(noraO.cum_over_count) style "notebookStyle"
            text "Came inside her pussy %i times" %(noraO.cum_inside_count) style "notebookStyle"
            text "      Pregnancy Score: [noraO.preg_score]/100" style "notebookStyle" italic True size 22
            text "Came inside her ass %i times" %(noraO.cum_inside_ass_count) style "notebookStyle"
            text "Came in her mouth %i times" %(noraO.cum_mouth_count) style "notebookStyle"
            text "Swallowed your cum %i times" %(noraO.cum_swallow_count) style "notebookStyle"
        vbox:
            xpos 400
            ypos 135
            xsize 300
            spacing 0
            text "Training:" style "notebookStyle"
            if noraO.cumslut:
                text "      Cumslut" style "notebookStyle" italic True size 22
            if noraO.anal:
                text "      Anal Lover" style "notebookStyle" italic True size 22
            if noraO.freeuse:
                text "      Free Use Slut" style "notebookStyle" italic True size 22
            if noraO.exhib:
                text "      Exhibitionist" style "notebookStyle" italic True size 22
            if not (noraO.cumslut or noraO.anal or noraO.freeuse or noraO.exhib):
                text "      None" style "notebookStyle" italic True size 22

screen stephInfoScreen:
    frame:
        background "Menu_Notebook.png"
        xalign 0.5
        yalign 0.15
        xsize 620 ysize 800
        #Girl Select
        vbox: ##Left Aligned vbox
            xalign 0.04
            yalign 0.65
            spacing 20
            imagebutton:
                idle "Mom_Menu_Note.png"
                hover "Mom_Menu_Note_Hover.png"
                action Jump("momInfo")
            imagebutton:
                idle "Lily_Menu_Note.png"
                hover "Lily_Menu_Note_Hover.png"
                action Jump("sisInfo")
            imagebutton:
                idle "Nora_Menu_Note.png"
                hover "Nora_Menu_Note_Hover.png"
                action Jump("noraInfo")
            imagebutton:
                idle "Steph_Menu_Note.png"
                hover "Steph_Menu_Note_Hover.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Alexia_Menu_Note.png"
                hover "Alexia_Menu_Note_Hover.png"
                action Jump("alexInfo")

        vbox: #Right Aligned vbox
            xalign 1.1425
            yalign 0.08
            spacing 20
            imagebutton:
                idle "Return_Menu_Note.png"
                hover "Return_Menu_Note_Up.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Help_Menu_Note.png"
                hover "Help_Menu_Note_Hover.png"
                action Jump ("helpInfo")
        vbox:
            xpos 100
            ypos 100
            xsize 600
            ysize 400
            text "Stephanie's Stats" style "notebookStyle" bold True underline True
            text "Influence: %i" %(stephO.slut_score) style "notebookStyle"
            text "      %s" %(stephO.get_slut_description()) style "notebookStyle" italic True size 22
            null height 5
            text "Resistance: %i" %(stephO.resist_score) style "notebookStyle"
            text "      %s" %(stephO.get_resist_description()) style "notebookStyle" italic True size 22
            null height 15
            text "Stripped %i times" %(stephO.naked_count) style "notebookStyle"
            text "Gave handjob %i times" %(stephO.hand_count) style "notebookStyle"
            text "Titfucked %i times" %(stephO.tit_count) style "notebookStyle"
            text "Gave blowjob %i times" %(stephO.blow_count) style "notebookStyle"
            text "Had sex %i times" %(stephO.sex_count) style "notebookStyle"
            null height 15
            if stephO.bc:
                text "Currently on birth control: Yes" style "notebookStyle"
            else:
                text "Currently on birth control: No" style "notebookStyle"
            text "Came onto her %i times" %(stephO.cum_over_count) style "notebookStyle"
            text "Came inside her pussy %i times" %(stephO.cum_inside_count) style "notebookStyle"
            text "      Pregnancy Score: [stephO.preg_score]/100" style "notebookStyle" italic True size 22
            text "Came inside her ass %i times" %(stephO.cum_inside_ass_count) style "notebookStyle"
            text "Came in her mouth %i times" %(stephO.cum_mouth_count) style "notebookStyle"
            text "Swallowed your cum %i times" %(stephO.cum_swallow_count) style "notebookStyle"
        vbox:
            xpos 400
            ypos 135
            xsize 300
            spacing 0
            text "Training:" style "notebookStyle"
            if stephO.cumslut:
                text "      Cumslut" style "notebookStyle" italic True size 22
            if stephO.anal:
                text "      Anal Lover" style "notebookStyle" italic True size 22
            if stephO.freeuse:
                text "      Free Use Slut" style "notebookStyle" italic True size 22
            if stephO.exhib:
                text "      Exhibitionist" style "notebookStyle" italic True size 22
            if not (stephO.cumslut or stephO.anal or stephO.freeuse or stephO.exhib):
                text "      None" style "notebookStyle" italic True size 22

screen alexInfoScreen:
    frame:
        background "Menu_Notebook.png"
        xalign 0.5
        yalign 0.15
        xsize 620 ysize 800
        #Girl Select
        vbox: ##Left Aligned vbox
            xalign 0.04
            yalign 0.65
            spacing 20
            imagebutton:
                idle "Mom_Menu_Note.png"
                hover "Mom_Menu_Note_Hover.png"
                action Jump("momInfo")
            imagebutton:
                idle "Lily_Menu_Note.png"
                hover "Lily_Menu_Note_Hover.png"
                action Jump("sisInfo")
            imagebutton:
                idle "Nora_Menu_Note.png"
                hover "Nora_Menu_Note_Hover.png"
                action Jump("noraInfo")
            imagebutton:
                idle "Steph_Menu_Note.png"
                hover "Steph_Menu_Note_Hover.png"
                action Jump("stephInfo")
            imagebutton:
                idle "Alexia_Menu_Note.png"
                hover "Alexia_Menu_Note_Hover.png"
                action Jump("toggleInfoButton")

        vbox: #Right Aligned vbox
            xalign 1.1425
            yalign 0.08
            spacing 20
            imagebutton:
                idle "Return_Menu_Note.png"
                hover "Return_Menu_Note_Up.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Help_Menu_Note.png"
                hover "Help_Menu_Note_Hover.png"
                action Jump ("helpInfo")
        vbox:
            xpos 100
            ypos 100
            xsize 600
            ysize 400
            text "Alexia's Stats" style "notebookStyle" bold True underline True
            text "Influence: %i" %(alexO.slut_score) style "notebookStyle"
            text "      %s" %(alexO.get_slut_description()) style "notebookStyle" italic True size 22
            null height 5
            text "Resistance: %i" %(alexO.resist_score) style "notebookStyle"
            text "      %s" %(alexO.get_resist_description()) style "notebookStyle" italic True size 22
            null height 15
            text "Stripped %i times" %(alexO.naked_count) style "notebookStyle"
            text "Gave handjob %i times" %(alexO.hand_count) style "notebookStyle"
            text "Titfucked %i times" %(alexO.tit_count) style "notebookStyle"
            text "Gave blowjob %i times" %(alexO.blow_count) style "notebookStyle"
            text "Had sex %i times" %(alexO.sex_count) style "notebookStyle"
            null height 15
            if alexO.bc:
                text "Currently on birth control: Yes" style "notebookStyle"
            else:
                text "Currently on birth control: No" style "notebookStyle"
            text "Came onto her %i times" %(alexO.cum_over_count) style "notebookStyle"
            text "Came inside her pussy %i times" %(alexO.cum_inside_count) style "notebookStyle"
            text "      Pregnancy Score: [alexO.preg_score]/100" style "notebookStyle" italic True size 22
            text "Came inside her ass %i times" %(alexO.cum_inside_ass_count) style "notebookStyle"
            text "Came in her mouth %i times" %(alexO.cum_mouth_count) style "notebookStyle"
            text "Swallowed your cum %i times" %(alexO.cum_swallow_count) style "notebookStyle"
        vbox:
            xpos 400
            ypos 135
            xsize 300
            spacing 0
            text "Training:" style "notebookStyle"
            if alexO.cumslut:
                text "      Cumslut" style "notebookStyle" italic True size 22
            if alexO.anal:
                text "      Anal Lover" style "notebookStyle" italic True size 22
            if alexO.freeuse:
                text "      Free Use Slut" style "notebookStyle" italic True size 22
            if alexO.exhib:
                text "      Exhibitionist" style "notebookStyle" italic True size 22
            if not (alexO.cumslut or alexO.anal or alexO.freeuse or alexO.exhib):
                text "      None" style "notebookStyle" italic True size 22

screen helpInfoScreen:
    frame:
        background "Menu_Notebook.png"
        xalign 0.5
        yalign 0.15
        xsize 620 ysize 800
        vbox: ##Left Aligned vbox
            xalign 0.04
            yalign 0.65
            spacing 20
            imagebutton:
                idle "Mom_Menu_Note.png"
                hover "Mom_Menu_Note_Hover.png"
                action Jump("momInfo")
            imagebutton:
                idle "Lily_Menu_Note.png"
                hover "Lily_Menu_Note_Hover.png"
                action Jump("sisInfo")
            imagebutton:
                idle "Nora_Menu_Note.png"
                hover "Nora_Menu_Note_Hover.png"
                action Jump("noraInfo")
            imagebutton:
                idle "Steph_Menu_Note.png"
                hover "Steph_Menu_Note_Hover.png"
                action Jump("stephInfo")
            imagebutton:
                idle "Alexia_Menu_Note.png"
                hover "Alexia_Menu_Note_Hover.png"
                action Jump("alexInfo")

        vbox: #Right Aligned vbox
            xalign 1.1425
            yalign 0.08
            spacing 20
            imagebutton:
                idle "Return_Menu_Note.png"
                hover "Return_Menu_Note_Up.png"
                action Jump("toggleInfoButton")
            imagebutton:
                idle "Help_Menu_Note.png"
                hover "Help_Menu_Note_Hover.png"
                action Jump ("toggleInfoButton")

        viewport id "vp":
            xoffset 80
            yoffset 60
            xfill True
            xsize 520
            ymaximum 700
            mousewheel True
            vbox:
                spacing 10
                #Things I want to include
                #rambling before you do your research and learn everything.
                #Once you figure out the blue serums, replace it with the basics of influence and resistance, and how they can be manipulated.
                #After you unlock the different serums, give details about what they do.

                if knows_blue_serum:
                    text ("    With access to the lab equipment I'll be able to manufacture serum. The process is quick and the materials are inexpensive, so I should be able to get away with this in the lab while I work.") style "notebookStyle_Small"
                    text ("    The effects should be immediate; partial removal of social expectations, influenced by their actions immediately after receiving a dose. For the largest effect, I should try and push my luck as far as I can.") style "notebookStyle_Small"
                    text ("    I'll need to be careful not to try the same trick too many times though. Giving a dose to a girl under circumstances she's been in before will raise alarm bells, and she'll be more resistant to my efforts going forward.") style "notebookStyle_Small"
                    text ("    If that happens, I'll just need to back off for a while. Finding new situations for them to experience should help too, as they become more comfortable with their new ways of thinking. When in doubt, I'll just have to explore.") style "notebookStyle_Small"

                if knows_advanced_info:
                    if not (knows_purple_serum or knows_red_serum):
                        text ("    Everything I've found so far points to the possibility of further development, but I still need the details. The papers I've read had all the important details left out, which can't be a coincidence.") style "notebookStyle_Small"
                        text ("    Nora must know more about this research, if I can convince her to help me I may be able to get the information I need. If she won't, then I'm sure it's stored somewhere in the lab. I just need time to look for it.") style "notebookStyle_Small"
                        text ("    What I have seen looks to be far more advanced than what I'm capable of on my own. I'll need help in the lab to get anywhere. Maybe Stephanie can be persuaded to lend a hand.") style "notebookStyle_Small"
                        text ("    As if that's not enough, anything more advanced is going to need precursors way more pure than we keep in the lab. I'll have to purchase them myself, which won't be cheap.") style "notebookStyle_Small"
                    else:
                        text ("    I've got the synthesis details I need now, it's just a matter of getting time in the lab to do some work. It will be too complicated to do while Nora's watching me, so I'll have to find some other way.") style "notebookStyle_Small"
                        if (has_lab_assistant):
                            text ("    Stephanie's agreed to work with me as a lab assistant. If I bring her everything we need during the morning, she'll help me with whatever I need before Nora gets in to work.") style "notebookStyle_Small"
                        if (knows_red_serum):
                            text ("    This red serum type seems to be very agressive. It's stronger than the generic blue variety I've been using and strips away more of the social barriers the girls have.") style "notebookStyle_Small"
                            text ("    That sudden shift can be shocking though, I should expect a higher than normal spike in resistance by a girl after using it. I may be able to get away with it in a completely new situation though.") style "notebookStyle_Small"
                            text ("    To make a dose I'll need a unit of serum supplies, three doses of blue serum, and some help from a knowledgable lab assistant.") style "notebookStyle_Small"
                        if (knows_purple_serum):
                            text ("    The purple serum type is a much subtler approach. It's noticeably less effective at breaking down social barriers, but that makes it much less noticeable when it's used.") style "notebookStyle_Small"
                            text ("    This will be particularly useful when I end up dosing a girl in situation she's been in before, lowering their future resistance. Unfortunately it won't get rid of it entirely.") style "notebookStyle_Small"
                            text ("    To make a dose I'll need a unit of serum supplies, three doses of blue serum, and some help from a knowledgeable lab assistant.") style "notebookStyle_Small"
        vbar value YScrollValue("vp") at right xoffset 40

label toggleInfoButton:
    call screen infoScreen
    return
label noraInfo:
    call screen noraInfoScreen
    return
label stephInfo:
    call screen stephInfoScreen
    return
label sisInfo:
    call screen sisInfoScreen
    return
label momInfo:
    call screen momInfoScreen
    return
label alexInfo:
    call screen alexInfoScreen
    return
label helpInfo:
    call screen helpInfoScreen
    return

label reset_period_trackers:
    $ phone_call_made = False
    $ skip_nobody_home_lab_event = False
    $ skip_find_alex = False
    $ steph_in_lab = False
    $ steph_not_in_lab = False
    $ nora_in_lab = False
    $ nora_not_in_lab = False
    $ sis_in_room = False
    $ sis_not_in_room = False
    $ sis_date_checked = False
    $ lab_cleaned_up = False
    $ maj_night_event_triggered = False
    $ sleep_in_missed = False
    return

label gain_xp:
    $ serum_xp += 1
    if not practiced_serum_skill:
        if serum_xp > 10:
            "Your efforts are beginning to pay off. You are definitely better at producing serum now than you were when you first started."
            $ practiced_serum_skill = True
    elif not expert_serum_skill:
        if serum_xp > 20:
            "You now know this lab like the back of your hand. You have become extremely efficient at creating serums."
            $ expert_serum_skill = True
    return

screen hud: ##displays stuff for the player during normal gameplay
    $day_name = "Sunday"
    if (day%7) == 0:
        $day_name = "Sunday"
    elif (day%7 == 1):
        $day_name = "Monday"
    elif (day%7 == 2):
        $day_name = "Tuesday"
    elif (day%7 == 3):
        $day_name = "Wednesday"
    elif (day%7 == 4):
        $day_name = "Thursday"
    elif (day%7 == 5):
        $day_name = "Friday"
    elif (day%7 == 6):
        $day_name = "Saturday"

    $time_name = "Morning"
    if dayTime == 0:
        $time_name = "Morning"
    elif dayTime == 1:
        $time_name = "Afternoon"
    elif dayTime == 2:
        $time_name = "Night"



    text ("Day %i/[game_length] - %s %s \n{color=#67c149}Money: $%i" %(day, day_name, time_name, player_money)) style "hudStyle" at topleft #TODO make this a style and unify the UI in v0.4
    text ("Serum Count\n{color=#3179ed}Blue Serum: %i\n{color=#b831ed}Purple Serum: %i\n{color=#e20b61}Red Serum: %i\n{color=#8e8e8e}Serum Supplies: %i" %(player_blue_serum, player_purple_serum, player_red_serum, player_serum_supplies)) size 25 style "hudStyle" text_align 1.0 at right
    text ("Influence\n{color=#57d100}Mom: %i (%i)\n{color=#d100ae}Lily: %i (%i)\n{color=#d1cd00}Alexia: %i (%i)\n{color=#b70000}Stephanie: %i (%i)\n{color=#848484}Nora: %i (%i)" %(momO.slut_score,momO.resist_score, sisO.slut_score, sisO.resist_score, alexO.slut_score, alexO.resist_score, stephO.slut_score, stephO.resist_score, noraO.slut_score, noraO.resist_score)) size 25 style "hudStyle" at left
    ##textbutton "Return" xalign 0.5 yalign 0.98 style "hudStyle" action Return()



label newDay: #go here, not morning. Otherwise days get all screwed up.
    call reset_period_trackers
    $weekend = ((day+1)%7==0 or (day%7)==0) #Calculates it once to figure out if the night was a weekday or not
    #Night time stuff, before it's a new day

    $ noraO.daily_change_resist()
    $ stephO.daily_change_resist()
    $ momO.daily_change_resist()
    $ sisO.daily_change_resist()
    $ alexO.daily_change_resist()
    # $ noraO.change_resist(-1) ##Lower resistances by one each day.
    # $ stephO.change_resist(-1)
    # $ momO.change_resist(-1)
    # $ sisO.change_resist(-1)
    # $ alexO.change_resist(-1)

    if not weekend and not went_Work:
        "Missing work means your paycheck is reduced."
        $ current_Wage += -missed_Day_Deduction

    scene bg house_day
    with fade

    $day += 1 #Monday is day = 1,8,15, ect.
    $dayTime = 0
    $weekend = ((day+1)%7==0 or (day%7)==0) #Checks if this new day is a weekday

    $ off_Work = False
    $ went_Work = False

    if (day == 40): #Intro to the beach
        "There's a knock on your door early in the morning, shortly followed by the sound of it being opened."
        show sis casual1 at right
        me "Lily? What's wrong?"
        "Lily holds a finger up to her lips and slides into the room, closing the door behind her."
        sis "Shh. Mom's about to come up, I need you to play along, okay?"
        me "With what? What time is it?"
        sis "Just trust me, please? You'd be doing me a huge favour."
        "There's another knock on your door."
        mom "Lily? [inputName]?"
        sis "Yeah, he's in here Mom."
        "Lily gives you one last pleading look, then opens your door."
        show mom casual at left
        mom "Good morning [inputName], I hope we didn't wake you."
        sis "No, he was up when I got here."
        me "Yeah, I guess I was. Uh, what's up?"
        mom "Well, I just wanted to double check with you that you're okay with looking after your sister on Saturday."
        me "Looking after Lily?"
        sis "Of course! Looking after me, at the beach."
        me "Right, the beach. On Saturday. Right..."
        mom "Okay, good to hear it. I want you to keep a sharp eye on each other and make sure you're both safe."
        sis "Sure thing Mom, thanks again for letting us go."
        "Lily gives your mom a hug while you sit up and rub your eyes."
        mom "You're welcome sweetheart. I've got to go get ready for work, I'll talk to you both later."
        hide mom
        "Mom leaves your room, and Lily closes the door behind her."
        sis "Whew, thanks for that [inputName]."
        me "Yeah, mind explaining what that was all about?"
        sis "Okay, so the beach is opening in a few days and I really want to go. I told Mom, but she freaked out about me being out there on my own."
        "Lily sits down on your bed beside you."
        sis "So, I told her that you had agreed to go with me already. You don't have to though, I just needed her to calm down about the whole thing."
        me "Oh great, so now when you run off and get into trouble you'll be dragging me down too? I don't think so."
        sis "Fine, then just come along with me so Mom doesn't worry. I've been dying to get out on the beach since summer started."
        me "When were you planning to go again?"
        $ beach_unlocked = True
        sis "Saturday, it's the only day there are busses running down there and back."
        menu:
            "Go to the beach with Lily on Saturday.":
                me "Okay, fine, I'll go."
                sis "Thank you! You're the best!"
                "She leans over and hugs. After a few moments she lets go and stands back up, heading for the door."
                sis "I'll make sure to remind you Saturday morning. Ah, I'm so happy!"
                hide sis
                "She giggles a little and closes your door. You roll over, trying to get comfy in bed again."
                $ beach_girl = "Lily"

            "Tell her no and go back to sleep.":
                me "This Saturday? Sorry, I had stuff I wanted to do."
                sis "What, come on. Please!"
                me "No, I said I'm busy Lily."
                "Lily crosses her arms and pouts at you. You lie back down and roll over in response."
                me "Sorry Lily. Maybe next week or something?"
                sis "Fine. Come talk to me if you change your mind and want to go. I'll text you the bus information."
                hide sis
                "You hear her get up from the bed and walk out of your room, leaving you alone again. You shuffle around, trying to get comfy in bed again."


    if ((day-1)%7 == 0 and day>1): #ie is a Monday other than the first
        $ sleep_in_missed = True
        "Your paycheck arrives in the mail this morning."
        if sharing_wage:
            "You give mom some cash to cover your part of the bills and save the rest."
            $ moneyLeft = current_Wage - mom_Split_Wage_Amount
            if moneyLeft < 0:
                $ moneyLeft = 0
            "There's $[moneyLeft] left in your paycheck for you."
            $ player_money += moneyLeft
            show mom casual at right
            mom "Thank you sweetheart, you're really helping out around here."
            if momO.slut_score <= 20:
                "Mom gives you a big hug."
                mom "I promise I'll make it up to you somehow."
                $ momO.change_slut(1)
            if momO.slut_score > 20:
                call min_morningPay
        else:
            if current_Wage > 0:
                "You deposit the check online, gaining $[current_Wage]."
                $ player_money += current_Wage
            else:
                "You missed so much work there's no pay for this week!"

        $ current_Wage = default_Wage

    if ((day-1)%7 == 5 and beach_unlocked and beach_girl is not None):
        scene bg house_day
        call beach_check()
        $ beach_girl = None
        jump night


    if day >= game_length:
        jump endScreen
    else:
        if day > game_length-20:
            $daysLeft = game_length-day
            "The end of the summer semester is only [daysLeft] days away. Better make the most of the time you have left!"
        jump morning

label morning: #this is for the main gameplay loop at home.
    scene bg house_day
    $ dayTime = 0

    menu:
        "Get into the bathroom early." if slept_early and not weekend: #If you've slept early last night, you can get up early enough
            $ sleep_in_missed = True
            jump morningBathroom
        "Spend the morning with Mom." if weekend: #Mom is only home in the morning on weekends.
            $ sleep_in_missed = True
            jump talkMom
        "See if Lily is home." if not sis_not_in_room: #Random chance to be home each morning.
            $ sleep_in_missed = True
            jump checkSister
        "Text Someone." if (not phone_call_made) and (has_alex_number or has_steph_number or has_nora_number):
            $ sleep_in_missed = True
            jump textScreen
        "Spend time on the internet.":
            $ sleep_in_missed = True
            jump internetBrowse
        "Take a full day trip to a lab supply store." if weekend and knows_advanced_info and player_money > 100:
            $ sleep_in_missed = True
            "It takes two buses and an hour wait to get to the store, located in the middle of an industrial park."
            "You greet the clerk, who gives you a form to fill out for what you need."
            jump orderSupplies
        "Head to campus early." if not weekend: #Work is only on the week days.
            $ sleep_in_missed = True
            jump campusMorning
        "Sleep in today." if not sleep_in_missed: #Skip time
            $ sleep_in_missed = True
            if momO.slut_score > 30 and (not weekend) and wake_up.check_event():
                "You roll over in your bed, turn off your alarm, and drift gently back to sleep."
                mom "[inputName], are you still asleep?"
                show mom work at right
                me "Hmm?"
                "You roll over and look towards your door. Mom's stepped inside and closed it behind her. She's dressed up and ready for work already."
                mom "Come on now, you can't sleep your entire day away."
                me "I can't? Could have fooled me."
                "Mom crosses her arms and frowns."
                mom "You know what I mean. Now, what do I have to do to get you out of bed? I've only got a few minutes until I have to head off to work."
                menu:
                    "Ask for some help waking up.":
                        call min_mom_wakeup
                        if _return:
                            jump jumpTimeSkip
                        else:
                            jump jumpTimeStay

                    "Tell her to let you sleep.":
                        me "Please mom, I'm exhausted. Could you just let me sleep?"
                        "Mom sighs, then nods."
                        mom "Fine, I can't tell you what to do with your life. Just make sure you get into work on time."
                        "She steps out and closes the door behind her. Within a few minutes you're asleep again."
            jump jumpTimeSkip

label afternoon:
    scene bg house_afternoon
    with fade
    $ dayTime = 1
    $ slept_early = False
    menu:
        "Head to campus." if not weekend:
            jump campusAfternoon
        "Call in sick for work."if not weekend and not off_Work:
            jump homeSick
        "Spend the afternoon with Mom." if weekend:
            jump talkMom
        "See if Lily is home." if not sis_not_in_room:
            jump checkSister
        "Text Someone." if (not phone_call_made) and (has_alex_number or has_steph_number or has_nora_number):
            jump textScreen
        "Spend time on the internet.":
            jump internetBrowse
        "Take a nap.":
            jump night

label night:
    scene bg house_night
    with fade
    $dayTime = 2
    $ alex_beach_busy = False #Alexia gets back from the beach at this point.
    menu:
        "Spend the evening with Mom.":
            jump talkMom
        "See if Lily is home" if not sis_not_in_room:
            jump checkSister
        "Text Someone." if (not phone_call_made) and (has_alex_number or has_steph_number or has_nora_number):
            jump textScreen
        "Spend time on the internet.":
            jump internetBrowse
        "Head to bed early.":
            "You're feeling tired, so you head upstairs and go through your usual night time ritual."
            $ slept_early = True
            jump jumpTimeSkip

label jumpTimeSkip: #send anything here if it advances time at home.
    if dayTime == 0:
        call reset_period_trackers
        jump afternoon
    if dayTime == 1:
        call reset_period_trackers
        jump night
    if dayTime == 2:
        "Afterwards you decide it's time for bed."

        # check for serum events first
        if not maj_night_event_triggered:
            $ randChance = renpy.random.randint(0,1)
            if randChance == 0:
                if night_mom_drink_chance.check_event():
                    $ maj_night_event_triggered = True
                    scene bg house_night
                    with fade
                    jump momNightEncounter
                elif night_sis_drink_chance.check_event():
                    $ maj_night_event_triggered = True
                    scene bg house_night
                    with fade
                    jump sisNightEncounter
            else:
                if night_sis_drink_chance.check_event():
                    $ maj_night_event_triggered = True
                    scene bg house_night
                    with fade
                    jump sisNightEncounter
                elif night_mom_drink_chance.check_event():
                    $ maj_night_event_triggered = True
                    scene bg house_night
                    with fade
                    jump momNightEncounter

        # check for sleepover events
        if randChance == 0:
            if momO.slut_score > 30 and night_mom_sleepover_chance.check_event():
                scene bg house_night
                with fade
                "Some time during the night you're woken up by a soft knock at the door, then a creak as it's opened slightly."
                show mom night at right
                mom "[inputName], are you awake?"
                "You sit up in bed and rub your eyes."
                me "Uh, ya. What's wrong?"
                mom "Well, it's kind of embarrassing, but I'm having trouble sleeping. Do you think I could sleep with you tonight?"
                menu:
                    "Let her stay.":
                        call min_mom_sleep
                    "Tell her no.":
                        me "I don't sleep very well with other people in the bed, and I need to be alert tomorrow."
                        mom "Oh, of course. I'm sorry sweetheart."
                        me "It's okay. I hope you're able to get back to sleep. Maybe some tea or something would help."
                        #TODO: Major scene?
                        mom "I'll give that a try. Have a good night."
                        "She closes your door and you're fast asleep soon after."
                jump newDay
            elif sisO.slut_score > 30 and night_sis_sleepover_chance.check_event():
                scene bg house_night
                with fade
                #Lily events
                "Some time during the night you're woken up by a soft knock at the door, then a creak as it's opened slightly."
                show sis casual_night at right
                sis "Uh, [inputName]."
                "She whispers into the room. You sit up and rub your eyes."
                me "Uh, ya. What's wrong?"
                sis "I can't sleep, can I sleep in here?"
                menu:
                    "Let her stay.":
                        call min_sis_sleep
                    "Tell her no.":
                        me "I've got stuff to do in the morning Lily, I can't have you waking me up all the time. You'll just have to manage for tonight."
                        "Lily looks sad but nods."
                        sis "Okay, sorry I bothered you. Goodnight."
                        "She closes the door, and within a few minutes you're asleep again."
                jump newDay
        else:
            if sisO.slut_score > 30 and night_sis_sleepover_chance.check_event():
                scene bg house_night
                with fade
                #Lily events
                "Some time during the night you're woken up by a soft knock at the door, then a creak as it's opened slightly."
                show sis casual_night at right
                sis "Uh, [inputName]."
                "She whispers into the room. You sit up and rub your eyes."
                me "Uh, ya. What's wrong?"
                sis "I can't sleep, can I sleep in here?"
                menu:
                    "Let her stay.":
                        call min_sis_sleep
                    "Tell her no.":
                        me "I've got stuff to do in the morning Lily, I can't have you waking me up all the time. You'll just have to manage for tonight."
                        "Lily looks sad but nods."
                        sis "Okay, sorry I bothered you. Goodnight."
                        "She closes the door, and within a few minutes you're asleep again."
                jump newDay
            elif momO.slut_score > 30 and night_mom_sleepover_chance.check_event():
                scene bg house_night
                with fade
                "Some time during the night you're woken up by a soft knock at the door, then a creak as it's opened slightly."
                show mom night at right
                mom "[inputName], are you awake?"
                "You sit up in bed and rub your eyes."
                me "Uh, ya. What's wrong?"
                mom "Well, it's kind of embarrassing, but I'm having trouble sleeping. Do you think I could sleep with you tonight?"
                menu:
                    "Let her stay.":
                        call min_mom_sleep
                    "Tell her no.":
                        me "I don't sleep very well with other people in the bed, and I need to be alert tomorrow."
                        mom "Oh, of course. I'm sorry sweetheart."
                        me "It's okay. I hope you're able to get back to sleep. Maybe some tea or something would help."
                        #TODO: Major scene?
                        mom "I'll give that a try. Have a good night."
                        "She closes your door and you're fast asleep soon after."
                jump newDay
        jump newDay

label jumpTimeStay: #Send anything here if it keeps time where it is.
    if dayTime == 0:
        jump morning
    if dayTime == 1:
        jump afternoon
    if dayTime == 2:
        jump night

label talkMom:
    with fade
    show mom casual at right
    me "Hey mom."
    mom "Hi, how are you doing?"
    me "Pretty well, enjoying the new job and trying to make the most out of the experience."
    mom "That's a great attitude to have."
    menu:
        "Offer to split your paycheck with her." if not sharing_wage:
            "You and mom sit together for a few minutes."
            me "I know things have been tough around the house mom."
            mom "Oh, we'll make ends meet somehow. We always do."
            me "I know, but it would be easier for everyone if I could contribute a little bit. How about I give a little bit of my paycheck each week, to help with food and stuff."
            mom "You don't have to do that honey, I'm sure I can take care of it."
            me "Seriously, I want to help out. It's not fair that you work overtime to put me and Lily through school."
            "Mom looks at you and smiles."
            mom "That's very mature of you. Okay then, I would appreciate the help."
            "Mom gives you a hug and a peck on the cheek, and you spend some time talking about other things."
            $ sharing_wage = True
            jump jumpTimeStay
        "Spend some time with your mom.":
            "You take a seat beside Mom, joining her while she watches TV."
            call hub_mom
            if _return:
                jump jumpTimeSkip
            else:
                jump jumpTimeStay
        "Ask her how her day went." if not momO.report_number == 0:
            me "So Mom, how did your day go?"
            call min_mom_report
            $ momO.report_number = 0
            jump jumpTimeStay
        "Ask her to visit the beach with you." if momO.slut_score > 20 and beach_girl is None and beach_unlocked:
            if momO.beach_count == 0:
                me "Hey Mom, I heard that the beach is open for the summer now. I was thinking about taking a trip up there on Saturday, if you wanted to come along."
                mom "Would you be heading up there with anyone else?"
                me "I wasn't planning on it. I was hoping we could make it a mother son outing."
                "Mom thinks for a moment, then smiles and nods."
                mom "I don't have anything planned that day. It sounds like a great chance for us to spend some time together. I'll have to dig out my swimsuit!"
                me "Great. I'll see you on Saturday then."
                $ beach_girl = "Mom"
            else:
                me "Hey Mom, if you're free on Saturday I was thinking we could take a trip down to the beach. What do you say?"
                "Mom thinks for a moment, then smiles and nods."
                mom "Sure, I don't have anything planned. Looking forward to it [inputName]."
                $ beach_girl = "Mom"
            jump jumpTimeStay

        "Talk to her about her birth control." if momO.slut_score > 100 or (momO.slut_score > 70 and momO.cumslut):
            if momO.bc:
                me "Hey Mom, you're on the pill. Right?"
                if momO.cumslut:
                    mom "Yes, I am sweetheart. When we're playing around, you don't have to worry and can finish wherever you want."
                else:
                    mom "Yes, I am sweetheart. You don't have to worry about that."
                menu:
                    "Tell her to stop taking her birth control pills.":
                        $ momO.bc = False
                        me "I think you should stop taking them from now on. Could you do that for me Mom?"
                        if momO.cumslut:
                            mom "Well... I think I can, as long as you try not to finish inside me too much. I still want you to do it sometimes though, I love how it feels."
                            me "I'll make sure to save it for special occasions. Thank you Mom."
                        else:
                            mom "If it's really important to you, I can. Just make sure you don't end up getting me pregnant, okay?"
                            me "I promise I'll be extra careful Mom. Thank you."

                    "Don't do anything about her birth control.":
                        me "Okay, good. I just wanted to check."
                        mom "That's very responsible of you."

            else:
                me "Hey Mom, you haven't been taking your birth control lately, right?"
                mom "No, not since you told me to stop."
                menu:
                    "Tell her to start taking her birth control pills again.":
                        $ momO.bc = True
                        me "I think you should start taking them again, just in case we get carried away."
                        mom "If that's what you want, I'll start up again tomorrow. I guess it would look strange if you got your own mom pregnant."

                    "Don't do anything about her birth control.":
                        me "Okay, good. I just wanted to check."
                        mom "Do you like how risky it is? It gives me chills just thinking about it..."

            "You finish talking with your mom and leave her to watch TV."
            jump jumpTimeStay

        "Cancel your trip to the beach." if beach_girl == "Mom":
            me "Hey Mom, I've got something that came up on Saturday. I don't think I'll be able to head to the beach with you."
            mom "Oh, okay sweetheart. I hope you have fun doing whatever you'll be doing. Let me know if you want to reschedule."
            $ beach_girl = None
            jump jumpTimeStay

        "Watch a movie together." if weekend and dayTime == 2:
            me "Hey mom, it's been a long week for you. How about throw a movie on the TV and spend some time together?"
            mom "Sounds like a great idea [inputName]. I'll wash the dishes quickly, you go and ask your sister if she'd like to join."
            hide mom
            menu:
                "See if Lily wants to join you.":
                    "You head over to Lily's room and knock."
                    sis "It's open!"
                    show sis casual1 at right
                    sis "Hey, what's up?"
                    me "Me and mom are going to watch a movie, want to join us?"
                    "Lily checks her phone."
                    sis "Sure, my friends cancelled so I'm home for the evening. I'll be out in a few minutes."
                    hide sis
                    "You return to the living room and start scrolling for a movie you'd all like."
                    "Shortly after both Lily and mom join you, and you decide to watch a comedy."
                    show sis casual1 at left
                    show mom casual at right
                    "An hour passes with the three of you relaxing on the couch and laughing."
                    mom "Hey [inputName], I have a bottle of wine above the fridge. It's been a long week and I think we could all use a little drink. Would you mind pouring us all a glass?"
                    sis "Wine sounds great, thanks mom."
                    me "Sure. Back in a moment."
                    hide sis
                    hide mom
                    "Mom pauses the movie while you head to the kitchen. You find the bottle of wine and grab a glass for each of you."
                    call resistance_gain_report(movie_threesome_event_object,momO,sisO)
                    if (player_blue_serum + player_purple_serum + player_red_serum > 1):
                        menu:
                            "Pour some serum into their drinks.":
                                jump maj_spikeMovieDrinksThreesome
                            "Return with the drinks.":
                                "You decide to leave the girls drinks alone."
                    call min_mom_lily_movie
                    jump jumpTimeSkip
                "Pretend to get Lily, then say she's busy.":
                    "You head out of the kitchen and go upstairs, then wait a minute in the upstairs bathroom. Once enough time has passed you rejoin your mom in the living room."
                    show mom casual at right
                    me "She wasn't in her room. Maybe she already had plans."
                    "Mom shrugs."
                    mom "Guess it's just me and my boy then. Come on and lets figure out what we want to watch."
                    "The two of you sit on the couch together and scroll through movies, eventually deciding on a comedy."
                    "About an hour later, mom pauses the movie."
                    mom "[inputName], I've got a bottle of wine above the fridge. It's been a long week for me and could use a drink, would you mind grabbing me a glass? Feel free to take some for yourself too."
                    me "Sure, no problem. Back in a moment."
                    hide mom
                    "You find the bottle of wine in the kitchen and grab a glass for both of you."
                    call resistance_gain_report(mom_movie_event_object,momO)
                    if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                        menu:
                            "Pour some serum in her wine.":
                                jump maj_spikeMovieDrinksMom
                            "Return with the drinks.":
                                "You decide to leave mom's drink alone."
                    show mom casual at right
                    "You return with a glass of wine in each hand and give one to mom. She takes it and resumes the movie."
                    "As midnight rolls around you've both finished your wine and decide to head to bed."
                    jump jumpTimeSkip
    jump jumpTimeSkip

label checkSister:
    if sis_in_room or ((not sis_not_in_room) and sister_chance.check_event()):
        jump sisIn
    else:
        $ sis_in_room = False
        $ sis_not_in_room = True
        jump sisRoom

label sisTalk:
    show sis casual1 at right
    if (not sis_date_checked) and weekend and (dayTime == 1 or dayTime == 2) and date_chance.check_event():
        $ sis_date_checked = True
        show sis casual1 at right
        "You find Lily in her room, pouting at her phone."
        me "Hey Lily, how's it going?"
        sis "Right now? Kind of shitily actually."
        "She locks her phone and falls back on her bed with a dramatic sigh."
        me "What's up?"
        sis "Well, apparently I'm not worth the time of day to this douche bag. We had movie tickets, and he just bailed on me."
        me "Ouch, that sucks."
        sis "Know what's worse? Jackass didn't even want to pay for his own ticket, so I bought his for him. I was just about to get dressed up for this, and now I've wasted two tickets worth of money."
        "Lily groans and rolls over, then screams into her pillow."
        menu:
            "Offer to buy a ticket off of her. -$15" if player_money >15:
                $ player_money += -15
                me "You know, I didn't have any plans tonight. If you don't have anyone else who wants it, I'll buy the ticket off of you."
                "Lily sits up and looks at you."
                sis "You don't even know what movie it is."
                me "How bad could it be, you're willing to sit through it. Come on, there's no reason to waste the tickets if we've got some free time."
                "Lily considers it for a few moments."
                me "Come on, too \"cool\" to watch a movie with your brother now? I'm even offering to pay for it!"
                sis "Fine! Fine, you can have the ticket."
                "Lily smiles and gets the ticket from her desk."
                sis "If we don't want to be late we should head off soon. Give me a moment to get changed."
                "You head to your own room to get your stuff together while Lily gets ready."
                sis "Okay, lets go!"
                show sis casual2 at right
                "You meet up with Lily, who's put on a black and red dress for the evening."
                me "You look great sis."
                sis "Thanks. Not who I intended to wear this outfit for, but I'm not letting it go to waste."
                "The two of you catch a quick bus to the movie theater and head into the theater just as ads are ending. The theater is mostly full, and you're forced to take seats way at the back."
                sis "Damn, all the good seats are taken. At least it's empty up at the top."
                "As you sit down Lily turns and looks at you."
                sis "Hey [inputName], thanks for doing this for me. Tonight would have sucked otherwise."
                me "No problem Lily, just being a good brother."
                "You settle in for the movie, which turns out to be a romantic comedy. About half way through you're starting to get hungry, and decide to get some popcorn."
                me "Hey, I'm going to get some food."
                sis "Grab me a drink, would you?"
                hide sis
                "You nod, and head out the concession stand. You get yourself a bag of popcorn and Lily a small soda."
                call resistance_gain_report(sis_movie_event_object,sisO)
                if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                    menu:
                        "Pour some serum in her drink.":
                            jump maj_spikeMovie
                        "Leave her drink alone.":
                            "You decide to her drink as it is and return to the theater."
                show sis casual2 at right
                sis "Thanks. You missed a pretty good joke."
                me "Oh well, I'm sure I'll live without it."
                "A man a row below turns around and shushes you."
                me "Sorry."
                "You and Lily enjoy the rest of the movie, then catch a bus home."
                "When you get up to the door, Lily gives you a hug and a kiss on the cheek."
                sis "Thanks for being a perfect date."
                me "No problem. I get to pick the movie next time though."
                "Lily giggles, and you both head back inside."

            "Pass on the opportunity.":
                me "Damn, that really sucks then. Maybe you can find a friend or something to go with you."
                sis "Maybe. I'll call around and see what's up with people."
                "Lily sits up, looking defeated."
                sis "Could you go tell mom I'll be around for dinner?"
                me "Sure. I'm sure things will turn out alright."
                "Lily nods, and you head to the kitchen to find your mom and let her know."
                jump jumpTimeStay
    else:
        $ sis_date_checked = True
        "You find Lily in her room reading on her phone."
        show sis casual1 at right
        sis "Hey bro, what's up?"
        call hub_sis ## Leads to Lily's hub scene
        if _return:
            jump jumpTimeSkip
        else:
            jump jumpTimeStay

    jump jumpTimeSkip

label sisIn:
    if (not sis_in_room) and peep_chance.check_event():
        $ sis_in_room = True
        $ sis_not_in_room = False
        if sisO.slut_score > 25 and mast_chance.check_event():
            jump sisMast
        else:
            call min_sisPeep
            if _return:
                jump jumpTimeSkip
            else:
                jump jumpTimeStay
    else:
        $ sis_in_room = True
        $ sis_not_in_room = False
        jump sisTalk

label sisMast:
    "You crack your sister's door open and are about to say something..."
    #scene with her masturbating, looking away.
    show sis mast2 at right
    "She hasn't noticed you. Her dress is bunched up at her waist, and her right hand is pumping rhythmically into her slit."
    "You can hear her moan softly, and you've got a perfect view of her ass and vagina like this."
    #pics
    menu:
        "Step into the room.":
            call min_sis_mast_2
            jump jumpTimeSkip
        "Stay outside the room and stroke yourself while watching.":
            #pics
            "Lily drives two fingers in deep with one hand, while using the other to rub her clit as fast as possible. She bites into a pillow to keep from crying out."
            "You're rock hard, and there's no way she's going to notice you. You pull out your cock and start stroking it as fast as possible."
            if momO.slut_score > 40 and mom_mast_chance.check_event():
                call min_mom_catch
            else:
                call min_sis_mast_1
            jump jumpTimeSkip
            # "With nothing else to do, you head to your room and get yourself cleaned up."
            # jump jumpTimeSkip
        "Sneak away before anyone notices you were here.":
            "Not wanting to risk being caught, you step away slowly from the door. You can hear Lily's breath growing faster as you head for the living room."
            jump jumpTimeStay

label sisRoom:
    "You crack your sisters door open, but find no one inside. If you wanted to search around, you may be able to do it without anyone noticing."
    menu:
        "Search her drawers.": #TODO Add chance for Lily to catch you.
            call min_sis_search_room
        "Search her computer.":
            call min_sis_search_computer
    jump jumpTimeStay

label internetBrowse:
    "You start up your computer in your room, intending to spend a few hours on the internet."
    menu:
        "Play video games.":
            "Video games seem like the perfect way to relax. You lean back and browse through your list of games, ready to jump, shoot, and puzzle away a few hours."
            if (not weekend and dayTime != 2): #ie. middle of the day. You're skipping work or calling in sick.
                call min_sis_video_game
                jump jumpTimeSkip

        "Watch some porn.":
            "A man needs some sort of release, especially surrounded by beautiful women. You browse the internet and find something to your liking."
            $ randChance = renpy.random.randint(0,1)
            if randChance == 0:
                if (weekend or dayTime == 2) and mom_interrupt_chance.check_event():
                    "A short search and you find something that should do the trick. You put your headphones on and lean back, pulling your cock out before stroking it."
                    "A few minutes later you're startled by a sound at the door."
                    call min_mominterruptPorn
                elif sis_interrupt_chance.check_event():
                    "A short search and you find something that should do the trick. You put your headphones on and lean back, pulling your cock out before stroking it."
                    "A few minutes later you're startled by a sound at the door."
                    call min_sisinterruptPorn
                else:
                    "After a while you're finished and get everything cleaned up."
            else:
                if sis_interrupt_chance.check_event():
                    "A short search and you find something that should do the trick. You put your headphones on and lean back, pulling your cock out before stroking it."
                    "A few minutes later you're startled by a sound at the door."
                    call min_sisinterruptPorn
                elif (weekend or dayTime == 2) and mom_interrupt_chance.check_event():
                    "A short search and you find something that should do the trick. You put your headphones on and lean back, pulling your cock out before stroking it."
                    "A few minutes later you're startled by a sound at the door."
                    call min_mominterruptPorn
                else:
                    "After a while you're finished and get everything cleaned up."
            jump jumpTimeSkip

        "Check out Alexia's Site." if alex_porn_site: #Threesome with Lily or Steph show up here too?
            "You pull up the site Alexia sent you and check through her most recent and popular releases."
            call min_alex_porn_visit

        "Access the online biology journals." if has_online_code:
            "The username and password Nora gave you grants access to a wide range of scholarly journals you couldn't find before."
            "It would take years to learn everything here, but you only want to know about a little bit of it all."
            if not knows_blue_serum:
                "You're able to pull up information about the drug you read about before. It should temporarily shut down social normative expectations, during which time the subject is very vulnerable to suggestion."
                "These suggestions also tend to stay in place afterwards. With repeated doses and careful guidance the things a person finds acceptable and normal can be shifted."
                "Also included in one of the papers are detailed synthesis instructions. You're certain you could get this done at the lab, and it's such a simple process that you could probably get it done without anyone knowing."
                "Unfortunately, research into this particular drug was ended early because there was no easy transport mechanism. The immediate effects will be fairly minor and short term. The drug should be a vivid blue."
                "Finally, the paper notes that repeated uses of the drug in the same situations often had the opposite effect as intended. You'll have to make each dose count and not force the same situation more than once."
                "You write down the instructions on a notebook, you feel ready to try this next time you're at the lab."
                $ knows_blue_serum = True
            else:
                 "You browse the newest articles in case something new has been learned. Unfortunately no new research has been done, and there's nothing more for you to learn here."
        "Read through the research papers Stephanie sent you." if (has_research_papers and not knows_advanced_info):
            "You bring up the email Stephanie sent you, and begin wading into the information."
            "Most of it goes above your head, but you know enough about biology now that you can navigate to what you want to know."
            "A team in Germany is doing similar research as Nora and Stephanie, and are sharing their results with a tweaked version of the drug, delivered using an organic molecule carrier."
            "They claim to be seeing an increased effect from the drug, resulting in a more strongly disinhibited individual for longer periods of time."
            "The paper goes into extensive detail about the material requirements, but seems to be thin on actual information about its synthesis."
            "Perhaps it's still under development, or protected by a patent. Either way, you don't think there's enough information here to make any improvements without learning more."
            "It's clear, however, that you'll need several additional components that aren't normally stocked in the lab. You could purchase these yourself on the weekend, but it won't be cheap."
            "Secondly, the outline of the process seems far more complicated than before. If you're going to have any chance of making improvements before the end of the summer, you're going to need help in the lab."
            "Finally, each dose of this improved serum would require several of your old recipe as a precursor. Having easy and uninterrupted access to the lab would make this a lot easier to do."
            $ knows_advanced_info = True

        "Post to online science group asking for details." if has_advanced_papers and not knows_purple_serum:
            "With the new account Nora has set up for you you're able to log in to a small forum set up online for scientists around the world."
            "You make a post, avoiding the details of your work so far, and ask for details about further development of the drug you're using."
            "It doesn't take long before there are a few responses, asking for further details or clarifications."
            "For a few hours you work online with other scientists, trading unreleased papers with each other in an attempt to improve the drug."
            "Finally the group you've assembled thinks it has a potential modification to make. It would result in a less powerful effect, but should also reduce any side effects or backlash from the recipient."
            "It is also going to need more time in the lab, extra supplies, and someone who knows their chemistry far better than you do."
            if has_lab_assistant:
                "Stephanie should be able to help you make this new purple variation, as long as you bring her three doses of your blue serum and some extra supplies."
            else:
                "Getting help in the lab is going to be the next hurdle. If you can find help, all you will need is three doses of your blue serum and extra supplies to produce the purple variation of your drug."
            "You thank everyone for their help and promise to report back with your initial results."
            $ knows_purple_serum = True

    jump jumpTimeSkip

label morningBathroom:
    $ slept_early = False
    scene bg bathroom
    "With a good nights sleep you're able to get up a little earlier and beat your mom and sister to the main bathroom."
    menu:
        "Grab a shower.":
            jump bathroomShower

        "Search the counter.":
            # Leads to major scenes with mom and Lily.
            "You lock the door behind you and start to dig through the various items on the bathroom counter."
            # TODO: Add extra stuff to find, not nessesarily scene releated.
            "Most of the flat surfaces in the bathroom are covered with makeup supplies that your mom and sister use."
            "Your mom's mouthwash bottle set to one side, and underneath the counter you find a small tube of flavoured toothpaste. Lily can't stand mint toothpaste, so she keeps a special supply for herself separate from you and your mom."
            menu:
                "Look at Mom's mouthwash.":
                    "The mouthwash is brightly coloured already, and would probably wash out any signs of the serum. You could pour a cup for your mom now and leave it for her."
                    call resistance_gain_report(mom_bathroom_event_object,momO)
                    menu:
                        "Add serum to your mom's mouthwash." if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                            jump maj_mom_shower
                        "Leave the mouthwash alone and have a shower.":
                            jump bathroomShower

                "Look at Lily's toothpaste.":
                    "The toothpaste is already multicoloured; you could mix a dose of serum into the top portion so that it comes out the next time the tube is used."
                    call resistance_gain_report(sis_bathroom_event_object,sisO)
                    menu:
                        "Add serum to your sister's toothpaste." if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                            jump maj_sis_shower
                        "Leave the toothpaste alone and have a shower.":
                            jump bathroomShower

                "Leave everything how you found it and grab a shower.":
                    jump bathroomShower



label bathroomShower:
    # Leads to minor scenes with mom and Lily.
    "Happy to enjoy a shower with hot water for once, you strip down and get into the shower."
    if shower_interupt_check.check_event():
        if renpy.random.randint(1,2) == 1:
            #Mom comes in first
            call min_mom_shower
        else:
            #Lily comes in first
            call min_sis_shower
    else:
        "You enjoy a relatively long, very relaxing shower, then head back to your room and get ready for the day."
    jump jumpTimeStay


label homeSick:
    "You cough a few times to get in the mood, then find Nora's work number on your cell phone. After a few rings she picks up and you prepare your best sick voice."
    nora "Hello, you've reached Nora. How can I help you?"
    me "Hey Nora, it's [inputName]."
    "You cough for dramatic effect."
    me "I'm not feeling great, I think I picked up a cold or something. I don't think I'll be able to make it into work today."
    if days_Off_Work < 4:
        nora "You sound pretty bad. I'm sure we can reschedule a few things so nothing gets missed. Take as much time as you need to feel better."
        me "Thanks Nora, I'll get back as soon as I can."
        nora "Get well soon, bye."
        "Nora hangs up. You've got the day to yourself now."
        $ days_Off_Work += 1
        $ off_Work = True
        $ went_Work = True

    else:
        nora "Again? This is getting to be a pretty regular thing [inputName]."
        me "I know, it's been a bad summer for me I guess."
        nora "Well there's really nothing we can do without you today. If you really can't come in I'll let Stephanie know and we'll head home early. I'll have to dock your pay for the day though."
        menu:
            "Thanks, talk to you later.":
                me "Thanks Nora, I'll get back to work as soon as I can. Bye."
                "You hang up quickly, glad to be through the worst of it. At least you've got the day to yourself now."
                $ days_Off_Work += 1
                $ off_Work = True

            "Wait, I think I can make it.":
                me "I didn't realize I'd hold up everything. I'll struggle into work, sorry for bothering you."
                nora "If you think you're able to come in we really need you right now. See you soon."
                "You hang up. Looks like you aren't getting off of work that easily any more."

    jump jumpTimeStay


label orderSupplies:
    menu:
        "Order enough for one dose of serum. -$100" if player_money >= 100:
            "You hand the form back, and let the clerk know you're a lab assistant doing research."
            "A lab tech in the back assembles your order, and gives you a small bag with your supplies."
            $ player_money += -100
            $ player_serum_supplies += 1
        "Order enough for three doses of serum. -$250" if player_money >= 250:
            "You hand the form back, and let the clerk know you're a lab assistant doing research."
            "A lab tech in the back assembles your order, and gives you a bag with your supplies."
            $ player_money += -250
            $ player_serum_supplies += 3
        "Order enough for five doses of serum. -$400" if player_money >= 400:
            "You hand the form back, and let the clerk know you're a lab assistant doing research."
            "A lab tech in the back assembles your order, and gives you a large bag with your supplies."
            $ player_money += -400
            $ player_serum_supplies += 5
        "Order enough for ten doses of serum. -$750" if player_money >= 750:
            "You hand the form back, and let the clerk know you're a lab assistant doing research."
            "A lab tech in the back assembles your order, and gives you a backpack worth of supplies."
            $ player_money += -750
            $ player_serum_supplies += 10
        "Try and negotiate a better price.":
            "You put the form down and ask the clerk if there's something you can do to get a better deal."
            "The clerk rolls his eyes and tells you to come back when you're ready to pay cash."
            $ slut_available = False
            if momO.slut_score > 110 or (momO.freeuse and momO.slut_score > 80):
                $ slut_available = True
            elif sisO.slut_score > 100 or (sisO.freeuse and sisO.slut_score > 70):
                $ slut_available = True
            elif alexO.slut_score > 80 or (alexO.freeuse and alexO.slut_score > 50):
                $ slut_available = True
            elif stephO.slut_score > 90 or (stephO.freeuse and stephO.slut_score > 60):
                $ slut_available = True
            elif noraO.slut_score > 120 or (noraO.freeuse and noraO.slut_score > 90):
                $ slut_available = True
            if slut_available:
                menu:
                    "Call Mom and ask her to use her charms on the clerk." if momO.slut_score > 110 or (momO.freeuse and momO.slut_score > 80):
                        "You text Mom and ask her to meet you. A while later she shows up and agrees to show the clerk a good time."
                    "Call Lily and ask her to use her charms on the clerk." if sisO.slut_score > 100 or (sisO.freeuse and sisO.slut_score > 70):
                        "You text Lily and ask her to meet you. A while later she shows up and agrees to show the clerk a good time."
                    "Call Alexia and ask her to use her charms on the clerk." if alexO.slut_score > 80 or (alexO.freeuse and alexO.slut_score > 50):
                        "You text Alex and ask her to meet you. A while later she shows up and agrees to show the clerk a good time."
                    "Call Steph and ask her to use her charms on the clerk." if stephO.slut_score > 90 or (stephO.freeuse and stephO.slut_score > 60):
                        "You text Steph and ask her to meet you. A while later she shows up and agrees to show the clerk a good time."
                    "Call Nora and ask her to use her charms on the clerk." if noraO.slut_score > 120 or (noraO.freeuse and noraO.slut_score > 90):
                        "You text Nora and ask her to meet you. A while later she shows up and agrees to show the clerk a good time."
                "Half an hour later they both return looking dishevelled. She smiles and waves at you as she heads out the door, leaving you alone with the clerk."
                me "So, are you sure we can't work something out?"
                menu:
                    "Have enough for one dose of serum, on the house":
                        "You hand the form back, and let the clerk know you're a lab assistant doing research."
                        "A lab tech in the back assembles your order, and gives you a small bag with your supplies."
                        $ player_money += 0
                        $ player_serum_supplies += 1
                    "Order enough for three doses of serum. -$180" if player_money >= 180:
                        "You hand the form back, and let the clerk know you're a lab assistant doing research."
                        "A lab tech in the back assembles your order, and gives you a bag with your supplies."
                        $ player_money += -180
                        $ player_serum_supplies += 3
                    "Order enough for five doses of serum. -$275" if player_money >= 275:
                        "You hand the form back, and let the clerk know you're a lab assistant doing research."
                        "A lab tech in the back assembles your order, and gives you a large bag with your supplies."
                        $ player_money += -275
                        $ player_serum_supplies += 5
                    "Order enough for ten doses of serum. -$500" if player_money >= 500:
                        "You hand the form back, and let the clerk know you're a lab assistant doing research."
                        "A lab tech in the back assembles your order, and gives you a backpack worth of supplies."
                        $ player_money += -500
                        $ player_serum_supplies += 10
            else:
                "You wonder if he might be a bit more generous if you could offer him a good time."
                "It might be worth trying again when you've got a girl with high obedience or freeuse training."
                jump orderSupplies
    "You spend the rest of the day getting back home, and get through the door a few hours after sunset."
    call reset_period_trackers
    jump night

label campusMorning:
    scene bg campus_day
    with fade
    $dayTime = 0
    menu:
        "Alexia may be on campus, see if you can find her." if not skip_find_alex:
            $ skip_find_alex = True
            jump alexTalk
        "Head to the lab." if not off_Work:
            jump labMorning
        "Take a nap under a tree.":
            "You settle in for a nice nap, head propped up by your backpack. After a few minutes you're drifting off to sleep."
            jump campusNap
        "Take a bus home.":
            jump morning

label campusAfternoon:
    scene bg campus_afternoon
    with fade
    $dayTime = 1
    menu:
        "Alexia may be hanging around, see if you can find her." if not skip_find_alex:
            $ skip_find_alex = True
            jump alexTalk
        "Head to the lab." if not off_Work:
            jump labAfternoon
        "Take a nap under a tree.":
            "You settle down for a nap under the noon day sun, and soon you're drifting off to sleep."
            jump campusNap
        "Take a bus home.":
            jump afternoon

label campusNight:
    scene bg campus_night
    with fade
    $dayTime = 2
    menu:
        "Head over to the lab." if not off_Work:
            jump labNight
        "It's getting late. Go home for the night.":
            if alex_bus_chance.check_event():
                call min_alex_bus
            jump night

label campusJumpTimeSkip:
    call reset_period_trackers
    if dayTime == 0:
        jump campusAfternoon
    if dayTime == 1:
        jump campusNight
    if dayTime == 2:
        "You catch a bus home, and are asleep the moment you reach your bed."
        jump newDay

label campusJumpTimeStay:
    if dayTime == 0:
        jump campusMorning
    if dayTime == 1:
        jump campusAfternoon
    if dayTime == 2:
        jump campusNight

label campusNap:

    $ randChance = renpy.random.randint(0,1)
    if randChance == 0:
        if alex_nap_interrupt_chance.check_event():
            call min_alex_nap
        elif dayTime == 0 and steph_nap_interrupt_chance.check_event():
            call min_steph_nap
    else:
        if dayTime == 0 and steph_nap_interrupt_chance.check_event():
            call min_steph_nap
        elif alex_nap_interrupt_chance.check_event():
            call min_alex_nap
    jump campusJumpTimeSkip

label alexTalk:
    "You find Alexia near the campus cafeteria."
    me "Hey Alexia!"
    show alex casual at right
    alex "Hey [inputName]! Come join me, I was just planning on getting some food."
    menu:
        "Sure. I'd love to. How about we hit up the cafeteria. -$5" if player_money > 5:
            alex "Sure, lets go."
            "You and Alexia enjoy a meal at the cafeteria. You wish you could spend more time talking to her, but the crowd around you is just too loud for any sort of reasonable conversation."
            $player_money += -5
            alex "I didn't think it would be this crowded during the summer."
            if (dayTime == 0 or dayTime == 2) and has_lab_code:
                menu:
                    "Take Alexia to the lab.":
                        me "Actually, the lab I work in isn't far from here. We could go there and get away from the crowd. I'd love to show you around."
                        alex "Sure, that sounds cool."
                        "She takes a gulp from her drink, then stands up."
                        alex "Lets go!"
                        "You lead Alexia into the basement of the science building, weaving your way towards the lab."
                        alex "Whoa, how do you not get lost down here?"
                        me "Who said I don't sometimes?"
                        "She laughs as you come to the right door. You key in the door code and check inside. The lights are off, and you and Alexia slip inside and lock the door behind you."
                        scene bg lab_day
                        with fade
                        show alex casual at right
                        "Alexia wanders up and down the desks of equipment."
                        alex "Damn, this stuff is serious! What do you do here?"
                        if (dayTime == 0 and alex_steph_lab_check.check_event()):
                            me "Well we..."
                            "The code lock on the door beeps a few times, then the door swings open."
                            show steph work at left
                            steph "Oh, hey [inputName]. I didn't think you'd be in this early."
                            "Stephanie steps into the lab and closes the door. It takes her a moment to notice Alexia standing near the back of the room."
                            if steph_knows_alex:
                                steph "Hello again Alexia. [inputName], you know we aren't suppose to have anyone else down here."
                                me "Yeah, I know. What can I do to change your mind?"
                                steph "Well, if I were to come into possession of some ice cream, I might end up forgetting..."
                            else:
                                $ steph_knows_alex = True
                                steph "Hello, I don't think we've met."
                                me "Stephanie, this is Alexia. Alexia, this is Stephanie, she works with me down here."
                                alex "Nice to meet you Stephanie, this seems like a pretty sweet place down here."
                                steph "It's certainly an interesting job. Does Nora know you two are down here?"
                                me "I was just giving her a quick tour, I didn't think there was any harm to it."
                                steph "Well, technically speaking we aren't allowed to have any untrained personnel in the lab. But..."
                                me "But?"
                                steph "But, if I were to come into possession of some ice cream I might just happen to forget."
                                "She gives you a wink and sits down at her desk."
                            call resistance_gain_report(lab_alex_steph_event_object,alexO,stephO)
                            menu:
                                "Buy the girls ice cream. -$20" if(player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0) and player_money >= 20:
                                    $ player_money -=20
                                    jump maj_stephalexthreesome

                                "Leave the lab.":
                                    me "I would if I could, but I'm broke at the moment. Can I take a rain check on that?"
                                    steph "Sure, but I really can't let you two be down here."
                                    alex "Come on [inputName], we can go hang out somewhere else. I don't want you to get in any trouble."
                                    scene bg campus_day
                                    show alex casual at right
                                    "Alexia grabs your arm and pulls you towards the door. You lead her back up to ground level."
                                    alex "Hey, I've got class in a little bit and should probably get going if I want to get a good seat. We'll hang out some other time, okay?"
                                    me "Uh, sure. See you later Alexia."
                                    "She gives you a wave goodbye and starts to walk towards the center of campus."

                        else:
                            call resistance_gain_report(lab_test_object,alexO)
                            if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                                menu:
                                    "Demonstrate the effects of the serum.":
                                        jump maj_alexLabTest
                                    "Just some biology stuff.":
                                        "You can't actually tell her what you've been doing with your free time here."
                            me "Oh, biology stuff. Honestly the other lab people do most of the hard work, I just help out with the machines and keep things tidy."
                            alex "That's cool, I guess."
                            "You show Alexia some of the fancier machines, turn on a few and make the lights flash, and otherwise do your best to impress her."
                            alex "This has been a cool tour [inputName]. Thanks for showing me around."
                            me "No problem. If we get some other cool stuff in I'll invite you back."
                            alex "Sounds good, looking forward to it."
                            "She leans forward and gives you a kiss on the cheek."
                            alex "Now, I think I'm going to need help getting out of here."

                    "Stay in the cafeteria.":
                        me "Ya, it's crazy. We should go somewhere else next time."
                        "She nods, and the two of you finish your food."
                        alex "This has been nice [inputName]. We should do it again some time."
                        "Alexia smiles and waves as she heads out, pushing her way through the crowd."

        "Sure. How about we head to the new coffee place. My treat. -$12" if player_money > 12:
            alex "Sounds great, I've been meaning to head over there for a while now."
            "You and Alexia head away from the cafeteria. The coffee shop has a nice patio that opens onto a grass field. You can see a few university students throwing a frisbee back and forth, and someone is playing a guitar."
            me "This place looks nice."
            alex "Ya, it does. I'm glad you offered. We really should hang out on campus more often."
            "Alexia smiles at you warmly. The two of you walk up to the counter and order a pair of coffees and some sandwiches."
            $ player_money += -12
            alex "The day looks great, lets sit outside."
            "You grab a table at the edge of the patio and sit down."
            alex "So, what are you doing around campus?"
            me "Nothing much. I've got a research assistant job over the summer so I'm here throughout the week."
            alex "Nothing much? That's plenty much! I'm very impressed [inputName]."
            me "Thanks, it's really not that impressive though."
            "Alexia takes a large sip of her coffee."
            alex "Ah! Damn!"
            "She puts the coffee down carefully and holds a hand up to her mouth."
            me "Too hot?"
            alex "Way too hot!"
            me "You should go get a cold drink or something, you don't want your tongue swelling up."
            alex "Does that even happen?"
            me "I don't know, but better safe than sorry."
            "Alexia stands up and turns around."
            alex "Just wait here, I'll be back in a moment!"
            hide alex
            "She runs off back inside the coffee shop."
            call resistance_gain_report(coffee_event_object,alexO)
            if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                menu:
                    "Pour some serum into her drink while she's gone.":
                        jump maj_spikeDrink
                    "Leave her drink alone.":
                        show alex casual at right
                        "Alexia comes back a few minutes later."
                        alex "Whew, some cold water definitely helped. I hope it's a more reasonable temperature now!"
                        "The two of you enjoy your drinks together, and talk about your experiences over the last few years."
                        "Eventually you both finish your drinks and food."
                        alex "This was great [inputName]. I hope we can get drinks together again some time."
                        me "Me too, talk to you later Alexia."
        "I'm dead broke right, maybe next time though.":
            if alexO.slut_score < 60 or not alex_porn_site:
                alex "Oh, no problem. Maybe you can join me next time then."
                "Alexia moves off into the crowd."
                jump campusJumpTimeStay
            else:
                alex "Oh, no problem. Maybe later then."
                "Alexia starts to head away, then stops."
                alex "Wait, I might have a deal for you then. I need something to post to my site tonight. Would you like to help me out?"
                menu:
                    "Help her out.":
                        call min_alex_porn_help

                    "Not right now.":
                        me "Sorry Alexia, I'm really busy right now. Maybe some other time though."
                        "Alexia pouts, but nods. You wave goodbye and leave."
                        jump campusJumpTimeStay

        "Ask to tag along and hang out.":
            me "I just grabbed something, but I'll tag along if you'd like some company."
            alex "Sure, I'd love some company."
            "Alexia gets her food and the two of you find a seat. You chat about nothing in particular while she eats."
            me "So, any plans for today? I've got some time to kill if you'd like to hang out."
            alex "Nope, no plans until later. There's a lecture hall around here that's always empty, I normally go there and watch a movie or something on the projector. Feel like coming along?"
            me "Sounds good to me. Lead the way."
            "Alexia cleans up her stuff and leads you to a different building, down into the basement, and into a small lecture hall. She walks up to the front of the room and starts up the computer."
            alex "Well, here we are."
            call hub_alex
            if _return:
                jump campusJumpTimeSkip
            else:
                jump campusJumpTimeStay

        "Ask for her phone number so you can meet up later." if alexO.slut_score > 10 and not has_alex_number:
            me "Alright, sounds good. I'm a little busy right now, but maybe we can get together some other time."
            alex "Sure, whenever you're free."
            me "You know, I don't actually have your phone number. We should swap, so we can get together some other time."
            "Alexia smiles and pulls her phone out of her pocket. You do the same and you both pull up new contact pages for each other, then swap phones. A minute later you're both done."
            alex "Great, talk to you later then [inputName]."
            me "Definitely, talk to you later."
            "Alexia heads off into the crowd. You check your phone; she's entered herself in as \"Alexia ;)\""
            $ has_alex_number = True
            jump campusJumpTimeStay

    jump campusJumpTimeSkip

label textScreen:
    "You flop down on the couch and pull out your phone and browse through your contacts."
    $phone_call_made = True
    menu:
        "Text Alexia." if has_alex_number and not alex_beach_busy:
            jump alexText
        "Text Stephanie." if has_steph_number:
            jump stephText
        "Text Nora." if has_nora_number:
            jump noraText

label alexText:
    "You pull up Alexia's number."
    menu:
        "Ask how she's doing.":
            me "Hey Alexia. Figured I'd say hi and see how you're doing. Everything's cool with me." #TODO text shortening/misspelling since it's text? Phone icon?

            if (not weekend) and test_chance.check_event():
                alex "Oh hey [inputName], kind of stressed out actually."
                me "What's going on?"
                alex "There's a test tomorrow, and I'm feeling totally fucked."
                me "Damn, that sucks. What subject?"
                alex "Chemical Structures for Bio students. It sucks a big one."
                "You've taken the engineering version of that class and got an A last year."
                menu:
                    "Invite her over to study in person.":
                        me "I took that course last year and got a pretty good mark. If you're able to come over I could help you out."
                        "There's a long pause. You can see Alexia write and erase a message several times. Finally she sends something."
                        alex "That would be a life saver, thank you so much. What's your address?"
                        "You text your address to her, then rush upstairs and clean your room up as much as possible while she drives over."
                        "Just as the last article of dirty clothes are shoved into the laundry room out of sight the doorbell rings. You rush to the door, take a second to catch your breath, then open it."
                        show alex casual at right
                        alex "Hey! Thanks again [inputName]."
                        "She comes forward and gives you a hug."
                        me "No problem, I cleared my desk off for us upstairs."
                        "You guide Alexia upstairs and into your room, where you both take a seat. Alexia pulls out a textbook and notepad and drops them on the desk."
                        alex "Okay, so this is where I've gotten so far. Section 4 makes literally no fucking sense though and I want to kill someone."
                        "You read part of the text book, then get up and get your old book from last year. Between the two sources you two begin making quick progress through the problems."
                        "After a finishing the section you both sit back and sigh."
                        me "There, only one more section to go and you should be good."
                        alex "Even if we don't get that far I don't think I'll fail. I'll settle for a D right now."
                        if (alexO.slut_score > 20):
                            "She turns to you and winks."
                            alex "Not just any D though, only the one you helped me get."
                            "She laughs, and you join her."
                        me "Well, we deserve a reward after all that. Would you like a drink?"
                        alex "No drink for me. I brought my own water bottle, and I can't have anything else 'cause I'm driving. Do you guys have any snack food though, popcorn or something?"
                        me "I think so, I'll check in the kitchen. Back in a few."
                        hide alex
                        "You head down stairs to the kitchen and start looking for snacks. Eventually you find a half eaten bag of popcorn and pour some into a bowl."
                        call resistance_gain_report(test_studying_object,alexO)
                        menu:
                            "Try putting some serum into her popcorn." if player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0 :
                                jump maj_alexStudy
                            "Leave the snacks alone.":
                                "You leave the popcorn bowl alone and head back up to your room."
                                me "Here you go."
                                alex "Awesome, thanks. A quick snack then we can finish up."
                                "The popcorn is a little stale, but you enjoy each others company and laugh about school work. Eventually you get back to work, and finish off the next section as well."
                                alex "[inputName], I can't thank you enough. You've saved my ass."
                                me "It's an ass worth saving. It's really just self interest."
                                "She laughs and punches you playfully in the shoulder."
                                alex "Well good, my ass is in your hands then."
                                if alexO.slut_score > 30:
                                    show alex strip14 at right
                                    "She turns around and bends over for you, lifting her skirt up."
                                    alex "See?"
                                    show alex casual at right
                                    "You give her ass a solid smack, and she laughs and stands back up."
                                "She gives you a quick peck on the cheek and thanks you one last time, then is out the door and in her car. You watch from the door while she drives away."

                    "Text her help with the practice problems.":
                        me "I took that class already, I can help you out with some of the problems. Just send me some pictures."
                        alex "Seriously?"
                        me "Ya, of course."
                        call min_alex_nudes
                        jump jumpTimeStay

            else:
                if (weekend and (dayTime == 0 or dayTime == 1)):
                    alex "Hey [inputName]. Things are pretty okay here, just getting ready to go out for a while."
                    me "Oh ya, what are you doing?"
                    alex "Some shopping, I'm looking for a new outfit for the summer."
                    alex "If you're not doing anything you're welcome to tag along."
                    menu:
                        "Join Alexia at the mall.":
                            me "Sounds like fun, I'll meet you there in thirty?"
                            alex "Sure, entrance three."
                            scene bg mall
                            show alex casual at right
                            "You get your stuff together and head out the door. A quick bus ride gets you to the mall, and you're able to find Alexia without any problems."
                            alex "Hey, glad you could make it."
                            me "Me too, it's nice to hang out together."
                            "She smiles and waves her hand to the mall."
                            alex "Somewhere, hidden in there, is a kick ass outfit for me. Think you can help me find it?"
                            me "I'll do my best. Lead the way."
                            "Alexia leads you through the mall, stopping at a few stores to look at different clothes. For the most part you chat about other stuff, like school or work."
                            "An hour passes, when Alexia stops."
                            alex "Man, we've been doing a ton of walking. Lets grab some bubble tea, my treat."
                            me "Sure thing, lead on."
                            "You swing by the food court and grab your drinks, then get back to shopping. As you approach the next store Alexia wants to check out, she stops and looks at the half finished drink."
                            alex "Crap, they won't let me inside with this. Do you think you could hold onto it for me, I'll just be a few minutes."
                            me "Sure, I'll wait out here for you."
                            alex "Sweet, thanks [inputName]."
                            hide alex
                            "Alexia hands you her drink and heads into the store."
                            call resistance_gain_report(mall_event_object,alexO)
                            if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                                menu:
                                    "Pour some serum into her drink while she's gone.":
                                        jump maj_spikeMallDrink
                                    "Leave her drink alone.":
                                        "You decide against doing anything to her drink."
                            show alex casual at right
                            "After a few minutes Alexia emerges from the store and takes her drink back."
                            alex "Thanks. They didn't have anything interesting in there anyway."
                            "You walk around for a little while longer, but Alexia seems to have exhausted all of her options."
                            alex "I guess it's just not meant to be. Maybe we'll come back some other day and see what they have again. I'd love for you to come along, if you want."
                            me "I'd love to, I had a great time."
                            alex "Excellent. Text me on the weekend and we can make plans."
                            "You walk to the bus stop together, then catch different busses home."
                        "Back out.":
                            me "Sorry Alexia, I've got plans for today. Maybe some other time though."
                            alex "Sure, whenever you're free. Maybe next weekend."
                            me "Sounds good. Talk to you later."
                            alex "Bye!"
                            jump jumpTimeStay
                else:
                    alex "Hey [inputName]. Things are pretty okay here, just watching some youtube stuff."
                    "You and Alexia trade messages back and forth for a little while before she has to head off."
                    jump jumpTimeStay

        "Flirt with Alexia.":
            me "Hey Alexia, how are you doing?"
            alex "Hey! I'm doing pretty good, just relaxing at home right now. How about you?"
            me "Better now that I'm talking to you. I've been feeling a little lonely."
            call min_alex_porn_start
            jump jumpTimeStay

        "Ask her to visit the beach with you." if alexO.slut_score > 20 and beach_girl is None and beach_unlocked:
            if alexO.beach_count == 0:
                me "Hey Alexia. I just found out that the beach was opened up to the public for the summer. I'm planning to head up there this Saturday, and I was wondering if you wanted to come along."
                alex "A trip to the beach? Sound awesome! Count me in! How do we get up there?"
                me "There's a direct bus that runs in the morning and afternoon. It should make travel super easy."
                alex "Great! I guess I'll talk to you then."

            else:
                me "Hey Alexia, I was going to head up to the beach this Saturday. You interested in comming along again?"
                alex "Yeah, I don't have anything going on. I'll get my swimsuit out again."
                me "Cool, talk to you then I guess."

            $ beach_girl = "Alex"
            jump jumpTimeStay

        "Cancel your trip to the beach." if beach_girl == "Alex":
            me "Hey Alexia. Hate to tell you this, but something came up on Saturday. I'm going to have to take a rain check on the beach trip."
            alex "Darn, that sucks. If you're free next weekend let me know and we can go then instead."
            me "Sure thing. Talk to you later."

            $ beach_girl = None
            jump jumpTimeStay

    jump jumpTimeSkip

label stephText:
    "You pull up Stephanie's number."
    menu:
        "Ask how she's doing.":
            if steph_party.check_event() and dayTime == 2 and (day%7 == 6 or day%7 ==5): #ie. Friday or Saturday night.
                me "Hey Steph, how's it going?"
                steph "Hey, you have great timing! I just got word from a friend. Want to come out to a party with me tonight?"
                menu: #TODO bring Lily or Alexia with you to the party.
                    "Sure!":
                        me "I'd love to, where should I meet you?"
                        "Stephanie sends you an address and a time."
                        steph "I've got to go get ready. See you soon!"
                        "You get ready, check the bus schedule, and head out. It doesn't take long before you're walking up to a house matching the address."
                        "You knock on the door, and it's opened by a blonde girl you haven't seen before."
                        me "Hey, I'm here with Stephanie."
                        "Blonde Girl" "Hey, come in. She just got here!"
                        "The music past the door is loud and bass heavy. People are hanging out in groups of two or three, talking, dancing, or drinking."
                        "Blonde Girl" "Hey Steph, your friend made it!"
                        "The blonde girl leads you through the house into what looks like the living room."
                        show steph casual at right
                        steph "[inputName]! Glad you made it!"
                        "Stephanie steps away from a table of drinks and gives you a hug."
                        me "Hey Stephanie. Hope I'm not running late."
                        steph "Late? We're just getting started here!"
                        "She picks up a drink and hands it to you, then takes one for herself."
                        steph "Come on, I'll show you around."
                        "Stephanie takes you by your free hand and starts leading you around the house. She introduces you to a few people, who's names you quickly forget."
                        "After a while you end up back in the living room."
                        steph "I need to run to the little girls room. Keep an eye on my drink. When I get back we're going to dance!"
                        hide steph
                        "Stephanie presses her drink into your hand and moves through the sparse crowd to the bathroom."
                        call resistance_gain_report(steph_party_event_object,stephO)
                        menu:
                            "Spike her drink.":
                                jump maj_stephParty
                            "Leave her drink alone.":
                                "You stand around awkwardly for a few minutes until Stephanie gets back."
                                show steph casual at right
                                steph "Much better. Now lets go, you look so lonely all by yourself." ##Good minor scene territory
                                "When the song changes Stephanie pulls you to the center of the room. She puts her arms up and starts to dance, singing along with the music."
                                "You do your best to keep up, but it's clear Stephanie is a much better dancer than you are. After a few songs you're out of breath and have to step away."
                                "For the rest of the evening you chat with Stephanie and enjoy yourself by drinking and partying."
                                "As the night wears on the party shows no signs of stopping, but you're beginning to get worn out. You find Stephanie to say your goodbyes, then head out and catch a bus home."

                    "Back out.":
                        me "Damn, I'd love to but I've got other stuff going on tonight. Maybe some other time, okay?"
                        steph "Sure, no problem. I've got to head out, see you at work on Monday then!"
                        jump jumpTimeStay
            else:
                "You and Stephanie exchange a few texts about work and school."
                me "So, anything exciting going on with you?"
                steph "A few of my friends are putting together a party in a little while, which should be sweet. If you want to come you're invited."
                me "Nice, when is it?"
                steph "They aren't sure yet. They basically just make it up as they go along anyway. If they get their act together either Friday or Saturday night."
                steph "Send me a text then if you're interested, and I'll check with them to see if it's still happening."
                me "Cool. Looking forward to it."
                steph "Me too! I don't get to go out as much as I use to, work's keeping me busy."
                "After a little while the two of you say goodbye."
                jump jumpTimeStay

        "Ask about playing tennis." if day%7 == 0 and dayTime == 0: #ie only Sunday Morning
            me "Hey Steph. I was wondering if your tennis offer still stands."
            steph "Hey! Of course, I can send you the address."
            steph "Do you have your own equipment?"
            #TODO add ability to buy tennis equipment.
            me "Nope, can I rent stuff there?"
            steph "Ya, I'll send you the link to their website. I'm just about to head out, see you soon?"
            menu:
                "Rent equipment and join her. -$30" if player_money >= 30:
                    $player_money += -30
                    me "Yep, I'm on my way now. See you soon."
                    "You get changed into your best sporting clothes and head out. After half an hour on a bus and a short walk you're at the tennis center Stephanie told you about."
                    "You head inside and talk to the rental person. They give you a proper pair or shoes and a racket, and you meet Stephanie in the lobby."
                    show steph sport at right
                    steph "Hey, glad you made it!"
                    me "Hey Stephanie. Glad I could come too."
                    steph "So it's pretty dead this time of day, we've got our pick of the courts outside."
                    me "Well, I don't exactly play tennis much. Is there a quiet one where I won't embarrass myself so much?"
                    "Stephanie laughs and starts leading you outside."
                    steph "Sure, there's one beside the building that's all by itself. It's fenced in on three sides, and nobody likes it because the light isn't great."
                    me "Thanks. I'd rather not get crushed in public."
                    "Stephanie leads you to the side of the building and drops her gear off at the side of the court."
                    steph "Okay, lets get started then, shall we?"
                    "She does a few warm up stretches, then takes her place on the far side and the two of you start rallying back and forth."
                    "After a few minutes, it's clear she's going easy on you and not trying very hard to win."
                    steph "So where did you learn to play?"
                    me "Back in highschool, we did a single unit on tennis in gym class."
                    steph "Well then you aren't too bad. At least we're getting some good exercise."
                    "You play tennis for a few more minutes. You're starting to get the hang of it, but Stephanie is barely winded. After an exchange she stops to take a break."
                    steph "Did you bring a drink?"
                    me "Damn, I didn't even think about it."
                    steph "No problem, I'll run in and grab you one. My treat, for coming all this way to hang out."
                    me "Thanks, I'll wait here and catch my breath."
                    hide steph
                    "Stephanie jogs around the corner of the building, leaving her own water bottle sitting beside her gear."
                    call resistance_gain_report(steph_tennis_event_object,stephO)
                    menu:
                        "Pour some serum into her waterbottle." if(player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                            jump maj_tennisSpike
                        "Wait for her to get back.":
                            "After a few minutes Stephanie comes back and throws you a cold bottle of water."
                    show steph sport at right
                    steph "Here you go. Ready to keep going?"
                    "You chug some water and put it to the side, then nod."
                    "You and Stephanie spend the rest of the morning chatting and getting some good exercise. Eventually both of you are tired, and decide to call it a day."
                    steph "I had a good time, send me a message if you want to do this again. If you like it you could even get your own equipment."
                    me "It was fun, definitely a good workout. I'll send you a message if I've got some spare time next week."
                    "Stephanie smiles and waves goodbye while you go and catch a bus home."
                "Back out.":
                    me "Ouch, the price is a little steep."
                    steph "Ya, I get free court time, but the rental costs suck."
                    me "I'll have to give it a miss for this week then. Maybe once I get my paycheck."
                    steph "Sure, hit me up when you're able."
                    jump jumpTimeStay
        "Flirt with Stephanie.":
            me "Hey Stephanie, how's it going?"
            steph "Pretty good, how about you?"
            me "Better now that I'm talking to you. You always find a way to make me smile."
            call min_steph_nudes
            jump jumpTimeStay

        "Ask her to visit the beach with you." if stephO.slut_score > 20 and beach_girl is None and beach_unlocked:
            if stephO.beach_count == 0:
                me "Hey Stephanie. I just heard the beach is open for the summer, I'm planning to head up there on Saturday if you want to come along with me."
                steph "Ooh, the beach. Sounds like a lot of fun. I'll pull out my swimsuit and get ready for it then. Thanks for the invite!"
                me "No problem. See you then."
            else:
                me "Hey Steph. I'm planning another trip up to the beach if you want to come along."
                steph "Sounds great. Saturday again?"
                me "Yeah. See you then."
            $beach_girl = "Steph"
            jump jumpTimeStay

        "Cancel your trip to the beach." if beach_girl == "Steph":
            me "Hey Steph. Something came up on Saturday, so I'm going to have to cancel our trip to the beach."
            steph "Damn, okay. Let me know if you want to reschedule."
            me "Will do, talk to you later."
            $ beach_girl = None
            jump jumpTimeStay

    jump jumpTimeSkip

label noraText:
    "You pull up Nora's number."
    menu:
        "Ask how she's doing.":
            #On the weekend, morning or afternoon, she needs help moving stuff sometimes. (New housework outfit?)
            #Low slut, you help and she thanks you (Major scene here in the future? TODO)
            #Medium slut, she wants to show off her lingerie to you after you're done. Thankyou blowjob.
            #High slut she wants to "thank you" somehow before you even do the job.
            if weekend and (dayTime == 0 or dayTime == 1) and moving_chance.check_event():
                nora "Hey [inputName]. Doing well here. I've got some house work I'm doing. Moving some furniture right now."
                me "Sounds like hard work."
                if noraO.slut_score < 40:
                    nora "It's a little difficult with only one person. I don't suppose I could buy your services in exchange for a pizza."
                    menu:
                        "Agree to help.":
                            call min_nora_housework_1
                            jump jumpTimeSkip
                        "Back out.":
                            me "Ah, sorry Nora. I'm busy right now. Maybe some other time though."
                            nora "Okay, no problem. I should get back to work then. Have a good weekend."
                            me "You too."
                            jump jumpTimeStay
                elif noraO.slut_score < 85:
                    nora "Well I'm here all by my self. I think I might need help moving everything. I don't suppose I could get your help in exchange for a reward?"
                    me "And what kind of reward would that be?"
                    nora "You'll just have to come over and find out."
                    menu:
                        "Agree to help":
                            call min_nora_housework_2
                            jump jumpTimeSkip
                        "Back out.":
                            me "Sorry Nora, but I'm busy right now. Maybe some other time."
                            nora "Okay, no problem. Have a good weekend."
                            me "You too."
                            jump jumpTimeStay
                else:
                    nora "It is. I'm all by myself here, and I could really use some help. I promise to make it worth your time if you come over and lend a hand."
                    menu:
                        "Agree to help.":
                            call min_nora_housework_3
                            jump jumpTimeSkip
                        "Back out.":
                            me "Sorry Nora, but I'm busy right now. Maybe some other time."
                            nora "Okay. I hope you have a good weekend then."
                            me "You too."
                            jump jumpTimeStay
            else:
                "You ask how Nora's doing. She takes a while to respond, then says she's busy and you'll have to talk later."
                jump jumpTimeStay

        "Ask for some biology studying help.":
            "You head upstairs and pull up some biology textbooks to read through. After finding a few interesting questions you send a text to Nora asking for her help solving them."
            if weekend and (dayTime == 0 or dayTime == 1) and study_chance.check_event():
                "Nora takes a long while to respond, and you begin wondering if you're just being ignored."
                nora "Huh, I can't figure this out here."
                me "Glad it's not just me then. They looked tricky."
                "Another long pause before she responds."
                nora "I don't have anything going on today, and those problems actually look interesting. If you're serious about figuring them out we could meet up."
                menu:
                    "Invite her over to help you study.":
                        me "I've got the day free, so you're welcome to come over."
                        nora "Okay, I'll grab some books."
                        "You send Nora your address, and she tells you she'll be there in about twenty minutes."
                        "You rush to get a study space set up, then let mom know that you're having a guest from work come over."
                        "By the time everything is arranged the doorbell rings. You open the door and let Nora in."
                        if nora_schoolgirl_check.check_event() and noraO.exhib and noraO.slut_score > 80: #She shows up in a slutty schoolgirl outfit.
                            call min_nora_schoolgirl
                            jump jumpTimeSkip
                        else:
                            me "Hey Nora, glad you could make it."
                            show nora casual at right
                            nora "Thank you [inputName], where should we sit?"
                            menu:
                                "Study in your room.":
                                    me "There are a few chairs upstairs. I hope you don't mind the mess."
                                    nora "No, it's fine. As long as we have a table, some pens, and some paper we should be able to make it work."
                                    "You show Nora to your room and close the door. The two of you take a seat by your desk and she opens up one of her books."
                                    nora "So I found the question you were looking at, but I think my edition is an older one. A few things were changed, but it might lead us in the right direction."
                                    "You and Nora talk about the problem for a while, trying to figure out how to approach it. Nora is the one with most of the ideas, you're just trying to keep up."
                                    "After half an hour of hard work she pauses."
                                    nora "[inputName], do you think I could get some water? All this talking is drying my throat out."
                                    me "Sure, back in a moment."
                                    hide nora
                                    "You head downstairs to the kitchen and get a glass of water for Nora."
                                    call resistance_gain_report(nora_study_event_object,noraO)
                                    if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                                        menu:
                                            "Pour some serum in her water.":
                                                jump maj_noraStudySpike
                                            "Leave her drink alone.":
                                                "You decide to leave her drink be."
                                    show nora casual at right
                                    "When you get back upstairs you place the drink down and get back to work."
                                    nora "Thanks. I had an idea, if we assume this is kept constant..."
                                    "After another hour of work you've finished the problem. Nora seems excited, but you're completely exhausted."
                                    nora "Well thank you [inputName], that was a fun one to figure out. We got there eventually though."
                                    me "Yep, we finally managed."
                                    "Nora collects her stuff and heads to the door. You wave goodbye, then head back inside."

                                "Study in the dining room.":
                                    me "There's plenty of space in our dining room. We can get set up there."
                                    nora "Excellent. It's important to have plenty of space to work with."
                                    show mom casual at left
                                    "Nora sets her books down and you get to work on the problems. A few minutes later mom walks into the room."
                                    mom "Hello, you must be Nora."
                                    "Nora stands up and shakes your mom's hand."
                                    nora "I am, a pleasure to meet you..."
                                    mom "Jennifer. It's so nice for you to take time out of your day to help [inputName]."
                                    nora "Oh it's no problem at all, he found some very interesting questions that I wanted to work on. He seems really invested in learning this himself."
                                    mom "Well that's good to hear. Would you like a glass of wine, or something else? I'd love to sit down and have a chat, if you don't mind the interruption."

                                    if mom_join_chance.check_event():
                                        nora "That sounds great actually. We've hit a dead end here, I think we could both use a break."
                                        mom "A perfect time to talk then. [inputName], there's some wine in the kitchen, above the fridge. Would you get it down and pour a drink for me and Nora?"
                                        me "Sure. Back in a moment."
                                        hide mom
                                        hide nora
                                        "You find the wine easily enough and pour two glasses."
                                        call resistance_gain_report(nora_mom_study_event_object,noraO,momO)
                                        if (player_blue_serum + player_purple_serum + player_red_serum > 1):
                                            menu:
                                                "Pour some serum in the wine.":
                                                    jump maj_noraMomThreesome
                                                "Leave their drinks alone.":
                                                    "You decide to leave their drinks be."
                                        "Wine in hand you return to find the two women deep in conversation."
                                        show mom casual at left
                                        show nora casual at right
                                        nora "Thank you [inputName]."
                                        mom "Thank you."
                                        "You join them for a while, but they seem perfectly content to talk to each other. About an hour passes before mom looks at her watch."
                                        mom "Look at the time, I've been keeping you from your work all day."
                                        nora "Oh that's fine. I don't think we were going to make any progress. I'm starting to think it was a misprint in the book anyway."
                                        mom "Well I'll let you two get back to it."
                                        nora "Actually, I think I need to be heading out. It was great having a chat with you Jennifer."
                                        mom "You're welcome here any time you want."
                                        "Nora collects her books and heads to the door. You wave to her as she leaves, then head back inside."
                                    else:
                                        nora "Nothing for me right now, thank you. I think we've just about finished this problem, so I'd like to finish it before we get distracted."
                                        mom "Of course, I should let you two get to work."
                                        "Mom heads out of the room, and you and Nora get back to work."
                                        "After an hour of work you've finished all the problems. Nora seems excited, but you're exhausted."
                                        nora "Well thank you [inputName], that was fun. Keep an eye out for any more like that, and let me know if you find some."
                                        me "Sure, will do."
                                        "You walk Nora to the door and wave goodbye, then head inside."
                    "Back out.":
                        me "I'm busy today, so I can't spend much more time on them. Maybe I'll work on it some other night."
                        nora "Okay. Thank you for the interesting problems, I'll see if I can solve them myself and send you the answers."
                        jump jumpTimeStay
            else:
                "A few minutes later Nora texts back a few hints for them, and an explanation of the principles you should know."
                "Beyond that, Nora doesn't seem to have time to help."
                jump jumpTimeStay

        "Flirt with Nora.":
            if (dayTime == 2 and not weekend): ## Nora public scene here. Call her and listen/watch while she fucks someone.
                me "Hey Nora, how's it going?"
                "There message shows it's been delivered and read. After a long pause there's a response."
                if nora_pull_over.check_event() and noraO.freeuse:
                    call min_nora_pull_over
                else:
                    call min_nora_nudes
            else:
                "You try and send a few flirty messages to Nora, but after a long wait she tells you she's busy."
            jump jumpTimeStay

        "Ask her to visit the beach with you." if noraO.slut_score > 35 and beach_girl is None and beach_unlocked:
            if noraO.beach_count == 0:
                me "Hey Nora. I'm planning a trip out to the beach this Saturday and wanted to invite you along."
                "There's a delay of a few minutes before Nora responds."
                nora "It's been forever since I was out to the beach. I'm glad it's finally opened again. Count me in, I'll dig out my swimsuit."

            else:
                me "Hey Nora. I'm planning another trip out to the beach on Saturday, if you want to come along."
                "There's a delay of a few minutes before Nora responds."
                nora "Sounds great, I'll get my stuff ready. Looking forward to it."
            $beach_girl = "Nora"
            jump jumpTimeStay

        "Cancel your trip to the beach." if beach_girl == "Nora":
            me "Hey Nora. I wanted to give you a heads up, something came up and I'll be busy on Saturday. We'll have to head to the beach some other time."
            "There's a delay of a few minutes, then Nora responds."
            nora "That's a shame. Let me know if you're free in the future then."
            $ beach_girl = None
            jump jumpTimeStay

    jump jumpTimeSkip

label stephTalk: #only in the morning. 'strip" is used in case you don't want to talk to steph and have one of the minor scenes trigger. Used when you call her into the lab.
    show steph work at right
    me "Hey Stephanie, how's it going."
    steph "It's going well. Good to see you're up bright and early today too."
    menu:
        "Spend some time together.":
            if knows_advanced_info and not has_lab_assistant:
                jump maj_stephConvinceAssistant
            else:
                call hub_steph
                if _return:
                    jump campusJumpTimeSkip
                else:
                    jump campusJumpTimeStay

        "See if she knows anything about the drug you're using" if knows_blue_serum and not has_research_papers:
            me "I've been doing some studying lately, and I was wondering if you could take a look at something for me."
            steph "Sure, what've you been looking at?"
            me "Well, since I started here I've been trying to figure out exactly what you two are doing. I did some reading online, and I found this."
            "You pull out a notebook and show her the scientific code for the drug you're using."
            me "It seems like this would be perfect for your organic molecule machine."
            "Stephanie takes the notebook from you and looks at the code, then turns and types it into a computer."
            steph "One moment."
            me "Sure."
            "She pulls up some research articles, nods in agreement, then turns back."
            steph "Ya, we've been looking into a lot of stuff exactly like this. Your research is out of date though, there's been a lot of changes since this paper was published."
            me "Really? I tried searching for more online and couldn't find anything."
            steph "Most of it hasn't made it to peer review yet, so unless research teams are sending you data directly you aren't going to see anything about it."
            me "Huh. Is there any way I could learn more?"
            "Stephanie pauses and thinks about it."
            steph "Well. I've got a few articles that might interest you, I could email them to you if you're really interested in all this."
            me "I am, biology has never been that interesting to me, but this summer it's grabbed my attention."
            "She smiles and hands you your notebook back."
            steph "Alright then, when I get home tonight I'll send you the papers. I'm glad you're finding this all so interesting!"
            me "So am I. We should get back to work before Nora chews us out."
            "Stephanie nods, and the two of you spend the rest of the day working normally in the lab."
            $ has_research_papers = True
        "Offer to pick up some drinks. -$10" if player_money>=10:
            me "It looks like you're still waking up a little bit. I can take a run to the coffee shop and grab us some drinks if you'd like."
            steph "Ooh, an iced cap is always great in the morning. I can get you some cash for it."
            me "No problem, my treat."
            hide steph
            $ player_money += -10
            "You head out and pick up a coffee for yourself and an iced cap for Stephanie."
            call resistance_gain_report(steph_drink_event_object,stephO)
            if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                "In the basement as you head back to the lab you have a few minutes without anyone around."
                menu:
                    "Pour some serum into Stephanie's drink.":
                        jump maj_stephSpikeDrink

                    "Leave her drink alone":
                        "You think better of spiking Stephanie's drink."
            show steph work at right
            steph "Ah, perfect. You're a life saver [inputName]."
            me "No problem at all."
            "You hand over her drink, and the two of you chat about various lab problems for a while."
            "You head out to get some fresh air as lunch draws close."
        "Have Stephanie help you make some red serum. -3 Blue, -1 Supply" if knows_red_serum and player_serum_supplies > 0 and player_blue_serum > 2 and has_lab_assistant:
            me "Stephanie, can you grab some supplies for me? I need your help."
            steph "Sure, one moment."
            "Stephanie helps you with the delicate biological processes, and after an hour of hard work you have two vials filled with a red liquid."
            $ player_serum_supplies += -1
            $ player_blue_serum += -3
            $ player_red_serum += 2
        "Have Stephanie help you make some purple serum. -3 Blue, -1 Supply" if knows_purple_serum and player_serum_supplies > 0 and player_blue_serum > 2 and has_lab_assistant:
            me "Stephanie, can you grab some supplies for me? I need your help."
            steph "Sure, one moment."
            "Stephanie helps you with the delicate biological processes, and after an hour of hard work you have two vials filled with a purple liquid."
            $ player_serum_supplies += -1
            $ player_blue_serum += -3
            $ player_purple_serum += 2
            #make a purple

        "Ask her to visit the beach with you." if stephO.slut_score > 20 and beach_girl is None and beach_unlocked:
            if stephO.beach_count == 0:
                me "Hey Stephanie. I just heard the beach is open for the summer and I'm planning to head up there on Saturday. If you want to come along I'd love the company."
                steph "Ooh, the beach. That sounds like a lot of fun. I'll have to pull out my swimsuit when I get home."
                me "So you're in?"
                steph "Definitly. I'll see you on Saturday I guess!"
            else:
                me "Hey Steph. I'm planning another trip up to the beach if you want to come along."
                steph "Sounds great. Saturday again?"
                me "Yeah, same plan as before."
                steph "Awesome, I'm in then. I guess I'll see you then."
            $beach_girl = "Steph"
            jump campusJumpTimeStay

        "Cancel your trip to the beach." if beach_girl == "Steph":
            me "Hey Stephanie. I've got something that came up this Saturday, so I won't be able to head to the beach like we planned."
            steph "Damn, that sucks. I guess just let me know if you want to reschedule."
            me "Will do."
            $ beach_girl = None
            jump campusJumpTimeStay

        "Talk to her about her birth control." if stephO.slut_score > 100 or (stephO.slut_score > 70 and stephO.cumslut):
            if stephO.bc:
                #intro
                me "Hey Stephanie, I wanted to ask you something. Are you on birth control right now?"
                if stephO.cumslut and stephO.freeuse:
                    steph "I'm taking the pill. Good thing too, I think I'd be pregnant four times over by now without it. Why do you ask?"
                else:
                    steph "I'm taking the pill, yeah. Why do you ask?"

                menu:
                    "Tell her to stop taking her birth control pills.":
                        $ stephO.bc = False
                        me "I want you to stop taking it from now on. I like the rush when there's a little bit of risk involved."
                        if stephO.freeuse:
                            steph "That might be a little dangerous, some of my friends really like to finish inside. If I'm not on the pill they might end up knocking me up."
                            me "Just have them wear condoms then. When you're with me I promise I'll be extra careful."
                            steph "Okay, I'll do it just for you [inputName]."
                        else:
                            steph "Well... I think I can manage that. We'll just have to be a little bit careful when we're together, okay?"
                            me "Of course, I'll be as careful as possible."

                    "Don't do anything about her birth control.":
                        me "Just checking, I wanted to make sure we weren't going to run into any problems."
                        if stephO.cumslut:
                            steph "Don't worry [inputName], you're free and clear to pump me full. I love how it feels when you do."
                        else:
                            steph "Don't worry [inputName], you'd have to be really dedicated to get me knocked up right now."

            else:
                #intro
                me "Hey Stephanie, I wanted to ask you something. You're not taking any birth control right now, right?"
                steph "No, I stopped when you asked me to. Is everything alright?"
                menu:
                    "Tell her to start taking her birth control pills again.":
                        $ stephO.bc = True
                        me "Everything is fine, I just think you should start taking it again. It was fun for a little bit, but I don't think I want to get you pregnant."
                        steph "Okay, if that's what you want. I'll start taking it again tomorrow."

                    "Don't do anything about her birth control.":
                        me "Everything is perfect. I just wanted to make sure nothing had changed."
                        if stephO.cumslut:
                            steph "Don't worry, you can still get me pregnant when you fill me up with that thick cum of yours. I won't change anything unless you want me to."
                        else:
                            steph "Don't worry, I'll talk to you first before I change anything."
                        me "That's very good to hear."

            "Once you're done talking to Stephanie you leave the lab and head back towards the center of campus."
            jump campusJumpTimeStay

        "Ask for the door code." if stephO.slut_score > 25 and not has_lab_code:
            me "Hey Stephanie, I've got a busy schedule for the next few weeks. It would be a lot easier for me to get stuff done if I had the door code - so I could come in and work even if you and Nora aren't around."
            steph "Oh, I didn't realize Nora hadn't given it to you yet. Here, let me write it down for you."
            "Stephanie grabs a bit of scrap paper from her desk and jots down a four digit code. She pauses before she hands you the paper."
            steph "I'm trusting you [inputName], make sure not to mess anything up in here when we aren't around."
            me "I promise, I'll leave everything exactly how I found it."
            "She nods and hands the note over. You take a second to commit it to memory, then stuff it in your pocket."
            me "Thanks a ton. I think I'm going to take a walk before Nora gets in, I'll talk to you in a little bit."
            "You say goodbye and leave the lab."
            $ has_lab_code = True
            jump campusJumpTimeStay

        "Ask for her phone number." if stephO.slut_score > 10 and not has_steph_number:
            me "Hey Stephanie, I don't think we have each others numbers right now, do we?"
            steph "No, I don't think we do."
            me "Maybe we should exchange them, in case there's ever an emergency."
            "She smiles and grabs her phone off of her desk, then puts it on a new contact page."
            steph "Here, put in your number and I'll do the same."
            me "Sounds good."
            "You give your phone to her, and she puts her number in. You swap phones back to their proper owners."
            steph "Do you play any sports?"
            me "Not often, why?"
            steph "I play tennis every morning on Sundays. If you ever want to come and hang out, just send me a text, okay?"
            me "Sure, it sounds like a good time."
            steph "Great. Now I've got some work to do before Nora gets in. Talk to you later."
            "You say goodbye and head out."
            $ has_steph_number = True
            jump campusJumpTimeStay

    jump campusJumpTimeSkip

label noraTalk: #At night
    if noraO.slut_score > 40 and nora_stripped_chance.check_event():
        call min_nora_walk_in
        jump jumpTimeSkip
    else:
        show nora work at right
        nora "Hello [inputName], need anything?"
        menu:
            "Talk about the lab.":
                me "No, just had some time to kill so I thought I'd see if I could help out here at all."
                if nora_party_chance.check_event():
                    nora "Really? You have perfect timing then. Stephanie just phoned and canceled on me, so I thought I was going to be stuck going alone."
                    me "Going where?"
                    nora "The faculty of science is having a party tonight, to celebrate the years work.  Stephanie and I were invited. I'm guessing spending the whole evening with a bunch of bureaucrats won't be fun."
                    nora "But there's an open bar, and the dress code is pretty loose. If you wanted to tag along I'd appreciate the company."
                    menu:
                        "Sure, I'd love to.":
                            me "Well I'd be a pretty crappy friend if I let you struggle through all that alone. I'm not doing anything else tonight, so sure I'll come."
                            "Nora looks visibly relieved."
                            nora "Thanks, if we stick together we can probably avoid most of the pencil pushers. I swear most of them didn't even pass their highschool science class."
                            "You and Nora leave the lab and head across campus to a small building used for public events. It's a two story glass building, right on the edge of campus."
                            "When you walk in the door a receptionist asks for your names. Nora gives hers, and says you're a late addition, replacing Stephanie."
                            "The receptionist checks ID, then nods and lets you both through."
                            me "Wow, this place looks pretty fancy."
                            "A waiter moves by with a tray of finger food, and you snatch something bright pink off of it."
                            nora "Yep. The department heads love this thing. It's all in the name of \"Networking\". It's like they forget some of us are actual scientists. Some of us have labs to run."
                            "She sighs and motions to a table at the far side of the room."
                            nora "I get the feeling it's going to be a long night. Would you mind grabbing us some drinks? I'm going to scope out a quiet corner for us to hide in until this is over."
                            me "Sure thing, back in a second."
                            hide nora
                            "You head over to the drink table and wait in a short line. When you reach the front, you ask for two glasses of red wine, then start heading back to Nora."
                            call resistance_gain_report(party_event_object,noraO)
                            menu:
                                "Pour some serum in her wine." if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
                                    jump maj_scienceParty
                                "Leave the drink alone and head back.":
                                    "You search around for a while until you find Nora again, standing behind a pillar out of sight with her phone out."
                                    show nora work at right
                                    me "Here you go, this should make things easier."
                                    nora "Thanks [inputName]."
                                    "For the rest of the evening you and Nora make small talk. She emerges from her hiding spot during a short speech, making a point of being noticed so people know she was there."
                                    "When she comes back she finishes her wine and leave the glass on a table."
                                    nora "Okay, that should be enough to avoid any office fallout. Lets get out of here."
                                    "You walk Nora to the parking lot where her car is and say goodnight."
                        "Actually, I have plans for tonight.":
                            me "Oh, actually I made plans for later tonight. I've got to be heading out in a few minutes."
                            "Nora looks a little deflated, but nods."
                            nora "I understand. I guess I'm on my own for this one then."
                            me "I'm sure you'll be fine. How bad could it be?"
                            nora "You're probably right. Anyway, I've got to get going or I'm going to be late."
                            "She heads to the door and locks it up behind both of you. You walk with her to ground level and say goodbye."
                            jump campusJumpTimeStay
                else:
                    nora "That's nice. I think there was actually some paperwork you missed doing that I need. Would you mind filling it out for me?"
                    me "Sure, I guess that's no problem."
                    "Nora heads to her desk and hands you a small stack of paper. For the rest of the evening you sit beside her and chat while you fill out paperwork."
                    menu:
                        "Ask for her phone number." if noraO.slut_score > 30 and not has_nora_number:
                            me "So Nora, I don't think I have your phone number if I ever need to reach you."
                            nora "You can always call the lab, it forwards everything to me if nobody picks up."
                            me "Right, but it's not always that important. I've been doing some bio studying, and it would be useful to have a way of getting in touch less formally. Like a text."
                            "Nora keeps doing paperwork at her desk."
                            nora "I suppose that's a good idea. It's good to hear you're taking this position so seriously. We've had a few lab assistants before you who just did it for the paycheck."
                            me "It's all interesting stuff, and I'm doing my best to learn."
                            "You pull out your phone and open a new contact for Nora. You pass it over, and she quickly enters in her cell number then passes it back."
                            me "Thanks Nora."
                            nora "No problem."
                            $ has_nora_number = True
                            jump campusJumpTimeStay
                        "Ask for the door code." if noraO.slut_score > 40 and not has_lab_code:
                            me "So Nora, I wanted to ask you something. I tend to get here early most days, before you show up, and it's nice to get some extra work done then. You keep the lab locked most of the time, so I need Stephanie to let me in."
                            nora "Okay, and?"
                            me "Well, if I had the code to the door I could get more work done without bothering Stephanie to let me in all the time."
                            nora "Well, we don't normally give out the code to interns, since you usually rotate through so quickly..."
                            "Nora takes a break from her paperwork and looks at you, thinking intently for a moment."
                            nora "But that doesn't seem to be the case with you. Alright [inputName], if you promise not to be causing any trouble while you're here I can give you the code."
                            me "I promise, I'll leave everything exactly how I found it."
                            "Nora nods and pulls out a piece of paper. She writes down a four digit code and hands it to you."
                            nora "There you go. Make sure you don't let anyone else find out about it, we have a lot of expensive equipment down here."
                            "You commit the code to memory, then fold the paper and shove it into your pocket."
                            me "Got it. Thanks Nora."
                            $ has_lab_code = True
                            jump campusJumpTimeStay
                        "Ask about your new Serum research." if knows_advanced_info and not has_advanced_papers:
                            me "So Nora, I've been doing some extracurricular activities lately. Doing my best to catch up to you and Stephanie."
                            nora "That's good. Self learning is one of the most important parts of being a scientist."
                            me "Right. I've been looking into the stuff you and Stephanie have been working on here actually, with your molecular delivery system."
                            nora "Oh, well that's some very advanced subject matter."
                            me "I know, I'm just barely making my way through the literature. It doesn't make it any easier when half the information I've been able to find online is incomplete."
                            nora "Well a lot of it is cutting edge stuff right now. Much of what we're doing here is going to take a year or two to be published anywhere."
                            "Nora moves a finished sheet to the side of her desk and grabs a new one to start working through."
                            nora "If you want to actually keep up to date, you need to be talking to researchers directly."
                            me "And is there any way you could help me with that?"
                            if noraO.slut_score > 40:
                                "Nora thinks about it for a moment."
                                nora "I think I can. One moment."
                                "Nora slides over to her computer and does some typing, then turns back."
                                nora "Okay, I've set you up a temporary account for the summer. You should be able to ask for details about whatever you're researching now."
                                me "Excellent, thank you Nora."
                                nora "Anything to help a curious student. What were you studying, by the way?"
                                me "Using your molecular delivery system as a platform for drug delivery. I think it may be kind of cool."
                                "Nora nods a little and smiles."
                                nora "Yes, I think it might be. Maybe you'll be able to do your PhD on it one day."
                                me "One day, ya."
                                $ has_advanced_papers = True
                            else:
                                "Nora thinks about it for a moment."
                                nora "I don't believe so, actually. The groups we have going are very small at the moment, and all of us are experts in our fields. I don't think you would get much out of it."
                                me "Oh, okay. Forget I asked then."
                                nora "I'm very happy you're looking into it though, that's the sign of a good student."
                            jump campusJumpTimeStay
                        "Talk about work.":
                            "You chat about how the lab has been running recently."

                    "Eventually it's late and Nora says she has to head out and lock the lab. You walk with her up to ground level and say goodbye."

            "Ask her to visit the beach with you." if noraO.slut_score > 30 and beach_girl is None and beach_unlocked:
                if noraO.beach_count == 0:
                    me "I don't need anything, but I'm planning a trip out to the beach this weekend and I wanted to invite you along."
                    nora "Oh, it's been forever since I was out to the beach. I'm glad they finally opened it up this summer. What day, exactly?"
                    me "Saturday. There's a direct bus there and back, so there are no worries about that."
                    "Nora thinks for a moment, then smiles and nods."
                    nora "Alright then, count me in. I'll have to dig out my swimsuit and get ready."

                else:
                    me "No, I don't need anything. I'm planning another trip out to the beach on Saturday, if you want to come along with me."
                    nora "That sounds great [inputName]. I'll be ready on Saturday."

                $ beach_girl = "Nora"
                jump campusJumpTimeStay

            "Cancel your trip to the beach." if beach_girl == "Nora":
                me "No, I don't need anything. I just wanted to let you know that I've had something come up on Saturday, so I won't be able to head to the beach."
                nora "Oh, that's a shame. If you want to reschedule just let me know."
                $ beach_girl = None
                jump campusJumpTimeStay

            "Talk to her about her birth control." if noraO.slut_score > 100 or (noraO.slut_score > 70 and noraO.cumslut):
                if noraO.bc:
                    #intro
                    me "I just had a quick question actually. Are you on birth control right now?"
                    nora "Yes, I'm taking the pill. Why do you ask?"
                    menu:
                        "Tell her to stop taking her birth control pills.":
                            $ noraO.bc = False
                            me "I wanted you to stop taking them, for me. I like the rush I get when there's a little risk involved."
                            if noraO.cumslut:
                                nora "The risk that you'll get me pregnant when you cum deep inside me? I think I can understand the appeal."
                                me "Yeah, that's exactly what I mean."
                            else:
                                nora "I suppose I could do that. You just need to promise you'll be careful where you finish, okay?"
                                me "Of course, I'll be as careful as possible."

                        "Don't do anything about her birth control.":
                            me "No reason, I just wanted to make sure you were safe."
                            nora "Don't worry about it [inputName]. Modern birth control is very effective. You would have to finish inside of me a hundred times over for there to be a real chance of anything happening."

                else:
                    #intro
                    me "I just had a quick question. You're not on the pill right now, right?"
                    nora "No, I stopped when you asked me to. Why?"
                    menu:
                        "Tell her to start taking her birth control pills again.":
                            $ noraO.bc = True
                            me "I think you should start taking your birth control again. I wouldn't want to accidently get you pregnant."
                            if noraO.cumslut:
                                nora "Would it be an accident if I asked you to do it? I was starting to enjoy how it felt, the risk made everything so much more intense."
                                me "Maybe some other time, right now I think it's better if you're safe."
                                nora "Alright [inputName], I'll start taking it tomorrow."

                        "Don't do anything about her birth control.":
                            me "No reason, I just wanted to make sure nothing had changed."
                            if noraO.cumslut:
                                nora "Just wanted to make sure your cumslut was still nice and breedable? I promise you [inputName], I haven't changed a thing."
                                me "Good to hear Nora, very good to hear."

                "Once you're done talking to Nora you leave the lab and return to the center of campus."
                jump campusJumpTimeStay

            "Ask for a favour.":
                me "Ya actually, if you have a moment."
                "Nora turns her full attention to you and waits for you to continue."
                call hub_nora
                if _return:
                    jump jumpTimeSkip
                else:
                    jump jumpTimeStay

    jump campusJumpTimeSkip

label labMorning:
    scene bg lab_day
    with fade


    if steph_in_lab or ((not steph_not_in_lab) and (not day%7 == 1) and steph_lab_chance.check_event()):
        $ steph_in_lab = True
        $ steph_not_in_lab = False
        "You knock on the lab door, and Stephanie opens it for you."
        if steph_stripped_chance.check_event() and stephO.slut_score > 25:
            call min_steph_walk_in
            jump campusJumpTimeSkip
        else:
            jump stephTalk
    else:
        $ steph_in_lab = False
        $ steph_not_in_lab = True
        "You knock and no one answers the door."
        menu:
            "Try the code lock.":
                if has_lab_code:
                    "You key in the lab door code and enter. You've got the lab entirely to yourself."  #TODO
                    if noraO.slut_score > 40 and nora_masturbating_chance.check_event():
                        jump min_nora_masturbating
                    else:
                        jump labAlone
                else:
                    "You try a few random codes, and each time the panel flashes back red at you. No luck just guessing."
                    "With nothing else to do here, you head back to the center of campus."
                    jump campusJumpTimeStay
            "Head back to the center of campus.":
                "Trying random codes until one works would take forever. Better to just not waste your time."
                jump campusJumpTimeStay


label labAfternoon:
    #usually steph and nora and work. Rarely alone
    scene bg lab_afternoon
    with fade

    $ went_Work = True
    if (not skip_nobody_home_lab_event) and nora_steph_lab_chance.check_event():
        $ skip_nobody_home_lab_event = True
        "You knock and no one answers the door."
        "A note taped to the doorknob reads \" Getting drinks. Be back soon. \". The door is propped open slightly, and you're able to enter."
        "The lights in the lab switch on automatically as you come in. You have the lab all to yourself for a few minutes."
        menu:
            "Impress the girls by cleaning everything up.":
                $ lab_cleaned_up = True
                #place holder
                "You spend a few minutes tidying up the lab. When Stephanie and Nora return, they give you a smoothie they picked up for you at the food court on campus and thank you for your hard work."
            "Quickly make some blue serum." if knows_blue_serum and expert_serum_skill:
                "Without anyone to worry about you quickly spin the machines up and get to work. After a few minutes they've produced a vial of vivid blue liquid."
                "You get the lab equipment cleaned up before anyone gets back."
                $ player_blue_serum += 1
                call gain_xp
            "Search Nora's Desk.":
                "You head over Nora's desk and pull open drawers, quickly looking through her notes for something useful."
                "You find several folders with the labs financial reports. Nora is obsessed with record keeping, she even keeps an estimate of how many paper clips are left in the supply closet."

                if panty_find_chance.check_event():
                    if noraO.slut_score < 40: #Nothing
                        "After a few minutes you give up, and return all the papers to where you found them."
                        "When Nora and Stephanie return, neither of them notice that anything was moved. They even bring you a smoothie."
                    elif noraO.slut_score < 80 and not noraO.freeuse: #Get her off, she does nothing.
                        call min_nora_panty_play_1
                        "The rest of the day goes by quickly, and before you know it Nora is telling you both to head home."
                        jump campusJumpTimeSkip
                    else: #Get her off, she goes along with it.
                        call min_nora_panty_play_2
                        "The rest of the day goes by quickly, and before you know it Nora is telling you both to head home."
                        jump campusJumpTimeSkip
                else:
                    "After a few minutes you give up, and return all the papers to where you found them."
                    "When Nora and Stephanie return, neither of them notice that anything was moved. They even bring you a smoothie."
            "Search Stephanie's Desk.":
                "You head over to Stephanie's desk and sift through the papers left on top."
                if (lab_code_chance.check_event() and not has_lab_code):
                    "After a few short minutes you find a four digit code scrawled and circled at the back of a notebook."
                    "Underneath the code are the words \"DOOR CODE! DONT FORGET\""
                    "You take a picture of the code with your phone, then put everything back together."
                    $ has_lab_code = True
                else:
                    "Nothing you find is very interesting, unless you find scribbled numbers and half written equations interesting."
                    "You try and return everything to where it was, but her desk is so disorganized you doubt she'll notice."
                "When Nora and Stephanie return, neither of them notice that anything was moved. They even bring you a smoothie."
        jump labAfternoon
    else:
        if not skip_nobody_home_lab_event:
            "The door is left open so you can come in."
        show steph work at right
        steph "Hey [inputName]. Glad you could make it."
        "Nora is at a machine and waves absentmindedly to you."
        show nora work at left
        menu:
            "Spend time chatting with Nora and Steph.":
                jump noraStephTalk
            "Get access to the labs online resources to learn more about the potential organic molecules." if not (knows_blue_serum or has_online_code):
                "You approach Nora."
                hide steph
                show nora at right
                me "Hey Nora, could I have a minute of your time?"
                nora "Sure [inputName]. How can I help you?"
                "She turns away from the machine she was working at."
                me "Well, chemical engineering has always been my strong point, but it seems like you two mostly do biology studies here."
                "Nora nods"
                nora "That's right, we wanted you to broaden our knowledge base. Cross disciplinary research and all that."
                me "Right. Well I'm feeling a little out of my element here, and I know you've got access to some of the online journals."
                me "Is there anyway you could get me access as well? I'd like to do some research on my own time to try and catch up with you two."
                "Nora leans against the desk and thinks for a moment."
                nora "Yes, I suppose that would be alright. I can give you log in credentials so you can access it online. You can't be studying during your work hours though, you understand?"
                me "Of course, of course. Thank you, this will really help me understand more of what's going on here."
                nora "No problem at all."
                "She moves to her personal computer and does some typing. A few minutes later you have a randomly generated username and password that should get you access to everything you need to know."
                $ has_online_code = True
                "You spend a few hours cleaning test tubes, testing machines, and otherwise making yourself useful."
                "Eventually Nora calls it a night and says she's closing the lab."
                jump campusJumpTimeSkip
            "Do lab work.":
                if knows_blue_serum:
                    "You're almost certain you could manufacture some of the blue serum you read about without Nora or Steph noticing."
                    menu:
                        "Try and make blue serum.":
                            if blueberry_caught.check_event():
                                jump maj_blueberryEvent
                            elif stockroom_check.check_event():
                                "You begin to ready the supplies, but before you can start the machines Nora calls out to you."
                                call min_steph_stockroom
                            else:
                                if lab_strip_chance.check_event():
                                    "With a few minutes of work and some careful sneaking you get all the supplies ready and the machines running."
                                    call min_nora_steph_work_undress
                                    $temp_slut_score = 0
                                    if (stephO.slut_score < noraO.slut_score):
                                        $temp_slut_score = stephO.slut_score
                                    else:
                                        $temp_slut_score = noraO.slut_score #ie. Use the lowest score only.
                                    if temp_slut_score < 10: #Work normally
                                        if expert_serum_skill:
                                            "By the end of the day they've produced three vials of vivid blue liquid."
                                            $ player_blue_serum += 3
                                            call gain_xp
                                        elif practiced_serum_skill:
                                            "By the end of the day they've produced two vials of vivid blue liquid."
                                            $ player_blue_serum += 2
                                            call gain_xp
                                        else:
                                            "By the end of the day they've produced a vial of vivid blue liquid."
                                            $ player_blue_serum += 1
                                            call gain_xp
                                    else:
                                        if practiced_serum_skill:
                                            "By the end of the day the distractions have caused you to ruin most of the serum. You are only able to salvage one vial of vivid blue liquid."
                                            $ player_blue_serum += 1
                                            call gain_xp
                                        else:
                                            "By the end of the day the distractions have caused you to ruin the serum, but at least you still gained some experience with the process."
                                            call gain_xp
                                else:
                                    if expert_serum_skill:
                                        "With a few minutes of work and some careful sneaking you get all the supplies ready and the machines running. By the end of the day they've produced three vials of vivid blue liquid."
                                        $ player_blue_serum += 3
                                        call gain_xp
                                    elif practiced_serum_skill:
                                        "With a few minutes of work and some careful sneaking you get all the supplies ready and the machines running. By the end of the day they've produced two vials of vivid blue liquid."
                                        $ player_blue_serum += 2
                                        call gain_xp
                                    else:
                                        "With a few minutes of work and some careful sneaking you get all the supplies ready and the machines running. By the end of the day you've produced one vial of vivid blue liquid."
                                        $ player_blue_serum += 1
                                        call gain_xp
                            jump campusJumpTimeSkip
                        "Too risky, just do normal lab work.":
                            "You spend a few hours cleaning test tubes, testing machines, and otherwise making yourself useful."
                            if stockroom_check.check_event():
                                call min_steph_stockroom
                            elif lab_strip_chance.check_event():
                                call min_nora_steph_work_undress
                            "Eventually Nora calls it a night and says she's closing the lab."
                else:
                    if lab_strip_chance.check_event():
                        call min_nora_steph_work_undress
                    else:
                        "You spend a few hours cleaning test tubes, testing machines, and otherwise making yourself useful."
                        "Eventually Nora calls it a night and says she's closing the lab."

                "Eventually Nora calls it a night and says she's closing the lab."
                jump campusJumpTimeSkip


label labNight:
    #alone time with nora, or lab is empty
    scene bg lab_night
    with fade
    if nora_in_lab or ((not nora_not_in_lab) and day%7 != 5 and nora_lab_chance.check_event()):
        $ nora_in_lab = True
        $ nora_not_in_lab = False
        "You knock on the lab door."
        nora "It's open, come in!"
        jump noraTalk
    else:
        $ nora_in_lab = False
        $ nora_not_in_lab = True
        "You knock and no one answers the door."
        if has_lab_code:
            $ temp_slut_score = 0
            if (noraO.slut_score > stephO.slut_score):
                $ temp_slut_score = stephO.slut_score
            else:
                $ temp_slut_score = noraO.slut_score

            if nora_steph_les_chance.check_event() and temp_slut_score > 30:
                call min_nora_steph_caught
                #Nora and Steph are making out/licking each other/scissoring. Sometimes want you to join.
            else:
                "You key in the lab door code and enter. You've got the lab entirely to yourself."
                jump labAlone
        else:
            "With no one in the lab you don't have a way in. You spend some time looking for Nora or Stephanie, but can't find either of them."
            jump campusJumpTimeStay
        jump campusJumpTimeSkip

label labAlone:
    "The lab lights turn on automatically for you as you enter. The machines all sit waiting for you to operate them."
    menu:
        "Make a batch of blue serums." if knows_blue_serum:
            #make a bunch of blues
            if expert_serum_skill:
                "Without having to worry about anyone noticing what you're doing you're able to produce a batch of five doses at once. You pocket them, reset all the equipment, and head out before Nora or Stephanie show up."
                $ player_blue_serum += 5
            elif practiced_serum_skill:
                "Without having to worry about anyone noticing what you're doing you're able to produce a batch of four doses at once. You pocket them, reset all the equipment, and head out before Nora or Stephanie show up."
                $ player_blue_serum += 4
            else:
                "Without having to worry about anyone noticing what you're doing you're able to produce a batch of three doses at once. You pocket them, reset all the equipment, and head out before Nora or Stephanie show up."
                $ player_blue_serum += 3
            call gain_xp
        "Search the entire lab.": ## add extra stuff to find at some point
            if chance_red.check_event() and knows_advanced_info and not knows_red_serum:
                #Find red serum notes
                "With some time completely alone in the lab, you begin a systematic search of it for anything you might find interesting."
                "Finally, after a long search, you come across a locked cabinet at the back of the office. The lock is a cheap office style one, and with a bent paperclip and a credit card you're able to get it open."
                "Inside there are a few rows of binders, all marked \"Confidential\"."
                "You grab a few and sit down at a bench to start reading."
                "The first few pages grab your attention immediately. There are a few printed off emails here between Nora and the head of a German research team doing similar work in Europe."
                "They're telling Nora that their work has been marked a government secret now, so they will have to stop all further collaboration. As a final token of their appreciation, they've included all their data up to now."
                "The next page includes a short description of their latest progress. It seems they've made a more aggressive version of the drug, but note that it's both more difficult to produce and prone to backlash from the recipient."
                "The rest of the binder is filled with work notes, descriptions of processes, and material counts. Half of it makes no sense to you, but with help you think you could produce a new version of your serum."
                if has_lab_assistant:
                    "If you bring Stephanie supplies and a batch of three blue serum, you will be able to produce some of this new red serum."
                else:
                    "Getting help for this will be the next hurdle. If you manage that, you will be able to use some extra supplies and a batch of three blue serum to produce some of this new red version."
                $ knows_red_serum = True
                "Once you've taken pictures of all the pages you need, you return the binders and manage to get the lock shut again."
            else:
                "With some time completely alone in the lab, you begin a systematic search of it for anything you might find interesting."
                "After a long while of searching, you've been able to turn up nothing of note though. Maybe there's nothing to find, or maybe you don't know enough about what you're looking for."
        "Back out of the lab and head back to the center of campus.":
            "With nothing to do here, you back out of the lab."
            jump campusJumpTimeStay
        "Call Stephanie into the lab." if has_steph_number and stephO.slut_score > 50 and dayTime == 0:
            "You text Stephanie asking for her to come into the lab. She shows up a few minutes later."
            $ steph_in_lab = True
            $ steph_not_in_lab = False
            jump stephTalk
    jump campusJumpTimeSkip
    #make serious serums

label noraStephTalk:
    "You and Stephanie get into a conversation about lab work. After a little while Nora finishes what she was doing and comes to join you."
    nora "You two have your nose to the grindstone I see."
    steph "Just trying to figure out a better way of separating proteins. [inputName] has a few good ideas."
    show nora work at left
    show steph work at right

    if lab_cleaned_up or snacks_chance.check_event():
        nora "Is that so? Excellent, we'll try them for the next run."
        me "Thanks, glad I could help."
        steph "More than help, the lab work's twice as easy with you around."
        nora "Agreed. How about we treat you to drinks or something, you've done enough to warrant a reward."
        me "You don't have to do that, just doing my job."
        steph "Come on, it's our treat."
        nora "Here, I'll give you some cash. Go and grab all three of us some smoothies or something. I'm calling the work day over for now."
        "Nora gives you some cash and you head out towards the food court on campus."
        hide steph
        hide nora
        call resistance_gain_report(lab_threesome_event_object,stephO,noraO)
        menu:
            "Grab the drinks and head back":
                "You return with drinks, and the three of you pull up chairs around a table and chat."
                show steph work at right
                show nora work at left
                "It's nice to have some time to hang out with the two of them and not worry about work at all."
                "Eventually it gets late and Nora tells you she needs to close the lab."

            "Pour a dose of serum into both drinks" if (player_blue_serum + player_purple_serum + player_red_serum > 1):
                jump maj_labThreesome
    else:
        nora "Is that so? Good. Keep up the good work. I've got some results for you to look at Steph, got a moment?"
        steph "Sure, no problem."
        nora "[inputName], there's a machine that's acting up, could you take a look? It's on my desk."
        me "Sure. I'll check."
        "You spend the day fixing the broken machine, then the three of you head out for the day."
    jump campusJumpTimeSkip

label momNightEncounter:
    "Late at night, you're awoken by a need to use the bathroom. Wiping the sleep from your eyes you get up and head towards the bathroom."
    "After doing your business, you're returning to your room when you notice mom's bedroom door is open slightly."
    menu:
        "Ignore it and go back to bed.":
            "Your bed calls to you, and within minutes you're sound asleep again."
            jump jumpTimeSkip
        "Peek inside and take a look.": #TODO add chance to peek on mom while she's masturbating.
            "You walk slowly and quietly up to mom's bedroom door and peer into the dark room. Her alarm clock paints the room in a dim red, and you can make out her sleeping form on the bed."
    "Beside her on the nightstand is a glass of water, half full."
    call resistance_gain_report(mom_night_event_object,momO)
    if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
        menu:
            "Sneak in and spike her drink.":
                jump maj_spikeMomNight
            "Leave while you can and head back to bed.":
                "Getting caught now would be disastrous. You decide to play it safe and head back to your bed. Within minutes you're sound asleep again."
                jump jumpTimeSkip
    else:
        #TODO Walk in and fuck her on high slut?
        "After watching her sleep for a while you decide that it's too risky being here. You head back to your room and fall asleep within minutes."
        jump jumpTimeSkip

label sisNightEncounter:
    "Late at night, you roll over in your bed. Your mouth is dry and you can't sleep."
    "Giving up, you stand up from bed and start making your way downstairs."
    "As you reach the hall you see another door opening."
    show sis casual_night at right
    me "Oh, hey sis."
    "Lily rubs the sleep out of her eyes."
    sis "[inputName]? What are you doing up?"
    me "My throat was dry. I'm getting a drink."
    "She nods."
    sis "Me too. Maybe the humidifier is broken or something."
    me "No point in us both going down. I'll grab you a glass of water."
    sis "Sure. Thanks."
    "Lily turns around and returns to her room, yawning loudly."
    hide sis
    "You walk downstairs and make your way to the kitchen, where you retrieve two glasses of water. One you down immediately for yourself, the other you get for Lily."
    call resistance_gain_report(sis_night_event_object,sisO)
    if (player_blue_serum > 0 or player_purple_serum > 0 or player_red_serum > 0):
        menu:
            "Get some serum and pour it in Lily's drink.":
                jump maj_spikeSisNight
            "Leave her drink alone and head back upstairs":
                "You think better of using the serum right now."
    "With her water in hand, you head back upstairs to Lily's room."
    me "Knock knock."
    show sis casual_night at right
    sis "Thanks [inputName]"
    me "No problem, have a good night."
    sis "You too."
    "You both head back to bed, and wake up the next morning feeling rested."
    jump newDay

label beach_check:
    if beach_girl == "Lily":
        "There's a knock at your door, followed by your sister opening it up."
        show sis casual1 at right
        sis "Hey [inputName], you in there?"
        me "Yeah. Come in."
        sis "Just checking to see if you're ready to head to the beach. We should give ourselves plenty of time to catch the bus."
        menu:
            "Head to the beach.":
                me "Yeah, I think I've got everything ready to go. I'll meet you downstairs in a few minutes."
                "Lily closes the door. You grab a bag with your swimsuit, a hat, and some sunscreen in it and head downstairs."
                jump beach_sis
            "Stay home.":
                me "Actually Lily, I think I'm going to have to cancel for today."
                sis "Aw, what? But I'm all ready to go!"
                me "Sorry, I've just had something that came up that I need to take care of."
                "Lily frowns and crosses her arms."
                sis "Really?"
                me "Really. I'm sure we'll get another chance to go though, I'll let you know when I've got a free Saturday again."
                sis "Fine. I guess I'll go pack all my stuff away again."
                hide sis
                "She turns around and leaves, closing your door behind her."


    elif beach_girl == "Mom":
        "There's a knock at your door."
        mom "[inputName], are you there?"
        me "Yeah Mom, what's up?"
        show mom casual at right
        "Mom opens your door and steps into your room."
        mom "I just wanted to make sure you've got all your stuff ready for our trip to the beach. We should get going soon."
        menu:
            "Head to the beach.":
                me "Yeah, I think I've got everything I need. I'll meet you downstairs in a few minutes."
                "Mom closes the door. You grab a bag with your swimsuit, a hat, and some sunscreen in it and head downstairs."
                jump beach_mom

            "Stay home.":
                me "Right, that's today. Sorry Mom, something came up at the last minute and I'm going to have to cancel."
                mom "Oh. Okay then."
                "Mom steps out of your room again, looking disappointed."
                me "We can try and reschedule, I'll let you know if I'm free."
                mom "It's fine, whenever you have the time sweetheart. Have a good day."
                hide mom
                "She closes your door, leaving you alone in your room."


    elif beach_girl == "Steph":
        "Your phone buzzes. It's a text from Stephanie."
        steph "Hey [inputName]. Just double checking we're still good for our trip to the beach today."
        menu:
            "Head to the beach.":
                me "Yep, I'll meet you at the bus terminal."
                steph "Cool, see you soon."
                "You grab a bag with your swimsuit, a hat, and some sunscreen in it and head downstairs."
                jump beach_steph

            "Stay home.":
                me "Actually, something came up at the last minute. I'm going to have to cancel."
                steph "Oh, okay. I guess I'll find something else to do today."
                me "Sorry, I'll try and make sure I'm actually free next time and reschedule."
                steph "Sure. Talk to you later."

    elif beach_girl == "Nora":
        "Your phone buzzes. It's a text from Nora."
        nora "Hello [inputName]. I'm about to head over to the bus terminal. No change of plans, right?"
        menu:
            "Head to the beach.":
                me "No changes, I'll be heading out soon too."
                nora "Excellent. See you soon."
                "You grab a bag with your swimsuit, a hat, and some sunscreen in it and head downstairs."
                jump beach_nora

            "Stay home.":
                me "Actually, something came up at the last minute. I'm going to have to cancel."
                nora "Okay. I hope it's nothing serious."
                me "No, but it's going to keep me busy unfortunately. Maybe we'll be able to reschedule to some other time."
                nora "Sure. Send me a text and we can see about next week. Talk to you later."


    elif beach_girl == "Alex":
        "Your phone buzzes. It's a text from Alexia."
        alex "Hey [inputName], ready to hit the beach?"
        menu:
            "Head to the beach.":
                me "Yeah, I'll be heading to the bus terminal soon."
                alex "Sweet, I'll see you there!"
                "You grab a bag with your swimsuit, a hat, and some sunscreen in it and head downstairs."
                jump beach_alex

            "Stay home.":
                me "Actually, something came up at the last minute. I'm going to have to cancel."
                alex "What? Boo!"
                me "Sorry, there's nothing I can do about it."
                if alexO.exhib:
                    alex "Well, I didn't get this little swimsuit for nothing. I'm going to go up anyway and show it off a little. Let me know if you're free some other weekend."
                    me "Will do. Have fun."
                    alex "Oh, I plan to ;) Talk to you later."
                    $ alex_beach_busy = True #TODO: Make this into a minor scene where she gives you beach stories.
                else:
                    alex "Boo! Boo I say! Let me know if you're actually free some other weekend I guess."
                    me "Will do. Talk to you later."
    $ beach_girl = None

    return

label skip_end_confirm:
    $ the_time_remain = game_length - day
    $ sex_chances_remain = the_time_remain//2 #You can have sex with each girl on average once every other day.
    "This will skip through the remaining [the_time_remain] days. You will receive an ending based on your current influence over each girl, as well as their training and other stats."
    menu:
        "Skip to the end of the game.":
            if (sisO.slut_score > 80 or momO.slut_score > 80 or noraO.slut_score > 80 or stephO.slut_score > 80 or alexO.slut_score > 80):
                "With [the_time_remain] remaining before the end of the summer you'll have [sex_chances_remain] chances to have sex with each girl, assuming you have enough influence over them."

            if (sisO.slut_score > 80):
                menu:
                    "Have sex with Lily as many times as possible to try and get her pregnant.":
                        "You spend your afternoons in Lily's bedroom, fucking her raw and filling her up with your cum."
                        $ sisO.inc_cum_repeat(sex_chances_remain)
                        "By the end of hte summer you've creampied her [sisO.cum_inside_count] times."

                    "Don't do anything special with Lily.":
                        "Lily flirts with you whenever she sees you, but you don't go out of your way to spend extra time with her."

            if (momO.slut_score > 80):
                menu:
                    "Have sex with Mom as many times as possible to try and get her pregnant.":
                        "You spend your evenings with your mom, riding her doggy style and pumping your load nice and deep inside of her pussy."
                        $ momO.inc_cum_repeat(sex_chances_remain)
                        "By the end of the summer you've finished in her a grand total of [momO.cum_inside_count] times."

                    "Don't do anything special with Mom.":
                        "Your mom comes into your room a few nights a week for the rest of the summer. You fool around once in a while, but you don't spend any extra time with her."

            if (noraO.slut_score > 80):
                menu:
                    "Have sex with Nora as many times as possible to try and get her pregnant.":
                        "You stay late at the lab each work day with Nora, bending her over her desk and taking her bareback. You make sure to pump your seed as deep as you can manage each time."
                        $ noraO.inc_cum_repeat(sex_chances_remain)
                        "By the end of the summer you've cum inside your boss [noraO.cum_inside_count] times."

                    "Don't do anything special with Nora.":
                        "Nora asks you to stay late at the lab a few times and flirts with you, but you don't go out of your way to spend any extra time with her."

            if (stephO.slut_score > 80):
                menu:
                    "Have sex with Stephanie as many times as possible to try and get her pregnant.":
                        "You make sure to get into the lab early each day to spend time with Stephanie. She loves it when you fill her up with warm cum."
                        $ stephO.inc_cum_repeat(sex_chances_remain)
                        "By the end of the summer you've cum inside of Stephanie a total of [stephO.cum_inside_count] times."

                    "Don't do anything special with Stephanie.":
                        "Stephanie drags you into the store room for some fun every few days, but you don't make any extra time for her in your schedule."

            if (alexO.slut_score > 80):
                menu:
                    "Have sex with Alexia as many times as possible to try and get her pregnant.":
                        "You meet up with Alexia every day for lunch, then find a quiet lecture hall where she can ride you cowgirl style. You make sure to pull her down onto your cock when you cum so she gets every last drop."
                        $ alexO.inc_cum_repeat(sex_chances_remain)
                        "By the end of the summer you've filled Alexia up with your cum [alexO.cum_inside_count] times."

                    "Don't do anything special with Alexia.":
                        "you and Alexia meet up for lunch a few times, but you don't go out of your way to spend extra time with her."

            jump endScreen

        "Return to the game.":
            return
    return
