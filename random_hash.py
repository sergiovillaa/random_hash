import hashlib
import os

MAX_INTENTOS = 1000

for intento in range(1, MAX_INTENTOS + 1):
    # Generar bytes aleatorios
    data = os.urandom(32)

    # Crear hash (MD5 → 32 caracteres hex)
    hash_hex = hashlib.md5(data).hexdigest()

    print(f"Intento {intento}: {hash_hex}")

    # Verificar dos ceros consecutivos
    if "00" in hash_hex:
        print(f"\n✅ Encontrado '00' en el intento {intento}")
        break
else:
    print("\n❌ No se encontraron dos ceros consecutivos en 1000 intentos")
