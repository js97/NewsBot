import praw
import time
import sched


def getSubmissions():

	reddit_instance = praw.Reddit('bot1')

	subs = []
	subs.append(reddit_instance.subreddit('news/top/?sort=top&t=week'))
	subs.append(reddit_instance.subreddit('economics/top/?sort=top&t=week'))
	subs.append(reddit_instance.subreddit('chomsky/top/?sort=top&t=week'))
	subs.append(reddit_instance.subreddit('economics/top/?sort=top&t=week'))
	subs.append(reddit_instance.subreddit('programming/top/?sort=top&t=week'))

	size = len(subs)

	for x in range(0,size):
		sub = subs.pop()
		for submission in sub.hot(limit=5):
			print('bot adding :', submission.title)
			
def main():
	
	DayOfWeek = datetime.datetime.today().weekday()
	
	# Is Sun. night or Mon. morning; we post for monday
	if DayOfWeek == 6
		getSubmissions()
	
if __name__ == '__main__':
	main()