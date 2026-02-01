import requests
import csv
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

GITHUB_TOKEN = "PASTE YOUR GITHUB PUBLIC ACCESS TOKEN HERE"

def create_session():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[403, 429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session

def find_github_developers():
    topics = [
        'react', 'angular', 'react-native',
        'python', 'docker', 'kubernetes', 'typescript'
    ]

    developers = []
    session = create_session()

    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {GITHUB_TOKEN}'
    }

    for topic in topics:
        print(f"🔍 Searching for {topic} developers...")

        url = (
            "https://api.github.com/search/users"
            f"?q=type:user+language:{topic}+followers:>50&per_page=5"
        )

        try:
            response = session.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Skipping {topic}: {e}")
            continue

        users = response.json().get('items', [])

        for user in users:
            try:
                user_response = session.get(
                    user['url'],
                    headers=headers,
                    timeout=10
                )
                user_response.raise_for_status()
                user_data = user_response.json()

                developer = {
                    'username': user_data['login'],
                    'name': user_data.get('name', ''),
                    'email': user_data.get('email', ''),
                    'topic': topic,
                    'followers': user_data.get('followers', 0),
                    'public_repos': user_data.get('public_repos', 0)
                }

                developers.append(developer)
                print(f"  ✅ Found: {user_data['login']} ({topic})")

                time.sleep(1)

            except requests.exceptions.RequestException:
                print(f"  ⚠️ Failed to fetch {user['login']}")
                continue

        time.sleep(3)

    return developers

def save_to_csv(developers, filename='developers.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                'username', 'name', 'email',
                'topic', 'followers', 'public_repos'
            ]
        )
        writer.writeheader()
        writer.writerows(developers)

    print(f"\n✅ Saved {len(developers)} developers to {filename}")

if __name__ == "__main__":
    print("🚀 Starting GitHub developer search...")
    devs = find_github_developers()
    save_to_csv(devs)
    print("\n🎉 Done! Upload developers.csv to Smartlead")
