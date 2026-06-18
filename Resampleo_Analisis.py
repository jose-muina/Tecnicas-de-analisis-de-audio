# %%
import IPython.display
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import soundfile as sf
from IPython.display import Audio

# Señal resampleada
audio, sr = sf.read('output_16bit.wav')
print('\nVector de la Señal Segmentada', audio)
print('Muestra del medio:', audio[50000:50010])
print('Largo array:', len(audio))
print('Frecuencia de Muestreo:', sr)
print('Duración:', len(audio)/sr)
print('Máximo valor:', np.max(np.abs(audio)))
plt.plot(audio)
plt.show()

# Señal original
audio_original, sr_original = sf.read('AnalisisTextos.mp3')
print('Frecuencia de Muestreo original:', sr_original)
print('Duración original:', len(audio_original)/sr_original)
print(' ')

# Reproducir original 
IPython.display.display(Audio(audio_original, rate=sr_original))

# Conversion a Mono si tiene dos canales

if len(audio_original.shape) > 1:

    audio_original = audio_original[:, 0]

# Modificar la frecuencia de muestreo (Hacer que dure mas tiempo)
factor_velocidad = 0.5  
sr_modificado = int(sr_original * factor_velocidad)

# Bajar la calidad del audio (8 bits)
niveles = 2 ** 8  
audio_baja_calidad = np.round((audio_original + 1) * (niveles - 1) / 2)
audio_baja_calidad = (audio_baja_calidad / (niveles - 1)) * 2 - 1

# 3. Reproducir las nuevas señales
print(f"Reproducir Modificado en Tiempo ({factor_velocidad}x):")
IPython.display.display(Audio(audio_original, rate=sr_modificado))

print("Reproducir con Baja Calidad (8 bits):")
IPython.display.display(Audio(audio_baja_calidad, rate=sr_original))
# %%