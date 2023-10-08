import praw

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT'
)

# List of finance-related subreddits
subreddits = ['stocks', 'investing', 'wallstreetbets']

for subreddit_name in subreddits:
    print(f"Fetching top posts from r/{subreddit_name}...\n")
    subreddit = reddit.subreddit(subreddit_name)

    # Fetch top hot posts
    hot_posts = subreddit.hot(limit=5)
    print(f"Top Hot Posts in r/{subreddit_name}:\n")
    for post in hot_posts:
        print(f"Title: {post.title}")
        print(f"Score: {post.score}")
        print(f"URL: {post.url}\n")

    # Fetch top rising posts
    rising_posts = subreddit.rising(limit=5)
    print(f"\nTop Rising Posts in r/{subreddit_name}:\n")
    for post in rising_posts:
        print(f"Title: {post.title}")
        print(f"Score: {post.score}")
        print(f"URL: {post.url}\n")
