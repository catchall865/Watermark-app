from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Water-Markup')
        self.frm = Frame(self)
        self.frm.grid(padx=20, pady=20)
        self.create_widgets()

    def show_image(self, image):
        img_photoimage = ImageTk.PhotoImage(image)
        self.panel = Label(self, image=img_photoimage)
        self.panel.photo = img_photoimage
        self.panel.grid(column=2, row=2)


    def get_image(self):
        path = askopenfilename(filetypes=[('Image File', ('.jpg', 'jpeg', '.png'))])

        self.image = Image.open(path)

        self.show_image(self.image)

    def save_image(self):
        filename = asksaveasfilename(defaultextension='.png')
        if filename:
            self.photo_saveable.save(filename)


    def create_watermark(self):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("arial.ttf", 36)
        text = self.watermark_entry.get()

        text_size = draw.textsize(text, font)

        x = self.image.width - text_size[0] - 10
        y = self.image.height - text_size[1] - 10

        draw.text((x, y), text, font=font)

        photo = ImageTk.PhotoImage(self.image)
        self.photo_saveable = ImageTk.getimage(photo)

        self.save_image()

        self.panel.destroy()

        self.final_panel = Label(self, image=photo)
        self.final_panel.photo = photo
        self.final_panel.grid(row=2, column=2)


    def create_widgets(self):
        select_button_label = Label(self.frm, text='Choose an image to watermark:')
        select_button_label.grid(column=0, row=1)

        select_button = Button(self.frm, text='Browse...' , command=self.get_image)
        select_button.grid(column=1, row=1)

        watermark_entry_label = Label(self.frm, text='Enter your watermark text:')
        watermark_entry_label.grid(column=0, row=2)

        self.watermark_entry = Entry(self.frm, width=25)
        self.watermark_entry.grid(column=1, row=2, padx=10, pady=10)

        create_button = Button(self.frm, text='Add Watermark', command=self.create_watermark)
        create_button.grid(row=3, column=1, padx=10, pady=10)

if __name__ == '__main__':
    app = App()
    app.mainloop()