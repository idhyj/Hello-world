from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import random
import math

app = Tk()
app.geometry("600x600")

# Create a blank image and drawing context
myImage = Image.new("RGB", (600, 600), "white")
drawingContext = ImageDraw.Draw(myImage)

# Function to generate random pink color
def random_pink():
    r = random.randint(200, 255)
    g = random.randint(100, 150)
    b = random.randint(150, 200)
    return r, g, b

# Number of circles
num_circles = 100

for _ in range(num_circles):
    # Random circle parameters
    x = random.randint(0, 600)
    y = random.randint(0, 600)
    radius = random.randint(10, 50)
    color = random_pink()

    # Draw dynamic circles with random pink color
    for i in range(36):  # 36 frames for smooth movement
        angle = math.radians(i * 10)  # Increment by 10 degrees for each frame
        offset_x = int(math.cos(angle) * i * 5)  # Dynamic movement offset
        offset_y = int(math.sin(angle) * i * 5)  # Dynamic movement offset
        drawingContext.ellipse(
            [(x - radius + offset_x, y - radius + offset_y),
             (x + radius + offset_x, y + radius + offset_y)],
            fill=color, outline=color)

# Resize the image
myImage = myImage.resize((600, 600), Image.ANTIALIAS)

# Save the artwork as an image file
myImage.save("generative_artwork.png")

# Convert the image to a Tkinter PhotoImage
artwork_image = ImageTk.PhotoImage(myImage)

# Create canvas and display the artwork
canvas = Canvas(app, width=600, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=artwork_image)

# Start the tkinter main loop
app.mainloop()
