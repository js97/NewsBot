import praw
import time
import sched
import datetime
import smtplib
from email.mime.text import MIMEText


def getSubmissions():

	reddit_instance = praw.Reddit('bot1')

	subs = []
	subs.append(reddit_instance.subreddit('news'))
	subs.append(reddit_instance.subreddit('economics'))
	subs.append(reddit_instance.subreddit('chomsky'))
	subs.append(reddit_instance.subreddit('programming'))
	subs.append(reddit_instance.subreddit('rust'))
	subs.append(reddit_instance.subreddit('python'))
	subs.append(reddit_instance.subreddit('machinelearning'))
	subs.append(reddit_instance.subreddit('cpp'))

	#size = len(subs)
	#count = 0
	#for x in range(0,size):
	#	sub = subs.pop()
	#	for submission in sub.top('week',limit=2):
	#		print('\nADD: ', submission.title)
	return subs
	
def prompt(prompt):
    return input(prompt).strip()

def createFile:


def sendEmail(sub_list):
	
	createFile()
	with open('file.txt') as fp:
		msg = MIMEText(fp.read())

	email = ''
	password = ''

	msg['Subject'] = 'The contents'
	msg['From'] = 'email'
	msg['To'] = 'email'
	msg_ = msg.as_string()

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	
	server.login(email,password)
	server.set_debuglevel(1)
	server.sendmail(email,email, msg_)
	server.quit()	

def main():
	
	DayOfWeek = datetime.datetime.today().weekday()
	print('Waiting...\n')
	#time.sleep(1)
	#if DayOfWeek == 6:
	sendEmail(getSubmissions())
	
if __name__ == '__main__':
	#while 1:
	main()
