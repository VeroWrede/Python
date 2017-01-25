n = raw_input("Player one, rock paper scissor?? :  ")
m = raw_input("Player two, rock paper scissor?? :  ")
lst = {'rock', 'scissor', 'paper'}

if n in lst and m in lst: 
    if n == m:
        print "You read minds! Try again"
    elif n == 'paper' and m == 'rock':
        print "Player one winns"
        break
    elif n == 'rock' and m == 'paper':
        print "Player two winns"
        break 
    elif n == "paper" and m == "scissor":
        print "Player one winns"
        break
    elif n == "rock" and m == "scissor":
        print "Player one winns"
        break
    elif n == 'scissor' and m == 'paper':
        print "Player one winns"
        break
    elif n == 'scissor' and m == 'rock':
        print " Player two winns" 
        break
            
        
        


# rock > scissor > paper > rock