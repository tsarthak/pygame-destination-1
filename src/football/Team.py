from football.Character import Character
from football.ShapeTypes import ShapeTypes
from football.ShapeDescriptor import ShapeDescriptor


# represents multiple characters in a team instance.
class Team:
    def __init__(self, team_size, formation: str, color):
        self._players = []
        temp = formation.split('-')
        self._formation = {
            "F": temp[0],
            "M": temp[1],
            "D": temp[2],
            "G": 1
        }
        self.__make_team__(team_size, color)

    def __make_team__(self, team_size, team_color):
        for count in range(0, team_size, 1):
            self._players.append(Character(
                ShapeDescriptor(
                    ShapeTypes.CIRCLE,
                    radius=10,
                    color=team_color
                ),
                3
            )
            )

    def __iter__(self):
        return iter(self._players)
