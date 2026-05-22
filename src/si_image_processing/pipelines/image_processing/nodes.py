from PIL import Image, ImageFilter, ImageDraw

def process_image(input_path: str, output_path: str):
    # Abrir la imagen
    image = Image.open(input_path)
    
    # Rotar 45 grados
    rotated = image.rotate(45)
    
    # Aplicar filtro de relieve (EMBOSS)
    filtered = rotated.filter(ImageFilter.EMBOSS)
    
    # Dibujar texto sobre la imagen
    draw = ImageDraw.Draw(filtered)
    draw.text((20, 20), "UCV - Sistemas Inteligentes", fill="white")
    
    # Guardar la imagen procesada
    filtered.save(output_path)
    
    return output_path