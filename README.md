# Telegram Bot for translating
#### Telegram bot for translating in Python using aiogram, PostgreSQL, Reverso Context API and Google Translator
Telegram bot gets source and target languages from user and stores it in database. User can enter word/phrase and get translation of that.

The <b>PostgreSQL</b> database is used for data storage.

The bot, receiving a request from the user, processes it using the aiogram library, which interacts with the Telegram bot API.


## Table of context
* [What the bot can do](#What-the-bot-can-do)
* [Technologies Used](#Technologies-Used)
* [Setup](#Setup)
    * [How to start](#How-to-start)
        * [Launching with a Linux distribution](#Example-of-running-on-a-Linux-distribution-like-Ubuntu)
        * [How to run a bot on others OS?](#How-to-run-a-bot-on-others-OS?)
        * [Errors](#Errors)
* [Project status](#Project-status)

## What the bot can do
* Setting source and target language
* Translate words/phrases in under of Reverso Context
* Sharing a link to Google Translator if no words/phrases are found on the given dictionary
* Provides some statistics to the admin user
  * Command /admin_on checkes if user is admin (admin is set in .env file)
  * Then user gets list of others commands to see a statistic
## Technologies Used
* Python3.8
* PostgreSQL
* aiogram 2.20
* reverso-context-api 0.5

## Setup
* All packages are located in requirements.txt
* Environmental variables are located in .env (you must change example.env file)
### How to start
#### Example of running on a Linux distribution like Ubuntu
1. Download project locally
2. Run following to activate a virtualenv in your terminal:
    * `python3 -m venv env`
    * `. env/bin/activate`
3. Run: `pip install -r requirements.txt` to install all necessary packages
4. Run: `bash launch_bot.sh` to launch a bot
#### How to run a bot on others OS?
1. Download project locally
2. Create venv and activate that
3. Run: `pip install -r requirements.txt` to install all necessary packages
4. Run: `python app.py` to launch a bot
#### Errors
1. Aiogram library works well on Linux OS, but may crash on other operating systems
    * Try download [aiogram](https://pypi.org/project/aiogram/) and [install](https://docs.aiogram.dev/en/latest/install.html) it
    * Note: aiogram cannot work with python 3.6 and under
2. Python's and pip's versions can differ from the same in that project 

## Project status
Project is in progress

## Room for improvement
#### Future features:
* Adding new languages
* Adding feature for admin to get more statistic information

#### Future changing:
* Replace poolling with webhook
