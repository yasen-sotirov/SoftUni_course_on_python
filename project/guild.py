from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        pass

    def kick_player(self, player_name: str):
        pass

    def guild_info(self):
        output = '\n'.join()
        return f"Guild: {self.name}\n{output}"
