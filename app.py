import os
import json
from urllib.request import urlopen

from string import Template

url = "https://raw.githubusercontent.com/polkadot-js/phishing/master/all.json"

block_template = Template("""# PHISHBLOCKBEGIN
domain+body+title+media_description: [$blocklist]
action: spam
action_reason: "Domain on polkadot.js.org blocklist [{{match}}]"
# PHISHBLOCKEND""")

def print_block(deny):
    # TODO: somehow check if content has changed
    content = block_template.substitute(blocklist=", ".join(deny))
    from pprint import pprint
    pprint(content)

with urlopen(url) as response:
    try:
        all = json.load(response)
        deny = all['deny']
        print_block(deny)
        print("-" * 10)
        print(f'{len(deny)} hosts on deny list.')
    except json.JSONDecodeError:
        print("JSON malformed from GitHub")
