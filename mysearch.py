import webbrowser

def search_engine():
    print("Welcome to Eric's Search Engine (type 'exit' to quit)")
    
    while True:
        query = input("\nSearch > ")
        
        if query.lower() == 'exit':
            print("Goodbye!")
            break

        print("Choose a search engine:")
        print("1. Google")
        print("2. Bing")
        print("3. DuckDuckGo")

        engine = input("Enter number (1-3): ")

        if engine == '1':
            url = f"https://www.google.com/search?q={query}"
        elif engine == '2':
            url = f"https://www.bing.com/search?q={query}"
        elif engine == '3':
            url = f"https://duckduckgo.com/?q={query}"
        else:
            print("Invalid input. Using Google by default.")
            url = f"https://www.google.com/search?q={query}"

        print(f"Searching for: {query}")
        webbrowser.open(url)

if __name__ == "__main__":
    search_engine()