import re

entradas_compradas = []

def mostrar_menu_principal():
    print("\n--- MENU PRINCIPAL - CONEJO SIMPATICO ---")
    print("""
1. Comprar entrada.
2. Consultar comprador.
3. Cancelar compra.
4.- Salir""") 
    print("--------------------------------------------------")

def comprar_entrada():
    print("\n--- COMPRAR ENTRADA ---")

    nombre_comprador = ""
    while True:
        nombre_comprador = input("Ingrese nombre del comprador: ").strip()
        if not nombre_comprador:
            print("El nombre del comprador no puede estar vacío.")
        else:
            nombre_existe = False
            for entrada in entradas_compradas:
                if entrada["nombre"].lower() == nombre_comprador.lower():
                    nombre_existe = True
                    break
            
            if nombre_existe:
                print("Error: El nombre del comprador ya existe. Debe ser único.")
            else:
                break

    tipo_entrada = ""
    while True:
        tipo_entrada = input("Ingrese tipo de entrada (G para General, V para VIP): ").strip().upper()
        if tipo_entrada == "G" or tipo_entrada == "V":
            break
        else:
            print("Tipo de entrada no válido. Solo se permite 'G' o 'V'.")

    codigo_confirmacion = ""
    while True:
        codigo_confirmacion = input("Ingrese código de confirmación (mín. 6 caracteres, 1 mayúscula, 1 número, sin espacios): ").strip()
        
        if len(codigo_confirmacion) < 6:
            print("El código de confirmación debe tener al menos 6 caracteres.")
        elif not re.search(r'[A-Z]', codigo_confirmacion):
            print("El código de confirmación debe contener al menos 1 letra mayúscula.")
        elif not re.search(r'\d', codigo_confirmacion):
            print("El código de confirmación debe contener al menos 1 número.")
        elif ' ' in codigo_confirmacion:
            print("El código de confirmación no puede tener espacios en blanco.")
        else:
            break

    nueva_entrada = {
        "nombre": nombre_comprador,
        "tipo": tipo_entrada,
        "codigo": codigo_confirmacion
    }
    entradas_compradas.append(nueva_entrada)
    print("\n¡Entrada registrada exitosamente!")

def consultar_comprador():
    print("\n--- CONSULTAR COMPRADOR ---")
    nombre_a_buscar = input("Ingrese el nombre del comprador a consultar: ").strip()

    comprador_encontrado = False
    for entrada in entradas_compradas:
        if entrada["nombre"].lower() == nombre_a_buscar.lower():
            print(f"\nDatos del comprador '{entrada['nombre']}':")
            print(f"Tipo de entrada: {entrada['tipo']}")
            print(f"Código de confirmación: {entrada['codigo']}")
            comprador_encontrado = True
            break
    
    if not comprador_encontrado:
        print("El comprador no se encuentra.")

def cancelar_compra():
    print("\n--- CANCELAR COMPRA ---")
    nombre_a_cancelar = input("Ingrese el nombre del comprador para cancelar la compra: ").strip()

    compra_cancelada = False
    for i, entrada in enumerate(entradas_compradas):
        if entrada["nombre"].lower() == nombre_a_cancelar.lower():
            del entradas_compradas[i]
            print("¡Compra cancelada!")
            compra_cancelada = True
            break
    
    if not compra_cancelada:
        print("No se pudo cancelar la compra.")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Ingrese su opción: ").strip()

        if opcion == '1':
            comprar_entrada()
        elif opcion == '2':
            consultar_comprador()
        elif opcion == '3':
            cancelar_compra()
        elif opcion == '4':
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    main()