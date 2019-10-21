FROM ubuntu:18.04
RUN apt-get update && apt-get install python3 python3-pip git vim -qy
WORKDIR /repo
RUN git clone https://github.com/thethiny/DiscordYoutubeBot.git bot && pip3 install -r bot/requirements.txt
WORKDIR /repo/bot