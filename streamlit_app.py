# app.py - CASINOPRO COMPLETO CON TODO LO QUE DESARROLLAMOS
import streamlit as st
import json
import pandas as pd
from datetime import datetime
from difflib import SequenceMatcher

# CONFIGURACIÓN MÓVIL
st.set_page_config(
    page_title="CasinoPro Completo",
    page_icon="🎰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================== BASE DE DATOS COMPLETA ====================
class CasinoProCompleteDB:
    def __init__(self):
        # ========== MANUALES DE ACEPTADORES COMPLETOS ==========
        self.aceptadores = {
            "MEI SCN66 Advance": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador de Billetes de Alta Seguridad",
                "voltaje": "+24V DC ±5%",
                "consumo": "3.5A máximo",
                "comunicacion": "RS-232, MDB v4.0, USB 3.0, Ethernet",
                "billetes_aceptados": "MXN: Todas + USD: $1-$100 + EUR: €5-€500",
                "conectores": [
                    "CN1: 20-pin - Principal alta densidad",
                    "CN2: 8-pin - Comunicaciones avanzadas",
                    "CN3: 6-pin - Alimentación"
                ],
                "codigos_error": {
                    "SCN-001": "Spectrometer Calibration Lost",
                    "SCN-002": "Magnetic Sensor Array Failure", 
                    "SCN-003": "CMOS Camera Module Fault"
                },
                "problemas_comunes": [
                    "SCN-001 Error: Ejecutar recalibración espectrómetro",
                    "Falsos rechazos: Ajustar thresholds de confianza",
                    "Comunicación Ethernet: Verificar configuración VLAN"
                ]
            },
            "MEI CashFlow 7000": {
                "fabricante": "MEI (Crane Payment Innovations)", 
                "tipo": "Aceptador CashFlow Series",
                "voltaje": "+24V DC ±10%",
                "consumo": "2.8A máximo",
                "comunicacion": "RS-232, MDB, USB, Ethernet",
                "billetes_aceptados": "MXN: $20-$1000 | USD: $1-$100",
                "codigos_error": {
                    "CF-01": "CashFlow Sensor Error",
                    "CF-02": "Transport Mechanism Fault",
                    "CF-03": "Magnetic Sensor Error"
                },
                "problemas_comunes": [
                    "CF-01 Error: Limpiar cabezal validación completo",
                    "CF-04 Error: Verificar obstrucciones ruta óptica"
                ]
            },
            "JCM iVizion": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador con Visión Artificial", 
                "voltaje": "+24V DC ±10%",
                "consumo": "3.2A máximo",
                "comunicacion": "RS-232, MDB, Ethernet, WiFi",
                "billetes_aceptados": "Múltiples divisas + Billetes dañados",
                "codigos_error": {
                    "IV-100": "AI Vision System Failure",
                    "IV-101": "Neural Network Error",
                    "IV-102": "Camera Module Fault"
                },
                "problemas_comunes": [
                    "IV-100 Error: Reiniciar sistema IA completo",
                    "Falsos positivos: Re-entrenar modelo IA"
                ]
            }
        }

        # ========== MÁQUINAS TRAgamonedas COMPLETAS ==========
        self.maquinas = {
            "IGT S2000": {
                "fabricante": "International Game Technology",
                "año": 2010,
                "tipo": "Video Slot",
                "caracteristicas": ["MPU avanzado", "Display LCD", "Aceptador MEI"],
                "problemas_comunes": ["Fuente poder", "Display touch", "Comunicación MPU"]
            },
            "Aristocrat MK6": {
                "fabricante": "Aristocrat Technologies", 
                "año": 2008,
                "tipo": "Reel Slot",
                "caracteristicas": ["Sistema stepper", "Pantalla VFD", "Aceptador JCM"],
                "problemas_comunes": ["Motores stepper", "Fuente 28V", "Sensores reel"]
            },
            "Bally Alpha 2": {
                "fabricante": "Bally Technologies",
                "año": 2012, 
                "tipo": "Video Slot Multi-game",
                "caracteristicas": ["Plataforma Alpha 2", "Touch screen", "Sistema bonificación"],
                "problemas_comunes": ["Board CPU", "Touch screen", "Sistema audio"]
            },
            "Konami Concerto": {
                "fabricante": "Konami Gaming",
                "año": 2015,
                "tipo": "Cabinet Premium", 
                "caracteristicas": ["Display curva", "Audio surround", "Sistema concerto"],
                "problemas_comunes": ["Display LED", "Sistema audio", "Comunicación network"]
            }
        }

        # ========== INVENTARIO COMPLETO ==========
        self.inventario = [
            {"nombre": "🔌 Fuente IGT S2000", "stock": 3, "proveedor": "IGT Parts", "compatible": "IGT S2000/S Plus", "categoria": "Fuentes"},
            {"nombre": "📺 Display Touch IGT", "stock": 2, "proveedor": "IGT Parts", "compatible": "IGT S2000/S Plus", "categoria": "Displays"},
            {"nombre": "💰 Aceptador MEI SCN66", "stock": 5, "proveedor": "MEI Professional", "compatible": "Todos", "categoria": "Aceptadores"},
            {"nombre": "⚡ Fuente Aristocrat MK6", "stock": 1, "proveedor": "Aristocrat", "compatible": "Aristocrat MK6/MK5", "categoria": "Fuentes"},
            {"nombre": "🎯 Sensores Bola BCM", "stock": 8, "proveedor": "BCM Argentina", "compatible": "BCM RW-2000", "categoria": "Sensores"},
            {"nombre": "🖥️ MPU Board IGT S2000", "stock": 2, "proveedor": "IGT Parts", "compatible": "IGT S2000", "categoria": "Electrónica"},
            {"nombre": "🔊 Board Audio Bally", "stock": 4, "proveedor": "Bally Parts", "compatible": "Bally Alpha 2/Pro", "categoria": "Audio"},
            {"nombre": "🔄 Motores Stepper", "stock": 12, "proveedor": "Aristocrat", "compatible": "Aristocrat MK6/MK5", "categoria": "Mecánica"},
            {"nombre": "💡 Lámpara Display", "stock": 25, "proveedor": "Generic", "compatible": "Varios modelos", "categoria": "Iluminación"},
            {"nombre": "🔧 Kit Herramientas MEI", "stock": 3, "proveedor": "MEI Professional", "compatible": "Aceptadores MEI", "categoria": "Herramientas"}
        ]

        # ========== PROBLEMAS COMUNES COMPLETOS ==========
        self.problemas_comunes = {
            "no enciende": {
                "solucion": "🔧 Verificar fuente de poder y fusibles",
                "tiempo": "15-30 min",
                "dificultad": "Baja",
                "herramientas": ["Multímetro", "Destornilladores", "Probador fusibles"],
                "pasos": [
                    "1. 🔌 Desconectar alimentación eléctrica",
                    "2. 🔍 Revisar fusibles en fuente de poder",
                    "3. 📏 Medir voltajes +5V, +12V, +24V",
                    "4. 🔧 Reemplazar componentes defectuosos"
                ]
            },
            "error billetetero": {
                "solucion": "🧹 Limpiar y calibrar aceptador de billetes", 
                "tiempo": "30-45 min",
                "dificultad": "Media",
                "herramientas": ["Aire comprimido", "Alcohol isopropílico", "Kit limpieza MEI"],
                "pasos": [
                    "1. 🧹 Desconectar aceptador",
                    "2. 💧 Limpiar sensores con alcohol isopropílico", 
                    "3. 🔧 Verificar rodillos de alimentación",
                    "4. ⚙️ Ejecutar calibración desde menú servicio"
                ]
            },
            "pantalla negra": {
                "solucion": "📺 Revisar sistema de video y backlight",
                "tiempo": "25-40 min", 
                "dificultad": "Media",
                "herramientas": ["Destornilladores", "Multímetro", "Probador LVDS"],
                "pasos": [
                    "1. 🔌 Verificar cable LVDS/Video",
                    "2. ⚡ Medir voltaje backlight/inversor",
                    "3. 🔍 Revisar tarjeta de video",
                    "4. 📏 Probar display con fuente externa"
                ]
            },
            "no acepta billetes": {
                "solucion": "💰 Revisar y calibrar sistema de aceptación",
                "tiempo": "45-60 min",
                "dificultad": "Media-Alta",
                "herramientas": ["Kit limpieza MEI/JCM", "Software calibración", "Multímetro"],
                "pasos": [
                    "1. 🔧 Verificar señal ENABLE del aceptador",
                    "2. 🧹 Limpiar sensores de entrada",
                    "3. ⚙️ Calibrar thresholds de aceptación", 
                    "4. 🔄 Actualizar base datos de seguridad"
                ]
            },
            "comunicacion error": {
                "solucion": "📡 Revisar cables y configuración comunicación",
                "tiempo": "20-35 min",
                "dificultad": "Media", 
                "herramientas": ["Multímetro", "Probador RS-232", "Cables patch"],
                "pasos": [
                    "1. 🔌 Verificar cableado MDB/RS-232",
                    "2. ⚡ Comprobar voltajes de alimentación",
                    "3. 🔧 Revisar configuración protocolo",
                    "4. 🔄 Reiniciar controlador y aceptador"
                ]
            },
            "ruido mecanico": {
                "solucion": "🔊 Lubricar y ajustar componentes mecánicos",
                "tiempo": "30-50 min",
                "dificultad": "Media",
                "herramientas": ["Lubricante específico", "Destornilladores", "Aire comprimido"],
                "pasos": [
                    "1. 🔍 Identificar fuente del ruido",
                    "2. 💧 Lubricar mecanismos (solo lubricante autorizado)",
                    "3. 🔧 Ajustar tensión de rodillos/motores",
                    "4. 🧹 Limpiar área de trabajo"
                ]
            }
        }

        # ========== RULETAS BCM ==========
        self.ruletas = {
            "BCM ARISTOCRAT RW-2000": {
                "tipo": "Ruleta Electrónica Profesional",
                "fabricante": "BCM (Bally Manufacturing)", 
                "voltaje": "220V AC 50Hz",
                "caracteristicas": ["Rueda mecánica precisión", "Sistema apuestas digital", "Display LCD 42\""],
                "codigos_error": {
                    "BCM-001": "Error sensor de bola - Limpiar sensores ópticos",
                    "BCM-002": "Fallo encoder rueda - Recalibrar encoder",
                    "BCM-003": "Comunicación display - Verificar cable LVDS"
                }
            },
            "BCM iDECK ROULETTE": {
                "tipo": "Ruleta Sistema Apuestas Avanzado",
                "fabricante": "BCM (Bally Manufacturing)",
                "voltaje": "220V AC ±10%", 
                "caracteristicas": ["Sistema iDeck touch", "Pantalla multi-touch 55\"", "Gestión límites apuesta"],
                "codigos_error": {
                    "BCM-101": "Error touch screen - Calibrar pantalla",
                    "BCM-102": "Sistema apuestas offline - Reiniciar módulo"
                }
            }
        }

        self.reparaciones = []

# INICIALIZAR BASE DE DATOS COMPLETA
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

# ==================== INTERFAZ PRINCIPAL ====================
st.title("🎰 CASINOPRO - SISTEMA COMPLETO")
st.markdown("**Versión Completa con Todo el Contenido**")
st.markdown("---")

# MENÚ PRINCIPAL MEJORADO
menu = st.selectbox(
    "📱 **SELECCIONÁ UNA OPCIÓN:**",
    [
        "🏠 INICIO", 
        "🔍 DIAGNÓSTICO AVANZADO", 
        "💰 MANUALES ACEPTADORES",
        "🎰 MÁQUINAS REGISTRADAS", 
        "📦 INVENTARIO COMPLETO",
        "🎲 RULETAS BCM",
        "📝 NUEVA REPARACIÓN", 
        "📊 HISTORIAL COMPLETO"
    ]
)

st.markdown("---")

# ==================== PÁGINA DE INICIO ====================
if menu == "🏠 INICIO":
    st.header("🏠 Dashboard Completo")
    
    # Métricas completas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🔧 Problemas", len(st.session_state.db.problemas_comunes))
    with col2:
        st.metric("💰 Aceptadores", len(st.session_state.db.aceptadores))
    with col3:
        st.metric("🎰 Máquinas", len(st.session_state.db.maquinas))
    with col4:
        st.metric("📦 Repuestos", len(st.session_state.db.inventario))
    
    # Resumen rápido
    st.subheader("🚀 Acceso Rápido")
    cols = st.columns(4)
    with cols[0]:
        if st.button("🔍 Diagnóstico", use_container_width=True):
            st.session_state.menu_redirect = "🔍 DIAGNÓSTICO AVANZADO"
    with cols[1]:
        if st.button("💰 Aceptadores", use_container_width=True):
            st.session_state.menu_redirect = "💰 MANUALES ACEPTADORES"
    with cols[2]:
        if st.button("🎰 Máquinas", use_container_width=True):
            st.session_state.menu_redirect = "🎰 MÁQUINAS REGISTRADAS"
    with cols[3]:
        if st.button("📦 Inventario", use_container_width=True):
            st.session_state.menu_redirect = "📦 INVENTARIO COMPLETO"
    
    # Estadísticas avanzadas
    st.subheader("📊 Estadísticas del Sistema")
    
    total_stock = sum(item['stock'] for item in st.session_state.db.inventario)
    stock_bajo = sum(1 for item in st.session_state.db.inventario if item['stock'] <= 2)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📦 Total Stock", total_stock)
    with col2:
        st.metric("⚠️ Stock Bajo", stock_bajo)
    with col3:
        st.metric("📝 Reparaciones", len(st.session_state.db.reparaciones))

# ==================== DIAGNÓSTICO AVANZADO ====================
elif menu == "🔍 DIAGNÓSTICO AVANZADO":
    st.header("🔍 Diagnóstico Avanzado")
    
    # Selección de máquina
    modelo = st.selectbox(
        "🎰 **SELECCIONÁ EL MODELO:**",
        ["Seleccionar..."] + list(st.session_state.db.maquinas.keys()) + ["Otro modelo"]
    )
    
    if modelo == "Otro modelo":
        modelo = st.text_input("✍️ **ESCRIBÍ EL MODELO:**", placeholder="Modelo específico...")
    
    # Síntomas
    sintoma = st.selectbox(
        "🩺 **SÍNTOMA PRINCIPAL:**",
        ["Seleccionar..."] + list(st.session_state.db.problemas_comunes.keys())
    )
    
    detalles = st.text_area(
        "📝 **DETALLES ADICIONALES:**",
        placeholder="Describí el problema con más detalle, códigos de error, etc...",
        height=100
    )
    
    if st.button("🎯 EJECUTAR DIAGNÓSTICO COMPLETO", type="primary", use_container_width=True):
        if modelo and modelo != "Seleccionar..." and sintoma and sintoma != "Seleccionar...":
            with st.spinner("🔍 Analizando problema con base de datos completa..."):
                import time
                time.sleep(2)
                
                st.success("✅ **DIAGNÓSTICO COMPLETADO**")
                
                # Información extendida
                st.subheader("📋 Información de la Máquina")
                if modelo in st.session_state.db.maquinas:
                    maquina_info = st.session_state.db.maquinas[modelo]
                    st.info(f"**Fabricante:** {maquina_info['fabricante']}")
                    st.info(f"**Tipo:** {maquina_info['tipo']}")
                    st.info(f"**Año:** {maquina_info['año']}")
                
                # Diagnóstico principal
                st.subheader("🛠️ Diagnóstico y Solución")
                if sintoma in st.session_state.db.problemas_comunes:
                    problema = st.session_state.db.problemas_comunes[sintoma]
                    
                    st.success(f"**{problema['solucion']}**")
                    st.write(f"⏱️ **Tiempo estimado:** {problema['tiempo']}")
                    st.write(f"🎯 **Dificultad:** {problema['dificultad']}")
                    st.write(f"🧰 **Herramientas necesarias:** {', '.join(problema['herramientas'])}")
                    
                    # Pasos detallados
                    st.subheader("📋 Pasos Detallados:")
                    for paso in problema['pasos']:
                        st.write(paso)
                    
                    # Repuestos recomendados basados en modelo y síntoma
                    st.subheader("📦 Repuestos Recomendados")
                    repuestos_recomendados = []
                    
                    if "fuente" in sintoma.lower() or "enciende" in sintoma.lower():
                        repuestos_recomendados.extend(["Fuente IGT S2000", "Fuente Aristocrat MK6"])
                    if "pantalla" in sintoma.lower() or "display" in sintoma.lower():
                        repuestos_recomendados.extend(["Display Touch IGT", "Lámpara Display"])
                    if "billete" in sintoma.lower():
                        repuestos_recomendados.extend(["Aceptador MEI SCN66", "Kit Herramientas MEI"])
                    
                    for repuesto in repuestos_recomendados:
                        for item in st.session_state.db.inventario:
                            if repuesto.lower() in item["nombre"].lower():
                                status = "✅" if item['stock'] > 2 else "⚠️" if item['stock'] > 0 else "❌"
                                st.write(f"{status} **{item['nombre']}** - Stock: {item['stock']} unidades")
                
                else:
                    st.warning("⚠️ **Problema no identificado en base de datos**")
                    st.write("**Recomendación:** Contactar a soporte técnico especializado o revisar manuales específicos.")
        
        else:
            st.error("❌ **Completá todos los campos obligatorios**")

# ==================== MANUALES ACEPTADORES ====================
elif menu == "💰 MANUALES ACEPTADORES":
    st.header("💰 Manuales de Aceptadores")
    
    aceptador_seleccionado = st.selectbox(
        "🔧 **SELECCIONÁ EL ACEPTADOR:**",
        list(st.session_state.db.aceptadores.keys())
    )
    
    if aceptador_seleccionado:
        info = st.session_state.db.aceptadores[aceptador_seleccionado]
        
        st.subheader(f"📋 {aceptador_seleccionado}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Fabricante:** {info['fabricante']}")
            st.info(f"**Tipo:** {info['tipo']}")
            st.info(f"**Voltaje:** {info['voltaje']}")
        with col2:
            st.info(f"**Consumo:** {info['consumo']}")
            st.info(f"**Comunicación:** {info['comunicacion']}")
        
        # Billetes aceptados
        st.subheader("💵 Billetes Aceptados")
        st.write(info['billetes_aceptados'])
        
        # Conectores
        st.subheader("🔌 Conectores")
        for conector in info['conectores']:
            st.write(f"• {conector}")
        
        # Códigos de error
        st.subheader("❌ Códigos de Error")
        for codigo, descripcion in info['codigos_error'].items():
            st.write(f"**{codigo}:** {descripcion}")
        
        # Problemas comunes
        st.subheader("⚠️ Problemas Comunes y Soluciones")
        for problema in info['problemas_comunes']:
            st.write(f"• {problema}")

# ==================== MÁQUINAS REGISTRADAS ====================
elif menu == "🎰 MÁQUINAS REGISTRADAS":
    st.header("🎰 Máquinas en Base de Datos")
    
    for modelo, info in st.session_state.db.maquinas.items():
        with st.expander(f"🎰 {modelo} - {info['fabricante']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Tipo:** {info['tipo']}")
                st.write(f"**Año:** {info['año']}")
            with col2:
                st.write(f"**Fabricante:** {info['fabricante']}")
            
            st.subheader("⭐ Características")
            for caracteristica in info['caracteristicas']:
                st.write(f"• {caracteristica}")
            
            st.subheader("🔧 Problemas Comunes")
            for problema in info['problemas_comunes']:
                st.write(f"• {problema}")

# ==================== INVENTARIO COMPLETO ====================
elif menu == "📦 INVENTARIO COMPLETO":
    st.header("📦 Inventario Completo")
    
    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        categoria = st.selectbox(
            "📂 Filtrar por categoría:",
            ["Todas"] + list(set(item['categoria'] for item in st.session_state.db.inventario))
        )
    with col2:
        busqueda = st.text_input("🔍 Buscar por nombre:", placeholder="fuente, display, sensor...")
    
    # Estadísticas de inventario
    total_items = len(st.session_state.db.inventario)
    total_stock = sum(item['stock'] for item in st.session_state.db.inventario)
    items_sin_stock = sum(1 for item in st.session_state.db.inventario if item['stock'] == 0)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📦 Total Items", total_items)
    with col2:
        st.metric("🔢 Total Stock", total_stock)
    with col3:
        st.metric("❌ Sin Stock", items_sin_stock)
    
    # Mostrar inventario filtrado
    st.subheader("📊 Stock Detallado")
    
    for item in st.session_state.db.inventario:
        # Aplicar filtros
        if categoria != "Todas" and item['categoria'] != categoria:
            continue
        if busqueda and busqueda.lower() not in item['nombre'].lower():
            continue
        
        # Determinar emoji de estado
        if item['stock'] == 0:
            estado = "❌"
            color = "red"
        elif item['stock'] <= 2:
            estado = "⚠️" 
            color = "orange"
        else:
            estado = "✅"
            color = "green"
        
        with st.expander(f"{estado} {item['nombre']} - Stock: {item['stock']}"):
            st.write(f"**Categoría:** {item['categoria']}")
            st.write(f"**Proveedor:** {item['proveedor']}")
            st.write(f"**Compatibilidad:** {item['compatible']}")
            
            # Barra de stock visual
            stock_max = max(10, item['stock'] + 2)  # Para visualización
            porcentaje = (item['stock'] / stock_max) * 100
            
            if item['stock'] == 0:
                st.error("**URGENTE: REPONER STOCK**")
            elif item['stock'] <= 2:
                st.warning(f"**STOCK BAJO** - Quedan {item['stock']} unidades")
            else:
                st.success(f"**Stock suficiente** - {item['stock']} unidades")

# ==================== RULETAS BCM ====================
elif menu == "🎲 RULETAS BCM":
    st.header("🎲 Ruletas BCM")
    
    ruleta_seleccionada = st.selectbox(
        "🎯 **SELECCIONÁ LA RULETA:**",
        list(st.session_state.db.ruletas.keys())
    )
    
    if ruleta_seleccionada:
        info = st.session_state.db.ruletas[ruleta_seleccionada]
        
        st.subheader(f"📋 {ruleta_seleccionada}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Tipo:** {info['tipo']}")
            st.info(f"**Fabricante:** {info['fabricante']}")
        with col2:
            st.info(f"**Voltaje:** {info['voltaje']}")
        
        # Características
        st.subheader("⭐ Características")
        for caracteristica in info['caracteristicas']:
            st.write(f"• {caracteristica}")
        
        # Códigos de error
        st.subheader("❌ Códigos de Error")
        for codigo, solucion in info['codigos_error'].items():
            st.write(f"**{codigo}:** {solucion}")

# ==================== NUEVA REPARACIÓN ====================
elif menu == "📝 NUEVA REPARACIÓN":
    st.header("📝 Registrar Nueva Reparación")
    
    with st.form("nueva_reparacion_completa", clear_on_submit=True):
        st.subheader("📋 Datos de la Reparación")
        
        col1, col2 = st.columns(2)
        with col1:
            modelo = st.selectbox(
                "🎰 Modelo de Máquina:",
                ["Seleccionar..."] + list(st.session_state.db.maquinas.keys()) + ["Otro"]
            )
            if modelo == "Otro":
                modelo = st.text_input("✍️ Especificar modelo:")
        with col2:
            tecnico = st.text_input("👤 Técnico Responsable:")
        
        problema = st.selectbox(
            "🩺 Tipo de Problema:",
            ["Seleccionar..."] + list(st.session_state.db.problemas_comunes.keys()) + ["Otro"]
        )
        if problema == "Otro":
            problema = st.text_input("✍️ Describir problema:")
        
        solucion = st.text_area(
            "🛠️ Solución Aplicada:",
            placeholder="Describí detalladamente la solución aplicada, repuestos usados, tiempo invertido...",
            height=120
        )
        
        observaciones = st.text_area(
            "📝 Observaciones:",
            placeholder="Observaciones adicionales, recomendaciones, etc...",
            height=80
        )
        
        enviado = st.form_submit_button("💾 GUARDAR REPARACIÓN COMPLETA", type="primary", use_container_width=True)
        
        if enviado:
            if all([modelo, problema, solucion, tecnico]) and modelo != "Seleccionar..." and problema != "Seleccionar...":
                reparacion = {
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "modelo": modelo,
                    "problema": problema,
                    "solucion": solucion,
                    "tecnico": tecnico,
                    "observaciones": observaciones
                }
                
                st.session_state.db.reparaciones.append(reparacion)
                st.success("✅ **REPARACIÓN REGISTRADA EXITOSAMENTE**")
                st.balloons()
                
                # Mostrar resumen completo
                st.subheader("📋 Resumen de la Reparación")
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Fecha:** {reparacion['fecha']}")
                    st.write(f"**Máquina:** {reparacion['modelo']}")
                with col2:
                    st.write(f"**Problema:** {reparacion['problema']}")
                    st.write(f"**Técnico:** {reparacion['tecnico']}")
                
                st.write(f"**Solución:** {reparacion['solucion']}")
                if observaciones:
                    st.write(f"**Observaciones:** {reparacion['observaciones']}")
                
            else:
                st.error("❌ **COMPLETÁ TODOS LOS CAMPOS OBLIGATORIOS**")

# ==================== HISTORIAL COMPLETO ====================
elif menu == "📊 HISTORIAL COMPLETO":
    st.header("📊 Historial Completo de Reparaciones")
    
    if not st.session_state.db.reparaciones:
        st.info("📝 **Aún no hay reparaciones registradas**")
        st.write("Usá la opción 'Nueva Reparación' para comenzar a guardar tu trabajo.")
    else:
        # Filtros para el historial
        col1, col2 = st.columns(2)
        with col1:
            filtro_tecnico = st.selectbox(
                "👤 Filtrar por técnico:",
                ["Todos"] + list(set(rep['tecnico'] for rep in st.session_state.db.reparaciones))
            )
        with col2:
            filtro_modelo = st.selectbox(
                "🎰 Filtrar por máquina:",
                ["Todas"] + list(set(rep['modelo'] for rep in st.session_state.db.reparaciones))
            )
        
        # Aplicar filtros
        reparaciones_filtradas = st.session_state.db.reparaciones.copy()
        if filtro_tecnico != "Todos":
            reparaciones_filtradas = [rep for rep in reparaciones_filtradas if rep['tecnico'] == filtro_tecnico]
        if filtro_modelo != "Todas":
            reparaciones_filtradas = [rep for rep in reparaciones_filtradas if rep['modelo'] == filtro_modelo]
        
        # Mostrar reparaciones filtradas
        st.subheader(f"📋 Reparaciones Encontradas: {len(reparaciones_filtradas)}")
        
        for i, reparacion in enumerate(reversed(reparaciones_filtradas), 1):
            with st.expander(f"🔧 {i}. {reparacion['fecha']} - {reparacion['modelo']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Fecha:** {reparacion['fecha']}")
                    st.write(f"**Máquina:** {reparacion['modelo']}")
                with col2:
                    st.write(f"**Problema:** {reparacion['problema']}")
                    st.write(f"**Técnico:** {reparacion['tecnico']}")
                
                st.write(f"**Solución aplicada:** {reparacion['solucion']}")
                if reparacion.get('observaciones'):
                    st.write(f"**Observaciones:** {reparacion['observaciones']}")
        
        # Estadísticas del historial
        st.subheader("📈 Estadísticas del Historial")
        total_reparaciones = len(st.session_state.db.reparaciones)
        tecnicos_unicos = len(set(rep['tecnico'] for rep in st.session_state.db.reparaciones))
        modelos_unicos = len(set(rep['modelo'] for rep in st.session_state.db.reparaciones))
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📝 Total Reparaciones", total_reparaciones)
        with col2:
            st.metric("👥 Técnicos", tecnicos_unicos)
        with col3:
            st.metric("🎰 Modelos Diferentes", modelos_unicos)

# FOOTER COMPLETO
st.markdown("---")
st.caption("🎰 **CasinoPro Complete v2.0** - Sistema Técnico Integral para Casinos")
st.caption("📱 **Streamlit** + 🐍 **Python** + 💰 **Aceptadores** + 🎲 **Ruletas** + 🔧 **Diagnóstico Avanzado**")

# Manejo de redirecciones
if hasattr(st.session_state, 'menu_redirect'):
    st.experimental_set_query_params(menu=st.session_state.menu_redirect)
    del st.session_state.menu_redirect
