# eating apples

input_string = int(input())
while input_string != 'quit':
    mylist=input_string.split()
    print('Eating {1} {0} a day keeps the doctor away.'.format(mylist[0], mylist[1]))
    input_string = input()
