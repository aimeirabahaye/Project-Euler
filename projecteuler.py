#open a project euler question and print it to the screen with the answer
#if available

import urllib, re


url = 'https://projecteuler.net/problem='

def f():
    problem_number = raw_input('what is the problem\'s number?:\n')

    problem = urllib.urlopen(url + problem_number).read()
    print re.compile("\<p>(.*)\</p>").search(problem).group(1)

    see_answer = raw_input('do you want to see the answer? (yes, no):\n')
    
    if see_answer == 'yes':
        print 'ok..\n'
        
        try:
            print execfile((problem_number + '.py'))
        except IOError:
            print "You haven't solved this problem yet!"
            
    elif see_answer == 'no':
        print 'goodbye'
        return False
   
    return True

while f():
    f()