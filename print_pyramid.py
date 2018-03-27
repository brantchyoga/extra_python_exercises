# Implement a program that prints out a half-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     #
    ##
   ###
  ####
 #####
######

def half_pyramid(num):

    for i in range(num+1):
        print(' '* (num-i),'#'*i)
half_pyramid(6)

# Challenge
# Implement a program that prints out a full-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     # #
    ## ##
   ### ###
  #### ####
 ##### #####
###### ######


def pyramid(num):

    for i in range(num+1):
        print(' '* (num-i),'#'*i,' ','#'*i)
pyramid(6)
