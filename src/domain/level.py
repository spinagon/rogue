from domain.level_parts.room import Room

class Level:
    ROOM_COUNT = 9

    def __init__(self, difficult: float):
        self.rooms = self._generate_rooms(difficult)
        self.corridors = self._generate_corridors_by_rooms()

    def _generate_rooms(self, difficult: float):
        rooms = []

        for i in range(self.ROOM_COUNT):
            rooms.append(Room(difficult))

        return rooms

    def _generate_corridors_by_rooms(self):
        corridors = []

        # Что то для корректного соединения

        return corridors
