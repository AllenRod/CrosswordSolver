import random
import string
import nltk
import sys
import copy
import time

word_list = nltk.corpus.words.words()
word_dict = dict()
for word in word_list:
    word_len = len(word)
    if word_len not in word_dict:
        word_dict[word_len] = [word.upper()]
    else:
        current_list = word_dict[word_len]
        current_list.append(word.upper())
        word_dict[word_len] = current_list

class CrossWordBoard:
    def __init__(self, width, height, word_locations):
        self.width = width
        self.height = height
        self.word_locations = word_locations
        self.vertical_word = dict()
        self.horizontal_word = dict()
        self.letter_map = dict()
        self.fitness = 0
        self.word_count = 0
        
        for index in self.word_locations:
            tuple = self.word_locations[index]
            start_location = tuple[0]
            end_location = tuple[1]
            is_horizontal = True
            word_len = 0
            if start_location[0] == end_location[0]:
                word_len = abs(start_location[1] - end_location[1]) + 1
            elif start_location[1] == end_location[1]:
                is_horizontal = False
                word_len = abs(start_location[0] - end_location[0]) + 1
            
            if word_len == 0:
                print('Problem with start location and end location.')
                sys.exit(0)
            
            if is_horizontal:
                coord_list = []
                for i in range(word_len):
                    if end_location[1] > start_location[1]:
                        coord = (start_location[0], start_location[1] + i)
                    else:
                        coord = (start_location[0], start_location[1] - i)
                    
                    coord_list.append(coord)
                    self.letter_map[coord] = '\\'
                self.horizontal_word[index] = (coord_list, word_len)
            else:
                coord_list = []
                for i in range(word_len):
                    if end_location[0] > start_location[0]:
                        coord = (start_location[0] + i, start_location[1])
                    else:
                        coord = (start_location[0] - i, start_location[1])
                        
                    coord_list.append(coord)
                    self.letter_map[coord] = '\\'
                self.vertical_word[index] = (coord_list, word_len)
                
        self.word_count = len(self.horizontal_word) + len(self.vertical_word)
        
        
    def randomInit(self):
        # assign words to horizontal words first
        for index in self.horizontal_word:
            coord_list, word_len = self.horizontal_word[index]
            random_word_list = word_dict[word_len]
            random_word = random_word_list[random.randrange(len(random_word_list))].upper()
            word_index = 0
            #print(random_word)
            for coord in coord_list:
                self.letter_map[coord] = random_word[word_index]
                word_index += 1
        
        # assign words to vertical words 
        for index in self.vertical_word:
            coord_list, word_len = self.vertical_word[index]
            random_word_list = word_dict[word_len]
            random_word = random_word_list[random.randrange(len(random_word_list))].upper()
            word_index = 0
            #print(random_word)
            for coord in coord_list:
                self.letter_map[coord] = random_word[word_index]
                word_index += 1
        
    def printBoard(self):
        for w in range(2 * self.width + 1):
            print('-', end="")
        print()
        for h in range(self.height):
            print('|', end="")
            for w in range(self.width):
                if (h, w) in self.letter_map:
                    print(self.letter_map[(h, w)] + '|', end="")
                else:
                    print(" |", end="")
            print()
            for w in range(2 * self.width + 1):
                print('-', end="")
            print()
        print()
        
    def getWord(self, word_index):
        coord_list = None
        word_len = None
        
        if word_index in self.horizontal_word:
            coord_list, word_len = self.horizontal_word[word_index]
        elif word_index in self.vertical_word:
            coord_list, word_len = self.vertical_word[word_index]
        else:
            print('Error in mutation.')
            sys.exit(0)
        
        # return the word at the given index
        word = ''
        for coord in coord_list:
            word += self.letter_map[coord]
        return(word)
                
    def computeFitness(self):
        accepted_word_count = 0
        # go through horizontal words first
        for index in self.horizontal_word:
            coord_list, word_len = self.horizontal_word[index]
            word = ''
            for coord in coord_list:
                word += self.letter_map[coord]
            
            if word in word_dict[word_len]:
                accepted_word_count += 1

        # go through vertical words
        for index in self.vertical_word:
            coord_list, word_len = self.vertical_word[index]
            word = ''
            for coord in coord_list:
                word += self.letter_map[coord]
            
            if word in word_dict[word_len]:
                accepted_word_count += 1
        
        #print(accepted_word_count)
        self.fitness = accepted_word_count / self.word_count
        #print(self.fitness)
        
    def mutation(self):
        word_index = random.randrange(self.word_count)
        coord_list = None
        word_len = None
        
        if word_index in self.horizontal_word:
            coord_list, word_len = self.horizontal_word[word_index]
        elif word_index in self.vertical_word:
            coord_list, word_len = self.vertical_word[word_index]
        else:
            print('Error in mutation.')
            sys.exit(0)
        
        # generate a new random word and update board
        random_word_list = word_dict[word_len]
        random_word = random_word_list[random.randrange(len(random_word_list))].upper()
        word_index = 0
        #print(random_word)
        for coord in coord_list:
            self.letter_map[coord] = random_word[word_index]
            word_index += 1
            
    def crossover(self, word_index, crossover_word):
        coord_list = None
        word_len = None
        
        if word_index in self.horizontal_word:
            coord_list, word_len = self.horizontal_word[word_index]
        elif word_index in self.vertical_word:
            coord_list, word_len = self.vertical_word[word_index]
        else:
            print('Error in crossover.')
            sys.exit(0)
        
        # generate a new random word and update board
        word_index = 0
        for coord in coord_list:
            self.letter_map[coord] = crossover_word[word_index]
            word_index += 1
            
def performCrossover(board1, board2):
    word_index = random.randrange(board1.word_count)
    new_board1 = copy.deepcopy(board1)
    new_board2 = copy.deepcopy(board2)
    
    board1_word = board1.getWord(word_index)
    board2_word = board2.getWord(word_index)
    
    new_board1.crossover(word_index, board2_word)
    new_board2.crossover(word_index, board1_word)
    
    return (new_board1, new_board2)
                
if __name__ == '__main__':
    word_locations = dict()
    word_locations[0] = ((0, 3), (0, 7))
    word_locations[1] = ((0, 3), (4, 3))
    word_locations[2] = ((0, 5), (6, 5))
    word_locations[3] = ((3, 0), (3, 6))
    
    population = 100
    num_iteration = 2000
    crossover_ratio = 0.8
    board_list = []
    
    start_time = time.time()
    for i in range(population):
        board = CrossWordBoard(8, 7, word_locations)
        board.randomInit()
        board.computeFitness()
        board_list.append(board)
        
    for iter in range(num_iteration):
        # choose mutation or crossover based on ratio
        choice_prob = random.random()
        if choice_prob <= crossover_ratio:
            # perform crossover
            random_index1 = random.randrange(population)
            random_index2 = random_index1
            while random_index2 == random_index1:
                random_index2 = random.randrange(population)
                
            new_board1, new_board2 = performCrossover(board_list[random_index1], board_list[random_index2])
            new_board1.computeFitness()
            new_board2.computeFitness()
            board_list.append(new_board1)
            board_list.append(new_board2)
        else:
            # perform mutation
            random_index = random.randrange(population)
            new_board = copy.deepcopy(board_list[random_index])
            new_board.mutation()
            new_board.computeFitness()
            board_list.append(new_board)
            
        # sort all board based on fitness
        board_list.sort(key=lambda board : board.fitness, reverse=True)
        
        # remove board with low fitness from list until size of list equals population
        while len(board_list) > population:
            board_list = board_list[:-1]
            
        # fast termiation
        if board_list[0].fitness == 1:
            board_list[0].printBoard()
            break
            
    end_time = time.time()
    diff = end_time - start_time
    print('Running time: ' + str(diff))
    