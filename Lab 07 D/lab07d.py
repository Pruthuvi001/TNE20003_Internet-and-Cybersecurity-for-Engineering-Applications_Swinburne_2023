import urllib.request
import os

def download_html(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
        return html_content
    except urllib.error.URLError as e:
        print("Error:", e)
        return None

def extract_images(html_content):
    img_tags = []
    start = 0
    while True:
        start = html_content.find('<img', start)
        if start == -1:
            break
        end = html_content.find('>', start)
        if end == -1:
            break
        img_tags.append(html_content[start:end + 1])
        start = end + 1
    return img_tags

def download_images(img_tags, base_url):
    for img_tag in img_tags:
        src_start = img_tag.find('src="') + 5
        src_end = img_tag.find('"', src_start)
        if src_start != -1 and src_end != -1:
            img_url = img_tag[src_start:src_end]
            img_filename = os.path.basename(urllib.parse.urlparse(img_url).path)
            
            try:
                with urllib.request.urlopen(urllib.parse.urljoin(base_url, img_url)) as response:
                    img_data = response.read()
                    with open(img_filename, 'wb') as img_file:
                        img_file.write(img_data)
                print(f"Downloaded {img_filename}")
            except urllib.error.URLError as e:
                print(f"Error downloading {img_url}: {e}")

if __name__ == "__main__":
    url = "http://example.com"  # Replace with your target URL
    html_content = download_html(url)
    
    if html_content:
        img_tags = extract_images(html_content)
        download_images(img_tags, url)
