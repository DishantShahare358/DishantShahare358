import base64
import os
import re

png_path = r'D:\Github\github04\dishant-hero-nobg.png'
with open(png_path, 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

data_uri = f'data:image/png;base64,{b64_data}'

# ==========================================
# 1. UPDATE DISHANT-BANNER-LIGHT.SVG
# ==========================================
light_path = r'D:\Github\github04\dishant-banner-light.svg'
with open(light_path, 'r', encoding='utf-8') as f:
    light_content = f.read()

# Make sure Google Font Outfit & Poppins are imported
font_import = "@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Poppins:wght@600;700;800&display=swap');\n"
if "@import url('https://fonts.googleapis.com/css2?family=Outfit" not in light_content:
    light_content = light_content.replace("<style type=\"text/css\"><![CDATA[\n", "<style type=\"text/css\"><![CDATA[\n" + font_import)

# Embed base64 image
light_content = light_content.replace('./dishant-hero-nobg.png', data_uri)
light_content = light_content.replace('dishant-hero-nobg.png', data_uri)

# Stylish font update for Name "Dishant Shahare"
# If text tag or path is used for name, ensure font-family is 'Outfit', 'Poppins', sans-serif with gradient fill and letter-spacing
if '<g transform="translate(48,196)"' in light_content:
    # Replace path-based or plain text name with stylish text element
    old_name_g_pattern = r'<g transform=\"translate\(48,196\)\"[^>]*>.*?</g>'
    new_name_g = '<text x="48" y="190" font-family="\'Outfit\', \'Poppins\', sans-serif" font-size="52" font-weight="900" letter-spacing="1.5" fill="url(#nameg)" filter="url(#glow)">Dishant Shahare</text>'
    light_content = re.sub(old_name_g_pattern, new_name_g, light_content, flags=re.DOTALL)
elif 'Dishant Shahare</text>' not in light_content:
    # Ensure text is present with stylish font
    light_content = re.sub(r'aria-label=\"Dishant Shahare\"', r'aria-label="Dishant Shahare"', light_content)

with open(light_path, 'w', encoding='utf-8') as f:
    f.write(light_content)
print("Updated dishant-banner-light.svg successfully!")


# ==========================================
# 2. UPDATE DISHANT-BANNER.SVG
# ==========================================
dark_path = r'D:\Github\github04\dishant-banner.svg'
with open(dark_path, 'r', encoding='utf-8') as f:
    dark_content = f.read()

if "@import url('https://fonts.googleapis.com/css2?family=Outfit" not in dark_content:
    dark_content = dark_content.replace("<style type=\"text/css\"><![CDATA[\n", "<style type=\"text/css\"><![CDATA[\n" + font_import)

# Embed base64 image
start_idx = dark_content.find('<image')
if start_idx != -1:
    href_start = dark_content.find('href="', start_idx) + 6
    href_end = dark_content.find('"', href_start)
    dark_content = dark_content[:href_start] + data_uri + dark_content[href_end:]

# Stylish font for Name "Dishant Shahare"
if '<g transform="translate(48,196)"' in dark_content:
    old_name_g_pattern = r'<g transform=\"translate\(48,196\)\"[^>]*>.*?</g>'
    new_name_g = '<text x="48" y="190" font-family="\'Outfit\', \'Poppins\', sans-serif" font-size="52" font-weight="900" letter-spacing="1.5" fill="url(#nameg)" filter="url(#glow)">Dishant Shahare</text>'
    dark_content = re.sub(old_name_g_pattern, new_name_g, dark_content, flags=re.DOTALL)

with open(dark_path, 'w', encoding='utf-8') as f:
    f.write(dark_content)
print("Updated dishant-banner.svg successfully!")


# ==========================================
# 3. UPDATE DISHANT-LANYARD.SVG
# ==========================================
lanyard_path = r'D:\Github\github04\dishant-lanyard.svg'
with open(lanyard_path, 'r', encoding='utf-8') as f:
    lanyard_content = f.read()

if "@import url('https://fonts.googleapis.com/css2?family=Outfit" not in lanyard_content:
    lanyard_content = lanyard_content.replace("<style type=\"text/css\"><![CDATA[\n", "<style type=\"text/css\"><![CDATA[\n" + font_import)

lanyard_content = lanyard_content.replace('./dishant-hero-nobg.png', data_uri)
lanyard_content = lanyard_content.replace('dishant-hero-nobg.png', data_uri)
lanyard_content = lanyard_content.replace('@dishantshahare', '@DishantShahare358')

# Perfect face focus: adjust x, y, width, height for avatar circle (cx=210, cy=412, r=57)
# Setting x="135" y="348" width="150" height="225" and preserveAspectRatio="xMidYMin slice" zooms in perfectly on face!
old_image_pattern = r'<image[^>]+clip-path=\"url\(#avatarClip\)\"[^>]*>'
new_image_tag = f'<image x="135" y="348" width="150" height="225" clip-path="url(#avatarClip)" href="{data_uri}" preserveAspectRatio="xMidYMin slice"/>'
lanyard_content = re.sub(old_image_pattern, new_image_tag, lanyard_content)

# Update lanyard name font
lanyard_content = re.sub(
    r'<text x=\"210\" y=\"496\" text-anchor=\"middle\" font-size=\"18\" font-weight=\"bold\" fill=\"url\(#nameg2\)\" filter=\"url\(#glow2\)\">Dishant Shahare</text>',
    r'<text x="210" y="496" text-anchor="middle" font-family="\'Outfit\', \'Poppins\', sans-serif" font-size="20" font-weight="800" letter-spacing="0.5" fill="url(#nameg2)" filter="url(#glow2)">Dishant Shahare</text>',
    lanyard_content
)

with open(lanyard_path, 'w', encoding='utf-8') as f:
    f.write(lanyard_content)
print("Updated dishant-lanyard.svg successfully!")
