# YouTube Sub & Views Counter - Discord Bot

This Discord Bot will check the count of someone's subscribers using YouTube's API, and then report back to you via a reply, whether it is in a channel or a DM. Just make sure he's there.

## Usage:

    ?sub <type> <value>
example:

    ?sub user thethiny
    ?sub u thethiny
    ?sub channel UCf2NaTy_dk1HevjbUqVQL3Q
    ?sub thethiny
The last one assumes user by default.

## Notes:
Make sure to have a `keys.py` file that includes your 3 Discord Keys (Client ID, Client Secret, Token) and a YouTube API key as follows:

    CLIENT_ID = 
    CLIENT_SECRET = 
    TOKEN = 
    YOUTUBE_API = 


The bot does not have proper error handling, and doesn't yet support renaming channels to their display name (for example, renaming channel UCf2NaTy_dk1HevjbUqVQL3Q to thethiny). This is a feature that is to be added.

### Docker Notes:
If you're hosting it on a server, make sure to run it using `-it -d` so that you can launch other stuff on a server. If it's a single-deployment server, say **Heroku**, you're only going to need -it. Then you have to add it to your `/etc/rc.local` if you want it to start automatically in the background on your server as follows:
`docker run -it -d -v /location/of/keys.py:/repo/bot/keys.py THE_NAME_OF_THE_IMAGE`

<br>

#### *Feel free to contact me for any inquiries over on twitter or ymail @ thethiny*
