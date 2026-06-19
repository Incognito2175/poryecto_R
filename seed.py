from run import app
from app.database.database import db
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# Importaciones con las mayúsculas exactas de tus carpetas
from app.models.rol import Rol
from app.models.usuario import Usuario
from app.models.Inventario import Categoria, Prenda, Inventario, EstadoInventario


def sembrar_datos():
    with app.app_context():
        print("🔍 Verificando estado de la base de datos...")
        
        # 1. INSERCIÓN DE ROLES
        rol_admin = Rol.query.filter_by(nombre="Administrador").first()
        if not rol_admin:
            rol_admin = Rol(nombre="Administrador")
            rol_cliente = Rol(nombre="Cliente")
            db.session.add_all([rol_admin, rol_cliente])
            db.session.flush()
            print("✅ Roles registrados: Administrador y Cliente.")
        else:
            rol_cliente = Rol.query.filter_by(nombre="Cliente").first()

        # 2. INSERCIÓN DE USUARIOS CON CONTRASEÑA ENCRIPTADA (Bcrypt)
        usuario_check = Usuario.query.filter_by(correo="admin@rentstile.com").first()
        if not usuario_check:
            # Encriptamos las contraseñas convirtiéndolas en Hash antes de guardarlas
            pass_admin_hash = bcrypt.generate_password_hash("admin123").decode('utf-8')
            pass_cliente_hash = bcrypt.generate_password_hash("cliente123").decode('utf-8')

            admin_user = Usuario(
                idRol=rol_admin.idRol,
                nombre="Alejandro Administrador",
                documento="10203040",
                telefono="3001234567",
                correo="admin@rentstile.com",
                contrasena=pass_admin_hash,  # <-- GUARDA EL HASH SEGURO
                avatar="admin.png"
            )
            
            cliente_user = Usuario(
                idRol=rol_cliente.idRol,
                nombre="Camila Gomez",
                documento="50607080",
                telefono="3159876543",
                correo="camila@correo.com",
                contrasena=pass_cliente_hash,  # <-- GUARDA EL HASH SEGURO
                avatar="default.png"
            )
            db.session.add_all([admin_user, cliente_user])
            db.session.flush()
            print("✅ Usuarios registrados con contraseñas encriptadas mediante Bcrypt.")

        # 3. INSERCIÓN DE CATEGORÍAS
        cat_check = Categoria.query.filter_by(nombre="Vestidos de Gala").first()
        if not cat_check:
            categoria_gala = Categoria(nombre="Vestidos de Gala")
            categoria_coctel = Categoria(nombre="Vestidos de Cóctel")
            db.session.add_all([categoria_gala, categoria_coctel])
            db.session.flush()
            print("✅ Categorías registradas.")
        else:
            categoria_gala = cat_check

        # 4. INSERCIÓN DE PRENDAS Y UNIDADES
        prenda_check = Prenda.query.filter_by(nombre_prenda="Vestido Rojo Imperial").first()
        if not prenda_check:
            vestido_rojo = Prenda(
                idCategoria=categoria_gala.idCategoria,
                nombre_prenda="Vestido Rojo Imperial",
                descripcion="Vestido largo de satín con escote en V, ideal para graduaciones.",
                talla="M",
                color="Rojo",
                precio_alquiler=150000.00
            )
            db.session.add(vestido_rojo)
            db.session.flush()
            
            item_fisico1 = Inventario(
                idPrenda=vestido_rojo.idPrenda,
                codigo_interno="V-ROJO-001",
                estado=EstadoInventario.DISPONIBLE
            )
            db.session.add(item_fisico1)
            print("✅ Catálogo e inventario físico inicializados.")

        db.session.commit()
        print("🚀 ¡Todo listo! Datos de prueba encriptados guardados con éxito.")

if __name__ == '__main__':
    sembrar_datos()
