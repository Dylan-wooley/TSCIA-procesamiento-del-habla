import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer  # <--- Agregamos esto

documents = {
    "doc1": "Los egipcios construyeron las pirámides y desarrollaron una escritura jeroglífica.",
    "doc2": "La civilización romana fue una de las más influyentes en la historia occidental.",
    "doc3": "Los mayas eran expertos astrónomos y tenían un avanzado sistema de escritura.",
    "doc4": "La antigua Grecia sentó las bases de la democracia y la filosofía moderna.",
    "doc5": "Los sumerios inventaron la escritura cuneiforme y fundaron las primeras ciudades."
}

stop_words = set(stopwords.words('spanish'))
stemmer = SnowballStemmer('spanish')  # <--- Inicializamos el stemmer en español

def preprocess(text):
    tokens = word_tokenize(text.lower())
    # Guardamos la raíz (stem) de cada palabra que no sea una stopword
    return set([stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words])

index = {}
for doc_id, text in documents.items():
    words = preprocess(text)
    for word in words:
        if word not in index:
            index[word] = set()
        index[word].add(doc_id)

def boolean_search(query):
    terms = query.split() 
    if not terms:
        return set()
        
    first_term = terms[0]
    if first_term.upper() not in ["AND", "OR", "NOT"]:
        first_term = stemmer.stem(first_term.lower())
    else:
        first_term = first_term.lower()

    result_set = index.get(first_term, set()) if first_term not in ["and", "or", "not"] else set(documents.keys())

    i = 1
    while i < len(terms):
        op = terms[i]
        if op == "AND":
            i += 1
            if i < len(terms):
                next_term = stemmer.stem(terms[i].lower())  
                result_set &= index.get(next_term, set()) 
        elif op == "OR":
            i += 1
            if i < len(terms):
                next_term = stemmer.stem(terms[i].lower())  
                result_set |= index.get(next_term, set())
        elif op == "NOT":
            i += 1
            if i < len(terms):
                next_term = stemmer.stem(terms[i].lower())  
                result_set -= index.get(next_term, set()) 
        else:
            next_term = stemmer.stem(op.lower())  
            result_set &= index.get(next_term, set())
        i += 1
    
    return result_set

print("=== Buscador Booleano de Civilizaciones Antiguas ===")
print("Operadores disponibles: AND, OR, NOT (en mayúsculas)")
print("Escribí 'salir' para terminar el programa.\n")

while True:
    user_query = input("Ingrese una consulta booleana (o 'salir' para terminar): ")
    
    if user_query.strip().lower() in ['salir', 'saliu', 'salio']:
        print("Programa finalizado.")
        break
        
    if user_query.strip() == "":
        continue
        
    resultados = boolean_search(user_query)
    print(f" Documentos encontrados: {sorted(list(resultados))}\n")