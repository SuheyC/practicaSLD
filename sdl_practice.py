import json

# ============================================
# Cargar la base de conocimiento (recetas)
# ============================================
with open("recetas_completas.json", "r", encoding="utf-8") as f:
    recetas = json.load(f)

# ============================================
# Hechos base (tipos de ingredientes)
# ============================================
proteina_animal = [
    "pollo", "res", "cerdo", "pescado", "camaron", "huevo", "atun",
    "carne_res", "carne_molida", "chicharron", "pechuga", "pechugas",
    "filete", "pescado_blanco", "filete_de_pescado", "carne_de_cerdo",
    "carne_de_res", "milanesas_de_res", "carne"
]

proteina_vegetal = [
    "frijoles", "lentejas", "garbanzos", "soya", "tofu", "champiñones", "quinoa",
    "soya_texturizada", "frijoles_negros", "queso"
]

carbohidratos = [
    "arroz", "tortilla_de_maiz", "tortillas", "tortillas_de_maiz",
    "pan", "papa", "harina", "avena", "totopos", "tostadas",
    "harina_de_trigo", "maiz", "pan_molido", "masa_de_maiz",
    "arroz_integral", "pasta", "spaghetti", "bolillo", "maiz_pozolero"
]

verduras = [
    "lechuga", "tomate", "jitomate", "cebolla", "chile", "zanahoria",
    "calabaza", "berenjena", "espinaca", "pepino", "pimiento", "brocoli",
    "brocoli", "elote", "cilantro", "repollo", "limon", "limones", "pimiento_rojo",
    "pimiento_verde", "aguacate", "chiles_poblanos", "tomates_rojos",
    "tomates_verdes", "cebolla_morada", "aji", "calabacita", "calabacitas",
    "papas", "jitomates", "brócoli"
]

# ============================================
# Funciones de unificación (método SLD)
# ============================================

def unificar(x, y, sustitucion=None):
    if sustitucion is None:
        sustitucion = {}
    if x == y:
        return sustitucion
    if isinstance(x, str) and x[0].isupper():
        return unificar_var(x, y, sustitucion)
    if isinstance(y, str) and y[0].isupper():
        return unificar_var(y, x, sustitucion)
    return None

"""
# ===== Versión equivalente usando bucles (no recursiva) =====

def unificar_iterativo(x, y):
    sustitucion = {}
    pila = [(x, y)]  # se usa una pila para simular las llamadas recursivas

    while pila:
        a, b = pila.pop()
        if a == b:
            continue
        elif isinstance(a, str) and a[0].isupper():
            sustitucion[a] = b
        elif isinstance(b, str) and b[0].isupper():
            sustitucion[b] = a
        else:
            return None  # si no son iguales ni variables, no se puede unificar
    return sustitucion
"""

def unificar_var(var, valor, sustitucion):
    if var in sustitucion:
        return unificar(sustitucion[var], valor, sustitucion)
    elif isinstance(valor, str) and valor[0].isupper() and valor in sustitucion:
        return unificar(var, sustitucion[valor], sustitucion)
    else:
        nueva = sustitucion.copy()
        nueva[var] = valor
        return nueva
    
"""
# ===== Versión equivalente con bucles (no recursiva) =====

def unificar_var_iterativo(var, valor, sustitucion):
    nueva = sustitucion.copy()

    # Mientras el valor sea una variable presente en la sustitución,
    # seguimos "resolviendo" hasta encontrar un valor final.
    while isinstance(valor, str) and valor[0].isupper() and valor in nueva:
        valor = nueva[valor]

    nueva[var] = valor
    return nueva
"""

# ============================================
# Reglas (cláusulas de Horn)
# ============================================

def resolver_proteina_vegetal(receta):
    sustituciones = []
    for grupo, items in receta["ingredientes"].items():
        for ing in items.keys():
            base = ing.split("_")[0]
            for p in proteina_vegetal:
                subs = unificar(base, p)
                if subs is not None:
                    sustituciones.append(subs)
    return sustituciones


"""
def resolver_proteina_vegetal_recursivo(receta, grupos=None, sustituciones=None):
    # Inicializa los parámetros en la primera llamada
    if grupos is None:
        grupos = list(receta["ingredientes"].items())
    if sustituciones is None:
        sustituciones = []

    # Caso base: si no hay más grupos, termina la recursión
    if not grupos:
        return sustituciones

    # Toma el primer grupo y sus ingredientes
    grupo, items = grupos[0]
    for ing in items.keys():
        base = ing.split("_")[0]
        for p in proteina_vegetal:
            subs = unificar(base, p)
            if subs is not None:
                sustituciones.append(subs)

    # Llamada recursiva con el resto de los grupos
    return resolver_proteina_vegetal_recursivo(receta, grupos[1:], sustituciones)
"""

def resolver_proteina_animal(receta):
    sustituciones = []
    for grupo, items in receta["ingredientes"].items():
        for ing in items.keys():
            base = ing.split("_")[0]
            for p in proteina_animal:
                subs = unificar(base, p)
                if subs is not None:
                    sustituciones.append(subs)
    return sustituciones


"""
# ----------- Versión recursiva comentada -----------
def resolver_proteina_animal_recursivo(receta, grupos=None, sustituciones=None):
    if grupos is None:
        grupos = list(receta["ingredientes"].items())
    if sustituciones is None:
        sustituciones = []

    if not grupos:
        return sustituciones

    grupo, items = grupos[0]
    for ing in items.keys():
        base = ing.split("_")[0]
        for p in proteina_animal:
            subs = unificar(base, p)
            if subs is not None:
                sustituciones.append(subs)

    return resolver_proteina_animal_recursivo(receta, grupos[1:], sustituciones)
"""

def resolver_carbohidrato(receta):
    sustituciones = []
    for grupo, items in receta["ingredientes"].items():
        for ing in items.keys():
            base = ing.split("_")[0]
            for c in carbohidratos:
                subs = unificar(base, c)
                if subs is not None:
                    sustituciones.append(subs)
    return sustituciones

"""
# ----------- Versión recursiva comentada -----------
def resolver_carbohidrato_recursivo(receta, grupos=None, sustituciones=None):
    if grupos is None:
        grupos = list(receta["ingredientes"].items())
    if sustituciones is None:
        sustituciones = []

    if not grupos:
        return sustituciones

    grupo, items = grupos[0]
    for ing in items.keys():
        base = ing.split("_")[0]
        for c in carbohidratos:
            subs = unificar(base, c)
            if subs is not None:
                sustituciones.append(subs)

    return resolver_carbohidrato_recursivo(receta, grupos[1:], sustituciones)
"""

def resolver_verdura(receta):
    sustituciones = []
    for grupo, items in receta["ingredientes"].items():
        for ing in items.keys():
            base = ing.split("_")[0]
            for v in verduras:
                subs = unificar(base, v)
                if subs is not None:
                    sustituciones.append(subs)
    return sustituciones

"""
# ----------- Versión recursiva comentada -----------
def resolver_verdura_recursivo(receta, grupos=None, sustituciones=None):
    if grupos is None:
        grupos = list(receta["ingredientes"].items())
    if sustituciones is None:
        sustituciones = []

    if not grupos:
        return sustituciones

    grupo, items = grupos[0]
    for ing in items.keys():
        base = ing.split("_")[0]
        for v in verduras:
            subs = unificar(base, v)
            if subs is not None:
                sustituciones.append(subs)

    return resolver_verdura_recursivo(receta, grupos[1:], sustituciones)
"""

# ============================================
# Funciones principales
# ============================================

def es_vegetariana(nombre_receta):
    """Una receta es vegetariana si tiene proteína vegetal y no tiene proteína animal."""
    receta = recetas[nombre_receta]
    tiene_veg = bool(resolver_proteina_vegetal(receta))
    tiene_animal = bool(resolver_proteina_animal(receta))
    return tiene_veg and not tiene_animal

def es_completa(nombre_receta):
    """Una receta es completa si tiene proteína, carbohidrato y verdura."""
    receta = recetas[nombre_receta]
    tiene_proteina = bool(resolver_proteina_vegetal(receta) or resolver_proteina_animal(receta))
    tiene_carbo = bool(resolver_carbohidrato(receta))
    tiene_verdura = bool(resolver_verdura(receta))
    return tiene_proteina and tiene_carbo and tiene_verdura

# ============================================
# Programa principal (modo interactivo tipo SLD)
# ============================================

if __name__ == "__main__":
    print("=== Sistema de consulta de recetas (modo SLD) ===\n")
    
    while True:
        nombre = input("Escribe el nombre de la receta IGUAL QUE EN EL JSON (o 'salir' para terminar): ").strip()
        
        if nombre.lower() == "salir":
            print("\nPrograma finalizado. ¡Hasta pronto!")
            break
        
        if nombre not in recetas:
            print(f"La receta '{nombre}' no se encontró en la base de conocimiento.\n")
        else:
            vegetariana = es_vegetariana(nombre)
            completa = es_completa(nombre)
            print(f"\nResultados para '{nombre}':")
            print(f"  - Es vegetariana: {'Sí' if vegetariana else 'No'}")
            print(f"  - Es completa: {'Sí' if completa else 'No'}\n")

"""

# Versión RECURSIVA del bloque principal


def consultar_receta():
    # Se muestra el mensaje inicial una sola vez
    nombre = input("Escribe el nombre de la receta IGUAL QUE EN EL JSON (o 'salir' para terminar): ").strip()
    
    # Caso base de la recursión → condición de salida
    if nombre.lower() == "salir":
        print("\nPrograma finalizado. ¡Hasta pronto!")
        return  # termina la función (no hay más llamadas)
    
    # Si no existe la receta
    if nombre not in recetas:
        print(f"La receta '{nombre}' no se encontró en la base de conocimiento.\n")
    else:
        # Si existe, se consultan los resultados
        vegetariana = es_vegetariana(nombre)
        completa = es_completa(nombre)
        print(f"\nResultados para '{nombre}':")
        print(f"  - Es vegetariana: {'Sí' if vegetariana else 'No'}")
        print(f"  - Es completa: {'Sí' if completa else 'No'}\n")

    # Llamada recursiva: vuelve a preguntar al usuario
    consultar_receta()


# Ejecución del programa (reemplaza al while True)
if __name__ == "__main__":
    print("=== Sistema de consulta de recetas (modo SLD - versión recursiva) ===\n")
    consultar_receta()
"""
