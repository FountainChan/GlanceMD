# -*- coding: utf-8 -*-
# GlanceMD 图标生成：Marco 风格紫→粉对角渐变圆角方块 + 白色粗体 G
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = 512  # 画布尺寸
# Marco 主题渐变色（略提亮，视觉更明快）
C1 = (168, 85, 247)    # #a855f7 紫
C2 = (236, 72, 153)    # #ec4899 粉
C1B = (186, 113, 255)  # 提亮后的紫（渐变起点）

img = Image.new("RGBA", (S, S), (0, 0, 0, 0))

# ── 对角渐变（左上→右下，逐行插值叠加逐列微调）──
grad = Image.new("RGBA", (S, S))
gd = ImageDraw.Draw(grad)
for y in range(S):
    for_x = y / (S - 1)
    r = int(C1B[0] + (C2[0] - C1B[0]) * for_x)
    g = int(C1B[1] + (C2[1] - C1B[1]) * for_x)
    b = int(C1B[2] + (C2[2] - C1B[2]) * for_x)
    gd.line([(0, y), (S, y)], fill=(r, g, b, 255))

# ── 圆角蒙版：圆角方块 ──
RADIUS = 118
mask = Image.new("L", (S, S), 0)
md = ImageDraw.Draw(mask)
md.rounded_rectangle([0, 0, S - 1, S - 1], radius=RADIUS, fill=255)
icon = Image.new("RGBA", (S, S), (0, 0, 0, 0))
icon.paste(grad, (0, 0), mask)

# ── 顶部高光：白色径向柔光，增加"明亮"质感 ──
hl = Image.new("L", (S, S), 0)
hd = ImageDraw.Draw(hl)
hd.ellipse([S*0.05, -S*0.25, S*0.95, S*0.45], fill=70)
hl = hl.filter(ImageFilter.GaussianBlur(60))
white = Image.new("RGBA", (S, S), (255, 255, 255, 255))
icon.paste(Image.composite(white, icon, hl), (0, 0), mask)

# ── 白色粗体 G（居中，微投影保证小尺寸可读）──
draw = ImageDraw.Draw(icon)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 300)
bbox = draw.textbbox((0, 0), "G", font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
tx = (S - tw) / 2 - bbox[0]
ty = (S - th) / 2 - bbox[1]
# 投影
shadow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.text((tx + 6, ty + 10), "G", font=font, fill=(90, 20, 110, 120))
shadow = shadow.filter(ImageFilter.GaussianBlur(8))
icon = Image.alpha_composite(icon, shadow)
draw = ImageDraw.Draw(icon)
draw.text((tx, ty), "G", font=font, fill=(255, 255, 255, 255))

icon.save("assets/icon.png")

# ── 多分辨率 ICO ──
sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
icon.save("assets/icon.ico", format="ICO", sizes=sizes)
print("icon.png + icon.ico generated")
