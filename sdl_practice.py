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

def unificar_var(var, valor, sustitucion):
    if var in sustitucion:
        return unificar(sustitucion[var], valor, sustitucion)
    elif isinstance(valor, str) and valor[0].isupper() and valor in sustitucion:
        return unificar(var, sustitucion[valor], sustitucion)
    else:
        nueva = sustitucion.copy()
        nueva[var] = valor
        return nueva

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
