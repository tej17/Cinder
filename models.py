import sqlite3 as sql

def insertUser(username,password):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
	con.commit()
	con.close()

def retrieveUsers():
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM users WHERE id=(SELECT max(id) FROM users);")
	users = cur.fetchall()
	con.close()
	return users

def checkUser(username,password):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("SELECT COUNT(*) from users WHERE username = ? AND password = ?", (username,password))
	count = cur.fetchall()
	con.close()
	return count

def insertUserDetails(username,password,age,image,gender,email,description):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("INSERT INTO userdetails (username,password,age,image,gender,email,description) VALUES (?,?,?,?,?,?,?)",(username,password,age,image,gender,email,description))
	con.commit()
	cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
	con.commit()
	con.close()

def retrieveUserDetails(gender):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM userdetails WHERE gender != ? ",(gender,))
	users = cur.fetchall()
	con.close()
	return users

def findGender(username):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("SELECT gender from userdetails where username = ?",(username,))
	users = cur.fetchall()
	con.close()
	return users

def checkMatch(liker,victim):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("SELECT COUNT(*) from matches where (groom = ? AND bride = ?) OR (bride = ? AND groom = ?)",(liker,victim,victim,liker,))
	users = cur.fetchall()
	con.close()
	return users

def insertMatch(liker,liked):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("INSERT into matches (groom,bride) VALUES (?,?)",(liker,liked,))
	users = cur.fetchall()
	con.commit()
	con.close()

def checkOneSided(liker,liked):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("SELECT COUNT(*) from onesided where likedby = ? AND liked = ?",(liker,liked,))
	users = cur.fetchall()
	con.close()
	return users


def insertOnesidedLikes(liker,victim):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("INSERT into onesided (likedby,liked) VALUES(?,?)",(liker,victim,))
	users = cur.fetchall()
	con.commit()
	con.close()

def retrieveMatches(liker):
	con = sql.connect("flaskr.db")
	cur = con.cursor()
	cur.execute("SELECT * from onesided where likedby = ?",(liker,))
	users = cur.fetchall()
	con.close()	
	return users
