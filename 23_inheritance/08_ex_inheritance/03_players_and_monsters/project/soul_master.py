from project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)


soul_master_1 = SoulMaster("S.M", 1)

# print(str(soul_master_1))
# print(soul_master_1.__class__.__bases__[0].__name__)

