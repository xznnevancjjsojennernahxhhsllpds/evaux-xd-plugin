from userge import userge, Message

@userge.on_cmd(
    "xyz",
    about={
        "header": "Lyrics using Genius API",
        "description": "Song lyrics from Genius.com",
        "usage": "{tr}glyrics [Artist name] - [Song name]",
        "examples": "{tr}glyrics Eminem - Higher",
    },
)
async def xyz(message: Message):
