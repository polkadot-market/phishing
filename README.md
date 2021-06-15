Phishing
--------

Download [polkadot-js/phishing](https://github.com/polkadot-js/phishing) and add denied hosts to a subreddit automoderator.

If you wish to use this fork this repo and add the following repository secrets in the "repo secrets" settings on Github:

```
praw_client_id
praw_client_secret
praw_user_agent
praw_username
praw_password
subreddit
```

You will need to have created a Reddit "script" app [here](https://old.reddit.com/prefs/apps/) for the first two.

The user must be a moderator of the subreddit. Subreddit is a string like "polkadot_market".

You also need to add these two lines somewhere in your existing automoderator config:

```
# PHISHBLOCKBEGIN
# PHISHBLOCKEND
```
