import os
import matplotlib.pyplot as plt
import numpy as np
import librosa
import soundfile as sf
from IPython.display import Audio

carpeta_actual = os.path.dirname(os.path.abspath(__file__))

archivo_original = os.path.join(carpeta_actual, 'AnalisisTextos.mp3') 
archivo_procesado = os.path.join(carpeta_actual, 'AnalisisTextos_procesado.wav')

print(f"Buscando audio original en: {archivo_original}")

if not os.path.exists(archivo_original):
    raise FileNotFoundError("¡Error! No se encontró 'AnalisisTextos.mp3'. Asegurate de ponerlo en la misma carpeta que este script.")

print("\n=== PASO 2 y 3: RESAMPLEANDO AUDIO A 16kHz Y MONO ===")
audio, sr = librosa.load(archivo_original, sr=16000, mono=True)

sf.write(archivo_procesado, audio, samplerate=sr)
print(f"¡Audio resampleado con éxito y guardado en!: {archivo_procesado}")


print("\n=== PASO 4: MÉTRICAS CON PYTHON ===")
print("Vector de la señal segmentada (primeras 5 muestras):", audio[:5])
print("Cantidad de elementos de la muestra (Largo del array):", len(audio))
print("Frecuencia de Muestreo (Sampling Rate):", sr, "Hz")

duracion = len(audio) / sr
print(f"Duración en segundos del audio: {duracion:.2f} segundos")


print("\n=== PASO 5: GENERANDO GRÁFICO DE LA ONDA ===")
plt.figure(figsize=(10, 4))
plt.plot(audio, color='teal')
plt.title('Representación Visual de la Señal Sonora (Forma de Onda)')
plt.xlabel('Número de Muestra')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()


print("\n=== PASO 6: REPRODUCCIÓN ORIGINAL ===")
audio_original_widget = Audio(audio, rate=sr)


print("\n=== PASO 7: CONFIGURANDO VARIACIONES DE TIEMPO ===")
audio_rapido = Audio(audio, rate=sr * 2)

audio_lento = Audio(audio, rate=sr * 0.5)


print("\n=== PASO 8: REDUCIÓN DE CALIDAD A 8 BITS ===")
audio_baja_calidad = (audio * 2**3).astype(np.int8)
audio_degradado_widget = Audio(audio_baja_calidad, rate=sr)
print("Proceso completado. Listo para presentar las respuestas analíticas.")