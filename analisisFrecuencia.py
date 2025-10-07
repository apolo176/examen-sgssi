from collections import Counter

# Frecuencia típica del español (%)
frecuencia_espanol = [
    ('E', 13.68), ('A', 12.53), ('O', 8.68), ('S', 7.98), ('N', 6.71),
    ('R', 6.87), ('I', 6.25), ('D', 5.86), ('L', 4.97), ('C', 4.68),
    ('T', 4.63), ('U', 3.93), ('M', 3.15), ('P', 2.51), ('B', 1.42),
    ('G', 1.01), ('V', 0.90), ('Y', 0.90), ('Q', 0.88), ('H', 0.70),
    ('F', 0.69), ('Z', 0.52), ('J', 0.44), ('Ñ', 0.31), ('X', 0.22),
    ('K', 0.02), ('W', 0.01)
]

print("=== Análisis de Frecuencia Interactivo ===\n")

# Leer el texto cifrado desde frase.txt
try:
    with open("frase.txt", "r", encoding="utf-8") as f:
        texto_original = f.read()
except FileNotFoundError:
    print("❌ No se encontró el archivo 'frase.txt'")
    exit()

texto = texto_original.upper()
solo_letras = [c for c in texto if c.isalpha() or c == 'Ñ']

# Contar frecuencias
conteo = Counter(solo_letras)
total = sum(conteo.values())

if total == 0:
    print("❌ El archivo no contiene letras.")
    exit()

# Calcular porcentaje de aparición
frecuencias = {letra: (num / total) * 100 for letra, num in conteo.items()}
ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

print("Frecuencia de letras encontradas:\n")
for letra, freq in ordenadas:
    print(f"{letra}: {freq:.2f}%")

print("\n=== Sugerencias automáticas ===")
for i, (letra, _) in enumerate(ordenadas):
    if i < len(frecuencia_espanol):
        print(f"{letra} → {frecuencia_espanol[i][0]}")

# Diccionario de sustituciones (editable por el usuario)
sustituciones = {}

def aplicar_sustituciones(texto_original, sustituciones):
    resultado = ""
    for c in texto_original:
        upper = c.upper()
        if upper in sustituciones:
            nuevo = sustituciones[upper]
            resultado += nuevo if c.isupper() else nuevo.lower()
        else:
            resultado += c
    return resultado
# Bucle interactivo
print("\n--- Modo interactivo ---")
print("Escribe una sustitución en formato X=Y (ej: Q=E)")
print("Escribe 'ver' para mostrar el texto actual.")
print("Escribe 'guardar' para guardar y salir.")
print("Escribe 'borrar X' para eliminar una sustitución.\n")

while True:
    comando = input("👉 Sustitución: ").strip().upper()

    if comando == "GUARDAR":
        break
    elif comando == "VER":
        texto_sugerido = aplicar_sustituciones(texto_original, sustituciones)
        print("\n=== Texto actual ===")
        print(texto_sugerido)
        print("====================\n")
    elif comando.startswith("BORRAR "):
        letra = comando.split(" ")[1]
        if letra in sustituciones:
            del sustituciones[letra]
            print(f"🗑️  Sustitución de {letra} eliminada.")
        else:
            print(f"⚠️  No existe sustitución para {letra}.")
    elif "=" in comando:
        try:
            origen, destino = comando.split("=")
            origen, destino = origen.strip(), destino.strip()
            sustituciones[origen] = destino
            print(f"✅ Sustitución añadida: {origen} → {destino}")
        except ValueError:
            print("⚠️ Formato incorrecto. Usa X=Y")
    else:
        print("⚠️ Comando no reconocido. Usa VER, GUARDAR o X=Y")

# Aplicar y guardar resultado final
texto_final = aplicar_sustituciones(texto_original, sustituciones)
with open("frase_sugerida.txt", "w", encoding="utf-8") as f:
    f.write(texto_final)

print("\n✅ Resultado final guardado en 'frase_sugerida.txt'")
print("Sustituciones aplicadas:", sustituciones)