import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

documents = {
    "doc1": "La inteligencia artificial está revolucionando la tecnología.",
    "doc2": "El aprendizaje automático es clave en la inteligencia artificial.",
    "doc3": "Procesamiento del lenguaje natural y redes neuronales.",
    "doc4": "Las redes neuronales son fundamentales en deep learning.",
    "doc5": "El futuro de la IA está en el aprendizaje profundo."
}

stop_words = set(stopwords.words('spanish'))

def preprocess(text):
    tokens = word_tokenize(text.lower()) 
    return set([word for word in tokens if word.isalnum() and word not in stop_words])

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
        
    first_term = terms[0].lower()
    result_set = index.get(first_term, set()) if first_term not in ["and", "or", "not"] else set(documents.keys())

    i = 1
    while i < len(terms):
        op = terms[i]
        if op == "AND":
            i += 1
            if i < len(terms):
                next_term = terms[i].lower()
                result_set &= index.get(next_term, set())  
        elif op == "OR":
            i += 1
            if i < len(terms):
                next_term = terms[i].lower()
                result_set |= index.get(next_term, set())  
        elif op == "NOT":
            i += 1
            if i < len(terms):
                next_term = terms[i].lower()
                result_set -= index.get(next_term, set())  
        else:
            next_term = op.lower()
            result_set &= index.get(next_term, set())
        i += 1
    
    return result_set

print("=== Buscador Booleano de Inteligencia Artificial ===")
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