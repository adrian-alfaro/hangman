# here I want to test the more graphical aspects of the game
blanks = 'P I Z Z _'
lifes = 3
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#    This is a reference
#     ________
#    |        |     Remaining lifes: 3  
#    |        |
#    |    ( )_|     A B C D E 
#    |    /|\       F G H I J  
#    |   | | |      K L M N O  
#    |    / \       P Q R S T 
#    |   /   \      U V W X Y Z 
#    |__________
#
#    P I Z Z _ 
#
# Next letter is:

hang_1 = ('    ________' + '\n' +
          f'   |        |    Remaining lifes: {lifes}' + '\n' +
           '   |    ( )_|' + '\n' + 
          f'   |    /|\      {abc[0] } {abc[1] } {abc[2] } {abc[3] } {abc[4] }' + '\n' + 
          f'   |   | | |     {abc[5] } {abc[6] } {abc[7] } {abc[8] } {abc[9] }' + '\n' +
          f'   |    / \      {abc[10]} {abc[11]} {abc[12]} {abc[13]} {abc[14]}' + '\n' +
          f'   |   /   \     {abc[15]} {abc[16]} {abc[17]} {abc[18]} {abc[19] }' + '\n' +
          f'   |__________   {abc[20]} {abc[21]} {abc[22]} {abc[23]} {abc[24]} {abc[25]}' +
          '\n\n' + f'   {blanks}')

print(hang_1)


#     ________
#    |        |       
#    |    ( )_|     
#    |    /|\        
#    |   | | |       
#    |    / \       
#    |   /   \ 
#    | 
#    |__________