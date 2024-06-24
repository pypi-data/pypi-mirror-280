## SETUP
it doesn't take much to run the slackbot locally

from a fresh environment you can do:
```console
# install scalify and slackbot dependencies
pip install git+https://github.com/KhulnaSoft/scalify.git readyapi cachetools

# set necessary env vars
cat ~/.scalify/.env
│ File: /Users/nate/.scalify/.env
┼──────────────────────────────────────
│ SCALIFY_OPENAI_API_KEY=sk-xxx
│ SCALIFY_SLACK_API_TOKEN=xoxb-xxx
│
│ SCALIFY_OPENAI_ORGANIZATION=org-xx
│ SCALIFY_LOG_LEVEL=DEBUG
│
│ SCALIFY_CHROMA_SERVER_HOST=localhost
│ SCALIFY_CHROMA_SERVER_HTTP_PORT=8000
│ SCALIFY_GITHUB_TOKEN=ghp_xxx
```

### hook up to slack
- create a slack app
- add a bot user, adding as many scopes as you want
- set event subscription url e.g. https://{NGROK_SUBDOMAIN}.ngrok.io/chat

see ngrok docs for easiest start https://ngrok.com/docs/getting-started/

tl;dr:
```console
brew install ngrok/ngrok/ngrok
ngrok http 4200 # optionally, --subdomain $NGROK_SUBDOMAIN
python cookbook/slackbot/start.py # in another terminal
```

#### test it out

<img width="719" alt="image" src="https://github.com/KhulnaSoft/scalify/assets/31014960/a5948f7f-9aeb-4df0-b536-d61bb57dd1ab">

to deploy this to cloudrun, see:
- [Dockerfile.slackbot](/cookbook/slackbot/Dockerfile.slackbot)
- [image build CI](/.github/workflows/image-build-and-push-community.yaml)