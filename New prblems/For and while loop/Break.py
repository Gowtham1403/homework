############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the color"
#Continue until they is atleast 3 movies they both like




MovieNameList=[]
commonMovieList=[]
commonMovieCount = 0
#To run infinite time we give true
while (True) :
#ask the first user
    FirstUserMovie = input("What are the movies you like freind 1 ?")
    MovieNameList.append(FirstUserMovie)
#ask the second user
    SecondUserMovie = input("What are the movies you like friend 2 ? ")
    if SecondUserMovie in MovieNameList:
        print("You both friends like the same movies !!")
        commonMovieList.append(SecondUserMovie) 
        commonMovieCount+=1
 #check the condition whether it reach the maximum number
    if(commonMovieCount >= 3):
        break
    else:
        print ("Try again")
#print the common movies 
print("The common movies that like by two friends are : ")
print(commonMovieList)


'''
Output:

What are the movies you like freind 1 ?bahubali
What are the movies you like friend 2 ? kochadaiyaan
Try again
What are the movies you like freind 1 ?thunivu
What are the movies you like friend 2 ? thunivu
You both friends like the same movies !!
Try again
What are the movies you like freind 1 ?veeram
What are the movies you like friend 2 ? veeram
You both friends like the same movies !!
Try again
What are the movies you like freind 1 ?h
What are the movies you like friend 2 ? h
You both friends like the same movies !!
The common movies that like by two friends are :
['thunivu', 'veeram', 'h']
'''