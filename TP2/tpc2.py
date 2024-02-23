import re

def header_to_html(match):
    level = len(match.group(1))
    text = match.group(2)
    return f"<h{level}>{text}</h{level}>"

def bold_to_html(match):
    text = match.group(1)
    return f"<b>{text}</b>"

def italic_to_html(match):
    text = match.group(1)
    return f"<i>{text}</i>"

def blockquote_to_html(match):
    text = match.group(1)
    return f"<blockquote>{text}</blockquote>"

def ordered_list_to_html(match):
    items = match.group(1).strip().split('\n')
    html_list = "<ol>\n"
    for item in items:
        html_list += f"<li>{item.strip()}</li>\n"
    html_list += "</ol>"
    return html_list

def unordered_list_to_html(match):
    items = match.group(1).strip().split('\n')
    html_list = "<ul>\n"
    for item in items:
        html_list += f"<li>{item.strip()}</li>\n"
    html_list += "</ul>"
    return html_list

def link_to_html(match):
    title = match.group(1)
    url = match.group(2)
    return f'<a href="{url}">{title}</a>'

def image_to_html(match):
    alt_text = match.group(1)
    img_url = match.group(2)
    return f'<img src="{img_url}" alt="{alt_text}"/>'

def markdown_to_html(file_path):
    with open(file_path, 'r') as file:
        markdown_text = file.read()

    # Headers
    markdown_text = re.sub(r'^(#{1,6})\s+(.+)$', header_to_html, markdown_text, flags=re.MULTILINE)
    # Bold
    markdown_text = re.sub(r'\*\*(.*?)\*\*', bold_to_html, markdown_text)
    # Italic
    markdown_text = re.sub(r'\*(.*?)\*', italic_to_html, markdown_text)
    # Blockquote
    markdown_text = re.sub(r'^>\s+(.+)$', blockquote_to_html, markdown_text, flags=re.MULTILINE)
    # Ordered List
    markdown_text = re.sub(r'^\d+\.\s+(.+)$', ordered_list_to_html, markdown_text, flags=re.MULTILINE)
    # Unordered List
    markdown_text = re.sub(r'^-\s+(.+)$', unordered_list_to_html, markdown_text, flags=re.MULTILINE)
    # Link
    markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', link_to_html, markdown_text)
    # Image
    markdown_text = re.sub(r'!\[(.*?)\]\((.*?)\)', image_to_html, markdown_text)

    return markdown_text

html_output = markdown_to_html('input.md')
print(html_output)
with open('output.html', 'w') as file:
    file.write(html_output)