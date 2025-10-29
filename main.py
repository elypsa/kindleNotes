from bs4 import BeautifulSoup
import pyperclip

with open("crisis_cycle.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

sections = soup.find_all('div', class_='sectionHeading')

result = {}

for section in sections:
    heading_text = section.get_text(strip=True)
    notes = []
    # iterate siblings until next sectionHeading or no siblings
    for sibling in section.find_next_siblings():
        if sibling.name == 'div' and 'sectionHeading' in sibling.get('class', []):
            break
        if sibling.name == 'div' and 'noteText' in sibling.get('class', []):
            notes.append(sibling.get_text(strip=True))
    result[heading_text] = notes

to_clipboard = ""
for heading, notes in result.items():
    to_clipboard += f"Section: {heading}\n"
    for i, note in enumerate(notes, 1):
        to_clipboard += f"  Note {i}: {note}\n"
    to_clipboard += "\n"

# Copy the combined text to clipboard
pyperclip.copy(to_clipboard)

print("Extracted text has been copied to clipboard.")