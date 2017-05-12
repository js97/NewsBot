import praw
import time
import sched
import datetime

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

	size = len(subs)
	count = 0
	for x in range(0,size):
		sub = subs.pop()
		for submission in sub.top('week',limit=2):
			print('\nADD: ', submission.title)
			
def main():
	
	DayOfWeek = datetime.datetime.today().weekday()
	print('Waiting...\n')
	time.sleep(1)
	#if DayOfWeek == 6: #comment out for now, uncomment when working build is ready
	getSubmissions()
	
if __name__ == '__main__':
	while 1:
		main()
