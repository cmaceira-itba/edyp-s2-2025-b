import cv2
import numpy as np
import time

def demostrar_ventajas_numpy():
    """
    Demuestra las ventajas de vectorización de numpy vs loops de Python
    para operaciones de procesamiento de imágenes
    """

    # Cargar imagen
    imagen = cv2.imread('imagen.jpg')
    if imagen is None:
        # np.random.randint: Genera array de enteros aleatorios
        # Parámetros: (min, max, shape, dtype)
        # shape=(1920, 1080, 3) crea una imagen de 1920x1080 con 3 canales (BGR)
        imagen = np.random.randint(0, 255, (1920, 1080, 3), dtype=np.uint8)

    # imagen.shape: tupla con dimensiones del array (alto, ancho, canales)
    # [:2] toma solo los primeros 2 elementos (alto y ancho)
    alto, ancho = imagen.shape[:2]

    # cv2.split: separa los 3 canales de la imagen en 3 arrays numpy independientes
    # Retorna una tupla de arrays 2D, cada uno representando un canal (B, G, R)
    azul, verde, rojo = cv2.split(imagen)

    print(f"Tamaño de imagen: {imagen.shape}")
    print(f"Procesando {alto * ancho * 3:,} píxeles\n")

    # === Operación 1: Inversión de canal con numpy ===
    inicio = time.perf_counter()

    # OPERACIÓN VECTORIZADA: 255 - rojo
    # Numpy aplica la resta a CADA elemento del array simultáneamente
    # No hay loops explícitos, el operador '-' está sobrecargado para arrays
    # Internamente usa instrucciones SIMD del CPU para procesar múltiples píxeles a la vez
    rojo_invertido = 255 - rojo

    tiempo_numpy = time.perf_counter() - inicio
    print(f"Inversión con numpy: {tiempo_numpy*1000:.2f}ms")

    # Misma operación con loops de Python (sobre subset para evitar timeout)
    # .copy(): crea una copia independiente del array, no una vista
    subconjunto = rojo[:100, :100].copy()
    inicio = time.perf_counter()

    # LOOP TRADICIONAL: procesa pixel por pixel secuencialmente
    # Mucho más lento porque Python interpreta cada iteración
    for i in range(subconjunto.shape[0]):
        for j in range(subconjunto.shape[1]):
            subconjunto[i, j] = 255 - subconjunto[i, j]

    tiempo_loop = time.perf_counter() - inicio

    # Extrapolar a imagen completa
    ratio_pixeles = (alto * ancho) / (100 * 100)
    tiempo_loop_estimado = tiempo_loop * ratio_pixeles
    print(f"Inversión con loops (extrapolado): {tiempo_loop_estimado*1000:.2f}ms")
    print(f"Aceleración: {tiempo_loop_estimado/tiempo_numpy:.0f}x\n")

    # === Operación 2: Ajuste de brillo usando broadcasting ===
    factor_brillo = 1.3
    inicio = time.perf_counter()

    # BROADCASTING: imagen * factor_brillo
    # El escalar 1.3 se "transmite" automáticamente a cada elemento del array
    # Numpy expande conceptualmente 1.3 a un array del mismo tamaño que imagen
    # y luego multiplica elemento por elemento
    #
    # np.clip(array, min, max): limita valores al rango [min, max]
    # Evita que los píxeles excedan 255 o sean menores a 0
    #
    # .astype(np.uint8): convierte el resultado de float64 a uint8 (0-255)
    mas_brillante = np.clip(imagen * factor_brillo, 0, 255).astype(np.uint8)

    tiempo_broadcast = time.perf_counter() - inicio
    print(f"Ajuste de brillo (broadcasting): {tiempo_broadcast*1000:.2f}ms")

    # === Operación 3: Crear visualizaciones RGB ===

    # np.zeros_like(imagen): crea un array de ceros con la misma forma y tipo que imagen
    # Esto genera una imagen negra (todos los píxeles en 0)
    solo_rojo = np.zeros_like(imagen)

    # INDEXACIÓN AVANZADA: solo_rojo[:, :, 2]
    # [:, :, 2] significa: todas las filas, todas las columnas, canal 2 (rojo en BGR)
    # Asignar 'rojo' a este slice copia todos los valores del canal rojo
    # Los canales 0 y 1 quedan en 0 (negro)
    solo_rojo[:, :, 2] = rojo

    # Solo canal verde (canal índice 1)
    solo_verde = np.zeros_like(imagen)
    solo_verde[:, :, 1] = verde

    # Solo canal azul (canal índice 0)
    solo_azul = np.zeros_like(imagen)
    solo_azul[:, :, 0] = azul

    # === Operación 4: Máscara booleana - aislar píxeles brillantes ===
    inicio = time.perf_counter()

    # COMPARACIÓN VECTORIZADA: imagen > 200
    # Retorna un array booleano de la misma forma que imagen
    # True donde el píxel es > 200, False en caso contrario
    #
    # .all(axis=2): verifica si TODOS los canales son True a lo largo del axis 2 (canales)
    # axis=2 reduce las dimensiones de (alto, ancho, 3) a (alto, ancho)
    # Resultado: array 2D booleano donde True indica que R, G y B son todos > 200
    mascara_brillante = (imagen > 200).all(axis=2)

    resaltado = imagen.copy()

    # INDEXACIÓN BOOLEANA: resaltado[~mascara_brillante]
    # ~ es el operador NOT bit a bit, invierte la máscara booleana
    # Esta indexación selecciona SOLO los píxeles donde mascara_brillante es False
    # Luego aplica // 3 (división entera) solo a esos píxeles
    # Es como un "if" vectorizado sin escribir loops
    resaltado[~mascara_brillante] = resaltado[~mascara_brillante] // 3

    tiempo_mascara = time.perf_counter() - inicio
    print(f"Operación con máscara booleana: {tiempo_mascara*1000:.2f}ms\n")

    # === Operación 5: Combinación ponderada de canales ===
    inicio = time.perf_counter()

    # np.array: crea un array numpy desde una lista Python
    # Estos pesos corresponden a la percepción humana de luminosidad
    pesos = np.array([0.114, 0.587, 0.299])  # Pesos BGR para luminosidad

    # np.dot(imagen, pesos): PRODUCTO PUNTO vectorizado
    # Para cada píxel (B, G, R), calcula: B*0.114 + G*0.587 + R*0.299
    # Es equivalente a un loop que multiplica y suma, pero mucho más rápido
    # Resultado: array 2D (alto, ancho) con valores de escala de grises
    escala_grises = np.dot(imagen, pesos).astype(np.uint8)

    tiempo_dot = time.perf_counter() - inicio
    print(f"Escala de grises ponderada (producto punto): {tiempo_dot*1000:.2f}ms")

    # Mostrar resultados
    cv2.imshow('Original', imagen)
    cv2.imshow('Canal Rojo', solo_rojo)
    cv2.imshow('Canal Verde', solo_verde)
    cv2.imshow('Canal Azul', solo_azul)

    # cv2.merge: operación inversa a cv2.split
    # Combina 3 arrays 2D en un array 3D de 3 canales
    cv2.imshow('Rojo Invertido', cv2.merge([azul, verde, rojo_invertido]))
    cv2.imshow('Mas Brillante', mas_brillante)
    cv2.imshow('Areas Brillantes Resaltadas', resaltado)
    cv2.imshow('Escala de Grises Personalizada', escala_grises)

    print("\nPresiona cualquier tecla para cerrar las ventanas")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Retornar métricas para gráficos potenciales
    return {
        'tiempo_numpy': tiempo_numpy,
        'tiempo_loop': tiempo_loop_estimado,
        'aceleracion': tiempo_loop_estimado / tiempo_numpy
    }

if __name__ == "__main__":
    demostrar_ventajas_numpy()
