# Implement abstract class Figure with abc method check_cell
# Figure has self attrs - name, coordinate, team

from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, name, coordinate, team):
        self.name = name
        self.coordinate = coordinate
        self.team = team


    @abstractmethod
    def check_cell(self):
        pass


    def move(self, new_coordinate):
        self.coordinate = new_coordinate
        print(f'{self.name} ({self.team}) - move on {self.coordinate}')


    def can_not_move(self, new_coordinate):
        print(f"{self.name} ({self.team}) - can't move on {new_coordinate}")


# implement fabric classmethod create_from_dict for Figure
    @classmethod
    def create_from_dict(cls, data_dict):
        return cls(name=data_dict.get('FNAME'), coordinate=data_dict.get('FCOORDINATE'), team=data_dict.get('FTEAM'))

# Implement property display_name
# property display_name return string like - "Horse (black) - (2, 4)"
    def display_name(self):
        return f'{self.name} ({self.team}) - {self.coordinate}'


# Create classes Horse and Pawn, override method check_cell
class Pawn(Figure):
    def check_cell(self, new_coordinate):
        if self.team == 'white':
            if new_coordinate == (self.coordinate[0] + 1, self.coordinate[1]) and self.coordinate[0] < 8:
                self.move(new_coordinate)
            elif new_coordinate == (self.coordinate[0] + 2, self.coordinate[1]) and self.coordinate[0] == 2:
                self.move(new_coordinate)
            else:
                self.can_not_move(new_coordinate)
        else:
            if new_coordinate == (self.coordinate[0] - 1, self.coordinate[1]) and self.coordinate[0] > 1:
                self.move(new_coordinate)
            elif new_coordinate == (self.coordinate[0] - 2, self.coordinate[1]) and self.coordinate[0] == 7:
                self.move(new_coordinate)
            else:
                self.can_not_move(new_coordinate)


class Horse(Figure):
    def check_cell(self, new_coordinate):
        x_abs = abs(self.coordinate[0] - new_coordinate[0])
        y_abs = abs(self.coordinate[1] - new_coordinate[1])
        if x_abs == 2 and y_abs == 1 or x_abs == 1 and y_abs == 2:
            self.move(new_coordinate)
        else:
            self.can_not_move(new_coordinate)

pawn_1 = Pawn('Pawn_1', (2, 1), 'white')
print(pawn_1.display_name())
# result --> Pawn_1_w (white) - (2, 1)
pawn_1.check_cell((3, 1))
# result --> Pawn_1 (white) - move on (3, 1)

pawn_3 = Pawn('Pawn_3', (2, 3), 'white')
print(pawn_3.display_name())
# result --> Pawn_3 (white) - (2, 3)
pawn_3.check_cell((4, 3))
# result --> Pawn_3 (white) - move on (4, 3)

pawn_6 = Pawn('Pawn_6', (2, 6), 'white')
print(pawn_6.display_name())
# result --> Pawn_6 (white) - (2, 6)
pawn_6.check_cell((2, 7))
# result --> Pawn_6 (white) - can't move on (2, 7)

pawn_9 = Pawn('Pawn_9', (6, 1), 'black')
print(pawn_9.display_name())
# result --> Pawn_9 (black) - (6, 1)
pawn_9.check_cell((5, 1))
# result --> Pawn_9 (black) - move on (5, 1)

pawn_13 = Pawn('Pawn_13', (7, 5), 'black')
print(pawn_13.display_name())
# result --> Pawn_13 (black) - (7, 5)
pawn_13.check_cell((5, 5))
# result --> Pawn_3 (white) - move on (4, 3)

pawn_15 = Pawn('Pawn_15', (1, 7), 'black')
print(pawn_15.display_name())
pawn_15.check_cell((2, 7))
# result --> Pawn_15 (black) - can't move on (2, 7)

pawn_16 = Pawn.create_from_dict({"FNAME": "Pawn_16", "FCOORDINATE": (7, 8), "FTEAM": "black"})
print(pawn_16.display_name())
# result --> Pawn_8_b (black) - (7, 8)

horse_1 = Horse('Horse_1', (1, 2), 'white')
print(horse_1.display_name())
# result --> Horse_1 (white) - (1, 2)
horse_1.check_cell((3, 3))
# result --> Horse_1 (white) - move on (3, 3)

horse_3 = Horse('Horse_3', (7, 5), 'black')
print(horse_3.display_name())
# result --> Horse_3 (white) - (7, 5)
horse_3.check_cell((7, 7))
# result --> Horse_3 (white) - can't move on (7, 7)
