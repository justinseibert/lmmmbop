import math
import time
pattern_section = [6,4,2,0,2,4,6,0,1,2,3,5,6,1,4,7,4,1,6,5,3,2,1,0,]
pattern_section = [6,6,4,4,2,2,0,0,7,7,6,6,5,5,4,4,3,3,2,2,1,1,0,0,6,6,4,4,2,2,0,0,6,3,0,]
# pattern_section = [5,4,4,4,3,3,2,2,2,1,0,7,6,6,5,5,2,1,1,1,0,0,7,6,]
# pattern_section = [7,6,5,4,3,2,1,0,1,2,3,2,1,0,1,2,3,4,5,6,7,1,2,3,4,5,6,7,6,5,4,5,6,7,6,5,4,3,2,1,0,]
# pattern_section = [1,2,3,4,5,6,7,6,5,4,3,2,1,0,]
# pattern_construction = [[ 6,5,4,3 ],[ 5,4,3,2 ],[ 4,3,2,1 ],[ 3,2,1,0 ],[ 7,2,1,0 ],[ 7,6,1,0 ],[ 7,6,5,0 ],[ 7,6,5,4 ],]
# pattern_repeat = [[1,2,3],[1,0,3],[1,0,3],[1,0,3],[1,2,3],[0,0,3],[0,0,3],[0,0,3],]
# pattern_construction = [[ 0,1,2,4 ],[ 1,2,3,5 ],[ 2,3,4,6 ],[ 3,4,5,7 ],[ 0,4,5,6 ],[ 1,5,6,7 ],[ 0,2,6,7 ],[ 0,1,3,7 ],]
# pattern_repeat = [[ 0,11 ],[ 1,10 ],[ 2,9  ],[ 3,8  ],[ 4,15 ],[ 5,14 ],[ 6,13 ],[ 7,12 ],]

# pattern_section = [7,6,5,4,3,2,1,0,1,2,3,2,1,0,1,2,3,4,5,6,7,1,2,3,4,5,6,7,6,5,4,5,6,7,6,5,4,3,2,1,0] # diamond
pattern_construction = [[ 0,1,2,4 ],[ 1,2,3,5 ],[ 2,3,4,6 ],[ 3,4,5,7 ],[ 0,4,5,6 ],[ 1,5,6,7 ],[ 0,2,6,7 ],[ 0,1,3,7 ]]
pattern_repeat = [[ 0,11 ],[ 1,10 ],[ 2,9  ],[ 3,8  ],[ 4,15 ],[ 5,14 ],[ 6,13 ],[ 7,12 ]]

pattern_rows = [] # [False,False,False,False,5,6,7,8]
repeat_length = len(pattern_repeat)*len(pattern_repeat[0])

def seedPattern(row, col):
    the_pattern_set = pattern_section[(row)%len(pattern_section)] # point in pattern_section corresponding to row length
    the_pattern_index = col%len(pattern_rows[the_pattern_set])

    return pattern_rows[the_pattern_set][the_pattern_index]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def main():
    print('length = '+str(repeat_length))
    # pattern_iterator = len(pattern_construction[0])
    for val in pattern_construction: # [1,2,3,4]
        a = [' ']*repeat_length
        for v in val:
            for r in pattern_repeat[v]:
                # print(r)
                a[r] = '+'
            # print(a)
        # print('-'*10)
        pattern_rows.append(a)

    for row in range(0,len(pattern_section)*1):
        line = ""
        for col in range(0,repeat_length*6):
            line += seedPattern(row, col)
        time.sleep(0.05)
        print(line)

if __name__ == '__main__':
    import pattern01
    main()