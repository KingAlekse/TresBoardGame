import random


class Tres:

    def __init__(self):
        self.new_game()

    def new_game(self):
        self.outer_ring = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.middle_ring = [0, 0, 0, 0, 0, 0, 0, 0]
        self.inner_ring = [0, 0, 0, 0]
        self.center = [3]

        self.all_rings = [self.outer_ring,
                          self.middle_ring, self.inner_ring, self.center]

        #self.rotatable = [1, 0, 1]

        self.yellow_stock = 17
        self.blue_stock = 17

    def set_path(self, path: int):
        self.paths = [[(0, 0), (1, 0), (2, 0), (3, 0), (2, 2), (1, 4), (0, 8)],
                      [(0, 8), (1, 4), (2, 2), (3, 0), (2, 0), (1, 0), (0, 0,)],
                      [(0, 4), (1, 2), (2, 1), (3, 0), (2, 3), (1, 6), (0, 12)],
                      [(0, 12), (1, 6), (2, 3), (3, 0), (2, 1), (1, 2), (0, 4)]]
        return self.paths[path]

    def add_piece(self, color: int, path: int, depth: int):
        self.current_path = self.set_path(path)
        if depth == 6:
            if self.all_rings[self.current_path[depth][0]][self.current_path[depth][1]] == 1:
                self.yellow_stock += 1
            if self.all_rings[self.current_path[depth][0]][self.current_path[depth][1]] == 2:
                self.blue_stock += 1
            self.all_rings[self.current_path[depth][0]
                           ][self.current_path[depth][1]] = color
        else:
            if self.all_rings[self.current_path[depth][0]][self.current_path[depth][1]] != 0:
                self.add_piece(
                    self.all_rings[self.current_path[depth][0]][self.current_path[depth][1]], path, depth+1)
                self.all_rings[self.current_path[depth][0]
                               ][self.current_path[depth][1]] = color
                if depth == 0:
                    if color == 1:
                        self.yellow_stock -= 1
                    if color == 2:
                        self.blue_stock -= 1
            else:
                self.all_rings[self.current_path[depth][0]
                               ][self.current_path[depth][1]] = color
                if depth == 0:
                    if color == 1:
                        self.yellow_stock -= 1
                    if color == 2:
                        self.blue_stock -= 1

    def win_state(self):
        if self.center[0] == 1 and self.inner_ring[0] == 1 and self.inner_ring[2] == 1:
            return 1
        if self.center[0] == 2 and self.inner_ring[0] == 2 and self.inner_ring[2] == 2:
            return 2
        return 0

    # def able_rotation(self):
    #     if 1 in self.middle_ring or 2 in self.middle_ring:
    #         self.rotatable[1] = 1

    def rotate(self, ring: int):
        if ring == 0:
            last = self.outer_ring[-1]
            self.outer_ring.pop(-1)
            self.outer_ring.insert(0, last)
        if ring == 1:
            first = self.middle_ring[0]
            self.middle_ring.pop(0)
            self.middle_ring.append(first)
        if ring == 2:
            last = self.inner_ring[-1]
            self.inner_ring.pop(-1)
            self.inner_ring.insert(0, last)


class GamePlayTextVersion:

    def __init__(self):
        self.start_game()

    def game_over(self):
        if self.tres.win_state() == 0:
            return False
        return True

    def start_game(self):
        self.tres = Tres()

        current_player = random.randint(1, 2)
        players = ["yellow", "blue"]

        while True:
            if current_player == 1 and self.tres.yellow_stock == 0:
                current_player = 2
            elif current_player == 2 and self.tres.blue_stock == 0:
                current_player = 1

            print(f"{players[current_player - 1]}'s turn")
            print()

            where = int(input("add piece to where: "))
            self.tres.add_piece(current_player, where, 0)

            #self.tres.able_rotation()

            for i in self.tres.all_rings:
                print(i)
            print()
            if self.game_over():
                break

            while True:
                rotate = int(input("rotate ring: "))
                if rotate == 0:
                    self.tres.rotate(0)
                    break
                # elif rotate == 1 and self.tres.rotatable[1] == 0:
                #     print("can't rotate yet")
                elif rotate == 1: #and self.tres.rotatable[1] == 1:
                    self.tres.rotate(1)
                    break
                elif rotate == 2:
                    self.tres.rotate(2)
                    break

            print()
            for i in self.tres.all_rings:
                print(i)
            print()
            if self.game_over():
                break

            print(self.tres.yellow_stock)
            print(self.tres.blue_stock)
            print()

            if current_player == 1:
                current_player = 2
            elif current_player == 2:
                current_player = 1

        print()
        print(f"{players[self.tres.win_state() - 1]} wins")


if __name__ == "__main__":
    game = GamePlayTextVersion()
