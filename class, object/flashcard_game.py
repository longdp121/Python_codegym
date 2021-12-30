from random import choice, randint

class flashcard():
    def __init__(self):
        '''
        Keys from this dict is answer
        Values from this dict is question
        Question and answer have same index in list(keys()) and list(values())
        '''
        self.world_list = {'ong': 'bee', 'tho': 'rabbit', 
                            'cua': 'crab', 'meo': 'cat', 'ngua': 'horse', 
                            'khi': 'monkey', 'lua': 'donkey'}

    def vn_world(self):  #Sub-func
        '''
        This func return list of vnese world from world_list dict
        '''
        vn_world_list = self.world_list.keys()
        return list(vn_world_list)

    def en_world(self):  #Sub-func
        '''
        This func retunr list of en world from world_list dict
        '''
        en_world_list = self.world_list.values()
        return list(en_world_list)

    def randint_index(self):  #Sub-func
        '''
        This func give a randint num for index
        '''
        index = randint(0, len(self.world_list) - 1)
        return index

    def show_question(self):  #Sub-func
        '''
        This func print and return question which base on en_world index give by randint_index()
        '''
        question = (self.en_world())[self.randint_index()]
        print(f"What does \'{question}\' mean in Vietnamese?")
        return question

    def play_again(self):  #Sub-fun
        '''
        This func give option for breaking the loop or not
        '''
        play_again = str(input("Do you want to play again, y or n: "))
        while play_again not in ["n", "y"]:
            play_again = str(input("Do you want to play again, y or n: "))
        if play_again == "y":
            return True
        else:
            return False

    def main(self):  #main-func
        print("Let start!")
        while True:
            ask = self.show_question()
            real_index = self.en_world().index(ask)  #Give real index of en_world from the list. Avoid return other num when re-call randint func
            my_answer = str(input("Enter your answer: "))
            if my_answer == self.vn_world()[real_index]:  #Compare answer input with real index item from vn_world
                print("That's correct!")
            else:
                print(f"That's incorrect. The right answer is \'{self.vn_world()[real_index]}\'.")
            if self.play_again():
                continue
            else:
                break
        print("Goodbye!")

a = flashcard()
#print(a.en_world())
#print(a.vn_world())
#a.show_question()
#a.real_index()
a.main()