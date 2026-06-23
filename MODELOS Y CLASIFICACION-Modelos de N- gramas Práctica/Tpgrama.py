from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import pandas as pd
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def cargar_corpus(ruta_archivo):
    """Carga las líneas del archivo de texto manejando codificación latin-1."""
    try:
        #   tuve que usar 'latin-1' para evitar el UnicodeDecodeError con caracteres en español
        with open(ruta_archivo, 'r', encoding='latin-1') as f:
            return [linea.strip() for linea in f.readlines() if linea.strip()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}.")
        return []

def preparar_texto(texto_original):
    """
    Cumple con la preparación completa de la consigna:
    1. Tokens (word_tokenize)
    2. Stop_words (Filtro en español)
    3. Lemas (WordNetLemmatizer o reducción básica)
    """
    tokens = word_tokenize(texto_original.lower())
    
    stop_words_esp = stopwords.words("spanish")
    lemmatizer = WordNetLemmatizer()
    
    tokens_procesados = []
    for token in tokens:
        if (token not in stop_words_esp and 
            token not in string.punctuation and 
            token not in ["'s", '|', '--', "''", "``", "-", ".-", ".", "2025"]):
            
            lema = lemmatizer.lemmatize(token)
            tokens_procesados.append(lema)
            
    return " ".join(tokens_procesados)

def generar_grafico_ngramas(corpus_preparado):
    """
    Configura el CountVectorizer con min_df=2 y ngram_range=(2,3) 
    para graficar la comparación.
    """
    vectorizer = CountVectorizer(ngram_range=(2, 3), min_df=2)
    
    X = vectorizer.fit_transform(corpus_preparado)
    
    if X.shape[1] == 0:
        print("No se encontraron N-gramas que se repitan al menos 2 veces (min_df=2) en el texto proporcionado.")
        return

    df_ngramas = pd.DataFrame(
        X.sum(axis=0).T,
        index=vectorizer.get_feature_names_out(),
        columns=['frecuencia']
    )
    
    df_ngramas.sort_values(by='frecuencia', ascending=True).plot(
        kind='barh', 
        title='Comparación de 2-gramas y 3-gramas (min_df=2)',
        color='skyblue'
    )
    plt.xlabel('Cantidad de Apariciones')
    plt.ylabel('N-gramas (Secuencias)')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    archivo_opiniones = "CorpusEducacion.txt"
    
    lineas_corpus = cargar_corpus(archivo_opiniones)
    
    if lineas_corpus:
        corpus_final = [preparar_texto(linea) for linea in lineas_corpus]
        
        generar_grafico_ngramas(corpus_final)