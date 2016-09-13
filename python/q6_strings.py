# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

    """
    1) Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """

def donuts(count):
    s_prefix = 'Number of donuts: ' 
    if count < 10:
        return s_prefix + str(count) 
    else: 
        return s_prefix + "many" 


    """
    2) Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """

def both_ends(s):
    first2 = s[0:2]
    last2 = s[-2:]

    if len(s) < 2:
        return ' '
    if len(s) > 2:
        return first2 + last2


    """
    3) Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    
def fix_start(s):
    front = s[0] 
    back = s[1] 
    fixed_back = back.replace(front, '*') 
    return front + fixed_back 


    """
   4)  Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    
def mix_up(a, b): 
    a_swapped = b[:2] + a[2:] 
    b_swapped = a[:2] + b[2:]
    return a_swapped + ' ' + b_swapped 


    """
   5)  Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """

def verbing(s):
    if len(s) >= 3:
        return s + 'ing'
    if len(s) < 3:
        return s
    if (s[-3:] == 'ing'):
        return s + 'ly'



    """
  6) Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

def not_bad(s):
  n = s.find('not')
  b = s.find('bad')
  if n != -1 and b != -1 and b > n:
    s = s[:n] + 'good' + s[b+3:]
  return s


    """
    7) Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
 def front_back(a, b):
     a_middle = len(a)/2 
     b_middle = len(b)/2 
     if len (a) % 2 = 1: 
         a_middle = a_middle + 1 
     if len (b) % 2 = 1: 
         b_middle = b_middle + 1 
     return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]


