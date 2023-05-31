# get-userid-bot

[![GitHub license](https://img.shields.io/github/license/bmyronov/get-userid-bot)](https://github.com/bmyronov/get-userid-bot/blob/main/LICENSE)

## Overview
The `get-userid-bot` is a bot developed to retrieve the user ID for a given username on the Telegram messaging platform. It is built using Python and utilizes the `aiogram` library to interact with the Telegram Bot API.

## Features
- Retrieve the user ID for a given username on Telegram

## Installation
To install and run the `get-userid-bot`, follow the steps below:

### Prerequisites
- Python 3.6 or above
- pip package manager

### Clone the repository
```console
$ git clone https://github.com/bmyronov/get-userid-bot.git
$ cd get-userid-bot
```

### Set up the Telegram Bot API
To use the `get-userid-bot`, you need to create a Telegram bot and obtain the API token. Follow these steps:

1. Create a new bot by talking to the BotFather on Telegram. Follow the instructions to create a new bot and obtain the API token.

2. Once you have the API token, create a new file named `.env` in the project directory.

3. Inside the `.env` file, add the following line, replacing `<API_TOKEN>` with your Telegram Bot API token:
   ```
   BOT_TOKEN=<API_TOKEN>
   ```

### Start the bot
```console
$ docker compose up -d
```

## Usage
To use the `get-userid-bot`, follow these instructions:

1. Start a conversation with the bot on Telegram by searching for it using the username or by clicking on the provided bot link.

2. Once the conversation is started, you can use the following commands to interact with the bot:
   - `/start` - Start the conversation and receive a welcome message.
   - `/getid` - Retrieve the user ID.

3. The bot will respond with the user ID of the specified username.

## Contact
For any inquiries or questions, you can contact the project maintainer:
- Name: [Bohdan Myronov](https://github.com/bmyronov)
- GitHub: [bmyronov](https://github.com/bmyronov)

Feel free to reach out with any feedback or concerns.