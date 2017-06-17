import praw
import time
import sched
import datetime
import smtplib
from email.mime.text import MIMEText
import DBA as db


def get_submissions():

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

def create_file(sub_list):
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


def send_email(sub_list, to_this_email):
	
	create_file(sub_list)
	with open('file.txt') as f:
		msg = MIMEText(f.read())

	email = 'joshua.steubs@gmail.com'
	password = ''

	msg['Subject'] = 'Reddit Weekly Update'
	msg['From'] = email
	msg['To'] = to_this_email
	msg_ = msg.as_string()

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	
	server.login(email,password)
	server.set_debuglevel(1)
	server.sendmail(email,email, msg_)
	server.quit()	

def main():
	
	DayOfWeek = datetime.datetime.today().weekday()
	HourOfDay = datetime.datetime.today().hour
	MinOfHour = datetime.datetime.today().minute
	
	print('Waiting...\n')
	email_list = db.get_emails()

	print (email_list)
	for email in email_list:
		send_email(get_submissions(), email)
	
if __name__ == '__main__':
	while 1:
		time.sleep(58)
		if DayOfWeek == 6 and HourOfDay == 8 and MinOfHour == 1:
			main()
			time.sleep(100)

	
