from project.player import Player
from project.guild import Guild


first_player = Player("George", 50, 100)
print(first_player.add_skill("Shield Break", 20))
print(first_player.player_info())
guild = Guild("UGT")
print(guild.assign_player(first_player))
print(guild.guild_info())
