# PasswordCrackingSystem
## programmer club colab

# Todo 
    ## attack manager
    the attack manager will monitor the attack, save all the data and progress of the clients.
    the clients will report with their progress after completing a block and the manager will assign them a new block to crack.
    
# a bit of explanation
when the attack starts the server will send the clients a metadata packet with the hash type (sha256, md5, etc...), and the hashed password we are want to find.
after the client gets that packet it will send a OK response to make sure its still alive and running.
next, the server will assign the client a block with some passwords to hash.
the client will hash all of them, check them out and report to the server if have been found.
if the client didnt find anything the server will assign anther block.
if any client did find the password, it will report to the server, and the server will close all of the other clients.
