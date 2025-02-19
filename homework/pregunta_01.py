# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import glob
import pandas as pd
def pregunta_01():

    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    


  
# 1. Determinar ruta de este archivo y ruta al ZIP
    base_dir = os.path.dirname(__file__)        # Carpeta donde está pregunta_01.py
    repo_root = os.path.join(base_dir, "..")      # Sube un nivel: raíz del repo
    zip_path  = os.path.join(repo_root, "files", "input.zip")
    
    # 2. Descomprimir input.zip en la raíz del repositorio (creando carpeta input/)
    input_folder = os.path.join(repo_root, "input")
    if not os.path.exists(input_folder):
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(repo_root)
    
    # 3. Crear la carpeta output/ si no existe
    output_folder = os.path.join(repo_root, "files", "output")
    os.makedirs(output_folder, exist_ok=True)
    
    # 4. Función auxiliar para leer archivos de un directorio (train o test)
    def build_dataset(split="train"):
        # Ruta a la carpeta (train/ o test/) dentro de input/
        split_folder = os.path.join(input_folder, split)
        
        # Subcarpetas: negative, positive, neutral
        sentiments = ["negative", "positive", "neutral"]
        
        data = []
        for sentiment in sentiments:
            sentiment_folder = os.path.join(split_folder, sentiment)
            # Buscar todos los .txt
            txt_files = glob.glob(os.path.join(sentiment_folder, "*.txt"))
            
            for txt_file in txt_files:
                # Leer todo el contenido del archivo como "phrase"
                with open(txt_file, "r", encoding="utf-8") as f:
                    phrase = f.read().strip()
                
                # Agregar un registro a la lista (se usa la clave "target" en lugar de "sentiment")
                data.append({
                    "phrase": phrase,
                    "target": sentiment
                })
        
        # Convertir a DataFrame con las columnas "phrase" y "target"
        df = pd.DataFrame(data, columns=["phrase", "target"])
        return df
    
    # 5. Construir y guardar train_dataset.csv
    train_df = build_dataset(split="train")
    train_csv_path = os.path.join(output_folder, "train_dataset.csv")
    train_df.to_csv(train_csv_path, index=False)
    
    # 6. Construir y guardar test_dataset.csv
    test_df = build_dataset(split="test")
    test_csv_path = os.path.join(output_folder, "test_dataset.csv")
    test_df.to_csv(test_csv_path, index=False)
