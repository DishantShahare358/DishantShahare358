import base64
import os

png_path = r'D:\Github\github04\dishant-hero-nobg.png'
with open(png_path, 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

data_uri = f'data:image/png;base64,{b64_data}'

# 1. dishant-banner-light.svg
banner_light_path = r'D:\Github\github04\dishant-banner-light.svg'
with open(banner_light_path, 'r', encoding='utf-8') as f:
    txt = f.read()

txt = txt.replace('./dishant-hero-nobg.png', data_uri)
txt = txt.replace('dishant-hero-nobg.png', data_uri)

with open(banner_light_path, 'w', encoding='utf-8') as f:
    f.write(txt)
print('Updated dishant-banner-light.svg successfully!')

# 2. dishant-banner.svg
banner_dark_path = r'D:\Github\github04\dishant-banner.svg'
with open(banner_dark_path, 'r', encoding='utf-8') as f:
    txt = f.read()

start_idx = txt.find('<image')
if start_idx != -1:
    href_start = txt.find('href="', start_idx) + 6
    href_end = txt.find('"', href_start)
    txt = txt[:href_start] + data_uri + txt[href_end:]

with open(banner_dark_path, 'w', encoding='utf-8') as f:
    f.write(txt)
print('Updated dishant-banner.svg successfully!')

# 3. dishant-lanyard.svg
lanyard_path = r'D:\Github\github04\dishant-lanyard.svg'
with open(lanyard_path, 'r', encoding='utf-8') as f:
    txt = f.read()

txt = txt.replace('./dishant-hero-nobg.png', data_uri)
txt = txt.replace('dishant-hero-nobg.png', data_uri)
txt = txt.replace('@dishantshahare', '@DishantShahare358')

# Focus on face for avatar clip
txt = txt.replace('x="130" y="325" width="160" height="140" clip-path="url(#avatarClip)" href="' + data_uri + '" preserveAspectRatio="xMidYTop slice"',
                  'x="130" y="350" width="160" height="220" clip-path="url(#avatarClip)" href="' + data_uri + '" preserveAspectRatio="xMidYMin slice"')

with open(lanyard_path, 'w', encoding='utf-8') as f:
    f.write(txt)
print('Updated dishant-lanyard.svg successfully!')
