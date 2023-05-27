from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont
from io import BytesIO
import requests

# class App(Tk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title('Water-Markup')
#         self.frm = Frame(self)
#         self.frm.grid(padx=20, pady=20)
#         self.create_widgets()

#     def show_image(self, image):
#         img_photoimage = ImageTk.PhotoImage(image)
#         panel = Label(self, image=img_photoimage)
#         panel.photo = img_photoimage
#         panel.grid(column=1, row=1)

#     def get_image(self):
#         path = askopenfilename(filetypes=[('Image File', ('.jpg', 'jpeg', '.png'))])

#         image = Image.open(path)
#         image = image.resize((1366, 768))

#         self.show_image(image)

#         # Create a drawing context
#         draw = ImageDraw.Draw(image)

#     def create_widgets(self):
#         file_select = Button(self.frm, text='Select image...' , command=self.get_image)
#         file_select.grid(column=0, row=1)

    # def create_watermark(image):
    #     # Define the font and text to use for the watermark
    #     font = ImageFont.truetype("arial.ttf", 36)
    #     text = "Watermark"

    #     # Get the size of the text
    #     text_size = draw.textsize(text, font)

    #     # Calculate the position of the text
    #     x = image.width - text_size[0] - 10
    #     y = image.height - text_size[1] - 10

    #     # Draw the text on the image
    #     draw.text((x, y), text, font=font)

    # # Convert the image to a PhotoImage object
    # photo = ImageTk.PhotoImage(image)

    # # Create a label with the image
    # label = ttk.Label(root, image=photo)
    # label.pack()
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()

root = Tk()
frm = Frame(root).grid()

base_url_label = ttk.Label(frm, text='Copy and paste the image url for the base image here:').grid(row=1, column=0)
base_url_entry = ttk.Entry(frm)
base_url_entry.grid(row=1, column=1)

wm_url_label = ttk.Label(frm, text='Copy and paste the image url for the watermark image here (make sure the background is transparent):').grid(row=2, column=0)
wm_url_entry = ttk.Entry(frm)
wm_url_entry.grid(row=2, column=1)

def combine_images():
    base_url = base_url_entry.get()
    wm_url = wm_url_entry.get()

    response_base = requests.get(url=base_url)
    response_wm = requests.get(url=wm_url)

    raw_data_base = response_base.content
    raw_data_wm = response_wm.content

    img_base = Image.open(BytesIO(raw_data_base))
    img_wm = Image.open(BytesIO(raw_data_wm))

    img_base = img_base.resize((1000, 750))
    img_wm = img_wm.resize((400, 300))

    combined_image = Image.new('RGBA', img_base.size, (0, 0, 0, 0))

    combined_image.paste(img_base, (0, 0))
    combined_image.paste(img_wm, (200, 150))

    combined_image.convert

    final_image = ImageTk.PhotoImage(combined_image)
    img_label = Label(frm, image=final_image).grid(row=0, column=0)
    img_label.photo = final_image


combine_button = ttk.Button(frm, text="Display Watermarked Image", command=combine_images).grid(row=3, column=1, pady=15)


root.mainloop()