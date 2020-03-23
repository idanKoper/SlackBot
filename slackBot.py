from slackclient import SlackClient

from twitterStream import *

token = "xoxb-964004944564-964026877748-1yI75iQ4Yn7sz7YW8M3Fvl1Y"
slackClient = SlackClient(token)


def slackConnect():
    return slackClient.rtm_connect()


def slackReadRTM():
    while True:
        print(slackClient.rtm_read())
        time.sleep(1)


def slackSendMassageToContentChannel():
    print(slackClient.api_call("api.test"))
    print(slackClient.api_call("auth.test"))


def send_message(channel_id, message):
    slackClient.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='bot',
        icon_emoji=':robot_face:'
    )


def send_massge_evexry_hour(channel_id, message):
    while True:
        time.sleep(3600)
        send_message(channel_id, message)


def send_massage_by_tweets():
    tweets = get_tweets(api, "PythonWeekly")
    send_message("CUEMLATB8", "--Python Weekly updates:--")
    for i in tweets:
        send_message("CUEMLATB8", i)
    tweets = get_tweets(api, "realpython")
    send_message("CUEMLATB8", "--Real Python updates:--")
    for i in tweets:
        send_message("CUEMLATB8", i)
    tweets = get_tweets(api, "fullstackpython")
    send_message("CUEMLATB8", "--Python Weekly updates:--")
    for i in tweets:
        send_message("CUEMLATB8", i)


if __name__ == '__main__':
    send_massage_by_tweets()
    send_massge_evexry_hour("CUEMLATB8", datetime.datetime.now())
