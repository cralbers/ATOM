'''if index(string.punctuation) = something fuck idk

Credits: https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file-using-dictionary/

'''

import string
import p61_data_analysis as p61

def fcounts(fname):
    '''
    '''
    with open(fname, 'r') as fcounts:
        # determine number of lines in file
        counter = 0
        content = fcounts.read()
        line_list = content.split('\n')

        d = {}
        for line in fcounts:
            line = line.strip()
            line = line.lower()
            words = line.split(' ')

            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    dict.append(word)
                    d[word] = 1
        for key in list(d.keys()):
            print(key, ':', d[key])
        print(d)

        for item in line_list:
            if item:
                counter = counter + 1

        # determine number of characters
        counter_2 = 0
        for char in content:
            if char not in string.punctuation and char != '\n':
                counter_2 =  counter_2 + 1

        # generate list of words in same case with no punctuation
        same_case_list = []
        for word in line_list:
            word = word.lower()
            word = word.strip(string.punctuation)
            same_case_list.append(word)

        # determine number of occurences of each word
        '''word_list = []
        for word in same_case_list:
            if word not in word_list:
                word_list.append(word)
        print(word_list)'''

        # print statements
        print('The number of lines in file', fname, 'is:', counter)
        print('The number of characters in file', fname, 'is:', counter_2)
        p61.frequencyTable(same_case_list)
