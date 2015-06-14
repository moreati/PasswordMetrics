#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################################
## This program takes a string as input (a password) and    ##
##  permutes the password.				    				##
##############################################################
# How to use: ./programName.py [password_string]            ##
# Example: ./transform.py ABCabc123!!!                      ##
# Note: Ensure the #!/location/to/python is correct		    ## 
# Note: Make sure to chmod a+x [filename] on your system 	## 
# Note: Some characters such as the ' and ; interact with   ##
# the shell and don't permute properly.	 Passing it in as   ##
# a file containing the password makes it perform better    ##
##############################################################

# Depths of printable ASCII symbols on mobile operating systems
# Key:
#   1 Available on the default keyboard
#   2 Available by switching keyboard once.
#   3 Available by switching keyboard twice.
#   - Not available, or requires a long press
# Source: http://jfranklin.me/prez/ACSAC-Poster-FINAL.pdf
#
#           ␠ ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
# ---------------------------------------------------------------------------
# iOS 8     1 2 2 2 2 2 2 2 2 2 2 2 1 2 1 2 2 2 3 3 3 2 2 3 3 3 3 2 3 3 3 3 3
# Android L 1 2 2 3 2 3 2 2 2 2 3 3 2 2 2 2 2 2 3 3 3 2 2 3 3 3 3 3 - 3 3 3 3
# WinPh 8.1 1 2 2 2 2 2 2 2 2 2 2 3 2 2 1 2 2 2 3 3 3 2 2 3 2 3 3 3 - 3 3 3 3
#
# MAXIMUM   1 2 2 3 2 3 2 2 2 2 3 3 2 2 2 2 2 2 3 3 3 2 2 3 3 3 3 3 - 3 3 3 3
# ---------------------------------------------------------------------------
#           ␠ ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

import string

__all__ = ['MOBILEOS_COMMON_SYMBOLS',
           'simple_key',
           'mobileos_key',
           'permute',
           ]

MOBILEOS_COMMON_SYMBOLS = '''!"$&'(),-./:;?@'''

def simple_key(c):
    '''Return a sort key to order characters by case, digits etc.

    The groups are: uppercase, lowercase, digits, other.
    '''
    if c in string.ascii_uppercase:
        return 10
    elif c in string.ascii_lowercase:
        return 20
    elif c in string.digits:
        return 30
    else:
        return 40

def mobileos_key(c):
    '''Return a sort key to order characters by mobile OS keyboard depth.

    The groups are: uppercase, lowercase, digits, common symbols, other.
    Common symbols are those available from the level 2 keyboard, across
    mobile operating systems.
    '''
    simple = simple_key(c)
    if simple < 40 or c in MOBILEOS_COMMON_SYMBOLS:
        return simple
    else:
        return 50

def permute(password, key=mobileos_key):
    '''Return a permuted of a password that is easier to type on a mobile
    device.

    Characters are grouped to minimize switching between keyboards, and
    hence reduce the number of keystrokes.

    >>> permute('m#o)fp^2aRf207')
    'Rmofpaf2207)#^'
    >>> permute('m#o)fp^2aRf207', key=simple_key)
    'Rmofpaf2207#)^'
    '''
    return ''.join(sorted(password, key=key))

def main():
    import sys

    password = sys.argv[1]
    new_password = permute(password)
    print(new_password)

if __name__ == '__main__':
    main()
