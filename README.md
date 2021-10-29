<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://github.com/jason-math/Hackbot">
    <img src="images/freetail_logo.png" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">HackBot</h1>

  <p align="center">
    An awesome Discord Bot to integrate into virtual hackathons!
    <br />
    <a href="https://github.com/jason-math/Hackbot/issues">Report Bug</a>
    ·
    <a href="https://github.com/jason-math/Hackbot/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Setting Up](#setting-up)
  * [Deployment](#deployment)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

Because of COVID-19, many activities, including Hackathons, are being forced to move online. However, organizing virtual hackathons is unfamiliar territory to most. I wanted to create a Discord bot that provides much needed functionality to run a successful virtual hackathon.

Of course, every virtual hackathon has its own set of needs, so I'll be adding more features over time. You may also suggest changes by forking this repo and creating a pull request or opening an issue.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With
* [Discord.py](https://discordpy.readthedocs.io/en/latest/)

<!-- GETTING STARTED -->
## Getting Started

This will be split into two sections:
1. Setting up your own bot to start writing code
2. Deploying this bot on your server

### Setting Up

This is an example of how to list things you need to use the software and how to install them.
* [Python](https://www.python.org/downloads/)
* Discord.py
```sh
pip install -U discord.py
```
* Dotenv
```sh
pip install -U python-dotenv
```
Note: If you are using PyCharm, you can install these directly into your project's virtual environment throught 'File > Settings > Project > Python Interpreter > Install' and choose the specified libraries.

Then, set up a Discord Account and Test Server if you haven't already. This will allow you to gain access to the [Developer Portal](http://discordapp.com/developers/applications) . 
Under 'Applications > Settings > OAuth2' give your bot the appropriate permissions. If you don't know what permissions to choose, just check 'Scopes > Bot' and 'Bot Permissions > General Permissions > Administrator' for now.
In a new tab, open the generated link under 'Scopes' and choose your test server.

Now your bot is all set up, it is time to start coding. To start, you will need the following two files:
* Bot.py - This is just a starting template to familiarize you with some basic syntax
```python
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice, number_of_sides):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)
``` 
* .env - This file will contain your bot key and other hidden data later on
```env
DISCORD_TOKEN={your-bot-token}
DISCORD_GUILD={your-server-name}
```
The bot token can be found in the Developer Portal under 'Applications > Settings > Bot > Token'. Don't give this token to anyone else.

Now, you can start editing Bot.py and be able to use your bot within the server!

If you would like to run the code already in this repository, simply clone the repository, rename 'dummyenv.txt' to '.env' and change the variables in it, and then enter this in the command line:
```sh
python bot.py
```

### Deployment

This section will be written very soon!

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jason Math - jasonmath@utexas.edu




