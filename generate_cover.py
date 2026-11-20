import os
from PIL import Image, ImageDraw, ImageFont

def generate_cover():
    width = 1200
    height = 800
    img = Image.new('RGB', (width, height), color=(11, 15, 23)) # Dark slate bg
    draw = ImageDraw.Draw(img)

    # Gradient header bar
    for x in range(width):
        r = int(99 + (168 - 99) * (x / width))
        g = int(102 + (85 - 102) * (x / width))
        b = int(241 + (247 - 241) * (x / width))
        draw.line([(x, 0), (x, 10)], fill=(r, g, b))

    # Grid effect or tech lines
    for y in range(80, height, 80):
        draw.line([(0, y), (width, y)], fill=(20, 26, 38), width=1)
    for x in range(80, width, 80):
        draw.line([(x, 0), (x, height)], fill=(20, 26, 38), width=1)

    # Accent badge
    draw.rounded_rectangle([(80, 80), (380, 130)], radius=12, fill=(30, 41, 59), outline=(99, 102, 241), width=2)
    draw.text((105, 93), "TURNKEY DEVELOPER KIT", fill=(165, 180, 252), font_size=20)

    # Main Title
    draw.text((80, 170), "1-Click Home Assistant", fill=(255, 255, 255), font_size=62)
    draw.text((80, 250), "& Telegram Alert Stack", fill=(99, 102, 241), font_size=62)

    # Subtitle
    subtitle = "Turnkey Docker configs, system health sensors & instant crash alerts in under 3 minutes."
    draw.text((80, 345), subtitle, fill=(148, 163, 184), font_size=26)

    # 3 Feature Pills
    features = [
        ("🐳 Pre-Configured Docker Compose", (25, 33, 50), (99, 102, 241)),
        ("⚡ 4 Production Alert Automations", (25, 33, 50), (16, 185, 129)),
        ("🛡️ Conflict-Free Broadcast Mode", (25, 33, 50), (245, 158, 11))
    ]
    
    y_pos = 430
    for title, bg_col, border_col in features:
        draw.rounded_rectangle([(80, y_pos), (720, y_pos + 60)], radius=10, fill=bg_col, outline=border_col, width=2)
        draw.text((110, y_pos + 16), title, fill=(241, 245, 249), font_size=22)
        y_pos += 80

    # Bottom Branding Bar
    draw.rounded_rectangle([(80, 690), (1120, 750)], radius=12, fill=(17, 24, 39), outline=(51, 65, 85), width=1)
    draw.text((110, 708), "By DimusTech  •  Ko-fi Shop Verified  •  No 409 Polling Conflicts", fill=(148, 163, 184), font_size=20)
    draw.text((950, 708), "⚡ Instant Setup", fill=(52, 211, 153), font_size=20)

    out_path = r"C:\Users\DimiBoy\Projects\turnkey-homeassistant-telegram-stack\cover.png"
    img.save(out_path, format="PNG")
    print(f"Saved cover image to {out_path}")

if __name__ == "__main__":
    generate_cover()
