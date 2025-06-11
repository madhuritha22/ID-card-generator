import csv
import os
from PIL import Image, ImageDraw, ImageFont
import img2pdf

ids = "final_templates"
template_path = 'ute_id_template.png'
csv_path = 'employee_data.csv'
pdf_path = 'output.pdf'
font_path = 'georgia.ttf'
image_size = (121, 121)
text_color = (255, 255, 255)
text_position = (75, 165)
font_size = 25
photo_position = (176, 19)

def generate_id(row):
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)
    template = template.convert("RGB")
    
    font = ImageFont.truetype(font_path, size=font_size) 
    text = row[0]
    draw.text(text_position, text, font=font, fill=text_color)

    path = row[2]
    employee_photo = Image.open(path)
    employee_photo = employee_photo.resize(image_size)
    template.paste(employee_photo, photo_position)
    filename = f"{row[0].replace(' ', '_')}.jpg"  
    save_path = os.path.join(ids, filename) 
    template.save(save_path)
    #print(f"Saved: {save_path}")
    template.show() 

def generate_id_all():
    with open(csv_path, 'r') as employee_data:
        csv_reader = csv.reader(employee_data)
        next(csv_reader)
        for row in csv_reader:
            print(row)
            generate_id(row)   

def pdf():
    image_files = [f for f in os.listdir(ids)]
    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert([os.path.join(ids, i) for i in image_files]))

def main():
    generate_id_all()
    pdf()

if __name__ == "__main__":
    main()            