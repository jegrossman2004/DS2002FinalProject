from typing import Final
import os
# from dotenv import load_dotenv
from discord import Intents, Client, Message
from random import choice, randint
import openai
import json
import pandas as pd;
import pymysql

###TOKEN LINE HERE, TOLD ME TO REMOVE FOR SECURITY REASONS


# Step 1: BOT SETUP Without intents your bot won't respond
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    host_ip = '127.0.0.1'
    port = '3306'
    user_id = 'root'
    pwd = 'TommyCutlets15!?'
    db_name = 'mets_data'
    conn = pymysql.connect(host=host_ip, user=user_id, password=pwd, database=db_name)

    if lowered == '':
        return 'Speak up bro'
    elif 'hello' in lowered or 'hi' in lowered:
        return 'Whats up bro'
    elif '!funfact' in lowered:
        return 'Having a fear of long words is called Hippopotomonstrosesquippedaliophobia. Yeah. Seriously.'
    elif '!movie' in lowered:
        i = randint(1, 6)
        if i == 1:
            return 'I recommend you watch 2001: A Space Odyssey!'
        elif i == 2:
            return 'I recommend you watch Spider-Man!'
        elif i == 3:
            return 'I recommend you watch The Matrix!'
        elif i == 4:
            return 'I recommend you watch the Lord of the Rings trilogy!'
        elif i == 5:
            return 'I recommend you watch Star Wars!'
        else:
            return 'I recommend you watch Interstellar!'
    elif 'help' in lowered:
        return ('you can say !data1, !data2, or !data3 to access 3 different tables of data! You can also say !movie '
                'to get a movie recommendation or say !funfact to learn a fun fact!')
    elif '!data1' in lowered:
        return str(pd.read_sql('SELECT td.team_name, AVG(scoring_plays) AS avg_scoring_plays FROM '
                               'mets_data.mets_game_scoring_plays sp JOIN mets_data.mets_schedule s ON sp.game_number ='
                               's.game_number JOIN team_data td ON s.opponent = td.team_abbreviation GROUP BY '
                               'td.team_name ORDER BY avg_scoring_plays;', conn))
    elif '!data2' in lowered:
        return str(
            pd.read_sql('SELECT s.ballpark, ROUND(AVG(s.left_field_distance + s.center_field_distance + '
                        's.right_field_distance) / 3, 2) AS avg_distance FROM mlb_standings st JOIN team_data td ON '
                        'td.team_name = st.team_name JOIN mlb_stadiums s ON s.team_abbreviation = td.team_abbreviation '
                        'GROUP BY st.team_name, s.ballpark ORDER BY avg_distance DESC;', conn))
    elif '!data3' in lowered:
        return str(pd.read_sql(
            'SELECT s.game_number, s.date,COUNT(h.highlight_links) AS num_highlights FROM mets_highlights h '
            'JOIN mets_schedule s ON h.game_number = s.game_number GROUP BY s.game_number,s.date HAVING NOT '
            'COUNT(h.highlight_links) = 10;', conn))

    else:
        return "I'm sorry, I don't understand!"


# Step 2: Message Function
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty becuase intents were not enabled...prob)')
        return
    # check to see if you need to resopnd to private messages
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# Step 3: Handle the startup of the bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# Step 4:  Let's handle the messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:  # The bot wrote the message, or the bot talks to itself
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# Step 5 Main Starting point

def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
