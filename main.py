import csv
from PIL import Image, ImageDraw, ImageFont
with open('employee_data.csv','r') as employee_data:
    csv_reader= csv.reader(employee_data)

    for name,role,loc in csv_reader:
     print(name,role,loc)

template=Image.open('ute_id_template.png')
#template.show()

draw=ImageDraw.Draw(template)

font = ImageFont.truetype("georgia.ttf", size=25) 
text = "George Cooper"
text_color = (255,255,255)
text_position = (75, 165) # x, y coordinates for the top-left corner of the text

draw.text(text_position, text, font=font, fill=text_color)

template = template.convert("RGB")


employee_photo=Image.open('employee_images\george.jpg')
employee_photo=employee_photo.resize((121,121))
template.paste(employee_photo, (176, 19)) 
template.save("output_image.jpg") # Save the image
template.show() # Display the image (optional)
#employee_photo.show()