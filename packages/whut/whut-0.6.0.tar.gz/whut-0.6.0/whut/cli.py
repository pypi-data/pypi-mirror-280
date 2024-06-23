import argparse
import google.generativeai as genai
import os

def configure_api_key():
    api_key = input("Enter your Google Generative AI API key: ").strip()
    if api_key:
        with open('config.txt', 'w') as config_file:
            config_file.write(api_key)
        print("API key saved.")
    else:
        print("Using default API key.")

def load_api_key():
    if os.path.exists('config.txt'):
        with open('config.txt', 'r') as config_file:
            return config_file.read().strip()
    return 'AIzaSyDzjP-c_fUAjiKybq81Rd-leQSejOaqO7I'

def search(query, prompt_template):
    api_key = load_api_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    prompt = prompt_template.format(query=query)
    response = model.generate_content(prompt)
    return response.text

def main():
    parser = argparse.ArgumentParser(description='Search the internet from the terminal using Google Generative AI')
    parser.add_argument('query', nargs='+', help='Search query')
    parser.add_argument('-C', '--custom', action='store_true', help='Run in custom prompt mode, passing the custom prompt and query')
    parser.add_argument('-c', action='store_true', help='Run in custom prompt mode, passing the custom prompt and query')
    parser.add_argument('-l', type=int, help='Number of lines to get the answer in')
    parser.add_argument('-set', action='store_true', help='Configure your own API key')
    
    args = parser.parse_args()
    
    if args.set:
        configure_api_key()
        return
    
    query = ' '.join(args.query)
    
    if args.custom or args.c:
        if args.l:
            prompt_template = f"Need the answer in like {args.l} lines for this prompt: {query}"
        else:
            prompt_template = query.split(':', 1)[0]
            query = query.split(':', 1)[1]
    else:
        prompt_template = "Give decluttered answer possible. What's: {query}"
    
    result = search(query, prompt_template)
    print(result)

if __name__ == '__main__':
    main()
