import requests
from bs4 import BeautifulSoup
import os

def scrape_website(url):
    """
    Scrapes a website and saves the content to an HTML file.

    Args:
        url (str): The URL of the website to scrape.
    """
    try:
        # Fetch the website content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the main content (adapt this to your target website)
        #  This is a placeholder.  You'll need to inspect the website
        #  you're scraping to find the correct HTML elements.
        main_content = soup.find('div', {'class': 'main-content'})  # Example

        if main_content:
            # Create a simple HTML page
            html_output = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Scraped Content</title>
                <link rel="stylesheet" href="style.css">
            </head>
            <body>
                <div class="container">
                    {str(main_content)}
                </div>
            </body>
            </html>
            """

            # Save the HTML to a file
            output_dir = "output"  # Directory for output files
            os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
            output_file = os.path.join(output_dir, "index.html")  # Consistent filename
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(html_output)

            print(f"Scraped content saved to {output_file}")
        else:
            print("Main content not found on the page.")
            return  # Exit if main content not found

    except requests.exceptions.RequestException as e:
        print(f"Error fetching or processing {url}: {e}")
        return  # Exit if there's an error fetching the page
    except Exception as e:
        print(f"An error occurred: {e}")
        return # Exit on other exceptions



def create_stylesheet(output_dir):
    """Creates a simple CSS stylesheet.

    Args:
        output_dir (str): The directory to save the CSS file in.
    """
    css_content = """
    .container {
        max-width: 800px;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-family: sans-serif;
        line-height: 1.6;
    }
    /* Add more styles as needed */
    """
    css_file = os.path.join(output_dir, "style.css")
    with open(css_file, "w", encoding="utf-8") as f:
        f.write(css_content)
    print(f"Created stylesheet: {css_file}")


# Example usage:
target_url = "https://en.wikipedia.org/wiki/Dieterich_Buxtehude"  # Replace with the URL you want to scrape
output_directory = "output" # set the output
os.makedirs(output_directory, exist_ok=True) # Ensure the output directory exists
scrape_website(target_url)
create_stylesheet(output_directory) # create the stylesheet
print("Scraping complete.")
