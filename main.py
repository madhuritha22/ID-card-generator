import csv
import os
from PIL import Image, ImageDraw, ImageFont
import img2pdf

ids="final_templates"
def generate_id(row):
    template=Image.open('ute_id_template.png')
    draw=ImageDraw.Draw(template)

    font = ImageFont.truetype("georgia.ttf", size=25) 
    text = row[0]
    text_color = (255,255,255)
    text_position = (75, 165)

    draw.text(text_position, text, font=font, fill=text_color)

    template = template.convert("RGB")

    path = row[2]
    employee_photo=Image.open(path)
    employee_photo=employee_photo.resize((121,121))
    template.paste(employee_photo, (176, 19))
    filename = f"{row[0].replace(' ', '_')}.jpg"  
    save_path = os.path.join(ids, filename) 
    template.save(save_path)
    print(f"Saved: {save_path}")
    template.show() 


with open('employee_data.csv','r') as employee_data:
    csv_reader= csv.reader(employee_data)
    header=next(csv_reader)
    for row in csv_reader:
     print(row)
     generate_id(row)   

image_files = [f for f in os.listdir("final_templates")]
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([os.path.join("final_templates", i) for i in image_files]))