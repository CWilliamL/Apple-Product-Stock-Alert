# Apple-Product-Stock-Alert
An alert to get Hong Kong Apple Store stock availability on Telegram Channel

# Usage
Monitor interested Apple's products if they are back stock and available to order in APU. In order to avoid IP getting ban from Apple, proxy is used. To let the process do quickly, threading is applied so each checking won't be blocked by the others.

![image](https://user-images.githubusercontent.com/75830784/146634554-f5533431-c41d-45ab-ab1b-ee993a5b83ce.png)


# How to use
Prepare: Proxy Pool

1. Git clone the repository
2. Pip install the packages in requirements.txt
3. Set the interest Apple product you want to monitor in bot.py
4. Get a telegram bot from telegram BotFather. 
5. Copy the Token and paste to bot.py
6. Create a new channel and add the bot into the channel
7. Get the chat id, https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
8. Copy and paste the chat id to bot.py
9. RUN!

# Run the program on background in Ubuntu
nohup /path/to/python/script.py ARGS < /dev/null > outputfile 2>&1 &
nohup command >/dev/null 2>&1   # doesn't create nohup.out

TO STOP THE nohup BACKGROUND PROCESS

ps -ef | grep botver2

Then you will see the PID

Use "kill {PID}" to kill the program
