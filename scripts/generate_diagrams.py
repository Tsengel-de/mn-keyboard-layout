#!/usr/bin/env python3
"""
Generate crisp, high-resolution vector and raster keyboard layout diagrams.
With automatic font fallback for Classical Mongolian Script (Noto Sans Mongolian)
and vector Mongolian flag badge to eliminate all emoji square tofu.
Author: Tsengel (tsengel.de)
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = str(REPO_ROOT / "docs" / "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_BICHIG = "/usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf"

# Layout Definitions
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
    ('|', '\\', '|', True)
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
    ('|', '\\', '|', True)
]

BICHIG_ROW1 = [
    ('~', '᠄', '`', False), ('!', '᠑', '1', False), ('@', '᠒', '2', False), ('#', '᠓', '3', False),
    ('₮', '᠔', '4', True), ('%', '᠕', '5', False), ('^', '᠖', '6', False), ('&', '᠗', '7', False),
    ('*', '᠘', '8', False), ('(', '᠙', '9', False), (')', '᠐', '0', False), ('_', '-', '—', False),
    ('+', '=', '×', False)
]

BICHIG_ROW2 = [
    ('Q', 'ᠥ', 'Ö', True), ('W', 'ᠦ', 'Ü', True), ('E', 'ᠡ', 'E', True), ('R', 'ᠷ', 'R', False),
    ('T', 'ᠲ', 'T', True), ('Y', 'ᠶ', 'Y', False), ('U', 'ᠤ', 'U', True), ('I', 'ᠢ', 'I', False),
    ('O', 'ᠣ', 'O', False), ('P', 'ᠫ', 'P', False), ('{', '[', '᠈', True), ('}', ']', '᠉', True),
    ('|', '\\', '', True)
]

BICHIG_ROW3 = [
    ('A', 'ᠠ', 'A', False), ('S', 'ᠰ', 'S', False), ('D', 'ᠳ', 'D', False), ('F', 'ᠹ', 'F', False),
    ('G', 'ᠭ', 'G', False), ('H', 'ᠬ', 'H', False), ('J', 'ᠵ', 'J', False), ('K', 'ᠺ', 'K', False),
    ('L', 'ᠯ', 'L', False), (':', ';', '', True), ('"', "'", 'MVS', True)
]

BICHIG_ROW4 = [
    ('Z', 'ᠽ', 'Z', False), ('X', 'ᠱ', 'Sh', False), ('C', 'ᠴ', 'Ch', False), ('V', 'ᠸ', 'V', False),
    ('B', 'ᠪ', 'B', False), ('N', 'ᠨ', 'N', False), ('M', 'ᠮ', 'M', False), ('<', '᠂', ',', True),
    ('>', '᠃', '.', True), ('?', '/', '', True)
]

def is_mongol_script(text):
    for ch in text:
        if 0x1800 <= ord(ch) <= 0x18AF:
            return True
    return False

def draw_flag_badge(draw, x, y, h=34):
    """Draw a clean, crisp vector Mongolian flag [Red | Blue | Red]"""
    w_stripe = 16
    r1 = [x, y, x + w_stripe, y + h]
    b1 = [x + w_stripe, y, x + w_stripe * 2, y + h]
    r2 = [x + w_stripe * 2, y, x + w_stripe * 3, y + h]
    draw.rectangle(r1, fill='#da2032')
    draw.rectangle(b1, fill='#0055a5')
    draw.rectangle(r2, fill='#da2032')
    # Outline
    draw.rectangle([x, y, x + w_stripe * 3, y + h], outline='#ffffff', width=1)

def render_layout(title, subtitle, row1, row2, row3, row4, mode='normal', out_filename='keyboard.png'):
    width = 2000
    height = 920
    im = Image.new('RGB', (width, height), color='#0f172a') # Dark slate
    draw = ImageDraw.Draw(im)

    font_title = ImageFont.truetype(FONT_BOLD, 32)
    font_sub = ImageFont.truetype(FONT_REG, 19)
    font_main = ImageFont.truetype(FONT_BOLD, 28)
    font_main_bichig = ImageFont.truetype(FONT_BICHIG, 36)
    font_top = ImageFont.truetype(FONT_REG, 17)
    font_top_bichig = ImageFont.truetype(FONT_BICHIG, 22)
    font_alt = ImageFont.truetype(FONT_BOLD, 16)
    font_special = ImageFont.truetype(FONT_BOLD, 18)

    # Draw flag badge
    draw_flag_badge(draw, 60, 42, h=34)

    # Title & Subtitle (WITHOUT raw flag emoji to avoid square tofu)
    draw.text((125, 40), title, fill='#38bdf8', font=font_title)
    draw.text((60, 90), subtitle, fill='#94a3b8', font=font_sub)

    start_x = 60
    start_y = 145
    key_h = 110
    gap = 12
    key_w = 110

    # Row 1
    cur_x = start_x
    for k in row1:
        draw_key(draw, cur_x, start_y, key_w, key_h, k, mode, font_main, font_main_bichig, font_top, font_top_bichig, font_alt)
        cur_x += key_w + gap
    draw_special_key(draw, cur_x, start_y, 180, key_h, "Backspace ⌫", font_special)

    # Row 2
    cur_y = start_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 160, key_h, "Tab ⇥", font_special)
    cur_x = start_x + 160 + gap
    for k in row2:
        draw_key(draw, cur_x, cur_y, key_w, key_h, k, mode, font_main, font_main_bichig, font_top, font_top_bichig, font_alt)
        cur_x += key_w + gap

    # Row 3
    cur_y = cur_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 190, key_h, "Caps Lock ⇪", font_special)
    cur_x = start_x + 190 + gap
    for k in row3:
        draw_key(draw, cur_x, cur_y, key_w, key_h, k, mode, font_main, font_main_bichig, font_top, font_top_bichig, font_alt)
        cur_x += key_w + gap
    draw_special_key(draw, cur_x, cur_y, 230, key_h, "Enter ↵", font_special, is_accent=True)

    # Row 4
    cur_y = cur_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 240, key_h, "Shift ⇧", font_special, is_shift=(mode == 'shift'))
    cur_x = start_x + 240 + gap
    for k in row4:
        draw_key(draw, cur_x, cur_y, key_w, key_h, k, mode, font_main, font_main_bichig, font_top, font_top_bichig, font_alt)
        cur_x += key_w + gap
    draw_special_key(draw, cur_x, cur_y, 300, key_h, "Shift ⇧", font_special, is_shift=(mode == 'shift'))

    # Row 5 (Space Row)
    cur_y = cur_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 140, key_h, "Ctrl", font_special)
    draw_special_key(draw, start_x + 152, cur_y, 130, key_h, "Alt", font_special)
    
    space_w = 780
    space_x = start_x + 294
    draw.rounded_rectangle([space_x, cur_y, space_x + space_w, cur_y + key_h], radius=10, fill='#1e293b', outline='#334155', width=2)
    draw.text((space_x + 320, cur_y + 40), "Spacebar", fill='#64748b', font=font_special)

    altgr_x = space_x + space_w + gap
    draw_special_key(draw, altgr_x, cur_y, 160, key_h, "AltGr", font_special, is_altgr=(mode == 'altgr'))

    nnbsp_x = altgr_x + 160 + gap
    draw_special_key(draw, nnbsp_x, cur_y, 220, key_h, "NNBSP (\\u202F)", font_special, is_accent=True)

    out_path = os.path.join(OUTPUT_DIR, out_filename)
    im.save(out_path, quality=95)
    print(f"Generated: {out_path}")

def draw_key(draw, x, y, w, h, k, mode, f_main, f_main_bichig, f_top, f_top_bichig, f_alt):
    top, main, alt, devops = k

    bg = '#1e293b'
    border = '#334155'
    if devops:
        bg = '#132e27'
        border = '#059669'

    if mode == 'altgr' and alt:
        bg = '#3b2505'
        border = '#d97706'

    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=bg, outline=border, width=2)

    # Top text
    top_color = '#38bdf8' if mode == 'shift' else '#94a3b8'
    used_top_font = f_top_bichig if is_mongol_script(top) else f_top
    draw.text((x + 12, y + 10), top, fill=top_color, font=used_top_font)

    # Alt text
    alt_color = '#fbbf24' if mode == 'altgr' else '#b45309'
    if alt:
        draw.text((x + w - 38, y + 10), alt, fill=alt_color, font=f_alt)

    # Main text
    main_color = '#ffffff' if mode == 'normal' else '#cbd5e1'
    char_to_draw = alt if (mode == 'altgr' and alt) else main
    fill_color = '#fbbf24' if (mode == 'altgr' and alt) else main_color
    used_main_font = f_main_bichig if is_mongol_script(char_to_draw) else f_main

    # Center placement
    bbox = draw.textbbox((0, 0), char_to_draw, font=used_main_font)
    text_w = bbox[2] - bbox[0]
    center_x = x + (w - text_w) // 2
    center_y = y + (40 if is_mongol_script(char_to_draw) else 46)

    draw.text((center_x, center_y), char_to_draw, fill=fill_color, font=used_main_font)

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
    draw.text((x + 18, y + 42), label, fill=text_color, font=font)

if __name__ == '__main__':
    # 1. Modern Ergonomic
    render_layout(
        "Mongolian Modern Ergonomic & DevOps Keyboard Layout (Normal & Shift)",
        "Q = Ө, W = Ү | Native Code Brackets [ ] { } \\ | Preserved | Author: Tsengel (tsengel.de)",
        ERGO_ROW1, ERGO_ROW2, ERGO_ROW3, ERGO_ROW4,
        mode='normal',
        out_filename="layout-ergonomic-normal.png"
    )

    # 2. Modern Ergonomic (AltGr)
    render_layout(
        "Mongolian Modern Ergonomic - AltGr Extension Layer",
        "AltGr + T / 4 = ₮ (Tugrik) | AltGr + D/F = « » | AltGr + Q/W = Ъ/Ь | AltGr + Space = \\u202F (NNBSP)",
        ERGO_ROW1, ERGO_ROW2, ERGO_ROW3, ERGO_ROW4,
        mode='altgr',
        out_filename="layout-ergonomic-altgr.png"
    )

    # 3. Classic Tsengel Layout
    render_layout(
        "Mongolian Classic Tsengel Layout (2021 Edition)",
        "Brackets [ = ө, ] = ү | Q = ъ, W = ь | Author: Tsengel (tsengel.de)",
        ERGO_ROW1, CLASSIC_ROW2, ERGO_ROW3, ERGO_ROW4,
        mode='normal',
        out_filename="layout-classic-normal.png"
    )

    # 4. Classical Mongol Bichig
    render_layout(
        "Classical Mongolian Script Layout (Худам Монгол Бичиг)",
        "Q=ᠥ(Ö), W=ᠦ(Ü), E=ᠡ(E), O=ᠣ(O), U=ᠤ(U), I=ᠢ(I), A=ᠠ(A) | Shift+Space = \\u202F (NNBSP) | Author: Tsengel",
        BICHIG_ROW1, BICHIG_ROW2, BICHIG_ROW3, BICHIG_ROW4,
        mode='normal',
        out_filename="layout-bichig.png"
    )
