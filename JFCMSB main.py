# TODO: Add top text to images in jetfuel_images. Probably going to have to re-do all the links and make a new imgbb album.

import discord
import jetfuel as jf
import jetfuel_images as jf_i
TOKEN = 'ODc5MDg1MjY0MTQyNzI5MjI3.YSKl8w.2A6xJXipWwHF8zC66ItTvX7WU3A'

class based_bot(discord.Client):     
    async def on_ready(self):
        print("I {0.user} have your wife and kids".format(client))

    async def on_message(self, message):
        username = str(message.author.name) # Stores username of message sender in variable
        usr_msg = str(message.content) # Stores message content in variable
        channel = str(message.channel.name) # Stores channel name in variable
        print(f'{username}: {usr_msg} ({channel})') # Prints channel logs to Python's stdout
        #print(f'{usr_msg.lower()}, {usr_msg.lower()[0]}, {usr_msg.lower()[-1]}')
        #print(dir(message.author), '\n',  dir(message.content), '\n', dir(message.channel))

        #for i in range(60):
        #    await message.channel.send('chanceisgod'*29)
        
        
        if message.author == client.user: # Disables bot from responding to itself
            return
        
        if jf.find(usr_msg.lower(),['https']): # Disables responding to text in links
            return
        if usr_msg.lower()[0] == '<' and usr_msg.lower()[-1] == '>' or usr_msg.lower()[0] == '<' or usr_msg.lower()[-1] == '>':
            return

        ##if message.channel.name == 'general': # Set channel name for bot to monitor and respond to messages in
        # Write new messages/responses using the formats below

        # Copypastas
        if usr_msg.lower() == 'what the fuck did you just say about me?':      # Marine Copypasta
            await message.channel.send('You little bitch. I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, '
            'and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US Armed Forces. You are nothing to me but just another target. '
            'I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that '
            'shit to me over the Internet? Think again, fucker. As we speak, I am contacting my secret network of spies across the USA and your IP is being traced right now so you better '
            'prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill '
            'you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the '
            'United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known '
            'what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and '
            'now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.')

        elif usr_msg.lower() == 'tell me about the rabbit from zootopia':      # Zootopia Copypasta
            await message.channel.send("So, you know that rabbit from Zootopia? Yeah, I genuinely don\'t think that cooch ever ends. "
             "It\'s a black hole that goes on forever, because I\'ve seen yiff where she gets fucked by a dude who has a cock that\'s "
             "almost twice her size, yet she still manages to both stay alive and experience pleasure from what other beings would be a certain death, "
             "I don\'t even think she has any organs other that her genitals, and even then, how does the dick not come out to the other side? "
             "It\'s almost as if the dick enters a wormhole or something like that.\n\nI swear man, that coochie\'s lovecraftian. It scares me...")

        elif jf.find(usr_msg.lower(),['among us','amongus','amogus']):        # Amogus Copypasta
            await message.channel.send('STOP POSTING ABOUT AMONG US, I\'M TIRED OF SEEING IT! My friends on TikTok send me memes, on Discord it\'s fucking memes, '
            'i was in a server, right? and ALL of the channels are just Among Us stuff. I-I showed my Champion underwear to my girlfriend, and the logo i flipped it and '
            'i said \"Hey babe, when the underwear sus HAHA ding ding ding ding ding ding ding ding ding ding\" I FUCKING LOOKED AT A TRASH CAN, I SAID \"THAT\'S A BIT SUSSY\", '
            'I LOOKED AT MY PENIS, I THINK OF THE ASTRONAUT\'S HELMET, AND I GO \"PENIS, more like peenSUS\" AAAAAAAAAAAAAAA')
            
        
        # Odds and Ends
        if usr_msg.lower() == '!random':     # le 'random'
            response = f'This is your random number: 5'
            await message.channel.send(response)
        if usr_msg.lower() == 'i\'m about to have a certified gamer moment':     # Gamer moment
            await message.channel.send(f'User {username} has been banned from channel')
        if usr_msg.lower() == '!randomeme':     # Randomeme: the AI generated random meme function
            await message.channel.send(jf.randomeme())
        if usr_msg.lower() == 'who is chubs?':  # Chubs the Penguin
            await message.channel.send('I have done indescribable, horrid things to this penguin named Chubs')
            #await message.channel.send('I pumped a ridiculous, abhorrent amount of cummies to this penguin named Chubs')
            await message.channel.send(jf_i.chubs_the_penuin)
            
        
        # 69 420 Nice Blaze it
        if jf.find(usr_msg.lower(),['69','sixty nine','sixty-nine']):      # 69 Nice
            await message.channel.send('Nice')
        if jf.find(usr_msg.lower(),['420','four twenty''four-twenty','4:20','4 20']):      # 420 Blaze it
            await message.channel.send('Blaze it  :flame:')


        # That tragedy
        if jf.find(usr_msg.lower(),'based'):
            await message.channel.send(jf_i.based_tragedy)
        # Agony
        if jf.find(usr_msg.lower(),['agony','suffering','anguish','misery','torment','woe','torture']):
            await message.channel.send(jf_i.agony)
        # Biden
        if jf.find(usr_msg.lower(),['afghanistan','united states','beauty in its purest form']):
            await message.channel.send(jf_i.biden)
        # Obama
        if jf.find(usr_msg.lower(),['nigger','nigga','n-word','n word','nword','black','barack','obama','niger','niga']):
            await message.channel.send(jf_i.obama)
        # Obama hot
        if jf.find(usr_msg.lower(), ['lust', ' hot ', ' hot', 'hot ']):
            await message.channel.send(jf_i.obama_hot)
        # Alex Miller Likes Persona
        if jf.find(usr_msg.lower(),['alex miller','alexmiller','persona']):
            await message.channel.send(jf_i.alex_miller_Persona)
        # The Zodiac Killer
        if jf.find(usr_msg.lower(),['zodiac killer','zodiackiller']):
            await message.channel.send(jf_i.zodiac_killer)
        # Cartoon turtle
        if jf.find(usr_msg.lower(),['turtle','shithead']):
            await message.channel.send(jf_i.cartoon_turtle)
        # Super Horny Man
        if jf.find(usr_msg.lower(),'horny'):
            await message.channel.send(jf_i.super_horny_man)
        # Trump and Epstein
        if ' red ' in usr_msg.lower():
            await message.channel.send(jf_i.trumpstein)
        # John Mcain
        if jf.find(usr_msg.lower(),['john mcain','john mccain']):
            await message.channel.send(jf_i.john_mcain)
        # Pearl Harbor Poggers
        if jf.find(usr_msg.lower(),['poggers','pog']):
            await message.channel.send(jf_i.pearl_harbor_poggers)
        # Sorry Bro I almost forgot... *mwah*
        if jf.find(usr_msg.lower(),['going to sleep','heading out','headin out','goin to sleep']):
            await message.channel.send('Sorry bro I almost forgot...')
            await message.channel.send(jf_i.sorry_bro)
            await message.channel.send('*mwah*')
        # Katrina
        if jf.find(usr_msg.lower(), 'katrina'):
            await message.channel.send(jf_i.katrina)


        # The Yeet Repyeeter
        if usr_msg.lower() == 'yeet':
            await message.channel.send("Yeet"*474)
        if usr_msg.lower() == 'yeet+':
            await message.channel.send("Yeet"*474)
            await message.channel.send("Yeet"*474)
            await message.channel.send("Yeet"*474)
        # What is a man?
        if 'what is a man?' in usr_msg.lower():
            await message.channel.send('A MISERABLE LITTLE PILE OF SECRETS')


        # Tachyon-specific responses
        if username == "Tachyon":

            # The bit
            if usr_msg.lower() == 'i made a bot':
                await message.channel.send("And it sucks")
                return

            if usr_msg.lower() == 'fuck you':
                await message.channel.send('No, fuck you')
                return

            if usr_msg.lower() == 'prepare for trouble!':
                await message.channel.send('And make it double!')
                return

            if usr_msg.lower() == 'testing':
                await message.channel.send('1 2 3')
                return


        # God King-specific responses
        #if username == "God Emporor Al Gore":
        #    await message.channel.send("^^^ hehe smol peepee be like ^^^")
        #    return

        return
    



# Actual execution code
client = based_bot()
client.run(TOKEN)