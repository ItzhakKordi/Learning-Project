 #Menu
 import random

 def menuscreen(start,options,exit):
 	print("1.Start the game")
 	print("2.Options (in progress)")
 	print("3.Exit")

 def playerturn(player,health):
 	print("It's ",player[1]," turn")
 	choice = int(input("Which attack would you like to use?"))
 	attacks(choice)

 def attacks(attacktype)
 	if attacktype == 'Punch':
 		damage = random.randint(1,5)
 		hitchance = random.randint(0,100)
 		if hitchance > 25:
 			hit = True
 		else:
 			hit = False
 	if attacktype == 'Kick':
 		damage = random.randint(4,15)
 		hitchance = random.randint(0,100)
 		if hitchance < 50:
 			hit = True
 		else:
 			hit = False
 	if attacktype == 'Headbut':
 		damage = random.randint(10,20)
 		hitchance = random.randint(0,100)
 		if hitchance < 25:
 			hit = True
 		else:
 			hit = False
 	attackdata = [damage,hit]
 	return attackdata

 def switchplayer(player):
 	if player == 1:
 		return 2
 	else:
 		return 1
 def checkhealth(player1,player2):
 	if player1[0] <=0:
 		print(player2[1]," has won the game")
 		endgame()
 	elif player2[0] <=0:
 		print(player1[1]," has won the game")
 		endgame()
 def endgame():
 	return False





 	




 attacks = ['Punch','Kick','Headbut']	

 	menu=int(input("press a number on the menu to procceed"))
 	if menu == 1:
 		startgame()
 	elif menu == 2:
 		options()
 	elif menu == 3:
 		exit()



 	
 menu=int(input("press a number on the menu to procceed"))


 
