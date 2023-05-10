# here I want to test the more graphical aspects of the game

#    Remaining lives: 3 
#     ________
#    |        |     A B C D E  
#    |    ( )_|     F G H I J 
#    |    /|\       K L M N O  
#    |   | | |      P Q R S T  
#    |    / \       U V W X Y Z
#    |   /   \ 
#    | 
#    |__________
#
#    P I Z Z _ 

hang_3 = (' '*4 + '_'*8 + '\n'
          + ' '*3 + '|' + ' '*8 + '|')

hang_4 = ('    ________' + '\n' + '   |        |    Remaining lives: 3' + '\n' + '   |    ( )_|' + '\n' + 
          '   |    /|\      A B C D E' + '\n' + '   |   | | |     F G H I J' + '\n' + '   |    / \  ')

print(hang_4)


#     ________
#    |        |       
#    |    ( )_|     
#    |    /|\        
#    |   | | |       
#    |    / \       
#    |   /   \ 
#    | 
#    |__________