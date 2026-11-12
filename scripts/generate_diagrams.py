#!/usr/bin/env python3
"""
Generate crisp, high-resolution vector (SVG) and raster (PNG) keyboard layout diagrams.
Author: Tsengel (tsengel.de)
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "/home/bachka/repos-privat/tsengel-de/language-dev/mn-keyboard-layout/docs/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# Layout Definitions
# Format of key: (top_label, main_label, alt_label, is_devops)

ERGO_ROW1 = [
    ('~', 'ё', '~', False), ('!', '1', '№', False), ('@', '2', '²', False), ('#', '3', '³', False),
    ('$', '4', '₮', True), ('%', '5', '€', False), ('^', '6', '¼', False), ('&', '7', '½', False),
    ('*', '8', '¾', False), ('(', '9', '‘', False), (')', '0', '’', False), ('_', '-', '—', False),
    ('+', '=', '×', False)
]

ERGO_ROW2 = [
    ('Ө', 'ө', 'ъ', True), ('Ү', 'ү', 'ь', True), ('Э', 'э', '€', False), ('Р', 'р', '®', False),
    ('Т', 'т', '₮', True), ('Й', 'й', 'е', False), ('У', 'у', '„', False), ('И', 'и', '“', False),
    ('О', 'о', '”', False), ('П', 'п', ';', False), ('{', '[', '«', True), ('}', ']', '»', True),
    ('|', '\\', '¦', True)
]

ERGO_ROW3 = [
    ('А', 'а', 'μ', False), ('С', 'с', '£', False), ('Д', 'д', '«', True), ('Ф', 'ф', '»', True),
    ('Г', 'г', '{', False), ('Х', 'х', '<', False), ('Ж', 'ж', '>', False), ('К', 'к', '}', False),
    ('Л', 'л', '№', False), (':', ';', 'щ', True), ('Ы', 'ы', "'", False)
]

ERGO_ROW4 = [
    ('З', 'з', '—', False), ('Ш', 'ш', 'щ', False), ('Ц', 'ц', '©', False), ('В', 'в', '–', False),
    ('Б', 'б', '°', False), ('Н', 'н', '·', False), ('М', 'м', '±', False), ('Ч', 'ч', ',', False),
    ('Ю', 'ю', '.', False), ('Я', 'я', '?', False)
]

CLASSIC_ROW2 = [
    ('Ъ', 'ъ', "'", False), ('Ь', 'ь', '`', False), ('Э', 'э', '€', False), ('Р', 'р', '®', False),
    ('Т', 'т', '₮', True), ('Е', 'е', '™', False), ('У', 'у', '„', False), ('И', 'и', '“', False),
    ('О', 'о', '”', False), ('П', 'п', ';', False), ('Ө', 'ө', '[', True), ('Ү', 'ү', ']', True),
    ('|', '\\', '¦', True)
]

BICHIG_ROW2 = [
    ('ᠥ', 'ᠥ', 'FVS1', True), ('ᠦ', 'ᠦ', 'FVS2', True), ('ᠡ', 'ᠡ', 'MVS', True), ('ᠷ', 'ᠷ', '', False),
    ('ᠲ', 'ᠲ', '₮', True), ('ᠶ', 'ᠶ', '', False), ('ᠤ', 'ᠤ', 'FVS3', True), ('ᠢ', 'ᠢ', '', False),
    ('ᠣ', 'ᠣ', '', False), ('ᠫ', 'ᠫ', ';', False), ('{', '[', '᠈', True), ('}', ']', '᠉', True),
    ('|', '\\', '', True)
]

BICHIG_ROW3 = [
    ('ᠠ', 'ᠠ', '', False), ('ᠰ', 'ᠰ', '', False), ('ᠳ', 'ᠳ', '', False), ('ᠹ', 'ᠹ', '', False),
    ('ᠭ', 'ᠭ', '', False), ('ᠬ', 'ᠬ', '', False), ('ᠵ', 'ᠵ', '', False), ('ᠺ', 'ᠺ', '', False),
    ('ᠯ', 'ᠯ', '', False), (':', ';', '', True), ('"', "'", 'MVS', True)
]

BICHIG_ROW4 = [
    ('ᠽ', 'ᠽ', '', False), ('ᠱ', 'ᠱ', '', False), ('ᠴ', 'ᠴ', '', False), ('ᠸ', 'ᠸ', '', False),
    ('ᠪ', 'ᠪ', '', False), ('ᠩ', 'ᠨ', '', False), ('ᠮ', 'ᠮ', '', False), ('<', '᠂', ',', True),
    ('>', '᠃', '.', True), ('?', '/', '', True)
]

def render_layout(title, subtitle, row1, row2, row3, row4, mode='normal', out_filename='keyboard.png'):
    width = 2000
    height = 920
    im = Image.new('RGB', (width, height), color='#0f172a') # Dark slate theme
    draw = ImageDraw.Draw(im)

    font_title = ImageFont.truetype(FONT_BOLD, 36)
    font_sub = ImageFont.truetype(FONT_REG, 20)
    font_main = ImageFont.truetype(FONT_BOLD, 28)
    font_top = ImageFont.truetype(FONT_REG, 17)
    font_alt = ImageFont.truetype(FONT_BOLD, 17)
    font_special = ImageFont.truetype(FONT_BOLD, 19)

    # Title
    draw.text((60, 40), title, fill='#38bdf8', font=font_title)
    draw.text((60, 85), subtitle, fill='#94a3b8', font=font_sub)

    start_x = 60
    start_y = 140
    key_h = 110
    gap = 12
    key_w = 110

    # Row 1
    cur_x = start_x
    for k in row1:
        draw_key(draw, cur_x, start_y, key_w, key_h, k, mode, font_main, font_top, font_alt)
        cur_x += key_w + gap
    # Backspace
    draw_special_key(draw, cur_x, start_y, 180, key_h, "Backspace ⌫", font_special)

    # Row 2
    cur_y = start_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 160, key_h, "Tab ⇥", font_special)
    cur_x = start_x + 160 + gap
    for k in row2:
        draw_key(draw, cur_x, cur_y, key_w, key_h, k, mode, font_main, font_top, font_alt)
        cur_x += key_w + gap

    # Row 3
    cur_y = cur_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 190, key_h, "Caps Lock ⇪", font_special)
    cur_x = start_x + 190 + gap
    for k in row3:
        draw_key(draw, cur_x, cur_y, key_w, key_h, k, mode, font_main, font_top, font_alt)
        cur_x += key_w + gap
    # Enter
    draw_special_key(draw, cur_x, cur_y, 230, key_h, "Enter ↵", font_special, is_accent=True)

    # Row 4
    cur_y = cur_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 240, key_h, "Shift ⇧", font_special, is_shift=(mode == 'shift'))
    cur_x = start_x + 240 + gap
    for k in row4:
        draw_key(draw, cur_x, cur_y, key_w, key_h, k, mode, font_main, font_top, font_alt)
        cur_x += key_w + gap
    draw_special_key(draw, cur_x, cur_y, 300, key_h, "Shift ⇧", font_special, is_shift=(mode == 'shift'))

    # Row 5 (Space Row)
    cur_y = cur_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 140, key_h, "Ctrl", font_special)
    draw_special_key(draw, start_x + 152, cur_y, 130, key_h, "Alt", font_special)
    
    # Spacebar
    space_w = 780
    space_x = start_x + 294
    draw.rounded_rectangle([space_x, cur_y, space_x + space_w, cur_y + key_h], radius=10, fill='#1e293b', outline='#334155', width=2)
    draw.text((space_x + 320, cur_y + 40), "Spacebar", fill='#64748b', font=font_special)

    # AltGr
    altgr_x = space_x + space_w + gap
    draw_special_key(draw, altgr_x, cur_y, 160, key_h, "AltGr", font_special, is_altgr=(mode == 'altgr'))

    # NNBSP key
    nnbsp_x = altgr_x + 160 + gap
    draw_special_key(draw, nnbsp_x, cur_y, 220, key_h, "NNBSP (\\u202F)", font_special, is_accent=True)

    out_path = os.path.join(OUTPUT_DIR, out_filename)
    im.save(out_path, quality=95)
    print(f"Generated: {out_path}")

def draw_key(draw, x, y, w, h, k, mode, f_main, f_top, f_alt):
    top, main, alt, devops = k

    # Background color
    bg = '#1e293b' # Slate dark
    border = '#334155'
    if devops:
        bg = '#132e27' # Emerald tint
        border = '#059669'

    if mode == 'altgr' and alt:
        bg = '#3b2505' # Amber tint
        border = '#d97706'

    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=bg, outline=border, width=2)

    # Top text (Shift state)
    top_color = '#38bdf8' if mode == 'shift' else '#94a3b8'
    draw.text((x + 14, y + 10), top, fill=top_color, font=f_top)

    # Alt text (AltGr state)
    alt_color = '#fbbf24' if mode == 'altgr' else '#b45309'
    if alt:
        draw.text((x + w - 32, y + 10), alt, fill=alt_color, font=f_alt)

    # Main text (Normal state)
    main_color = '#ffffff' if mode == 'normal' else '#cbd5e1'
    if mode == 'altgr' and alt:
        # Highlight alt char as main
        draw.text((x + 40, y + 48), alt, fill='#fbbf24', font=f_main)
    else:
        draw.text((x + 40, y + 48), main, fill=main_color, font=f_main)

def draw_special_key(draw, x, y, w, h, label, font, is_accent=False, is_shift=False, is_altgr=False):
    bg = '#1e293b'
    border = '#334155'
    text_color = '#94a3b8'

    if is_accent:
        bg = '#0284c7'
        border = '#38bdf8'
        text_color = '#ffffff'
    elif is_shift:
        bg = '#1d4ed8'
        border = '#60a5fa'
        text_color = '#ffffff'
    elif is_altgr:
        bg = '#b45309'
        border = '#fbbf24'
        text_color = '#ffffff'

    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=bg, outline=border, width=2)
    draw.text((x + 20, y + 40), label, fill=text_color, font=font)

if __name__ == '__main__':
    # 1. Modern Ergonomic (Normal & Shift)
    render_layout(
        "🇲🇳 Mongolian Modern Ergonomic & DevOps Keyboard Layout (Үндсэн & Shift)",
        "Q = Ө, W = Ү | Native Code Brackets [ ] { } \\ | Preserved | Author: Tsengel (tsengel.de)",
        ERGO_ROW1, ERGO_ROW2, ERGO_ROW3, ERGO_ROW4,
        mode='normal',
        out_filename="layout-ergonomic-normal.png"
    )

    # 2. Modern Ergonomic (AltGr Layer)
    render_layout(
        "🇲🇳 Mongolian Modern Ergonomic - AltGr Өргөтгөл Давхарга (AltGr Layer)",
        "AltGr + T / 4 = ₮ (Төгрөг) | AltGr + D/F = « » | AltGr + Q/W = Ъ/Ь | AltGr + Space = \\u202F (NNBSP)",
        ERGO_ROW1, ERGO_ROW2, ERGO_ROW3, ERGO_ROW4,
        mode='altgr',
        out_filename="layout-ergonomic-altgr.png"
    )

    # 3. Classic Tsengel Layout
    render_layout(
        "🇲🇳 Mongolian Classic Tsengel Layout (2021 Анхны Хувилбар)",
        "Brackets [ = ө, ] = ү | Q = ъ, W = ь | Author: Tsengel (tsengel.de)",
        ERGO_ROW1, CLASSIC_ROW2, ERGO_ROW3, ERGO_ROW4,
        mode='normal',
        out_filename="layout-classic-normal.png"
    )

    # 4. Classical Mongol Bichig
    render_layout(
        "🇲🇳 Classical Mongolian Script Layout (Худам Монгол Бичиг)",
        "ᠥ (Q), ᠦ (W), ᠡ (E), ᠣ (O), ᠤ (U), ᠢ (I), ᠠ (A) | Shift+Space = \\u202F (NNBSP) | Author: Tsengel (tsengel.de)",
        ERGO_ROW1, BICHIG_ROW2, BICHIG_ROW3, BICHIG_ROW4,
        mode='normal',
        out_filename="layout-bichig.png"
    )
