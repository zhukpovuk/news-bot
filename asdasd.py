import peewee
from peewee import *

db = SqliteDatabase('news_bot.db')


class Stat(Model):
    name = CharField(unique=True)
    business_number_of_requests= IntegerField()
    entertainment_number_of_requests= IntegerField()


    class Meta:
        database = db
        order_by = 'name'
        db_table = 'stats'

def write_player(nick):
    with db:
        player = {'name': nick, 'business_number_of_requests': 0, 'entertainment_number_of_requests': 0}
        Stat.insert(player).execute()


def check_name(nick):
    with db:
        unique_name = True
        query = Stat.select(Stat.name)
        for stat in query:
            if stat.name.lower() == nick.lower():
                unique_name = False
                break
        return unique_name


def get_stats(nick):
    with db:
        player_stats = Stat.get(Stat.name == nick)
        return [player_stats.name, player_stats.business_number_of_requests, player_stats.entertainment_number_of_requests]


def update_stats(nick, result):
    with db:
        player_stats = get_stats(nick)
        if (result == 'business') or (result == '/business'):
            player_stats[1] += 1
        elif (result == 'entertainment') or (result == '/entertainment'):
            player_stats[2] += 1
        query=Stat.update({Stat.business_number_of_requests: player_stats[1], Stat.entertainment_number_of_requests: player_stats[2]}).where(Stat.name == nick)
        query.execute()
