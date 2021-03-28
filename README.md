# notification-pipeline
This is a notification pipeline written in python, which uses a common base `notification.txt` file to connect any script to an standardized discord notification system. 

### What is going on?
 
This code creates a pipeline between your scripts and discord bots using a common file that your code writes the notifications in and this tool picks them up and send them to your discord using bot token.

### How do I edit and use it?
* Create a discord bot (I am not adding those instructions here, there are numerous articles online on how to do that. )  
* Add the discord bot's token to `.env` file in the same folder as this script.
* Once that's done, your pipeline side of things are done.  
* Now just modify your scripts to add the notification to a file in same folder as this script.  
* Add that file's name in this code.  
* Use `!notifications` in your discord channel wherever you have added the bot to start it.

#### Requirements // Dependencies:
 * A discord bot token (google how to make discord bot.)
 * pip packages:
      - discord
      - dotenv (if getting errors during install, use `pip3 install python-dotenv`)
      - ... that's it I guess, If I missed anything, send PRs! (please)
 * Brain usually helps. 

### TODO
* Add error handling.    
* Beautify the notifications a bit more.  
* ... Thats about it in what I can find. If you think something else should be added or some feature that you'd like to add, send PRs! 
