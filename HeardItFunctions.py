#!/usr/bin/env python3
import random
import smtplib
import praw 
import prawcore

def processCredentials(fileName):
  raw_credentials = open(fileName,'r')
  credentials = []

  for i in range(6):
    hold = raw_credentials.readline().strip().split("=")
    credentials.append(hold[1])

  #this line is processing and splitting the receivers info 
  credentials.append(raw_credentials.readline().strip().split('=')[1].split(','))
  
  return credentials


def getNewMusic(credentials):
  reddit = praw.Reddit(client_id = credentials[0], client_secret = credentials[1], user_agent = credentials[2])
  #take out values when uploading ^^

  subreddits = open('musicSubs.txt','r')
  musicfound = open('musicFound.txt','w')


  for i in subreddits:
    k = i.split(',')
    k[1] = int(k[1].rstrip())
    counter = 0   
    for submission in reddit.subreddit(k[0]).hot():
      if submission.is_self == False:
        url = submission.url
        title = submission.title
        if 'youtu' in url and '-' in title:
          if "antano" not in title and 'review' not in title and 'REVIEW' not in title:
            if counter < k[1]:
              sub = str(submission.subreddit)       
              print([sub,title,url])
              musicfound.write(sub+'|||'+title+'|||'+url+"\n")
              counter += 1
                
  subreddits.close()
  musicfound.close()
  return


def preparePlaylist(length,credentials):
  playlist = "http://www.youtube.com/watch_videos?video_ids="

  raw = open('musicFound.txt',"r")


  hold = []

  # if sum(1 for line in raw) < length:
  #   getNewMusic()

  raw = open('musicFound.txt',"r")

  for i in raw:
    hold.append(i)
    
  if len(hold) < length:
    getNewMusic(credentials)
    for i in raw:
      hold.append(i)


  description =''

  randomChosen = random.sample(range(0,len(hold)),length)

  for i in randomChosen:
    chosen = hold[i]
    chosen = chosen.split('|||')
    chosen[2] = chosen[2][:-1]
    
    if "youtu.be" in chosen[2]:
      vid = chosen[2].split('.be/')
    else:
      if 'v=' in chosen[2]: 
        vid = chosen[2].split('v=')
      else:
        vid = chosen[2].split('v%3D')
    
    playlist += vid[1][0:11] +","
    description +=  chosen[0] + " | " + chosen[1] +"\n"+"\n"
  
  for x in randomChosen[::-1]:
    hold.pop(0)

  updatedlist = open('musicFound.txt','w')
  for i in hold:
    updatedlist.write(i)

  updatedlist.close()
  raw.close()
  print("Playlist Created Successfully")
  return [playlist,description]


def emailMusic(playlist,credentials):
  username = credentials[3]
  password = credentials[4]
  sender = credentials[5]
  receivers = credentials[6]

  counter = 0

  while counter < 3: # number of tries
    try:
       server = smtplib.SMTP('smtp.gmail.com',587)
       server.starttls()
       server.ehlo()
       server.login(username,password)
       server.sendmail(sender, receivers,"Subject: <heres New Music>" +"\n"+ playlist[1] +"\n"+ playlist[0])         
       print("Successfully sent email")
       counter = 4
    except:
       print("Error: unable to send email try number ", counter)
       counter += 1



'''
#Fuck using the youtube api till further notice

key =

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from datetime import date

today = date.today().strftime("%d/%m/%Y")

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():

if __name__ == "__main__":
    main()
'''
