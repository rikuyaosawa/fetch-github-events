import argparse
from commands.fetch import fetch_user_events


def main():
    parser = argparse.ArgumentParser(description="GitHub Info Fetching CLI App")
    parser.add_argument("username", help="GitHub username")
    parser.add_argument(
        "--limit", type=int, default=10, help="Number of activities to fetch"
    )
    args = parser.parse_args()
    fetch_user_events(args.username, args.limit)


if __name__ == "__main__":
    main()
