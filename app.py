import os
import json
from urllib.request import urlopen

from string import Template

url = "https://raw.githubusercontent.com/polkadot-js/phishing/master/all.json"
subreddit_name = os.getenv("subreddit")

block_template = Template("""# PHISHBLOCKBEGIN
domain+body+title+media_description: [$blocklist]
action: spam
# PHISHBLOCKEND""")

def update_automoderator(deny):
    reddit = praw.Reddit()
    subreddit = reddit.subreddit(str(subreddit_name))
    wikipage = subreddit.wiki["config/automoderator"]
    content_md = wikipage.content_md
    begin_md = content_md.split("# PHISHBLOCKBEGIN")[0]
    end_md = content_md.split('# PHISHBLOCKEND')[1]
    middle_md = block_template.substitute(blocklist=", ".join(deny))
    new_content = begin_md + middle_md + end_md
    if new_content != content_md:
        output = wikipage.edit(new_content, 'update blocklist')
        print(f"Updated automoderator config {output}")
    else:
        print("Config is already up to date.")

with urlopen(url) as response:
    try:
        all = json.load(response)
        deny = all['deny']
        print(f'{len(deny)} hosts on deny list.')
        try:
            import praw
            print("Attempting to update automoderator config.")
            update_automoderator(deny)
        except ModuleNotFoundError:
            print("You need to install praw if you want to update automoderator config")
    except json.JSONDecodeError:
        print("JSON malformed from GitHub")
