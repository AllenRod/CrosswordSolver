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

def geneticAlgorithm(width, height, word_locations, population, num_iteration, tournament_size, crossover_ratio):
    board_list = []
    start_time = time.time()
    crossover_count = 0
    mutation_count = 0
    best_board = None
    
    for i in range(population):
        board = CrossWordBoard(width, height, word_locations)
        board.randomInit()
        board.computeFitness()
        board_list.append(board)
        
    for iter in range(num_iteration):
        if iter % 5000 == 0:
            print('Current iteration: ' + str(iter))
            
        # choose tournament size of individuals
        tournament_list = []
        while len(tournament_list) < tournament_size:
            individual = random.randrange(population)
            if individual not in tournament_list:
                tournament_list.append(individual)
        
        # sort individuals in tournament based on fitness
        tournament_list.sort(key=lambda board_index : board_list[board_index].fitness, reverse=True)
    
        # choose mutation or crossover based on ratio
        choice_prob = random.random()
        if choice_prob <= crossover_ratio:
            # perform crossover
            individual_index1 = tournament_list[0]
            individual_index2 = tournament_list[1]
                
            new_board1, new_board2 = performCrossover(board_list[individual_index1], board_list[individual_index2])
            new_board1.computeFitness()
            new_board2.computeFitness()
            board_list.append(new_board1)
            board_list.append(new_board2)
            crossover_count += 1
        else:
            # perform mutation
            individual_index = tournament_list[0]
            new_board = copy.deepcopy(board_list[individual_index])
            new_board.mutation()
            new_board.computeFitness()
            board_list.append(new_board)
            mutation_count += 1
            
        # sort all board based on fitness
        board_list.sort(key=lambda board : board.fitness, reverse=True)
        
        # remove board with low fitness from list until size of list equals population
        while len(board_list) > population:
            board_list = board_list[:-1]
            
        #if best_board is None or board_list[0].fitness > best_board.fitness:
        #    best_board = copy.deepcopy(board_list[0])
        
        # fast termiation
        if board_list[0].fitness == 1:
            break
            
    end_time = time.time()
    diff = end_time - start_time
    print('Running time: ' + str(diff))
    print('Number of crossover: ' + str(crossover_count))
    print('Number of mutation: ' + str(mutation_count))
    
    print('Best Board')
    board_list[0].printBoard()
    print('Best board fitness: ' + str(board_list[0].fitness))
    
def easyExample():
    word_locations = dict()
    word_locations[0] = ((0, 3), (0, 7))
    word_locations[1] = ((0, 3), (4, 3))
    word_locations[2] = ((0, 5), (6, 5))
    word_locations[3] = ((3, 0), (3, 6))
    
    population = 100
    num_iteration = 2000
    tournament_size = 5
    crossover_ratio = 0.8
    
    geneticAlgorithm(8, 7, word_locations, population, num_iteration, tournament_size, crossover_ratio)
    
def mediumExample0():
    word_locations = dict()
    word_locations[0] = ((0, 0), (0, 5))
    word_locations[1] = ((2, 0), (2, 3))
    word_locations[2] = ((4, 0), (4, 5))
    word_locations[3] = ((0, 0), (5, 0))
    word_locations[4] = ((0, 2), (5, 2))
    word_locations[5] = ((3, 4), (3, 5))
    word_locations[6] = ((3, 4), (5, 4))
    word_locations[7] = ((0, 5), (4, 5))
    
    population = 3000
    num_iteration = 12000
    tournament_size = 50
    crossover_ratio = 0.7
    
    geneticAlgorithm(6, 6, word_locations, population, num_iteration, tournament_size, crossover_ratio)
    
def mediumExample():
    word_locations = dict()
    word_locations[0] = ((0, 3), (0, 5))
    word_locations[1] = ((1, 2), (1, 6))
    word_locations[2] = ((2, 1), (2, 7))
    word_locations[3] = ((3, 0), (3, 3))
    word_locations[4] = ((3, 5), (3, 8))
    word_locations[5] = ((4, 0), (4, 2))
    word_locations[6] = ((4, 6), (4, 8))
    word_locations[7] = ((5, 0), (5, 3))
    word_locations[8] = ((5, 5), (5, 8))
    word_locations[9] = ((6, 1), (6, 7))
    word_locations[10] = ((7, 2), (7, 6))
    word_locations[11] = ((8, 3), (8, 5))
    
    word_locations[12] = ((3, 0), (5, 0))
    word_locations[13] = ((2, 1), (6, 1))
    word_locations[14] = ((1, 2), (7, 2))
    word_locations[15] = ((0, 3), (3, 3))
    word_locations[16] = ((5, 3), (8, 3))
    word_locations[17] = ((0, 4), (2, 4))
    word_locations[18] = ((6, 4), (8, 4))
    word_locations[19] = ((0, 5), (3, 5))
    word_locations[20] = ((5, 5), (8, 5))
    word_locations[21] = ((1, 6), (7, 6))
    word_locations[22] = ((2, 7), (6, 7))
    word_locations[23] = ((3, 8), (5, 8))
    
    population = 6000
    num_iteration = 250000
    tournament_size = 50
    crossover_ratio = 0.7
    
    geneticAlgorithm(9, 9, word_locations, population, num_iteration, tournament_size, crossover_ratio)

#def hardExample():
#    word_locations = dict()
#    word_locations[0] = ((0, 0), (6, 0))
#    word_locations[1] = ((0, 1), (2, 1))
#    word_locations[2] = ((0, 2), (1, 2))
#    word_locations[3] = ((0, 5), (1, 5))
#    word_locations[4] = ((0, 6), (2, 6))
#    word_locations[5] = ((0, 7), (1, 7))
#    word_locations[6] = ((4, 1), (5, 1))
#    word_locations[7] = ((7, 1), (8, 1))
#    word_locations[8] = ((3, 2), (4, 2))
#    word_locations[9] = ((6, 2), (8, 2))
#    word_locations[10] = ((2, 3), (5, 3))
#    word_locations[11] = ((7, 3), (8, 3))
#    word_locations[12] = ((1, 4), (3, 4))
#    word_locations[13] = ((5, 4), (7, 4))
#    word_locations[14] = ((3, 5), (6, 5))
#    word_locations[15] = ((4, 6), (5, 6))
#    word_locations[16] = ((7, 6), (8, 6))
#    word_locations[17] = ((3, 7), (4, 7))
#    word_locations[18] = ((6, 7), (8, 7))
#    word_locations[19] = ((2, 8), (8, 8))
#    
#    word_locations[20] = ((0, 0), (0, 3))
#    word_locations[21] = ((0, 5), (0, 8))
#    word_locations[22] = ((1, 0), (1, 2))
#    word_locations[23] = ((1, 4), (1, 7))
#    word_locations[24] = ((2, 0), (2, 1))
#    word_locations[25] = ((3, 2), (3, 5))
#    word_locations[26] = ((3, 7), (3, 8))
#    word_locations[27] = ((4, 0), (4, 3))
#    word_locations[28] = ((4, 5), (4, 8))
#    word_locations[29] = ((5, 0), (5, 1))
#    word_locations[30] = ((5, 3), (5, 6))
#    word_locations[31] = ((6, 4), (6, 5))
#    word_locations[32] = ((6, 7), (6, 8))
#    word_locations[33] = ((7, 1), (7, 4))
#    word_locations[34] = ((7, 6), (7, 8))
#    word_locations[35] = ((8, 0), (8, 3))
#    word_locations[36] = ((8, 5), (8, 8))
#    
#    population = 5000
#    num_iteration = 20000
#    tournament_size = 10
#    crossover_ratio = 0.8
#    
#    geneticAlgorithm(9, 9, word_locations, population, num_iteration, tournament_size, crossover_ratio)
    
def hardExample():
    word_locations = dict()
    word_locations[0] = ((0, 0),  (0, 3))
    word_locations[1] = ((0, 5),  (0, 7))
    word_locations[2] = ((0, 9),  (0, 12))
    word_locations[3] = ((1, 0),  (1, 3))
    word_locations[4] = ((1, 5),  (1, 7))
    word_locations[5] = ((1, 9),  (1, 12))
    word_locations[6] = ((2, 0),  (2, 3))
    word_locations[7] = ((2, 5),  (2, 7))
    word_locations[8] = ((2, 9),  (2, 12))
    word_locations[9] = ((10, 0),  (10, 3))
    word_locations[10] = ((10, 5),  (10, 7))
    word_locations[11] = ((10, 9),  (10, 12))
    word_locations[12] = ((11, 0),  (11, 3))
    word_locations[13] = ((11, 5),  (11, 7))
    word_locations[14] = ((11, 9),  (11, 12))
    word_locations[15] = ((12, 0),  (12, 3))
    word_locations[16] = ((12, 5),  (12, 7))
    word_locations[17] = ((12, 9),  (12, 12))
    word_locations[18] = ((3, 0),  (3, 5))
    word_locations[19] = ((3, 7),  (3, 12))
    word_locations[20] = ((9, 0),  (9, 5))
    word_locations[21] = ((9, 7),  (9, 12))
    word_locations[22] = ((4, 3),  (4, 5))
    word_locations[23] = ((4, 7),  (4, 9))
    word_locations[24] = ((8, 3),  (8, 5))
    word_locations[25] = ((8, 7),  (8, 9))
    word_locations[26] = ((5, 0),  (5, 4))
    word_locations[27] = ((5, 8),  (5, 12))
    word_locations[28] = ((7, 0),  (7, 4))
    word_locations[29] = ((7, 8),  (7, 12))
    word_locations[30] = ((6, 0),  (6, 2))
    word_locations[31] = ((6, 10),  (6, 12))
    word_locations[32] = ((0, 0),  (3, 0))
    word_locations[33] = ((5, 0),  (7, 0))
    word_locations[34] = ((9, 0),  (12, 0))
    word_locations[35] = ((0, 1),  (3, 1))
    word_locations[36] = ((5, 1),  (7, 1))
    word_locations[37] = ((9, 1),  (12, 1))
    word_locations[38] = ((0, 2),  (3, 2))
    word_locations[39] = ((5, 2),  (7, 2))
    word_locations[40] = ((9, 2),  (12, 2))
    word_locations[41] = ((0, 10),  (3, 10))
    word_locations[42] = ((5, 10),  (7, 10))
    word_locations[43] = ((9, 10),  (12, 10))
    word_locations[44] = ((0, 11),  (3, 11))
    word_locations[45] = ((5, 11),  (7, 11))
    word_locations[46] = ((9, 11),  (12, 11))
    word_locations[47] = ((0, 12),  (3, 12))
    word_locations[48] = ((5, 12),  (7, 12))
    word_locations[49] = ((9, 12),  (12, 12))
    word_locations[50] = ((0, 3),  (5, 3))
    word_locations[51] = ((7, 3),  (12, 3))
    word_locations[52] = ((0, 9),  (5, 9))
    word_locations[53] = ((7, 9),  (12, 9))
    word_locations[54] = ((3, 4),  (5, 4))
    word_locations[55] = ((7, 4),  (9, 4))
    word_locations[56] = ((3, 8),  (5, 8))
    word_locations[57] = ((7, 8),  (9, 8))
    word_locations[58] = ((0, 5),  (4, 5))
    word_locations[59] = ((8, 5),  (12, 5))
    word_locations[60] = ((0, 7),  (4, 7))
    word_locations[61] = ((8, 7),  (12, 7))
    word_locations[62] = ((0, 6),  (2, 6))
    word_locations[63] = ((10, 6),  (12, 6))
    
    population = 6000
    num_iteration = 250000
    tournament_size = 50
    crossover_ratio = 0.7
    
    geneticAlgorithm(13, 13, word_locations, population, num_iteration, tournament_size, crossover_ratio)
    
if __name__ == '__main__':
    #easyExample()
    #mediumExample()
    #mediumExample0()
    hardExample()