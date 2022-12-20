class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        front = set(rooms[0])
        opened = {0}
        while front:
            newfront = set()
            for key in front:
                opened.add(key)
                for k in rooms[key]:
                    if k not in opened:
                        newfront.add(k)
            front = newfront
        return len(opened) == len(rooms)
