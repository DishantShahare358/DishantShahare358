import base64
import re

png_path = r'D:\Github\github04\dishant-hero-nobg.png'
with open(png_path, 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

data_uri = f'data:image/png;base64,{b64_data}'

lanyard_path = r'D:\Github\github04\dishant-lanyard.svg'
with open(lanyard_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure base64 image data URI is present
content = content.replace('./dishant-hero-nobg.png', data_uri)
content = content.replace('dishant-hero-nobg.png', data_uri)

# Update avatar <image> tag with face-only zoom:
# Position: x=13, y=307, width=340, height=511 (centers character's head & face in cx=210, cy=412 avatar circle)
pattern = r'<image[^>]+clip-path=\"url\(#avatarClip\)\"[^>]*>'
new_image_tag = f'<image x="13" y="307" width="340" height="511" clip-path="url(#avatarClip)" href="{data_uri}" preserveAspectRatio="none"/>'

content = re.sub(pattern, new_image_tag, content)

# Ensure username @DishantShahare358 is present
content = content.replace('@dishantshahare', '@DishantShahare358')

with open(lanyard_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully updated dishant-lanyard.svg with enlarged face focus!')
