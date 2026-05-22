import os
from PIL import Image
from si_image_processing.pipelines.image_processing.nodes import process_image

def test_process_image(tmp_path):
    """
    Prueba unitaria para verificar que el nodo de procesamiento de imágenes 
    funciona correctamente.
    """
    # 1. Configurar rutas temporales provistas por Pytest (tmp_path)
    input_img_path = str(tmp_path / "test_input.jpg")
    output_img_path = str(tmp_path / "test_output.jpg")
    
    # 2. Crear una imagen falsa de 100x100 en la carpeta temporal para la prueba
    img = Image.new('RGB', (100, 100), color='red')
    img.save(input_img_path)

    # 3. Ejecutar tu función (el nodo)
    result = process_image(input_img_path, output_img_path)

    # 4. Validar (Asserts) que la función hizo su trabajo
    assert result == output_img_path  # Verifica que retorna la ruta correcta
    assert os.path.exists(output_img_path)  # Verifica que la imagen procesada realmente se creó