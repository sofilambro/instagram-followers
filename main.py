from bs4 import BeautifulSoup

def extract_usernames_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        return [a.text.strip() for a in soup.find_all('a')]

def main():
    following = extract_usernames_from_html('data/following.html')
    followers = extract_usernames_from_html('data/followers.html')

    not_following_back = [user for user in following if user not in followers]

    print("🔍 Users you follow who don't follow you back:")
    for user in not_following_back:
        print(user)

if __name__ == "__main__":
    main()
