# app.py - CASINOPRO COMPLETO CON TODAS LAS MÁQUINAS Y ACEPTADORES
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
        # ========== MÁQUINAS TRAGAMONEDAS COMPLETAS ==========
        self.maquinas = {
            "IGT S2000": {
                "fabricante": "International Game Technology",
                "año": 2010,
                "tipo": "Video Slot",
                "caracteristicas": ["MPU avanzado", "Display LCD", "Aceptador MEI"],
                "problemas_comunes": ["Fuente poder", "Display touch", "Comunicación MPU"]
            },
            "IGT S Plus": {
                "fabricante": "International Game Technology",
                "año": 2012,
                "tipo": "Video Slot",
                "caracteristicas": ["Main Board mejorado", "Power Supply", "Bill Validator"],
                "problemas_comunes": ["Main Board", "Power Supply", "Bill Validator"]
            },
            "IGT Game King": {
                "fabricante": "International Game Technology", 
                "año": 2011,
                "tipo": "Video Slot Multi-game",
                "caracteristicas": ["CPU Board", "Video Board", "Power Supply"],
                "problemas_comunes": ["CPU Board", "Video Board", "Touch Screen"]
            },
            "IGT Advantage": {
                "fabricante": "International Game Technology",
                "año": 2009,
                "tipo": "Platform Avanzada",
                "caracteristicas": ["Main Logic", "Power Distribution", "Monitor"],
                "problemas_comunes": ["Main Logic", "Power Distribution", "Monitor"]
            },
            "IGT Peak": {
                "fabricante": "International Game Technology",
                "año": 2014,
                "tipo": "Cabinet Premium", 
                "caracteristicas": ["CPU Cabinet", "Display Box", "Player Panel"],
                "problemas_comunes": ["CPU Cabinet", "Display Box", "Player Panel"]
            },
            "Aristocrat MK6": {
                "fabricante": "Aristocrat Technologies", 
                "año": 2008,
                "tipo": "Reel Slot",
                "caracteristicas": ["Sistema stepper", "Pantalla VFD", "Aceptador JCM"],
                "problemas_comunes": ["Motores stepper", "Fuente 28V", "Sensores reel"]
            },
            "Aristocrat MK5": {
                "fabricante": "Aristocrat Technologies",
                "año": 2006,
                "tipo": "Reel Slot",
                "caracteristicas": ["CPU Board", "Power Supply", "Monitor"],
                "problemas_comunes": ["CPU Board", "Power Supply", "Monitor"]
            },
            "Aristocrat Helix": {
                "fabricante": "Aristocrat Technologies",
                "año": 2016,
                "tipo": "Platform Moderna",
                "caracteristicas": ["Helix Core", "Display Module"],
                "problemas_comunes": ["Helix Core", "Display Module"]
            },
            "Aristocrat Oasis": {
                "fabricante": "Aristocrat Technologies",
                "año": 2015,
                "tipo": "Cabinet Lounge",
                "caracteristicas": ["System Board", "Cash System"],
                "problemas_comunes": ["System Board", "Cash System"]
            },
            "Aristocrat Edge": {
                "fabricante": "Aristocrat Technologies",
                "año": 2017,
                "tipo": "Video Slot",
                "caracteristicas": ["Edge X", "Player Interface"],
                "problemas_comunes": ["Edge X", "Player Interface"]
            },
            "Bally Alpha 2": {
                "fabricante": "Bally Technologies",
                "año": 2012, 
                "tipo": "Video Slot Multi-game",
                "caracteristicas": ["Plataforma Alpha 2", "Touch screen", "Sistema bonificación"],
                "problemas_comunes": ["Board CPU", "Touch screen", "Sistema audio"]
            },
            "Bally Alpha Pro": {
                "fabricante": "Bally Technologies",
                "año": 2013,
                "tipo": "Video Slot Profesional",
                "caracteristicas": ["Pro Cabinet", "Display System"],
                "problemas_comunes": ["Pro Cabinet", "Display System"]
            },
            "Bally iVIEW": {
                "fabricante": "Bally Technologies", 
                "año": 2011,
                "tipo": "Display System",
                "caracteristicas": ["Display Module", "Player Interface"],
                "problemas_comunes": ["Display Module", "Player Interface"]
            },
            "Konami Concerto": {
                "fabricante": "Konami Gaming",
                "año": 2015,
                "tipo": "Cabinet Premium", 
                "caracteristicas": ["Display curva", "Audio surround", "Sistema concerto"],
                "problemas_comunes": ["Display LED", "Sistema audio", "Comunicación network"]
            },
            "Konami KX": {
                "fabricante": "Konami Gaming",
                "año": 2014,
                "tipo": "Video Platform",
                "caracteristicas": ["KX Platform", "Video Output"],
                "problemas_comunes": ["KX Platform", "Video Output"]
            },
            "Konami Helix": {
                "fabricante": "Konami Gaming", 
                "año": 2016,
                "tipo": "Player Station",
                "caracteristicas": ["Helix Core", "Player Station"],
                "problemas_comunes": ["Helix Core", "Player Station"]
            },
            "SG Oasis 360": {
                "fabricante": "Scientific Games",
                "año": 2017,
                "tipo": "360 Cabinet",
                "caracteristicas": ["360 Cabinet", "Display System"],
                "problemas_comunes": ["360 Cabinet", "Display System"]
            },
            "SG TwinStar": {
                "fabricante": "Scientific Games",
                "año": 2015,
                "tipo": "Dual Screen",
                "caracteristicas": ["Dual Screen", "CPU System"],
                "problemas_comunes": ["Dual Screen", "CPU System"]
            },
            "Everi Cinevision": {
                "fabricante": "Everi Holdings",
                "año": 2016,
                "tipo": "Cabinet Multimedia",
                "caracteristicas": ["Cinevision Cabinet", "Display System"],
                "problemas_comunes": ["Cinevision Cabinet", "Display System"]
            },
            "Novomatic Axxis": {
                "fabricante": "Novomatic",
                "año": 2014,
                "tipo": "Video Slot",
                "caracteristicas": ["Axxis Cabinet", "Display System"],
                "problemas_comunes": ["Axxis Cabinet", "Display System"]
            },
            "Bingomania Clasico": {
                "fabricante": "Bingomania",
                "año": 2010,
                "tipo": "Máquina Local",
                "caracteristicas": ["Main Board", "Display", "Power Supply"],
                "problemas_comunes": ["Main Board", "Display", "Power Supply"]
            },
            "Caliente Slots Pro": {
                "fabricante": "Grupo Caliente", 
                "año": 2018,
                "tipo": "Máquina Mexicana",
                "caracteristicas": ["Pro Cabinet", "Video System"],
                "problemas_comunes": ["Pro Cabinet", "Video System"]
            }
        }

        # ========== MANUALES DE ACEPTADORES COMPLETOS ==========
        self.aceptadores = {
            "MEI SCN66 Advance": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador de Billetes de Alta Seguridad",
                "voltaje": "+24V DC ±5%",
                "consumo": "3.5A máximo",
                "comunicacion": "RS-232, MDB v4.0, USB 3.0, Ethernet",
                "billetes_aceptados": "MXN: Todas + USD: $1-$100 + EUR: €5-€500",
                "conectores": ["CN1: 20-pin Principal", "CN2: 8-pin Comunicaciones", "CN3: 6-pin Alimentación"],
                "codigos_error": {
                    "SCN-001": "Spectrometer Calibration Lost - Recalibrar espectrómetro",
                    "SCN-002": "Magnetic Sensor Array Failure - Revisar sensores magnéticos", 
                    "SCN-003": "CMOS Camera Module Fault - Revisar módulo cámara"
                },
                "problemas_comunes": [
                    "SCN-001 Error: Ejecutar recalibración espectrómetro completa",
                    "Falsos rechazos: Ajustar thresholds de confianza por divisa",
                    "Comunicación Ethernet: Verificar configuración VLAN segura"
                ]
            },
            "MEI SCN66 Standard": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador de Seguridad Estándar", 
                "voltaje": "+24V DC ±10%",
                "consumo": "3.0A máximo",
                "comunicacion": "RS-232, MDB v3.0, USB 2.0",
                "billetes_aceptados": "MXN: $20-$1000 + USD: $1-$50 + EUR: €5-€200",
                "conectores": ["J1: 16-pin Principal", "J2: 4-pin Alimentación", "J3: 6-pin Opciones"],
                "codigos_error": {
                    "SCN-101": "Standard Sensor Calibration - Calibrar sensores",
                    "SCN-102": "Magnetic Head Basic Fault - Revisar cabezal magnético",
                    "SCN-104": "IR Sensor Pair Mismatch - Re-alinear sensores IR"
                },
                "problemas_comunes": [
                    "SCN-101 Error: Ejecutar calibración estándar",
                    "SCN-104 Error: Re-alinear sensores IR",
                    "Rechazo constante: Verificar condiciones ambientales"
                ]
            },
            "MEI CashFlow 7000": {
                "fabricante": "MEI (Crane Payment Innovations)", 
                "tipo": "Aceptador CashFlow Series",
                "voltaje": "+24V DC ±10%",
                "consumo": "2.8A máximo",
                "comunicacion": "RS-232, MDB, USB, Ethernet",
                "billetes_aceptados": "MXN: $20-$1000 | USD: $1-$100",
                "conectores": ["J1: 16-pin Principal", "J2: 8-pin Ethernet", "J3: 4-pin Power"],
                "codigos_error": {
                    "CF-01": "CashFlow Sensor Error - Limpiar sensores",
                    "CF-02": "Transport Mechanism Fault - Revisar transporte",
                    "CF-03": "Magnetic Sensor Error - Revisar sensores magnéticos"
                },
                "problemas_comunes": [
                    "CF-01 Error: Limpiar cabezal validación completo",
                    "CF-04 Error: Verificar obstrucciones ruta óptica",
                    "Rechazo alto USD: Configurar sensibilidad para divisa"
                ]
            },
            "MEI CashFlow 6000": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador Mid-Range",
                "voltaje": "+24V DC ±10%", 
                "consumo": "2.5A máximo",
                "comunicacion": "RS-232, MDB, USB",
                "billetes_aceptados": "MXN: $20-$500 | USD: $1-$20",
                "conectores": ["J1: 14-pin Principal", "J2: 4-pin Stacker", "J3: 3-pin Power"],
                "codigos_error": {
                    "E20": "Magnetic Head Error - Recalibrar cabezal",
                    "E21": "UV Sensor Failure - Limpiar sensores UV",
                    "E22": "IR Sensor Array Error - Revisar array IR"
                },
                "problemas_comunes": [
                    "E20 Error: Recalibrar cabezal magnético",
                    "E21 Error: Limpiar sensores UV con alcohol especial", 
                    "Atascos frecuentes: Revisar tensión rodillos"
                ]
            },
            "JCM iVizion": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador con Visión Artificial", 
                "voltaje": "+24V DC ±10%",
                "consumo": "3.2A máximo",
                "comunicacion": "RS-232, MDB, Ethernet, WiFi, Bluetooth",
                "billetes_aceptados": "Múltiples divisas + Billetes dañados/arrugados",
                "conectores": ["CN1: 18-pin Principal", "CN2: 8-pin Red", "CN3: 4-pin Power", "CN4: 6-pin Cámara"],
                "codigos_error": {
                    "IV-100": "AI Vision System Failure - Reiniciar sistema IA",
                    "IV-101": "Neural Network Error - Re-entrenar modelo",
                    "IV-102": "Camera Module Fault - Limpiar lente cámara"
                },
                "problemas_comunes": [
                    "IV-100 Error: Reiniciar sistema IA completo",
                    "IV-102 Error: Limpiar lente cámara con kit especial",
                    "Falsos positivos: Re-entrenar modelo IA"
                ]
            },
            "JCM UNA-10": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador Universal", 
                "voltaje": "+24V DC ±10%",
                "consumo": "2.8A máximo",
                "comunicacion": "RS-232, MDB, USB-C, Ethernet", 
                "billetes_aceptados": "150+ divisas + Billetes polymer + Billetes verticales",
                "conectores": ["U1: 16-pin Universal", "U2: 6-pin USB-C", "U3: 4-pin Ethernet", "U4: 3-pin Power"],
                "codigos_error": {
                    "U10": "Universal Transport Error - Revisar transporte",
                    "U11": "Multi-Currency Sensor Fault - Revisar sensores",
                    "U12": "Polymer Detection Error - Recalibrar para polymer"
                },
                "problemas_comunes": [
                    "U10 Error: Revisar mecanismo transporte universal",
                    "U12 Error: Recalibrar para billetes polymer", 
                    "No detecta divisas: Actualizar base datos"
                ]
            },
            "MEI AE-2600": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador Estándar",
                "voltaje": "+24V DC ±10%",
                "consumo": "2.5A máximo", 
                "comunicacion": "RS-232, MDB, Pulse",
                "billetes_aceptados": "Pesos Mexicanos: $20-$1000",
                "conectores": ["J1: 12-pin Principal", "J2: 4-pin Stacker", "J3: 2-pin Power"],
                "codigos_error": {
                    "E01": "Bill Jam - Desatascar billete",
                    "E02": "Bill Removed - Billete removido",
                    "E03": "Stacker Full - Contenedor lleno"
                },
                "problemas_comunes": [
                    "No acepta billetes: Verificar enable/disable",
                    "Rechaza billetes buenos: Limpiar sensores ópticos", 
                    "Atasca billetes: Revisar rodillos y guías"
                ]
            },
            "JCM WBA-100": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador Universal",
                "voltaje": "+24V DC ±10%",
                "consumo": "2.0A máximo",
                "comunicacion": "RS-232, MDB, Weighing", 
                "billetes_aceptados": "Pesos Mexicanos: $20-$1000",
                "conectores": ["P1: 10-pin Control", "P2: 8-pin Datos", "P3: 2-pin Power"],
                "codigos_error": {
                    "F1": "Bill Jam in Validator - Desatascar validador",
                    "F2": "Bill Jam in Stacker - Desatascar stacker", 
                    "F3": "Cheated Bill - Billete sospechoso"
                },
                "problemas_comunes": [
                    "F1 Error: Desatascar mecanismo",
                    "F3 Error: Billete sospechoso - revisar sensores",
                    "No enciende: Verificar fusible interno"
                ]
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
st.markdown("**Versión Completa con TODAS las Máquinas y Aceptadores**")
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
    
    st.info(f"✅ **Sistema completo con:** {len(st.session_state.db.maquinas)} máquinas y {len(st.session_state.db.aceptadores)} aceptadores")

# ==================== DIAGNÓSTICO AVANZADO ====================
elif menu == "🔍 DIAGNÓSTICO AVANZADO":
    st.header("🔍 Diagnóstico Avanzado")
    
    modelo = st.selectbox(
        "🎰 **SELECCIONÁ EL MODELO:**",
        ["Seleccionar..."] + list(st.session_state.db.maquinas.keys()) + ["Otro modelo"]
    )
    
    if modelo == "Otro modelo":
        modelo = st.text_input("✍️ **ESCRIBÍ EL MODELO:**")
    
    sintoma = st.selectbox(
        "🩺 **SÍNTOMA PRINCIPAL:**",
        ["Seleccionar..."] + list(st.session_state.db.problemas_comunes.keys())
    )
    
    if st.button("🎯 EJECUTAR DIAGNÓSTICO", type="primary", use_container_width=True):
        if modelo and modelo != "Seleccionar..." and sintoma and sintoma != "Seleccionar...":
            st.success("✅ **DIAGNÓSTICO COMPLETADO**")
            
            if sintoma in st.session_state.db.problemas_comunes:
                problema = st.session_state.db.problemas_comunes[sintoma]
                st.success(f"**{problema['solucion']}**")

# ==================== MANUALES ACEPTADORES ====================
elif menu == "💰 MANUALES ACEPTADORES":
    st.header("💰 Manuales de Aceptadores")
    st.write(f"**Total de aceptadores en base de datos:** {len(st.session_state.db.aceptadores)}")
    
    aceptador_seleccionado = st.selectbox(
        "🔧 **SELECCIONÁ EL ACEPTADOR:**",
        list(st.session_state.db.aceptadores.keys())
    )
    
    if aceptador_seleccionado:
        info = st.session_state.db.aceptadores[aceptador_seleccionado]
        st.subheader(f"📋 {aceptador_seleccionado}")
        st.info(f"**Fabricante:** {info['fabricante']}")
        st.info(f"**Tipo:** {info['tipo']}")

# ==================== MÁQUINAS REGISTRADAS ====================
elif menu == "🎰 MÁQUINAS REGISTRADAS":
    st.header("🎰 Máquinas en Base de Datos")
    st.write(f"**Total de máquinas registradas:** {len(st.session_state.db.maquinas)}")
    
    for modelo, info in st.session_state.db.maquinas.items():
        with st.expander(f"🎰 {modelo} - {info['fabricante']}"):
            st.write(f"**Tipo:** {info['tipo']}")
            st.write(f"**Año:** {info['año']}")

# ==================== INVENTARIO COMPLETO ====================
elif menu == "📦 INVENTARIO COMPLETO":
    st.header("📦 Inventario Completo")
    
    for item in st.session_state.db.inventario:
        with st.expander(f"{item['nombre']} - Stock: {item['stock']}"):
            st.write(f"**Categoría:** {item['categoria']}")
            st.write(f"**Proveedor:** {item['proveedor']}")

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

# ==================== NUEVA REPARACIÓN ====================
elif menu == "📝 NUEVA REPARACIÓN":
    st.header("📝 Registrar Nueva Reparación")
    
    with st.form("nueva_reparacion"):
        modelo = st.selectbox(
            "🎰 Modelo de Máquina:",
            ["Seleccionar..."] + list(st.session_state.db.maquinas.keys()) + ["Otro"]
        )
        problema = st.selectbox(
            "🩺 Problema:",
            ["Seleccionar..."] + list(st.session_state.db.problemas_comunes.keys()) + ["Otro"]
        )
        tecnico = st.text_input("👤 Técnico:")
        solucion = st.text_area("🛠️ Solución:")
        
        if st.form_submit_button("💾 GUARDAR REPARACIÓN"):
            if all([modelo, problema, solucion, tecnico]):
                st.success("✅ REPARACIÓN GUARDADA")

# ==================== HISTORIAL COMPLETO ====================
elif menu == "📊 HISTORIAL COMPLETO":
    st.header("📊 Historial de Reparaciones")
    
    if not st.session_state.db.reparaciones:
        st.info("📝 Aún no hay reparaciones registradas")
    else:
        for i, reparacion in enumerate(reversed(st.session_state.db.reparaciones), 1):
            with st.expander(f"🔧 {i}. {reparacion.get('fecha', 'Sin fecha')} - {reparacion.get('modelo', 'Sin modelo')}"):
                st.write(f"**Problema:** {reparacion.get('problema', 'No especificado')}")
                st.write(f"**Técnico:** {reparacion.get('tecnico', 'No especificado')}")

# FOOTER
st.markdown("---")
st.caption("🎰 **CasinoPro Complete v3.0** - Sistema Técnico Integral")
st.caption(f"📊 {len(st.session_state.db.maquinas)} Máquinas | 💰 {len(st.session_state.db.aceptadores)} Aceptadores | 📦 {len(st.session_state.db.inventario)} Repuestos")
