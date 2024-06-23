import click
import requests
import random

# List of quote APIs (you can add more)
QUOTE_APIS = [
    "https://api.quotable.io/random",
    "https://zenquotes.io/api/random",
    "https://favqs.com/api/qotd",
]


def get_random_quote():
    # Choose a random API
    api_url = random.choice(QUOTE_APIS)

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()

        # Extract quote and author based on API structure
        if "content" in data:  # Quotable API
            quote = data["content"]
            author = data["author"]
        elif "quote" in data and "body" in data["quote"]:  # FavQs API
            quote = data["quote"]["body"]
            author = data["quote"]["author"]
        elif isinstance(data, list) and data:  # ZenQuotes API
            quote = data[0]["q"]
            author = data[0]["a"]
        else:
            return "Unable to parse quote from the API.", ""

        return quote, author
    except requests.RequestException as e:
        return f"An error occurred: {str(e)}", ""


@click.command()
def random_quote():
    """Print a random quote."""
    quote, author = get_random_quote()
    click.echo(click.style(quote, fg="green", bold=True))
    if author:
        click.echo(click.style(f" - {author}"))


def main():
    random_quote()


if __name__ == "__main__":
    main()
