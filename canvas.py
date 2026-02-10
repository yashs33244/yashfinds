"""
Threshold Cartography — Final Polish
Tightened proportions. No wasted space. Museum-ready.
"""

from PIL import Image, ImageDraw, ImageFont
import math, os, random

random.seed(42)

W, H = 2400, 2800  # Tightened height — no dead space
BG = "#0B0D10"
PRIMARY = "#E8E4DD"
ACCENT = "#C94A42"
SECONDARY = "#3E6070"
FAINT = "#141820"
DIM = "#222830"
WHISPER = "#485060"
MUTED = "#303840"

FONTS = "/Users/yashbinocs/.config/opencode/skills/canvas-design/canvas-fonts"
OUT = "/Users/yashbinocs/Desktop/my-projects/pinterest-amazon-bot/landing-canvas.png"


def F(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


f_title = F("Italiana-Regular.ttf", 92)
f_sub = F("Jura-Light.ttf", 22)
f_label_sm = F("InstrumentSans-Regular.ttf", 12)
f_accent = F("Italiana-Regular.ttf", 140)
f_section = F("Jura-Medium.ttf", 19)
f_nav = F("InstrumentSans-Bold.ttf", 12)
f_num = F("Jura-Light.ttf", 50)
f_coord = F("DMMono-Regular.ttf", 9)
f_cta = F("InstrumentSans-Bold.ttf", 16)
f_serif_i = F("Lora-Italic.ttf", 13)
f_mono_sm = F("GeistMono-Regular.ttf", 11)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

M = 160
R = W - M

# ============================================================
# 1. STRUCTURAL GRID
# ============================================================

for y in range(M, H - M, 36):
    c = DIM if y % 180 == 0 else FAINT
    draw.line([(M, y), (R, y)], fill=c, width=1)

cols = [M + i * ((R - M) // 5) for i in range(6)]
for x in cols:
    draw.line([(x, M - 30), (x, H - M + 30)], fill=FAINT, width=1)

for x in cols:
    for y in range(M, H - M, 180):
        s = 4
        draw.line([(x - s, y), (x + s, y)], fill=DIM, width=1)
        draw.line([(x, y - s), (x, y + s)], fill=DIM, width=1)

# ============================================================
# 2. EDGE COORDINATES
# ============================================================

for i, y in enumerate(range(M, H - M, 180)):
    t = f"{chr(65 + i % 26)}{i:02d}"
    draw.text((M - 46, y - 4), t, fill=MUTED, font=f_coord)
    draw.text((R + 14, y - 4), t, fill=MUTED, font=f_coord)

for i, x in enumerate(range(M, R + 1, (R - M) // 10)):
    draw.text((x - 4, M - 48), f"{i:02d}", fill=MUTED, font=f_coord)
    draw.text((x - 4, H - M + 38), f"{i:02d}", fill=MUTED, font=f_coord)

# ============================================================
# 3. CONSTELLATION FIELD
# ============================================================

for _ in range(420):
    px = 1350 + random.gauss(0, 300)
    py = 320 + random.gauss(0, 200)
    if M + 20 < px < R - 20 and M + 20 < py < 740:
        b = random.random()
        if b > 0.94:
            draw.ellipse([(px - 2, py - 2), (px + 2, py + 2)], fill=PRIMARY)
        elif b > 0.82:
            draw.ellipse([(px - 1, py - 1), (px + 1, py + 1)], fill=SECONDARY)
        else:
            draw.ellipse([(px, py), (px + 1, py + 1)], fill=DIM)

# Transitional mist
for _ in range(60):
    px = M + random.random() * (R - M)
    py = 740 + random.random() * 300
    draw.rectangle([(px, py), (px + 1, py + 1)], fill=FAINT)

# ============================================================
# 4. ORIGIN WAYPOINT
# ============================================================

ox, oy = 400, 520

for r_val in [140, 112, 84, 56, 28]:
    c = SECONDARY if r_val == 140 else DIM
    draw.ellipse(
        [(ox - r_val, oy - r_val), (ox + r_val, oy + r_val)], outline=c, width=1
    )

draw.ellipse([(ox - 5, oy - 5), (ox + 5, oy + 5)], fill=ACCENT)

for angle in range(0, 360, 15):
    rad = math.radians(angle)
    ri, ro = 136, 144
    x1, y1 = ox + ri * math.cos(rad), oy + ri * math.sin(rad)
    x2, y2 = ox + ro * math.cos(rad), oy + ro * math.sin(rad)
    tc = PRIMARY if angle % 90 == 0 else DIM
    draw.line([(x1, y1), (x2, y2)], fill=tc, width=1)

draw.text((ox + 160, oy - 22), "ORIGIN", fill=WHISPER, font=f_label_sm)
draw.text((ox + 160, oy - 6), "Point of first contact", fill=MUTED, font=f_coord)

# ============================================================
# 5. TITLE
# ============================================================

ty = 210
draw.text((M + 4, ty), "Smart Picks", fill=PRIMARY, font=f_title)

rule_y = ty + 106
draw.line([(M, rule_y), (M + 500, rule_y)], fill=SECONDARY, width=1)
draw.line([(M, rule_y - 4), (M, rule_y + 4)], fill=SECONDARY, width=1)
draw.line([(M + 500, rule_y - 4), (M + 500, rule_y + 4)], fill=SECONDARY, width=1)

draw.text((M + 4, rule_y + 12), "CURATED PRODUCT CARTOGRAPHY", fill=WHISPER, font=f_sub)
draw.text((M + 520, rule_y + 2), "EST. 2026", fill=MUTED, font=f_coord)

# ============================================================
# 6. THREE TERRITORIES
# ============================================================

zones = [
    (
        M + 20,
        830,
        "01",
        "HOME",
        "Decor & Organization",
        "Threshold objects for dwelling spaces",
    ),
    (
        M + 720,
        830,
        "02",
        "CRAFT",
        "Kitchen & Tools",
        "Essential instruments of daily ritual",
    ),
    (
        M + 1420,
        830,
        "03",
        "FORM",
        "Tech & Aesthetic",
        "Where function meets visual order",
    ),
]

for x, y, num, title, sub, note in zones:
    draw.text((x, y), num, fill=DIM, font=f_num)
    draw.line([(x + 76, y + 6), (x + 76, y + 50)], fill=SECONDARY, width=1)
    draw.text((x + 92, y + 4), title, fill=PRIMARY, font=f_section)
    draw.text((x + 92, y + 26), sub, fill=WHISPER, font=f_label_sm)
    draw.text((x + 92, y + 42), note, fill=MUTED, font=f_coord)

    for row in range(3):
        for col in range(30):
            dx = x + col * 8
            dy = y + 62 + row * 8
            if random.random() > 0.3:
                f = SECONDARY if random.random() > 0.95 else DIM
                draw.rectangle([(dx, dy), (dx + 1, dy + 1)], fill=f)

# ============================================================
# 7. THRESHOLD HORIZON
# ============================================================

hl = 1040
draw.line([(M, hl), (R, hl)], fill=SECONDARY, width=2)

for x in range(M, R, 16):
    h = 5 if x % 80 == 0 else 2
    draw.line([(x, hl - h), (x, hl)], fill=DIM, width=1)

# Atmospheric echo
for offset in [3, 6, 10]:
    draw.line([(M, hl + offset), (R, hl + offset)], fill=FAINT, width=1)

draw.text((R - 200, hl + 14), "THRESHOLD  37.7749N", fill=MUTED, font=f_coord)

# ============================================================
# 8. WAYPOINTS + PATHS
# ============================================================

wps = [
    (1620, 970, 45, "DISCOVER"),
    (340, 1580, 55, "CURATE"),
    (1460, 2060, 38, "COLLECT"),
]


def dashed(p1, p2, color, dl=7, gl=5):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    L = math.sqrt(dx * dx + dy * dy)
    if L == 0:
        return
    ux, uy = dx / L, dy / L
    pos = 0
    while pos < L:
        e = min(pos + dl, L)
        draw.line(
            [(p1[0] + ux * pos, p1[1] + uy * pos), (p1[0] + ux * e, p1[1] + uy * e)],
            fill=color,
            width=1,
        )
        pos = e + gl


pts = [(ox, oy)] + [(w[0], w[1]) for w in wps]
for i in range(len(pts) - 1):
    dashed(pts[i], pts[i + 1], DIM)

for wx, wy, wr, lbl in wps:
    draw.ellipse([(wx - wr, wy - wr), (wx + wr, wy + wr)], outline=DIM, width=1)
    draw.ellipse([(wx - 3, wy - 3), (wx + 3, wy + 3)], fill=SECONDARY)
    draw.text((wx + wr + 12, wy - 6), lbl, fill=WHISPER, font=f_label_sm)

# ============================================================
# 9. MONUMENTAL WORD
# ============================================================

draw.text((M, 1140), "arrive.", fill=ACCENT, font=f_accent)
draw.text(
    (M + 8, 1300),
    "The moment before discovery becomes possession.",
    fill=MUTED,
    font=f_serif_i,
)

# ============================================================
# 10. PRODUCT GRID — full width
# ============================================================

gy_start = 1400
cell = 68
gap = 7
gcols = int((R - M) / (cell + gap))
grows = 6

palette = [BG, FAINT, DIM, SECONDARY, "#1A2830", "#151E24", MUTED, "#1E2A34"]

accent_cells = {
    (0, 3),
    (0, 10),
    (0, 18),
    (1, 7),
    (1, 15),
    (1, 22),
    (2, 1),
    (2, 11),
    (2, 20),
    (3, 5),
    (3, 14),
    (3, 23),
    (4, 0),
    (4, 9),
    (4, 17),
    (5, 4),
    (5, 12),
    (5, 21),
}
secondary_cells = {
    (0, 7),
    (0, 15),
    (1, 2),
    (1, 19),
    (2, 6),
    (2, 15),
    (3, 10),
    (3, 21),
    (4, 4),
    (4, 14),
    (4, 23),
    (5, 1),
    (5, 9),
    (5, 17),
}

for row in range(grows):
    for col in range(gcols):
        gx = M + col * (cell + gap)
        gy = gy_start + row * (cell + gap)
        if gx + cell > R:
            continue

        if (row, col) in accent_cells:
            fc = ACCENT
        elif (row, col) in secondary_cells:
            fc = SECONDARY
        else:
            idx = (row * 3 + col * 7 + row * col * 2) % len(palette)
            fc = palette[idx]

        draw.rectangle([(gx, gy), (gx + cell, gy + cell)], fill=fc)
        n = f"{row * gcols + col + 1:02d}"
        draw.text((gx + 3, gy + 3), n, fill=WHISPER, font=f_coord)

cap_y = gy_start + grows * (cell + gap) + 8
draw.text(
    (M, cap_y),
    f"FIG. 01  /  PRODUCT TERRAIN MAP  /  {grows * gcols} CURATED OBJECTS",
    fill=MUTED,
    font=f_coord,
)

# ============================================================
# 11. NAVIGATION
# ============================================================

ny = cap_y + 50
draw.line([(M, ny), (R, ny)], fill=DIM, width=1)

navs = ["ORIGIN", "DISCOVER", "CURATE", "COLLECT", "ARRIVE"]
sp = (R - M) // len(navs)

for i, item in enumerate(navs):
    nx = M + i * sp
    active = i == 4
    c = ACCENT if active else WHISPER
    draw.text((nx, ny + 12), item, fill=c, font=f_nav)
    if active:
        bb = draw.textbbox((nx, ny + 12), item, font=f_nav)
        draw.line([(nx, ny + 30), (bb[2], ny + 30)], fill=ACCENT, width=2)

# ============================================================
# 12. FOOTER
# ============================================================

fy = ny + 60
draw.text(
    (M, fy), "in.pinterest.com / cinematicvision1403", fill=WHISPER, font=f_mono_sm
)
draw.text(
    (M, fy + 20),
    "SMART PICKS  /  THRESHOLD CARTOGRAPHY  /  EST. 2026",
    fill=MUTED,
    font=f_coord,
)

# CTA
ctx = R - 240
cty = fy - 2
draw.rectangle([(ctx, cty), (ctx + 230, cty + 40)], outline=ACCENT, width=2)
draw.text((ctx + 22, cty + 10), "BEGIN DISCOVERY", fill=ACCENT, font=f_cta)
ax = ctx + 202
ay = cty + 20
draw.line([(ax, ay), (ax + 10, ay)], fill=ACCENT, width=2)
draw.line([(ax + 7, ay - 3), (ax + 10, ay)], fill=ACCENT, width=2)
draw.line([(ax + 7, ay + 3), (ax + 10, ay)], fill=ACCENT, width=2)

# ============================================================
# 13. COMPASS
# ============================================================

ccx, ccy = R - 50, H - M - 30
cr = 24
draw.ellipse([(ccx - cr, ccy - cr), (ccx + cr, ccy + cr)], outline=DIM, width=1)
for a in [0, 90, 180, 270]:
    rad = math.radians(a)
    draw.line(
        [
            (ccx + (cr - 4) * math.cos(rad), ccy + (cr - 4) * math.sin(rad)),
            (ccx + (cr + 4) * math.cos(rad), ccy + (cr + 4) * math.sin(rad)),
        ],
        fill=PRIMARY if a == 270 else DIM,
        width=1,
    )
draw.text((ccx - 3, ccy - cr - 14), "N", fill=WHISPER, font=f_coord)
draw.ellipse([(ccx - 2, ccy - 2), (ccx + 2, ccy + 2)], fill=SECONDARY)

# ============================================================
# 14. MARGIN MARKS + BOTTOM TICKS
# ============================================================

for _ in range(20):
    mx = random.choice([random.randint(40, M - 20), random.randint(R + 20, W - 40)])
    my = random.randint(M, H - M)
    s = 3
    draw.line([(mx - s, my), (mx + s, my)], fill=DIM, width=1)
    draw.line([(mx, my - s), (mx, my + s)], fill=DIM, width=1)

for x in range(M, R, 20):
    th = 5 if x % 100 == 0 else 2
    draw.line([(x, H - M + 16), (x, H - M + 16 + th)], fill=DIM, width=1)

# ============================================================
# SAVE
# ============================================================

img.save(OUT, "PNG", quality=100)
print(f"Saved: {OUT} ({W}x{H})")
