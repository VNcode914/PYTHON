import random
u= random.randint(1,45)
print("your high score is :",u)
with open("FILE/practice/hi_score.txt","r") as f:
    hi_score=f.read().strip()
if(hi_score==""):
    hi_score="0"
    
if(u>int(hi_score)):
    with open("FILE/practice/hi_score.txt","w") as f:
        i=f.write(str(u))
        print("new hi score is ",u)
    





# def game():
#     print("the game has started")
#     score = random.randint(1, 89)
#     with open("FILE/hiscore.txt","a+") as f
#     hiscore=f.read()
#     print(f"your high schore is ,{score}")
#     return score
# if(score >int (hiscore) or hiscore==""):
#     print(f.write())