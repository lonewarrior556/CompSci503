import random 


f=open('words.txt')

a='word'
ls=[]
while a!='':
    a=f.readline()
    ls.append(a[:-2])

print "ok ready let's begin"

def printstrikes(n):
    print '\n'
    striked=n*' x '
    chance=(7-n)*' _ '
    print striked+chance

def printfield(word,guessed):
    field=''
    for x in word:
        if x in guessed:
            field+=' '+x+' '
        else: field+=' _ '
    if '_' in field:
        print field
    else: 
        print "You win!"
        return 'done'



playing=True

while playing:
    word=random.choice(ls)
    strike=0
    guessed=''
    done='no'
    while strike < 7 and done!='done':
        print '\n'
        print "strikes:"
        printstrikes(strike)
        print '\n'
        print '\n'
        done=printfield(word,guessed)
        g=raw_input("guess a letter... ")
        if g in word:
            guessed+=g
        else: 
            strike+=1
            if strike==7:
                print "You lose"
    end=raw_input('play again?, y/n ')
    if end=='n':
        playing=False

