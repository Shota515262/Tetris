from PIL import Image, ImageDraw
import random
import math

WIDTH = 800
HEIGHT = 600

NUM_ROSES = 120
NUM_FRAMES = 40

frames = []

roses = []

for _ in range(NUM_ROSES):
    roses.append({
        "x": random.randint(0, WIDTH),
        "y": random.randint(-HEIGHT, HEIGHT),
        "speed": random.uniform(2, 6),
        "size": random.randint(6, 14),
        "color": random.choice([
            (255, 80, 80),
            (255, 120, 120),
            (255, 80, 180),
            (200, 100, 255)
        ])
    })

for frame_number in range(NUM_FRAMES):

    image = Image.new("RGB", (WIDTH, HEIGHT), (5, 5, 20))
    draw = ImageDraw.Draw(image)

    for rose in roses:

        rose["y"] += rose["speed"]

        if rose["y"] > HEIGHT + 20:
            rose["y"] = -20
            rose["x"] = random.randint(0, WIDTH)

        x = rose["x"]
        y = rose["y"]
        size = rose["size"]

        for angle in range(0, 360, 60):

            px = x + math.cos(math.radians(angle)) * size
            py = y + math.sin(math.radians(angle)) * size

            draw.ellipse(
                (
                    px - size,
                    py - size,
                    px + size,
                    py + size
                ),
                fill=rose["color"]
            )

        draw.ellipse(
            (
                x - size // 2,
                y - size // 2,
                x + size // 2,
                y + size // 2
            ),
            fill=(255, 220, 0)
        )

    frames.append(image)

frames[0].save(
    "rose_rain.gif",
    save_all=True,
    append_images=frames[1:],
    duration=80,
    loop=0
)

print("rose_rain.gif created successfully!")