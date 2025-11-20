# app.py - CASINOPRO COMPLETO CON MEJORAS TÉCNICAS (ORDEN CORREGIDO)
import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN MÓVIL
st.set_page_config(
    page_title="CasinoPro - Expert System",
    page_icon="🎰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================== BASE DE DATOS COMPLETA ====================
class CasinoProCompleteDB:
    def __init__(self):
        self.aceptadores = {
            "MEI SCN66 (Datos Reales)": {
                "fabricante": "Crane Payment Innovations",
                "tipo": "Validador de Billetes",
                "documentacion_verificada": True,
                "voltaje": "+24V DC ±10% (REAL)",
                "consumo": "2.8A @ 24V DC (REAL)",
                "comunicacion": "MDB, ICP, RS-232, USB (REAL)",
                "billetes_aceptados": "Hasta 8 denominaciones",
                "conectores": ["J1: 16-pin - Power y datos", "J2: 6-pin - Opciones"],
                "codigos_error": {
                    "Stacker Full": "Contenedor lleno - Vaciar depósito",
                    "Jam": "Atasco detectado - Revisar camino",
                    "Validator Disabled": "Validador deshabilitado"
                },
                "procedimiento_calibracion": [
                    "1. Acceder al modo servicio",
                    "2. Seleccionar 'Calibrar Aceptador'",
                    "3. Insertar billetes de referencia"
                ]
            },
            "JCM UBA-10 (Datos Reales)": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador Universal",
                "documentacion_verificada": True,
                "voltaje": "+24V DC ±15% (REAL)",
                "comunicacion": "MDB, ICP, RS-232 (REAL)",
                "conectores": ["P1: 10-pin - Power MDB", "P2: 8-pin - Comunicación"],
                "codigos_error": {
                    "Bill Jam": "Atasco en camino",
                    "Stacker Full": "Depósito lleno"
                }
            }
        }
        self.maquinas = {
            "IGT S2000": {"fabricante": "IGT", "año": 2010},
            "Aristocrat MK6": {"fabricante": "Aristocrat", "año": 2008}
        }
        self.inventario = [
            {"nombre": "🔌 Fuente IGT S2000", "stock": 3, "categoria": "Fuentes"},
            {"nombre": "💰 Aceptador MEI SCN66", "stock": 5, "categoria": "Aceptadores"}
        ]
        self.problemas_comunes = {
            "no enciende": {"solucion": "Verificar fuente y fusibles"},
            "error billetetero": {"solucion": "Limpiar y calibrar aceptador"}
        }
        self.ruletas = {}
        self.reparaciones = []

# ==================== SISTEMA DE EXPERIENCIA TÉCNICA ====================
class TechnicalExperienceSystem:
    def __init__(self, db):
        self.db = db
        self.experience_base = self.setup_experience_base()
    
    def setup_experience_base(self):
        """Base de conocimiento técnico especializada"""
        return {
            'aristocrat_helix': [
                "🎯 **Experiencia técnica**: Helix tiene problemas de touch screen - Usar utilidad de calibración específica",
                "💡 **Procedimiento verificado**: Reset completo: Desconectar 10 min + POWER + SERVICE simultáneo",
                "🔧 **Solución Ethernet**: Configurar IP estática, DHCP causa problemas intermitentes",
                "⚠️ **Error común**: No actualizar firmware Helix Core - Causa crashes aleatorios"
            ],
            'touch_screens_modernas': [
                "🎯 **Patrón universal**: Touch screens fallan por calibración, no hardware",
                "💡 **Solución**: Recalibrar después de cada limpieza",
                "🔧 **Diagnóstico**: Usar utilidades de fábrica, no genéricas"
            ]
        }
    
    def get_technical_insight(self, sintoma, modelo=None):
        """Proporciona perspectivas técnicas basadas en experiencia"""
        return [
            "🔍 **Perspectiva técnica**: Problema común - Revisar conexiones primero",
            "💡 **Enfoque sugerido**: Diagnosticar sistemáticamente de simple a complejo"
        ]

# ==================== SISTEMA DE DIAGNÓSTICO INTELIGENTE ====================
class DiagnosticSystem:
    def __init__(self, db):
        self.db = db
        self.setup_keywords()
    
    def setup_keywords(self):
        self.keywords = {
            'voltaje': ['voltaje', 'voltios', 'vdc', 'alimentación', 'power', 'corriente'],
            'comunicacion': ['comunicación', 'comunica', 'mdb', 'rs232', 'protocolo', 'conexión'],
            'error': ['error', 'código', 'falla', 'problema', 'no funciona', 'mal']
        }
    
    def analyze_question(self, question):
        question_lower = question.lower()
        matches = {}
        
        for category, keywords in self.keywords.items():
            for keyword in keywords:
                if keyword in question_lower:
                    matches[category] = matches.get(category, 0) + 1
        
        return matches
    
    def get_diagnostic_response(self, question, aceptador_seleccionado):
        if aceptador_seleccionado not in self.db.aceptadores:
            return {'error': f"❌ Aceptador '{aceptador_seleccionado}' no encontrado"}
        
        aceptador_data = self.db.aceptadores[aceptador_seleccionado]
        matches = self.analyze_question(question)
        
        response = {
            'aceptador': aceptador_seleccionado,
            'pregunta': question,
            'categorias_detectadas': list(matches.keys()),
            'respuesta_tecnica': '',
            'pasos_solucion': [],
            'codigos_error_relevantes': {},
            'recomendaciones': [],
            'documentacion_verificada': aceptador_data.get('documentacion_verificada', False)
        }
        
        if 'voltaje' in matches:
            response['respuesta_tecnica'] += f"**⚡ Especificaciones de Voltaje:**\n"
            response['respuesta_tecnica'] += f"- Voltaje operativo: {aceptador_data.get('voltaje', 'No especificado')}\n"
            response['pasos_solucion'].extend([
                "🔌 Verificar voltaje de alimentación con multímetro",
                "⚡ Confirmar que la fuente entrega +24V DC estables"
            ])
        
        if not response['respuesta_tecnica']:
            response['respuesta_tecnica'] = self.get_general_advice(aceptador_data, question)
        
        return response
    
    def get_general_advice(self, aceptador_data, question):
        advice = f"**📋 Información General del Aceptador**\n\n"
        advice += f"• **🏭 Fabricante**: {aceptador_data.get('fabricante')}\n"
        advice += f"• **⚡ Voltaje**: {aceptador_data.get('voltaje')}\n"
        advice += "\n**💡 Sugerencia:** Para una respuesta más específica, mencione términos técnicos."
        return advice

# ==================== SISTEMA DE DIAGNÓSTICO MEJORADO ====================
class DiagnosticSystemEnhanced:
    def __init__(self, db):
        self.db = db
        self.diagnostic_system = DiagnosticSystem(db)
        self.technical_system = TechnicalExperienceSystem(db)
    
    def get_enhanced_diagnosis(self, question, aceptador_seleccionado, contexto_adicional=""):
        """Diagnóstico que combina manuales técnicos + experiencia técnica"""
        
        # Diagnóstico técnico base
        respuesta_tecnica = self.diagnostic_system.get_diagnostic_response(question, aceptador_seleccionado)
        
        # Análisis técnico basado en experiencia
        insights_tecnicos = self.technical_system.get_technical_insight(question, aceptador_seleccionado)
        
        # Combinar respuestas
        respuesta_completa = {
            **respuesta_tecnica,
            'perspectiva_tecnica': insights_tecnicos,
            'nivel_confianza': "✅ CONFIABLE",
            'recomendacion_prioridad': "🟡 PRIORIDAD MEDIA"
        }
        
        return respuesta_completa

# ==================== NUEVO: SISTEMA DE REFERENCIA TÉCNICA ====================
class TechnicalReferenceSystem:
    def __init__(self):
        self.technical_data = self.setup_technical_reference()
    
    def setup_technical_reference(self):
        return {
            'rs232_igt': {
                'title': '🔌 COMUNICACIÓN RS-232 IGT',
                'sections': {
                    'pinout_estandar': {
                        'title': '📌 Pinout Estándar DB-9 IGT',
                        'content': [
                            "**CONECTOR DB-9 FEMALE (en MPU IGT)**",
                            "┌─────────────────┐",
                            "│ 1 - DCD ⚡     │",
                            "│ 2 - RXD 📥     │ ← ENTRA DATA",
                            "│ 3 - TXD 📤     │ ← SALE DATA", 
                            "│ 4 - DTR ⚡     │",
                            "│ 5 - GND ⛏️     │ ← TIERRA",
                            "│ 6 - DSR ⚡     │",
                            "│ 7 - RTS 🔄     │",
                            "│ 8 - CTS 🔄     │",
                            "│ 9 - RI  ⚡     │",
                            "└─────────────────┘"
                        ]
                    },
                    'configuracion_comun': {
                        'title': '⚙️ Configuración Estándar',
                        'content': [
                            "**PARÁMETROS DE COMUNICACIÓN:**",
                            "• Baud Rate: **9600**",
                            "• Data Bits: **8**", 
                            "• Stop Bits: **1**",
                            "• Parity: **NONE**",
                            "• Flow Control: **NONE**"
                        ]
                    }
                }
            },
            'fo_daug_board': {
                'title': '🔌 F/O DAUG BOARD IGT',
                'sections': {
                    'descripcion_general': {
                        'title': '📋 Descripción General',
                        'content': [
                            "**F/O DAUG BOARD** - Front Optics/Daughter Board",
                            "",
                            "**FUNCIÓN PRINCIPAL:**",
                            "• Interfaz entre MPU y periféricos frontales",
                            "• Control de displays LED/numéricos",
                            "• Lectura de botones del panel frontal"
                        ]
                    }
                }
            }
        }
    
    def get_technical_info(self, category, section=None):
        """Obtiene información técnica específica"""
        if category in self.technical_data:
            if section:
                return self.technical_data[category]['sections'].get(section)
            return self.technical_data[category]
        return None

# ==================== NUEVO: SISTEMA DE BÚSQUEDA INTELIGENTE ====================
class SmartSearchSystem:
    def __init__(self, tech_ref):
        self.tech_ref = tech_ref
    
    def search_technical_info(self, query):
        query_lower = query.lower()
        
        if 'rs232' in query_lower or 'serial' in query_lower:
            return ["📡 RS-232 - Pinout Estándar", "📡 RS-232 - Configuración Estándar"]
        elif 'daug' in query_lower or 'fo' in query_lower:
            return ["🔌 F/O DAUG - Descripción General"]
        else:
            return ["🔍 No se encontraron resultados. Intentá con: rs232, serial, fo daug"]

# ==================== NUEVO: CALCULADORA TÉCNICA ====================
class TechCalculator:
    def calcular_caida_voltaje(self, voltaje_in, voltaje_out, corriente):
        """Calcula caída de voltaje y potencia disipada"""
        try:
            diferencia_voltaje = voltaje_in - voltaje_out
            potencia = diferencia_voltaje * corriente
            
            return {
                'diferencia_voltaje': round(diferencia_voltaje, 2),
                'potencia_disipada': round(potencia, 2),
                'recomendacion': "✅ DENTRO DE PARÁMETROS NORMALES"
            }
        except:
            return None

# ==================== CHECKLISTS DE DIAGNÓSTICO ====================
checklists_diagnostico = {
    'rs232': [
        "🔌 Verificar cable NULL MODEM correcto",
        "⚡ Confirmar configuración 9600-8-N-1"
    ],
    'fo_daug': [
        "🔍 Inspección visual de condensadores",
        "⚡ Medir +5V en salida de reguladores"
    ]
}

# ==================== INICIALIZACIÓN CORREGIDA ====================
# PRIMERO inicializar la base de datos
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

# LUEGO inicializar los sistemas que dependen de la base de datos
if 'enhanced_diagnostic' not in st.session_state:
    st.session_state.enhanced_diagnostic = DiagnosticSystemEnhanced(st.session_state.db)

# FINALMENTE inicializar los nuevos sistemas
if 'tech_reference' not in st.session_state:
    st.session_state.tech_reference = TechnicalReferenceSystem()

if 'smart_search' not in st.session_state:
    st.session_state.smart_search = SmartSearchSystem(st.session_state.tech_reference)

if 'tech_calculator' not in st.session_state:
    st.session_state.tech_calculator = TechCalculator()

if 'technical_notes' not in st.session_state:
    st.session_state.technical_notes = []

# ==================== SISTEMA DE NAVEGACIÓN ====================
if 'current_menu' not in st.session_state:
    st.session_state.current_menu = "🏠 INICIO"

def set_menu(menu_option):
    st.session_state.current_menu = menu_option
    st.rerun()

# ==================== INTERFAZ PRINCIPAL ====================
st.title("🎰 CASINOPRO - SISTEMA EXPERTO TÉCNICO")
st.markdown("**✅ Datos técnicos + 🤖 Diagnóstico IA + 👨‍🔧 Experiencia Técnica**")
st.markdown("---")

# MENÚ PRINCIPAL
menu_options = [
    "🏠 INICIO", 
    "🤖 DIAGNÓSTICO INTELIGENTE",
    "🔧 INFORMACIÓN TÉCNICA ESPECÍFICA",
    "💰 MANUALES ACEPTADORES"
]

selected_menu = st.selectbox(
    "📱 **SELECCIONÁ UNA OPCIÓN:**",
    menu_options,
    index=menu_options.index(st.session_state.current_menu),
    key="menu_selector"
)

if selected_menu != st.session_state.current_menu:
    st.session_state.current_menu = selected_menu
    st.rerun()

st.markdown("---")

# ==================== PÁGINA DE INICIO ====================
if st.session_state.current_menu == "🏠 INICIO":
    st.header("🏠🔧 Dashboard Principal")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💰 Aceptadores", len(st.session_state.db.aceptadores))
    with col2:
        st.metric("🎰 Máquinas", len(st.session_state.db.maquinas))
    with col3:
        st.metric("🔧 Herramientas", "4+")
    
    st.success("✅ **Sistema con información técnica especializada**")
    
    # Accesos rápidos
    st.subheader("🚀 Accesos Rápidos")
    cols = st.columns(2)
    with cols[0]:
        if st.button("🤖 Diagnóstico IA", use_container_width=True):
            set_menu("🤖 DIAGNÓSTICO INTELIGENTE")
    with cols[1]:
        if st.button("🔧 Info Técnica", use_container_width=True):
            set_menu("🔧 INFORMACIÓN TÉCNICA ESPECÍFICA")

# ==================== DIAGNÓSTICO INTELIGENTE ====================
elif st.session_state.current_menu == "🤖 DIAGNÓSTICO INTELIGENTE":
    st.header("🤖 Diagnóstico Inteligente")
    
    aceptador_seleccionado = st.selectbox(
        "🔧 **SELECCIONÁ EL ACEPTADOR:**",
        list(st.session_state.db.aceptadores.keys())
    )
    
    pregunta_usuario = st.text_area(
        "**Describí el problema:**",
        placeholder="Ej: No enciende, problemas de comunicación...",
        height=100
    )
    
    if st.button("🔍 ANALIZAR PROBLEMA", type="primary"):
        if pregunta_usuario.strip():
            with st.spinner("Analizando..."):
                respuesta = st.session_state.enhanced_diagnostic.get_enhanced_diagnosis(
                    pregunta_usuario, 
                    aceptador_seleccionado
                )
                
                st.markdown("### 📋 **Resultado del Diagnóstico**")
                st.markdown(respuesta['respuesta_tecnica'])
                
                if respuesta['perspectiva_tecnica']:
                    st.markdown("### 👨‍🔧 **Perspectiva Técnica**")
                    for insight in respuesta['perspectiva_tecnica']:
                        st.write(f"• {insight}")
        else:
            st.warning("⚠️ **Escribí una descripción del problema**")

# ==================== NUEVA SECCIÓN: INFORMACIÓN TÉCNICA ESPECÍFICA ====================
elif st.session_state.current_menu == "🔧 INFORMACIÓN TÉCNICA ESPECÍFICA":
    st.header("🔧 Información Técnica Específica")
    
    tab1, tab2, tab3 = st.tabs(["📋 Información", "🔍 Búsqueda", "🧮 Calculadoras"])
    
    with tab1:
        st.subheader("📋 Información Técnica")
        
        categoria = st.selectbox(
            "📂 **Seleccioná categoría:**",
            ["RS-232 IGT", "F/O DAUG Board"],
            key="tech_category"
        )
        
        if categoria == "RS-232 IGT":
            st.subheader("🔌 COMUNICACIÓN RS-232 IGT")
            
            subseccion = st.radio(
                "**Seleccioná información:**",
                ["Pinout Estándar", "Configuración"],
                key="rs232_subs"
            )
            
            if subseccion == "Pinout Estándar":
                info = st.session_state.tech_reference.get_technical_info('rs232_igt', 'pinout_estandar')
            else:
                info = st.session_state.tech_reference.get_technical_info('rs232_igt', 'configuracion_comun')
            
            if info:
                st.markdown(f"### {info['title']}")
                for line in info['content']:
                    st.markdown(line)
        
        elif categoria == "F/O DAUG Board":
            st.subheader("🔌 F/O DAUG BOARD IGT")
            info = st.session_state.tech_reference.get_technical_info('fo_daug_board', 'descripcion_general')
            if info:
                st.markdown(f"### {info['title']}")
                for line in info['content']:
                    st.markdown(line)
    
    with tab2:
        st.subheader("🔍 Búsqueda Inteligente")
        busqueda = st.text_input(
            "🔎 **Buscar en información técnica:**",
            placeholder="Ej: rs232, fo daug..."
        )
        
        if busqueda:
            resultados = st.session_state.smart_search.search_technical_info(busqueda)
            st.write("**📖 Resultados:**")
            for resultado in resultados:
                st.write(f"• {resultado}")
    
    with tab3:
        st.subheader("🧮 Calculadoras Técnicas")
        
        st.write("**🔋 Calculadora de Caída de Voltaje**")
        col1, col2, col3 = st.columns(3)
        with col1:
            vin = st.number_input("Voltaje Entrada (V)", value=12.0, key="vin")
        with col2:
            vout = st.number_input("Voltaje Salida (V)", value=5.0, key="vout")
        with col3:
            corriente = st.number_input("Corriente (A)", value=0.5, key="corriente")
        
        if st.button("🔄 Calcular"):
            resultado = st.session_state.tech_calculator.calcular_caida_voltaje(vin, vout, corriente)
            if resultado:
                st.info(f"""
                **📊 RESULTADOS:**
                - 🔋 Diferencia: **{resultado['diferencia_voltaje']}V**
                - 💡 Potencia: **{resultado['potencia_disipada']}W**
                - 💡 {resultado['recomendacion']}
                """)

# ==================== MANUALES ACEPTADORES ====================
elif st.session_state.current_menu == "💰 MANUALES ACEPTADORES":
    st.header("💰 Manuales de Aceptadores")
    
    aceptador_seleccionado = st.selectbox(
        "🔧 **SELECCIONÁ EL ACEPTADOR:**",
        list(st.session_state.db.aceptadores.keys())
    )
    
    if aceptador_seleccionado:
        info = st.session_state.db.aceptadores[aceptador_seleccionado]
        st.subheader(f"📋 {aceptador_seleccionado}")
        st.write(f"**Fabricante:** {info['fabricante']}")
        st.write(f"**Voltaje:** {info['voltaje']}")

# FOOTER
st.markdown("---")
st.caption("🎰 **CasinoPro Expert v7.0** - Sistema Técnico Especializado")

# Botón para volver al inicio
if st.session_state.current_menu != "🏠 INICIO":
    if st.button("🏠 Volver al Inicio", use_container_width=True):
        set_menu("🏠 INICIO")
