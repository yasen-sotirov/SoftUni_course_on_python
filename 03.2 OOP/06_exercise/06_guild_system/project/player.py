class Player:

    def __init__(self, player_name, hp: int, mp: int):
        self.player_name = player_name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild_of_the_player = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection " \
               f"of the player {self.player_name}"

    def player_info(self):
        return f"Name: {self.player_name}\n" \
               f"Guild: {self.guild_of_the_player}\n" \
               f"HP: {self.hp}\n" \
               f"MP: {self.mp}\n" +\
            '\n'.join([f"==={key} - {value}" for key, value in self.skills.items()])




