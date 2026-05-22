from typing import Dict
from kedro.pipeline import Pipeline
from si_image_processing.pipelines.image_processing.pipeline import create_pipeline as ip_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    """Registra los pipelines del proyecto."""
    
    # Cargamos nuestro pipeline de procesamiento de imágenes
    image_processing_pipeline = ip_pipeline()

    return {
        # Lo registramos como el pipeline por defecto y también con un nombre específico
        "__default__": image_processing_pipeline,
        "image_processing": image_processing_pipeline,
    }