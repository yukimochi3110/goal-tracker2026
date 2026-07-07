"""Generate apple-touch-icon.png (180x180) matching the login screen logo."""
from PIL import Image, ImageDraw
import math

SIZE = 180
CORNER = 38  # border-radius (≈21% of 180, matching the app's 16px/52px ratio)

# Gradient colors: #8ED4A8 → #38AD6C (135deg, top-left to bottom-right)
C0 = (142, 212, 168)
C1 = (56,  173, 108)

# ── 1. Gradient background ──────────────────────────────────────────────────
grad = Image.new('RGB', (SIZE, SIZE))
diag = math.sqrt(2) * SIZE
for y in range(SIZE):
    for x in range(SIZE):
        t = min(1.0, max(0.0, (x + y) / (SIZE * 2 - 2)))
        r = int(C0[0] + (C1[0] - C0[0]) * t)
        g = int(C0[1] + (C1[1] - C0[1]) * t)
        b = int(C0[2] + (C1[2] - C0[2]) * t)
        grad.putpixel((x, y), (r, g, b))

# ── 2. Rounded-rect mask ────────────────────────────────────────────────────
mask = Image.new('L', (SIZE, SIZE), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, SIZE-1, SIZE-1], radius=CORNER, fill=255)

img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
img.paste(grad, mask=mask)

# ── 3. Plant / sprout icon ──────────────────────────────────────────────────
# SVG paths defined on a 24×24 viewBox, scale to fit the icon.
# Bounding box of paths: x[10..22], y[8..23]  →  14w × 15h
SCALE = 6.8          # each SVG unit = 6.8 px  →  icon ≈ 95×102 px
OX = SIZE / 2 - 16 * SCALE   # centre on SVG x=16
OY = SIZE / 2 - 15 * SCALE   # centre on SVG midpoint y≈15.5

def pt(sx, sy):
    return (OX + sx * SCALE, OY + sy * SCALE)

def cubic(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t  = i / n
        mt = 1 - t
        x  = mt**3*p0[0] + 3*mt**2*t*p1[0] + 3*mt*t**2*p2[0] + t**3*p3[0]
        y  = mt**3*p0[1] + 3*mt**2*t*p1[1] + 3*mt*t**2*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts

WHITE = (255, 255, 255, 242)   # rgba(255,255,255,0.95)
draw  = ImageDraw.Draw(img, 'RGBA')

# Stem:  M16 23 v-9  →  line (16,23)→(16,14)
sw = round(1.8 * SCALE)       # stroke-width scaled
draw.line([pt(16, 23), pt(16, 14)], fill=WHITE, width=sw)

# Left leaf: M16 19 C13 19 10 16 10 12 C14 12 16 15 16 19 Z  (filled)
leaf_l  = cubic(pt(16,19), pt(13,19), pt(10,16), pt(10,12))
leaf_l += cubic(pt(10,12), pt(14,12), pt(16,15), pt(16,19))
draw.polygon(leaf_l, fill=WHITE)

# Right leaf: M16 15 C19 15 22 12 22 8 C18 8 16 11 16 15 Z  (filled)
leaf_r  = cubic(pt(16,15), pt(19,15), pt(22,12), pt(22,8))
leaf_r += cubic(pt(22,8),  pt(18,8),  pt(16,11), pt(16,15))
draw.polygon(leaf_r, fill=WHITE)

# ── 4. Save ─────────────────────────────────────────────────────────────────
out = img.convert('RGB')   # flatten RGBA → RGB for PNG (Safari reads RGB fine)
out.save('apple-touch-icon.png', 'PNG')
print("apple-touch-icon.png generated (180×180)")
