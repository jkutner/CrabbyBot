from slackeventsapi import SlackEventAdapter
import slack
import os

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
token = os.environ["SLACK_TOKEN"]
slack_client = slack.WebClient(token=token)

@slack_events_adapter.on("app_mention")
def handle_mention(event_data):
    event = event_data["event"]
    channel = event["channel"]
    user = event["user"]
    message = "<@%s> :zipper_mouth_face:" % (user)
    slack_client.chat_postMessage(channel=channel, text=message)

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
PORT = os.environ["PORT"]
slack_events_adapter.start(host="0.0.0.0", port=PORT)