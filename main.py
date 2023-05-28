 

# root = Tk()
# frm = Frame(root).grid()

# base_url_label = ttk.Label(frm, text='Copy and paste the image url for the base image here:').grid(row=1, column=0)
# base_url_entry = ttk.Entry(frm)
# base_url_entry.grid(row=1, column=1)

# wm_url_label = ttk.Label(frm, text='Copy and paste the image url for the watermark image here (make sure the background is transparent):').grid(row=2, column=0)
# wm_url_entry = ttk.Entry(frm)
# wm_url_entry.grid(row=2, column=1)

# def combine_images():
#     base_url = base_url_entry.get()
#     wm_url = wm_url_entry.get()

#     response_base = requests.get(url=base_url)
#     response_wm = requests.get(url=wm_url)

#     raw_data_base = response_base.content
#     raw_data_wm = response_wm.content

#     img_base = Image.open(BytesIO(raw_data_base))
#     img_wm = Image.open(BytesIO(raw_data_wm))

#     img_base = img_base.resize((1000, 750))
#     img_wm = img_wm.resize((400, 300))

#     combined_image = Image.new('RGBA', img_base.size, (0, 0, 0, 0))

#     combined_image.paste(img_base, (0, 0))
#     combined_image.paste(img_wm, (200, 150))

#     combined_image.convert

#     final_image = ImageTk.PhotoImage(combined_image)
#     img_label = Label(frm, image=final_image).grid(row=0, column=0)
#     img_label.photo = final_image


# combine_button = ttk.Button(frm, text="Display Watermarked Image", command=combine_images).grid(row=3, column=1, pady=15)


# root.mainloop()