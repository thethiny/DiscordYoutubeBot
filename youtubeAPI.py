import requests, json
from bs4 import BeautifulSoup as Soup
from keys import YOUTUBE_API

def parse_channel(message):
    message = message.lower()
    
valid_types = [
    "user",
    "c",
    "channel"
]

def parse(message):
    content = message.lower().split()
    if len(content) < 2:
        raise Exception("Invalid Message")
    else:
        if content[1] == '/h':
            return "help"
        elif content[1] == '/r':
            return "rename"
        else:
            return "subs"
    
def get_account(message):
    content = message.split()
    if len(content) < 2:
        raise Exception("Invalid Message")
    elif len(content) == 2:
        return content[1], "user"
    else:
        return ' '.join(content[2:]), content[1].lower()
        
    
def get_url(user, type):
    url = "https://youtube.com/{0}/{1}/about"
    if type == 'user':
        url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={0}&key={1}"
    else:
        url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id={0}&key={1}"
    full_url = url.format(user, YOUTUBE_API)
    #print(full_url)
    return full_url
    
        
        
def get_subs(url):
    r = requests.get(url)
    subs = json.loads(r.text)["items"][0]["statistics"]["subscriberCount"]
    views = json.loads(r.text)["items"][0]["statistics"]["viewCount"]
    uploads = json.loads(r.text)["items"][0]["statistics"]["videoCount"]
    #s = Soup(r.content)
    #subs = s.find(class_='yt-subscription-button-subscriber-count-branded-horizontal').text
    #print(s.page_source)
    #print(subs)
    #print(url)
    return subs, views, uploads
    
def help_message():
    message = "Usage: ?sub <channel_type> <channel_name>\nExample:\n?sub thethiny\n?sub c thethiny\n?sub channel thethiny\n?sub user thethiny\n\n?rename_channel <channel_ID> **(not yet implemented)**\nExample:\n?rename_channel UCf2NaTy_dk1HevjbUqVQL3Q\nThis will save the channel's name into the bot.\n\nFor more help contact thethiny#9580"
    return message
    
def sub_message(user, subs):
    message = f"{user} has {subs[0]} subs, {subs[1]} views on {subs[2]} videos"
    return message
    
def get_channel_name(id):
    url = "https://www.googleapis.com/youtube/v3/channels?id={0}&part=snippet&key={1}".format(id, YOUTUBE_API)
    r = requests.get(url)
    channel_name = json.loads(r.text)["items"][0]["snippet"]["title"]
    return channel_name
    
def subs(message):
    user, type = get_account(message)
    print("Type:", type)
    if type not in valid_types:
        raise Exception("Invalid Channel Type")
    url = get_url(user, type)
    chan_stat = get_subs(url)
    if type != 'user':
        user = get_channel_name(user)
    return sub_message(user, chan_stat)
    
def get_sub_count(message):
    try:
        type = parse(message)
        
        if type == "help":
            return help_message()
        elif type == "rename":
            return rename(message)
        elif type == "subs":
            return subs(message)
        else:
            raise Exception("Invalid Message")
    except Exception as e:
        print(e)
        if e.args[0] == "'NoneType' object has no attribute 'text'":
            return "Channel Not Found"
        else:
            return "An Error Occured. Type ?sub /h for how to use."
    
    
        