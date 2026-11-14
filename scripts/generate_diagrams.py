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

# Bachka mn-custom Layout Definitions (All 35 letters on Layer 1 & 2)
BACHKA_ROW1 = [
    ('~', 'ё', '~', False), ('!', '1', '№', False), ('@', '2', '²', False), ('#', '3', '³', False),
    ('$', '4', '₮', True), ('%', '5', '€', False), ('^', '6', '¼', False), ('&', '7', '½', False),
    ('*', '8', '¾', False), ('(', '9', '‘', False), (')', '0', '’', False), ('_', '-', '¥', False),
    ('+', '=', '×', False)
]

BACHKA_ROW2 = [
    ('Ъ', 'ъ', "'", True), ('Ь', 'ь', '`', True), ('Э', 'э', '€', False), ('Р', 'р', '®', False),
    ('Т', 'т', '₮', True), ('Е', 'е', '™', False), ('У', 'у', '„', False), ('И', 'и', '“', False),
    ('О', 'о', '”', False), ('П', 'п', ';', True), ('Ө', 'ө', '[', True), ('Ү', 'ү', ']', True)
]

BACHKA_ROW3 = [
    ('А', 'а', 'μ', False), ('С', 'с', '£', False), ('Д', 'д', '«', True), ('Ф', 'ф', '»', True),
    ('Г', 'г', '{', True), ('Х', 'х', '<', False), ('Ж', 'ж', '>', False), ('К', 'к', '}', True),
    ('Л', 'л', '№', False), ('Щ', 'щ', ':', True), ('Ы', 'ы', '…', True), ('Й', 'й', '\\', True)
]

BACHKA_ROW4 = [
    ('З', 'з', '—', False), ('Ш', 'ш', '–', False), ('Ц', 'ц', '©', False), ('В', 'в', '', False),
    ('Б', 'б', '', False), ('Н', 'н', '<', False), ('М', 'м', '>', False), ('Ч', 'ч', ',', True),
    ('Ю', 'ю', '.', True), ('Я', 'я', '?', True)
]

# Classical Mongolian Script (Tsengel Phonetics: [=ᠥ, ]=ᠦ, A=ᠠ, E=ᠡ...)
BICHIG_ROW1 = [
    ('᠀', '᠄', '~', False, '`', ':'),
    ('!', '᠑', '1', False, '1', '1'),
    ('@', '᠒', '2', False, '2', '2'),
    ('#', '᠓', '3', False, '3', '3'),
    ('$', '᠔', '₮', True, '4', '4'),
    ('%', '᠕', '5', False, '5', '5'),
    ('^', '᠖', '6', False, '6', '6'),
    ('&', '᠗', '7', False, '7', '7'),
    ('*', '᠘', '8', False, '8', '8'),
    ('(', '᠙', '9', False, '9', '9'),
    (')', '᠐', '0', False, '0', '0'),
    ('_', '-', '—', False, '-', '-'),
    ('+', '=', '×', False, '=', '=')
]

BICHIG_ROW2 = [
    ('MVS', '\u180B', "'", True, 'Q', 'FVS1'),
    ('FVS3', '\u180C', '`', True, 'W', 'FVS2'),
    ('ᠡ', 'ᠡ', '\u180E', False, 'E', 'э'),
    ('ᠷ', 'ᠷ', '®', False, 'R', 'р'),
    ('ᠲ', 'ᠲ', '₮', True, 'T', 'т'),
    ('ᠶ', 'ᠶ', '™', False, 'Y', 'й'),
    ('ᠤ', 'ᠤ', '„', False, 'U', 'у'),
    ('ᠢ', 'ᠢ', '“', False, 'I', 'и'),
    ('ᠣ', 'ᠣ', '”', False, 'O', 'о'),
    ('ᠫ', 'ᠫ', ';', False, 'P', 'п'),
    ('ᠥ', 'ᠥ', '[', True, '[', 'ө'),
    ('ᠦ', 'ᠦ', ']', True, ']', 'ү')
]

BICHIG_ROW3 = [
    ('ᠠ', 'ᠠ', 'μ', False, 'A', 'а'),
    ('ᠰ', 'ᠰ', '£', False, 'S', 'с'),
    ('ᠳ', 'ᠳ', '᠈', True, 'D', 'д'),
    ('ᠹ', 'ᠹ', '᠉', True, 'F', 'ф'),
    ('ᠭ', 'ᠭ', '{', True, 'G', 'г'),
    ('ᠬ', 'ᠬ', '<', False, 'H', 'х'),
    ('ᠵ', 'ᠵ', '>', False, 'J', 'ж'),
    ('ᠺ', 'ᠺ', '}', True, 'K', 'к'),
    ('ᠯ', 'ᠯ', '№', False, 'L', 'л'),
    (';', ';', ':', True, ';', ';'),
    ('"', "'", '\u180E', True, "'", "'"),
    ('|', '\\', '\\', True, '\\', '\\')
]

BICHIG_ROW4 = [
    ('ᠽ', 'ᠵ', '—', False, 'Z', 'з'),
    ('ᠱ', 'ᠱ', '–', False, 'X', 'ш'),
    ('ᠼ', 'ᠼ', '©', False, 'C', 'ц'),
    ('ᠸ', 'ᠸ', '', False, 'V', 'в'),
    ('ᠪ', 'ᠪ', '', False, 'B', 'б'),
    ('ᠩ', 'ᠨ', '<', True, 'N', 'н'),
    ('ᠮ', 'ᠮ', '>', False, 'M', 'м'),
    ('ᠴ', 'ᠴ', ',', True, ',', 'ч'),
    ('.', '᠃', '.', True, '.', '.'),
    ('?', '/', '?', False, '/', '/')
]

def is_mongol_script(text):
    for ch in text:
        if 0x1800 <= ord(ch) <= 0x18AF or ord(ch) == 0x202F:
            return True
    return False

def draw_mixed_text(draw, xy, text, fill, font_default, font_bichig):
    """Draw mixed Latin/Cyrillic and Classical Mongolian script without tofu squares."""
    x, y = xy
    for ch in text:
        font = font_bichig if is_mongol_script(ch) else font_default
        y_offset = -4 if is_mongol_script(ch) else 0
        draw.text((x, y + y_offset), ch, fill=fill, font=font)
        try:
            adv = font.getlength(ch)
        except AttributeError:
            bbox = draw.textbbox((x, y + y_offset), ch, font=font)
            adv = bbox[2] - bbox[0]
        x += adv

def draw_flag_badge(draw, x, y, h=34):
    """Draw a clean, crisp vector Mongolian flag [Red | Blue | Red]"""
    w_stripe = 16
    r1 = [x, y, x + w_stripe, y + h]
    b1 = [x + w_stripe, y, x + w_stripe * 2, y + h]
    r2 = [x + w_stripe * 2, y, x + w_stripe * 3, y + h]
    draw.rectangle(r1, fill='#da2032')
    draw.rectangle(b1, fill='#0055a5')
    draw.rectangle(r2, fill='#da2032')
    draw.rectangle([x, y, x + w_stripe * 3, y + h], outline='#ffffff', width=1)

def render_layout(title, subtitle, row1, row2, row3, row4, mode='normal', out_filename='keyboard.png'):
    width = 2000
    height = 920
    im = Image.new('RGB', (width, height), color='#0f172a') # Dark slate
    draw = ImageDraw.Draw(im)

    font_title = ImageFont.truetype(FONT_BOLD, 32)
    font_sub = ImageFont.truetype(FONT_REG, 19)
    font_sub_bichig = ImageFont.truetype(FONT_BICHIG, 24)
    font_main = ImageFont.truetype(FONT_BOLD, 28)
    font_main_bichig = ImageFont.truetype(FONT_BICHIG, 36)
    font_top = ImageFont.truetype(FONT_REG, 17)
    font_top_bichig = ImageFont.truetype(FONT_BICHIG, 22)
    font_alt = ImageFont.truetype(FONT_BOLD, 16)
    font_alt_bichig = ImageFont.truetype(FONT_BICHIG, 20)
    font_special = ImageFont.truetype(FONT_BOLD, 18)
    font_badge = ImageFont.truetype(FONT_BOLD, 17)
    font_latin = ImageFont.truetype(FONT_REG, 13)

    # Draw flag badge
    draw_flag_badge(draw, 60, 42, h=34)

    # Title & Subtitle (mixed fallback prevents tofu squares in subtitle second line)
    draw_mixed_text(draw, (125, 40), title, '#38bdf8', font_title, font_main_bichig)
    draw_mixed_text(draw, (60, 90), subtitle, '#94a3b8', font_sub, font_sub_bichig)

    start_x = 60
    start_y = 145
    key_h = 110
    gap = 12
    key_w = 110

    # Row 1
    cur_x = start_x
    for k in row1:
        draw_key(draw, cur_x, start_y, key_w, key_h, k, mode, font_main, font_main_bichig, font_top, font_top_bichig, font_alt, font_alt_bichig, font_badge, font_latin)
        cur_x += key_w + gap
    draw_special_key(draw, cur_x, start_y, 180, key_h, "Backspace ⌫", font_special)

    # Row 2
    cur_y = start_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 160, key_h, "Tab ⇥", font_special)
    cur_x = start_x + 160 + gap
    for k in row2:
        draw_key(draw, cur_x, cur_y, key_w, key_h, k, mode, font_main, font_main_bichig, font_top, font_top_bichig, font_alt, font_alt_bichig, font_badge, font_latin)
        cur_x += key_w + gap

    # Row 3
    cur_y = cur_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 190, key_h, "Caps Lock ⇪", font_special)
    cur_x = start_x + 190 + gap
    for k in row3:
        draw_key(draw, cur_x, cur_y, key_w, key_h, k, mode, font_main, font_main_bichig, font_top, font_top_bichig, font_alt, font_alt_bichig, font_badge, font_latin)
        cur_x += key_w + gap
    draw_special_key(draw, cur_x, cur_y, 230, key_h, "Enter ↵", font_special, is_accent=True)

    # Row 4
    cur_y = cur_y + key_h + gap
    draw_special_key(draw, start_x, cur_y, 240, key_h, "Shift ⇧", font_special, is_shift=(mode == 'shift'))
    cur_x = start_x + 240 + gap
    for k in row4:
        draw_key(draw, cur_x, cur_y, key_w, key_h, k, mode, font_main, font_main_bichig, font_top, font_top_bichig, font_alt, font_alt_bichig, font_badge, font_latin)
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

def draw_key(draw, x, y, w, h, k, mode, f_main, f_main_bichig, f_top, f_top_bichig, f_alt, f_alt_bichig, f_badge=None, f_latin=None):
    top = k[0]
    main = k[1]
    alt = k[2]
    devops = k[3]
    latin = k[4] if len(k) > 4 else ''
    sub = k[5] if len(k) > 5 else ''

    bg = '#1e293b'
    border = '#334155'
    if devops:
        bg = '#132e27'
        border = '#059669'

    if mode == 'altgr' and alt:
        bg = '#3b2505'
        border = '#d97706'
    elif mode == 'shift':
        bg = '#1e3a5f'
        border = '#2563eb'

    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=bg, outline=border, width=2)

    # Top text (Shift symbol)
    top_color = '#38bdf8' if mode == 'shift' else '#94a3b8'
    used_top_font = f_top_bichig if is_mongol_script(top) else f_top
    draw.text((x + 12, y + 10), top, fill=top_color, font=used_top_font)

    # Alt text (AltGr / Option symbol)
    alt_color = '#fbbf24' if mode == 'altgr' else '#b45309'
    if alt:
        used_alt_font = f_alt_bichig if is_mongol_script(alt) else f_alt
        draw.text((x + w - 38, y + 10), alt, fill=alt_color, font=used_alt_font)

    # Main text (Base symbol)
    char_to_draw = main
    fill_color = '#ffffff'
    if mode == 'shift':
        char_to_draw = top
        fill_color = '#38bdf8'
    elif mode == 'altgr' and alt:
        char_to_draw = alt
        fill_color = '#fbbf24'

    used_main_font = f_main_bichig if is_mongol_script(char_to_draw) else f_main

    # Center placement
    bbox = draw.textbbox((0, 0), char_to_draw, font=used_main_font)
    text_w = bbox[2] - bbox[0]
    center_x = x + (w - text_w) // 2
    center_y = y + (36 if is_mongol_script(char_to_draw) else 44)

    draw.text((center_x, center_y), char_to_draw, fill=fill_color, font=used_main_font)

    # Bottom-left: Physical Latin key
    if latin and f_latin:
        draw.text((x + 12, y + h - 26), latin, fill='#64748b', font=f_latin)

    # Bottom-right: Cyrillic companion helper badge
    if sub and f_badge:
        bbox_sub = f_badge.getbbox(sub)
        sub_w = bbox_sub[2] - bbox_sub[0]
        draw.text((x + w - sub_w - 12, y + h - 28), sub, fill='#38bdf8', font=f_badge)

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
    # 1. Cyrillic - Base (Normal) Layer
    render_layout(
        "Mongolian Cyrillic Keyboard Layout - Base Layer (Үндсэн үе)",
        "Бүх 35 үсэг 1-р үе дээр шууд: Q=ъ, W=ь, E=э, Y=е, [=ө, ]=ү, ;=щ, '=ы, \\=й | Зохиогч: Цэнгэл (Tsengel / tsengel.de)",
        BACHKA_ROW1, BACHKA_ROW2, BACHKA_ROW3, BACHKA_ROW4,
        mode='normal',
        out_filename="layout-cyrillic-normal.png"
    )

    # 2. Cyrillic - Shift Layer
    render_layout(
        "Mongolian Cyrillic Keyboard Layout - Shift Layer (Shift дарсан үе)",
        "Том үсгүүд: Ъ, Ь, Э, Е, Ө, Ү, Щ, Ы, Й, Ё болон тусгай тэмдэгтүүд | Зохиогч: Цэнгэл (Tsengel / tsengel.de)",
        BACHKA_ROW1, BACHKA_ROW2, BACHKA_ROW3, BACHKA_ROW4,
        mode='shift',
        out_filename="layout-cyrillic-shift.png"
    )

    # 3. Cyrillic - AltGr / Option Layer
    render_layout(
        "Mongolian Cyrillic Keyboard Layout - AltGr / Option Layer (Програмист & Тэмдэгт үе)",
        "AltGr: [ ] { } \\ | ; : ` ' \" ₮ € « » — – … | Зохиогч: Цэнгэл (Tsengel / tsengel.de)",
        BACHKA_ROW1, BACHKA_ROW2, BACHKA_ROW3, BACHKA_ROW4,
        mode='altgr',
        out_filename="layout-cyrillic-altgr.png"
    )

    # 4. Classical Mongol Bichig
    render_layout(
        "Classical Mongolian Script Layout - Tsengel Phonetics (Сонгодог Монгол Бичиг)",
        "[ = ᠥ (Ö), ] = ᠦ (Ü), A=ᠠ, E=ᠡ, I=ᠢ, O=ᠣ, U=ᠤ | Shift+Space = \\u202F (NNBSP) | Зохиогч: Цэнгэл (Tsengel / tsengel.de)",
        BICHIG_ROW1, BICHIG_ROW2, BICHIG_ROW3, BICHIG_ROW4,
        mode='normal',
        out_filename="layout-bichig.png"
    )
