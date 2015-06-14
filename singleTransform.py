#!/usr/bin/python
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

def permute(password):
    def key(c):
		if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			return 10
		elif c in "abcdefghijklmnopqrstuvwxyz":
			return 20
		elif c in "0123456789":
			return 30
		else : 
			return 40
    return ''.join(sorted(password, key=key))

if __name__ == '__main__':
    import sys

    # take in an argument from the command line 
    password = sys.argv[1]

    # Call the primary function
    newPass = permute(password)

    # print result
    print newPass

