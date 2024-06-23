# Whut

Whut is a versatile command-line tool that leverages Google Generative AI to search the internet and provide decluttered answers directly in your terminal. With Whut, you can configure your own API key, customize search prompts, and specify response lengths.

## Features

- **Configuration Mode**: Set your own API key for personalized usage.
- **Default Mode**: Get decluttered answers using a standard prompt.
- **Custom Mode**: Pass queries directly to the API without modification.
- **Limited Length Mode**: Specify the number of lines for the answer.

## Installation

You can install Whut from PyPI:

```pip install whut```

> Info here: https://pypi.org/project/whut/


## Usage
### Basic Search
To perform a basic search, simply type:

```whut "your search query"```   

 example:
            
    whut "Mahatma Gandhi"


### Configuration Mode

To set your own API key, use the -set flag:    

    whut -set


### Custom Mode

To pass the query directly to the API, use the -c flag:   


```whut -c "your search query"```    

Example: 

    whut -c "Sam Altman"

### Limited Length Mode

To get an answer with a specific number of lines, use the -c flag along with the -l flag:

```whut -c -l <number> "your search query"```    
Example: 

    whut -c -l 5 "Sam Altman"

### Custom Prompt
You can customize the search prompt by using the `-C` or `-c` option followed by a colon (`:`) and then your query:


```whut -C "Please provide detailed information about: Your search query"```   

Example:
    
    whut -C "Tell me in detail about: Sam Altman"




