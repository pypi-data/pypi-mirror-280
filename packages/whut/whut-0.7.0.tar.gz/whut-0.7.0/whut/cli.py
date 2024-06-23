from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress
import argparse
import time
import os

import google.generativeai as genai  # Assuming this is a correct import for your setup

console = Console()

def configure_api_key():
    api_key = console.input("[bold yellow]Enter your Google Generative AI API key: [/bold yellow]").strip()
    if api_key:
        with open('config.txt', 'w') as config_file:
            config_file.write(api_key)
        console.print("[bold green]API key saved successfully.[/bold green]")
    else:
        console.print("[bold yellow]Using default API key.[/bold yellow]")

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
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Searching...", total=100)
        while not progress.finished:
            progress.update(task, advance=0.5)
            time.sleep(0.02)
        response = model.generate_content(prompt)
    
    return response.text.strip()

def main():
    parser = argparse.ArgumentParser(description='Search the internet from the terminal using Google Generative AI')
    parser.add_argument('query', nargs='*', help='Search query')
    parser.add_argument('-C', '--custom', action='store_true', help='Run in custom prompt mode, passing the custom prompt and query')
    parser.add_argument('-c', action='store_true', help='Run in custom prompt mode, passing the custom prompt and query')
    parser.add_argument('-l', type=int, help='Number of lines to get the answer in')
    parser.add_argument('-set', action='store_true', help='Configure your own API key')
    
    args = parser.parse_args()
    
    if args.set:
        configure_api_key()
        return
    
    if not args.query:
        parser.error("the following arguments are required: query")
    
    query = ' '.join(args.query)
    
    if args.custom or args.c:
        if args.l:
            prompt_template = f"Need the answer in like {args.l} lines for this prompt: {query}"
        else:
            prompt_template = query.split(':', 1)[0]
            query = query.split(':', 1)[1]
    else:
        prompt_template = "Give decluttered answer for the query: {query}"
    
    result = search(query, prompt_template)
    
    # Calculate the height of the panel dynamically based on the number of lines in the result
    result_lines = len(result.splitlines())
    panel_height = min(result_lines + 7, 17)  # Adjusting for title, subtitle, and preventing excessive blank space

    # Main content panel
    main_content = Panel(
        Text(result, style="green"),
        title=f"[bold magenta]Search Result 🔍[/bold magenta]",
        subtitle=f"[bold cyan]Query: {query} 💡[/bold cyan]",
        border_style="bold yellow",
        padding=(1, 1),
        height=panel_height,
        expand=True
    )

    # Display the main content panel
    console.print(main_content)

if __name__ == '__main__':
    main()
