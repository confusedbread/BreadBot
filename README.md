# BreadBot

A discord bot for my personal usage. Currently a work in progress.

## Setup

For obvious reasons the file .bot-key is not provided. Create your own and put in your bot key into the file.

### Prerequisites
* Python 3.5+ ; Lowest version tested: 3.6
* [discord.py](https://github.com/Rapptz/discord.py)

## API

### app.py
Add new async event consumers: <br />
```python
@bot.event
async def on_some_event(payload):
    # send payload to data handler
    data_handler(payload)
```
These are defined by the Client API provided by `discord.py` (https://discordpy.readthedocs.io/en/latest/api.html#client)

### commands/
Module definition for simple commands.
```
async def hello(bot, message):
    await message.channel.send('Hello! Me Bot {}'.format('🀇'))
```

### features/
Module support both for more complex features and one offs.

TODO: Features
- Music bot integration
- Japanese Translator Ingtegration Python romkan library

## Deploy
Heroku autodeploys on changes to master 
- `heroku ps:scale worker=1`
- `heroku logs --tail`

## Docs
- discord.py: https://discordpy.readthedocs.io/en/latest/api.html#
- twich api: https://dev.twitch.tv/docs/api/reference
- heroku startup: https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true
- heroku dashboard: https://dashboard.heroku.com/apps/confusedbread-bot/resources