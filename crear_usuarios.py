from database import SessionLocal, Usuario

def registrar_usuarios():
    db = SessionLocal()
    
    # Lista de los nuevos usuarios para MARA INGENIEROS
    # Puedes cambiar los nombres y contraseñas por los reales aquí:
    nuevos_usuarios = [
        # --- Administradores ---
        {"nombre": "admin1", "password": "MaraAdmin2026*", "rol": "Gerencia"},
        {"nombre": "admin2", "password": "MaraAdmin2026#", "rol": "Gerencia"},
        
        # --- Operarios ---
        {"nombre": "operario1", "password": "MaraOp2026_1", "rol": "Operario"},
        {"nombre": "operario2", "password": "MaraOp2026_2", "rol": "Operario"},
        {"nombre": "operario3", "password": "MaraOp2026_3", "rol": "Operario"},
        {"nombre": "operario4", "password": "MaraOp2026_4", "rol": "Operario"},
    ]
    
    usuarios_creados = 0
    for u_data in nuevos_usuarios:
        # Verificar si el usuario ya existe para no duplicarlo
        existe = db.query(Usuario).filter(Usuario.nombre == u_data["nombre"]).first()
        if not existe:
            # Creamos el usuario vinculando los campos correspondientes a tu modelo
            nuevo_usuario = Usuario(
                nombre=u_data["nombre"],
                password_hash=u_data["password"], # Tu base de datos guarda la clave en este campo
                rol=u_data["rol"]
            )
            db.add(nuevo_usuario)
            usuarios_creados += 1
            print(f"✅ Usuario '{u_data['nombre']}' registrado con rol [{u_data['rol']}]")
        else:
            print(f"⚠️ El usuario '{u_data['nombre']}' ya existía en el sistema.")
            
    db.commit()
    db.close()
    print(f"\n🚀 Proceso terminado. Se crearon {usuarios_creados} nuevos usuarios con éxito.")

if __name__ == "__main__":
    registrar_usuarios()