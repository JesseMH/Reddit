import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("linuxmasterrace")

for submission in subreddit.new(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")