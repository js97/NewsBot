import praw
import time
import sched
import datetime
import smtplib
from email.mime.text import MIMEText

def getSubmissions():

	reddit_instance = praw.Reddit('bot1')

	subs = []
	subs.append(reddit_instance.subreddit('cpp'))
	subs.append('cpp')
	subs.append(reddit_instance.subreddit('economics'))
	subs.append('economics')
	subs.append(reddit_instance.subreddit('chomsky'))
	subs.append('chomsky')
	subs.append(reddit_instance.subreddit('programming'))
	subs.append('programming')
	subs.append(reddit_instance.subreddit('python'))
	subs.append('python')
	subs.append(reddit_instance.subreddit('machinelearning'))
	subs.append('machinelearning')
	subs.append(reddit_instance.subreddit('news'))
	subs.append('news')
	return subs

def createFile(sub_list):
	with open('file.txt','w') as f:
		while len(sub_list) is not 0:
			f.write('/r/')
			f.write(sub_list.pop())
			f.write('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
			f.write('\n')
			for submission in sub_list.pop().top('week',limit=3):
				f.write(submission.title)
				f.write('\n')
				f.write(submission.url)
				f.write('\n')

			f.write('\n')


def sendEmail(sub_list):
	
	createFile(sub_list)
	with open('file.txt') as f:
		msg = MIMEText(f.read())

	email = ''
	password = ''

	msg['Subject'] = 'Reddit Weekly Update'
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
	if DayOfWeek == 6:
		sendEmail(getSubmissions())
	
if __name__ == '__main__':
	while 1:
		main()
