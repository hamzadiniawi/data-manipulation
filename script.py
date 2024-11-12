from bs4 import BeautifulSoup

# Input and output file paths
input_file_path = 'htmlList.txt'
output_file_path = 'extracted_data.txt'

# Open the output file for writing
with open(output_file_path, 'w') as output_file:
    # Open the input file and read each line
    with open(input_file_path, 'r') as file:
        for line in file:
            # Parse each line with BeautifulSoup
            soup = BeautifulSoup(line, 'html.parser')
            people_info = []
            
            # Find each person block by identifying div containers that match the person's structure
            for card in soup.find_all('div', class_='card_entrepreneur'):
                # Extract Name
                name_tag = card.find('h5', class_='title_card_entrepreneur')
                name = name_tag.get_text(strip=True) if name_tag else 'N/A'
                
                # Extract Post
                post_tag = card.find('div', class_='mt_2').find('span')
                post = post_tag.get_text(strip=True) if post_tag else 'N/A'
                
                # Extract Social Media Links
                social_links = card.find('div', class_='social_media').find_all('a')
                linkedin = facebook = email = 'N/A'
                
                for link in social_links:
                    href = link.get('href')
                    if 'linkedin.com' in href:
                        linkedin = href.strip()
                    elif 'facebook.com' in href:
                        facebook = href.strip()
                    elif 'mailto:' in href:
                        email = href.strip()
                
                # Format each person's information
                person_info = f"Name: {name} | Post: {post} | LinkedIn: {linkedin} | Facebook: {facebook} | Email: {email}"
                people_info.append(person_info)
            
            # Join all persons' information with ##### for each line
            output_line = " ##### ".join(people_info)
            output_file.write(output_line + '\n')

print("Extraction complete. Check extracted_data.txt for results.")
