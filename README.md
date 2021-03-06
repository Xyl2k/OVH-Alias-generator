## OVH Alias Generator

This is a python script who use the OVH API v6 to create easily new mail redirection.

### Why ?
The idea is to use one mail per site you register, for example: ebay@yourdomain.fr, amazon@yourdomain.fr, etc... And all thoses mail adresses would just redirect to your main mail adress.
This way when you receive a junk mail, all you have to do is to look at the recipient adress to know who's the fucker who shared your mail addy.
And if the guys continue to spam you just have to delete the redirection.
I'm a customer of OVH and one of my plan allow me to create 1000 mail redirections, i guess it's enough for that usage.

The idea of using one mail per site is great but terribly frustrating to do if you do it the traditional way: You have to log in to your OVH manager, click on Emails, then click your domain, then click on Emails, then click on  Manage redirections, then click on Add a redirection... Oh.. wow all that time lost, and it's painfull to do...
But OVH offer also a great [API](https://eu.api.ovh.com/console/#/email/domain/%7Bdomain%7D/redirection#POST) to do operations on your plans. This script allow you to create a new alias directly from your terminal in one click.

### Stuff needed:

+ OVH python wrapper: ```pip install ovh```


### Getting Started
1. **Download zip file and extract the files (ovh.conf, consumerkey.py, redirector.py)**
2. Create your keys on [OVH Website](https://eu.api.ovh.com/createApp/) once you have application_key and application_secret fill it in ovh.conf and call consumerkey.py like this: ```python consumerkey.py yourdomain.fr``` then the script will call OVH and reply you with an URL you must visit to obtain your consumer_key.
3. Once you have everything fill application_key, application_secret, consumer_key in redirector.py. and you are ready to go.
4. Usage example : ```python redirector.py mydomain.fr ebay realmail```
This will create an alias ebay@mydomain.fr who will redirect mails to realmail@mydomain.fr

![redirector](https://user-images.githubusercontent.com/8536299/45780116-25629c00-bc5d-11e8-86a8-9c4d7e982ce0.png)