
'''Write a Python program to reverse a string.

Sample String : "1234abcd"
Expected Output : "dcba4321"'''



def string_reverse():

    '''take a input from user'''
    str1=input('enter string: ')

    '''creat an empty string to concatenation of resulting strings'''
    rstr1 = ''
    index = len(str1)

    while index > 0:
        '''concatenating from last element of the string'''
        rstr1 =rstr1+str1[ index - 1 ]      
        index = index - 1
    return rstr1
print(string_reverse())

