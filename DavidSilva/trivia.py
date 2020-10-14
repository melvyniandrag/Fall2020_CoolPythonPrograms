iprint('Hello, Welcome to Trivia By David Silva')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. The beaver is the national emblem of which counrty? ')
    if ans.lower() == 'Canada' :
       score += 1
       print('correct') 
    else:
       print('Incorrect')	
          
          
    ans = input('2. What word can go before "decision","personality","second"?') 
    if ans.lower() == 'Split' :
       score += 1
       print('correct') 
    else:
       print('Incorrect')	
          
          
    ans = input('3. What does the H stand for in the medical abbreviation ADHD ? ')
    if ans.lower() == 'Hyperactivity' :
       score += 1
       print('correct') 
    else:
       print('Incorrect')	
          
          
          
    ans = input('4. Who was the prsident during World War 1? ')
    if ans.lower() == 'Woodrow Wilson' :
       score += 1
       print('correct') 
    else:
            print('Incorrect')

    print('Thank You for playing, you got', score, "question correct." 
    mark = (score/total_q) * 100

    print("Mark:", mark + '%'))
print('Goodbye')
