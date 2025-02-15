import markdown

# Function to convert markdown text to HTML
def convert_markdown_to_html(input_file, output_file):
    # Open the markdown file to read
    with open(input_file, 'r') as md_file:
        md_text = md_file.read()

    # Convert markdown to HTML
    html = markdown.markdown(md_text)

    # Write the HTML output to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html)

# Example usage
input_file = 'input.md'  # Path to the input markdown file
output_file = 'output.html'  # Path to the output HTML file
convert_markdown_to_html(input_file, output_file)
