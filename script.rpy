# Title Pending lol please help


define unknown = Character('???')
define tm = Character('Taylor May')
define r = Character('Rae')
define h = Character('Hail')
define s = Character('Solar')
define g = Character('Grei')
define m = Character('Mye')
define p = Character('Paul')
define d = Character('Devil')
define e = Character('Employee')

default hallway_explored = False
default pool_explored = False
default rec_room_explored = False
default bedroom_explored = False
default kitchen_explored = False
default patio_explored = False
default counter = 0

default havent_done_much_yet = False

default lobby = False
default hallway = False
default pool = False
default kitchen = False
default patio = False

default rae_visited = False
default hail_visited = False
default solar_visited = False
default mye_visited = False

default rae = False
default hail = False
default solar = False
default mye = False
default killers = 0

label start:

    # scene bg book

    show text "-- Author's Note -" at truecenter
    with dissolve
    pause 2
    hide text
    with dissolve

    show text "May you find solace in that" at truecenter 
    with dissolve
    pause 2
    hide text 
    with dissolve

    show text "this is all a world of nonsense." at truecenter 
    with dissolve
    pause 2
    hide text 
    with dissolve

    show text "A confined space" at truecenter 
    with dissolve
    pause 2
    hide text 
    with dissolve

    show text "where pain, regrets," at truecenter 
    with dissolve
    pause 2
    hide text 
    with dissolve

    show text "and fumblings were created" at truecenter 
    with dissolve
    pause 2
    hide text 
    with dissolve

    show text "to exist within themselves." at truecenter 
    with dissolve
    pause 2
    hide text 
    with dissolve

    show text "… It was never my intention" at truecenter 
    with dissolve
    pause 2
    hide text 
    with dissolve

    show text "to hurt anyone but myself." at truecenter 
    with dissolve
    pause 2
    hide text 
    with dissolve

    pause 2

    # scene lobby
    
    # show rae hesitant talk at right

    unknown "You finally get a vacation, but you're reading a book like always?"

    # show tm talk at left

    # show rae neutral at right    

    tm "A gift that wasn't asked for is just a burden."

    unknown "Dude… just try and have some fun. This is a nice place, and the reservation was pricey." 

    unknown "What're you reading anyway? Isn't this the author that killed himself recently? Why're you reading something so depressing? Is it any good?"

    unknown "I only got through the first page, Rae." 

    r "Then there's nothing to miss about leaving it! At least look around a little. You might find something fun." 

    tm "..." 

    "Well, here I am in this fancy lobby."

    "All those holiday bonuses and whatnot… I can't believe Rae chose to spend it on this."

    "I know I pay him well and he has expensive tastes but… This one feels a bit out of place." 

    jump explore


label explore:

    if hallway_explored and pool_explored and rec_room_explored and bedroom_explored and kitchen_explored and patio_explored:

        jump finished_exploring

    else:

        "Where would you like to go?" #TODO

        menu:

            "Hallway":

                jump hallway_exploration

            "Pool":

                jump pool_exploration

            "Recreation Room":

                jump rec_room_exploration

            "Bedroom":

                jump bedroom_exploration

            "Kitchen":

                jump kitchen_exploration

            "Patio":

                jump patio_exploration
    

label hallway_exploration:

    $ hallway_explored = True

    "Oh, that's…"

    unknown "Is that from the Fall 20XX Collection?"

    unknown "… Yeah."

    "That's definitely that singer Rae is obsessed with, Hail."

    "So that's why he chose this place."

    "… Where did he go, anyway?"

    unknown "Hm. It looks good on you. I made a new one that would look better. It's releasing next season. I'll gift it to you."

    h "You're the designer? I thought you tried to keep your identity secret."

    unknown "I've heard about you. I doubt you'd do anything annoying about it."

    h "Haha, thanks. Are you a fan? I can give you a signature if you have a pen."

    unknown "Wouldn't know where to put it. I'm good."

    tm "Looks like this spot is popular with celebrities."

    tm "I guess that makes sense, with how few guests are allowed at a time."

    jump explore


label pool_exploration:

    $ pool_explored = True

    "Sign: [[Sorry! The pool is closed for cleaning.]"

    "Every single online review mentioned that the pool was closed on their trip. Shouldn't have expected otherwise."

    "I guess it's a bit pointless for a beach-side resort to have a pool anyway."

    r "What? The pool is closed. I wanted to go."

    tm "Did you bring a full-body wetsuit?"

    r "Uh, no? I was just going to buy a swimsuit here."

    tm "You… You have been picking at your stitches ever since the bandages came off." 

    tm "And you want to enter chlorinated water?"

    r "..." 

    tm "I better not see you anywhere near that beach." 

    jump explore


label bedroom_exploration:

    $ bedroom_explored = True
    
    "Rae would never stop nagging me for going back to my room right after we got here."

    jump explore


label kitchen_exploration:

    $ kitchen_explored = True
    
    e "Hello! Apologies, but guests are not allowed in the kitchen during normal circumstances!"

    e "Please, leave! Respectfully, get out!"

    menu:
        "My bad.":

            "*leaves*" ##complains about empty code block #TODO

        "'Normal circumstances?'":

            e "Yes! Everything is exceedingly normal right now, isn't it?"

            e "So get out! I hate people in my space!"

    tm "… Why did I even want to go to the kitchen in the first place?"

    jump explore


label rec_room_exploration:

    $ rec_room_explored = True
    
    g "Hello, I am Grei, the current resort manager. Guest Taylor May and…"

    g "I only have the name on file."

    r "I'm Rae."

    g "Guest Rae." 
    
    g "How has your stay been thus far? "

    r "Pretty good, thanks!"

    if pool_explored:

        menu: 

            "Why is the pool closed?":

                g "The pool is currently unavailable to guests."

                tm "… That really doesn't explain much."

                g "If you want to swim, I would suggest the very clean and privately owned beach this resort has."

                tm "…"

            "Haven't done much yet.":

                $ havent_done_much_yet = True
            
                tm "Just walking around so far."

                g "I hope you enjoy what the resort has to offer."

                tm "Thanks."

    if not havent_done_much_yet:

        menu:

            "Haven't done much yet.":
                
                    tm "Just walking around so far."

                    g "I hope you enjoy what the resort has to offer."

                    tm "Thanks."

    "There's a store here, but it says 'CLOSED:  Open to guests at a later time.'" 

    r "Oh, I see a syringe behind the glass." 

    tm "What kind of store is this supposed to be?"

    jump explore


label patio_exploration:

    $ patio_explored = True
    
    unknown "-Oof."

    tm "Oh, sorry, didn't mean to bump into you."

    unknown "That's okay, I wasn't paying attention."
    
    "Well, here's the patio. The beach seems to be the star attraction at this resort."

    "You can see it pretty well from this cliffside view."

    "And nothing else."
    
    tm "…I'm glad I brought a book."  

    r "I better not see you on that book this whole trip."

    tm "..." 

    "I need to stop talking out loud." 

    jump explore


label finished_exploring:

    tm "Well… that was pretty much the whole building."

    "This resort… doesn't have much going for it. I would think it's a good place for celebrities to secretly hook up,"

    "but the people here don't even seem to know each other."

    tm "What exactly should I do here for the next few days-"

    "Suddenly, the doors open with a loud banging noise."

    unknown "Ahh! Sorry I'm late!"

    unknown "I missed check-in, but I should still be able to check-in, right?"

    unknown "Here's my bags, if you could take them to my room."

    # CG HERE. He hands them to Rae. Rae gets a funny little face. 

    unknown "I reserved a room under the name Paul."

    r " "

    g "I'll take them to your room, sir."

    p "Thank you! Is this little man here just a trainee?" 

    r "Do I LOOK like-"

    "I pull Rae aside before he starts something."

    tm "Calm down, Rae." 

    "I lower my voice."

    tm "Your little celebrity-hero is here, you don't want to look bad in front of him, yeah?"

    r "…"

    "He put on his usual smile. Crisis avoided."

    "There's no end to trouble when Rae gets mad."

    e "Dinner's ready!"

    e "Everyone please gather in the dining room."

    e "Or we can bring your food to your room, if you'd like."

    h "..."

    r "..." 

    unknown "..." #Mateo

    unknown "..." #Solar

    tm "..."

    "We went to our rooms." 

    p "Oh, well… I'd like to see the dining room!" 

    jump next_day


label next_day:

    tm "... I guess it's not too bad to have a day off every now and then."

    tm "No incidents, no cleanups…" 

    tm "Let's go meet Rae in the lobby." 

    # corpse 

    tm "..." 

    tm "... That is none of my business." 

    "Suddenly, Grei appears beside me." 

    g "Esteemed guest of our resort, it seems there's been an unfortunate event!" 

    "He's nearly yelling, but his face is still completely deadpan…" 

    g "The resort has deemed you the most suited to solve the mystery behind Sir Paul's death." 

    "The amount of emotion he's putting into his words is impressive."

    "Almost as impressive as how much his face says 'I'm not paid enough for this.'" 

    g "There are eyes you cannot see. The resort is a body that functions as if it is breathing." 

    g "There is a process-a system-to a death occurring in the resort."

    g "The truth is already known, and it is your job to unveil it." 

    tm "Why me?"

    g "... Dude we know you're a detective." 

    "Oh, he broke character." 

    "And knows my personal information." 

    g "*coughs* The resort knows all that exists within itself." 

    g "It has determined the role each here shall play." 

    tm "No thanks."

    g "Rules of the resort are absolute, by nature, by law."

    g "Obstruction of the rules are punishable by torture, up until death."

    "I get a bad feeling." 

    tm "... Where are the other guests?"

    g "Ah, as expected of our star player. Good instincts."

    g "Each suspect is currently bound within their rooms."

    tm "Like, literally tied up?"

    g "Yeah they're tied to a chair by some rope right now." 

    tm "Oh. Hell no." 

    jump interrogation_start


label interrogation_start:

    tm "I should go to Rae first. He's going to get hurt if I don't get him out of those ropes."

    if counter == 0:

        menu:
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

    elif counter == 1:
        menu:
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

    elif counter == 2:
        menu:
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

    elif counter == 3:
        menu:
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

    elif counter == 4:
        menu:
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

    elif counter == 5:
        menu:
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

    elif counter == 6:
        menu:
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

    elif counter == 7:
        menu:
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

    elif counter == 8:
        menu:
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

    elif counter == 9:
        menu:
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to Rae":
                jump rae_room
            "Go to someone else":
                $ counter += 1
                jump loop

# A counter activates each time you choose "go somewhere else"
# Go to Rae multiplies on the screen, each goes to the same destination 
# Each response to Option 2 is different until loop 50 or something ends the game

label loop:

    if counter == 1:
        tm "...? Why would I do that?"
        jump interrogation_start
    
    if counter == 2:
        "... Why. Would I do that."
        jump interrogation_start

    elif counter == 3:
        "..."
        jump interrogation_start
    
    elif 4 <= counter <= 9:
        "... …" 
        jump interrogation_start

    elif counter == 10:
        "Taylor May punches the screen so hard it cracks"

    #idk if i should add dialogue from may here, it would be slightly 4th-wall breaking stuff
    
    "[[ENDING: Strong Will.]" 
    return

label rae_room:

    if not rae_visited:

        $ rae_visited = True

        "I fast-walk to Rae's room."

        # scene chair ← might not do

        tm "Rae…" 

        tm "Could you really not have waited a bit longer to dislocate your hands?"

        r "Haha, my bad! I thought it would work but I pulled out the wrong part." 

        r "They make it look easier in the movies."

        r "Good thing you came before I tried again!" 

        tm "..."

        "I untie the ropes. The knots… were quite well done."

        tm "Weird situation. So, downstairs-"

        r "--Yeah. I pretty much get what's going on."

        r "... I think the 'rules' are pretty serious here."

        r "It would be best to behave for now, May."

        "If Rae's bossing me around, I guess it's a big deal."

        "Though the way he interrupted me is as annoying as usual." #not sure about this line

        tm "Did Grei already show up?"

        r "Yep! Got a rundown of the rules."

        tm "Oh, right. I left before I got to hear those."

        tm "Did you break one already?"

        r "I tried!" 

        tm "..." 

        r "..." 

        r "That's the thing."

        r "The punishments are real, and..." 

        r "Ah, whatever. Let's just play this little game."

        r "I didn't kill Paul, but I did mess with him last night."

        tm " "

        r "Don't give me that look!"

        r "I wasn't trying to permanently hurt him or anything!"

        r "He was drunk and drinking, so I gave him a special treat."

        r "It was supposed to make him feel a bit bad for a little while, that's all."

        tm "... You were trying to knock him out for the rest of the trip."

        r "Yeah basically. Besides, you know if I had killed him there wouldn't have been a body to find."

        tm "I know." 

        tm "Is that all the info you have?"

        r "Yep! Not sure who did everything else, I went back to my room after that." 

        r "Who would've thought he'd be so messed up by the time I saw him again, haha!"

        tm "You saw the body?"

        r "Yep! Didn't get to really examine it, though. Laceration wounds, likely a knife, cause of death undeterminable from observation." 

        tm "... How far away from the body were you?"

        r "Don't give me that look!" 

        r "I didn't get to go downstairs before Grei caught me."

        r "Ugh… The weapon was probably nice and sharp? The cuts looked clean." 

        tm "Alright, good enough."

        r "Cool. I'm not allowed to help out other than as a witness, and Grei told me to go to the lobby after interrogation." 

        tm "Any other rules I should know?"

        r "Oh, yeah! Important one. You're not allowed to harm the suspects."

        tm "... At all?"

        r "Nothing bigger than a bug bite!" 

        tm "That's oddly specific."

        r "Eh, Grei was using some awful script on me so that's what I got out of it."

        r "Have fun with the other suspects! I don't think there's a rule that they can't hurt you." 

        tm "... Great." 

        "I guess that's what the ropes are for."

        r "Oh! And the employees should be interrogable too. It's not in the rules or anything, but it seems pretty obvious some of them should have seen things." 

        tm "Hm…" #smiling

        "Rae heads to the lobby, and I follow him there." 

        # rae goes to the lobby and tm has the chance to inspect the room.
        
        # Added to inventory: Rae's evidence (poison bottle)

        # → Items: Hail's Debut CD (collectible), Luggage case (commentable)

        # Hail's Debut CD: Go Away/I am my own god (Debut Single)

        jump locations

    else:

        "IHSJDNGIJSDKGNJSDNFJ" #TODO

        jump locations

# tm goes to the other rooms "randomly", though they're scripted linearly.

# Room backtracking is possible, except the lobby. 

label locations:

    "Where would you like to go?"

    if solar_visited and hail_visited and mye_visited:

        menu:
            
            "Lobby":

                jump lobby

            "Kitchen":

                jump kitchen

            "Pool":

                jump pool

            "Patio":

                jump patio

            "Hallway":

                jump hallway

            "Go to one of the bedrooms":

                jump bedrooms

            "I'm done viewing the rooms":

                jump back_to_lobby

    elif solar_visited and hail_visited:

        if not pool:

            menu:
            
                "Lobby":

                    jump lobby

                "Kitchen":

                    jump kitchen

                "Pool":

                    jump pool

                "Hallway":

                    jump hallway

                "Go to one of the bedrooms":
                    jump bedrooms
        
        else: 

            menu:
            
                "Lobby":

                    jump lobby

                "Kitchen":

                    jump kitchen

                "Pool":

                    jump pool

                "Patio":

                    jump patio

                "Hallway":

                    jump hallway

                "Go to one of the bedrooms":
                    jump bedrooms

    elif solar_visited:

        menu:
            
            "Lobby":

                jump lobby

            "Kitchen":

                jump kitchen

            "Hallway":

                jump hallway

            "Go to one of the bedrooms":

                jump bedrooms

    else:

        menu:
            
            "Lobby":

                jump lobby

            "Kitchen":

                jump kitchen

            "Go to one of the bedrooms":

                jump bedrooms


label bedrooms:

    "Who's room would you like to go to?"

    if solar_visited:

        if hail_visited:

            if mye_visited:

                menu:

                    "Rae's Bedroom":

                        jump rae_room

                    "Solar's Bedroom":

                        jump solar_room

                    "Hail's Bedroom":

                        jump hail_room

                    "Mye's Bedroom":

                        jump mye_room

                    "I want to go somewhere else instead.":

                        jump locations

            else:

                menu:

                    "Rae's Bedroom":

                        jump rae_room

                    "Solar's Bedroom":

                        jump solar_room
                        
                    "Hail's Bedroom":

                        jump hail_room

                    "I want to go somewhere else instead.":

                        jump locations

        elif mye_visited:

            menu:

                "Rae's Bedroom":

                    jump rae_room

                "Solar's Bedroom":

                    jump solar_room

                "Mye's Bedroom":

                    jump mye_room

                "I want to go somewhere else instead.":

                    jump locations

        else:

            menu:

                "Rae's Bedroom":

                    jump rae_room

                "Solar's Bedroom":

                    jump solar_room

                "I want to go somewhere else instead.":

                    jump locations

    elif hail_visited:

        if mye_visited:

            menu:

                "Rae's Bedroom":

                    jump rae_room
                    
                "Hail's Bedroom":

                    jump hail_room

                "Mye's Bedroom":

                    jump mye_room

                "I want to go somewhere else instead.":

                    jump locations

        else:

            menu:

                "Rae's Bedroom":

                    jump rae_room
                    
                "Hail's Bedroom":

                    jump hail_room

                "I want to go somewhere else instead.":

                    jump locations

    elif mye_visited:

        menu:

            "Rae's Bedroom":

                jump rae_room

            "Mye's Bedroom":

                jump mye_room

            "I want to go somewhere else instead.":

                jump locations

    else:

        menu:

            "Rae's Bedroom":

                jump rae_room

            "I want to go somewhere else instead.":

                jump locations

# Go to: Lobby (removed, Grei), Kitchen (chef), Pool (employee, purple), Patio (employee, pink), Hallway (employee, scar) 

# so choose a spot to go (scripted), get 1 key, go to next room. 

label lobby:

    if not lobby:

        $ lobby = True
        
        g "Once individual interrogation is done, the detective is no longer allowed to speak to the suspects." 

        tm "So they're just chilling here until I'm done?"

        g "Yep."

        tm "... Are suspects allowed to hurt each other?"

        g "Yep."

        "... Good thing I sent Rae first. He should be able to damage control if anything happens." 

        "I think about what Rae said. If the weapon was a knife, then…"

        tm "Well, I should check the kitchen first."     

        jump locations
    
    elif not kitchen:

        "I should check the kitchen first." #ToDo

        jump locations

    else:

        "GHSDJGHNIHAESB IHEAF" #TODO

        jump locations


label kitchen:

    if not kitchen:

        $ kitchen = True
            
        "The chef I met earlier is here."

        e "Here for a key?"

        tm "What?"

        e "Oh, you didn't even know?"

        e "The first room you decide to open is a freebie. The rest need a key from an employee to open." 

        tm "..."

        e "..."

        tm "And you're not just going to hand it over."

        e "Nope! That'd be no fun. We get bored around here, you know."

        tm "Can't you all just play with the corpse or something."

        e "Ew, no. Well… Some of us used to but they're all bored of it at this point." 

        tm "That many murders happen here?"

        e "... This isn't a normal resort, I think you and your partner are bright enough to have noticed." 

        e "But anyways! Yeah, I'm pretty pissed!"

        e "I'll be nice, because I'm pissed off!"

        e "Someone stole one of my kitchen knives." 

        "Oh, that'd be great evidence if I find it."

        e "They put back that filthy thing like I wouldn't notice?"

        tm "..."

        e "You have to wash things that touch blood, especially nasty little man blood, thoroughly! You can't just run water and think that's good enough!" 
        
        tm "..."

        e "And I better not see you inside the kitchen. Ever."

        e "I'm already trying not to snap at the person who put their disgusting little footprints on my floor." 

        tm "You know who it was?"

        e "I could tell from the shoe prints… ugh… I feel sick just remembering it." 

        e "Anyways, whatever. Here's your key, the others will probably ask you to do something annoying first."        
            
        "Item acquired: Room Key." 
        "Evidence Collected: Stolen Knife from Kitchen (Testimony)"
        # "Someone stole one of my kitchen knives. / I'm already trying not to snap at the person who put their nasty little footprints on my floor." 

        tm "This is for.. Room 03." 

        jump solar_room
    
    else:

        e "I already told you everything I know. Go away now" #TODO

        jump locations


label solar_room:

    if not solar_visited:

        $ solar_visited = True

        "The blue-haired person I bumped into on the patio is here." 

        "They flinched really badly when I opened the door, and they're sweating really badly."

        "This would be so much easier if I could treat this like work…"

        tm "Hey, what's your name?"

        s "... S-solar."

        tm "Solar, if I undo the ropes, you won't do anything odd, right?"

        s "I, I won't." 

        "I make eye contact with them as I undo the ropes. Yeah, they definitely did something."
        
        tm "First kill?"

        "They nearly fall off the chair." 

        "… It's been a while since I've had a suspect this easy." 
        
        "Crouching over, I put my hands on their shoulders"

        tm "You're a very lucky person." 

        tm "Do you live in the XX area?"

        "Their eyes widen as they look up at me." 

        s "H-how did you…"
        
        "Your bag has your University's Mascot on it, silly."     

        tm "That's very, very lucky for you. That area has a lot of clients of mine."

        "Well… there and more." 
        
        tm "Whatever happens to you, I can protect you."
        
        tm "From law enforcement, government officials, to the people who stay behind the scenes."
        
        tm "I have a very good relationship with every. single. one." 

        tm "I can help you. Can you trust me?"

        # CG Solar

        s "..."

        "Solar looks at me, their eyes shaking." 

        "... But glinting with hope." 

        s "You… Who are you?"

        # CG Taylor May
        
        tm "I'm a detective with a 100\% success rate, and 100\% clean record." 

        tm "That makes me very, very important to a lot of people." 

        tm "So I can help you, Solar." 

        tm "Don't worry, I'll take care of everything for you." 

        #CG back to normal. Solar leaves
        
        tm "Hmm… well, not too bad I guess."

        tm "I'm not sure I have the full picture here, but Rae poisoned Paul and at some point Paul bumped into Solar." 

        tm "Solar definitely did something… but they still wouldn't say what." 

        "There wasn't much blood around the death site, so Paul must have been pretty inpacitated by the time he got slashed up." 

        tm "Well… Regardless, I need to free the other suspects from their rooms." 

        #explore Solar's room

        # Evidence Acquired: Just a Backpack. 

        # Just a Backpack: Solar's only luggage is this small bag. Other than his wallet, there's nothing else in it. Not even a spare change of clothes." 

        # when rae and solar are alone, they have a conversation. tm pov is cut off for the inbetween scenes

        jump rae_solar_cut_scene 

    else:

        "IHSJDNGIJSDKGNJSDNFJ" #TODO

        jump locations


label rae_solar_cut_scene: #TODO

    r "..."

    s "..." 

    r "You have a crush on May, don't you?"

    s "W-what?"

    r "He told you he could save you, and you saw the halo around his head?"

    s "I…" 

    r "I've seen it happen plenty of times."

    "Solar is looking down and sweating."

    "Well, he's been sweating the whole time." 

    r "Tell me, who's the person you love most in the world?"

    s "..."

    s "I don't really have anyone like that."

    r "Then you can't date May."

    s "No, well, I mean, I only just met him…"

    r "No. It's you."

    r "The answer should've been yourself."

    r "Love yourself more than anyone else, prioritize yourself the most."

    r "You can't date May if you can't do that."

    r "You haven't seen it. May only has a half-hearted hero complex."

    r "He'll save you, he'll like that you're infatuated with him."

    r "And then he'll get tired of you." 

    s "... How do you know that?"

    r "Because I dated him. :/"

    r "And I'm the only ex he has that's still alive." 

    s "He killed them!?" 

    r "Umm no? Why would he do that?"

    s "But you said…" 

    r "The only people who fall in love with May are little desperate and suicidal bitches like you." 

    r "May can't stand having 'useless people' around him past the honeymoon phase."

    r "How do you think someone who just found their savior would feel when they're abandoned?"

    menu:
        "That's horrible…":

            r "Yeah, it's pretty shitty to half-ass things."

            r "Just take his help for now and walk on your own feet after."  

        "But I still like him.":

            r "Hm? Really?"

            r "Then…"

    r "Good luck." 

    jump locations


label hallway:

    if not hallway:

        $ hallway = True

        "There's an employee here. I don't remember seeing him before."

        menu:
        
            "Is your mouth ok?":

                e "Is your face ok, ugly?"
            
                e "Liike, um, hello. Nice to meet you too." 
            
                tm "Sorry, that was my bad."
        
            "Hey.":
            
                e "Heyy. Whatsup?"
            
        tm "I'm Taylor May, I was wondering if you saw anything last night." 

        e "Sure I did. Most of us are up during the night." 

        tm "Then…"

        e "You don't think you're getting info for free, right?" 

        tm "... What do you want." 

        e "Don't look at me like that lol. I'm not as tough to please as the other cunts around here. I just want a signature from Hail."

        "No, that's probably the hardest thing you could ask for." 

        e "Oh, and tell Rae he was pretty good last night."

        tm "Absolutely not."

        e "Buzzkill."

        "Quest received: Hail's signature." 

        "How the hell am I supposed to do this?"

        tm "... Wait." 

        tm "Were you with Rae all night last night?" 

        e "Yeah duh." 

        e "... Oh. Oops." 

        tm "Your evidence is just that Rae didn't leave his room at all last night, isn't it?"

        e "..."

        e "At least get me one of the chef's parfaits for me pleaase." 

        tm "Oh my god." 

        jump kitchen_for_parfait

    if hallway:

        "I don't really want to hear more about their escapades..." #TODO

        jump locations


label kitchen_for_parfait:

    e "Someone asked for one of my parfaits, right?"

    tm "Yep."

    e "Yeah they always do." 

    e "Who's it for."

    tm "Employee in pink."

    e "... What shade of pink?"

    tm "Pastel?"

    e "No problem. One parfait." 

    e "Tell him to swing by after work ends."

    tm "..." 

    tm "Popular guy." 

    e "I knoww. I've been trying to go steady with him for forever. I'd still let him play his games, I don't know why he's so against it." 

    e "I just want to spend more time together, you know?"

    tm "I guess."

    e "We have plenty of time here, anyway." 

    "Acquired: Perfect Parfait." 

    jump back_to_hallway


label back_to_hallway:
    
    e "Didya get it?"
    
    "I hand over the parfait."
    
    e "Yayy! Chef's parfaits are the best."
    
    tm "He said to drop by after work for it." 
    
    e "Ugh noo… Chef plays too rough." 
    
    e "My [[redacted] totally [[redacted] when he [[redacted] [[redacted] [[redacted], not to mention when he-"
    
    tm "I really don't need to know, man." 
    
    e "Totaall buzzkill." 
    
    e "I might go tonight though, I don't mind it half the time."
    
    tm "Just give me the key." 

    "Acquired: Room Key." 
    
    e "Have fun in there, lucky man." 

    "... I have a guess who's in Room 02."

    jump hail_room


label hail_room:

    if not hail_visited:

        $ hail_visited = True
        
        "Hail is tied up on the chair, as expected. He seems pretty calm, but if looks could kill..." 

        "With the 'can't attack but can't defend' rules, it'd probably be bad." 

        tm "Can you behave if I let you go? Trust me, I'm not doing this 'cause I want to." 

        h "... Trust you?"
        
        tm "I've heard a lot about you from my work partner." 

        h "He's a fan."

        "Right, this guy hates the vast majority of his fans. Violently."

        tm "Listen, he thinks I don't know but…"
        
        tm "He's the one that's been cleaning up your little messes." 

        h "Oh?"

        tm "He's good at it. Nothing left to find, right?"

        h "... Hm. Yeah. I made an exception and send him my new songs early." 

        tm "I know. He skips work for it every time." 

        tm "With song titles like 'the creep that was following me is in the alleyway next to the park, and you won't find a trace of him just like the rest.'"

        tm "Rae… how did you think I wouldn't know." 
        
        h "You sure you're not a fan?"

        "I said all of that out loud, didn't I." 

        tm "... I like your older songs more." 

        h "..." 

        h "Bad taste." 

        "I undo his ropes."
        
        tm "So did you do anything to that guy last night?"

        h "You really think I'm going to answer that?"

        tm "Was worth a shot." 

        h "It's too bad your partner couldn't come this time. I have a pocket knife on me."

        h "Didn't have time to toss it out, so think of it what you will." 

        h "But you know, my record is very, very clean." 

        "He winks at me. I kind of get why he has so many hardcore fans." 

        tm "... There's only one more person after you, wait in the lobby for a bit. Don't start anything. Rae will stop you if you do." 

        h "There's nothing to start, anyway." 

        # hail leaves

        tm "Well… I know Hail has the temperment to have done something."

        "The pocketknife is clean, obviously. He may be an amateur, but he wouldn't be dumb enough to leave blood on it." 
        
        "Evidence Acquired: Pocket Knife." 

        # explore room - [[laptop = collectible, suitcase = observable]

        "Evidence Acquired: Old E-mails." 
    
        # Old E-mails: Between Hail and Rae, it's pretty obvious. Rae wrote whole paragraphs while Hail replies with about two words max… I'm surprised he took the time to read through these." 

        jump rae_solar_hail

    else:

        "IHSJDNGIJSDKGNJSDNFJ" #TODO

        jump locations


label rae_solar_hail:

    r "..."

    s "..."

    h "..."

    "It's dead silent in the lobby."

    "If the employees weren't so good at cleaning, there would be at least a few flies to break the silence."

    jump locations


label pool:

    if not pool:

        $ pool = True

        "Surprisingly, there's an employee in front of the pool." 

        e "The one with the blue hair was on the patio for a very long time."

        e "Other than that, I don't have anything for you."

        tm "Thanks for letting me know." 

        e "If you need my help later… I'd like you to get the pool room key." 

        tm "Your help?"

        e "..." 

        "Not going to clarify, huh." 
        
        tm "Where would I get the pool room key?"
        
        e "The store will open up soon. You can get it then." 
        
        tm "So it opens after this play-trial ends?"
        
        e "There's no point in going to the rec room before then."

        if solar_visited and hail_visited:
        
            e "The last employee with a key should be on the patio."  #just in case they haven't been everywhere yet.
        
        tm "Thank you."

        jump locations

    elif not patio:

        "I should go see the employee on the patio." #TODO

        jump locations

    else: 

        e "You're back?" #TODO

        jump locations


label patio:

    if not patio:

        $ patio = True

        "I head to the patio. Like the employee said, there's someone here."

        e "Hii." 
        
        tm "What do you want."
        
        e "Aw, you're no fun." 
        
        tm "I've gotten that a few times today." 
        
        e "Chef's parfait!"
        
        "I guess I need to go see him again."

        jump kitchen_for_parfait_2
    
    else:

        "sidhgjaksngdkjasn" #TODO

        jump locations


label kitchen_for_parfait_2:

    e "Back again."

    tm "I need another parfait."

    e "Which employee?"

    tm "Hot pink."

    "He looks at me, and I look at him."

    e "No."

    tm "Why."

    e "I don't get anything out of that."

    "I guess it's time to improvise." 

    tm "You know, there's no rule about hurting employees, is there?"

    e "Oh? Want to try and find out?"

    tm "I was hoping I could ask that question." 

    tm "But regular employees aren't allowed to leave their assigned area, are they?"

    "Why else would one just be standing in the hallway all day." 

    e "..."

    tm "And I haven't set a single foot into your kitchen."

    tm "You guys know quite a bit about me."

    tm "But do you know how well I fight?"

    tm "Do you think your beau could win?"

    tm "He didn't seem all that fit."

    e "..." 

    e "He'd win, in a normal fight."

    e "You're lucky there are rules about employees hurting players." 

    tm "Players?"

    e "Ah, whatever. Take the parfait and leave." 

    e "That was pretty good though." 

    e "We're all a bit curious about how your... work record is so well done."

    e "I wouldn't mind if you want to play around after this game is over."

    tm "So you like playing around too."

    e "Most of us do. It gets boring at the resort off-season, you know."

    "Item acquired: Half-assed Parfait."

    "'Players,' 'rules', and 'game,' huh."
    
    "I hate unpaid work, but I'm curious about this resort." 

    jump back_to_patio


label back_to_patio:

    tm "Here. It was a pain to get."

    e "Mann I get the leftovers again."

    e "Well, that's the usual."

    e "Umm. I saw that guy, Hail, for a second last night."
    
    "Evidence acquired: Hail (testimony)."
    
    "Item acquired: Room Key."

    "Only one room left." 

    jump mye_room


label mye_room:

    if not mye_visited:

        $ mye_visited = True

        "Hello."

        "I don't know much about this person, and I can't gather much just from looking at him right now."

        "Other than that he's pretty calm."

        tm "What's your name?"

        m "Mye."

        tm "Could you please behave if I undo the ropes?"

        m "You're not going to question me while I'm still tied up?"

        tm "This really isn't the kind of interrogation process I'm used to. I don't really see a point to asking questions when you can just lie through it." 

        m "Hm. Well, I don't really care."

        m "I took this trip on a whim to get inspiration by the beach. Not get tied up in my room."

        m "I really do hope this resort provides return services." 

        "Yeah… something tells me no one's getting their deposit back." 

        "I undo his ropes." 

        "Mye leaves without another word." 

        tm "... I wish I could use my work tools." 

        "Solar is pretty easy to read, so that went fine."

        "But the murder was pretty gruesome, and I still don't know the exact cause of death."

        # "Seriously… with these useless interrogations and not being able to inspect the corpse… what are they expecting from me?"
        #unsure if i want this statement since there's a similar one later on

        # Room exploration time
        # Collectible: knife; observable: briefcase

        "Huh?"

        "These are…"

        tm "These are the knives used by the xx area serial killer."

        "The shape and sizes of the blades, their unique curve, their impossible sharpness."

        "The xx area serial killer is a mysterious individual that slashes their victims after death."

        "Wounds as clean as scalpel cuts, and slashes are deep enough to expose bones."

        "There have been a few copycats, but I could always tell which ones were the fakes." 

        tm "I…"

        tm "I'm…"

        #cg tm happy

        tm "I'm such a big fan." 

        "I grab a knife. It cuts through my fingers like it's nothing."

        "Even with this, I don't feel pain well. How deep did Rae say was too deep?"

        "This much is fine right? Just a little bit more is fine, right?"

        "Acquired: Knife Briefcase." 

        jump locations

    else:

        "IHSJDNGIJSDKGNJSDNFJ" #TODO

        jump locations


label back_to_lobby:

    r "May, what the hell happened to your hand?"

    tm "... I got carried away."

    "I pretend to ignore the stares I feel on me."

    g "Medic." 

    "The employee in the purple dress comes over." 

    "She bandages my hand with ease." 

    g "Dear guest, I hope you have gathered all the information you need."

    g "Judgment will begin shortly, but first, how about you all get to know each other?"

    tm "Do we really have-"

    g "You have to. Hurry it up." 

    g "I'm supposed to call out your names from this list, but I think most of you wouldn't want me to say these names out loud." 

    g "This isn't a classroom, so just start yourselves." 

    "..." 

    r "Hii I'm Rae! I'm May's one-and-only assistant. I do little jobs like deliveries and taking out trash!"

    "Very Rae of Rae to go first." 

    tm "He does everything I don't, and very well." 

    tm "I'm Taylor May, a freelance detective."

    tm "I wasn't hired for this case, and I really wouldn't have done anything if I hadn't been forced to." 

    s "... I-I'm Solar… I'm a university student." 

    h "Hail. Singer."

    m "Mye. Fashion designer." 

    g "Good enough."

    tm "Seriously?"

    g "Our dearest guest. What conclusion have you come to?"

    "Who committed the crime?"

    "With this amount of evidence… it feels like a damn guessing game." 

    "(Game master recommends you save here!)"

    jump chose_killers


label chose_killers:

    "Who killed Paul? You may select up to 4 guilty parties. If you've made a mistake you can just reselect them." #TODO

    "So far you have accused:"

    if rae:

        "Rae."

    if solar:

        "Solar."

    if hail:

        "Hail."

    if mye:

        "Mye."

    if not rae and not solar and not hail and not mye:

        "No one."
       
    menu: 

        "Rae":

            if not rae:

                $ rae = True
                $ killers += 1
                jump rae

            if rae:

                $ rae = False
                $ killers -= 1
                jump chose_killers

        "Solar":

            if not solar:

                $ solar = True
                $ killers += 1
                jump solar

            if solar:

                $ solar = False
                $ killers -= 1
                jump chose_killers

        "Hail":

            if not hail:

                $ hail = True
                $ killers += 1
                jump hail

            if hail:

                $ hail = False
                $ killers -= 1
                jump chose_killers

        "Mye":

            if not mye:

                $ mye = True
                $ killers += 1
                jump mye #TODO

            if mye:

                $ mye = False
                $ killers -= 1
                jump chose_killers

        "That's everyone.":

            jump evaluate_killers

    # if rae: 

    #     if solar: 

    #         if hail: 

    #             menu: #rae, solar, and hail accused

    #                 "Mye":
    #                     $ mye = True
    #                     $ killers += 1
    #                     jump myeDO

    #                 "That's everyone.":
    #                     jump evaluate_killers

    #         elif mye:

    #             menu: #rae, solar, and mye accused

    #                 "Hail":
    #                     $ hail = True
    #                     $ killers += 1
    #                     jump hail

    #                 "That's everyone.":
    #                     jump evaluate_killers

    #         else: 

    #             menu: #rae and solar accused

    #                 "Hail":
    #                     $ hail = True
    #                     $ killers += 1
    #                     jump hail

    #                 "Mye":
    #                     $ mye = True
    #                     $ killers += 1
    #                     jump myeDO

    #                 "That's everyone.":
    #                     jump evaluate_killers

    #     elif hail:

    #         if mye:

    #             menu: #rae, hail, and mye accused

    #                 "Solar":
    #                     $ solar = True
    #                     $ killers += 1
    #                     jump solar

    #                 "That's everyone.":
    #                     jump evaluate_killers

    #         else:

    #             menu: #rae and hail accused

    #                 "Solar":
    #                     $ solar = True
    #                     $ killers += 1
    #                     jump solar

    #                 "Mye":
    #                     $ mye = True
    #                     $ killers += 1
    #                     jump myeDO

    #                 "That's everyone.":
    #                     jump evaluate_killers

    #     elif mye:

    #         menu: #rae and mye accused

    #             "Solar":
    #                 $ solar = True
    #                 $ killers += 1
    #                 jump solar

    #             "Hail":
    #                 $ hail = True
    #                 $ killers += 1
    #                 jump hail
                
    #             "That's everyone.":
    #                 jump evaluate_killers

    #     else:

    #         menu: #rae accused

    #             "Solar":
    #                 $ solar = True
    #                 $ killers += 1
    #                 jump solar

    #             "Hail":
    #                 $ hail = True
    #                 $ killers += 1
    #                 jump hail

    #             "Mye":
    #                 $ mye = True
    #                 $ killers += 1
    #                 jump myeDO

    #             "That's everyone.":
    #                 jump evaluate_killers

    # elif solar:

    #     if hail:

    #         if mye:

    #             menu: #solar, hail, and mye accused

    #                 "Rae":
    #                     $ rae = True
    #                     $ killers += 1
    #                     jump rae

    #                 "That's everyone.":
    #                     jump evaluate_killers

    #         else:

    #             menu: #solar and hail accused

    #                 "Rae":
    #                     $ rae = True
    #                     $ killers += 1
    #                     jump rae

    #                 "Mye":
    #                     $ mye = True
    #                     $ killers += 1
    #                     jump myeDO

    #                 "That's everyone.":
    #                     jump evaluate_killers

    #     elif mye:

    #         menu: #solar and mye accused

    #             "Rae":
    #                 $ rae = True
    #                 $ killers += 1
    #                 jump rae

    #             "Hail":
    #                 $ hail = True
    #                 $ killers += 1
    #                 jump hail

    #             "That's everyone.":
    #                 jump evaluate_killers

    #     else:

    #         menu: #solar accused

    #             "Rae":
    #                 $ rae = True
    #                 $ killers += 1
    #                 jump rae

    #             "Solar":
    #                 $ solar = True
    #                 $ killers += 1
    #                 jump solar

    #             "Hail":
    #                 $ hail = True
    #                 $ killers += 1
    #                 jump hail

    #             "Mye":
    #                 $ mye = True
    #                 $ killers += 1
    #                 jump myeDO

    #             "That's everyone.":
    #                 jump evaluate_killers

    # elif hail:

    #     if mye:

    #         menu: #hail and mye accused

    #             "Rae":
    #                 $ rae = True
    #                 $ killers += 1
    #                 jump rae

    #             "Solar":
    #                 $ solar = True
    #                 $ killers += 1
    #                 jump solar

    #             "That's everyone.":
    #                 jump evaluate_killers

    #     else:

    #         menu: #hail accused

    #             "Rae":
    #                 $ rae = True
    #                 $ killers += 1
    #                 jump rae

    #             "Solar":
    #                 $ solar = True
    #                 $ killers += 1
    #                 jump solar

    #             "Mye":
    #                 $ mye = True
    #                 $ killers += 1
    #                 jump myeDO

    #             "That's everyone.":
    #                 jump evaluate_killers

    # elif mye:

    #     menu: #mye accused

    #         "Rae":
    #             $ rae = True
    #             $ killers += 1
    #             jump rae

    #         "Solar":
    #             $ solar = True
    #             $ killers += 1
    #             jump solar

    #         "Hail":
    #             $ hail = True
    #             $ killers += 1
    #             jump hail

    #         "That's everyone.":
    #             jump evaluate_killers

    # else:

    #     menu: #no one accused yet

    #         "Rae":
    #             $ rae = True
    #             $ killers += 1
    #             jump rae

    #         "Solar":
    #             $ solar = True
    #             $ killers += 1
    #             jump solar

    #         "Hail":
    #             $ hail = True
    #             $ killers += 1
    #             jump hail

    #         "Mye":
    #             $ mye = True
    #             $ killers += 1
    #             jump myeDO


label evaluate_killers:

    if killers == 1:
        jump single_accusation

    elif killers == 4 or killers == 2:
        jump partially_incorrect

    elif killers == 3:
        if rae and hail and solar:
            jump completely_correct
        else:
            jump partially_incorrect


label hail:

    g "Guest Hail, you have been accused of the crime of stabbing Guest Paul with a pocketknife of your own possession." 

    g "Do you have anything to say for your crime?"

    h "... He bumped into me and got drool on my shirt. It was disgusting." 

    "Rae nods voraciously."

    jump chose_killers


label rae:

    "Guest Rae, you have been accused of the crime of poisoning the Guest Paul." 

    r "Well like yeah but that didn't kill him."

    r "I mean I'll take the fall, I guess."

    jump chose_killers
    

label solar:

    g "Guest Solar, you have been accused of the crime of cutting Guesting Paul into a horrible mess, with a knife taken from the kitchen."

    e "I hate you." # chef

    g "Do you have anything to say for your crime?"

    s "I… I…"

    "They glance at me."

    s "I was going to kill myself here… I spent all my money and… I didn't have anything left behind…"

    s "I was going to do it, really, but I thought I should at least enjoy one day… since I paid so much…" 

    "Their eyes take on an odd shine."

    s "But then, I saw that person beat me to it."

    s "I got so mad."

    s "I'd never been so angry before."

    s "I was furious… I, I just snapped."

    s "..." 

    "Solar goes silent." 

    jump chose_killers

    
label mye: #TODO


label single_accusation:

    if mye:
        jump completely_incorrect

    g "Yes, that's correct. I applaud you."

    # maybe branch off into individual scenarios here

    tm "Great, so-"

    g "Unfortunately, dear guest, a story's ending is no good without the truth, the whole truth, and nothing but the truth."

    g "You didn't think you could get away with half-assing the job, did you?"

    tm "..." 

    jump bad_end


label partially_incorrect:

    g "... My dear guest. Unfortunately, there was an error in your deductions."

    g "Some parts of that accusation were irrelevant." 

    jump bad_end


label completely_incorrect:

    g "... My dear guest. Unfortunately, there was an error in your deductions."

    g "Not a single part of that accusation was relevant." 

    jump bad_end


label bad_end:

    g "Unfortunately, you have lost the first round." 

    g "We cannot continue forward like this."

    g "Do you have any final words?"

    tm "You guys should ease up with the rules here."

    g "Yeah, I wish."

    "With an odd sound, my vision goes blank." 

    "I couldn't see what happened, but I could tell very well what was happening to me." 

    # "I'm dying." not sure about this line

    "I hear screams, they sound distant."

    "I need to help Rae, but my vision won't come back."

    "I can feel it, vaguely, the blood rushing out of my body."

    "Whatever they did, it was really effective."

    "It almost hurts." 

    "I wonder who attacked me."

    tm "... I never expected to die here."

    "[[ENDING: Bad End]"

    return


label completely_correct:

    g "Esteemed guest, you have concluded this case perfectly."

    g "As witnessed by the resort, this murder was committed in three acts."

    g "Guest Rae poisoned the victim, leaving him intoxicated and vulnerable."

    g "Guest Hail stabbed the victim with a pocketknife, leaving him immobile."

    g "And Guest Solar slashed his body with a knife from the kitchen, leaving his corpse a mess." 

    e "Yeah fuck you in particular, buddy." #chef

    g "But the question remains: Who killed Guest Paul?"

    g "The resort has made an exception due to the complexity of this crime, and as well has given you another chance to learn about each other."

    g "All victims of each guest will appear above their heads."

    g "The resort has eyes, and it knows the truth of these matters."

    "[[Rae: 0 victims.]"

    "Hail in particular seems surprised."

    "[[Hail: X victims.]"

    "Rae nods in agreement. Paul isn't on his list." 

    "[[Solar: 1 victim.]"

    "So Solar did the finishing blow. From the way he's about to puke… he probably didn't know Paul wasn't dead when he found him."

    "[[Mye: XX victims.]"

    "Oh? So there are some victims that were never discovered." 

    "[[Taylor May: XXX victims.]"

    "The others look at me with expressions of either surprise or shock."

    "The employees seem to have already known."

    r "May won! Does he get a prize? Does he get to split it?"

    tm "Rae, this wasn't a contest."

    h "How the hell have you killed this many people and gotten away with it?"

    tm "I'm very good at my job. And as you know, Rae is very good at cleanup."

    r "And deliveries!"

    e "Hey, hey, so can you tell us about how you kill people?" #pastel pink

    tm "Well—"

    unknown "Guests and employees!"

    unknown "Questions can wait!"

    "The employees have all stiffened up."

    "Then, this voice must be…"

    unknown "My dear contestants, my lovely players, congratulations on successfully finishing your first round of my resort game."

    unknown "Unfortunately, there is no prize until you finish round two."

    tm "... No fucking way."

    unknown "This game has yet to be completed!"

    unknown "Your next challenge is, dear Taylor-"

    "It's Taylor May…"

    unknown "--is to answer a simple question!"

    unknown "And that question is…"
    
    # cg demon

    d "Who summoned a demon to the party?"

    return