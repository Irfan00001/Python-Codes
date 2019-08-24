
import random

List1 = ["A", "J", "K", "Q"]
Deck = []
for x in range(0, 4):
    for y in range(2, 11):
        Deck.append(y)
    for z in List1:
        Deck.append(z)

random.shuffle(Deck)
print(Deck)

class Player:
    def __init__(self):
        self.hand = []
        self.score = self.setScore()
        self.name = self.setName()

    def pickacard(self):
        # shuffles the card and the player picks up the first card
        random.shuffle(Deck)
        self.hand.append(Deck[0])
        print(self.hand)

        # removes the card from the deck when the player picks it up
        del (Deck[0])

    def setName(self):
        Name = input("Enter the player Name: ")
        return Name

    def getName(self):
        print(self.name)

    def getHand(self):
        print(self.hand)



    def setScore(self):
        Score = 0
        List1dict = {"A": 11, "J": 10, "K": 10, "Q": 10}
        for cards in self.hand:
            if cards in range(2, 11):
                print(cards)
                Score += int(cards)
                print(Score)
            elif cards in List1dict:
                print(cards)
                Score += List1dict[cards]
                print(Score)
        if (Score > 21):
            Score -= 10
        return Score



#
#


def game():
    player1 = Player()
    player2 = Player()
    while (True):
        print("It's " + player1.name + " turn")
        player1.pickacard()
        player1.setScore()
        print(player1.score)
        print("It's " + player2.name + " turn")
        player2.pickacard()
        player2.setScore()
        print(player2.score)
        if (player1.score == 21):
            print("The winner is " + player1.name)
            break
        elif (player2.score == 21):
            print("The winner is " + player2.name)
            break
# # def game():
# #     player1 = Player()
# #     player2= Player()
# #     while (True):
# #
# #         print("It's " + player1.name + " turn")
# #         player1.pickacard()
# #         player1.setScore()
# #         print("It's " + player2.name + " turn")
# #         player2.pickacard()
# #         player2.setScore()
# #         if (player1.score == 21):
# #             print("The winner is " + player1.name)
# #             break
# #         elif (player2.score == 21):
# #             print("The winner is " + player2.name)
# #             break
# #
# #
game()
