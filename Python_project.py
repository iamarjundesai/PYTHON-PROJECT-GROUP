# -*- coding: utf-8 -*-
from easygui import*
import sys
sum=0
while 1:
    msgbox("WELCOME TO KBC ")
    
    
    msg="Would you like to play"
    title="KBC"
    choices=["Yes","No"]
    choice= choicebox(msg,title,choices)
    
    if choice=='Yes':
        msg1= "Twinkle twinkle little____"
        title1= "Question 1"
        choices1= ["girl","planet","star","boy"]
        choice1= choicebox(msg1,title1,choices1)
        if choice1=='star': 
            msgbox("SAHI JAWAB!!!!")
	    sum=sum+1
        else:
             sys.exit()
        
        msg2= "who is known as the father of our nation"
        title2= "Question 2"
        choices2= ["Mohandas Gandhi","Indira Gandhi","Rahul Gandhi","Sonia Gandhi"]
        choice2= choicebox(msg2,title2,choices2)
        if choice2=='Mohandas Gandhi':
            msgbox("SAHI JAWAB!!!!")
            sum=sum+1
        else: 
              sys.exit()
        
        msg3= "The National Anthem Of INDIA has been written by___"
        title3="Question 3"
        choices3=["Rabindranath Tagore","Bankim Chandra Chatterjee","Sumitranandan Pant","Mirza Galiib"]
        choice3= choicebox(msg3,title3,choices3)
        if choice3=='Rabindranath Tagore':
            msgbox("SAHI JAWAB!!!!")
    	    sum=sum+1
        else: 
              sys.exit()
        
        msg4= "Which Cricketer has the record of scoring the fastest 10000 runs in ODI cricket "
        title4="Question 4"
        choices4=["Ricky Ponting","Sachin Tendulkar","Ab De Villiars","Virat Kohli"]
        choice4= choicebox(msg4,title4,choices4)
        if choice4=='Virat Kohli':
            msgbox("SAHI JAWAB!!!!")
 	    sum=sum+1
        else: 
              sys.exit()
         
          
        msg5= "Which movie won the oscar for the best movie in 2017?"
        title5="Question 5"
        choices5=["La La Land","Moonlight","The Post","Dunkirk"]
        choice5= choicebox(msg5,title5,choices5)
        if choice5=='Moonlight':
            msgbox("SAHI JAWAB!!!!")
       	    sum=sum+1
        else: 
              sys.exit()    
        
        msg6= "Which organisation has been successful in making fully reusable rockets?"
        title6="Question 6"
        choices6=["ISRO","NASA","Space X","ESA"]
        choice6= choicebox(msg6,title6,choices6)
        if choice6=='Space X':
            msgbox("SAHI JAWAB!!!!")
            sum=sum+1
        else: 
              sys.exit()    
              
        msg7= "Which of these is not a capital cities?"
        title7="Question 7"
        choices7=["Cape Town","Pretoria","Bloemfontein","Johannesburg"]
        choice7= choicebox(msg7,title7,choices7)
        if choice7=='Johannesburg':
            msgbox("SAHI JAWAB!!!!")
	    sum=sum+1
        else: 
              sys.exit()          
            
        msg8= "Who is the first woman to reach the top of Mt. Everest?"
        title8="Question 8"
        choices8=["Junko Tabei","Bachendri Pal","Stacy Allison","Wanda Rutkiewicz"]
        choice8= choicebox(msg8,title8,choices8)
        if choice8=='Junko Tabei':
            msgbox("SAHI JAWAB!!!!")
	    sum=sum+1
        else: 
              sys.exit()         
       
        msg9= "Which Chief Minister has served for the longest period of time?"
        title9="Question 9"
        choices9=["Jyoti Basu,West Bengal","Pawan Kumar Chumling,Sikkim","Gegong Apang,Arunachal Pradesh","Lal Thanhawla,Mizoram"]
        choice9= choicebox(msg9,title9,choices9)
        if choice9=='Pawan Kumar Chumling,Sikkim':
            msgbox("SAHI JAWAB!!!!")
	    sum=sum+1
        else: 
              sys.exit()    
              
        msg10= "Sojo aur Arjun ke Pita ka naam kya hain?"
        title10="Question 10"
        choices10=["Santosh","Sandeep","Sanjay","Sanjeev"]
        choice10= choicebox(msg10,title10,choices10)
        if choice10=='Sanjay':
            msgbox("SAHI JAWAB!!!!")
	    sum=sum+1
        else: 
              sys.exit()  
	msgbox   
              
    else:
        sys.exit()          
