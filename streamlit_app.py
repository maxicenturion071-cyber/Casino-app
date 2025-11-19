# app.py - CASINOPRO COMPLETO PARA STREAMLIT
import streamlit as st
import json
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN MÓVIL
st.set_page_config(
    page_title="CasinoPro Móvil",
    page_icon="🎰",
    layout="centered",
    initial_sidebar_state="collapsed"  # Menú optimizado para móvil
)

# TÍTULO PRINCIPAL
st.title("🎰 CASINOPRO")
st.markdown("**Sistema Técnico Móvil**")
st.markdown("---")

# BASE DE DATOS
class CasinoProDB:
    def __init__(self):
        self.problemas_comunes = {
            "no enciende": {
                "solucion": "🔧 Verificar fuente de poder y fusibles",
                "tiempo": "15 min",
                "dificultad": "Baja",
                "herramientas": ["Multímetro", "Destornilladores"]
            },
            "error billetetero": {
                "solucion": "🧹 Limpiar sensores ópticos del aceptador",
                "tiempo": "30 min", 
                "dificultad": "Media",
                "herramientas": ["Aire comprimido", "Alcohol isopropílico"]
            },
            "pantalla negra": {
                "solucion": "📺 Revisar cable de video y backlight",
                "tiempo": "25 min",
                "dificultad": "Media", 
                "herramientas": ["Destornilladores", "Multímetro"]
            },
            "no acepta billetes": {
                "solucion": "💰 Calibrar y limpiar aceptador",
                "tiempo": "45 min",
                "dificultad": "Media",
                "herramientas": ["Kit limpieza MEI", "Software calibración"]
            }
        }
        
        self.inventario = [
            {"nombre": "🔌 Fuente IGT S2000", "stock": 3, "proveedor": "IGT Parts", "compatible": "IGT S2000/S Plus"},
            {"nombre": "📺 Display Touch", "stock": 2, "proveedor": "IGT Parts", "compatible": "IGT S2000/S Plus"},
            {"nombre": "💰 Aceptador MEI SCN66", "stock": 5, "proveedor": "MEI Professional", "compatible": "Todos"},
            {"nombre": "⚡ Fuente Aristocrat MK6", "stock": 1, "proveedor": "Aristocrat", "compatible": "Aristocrat MK6/MK5"},
            {"nombre": "🎯 Sensores Bola BCM", "stock": 8, "proveedor": "BCM Argentina", "compatible": "BCM RW-2000"}
        ]
        
        self.reparaciones = []

# INICIALIZAR BASE DE DATOS
if 'db' not in st.session_state:
    st.session_state.db = CasinoProDB()

# MENÚ PRINCIPAL MÓVIL
menu = st.selectbox(
    "📱 **SELECCIONÁ UNA OPCIÓN:**",
    ["🏠 INICIO", "🔍 DIAGNÓSTICO", "📦 INVENTARIO", "📝 NUEVA REPARACIÓN", "📊 HISTORIAL"]
)

st.markdown("---")

# PÁGINA DE INICIO
if menu == "🏠 INICIO":
    st.header("🏠 Bienvenido a CasinoPro")
    
    # Métricas rápidas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🔧 Problemas", len(st.session_state.db.problemas_comunes))
    with col2:
        st.metric("📦 Repuestos", len(st.session_state.db.inventario))
    with col3:
        st.metric("📝 Reparaciones", len(st.session_state.db.reparaciones))
    
    st.info("💡 **Consejo:** Usá el selector de arriba para navegar.")
    
    # Accesos rápidos
    st.subheader("🚀 Accesos Rápidos")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔍 Diagnóstico Rápido", use_container_width=True):
            st.session_state.menu_redirect = "🔍 DIAGNÓSTICO"
            
    with col2:
        if st.button("📦 Ver Inventario", use_container_width=True):
            st.session_state.menu_redirect = "📦 INVENTARIO"

# PÁGINA DE DIAGNÓSTICO
elif menu == "🔍 DIAGNÓSTICO":
    st.header("🔍 Diagnóstico Express")
    
    # Inputs optimizados para móvil
    modelo = st.text_input(
        "🎰 **MODELO DE MÁQUINA:**",
        placeholder="Ej: IGT S2000, BCM RW-2000, Aristocrat MK6..."
    )
    
    sintoma = st.selectbox(
        "🩺 **SÍNTOMA PRINCIPAL:**",
        ["Seleccionar...", "no enciende", "error billetetero", "pantalla negra", "no acepta billetes", "otro"]
    )
    
    detalles = st.text_area(
        "📝 **DETALLES ADICIONALES:**",
        placeholder="Describí el problema con más detalle...",
        height=100
    )
    
    # Botón de diagnóstico
    if st.button("🎯 EJECUTAR DIAGNÓSTICO", type="primary", use_container_width=True):
        if modelo and sintoma != "Seleccionar...":
            with st.spinner("🔍 Analizando problema..."):
                # Simular análisis
                import time
                time.sleep(1)
                
                # Mostrar resultados
                st.success("✅ **DIAGNÓSTICO COMPLETADO**")
                
                # Información de la máquina
                st.subheader("📋 Información de la Máquina")
                st.info(f"**Modelo:** {modelo.upper()}")
                if detalles:
                    st.info(f"**Detalles:** {detalles}")
                
                # Resultados del diagnóstico
                st.subheader("🛠️ Solución Recomendada")
                
                if sintoma in st.session_state.db.problemas_comunes:
                    problema = st.session_state.db.problemas_comunes[sintoma]
                    
                    st.success(f"**{problema['solucion']}**")
                    st.write(f"⏱️ **Tiempo estimado:** {problema['tiempo']}")
                    st.write(f"🎯 **Dificultad:** {problema['dificultad']}")
                    st.write(f"🧰 **Herramientas necesarias:** {', '.join(problema['herramientas'])}")
                    
                    # Pasos de la solución
                    st.subheader("📋 Pasos a Seguir:")
                    if sintoma == "no enciende":
                        st.write("1. 🔌 Desconectar alimentación eléctrica")
                        st.write("2. 🔍 Revisar fusibles en fuente de poder") 
                        st.write("3. 📏 Medir voltajes con multímetro")
                        st.write("4. 🔧 Reemplazar componentes defectuosos")
                        
                    elif sintoma == "error billetetero":
                        st.write("1. 🧹 Desconectar aceptador")
                        st.write("2. 💧 Limpiar sensores con alcohol isopropílico")
                        st.write("3. 🔧 Verificar rodillos de alimentación")
                        st.write("4. ⚙️ Ejecutar calibración desde menú servicio")
                        
                else:
                    st.warning("⚠️ **Problema no identificado**")
                    st.write("Recomendación: Contactar a soporte técnico especializado.")
                
                # Sugerir repuestos
                st.subheader("📦 Repuestos Recomendados")
                repuestos_sugeridos = []
                if "igt" in modelo.lower():
                    repuestos_sugeridos = ["Fuente IGT S2000", "Display Touch"]
                elif "bcm" in modelo.lower():
                    repuestos_sugeridos = ["Sensores Bola BCM"]
                
                for repuesto in repuestos_sugeridos:
                    for item in st.session_state.db.inventario:
                        if repuesto.lower() in item["nombre"].lower():
                            st.write(f"• **{item['nombre']}** - Stock: {item['stock']} unidades")
                
        else:
            st.error("❌ **Completá el modelo y seleccioná un síntoma**")

# PÁGINA DE INVENTARIO
elif menu == "📦 INVENTARIO":
    st.header("📦 Gestión de Inventario")
    
    # Buscador
    busqueda = st.text_input(
        "🔍 **BUSCAR REPUESTO:**",
        placeholder="Ej: fuente, display, sensor..."
    )
    
    # Filtros rápidos
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 Ver Todo", use_container_width=True):
            st.session_state.filtro_stock = "todo"
    with col2:
        if st.button("⚠️ Stock Bajo", use_container_width=True):
            st.session_state.filtro_stock = "bajo"
    
    # Mostrar inventario
    st.subheader("📊 Stock Disponible")
    
    for item in st.session_state.db.inventario:
        # Aplicar filtros de búsqueda
        if busqueda and busqueda.lower() not in item["nombre"].lower():
            continue
            
        if hasattr(st.session_state, 'filtro_stock'):
            if st.session_state.filtro_stock == "bajo" and item["stock"] > 2:
                continue
        
        # Mostrar item
        with st.expander(f"{item['nombre']} - **Stock: {item['stock']}**"):
            st.write(f"**Proveedor:** {item['proveedor']}")
            st.write(f"**Compatibilidad:** {item['compatible']}")
            
            # Indicador de stock
            if item["stock"] == 0:
                st.error("❌ **SIN STOCK - REPONER URGENTE**")
            elif item["stock"] <= 2:
                st.warning(f"⚠️ **STOCK BAJO** - Quedan {item['stock']} unidades")
            else:
                st.success(f"✅ **Stock suficiente** - {item['stock']} unidades")
    
    # Estadísticas
    total_repuestos = len(st.session_state.db.inventario)
    stock_bajo = sum(1 for item in st.session_state.db.inventario if item["stock"] <= 2)
    sin_stock = sum(1 for item in st.session_state.db.inventario if item["stock"] == 0)
    
    st.metric("📦 Total Repuestos", total_repuestos)
    if stock_bajo > 0:
        st.metric("⚠️ Stock Bajo", stock_bajo)
    if sin_stock > 0:
        st.metric("❌ Sin Stock", sin_stock)

# PÁGINA DE NUEVA REPARACIÓN
elif menu == "📝 NUEVA REPARACIÓN":
    st.header("📝 Registrar Nueva Reparación")
    
    with st.form("nueva_reparacion", clear_on_submit=True):
        # Campos del formulario
        modelo = st.text_input("🎰 **MODELO DE MÁQUINA:**", placeholder="IGT S2000, BCM RW-2000...")
        
        col1, col2 = st.columns(2)
        with col1:
            problema = st.selectbox(
                "🩺 **PROBLEMA:**",
                ["No enciende", "Error billetetero", "Pantalla negra", "Comunicación", "Otro"]
            )
        with col2:
            tecnico = st.text_input("👤 **TÉCNICO:**", placeholder="Tu nombre")
        
        solucion = st.text_area(
            "🛠️ **SOLUCIÓN APLICADA:**",
            placeholder="Describí paso a paso la solución aplicada...",
            height=120
        )
        
        # Botón de envío
        enviado = st.form_submit_button(
            "💾 GUARDAR REPARACIÓN", 
            type="primary", 
            use_container_width=True
        )
        
        if enviado:
            if all([modelo, problema, solucion, tecnico]):
                # Crear registro
                reparacion = {
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "modelo": modelo,
                    "problema": problema,
                    "solucion": solucion,
                    "tecnico": tecnico
                }
                
                st.session_state.db.reparaciones.append(reparacion)
                st.success("✅ **REPARACIÓN REGISTRADA EXITOSAMENTE**")
                st.balloons()
                
                # Mostrar resumen
                st.subheader("📋 Resumen de la Reparación")
                st.write(f"**Fecha:** {reparacion['fecha']}")
                st.write(f"**Máquina:** {reparacion['modelo']}")
                st.write(f"**Problema:** {reparacion['problema']}")
                st.write(f"**Solución:** {reparacion['solucion']}")
                st.write(f"**Técnico:** {reparacion['tecnico']}")
                
            else:
                st.error("❌ **COMPLETÁ TODOS LOS CAMPOS**")

# PÁGINA DE HISTORIAL
elif menu == "📊 HISTORIAL":
    st.header("📊 Historial de Reparaciones")
    
    if not st.session_state.db.reparaciones:
        st.info("📝 **Aún no hay reparaciones registradas**")
        st.write("Usá la opción 'Nueva Reparación' para comenzar a guardar tu trabajo.")
    else:
        # Mostrar últimas reparaciones
        for i, reparacion in enumerate(reversed(st.session_state.db.reparaciones[-5:]), 1):
            with st.expander(f"📋 {reparacion['fecha']} - {reparacion['modelo']}"):
                st.write(f"**Problema:** {reparacion['problema']}")
                st.write(f"**Solución:** {reparacion['solucion']}")
                st.write(f"**Técnico:** {reparacion['tecnico']}")
        
        # Estadísticas
        st.subheader("📈 Estadísticas")
        total_reparaciones = len(st.session_state.db.reparaciones)
        tecnicos = set(rep['tecnico'] for rep in st.session_state.db.reparaciones)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("📝 Total Reparaciones", total_reparaciones)
        with col2:
            st.metric("👥 Técnicos Activos", len(tecnicos))

# FOOTER
st.markdown("---")
st.caption("📱 **CasinoPro Mobile v1.0** - Desarrollado para técnicos profesionales")
st.caption("⚡ **Streamlit** + 🐍 **Python** + 🎰 **Experiencia Casino**")

# MANEJO DE REDIRECCIONES
if hasattr(st.session_state, 'menu_redirect'):
    st.experimental_set_query_params(menu=st.session_state.menu_redirect)
    del st.session_state.menu_redirect
