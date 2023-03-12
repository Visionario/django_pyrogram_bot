django_pyrogram_bot 
------------   
### Django Pyrogram Bot      

Basic, simple and 100% functional example demonstrating how [Pyrogram](https://pyrogram.org/) integrates with [Django](https://www.djangoproject.com/), ready to use.

Version: 0.1.0

Supported:   
* Python: 3.10   
* Django: 4.x    
* Pyrogram: 2.0   

------------


Quickstart 
------------   

* Clone this repository
* Copy *settings.py.sample* on *settings.py*   
* Check and edit/change `PYROGRAM_BOT` data on settings using your token from [@BotFather](https://t.me/BotFather), `API_ID` and `API_HASH` from https://my.telegram.org/apps    
* Add your telegram "user_id" on `ADMINS` (settings file)    
* Create virtual environment   
  * `python3 -m venv venv`
* Install requirements   
  * `pip install -r requirements.txt`   
* Make migrations   
  * `python manage.py makemigrations`     
  * `python manage.py migrate`   
  * `python manage.py createsuperuser`   
* Start BOT:   
  * `python manage.py start_bot`
* Start Django (another terminal/console):  
  * `python manage.py runserver`   


-----------
# How this works

Django and pyrogram Bot works in separate spaces, but share the Django code.

That's why the bot is started with `python manage.py start_bot` and preferably before starting the Django session.

When the bot starts, the get_me() and Pyrogram `session string` values are automatically saved in the `running_bot_data.json` file, this data is shared so that Django can communicate using the running bot session.   

-----------
# Pyrogram 'plugins' directory

You will notice that there is a directory named `bot_plugins`, it is NOT a Django app.   

You can place all the necessary plugins for the bot since when the Pyrogram client starts it will search internally. I have left some basic commands for the demonstration in the example.

-----------
# Logs

Pyrogram and Django share the same logging system which is defined in Django's `settings.py`, please modify `LOGGING` as needed.

-----------
# Caveats

Django is not fully functional with Asynchronous Support, please read [Asynchronous support](https://docs.djangoproject.com/en/4.1/topics/async/) and Pyrogram makes extensive use of it, that's why you will sometimes get a warning of incompatibility which is solved very easily as need using [sync_to_async()](https://docs.djangoproject.com/en/4.1/topics/async/#asgiref.sync.sync_to_async)    

----------

# Contribution Guidelines

Contributions are welcome!   

----------


Live Long And Prosper - L.L.A.P 🖖