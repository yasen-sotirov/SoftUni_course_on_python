from player import Player


class Guild:
    def __init__(self, guild_name):
        self.guild_name = guild_name
        self.guild_players_list = []

    def assign_player(self, first_player: Player):
        if first_player.guild_of_the_player != self.guild_name and \
                first_player.guild_of_the_player != "Unaffiliated":
            return f"Player {first_player.player_name} is in another guild."

        if first_player.player_name in self.guild_players_list:
            return f"Player {first_player.player_name} is already in the guild."

        self.guild_players_list.append(first_player)
        first_player.guild_of_the_player = self.guild_name
        return f"Welcome player {first_player.player_name} to the guild {self.guild_name}"

    def kick_player(self, player_to_kick: str):
        if player_to_kick not in self.guild_players_list:
            return f"Player {player_to_kick} is not in the guild."
        return f"Player {player_to_kick} has been removed from the guild."

    def guild_info(self):
        output = '\n'.join(el.player_info() for el in self.guild_players_list)
        return f"Guild: {self.guild_name}\n{output}"


