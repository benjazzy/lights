from twitch import TwitchClient

client = TwitchClient(client_id='j3cd7zhcaho6mtin6y6h1cfpdi51x')
channel = client.channels.get_by_id(44322889)

print(channel.id)
print(channel.name)
print(channel.display_name)
