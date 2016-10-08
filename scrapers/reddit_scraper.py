import praw, itertools, csv

SUBREDDIT = 'Jokes'
NUM_SCRAPED = 1000
FNAME = 'jokes.csv'

if __name__ == '__main__':
    r = praw.Reddit(user_agent='my_scraper')
    r_jokes = r.get_subreddit(SUBREDDIT)

    # Top jokes
    top_jokes = r_jokes.get_top_from_all(limit=NUM_SCRAPED)
    with open(FNAME, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['submission_id', 'title', 'selftext', 'score'])
        while True:
            top_100 = itertools.islice(top_jokes, 100)
            if not top_100: break
            row = [[x.id, x.title, x.selftext, x.score] for x in top_100]
            writer.writerows(row)



    # # Controversial jokes
    # r_jokes.get_controversial_from_all(limit=NUM_SCRAPED)

