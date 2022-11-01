# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:35:28 2020

@author: HP
"""
import random

movies=["avengers","matrix","harry potter","golmaal","inception","prestige","now you can see me"]


def movie_qn(movie):
    n=len(movie)
    qn=list(movie)
    temp=[]
    for i in range(n):
        if(qn[i]==' '):
            temp.append(' ')
        else:
            temp.append("*")
    ques="".join(str(x) for x in temp)
    return ques

def is_present(letter,movie):
    c=movie.count(letter)
    if(c==0):
        return False
    else:
        return True

def unlock(modified_qn,letter,movie):
    ref=list(movie)
    ques=list(modified_qn)
    n=len(movie)
    temp=[]
    for i in range(n):
        if(ref[i]==' ' or ref[i]==letter):
            temp.append(ref[i])
        elif(ques[i]=="*"):
            temp.append("*")
        else:
            temp.append(ref[i])
    qn_new="".join(str(x) for x in temp)
    return qn_new

def play():
    p1=input("player 1 input your name: ")
    p2=input("player 2 input your name: ")
    pp1=0
    pp2=0
    turn=0
    
    willing=True
    cont=True
    while(willing):
        if(turn%2==0):
            print(p1," your turn")
            picked_movie=random.choice(movies)
            qn=movie_qn(picked_movie)
            print(qn)
            modified_qn=qn
            while(cont):
                letter=input("enter a letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,letter,picked_movie)
                    print(modified_qn)
                    a=int(input("press 1 to guess the movie or 2 to unlock another letter: "))
                    if(a==1):
                        ans=input("movie name: ")
                        if(ans==picked_movie):
                            print("correct movie name")
                            pp1=pp1+1
                            print(p1," your score: ",pp1)
                            cont=False
                        else:
                            print("wrong answer,try again")
                else:
                    print("wrong letter")
                    
            b=int(input("press 1 to play or 0 to quit"))
            if(b==0):
                print(p1," your score: ",pp1)
                print(p2," your score: ",pp2)
                print("thanks for playing")
                willing=False
                break
           
        turn=turn+1
        if(turn%2!=0):
            print(p2," your turn")
            picked_movie=random.choice(movies)
            qn=movie_qn(picked_movie)
            print(qn)
            modified_qn=qn
            cont=True
            while(cont):
                letter=input("enter a letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,letter,picked_movie)
                    print(modified_qn)
                    a=int(input("press 1 to guess the movie or 2 to unlock another letter: "))
                    if(a==1):
                        ans=input("movie name: ")
                        if(ans==picked_movie):
                            print("correct movie name")
                            pp2=pp2+1
                            print(p2," your score: ",pp2)
                            cont=False
                        else:
                            print("wrong answer,try again")
                else:
                    print("wrong letter")
                    
            b=int(input("press 1 to play or 0 to quit"))
            if(b==0):
                print(p1," your score: ",pp1)
                print(p2," your score: ",pp2)
                print("thanks for playing")
                willing=False
            
play()
                
         
            
                
            
            
           
