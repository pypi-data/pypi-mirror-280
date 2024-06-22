import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import argparse

def main():
    parser = argparse.ArgumentParser(description='Get top contributors from a subreddit')
    parser.add_argument('subreddit', type=str, help='The name of the subreddit')
    args = parser.parse_args()

    subreddit_name = args.subreddit
    base_url = f"https://old.reddit.com/r/{subreddit_name}/hot/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    user_contributions = defaultdict(int)

    def get_posts(url):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find_all('div', class_='thing', attrs={'data-author': True, 'data-score': True}), soup

    def get_comments(post_id):
        url = f"https://old.reddit.com/comments/{post_id}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find_all('div', class_='entry', attrs={'data-author': True, 'data-score': True})

    def scrape_reddit(url, limit=100):
        posts_scraped = 0
        while posts_scraped < limit:
            posts, soup = get_posts(url)
            for post in posts:
                author = post['data-author']
                score = int(post['data-score'])
                if author:
                    user_contributions[author] += score

                post_id = post['data-fullname'].split('_')[-1]
                comments = get_comments(post_id)
                for comment in comments:
                    comment_author = comment['data-author']
                    comment_score = int(comment['data-score'])
                    if comment_author:
                        user_contributions[comment_author] += comment_score

                posts_scraped += 1
                if posts_scraped >= limit:
                    break

            next_button = soup.find('span', class_='next-button')
            if next_button:
                url = next_button.find('a')['href']
            else:
                break

    scrape_reddit(base_url)
    sorted_contributions = sorted(user_contributions.items(), key=lambda x: x[1], reverse=True)

    print("Top Contributors:")
    for i, (user, upvotes) in enumerate(sorted_contributions, start=1):
        print(f"{i}. {user}: {upvotes} upvotes")

if __name__ == "__main__":
    main()
