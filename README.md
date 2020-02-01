# HeardIt
Python scripts that uses the reddit PRAW api to retrieve hot songs from selected subreddits, add the songs to a youtube playlist, and email the playlist to a list of emails. 

### Required
- Make an email account and add its credentials for the bot to use, if Gmail, enable less secure apps so that the script can use the email.
- Make a reddit account, get client_id and client_secret
- add both of these credentials to credentials.txt for the script to use.

Need to use python3

### Recommended
- Add names of music subreddits to the MusicSubs.txt to add different genres, the format is as follows: subreddit name, # of songs
- If on Unix system scedule HeardIt with crontab for weekly or daily emails.
