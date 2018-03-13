# Simple WebScrapping Practice
[![PyPI](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)

A python discord bot server to scrap some data of PACKT editor daily free book using BeautifulSoup4 and discord.py.


https://www.packtpub.com/packt/offers/free-learning/

Book cover saved as 'book_cover.jpg'
## Usage

Generate a [discord app token][token] and save it as `token.priv`. 
Otherwise you can use this bot already prepared.

```
echo 'NDIzMDc4OTEyODQzNzEwNDY0.DYlGiQ.rrCk8vz5qvX8VeS92fikSXqc00A' > token.priv
```

Then do the following to start the server:

```
python3 discord_server.py
```

In the case you are using the already prepared token use [this link][invite] to invite the bot to your discord server. Otherwise you can generate your by replacing the CLIENTID in the following link with your bot's client ID:

```
https://discordapp.com/oauth2/authorize?client_id=CLIENTID&scope=bot
```

When the bot is in the server type `!book` in any channel that the bot is allowed to write to use it. 

[invite]:https://discordapp.com/oauth2/authorize?client_id=423078912843710464&scope=bot
[token]: https://discordapp.com/developers/applications/me
## Requirements

- Python 3.4.2+
- `aiohttp` library
- `websockets` library
- [`discord.py`][discordpy] library 

[discordpy]: https://github.com/Rapptz/discord.py
