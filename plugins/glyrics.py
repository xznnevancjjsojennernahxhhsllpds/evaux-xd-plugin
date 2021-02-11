# ported from oub-remix to USERGE-X by AshSTR/ashwinstr

import lyricsgenius

from userge import Message, userge

if GENIUS is not None:
    genius = lyricsgenius.Genius(GENIUS)


@userge.on_cmd(
    "glyrics",
    about={
        "header": "Lyrics using Genius API",
        "description": "Song lyrics from Genius.com",
        "usage": "{tr}glyrics [Artist name] - [Song name]",
        "examples": "{tr}glyrics Eminem - Higher",
    },
)
async def lyrics(message: Message):
    song = message.input_str or message.reply_to_message.text
    if not song:
        await message.edit("Search song lyrics without song name?")
        return
    if GENIUS is None:
        await message.edit("Provide 'Genius access token' as `GENIUS` to config vars...")
        return
    if "-" in song:
        artist, song = song.split("-", 1)
    await message.edit(f"Searching lyrics for **{artist} - {song}** on Genius...`")
    lyr = genius.search_song(song, artist)
    if lyr is None:
        await message.edit(f"Couldn't find `{artist} - {song}` on Genius...")
        return
