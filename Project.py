# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:38:26 2018

@author: Darwin
"""

from nltk.corpus import words
import random
import sys
import time


words_list = words.words()
print(len(words_list))

dict_1 = {}
dict_2 = {}
dict_3 = {}
dict_4 = {}
dict_5 = {}
dict_6 = {}
dict_7 = {}
dict_8 = {}
dict_9 = {}
dict_10 = {}
dict_11 = {}
dict_12 = {}

word_dict = {}

for word in words_list:
    word_dict[word.lower()] = 1

for word in words_list:
    if len(word) == 1:
        dict_1[word.lower()] = 1
    if len(word) == 2:
        dict_2[word.lower()] = 1
    if len(word) == 3:
        dict_3[word.lower()] = 1
    if len(word) == 4:
        dict_4[word.lower()] = 1
    if len(word) == 5:
        dict_5[word.lower()] = 1
    if len(word) == 6:
        dict_6[word.lower()] = 1
    if len(word) == 7:
        dict_7[word.lower()] = 1
    if len(word) == 8:
        dict_8[word.lower()] = 1
    if len(word) == 9:
        dict_9[word.lower()] = 1
    if len(word) == 10:
        dict_10[word.lower()] = 1
    if len(word) == 11:
        dict_11[word.lower()] = 1
    if len(word) == 12:
        dict_12[word.lower()] = 1

#usia, ansi, orin, rene, haines, multi, ely, usc
# adding words to dict to complete solution for hard puzzle
dict_3['usc'] = 1
dict_3['ely'] = 1
dict_4['usia'] = 1
dict_4['ansi'] = 1
dict_4['orin'] = 1
dict_4['rene'] = 1
dict_5['multi'] = 1
dict_6['haines'] = 1

def minCons(indices, constraints, assignments):
    maxSteps = 350
    counter = 0
    
    while counter <= maxSteps:
        cVars = goal_check(indices, constraints, assignments)
              
        if cVars == []:
            print("Steps: ")
            print(counter)
            return assignments
            
        var = random.choice(cVars)
        if has_conflicts(var, constraints, assignments):
            assignments[var] = lcValue(var, indices, constraints, assignments)
        counter += 1
    
    correct = 0

    for word in assignments:
        if not has_conflicts(word, constraints, assignments):
            correct = correct + 1
    accuracy = correct/len(assignments) 
    print(str(accuracy))
    #print out accuracy; if greater than .65 print out the assignments
    if accuracy > .65:
        print(assignments)
    return None
        
def goal_check (indices, constraints, assignments):
    conflicted = []    
    for index in indices:
        if has_conflicts(index, constraints, assignments):
            conflicted.append(index)
    return conflicted        

def has_conflicts(index, constraints, assignments):
    currWord = assignments[index]
    for crosses in constraints[index]:
        neighbor = crosses[0]
        #print(crosses[1])
        #print(currWord)
        #print(index)
        #print(crosses[2])
        #print(assignments[neighbor])
        currLetter = currWord[crosses[1]-1]
        if assignments[neighbor][crosses[2]-1] != currLetter:
            return True
    return False
    
def lcValue (index, vars, constraints, assignments):  
    #valueConflicts = queue.PriorityQueue()  
    numConflicts = 0
    for neighbors in constraints[index]:
        currNeighbor = neighbors[0]
        if assignments[currNeighbor][neighbors[2]-1] != assignments[index][neighbors[1]-1]:
                numConflicts += 1
    word_len = vars[index]
    
    
    temp_word = assignments[index]      
    
    if word_len == 1:
        for word in dict_1:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word    
    
    if word_len == 2:
        for word in dict_2:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word    
    
    if word_len == 3:
        for word in dict_3:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word
                
    if word_len == 4:
        for word in dict_4:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word
                
    if word_len == 5:
        for word in dict_5:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word

    if word_len == 6:
        for word in dict_6:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word

    if word_len == 7:
        for word in dict_7:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]                
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word
                
    if word_len == 8:
        for word in dict_8:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word
                
    if word_len == 9:
        for word in dict_9:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word
                
    if word_len == 10:
        for word in dict_10:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word
                
    if word_len == 11:
        for word in dict_11:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word
                
    if word_len == 12:
        for word in dict_12:
            conflict_count = 0
            for neighbors in constraints[index]:
                currNeighbor = neighbors[0]
                if assignments[currNeighbor][neighbors[2]-1] != word[neighbors[1]-1]:
                    conflict_count += 1
            if conflict_count == 0:
                return word        
            elif conflict_count <= numConflicts:
                numConflicts = conflict_count
                temp_word = word
       
    return temp_word
    
'''    
#simple initialization

index_len = {1:5,2:7,3:5,4:7}
constraints = {1:[(2,3,1),(3,1,1)],
                  2:[(1,1,3),(4,4,6)],
                     3:[(1,1,1),(4,4,4)],
                        4:[(3,4,4),(2,6,4)]}

#another medium board
index_len = {1:6, 2:4, 3:2, 4:6, 5:6, 6:6, 7:3, 8:5}
constraints = {1:[(5,1,1),(6,3,1),(8,6,1)],
               2:[(5,1,3),(6,3,3)],
               3:[(7,1,1),(8,2,4)],
               4:[(5,1,5),(6,3,5),(7,5,2),(8,6,5)],
               5:[(1,1,1),(2,3,1),(4,5,1)],
               6:[(1,1,3),(2,3,3),(4,5,3)],
               7:[(3,1,1),(4,2,5)],
               8:[(1,1,6),(3,4,2),(4,5,6)]}

# unsolvable medium board                      
index_len = {1:3, 2:5, 3:7, 4:4, 5:4, 6:3, 7:3, 8:4, 9:4, 10:7, 11:5, 12:3,
             13:3, 14:5, 15:7, 16:4, 17:4, 18:3, 19:3, 20:4, 21:4, 22:7, 23:5, 24:3}
constraints = {1:[(16,1,1),(18,2,1),(20,3,1)],
              2:[(15,1,1),(16,2,2),(18,3,2),(20,4,2),(22,5,1)],
              3:[(14,1,1),(15,2,2),(16,3,3),(18,4,3),(20,5,3),(22,6,2),(23,7,1)],
              4:[(13,1,1),(14,2,2),(15,3,3),(16,4,4)],
              5:[(20,1,4),(22,2,3),(23,3,2),(24,4,1)],
              6:[(13,1,2),(14,2,3),(15,3,4)],
              7:[(22,1,4),(23,2,3),(24,3,2)],
              8:[(13,1,3),(14,2,4),(15,3,5),(17,4,1)],
              9:[(21,1,1),(22,2,5),(23,3,4),(24,4,3)],
              10:[(14,1,5),(15,2,6),(17,3,2),(19,4,1),(21,5,2),(22,6,6),(23,7,5)],
              11:[(15,1,7),(17,2,3),(19,3,2),(21,4,3),(22,5,7)],
              12:[(17,1,4),(19,2,3),(21,3,4)],
              13:[(4,1,1),(6,2,1),(8,3,1)],
              14:[(3,1,1),(4,2,2),(6,3,2),(8,4,2),(10,5,1)],
              15:[(2,1,1),(3,2,2),(4,3,3),(6,4,3),(8,5,3),(10,6,2),(11,7,1)],
              16:[(1,1,1),(2,2,2),(3,3,3),(4,4,4)],
              17:[(8,1,4),(10,2,3),(11,3,2),(12,4,1)],
              18:[(1,1,2),(2,2,3),(3,3,4)],
              19:[(10,1,4),(11,2,3),(12,3,2)],
              20:[(1,1,3),(2,2,4),(3,3,5),(5,4,1)],
              21:[(9,1,1),(10,2,5),(11,3,4),(12,4,3)],
              22:[(2,1,5),(3,2,6),(5,3,2),(7,4,1),(9,5,2),(10,6,6),(11,7,5)],
              23:[(3,1,7),(5,2,3),(7,3,2),(9,4,3),(10,5,7)],
              24:[(5,1,4),(7,2,3),(9,3,4)]}



# solvable medium board
# seed: 7034750912929758086
index_len = {1:3, 2:1, 3:5, 4:5, 5:1, 6:5, 7:3, 8:3, 9:4, 10:5, 11:3, 12:4, 13:3, 14:4}
constraints = {1:[(8,1,1),(10,2,1),(11,3,1)],
               2:[(14,1,1)],
               3:[(8,1,2),(10,2,2),(11,3,2),(13,4,1),(14,5,2)],
               4:[(8,1,3),(10,2,3),(11,3,3),(13,4,2),(14,5,3)],
               5:[(10,1,4)],
               6:[(13,1,3),(14,2,4)],
               7:[(9,1,1),(10,2,5),(12,3,1)],
               8:[(1,1,1),(3,2,1),(4,3,1)],
               9:[(7,1,1)],
               10:[(1,1,2),(3,2,2),(4,3,2),(5,4,1),(7,5,2)],
               11:[(1,1,3),(3,2,3),(4,3,3)],
               12:[(7,1,3)],
               13:[(3,1,4),(4,2,4),(6,3,1)],
               14:[(2,1,1),(3,2,5),(4,3,5),(6,4,2)]
               }
'''
# full crossword puzzle
index_len = {1:4, 2:3, 3:4, 4:4, 5:3, 6:4, 7:4, 8:3, 9:4, 10:6, 11:6, 12:3, 13:3, 14:5,
             15:5, 16:3, 17:3, 18:5, 19:5, 20:3, 21:3, 22:6, 23:6, 24:4, 25:3, 26:4, 27:4,
             28:3, 29:4, 30:4, 31:3, 32:4,
             33:4, 34:4, 35:4, 36:6, 37:5, 38:3, 39:5, 40:6, 41:4, 42:4, 43:4,
             44:3, 45:3, 46:3, 47:3, 48:3, 49:3, 50:3, 51:3, 52:6, 53:3, 54:3, 55:6,
             56:5, 57:5, 58:4, 59:4, 60:4, 61:4, 62:4, 63:4, 64:3}
constraints = {1:[(33,1,1),(34,2,1),(35,3,1),(36,4,1)],
              2:[(37,1,1),(38,2,1),(39,3,1)],
              3:[(40,1,1),(41,2,1),(42,3,1),(43,4,1)],
              4:[(33,1,2),(34,2,2),(35,3,2),(36,4,2)],
              5:[(37,1,2),(38,2,2),(39,3,2)],
              6:[(40,1,2),(41,2,2),(42,3,2),(43,4,2)],
              7:[(33,1,3),(34,2,3),(35,3,3),(36,4,3)],
              8:[(37,1,3),(38,2,3),(39,3,3)],
              9:[(40,1,3),(41,2,3),(42,3,3),(43,4,3)],
              10:[(33,1,4),(34,2,4),(35,3,4),(36,4,4),(44,5,1),(37,6,4)],
              11:[(39,1,4),(45,2,1),(40,3,4),(41,4,4),(42,5,4),(43,6,4)],
              12:[(36,1,5),(44,2,2),(37,3,5)],
              13:[(39,1,5),(45,2,2),(40,3,5)],
              14:[(46,1,1),(47,2,1),(48,3,1),(36,4,6),(44,5,3)],
              15:[(45,1,3),(40,2,6),(49,3,1),(50,4,1),(51,5,1)],
              16:[(46,1,2),(47,2,2),(48,3,2)],
              17:[(49,1,2),(50,2,2),(51,3,2)],
              18:[(46,1,3),(47,2,3),(48,3,3),(52,4,1),(53,5,1)],
              19:[(54,1,1),(55,2,1),(49,3,3),(50,4,3),(51,5,3)],
              20:[(52,1,2),(53,2,2),(56,3,1)],
              21:[(57,1,1),(54,2,2),(55,3,2)],
              22:[(58,1,1),(59,2,1),(60,3,1),(52,4,3),(53,5,3),(56,6,2)],
              23:[(57,1,2),(54,2,3),(55,3,3),(61,4,1),(62,5,1),(63,6,1)],
              24:[(58,1,2),(59,2,2),(60,3,2),(52,4,4)],
              25:[(56,1,3),(64,2,1),(57,3,3)],
              26:[(55,1,4),(61,2,2),(62,3,2),(63,4,2)],
              27:[(58,1,3),(59,2,3),(60,3,3),(52,4,5)],
              28:[(56,1,4),(64,2,2),(57,3,4)],
              29:[(55,1,5),(61,2,3),(62,3,3),(63,4,3)],
              30:[(58,1,4),(59,2,4),(60,3,4),(52,4,6)],
              31:[(56,1,5),(64,2,3),(57,3,5)],
              32:[(55,1,6),(61,2,4),(62,3,4),(63,4,4)],
              33:[(1,1,1),(4,2,1),(7,3,1),(10,4,1)],
              34:[(1,1,2),(4,2,2),(7,3,2),(10,4,2)],
              35:[(1,1,3),(4,2,3),(7,3,3),(10,4,3)],
              36:[(1,1,4),(4,2,4),(7,3,4),(10,4,4),(12,5,1),(14,6,4)],
              37:[(2,1,1),(5,2,1),(8,3,1),(10,4,6),(12,5,3)],
              38:[(2,1,2),(5,2,2),(8,3,2)],
              39:[(2,1,3),(5,2,3),(8,3,3),(11,4,1),(13,5,1)],
              40:[(3,1,1),(6,2,1),(9,3,1),(11,4,3),(13,5,3),(15,6,2)],
              41:[(3,1,2),(6,2,2),(9,3,2),(11,4,4)],
              42:[(3,1,3),(6,2,3),(9,3,3),(11,4,5)],
              43:[(3,1,4),(6,2,4),(9,3,4),(11,4,6)],
              44:[(10,1,5),(12,2,2),(14,3,5)],
              45:[(11,1,2),(13,2,2),(15,3,1)],
              46:[(14,1,1),(16,2,1),(18,3,1)],
              47:[(14,1,2),(16,2,2),(18,3,2)],
              48:[(14,1,3),(16,2,3),(18,3,3)],
              49:[(15,1,3),(17,2,1),(19,3,1)],
              50:[(15,1,4),(17,2,2),(19,3,2)],
              51:[(15,1,5),(17,2,3),(19,3,3)],
              52:[(18,1,4),(20,2,1),(22,3,4),(24,4,4),(27,5,4),(30,6,4)],
              53:[(18,1,5),(20,2,2),(22,3,5)],
              54:[(19,1,1),(21,2,2),(23,3,2)],
              55:[(19,1,2),(21,2,3),(23,3,3),(26,4,1),(29,5,1),(32,6,1)],
              56:[(20,1,3),(22,2,6),(25,3,1),(28,4,1),(31,5,1)],
              57:[(21,1,1),(23,2,1),(25,3,3),(28,4,3),(31,5,3)],
              58:[(22,1,1),(24,2,1),(27,3,1),(30,4,1)],
              59:[(22,1,2),(24,2,2),(27,3,2),(30,4,2)],
              60:[(22,1,3),(24,2,3),(27,3,3),(30,4,3)],
              61:[(23,1,4),(26,2,2),(29,3,2),(32,4,2)],
              62:[(23,1,5),(26,2,3),(29,3,3),(32,4,3)],
              63:[(23,1,6),(26,2,4),(29,3,4),(32,4,4)],
              64:[(25,1,2),(28,2,2),(31,3,2)]
              }
            
assignments = {}



randomRestarts = 100
startTime = time.time()

while randomRestarts > 0:
    seed = random.randrange(sys.maxsize)    
    # randomly choose seed for each restart
    rng = random.Random(seed)   
    
    for index in index_len:
        if index_len[index] == 1:
            assignments[index] = random.choice(list(dict_1))
        if index_len[index] == 2:
            assignments[index] = random.choice(list(dict_2))
        if index_len[index] == 3:
            assignments[index] = random.choice(list(dict_3))
        if index_len[index] == 4:
            assignments[index] = random.choice(list(dict_4))
        if index_len[index] == 5:
            assignments[index] = random.choice(list(dict_5))
        if index_len[index] == 6:
            assignments[index] = random.choice(list(dict_6))
        if index_len[index] == 7:
            assignments[index] = random.choice(list(dict_7))
        if index_len[index] == 8:
            assignments[index] = random.choice(list(dict_8))
        if index_len[index] == 9:
            assignments[index] = random.choice(list(dict_9))
        if index_len[index] == 10:
            assignments[index] = random.choice(list(dict_10))
        if index_len[index] == 11:
            assignments[index] = random.choice(list(dict_11))
        if index_len[index] == 12:
            assignments[index] = random.choice(list(dict_12))    
    
    
    if minCons(index_len, constraints, assignments) != None:
        print(assignments)
        time = time.time() - startTime
        print("Time: " + str(time))        
        randomRestarts = -100

    randomRestarts = randomRestarts - 1

if randomRestarts == 0:
    print("No solution found")
    time = time.time() - startTime
    print("Time: " + str(time))
    