# app.py - CASINOPRO COMPLETO CON MEJORAS TÉCNICAS
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

# ==================== SISTEMA DE EXPERIENCIA TÉCNICA ====================
class TechnicalExperienceSystem:
    def __init__(self, db):
        self.db = db
        self.experience_base = self.setup_experience_base()
    
    def setup_experience_base(self):
        """Base de conocimiento técnico especializada"""
        return {
            # ... (mantener todo el contenido existente igual)
            'aristocrat_helix': [
                "🎯 **Experiencia técnica**: Helix tiene problemas de touch screen - Usar utilidad de calibración específica",
                "💡 **Procedimiento verificado**: Reset completo: Desconectar 10 min + POWER + SERVICE simultáneo",
                # ... (todo el contenido anterior se mantiene igual)
            ],
            # ... (todas las demás secciones igual)
        }
    
    def get_technical_insight(self, sintoma, modelo=None):
        # ... (mantener método igual)
        pass

# ==================== SISTEMA DE DIAGNÓSTICO INTELIGENTE ====================
class DiagnosticSystem:
    # ... (mantener clase completa igual)
    pass

# ==================== SISTEMA DE DIAGNÓSTICO MEJORADO ====================
class DiagnosticSystemEnhanced:
    # ... (mantener clase completa igual)
    pass

# ==================== BASE DE DATOS COMPLETA ====================
class CasinoProCompleteDB:
    # ... (mantener clase completa igual)
    pass

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
                            "• Flow Control: **NONE**",
                            "",
                            "**PROTOCOLO:** SAS 6.0x"
                        ]
                    },
                    
                    'cableado_pc': {
                        'title': '🔗 Cableado para PC',
                        'content': [
                            "**CABLE NULL MODEM (IGT a PC):**",
                            "IGT Pin 2 (RXD) → PC Pin 3 (TXD)",
                            "IGT Pin 3 (TXD) → PC Pin 2 (RXD)",
                            "IGT Pin 5 (GND) → PC Pin 5 (GND)",
                            "",
                            "**NOTA:** IGT es DTE, PC es DTE - necesita crossover"
                        ]
                    },
                    
                    'comandos_sas_basicos': {
                        'title': '📡 Comandos SAS Básicos',
                        'content': [
                            "**FORMATO:** |STX|COMANDO|DATA|ETX|CHK|",
                            "",
                            "**COMANDOS PRINCIPALES:**",
                            "• |01| - Send SAS Address",
                            "• |03| - Game Lock", 
                            "• |04| - Game Unlock",
                            "• |2F| - Meter Readings",
                            "",
                            "**EJEMPLO RESPUESTA:**",
                            "|81|SAS Address: 01|"
                        ]
                    },
                    
                    'diagnostico_problemas': {
                        'title': '🔧 Diagnóstico de Problemas',
                        'content': [
                            "**SI NO HAY COMUNICACIÓN:**",
                            "1. ✅ Verificar cable NULL MODEM",
                            "2. ✅ Confirmar 9600-8-N-1 en software",
                            "3. ✅ Probar con loopback test",
                            "4. ✅ Verificar tierra común (GND)",
                            "",
                            "**SI DATOS CORRUPTOS:**",
                            "• Usar cable blindado < 3 metros",
                            "• Verificar fuente de alimentación",
                            "• Revisar conectores oxidados"
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
                            "• Lectura de botones del panel frontal",
                            "• Interfaz para optic readers",
                            "",
                            "**UBICACIÓN:** Área frontal, detrás del display"
                        ]
                    },
                    
                    'sistemas_compatibles': {
                        'title': '🎰 Sistemas que la Usan',
                        'content': [
                            "• IGT S2000 Series",
                            "• IGT S3000 Series", 
                            "• IGT Game King",
                            "• IGT Advantage Plus",
                            "",
                            "**NOTA:** Verificar modelo específico"
                        ]
                    },
                    
                    'problemas_comunes': {
                        'title': '⚠️ Problemas Comunes',
                        'content': [
                            "**NO ENCIENDEN DISPLAYS:**",
                            "• Verificar +5V en conector de poder",
                            "• Revisar reguladores LM7805/LM7812",
                            "• Chequear condensadores electrolíticos",
                            "",
                            "**BOTONES NO RESPONDEN:**",
                            "• Verificar ribbon cables",
                            "• Revisar matriz de botones",
                            "• Chequear drivers de input",
                            "",
                            "**COMUNICACIÓN MPU FALLA:**",
                            "• Verificar cableado a placa principal",
                            "• Revisar señales de data/clock"
                        ]
                    },
                    
                    'componentes_criticos': {
                        'title': '🔍 Componentes Críticos',
                        'content': [
                            "**REGULADORES DE VOLTAJE:**",
                            "• LM7805 (+5V) - Falla frecuente",
                            "• LM7812 (+12V) - Verificar salida",
                            "",
                            "**CONDENSADORES ELECTROLÍTICOS:**",
                            "• Se hinchan con el tiempo",
                            "• Causan inestabilidad de voltaje",
                            "",
                            "**CHIPS DRIVERS:**",
                            "• Control de displays LED",
                            "• Drivers de botones/inputs",
                            "",
                            "**EPROM DE CONFIGURACIÓN:**",
                            "• Contiene settings específicos"
                        ]
                    },
                    
                    'procedimiento_diagnostico': {
                        'title': '🛠️ Procedimiento de Diagnóstico',
                        'content': [
                            "**PASO A PASO:**",
                            "1. 🔌 DESCONECTAR ALIMENTACIÓN",
                            "2. 🔍 INSPECCIÓN VISUAL:",
                            "   - Condensadores hinchados",
                            "   - Pistas quemadas/rotas",
                            "   - Conectores oxidados",
                            "3. ⚡ MEDICIÓN DE VOLTAJES:",
                            "   +5V en reguladores",
                            "   +12V de entrada",
                            "   Tierra común",
                            "4. 🔄 PRUEBA EN MÁQUINA BUENA",
                            "5. 📊 VERIFICAR SEÑALES DATA"
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
        self.search_keywords = self.setup_search_index()
    
    def setup_search_index(self):
        return {
            'rs232': ['rs232', 'serial', 'comunicación', 'db9', 'pinout', 'sas'],
            'pinout': ['pinout', 'conector', 'pines', 'cableado', 'db9'],
            'fo_daug': ['fo daug', 'daughter board', 'front optics', 'display', 'botones'],
            'comandos': ['comandos', 'sas', 'protocolo', 'hex', 'respuesta'],
            'diagnostico': ['diagnóstico', 'problemas', 'fallas', 'no funciona', 'error'],
            'voltaje': ['voltaje', '+5v', '+12v', 'alimentación', 'fuente']
        }
    
    def search_technical_info(self, query):
        query_lower = query.lower()
        results = []
        
        for category, keywords in self.search_keywords.items():
            for keyword in keywords:
                if keyword in query_lower:
                    # Buscar en RS-232
                    if category in ['rs232', 'pinout', 'comandos', 'diagnostico']:
                        results.extend(self.search_in_rs232(category))
                    # Buscar en F/O DAUG
                    elif category in ['fo_daug', 'voltaje']:
                        results.extend(self.search_in_fo_daug(category))
        
        return results if results else ["🔍 No se encontraron resultados. Intentá con otras palabras."]
    
    def search_in_rs232(self, category):
        results = []
        rs232_data = self.tech_ref.get_technical_info('rs232_igt')
        
        for section_name, section_data in rs232_data['sections'].items():
            content_text = ' '.join(section_data['content']).lower()
            if any(keyword in content_text for keyword in self.search_keywords[category]):
                results.append(f"📡 RS-232 - {section_data['title']}")
        
        return results
    
    def search_in_fo_daug(self, category):
        results = []
        fo_daug_data = self.tech_ref.get_technical_info('fo_daug_board')
        
        for section_name, section_data in fo_daug_data['sections'].items():
            content_text = ' '.join(section_data['content']).lower()
            if any(keyword in content_text for keyword in self.search_keywords[category]):
                results.append(f"🔌 F/O DAUG - {section_data['title']}")
        
        return results

# ==================== NUEVO: CALCULADORA TÉCNICA ====================
class TechCalculator:
    def calcular_caida_voltaje(self, voltaje_in, voltaje_out, corriente):
        """Calcula caída de voltaje y potencia disipada"""
        try:
            diferencia_voltaje = voltaje_in - voltaje_out
            potencia = diferencia_voltaje * corriente
            resistencia = diferencia_voltaje / corriente if corriente > 0 else 0
            
            return {
                'diferencia_voltaje': round(diferencia_voltaje, 2),
                'potencia_disipada': round(potencia, 2),
                'resistencia_teorica': round(resistencia, 2),
                'recomendacion': self.analizar_resultados(potencia, diferencia_voltaje)
            }
        except:
            return None
    
    def analizar_resultados(self, potencia, diferencia):
        if potencia > 1.0:
            return "⚠️ ALTA POTENCIA - Considerá disipador de calor"
        elif diferencia > 3.0:
            return "🔍 GRAN CAÍDA - Verificar regulador apropiado"
        else:
            return "✅ DENTRO DE PARÁMETROS NORMALES"
    
    def calcular_resistencia_led(self, voltaje_fuente, voltaje_led, corriente_led):
        """Calcula resistencia para LED"""
        try:
            resistencia = (voltaje_fuente - voltaje_led) / (corriente_led / 1000)  # mA to A
            potencia = (voltaje_fuente - voltaje_led) * (corriente_led / 1000)
            
            return {
                'resistencia': round(resistencia, 1),
                'potencia': round(potencia, 3),
                'valor_comercial': self.encontrar_valor_comercial(resistencia)
            }
        except:
            return None
    
    def encontrar_valor_comercial(self, resistencia):
        valores_comerciales = [10, 22, 47, 100, 220, 470, 1000, 2200, 4700, 10000]
        for valor in valores_comerciales:
            if valor >= resistencia * 0.8:  # Margen del 20%
                return f"{valor} Ω"
        return "Valor no estándar - usar combinación serie/paralelo"

# ==================== NUEVO: CHECKLISTS DE DIAGNÓSTICO ====================
checklists_diagnostico = {
    'rs232': [
        "🔌 Verificar cable NULL MODEM correcto",
        "⚡ Confirmar configuración 9600-8-N-1", 
        "🔍 Probar con loopback test",
        "📏 Usar cable < 3 metros blindado",
        "🔧 Verificar drivers USB-Serial instalados",
        "💾 Probar con software terminal básico"
    ],
    
    'fo_daug': [
        "🔍 Inspección visual de condensadores",
        "⚡ Medir +5V en salida de reguladores",
        "🔌 Verificar todos los ribbon cables",
        "💡 Revisar integridad de pistas en PCB",
        "🔄 Probar en máquina conocida buena",
        "📊 Verificar señales de clock y data"
    ],
    
    'fuente_poder': [
        "⚡ Medir voltajes +5V, +12V, +24V",
        "🔍 Revisar fusibles y protección",
        "💨 Limpiar ventiladores y disipadores",
        "📈 Verificar ripple en osciloscopio",
        "🔌 Chequear conectores de entrada",
        "🌡️ Monitorear temperatura de operación"
    ]
}

# ==================== NUEVO: REGISTRO DE PROBLEMAS ====================
class ProblemLogger:
    def __init__(self):
        self.problem_history = []
    
    def log_problem(self, maquina, problema, solucion, exitoso=True):
        registro = {
            'fecha': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'maquina': maquina,
            'problema': problema,
            'solucion': solucion,
            'exitoso': exitoso
        }
        self.problem_history.append(registro)
        return registro
    
    def get_similar_problems(self, problema_actual):
        problemas_similares = []
        problema_lower = problema_actual.lower()
        
        for registro in self.problem_history:
            if (problema_lower in registro['problema'].lower() or 
                problema_lower in registro['solucion'].lower()):
                problemas_similares.append(registro)
        
        return problemas_similares[:5]

# ==================== INICIALIZACIÓN COMPLETA ====================
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

if 'enhanced_diagnostic' not in st.session_state:
    st.session_state.enhanced_diagnostic = DiagnosticSystemEnhanced(st.session_state.db)

# INICIALIZAR NUEVOS SISTEMAS
if 'tech_reference' not in st.session_state:
    st.session_state.tech_reference = TechnicalReferenceSystem()

if 'smart_search' not in st.session_state:
    st.session_state.smart_search = SmartSearchSystem(st.session_state.tech_reference)

if 'tech_calculator' not in st.session_state:
    st.session_state.tech_calculator = TechCalculator()

if 'problem_logger' not in st.session_state:
    st.session_state.problem_logger = ProblemLogger()

# INICIALIZAR NOTAS TÉCNICAS
if 'technical_notes' not in st.session_state:
    st.session_state.technical_notes = []

# ==================== SISTEMA DE NAVEGACIÓN MEJORADO ====================
if 'current_menu' not in st.session_state:
    st.session_state.current_menu = "🏠 INICIO"

def set_menu(menu_option):
    st.session_state.current_menu = menu_option
    st.rerun()

# ==================== INTERFAZ PRINCIPAL ACTUALIZADA ====================
st.title("🎰 CASINOPRO - SISTEMA EXPERTO TÉCNICO")
st.markdown("**✅ Datos técnicos + 🤖 Diagnóstico IA + 👨‍🔧 Experiencia Técnica Especializada**")
st.markdown("---")

# MENÚ PRINCIPAL ACTUALIZADO CON NUEVA OPCIÓN
menu_options = [
    "🏠 INICIO", 
    "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO",
    "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO",
    "🔧 INFORMACIÓN TÉCNICA ESPECÍFICA",  # NUEVA OPCIÓN
    "💰 MANUALES ACEPTADORES",
    "🎰 MÁQUINAS REGISTRADAS", 
    "📦 INVENTARIO COMPLETO"
]

# Selectbox para navegación
selected_menu = st.selectbox(
    "📱 **SELECCIONÁ UNA OPCIÓN:**",
    menu_options,
    index=menu_options.index(st.session_state.current_menu),
    key="menu_selector"
)

# Actualizar estado si cambió el selectbox
if selected_menu != st.session_state.current_menu:
    st.session_state.current_menu = selected_menu
    st.rerun()

st.markdown("---")

# ==================== PÁGINA DE INICIO (MANTENER IGUAL) ====================
if st.session_state.current_menu == "🏠 INICIO":
    st.header("🏠🔧 Dashboard con Conocimiento Técnico Integrado")
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💰 Aceptadores", len(st.session_state.db.aceptadores))
    with col2:
        st.metric("🎰 Máquinas", len(st.session_state.db.maquinas))
    with col3:
        st.metric("📦 Repuestos", len(st.session_state.db.inventario))
    with col4:
        st.metric("🔧 Soluciones Técnicas", "187+")
    
    st.success("✅ **Sistema con conocimiento técnico especializado y procedimientos verificados**")
    
    # Nueva sección
    st.subheader("🤖👨‍🔧🔧 Diagnóstico con Experiencia Técnica")
    st.info("""
    **Sistema potenciado con conocimiento técnico real de:**
    - **Aristocrat Helix/Oasis/Edge** - Plataformas modernas
    - **Bally Alpha Pro/Alpha 2** - Sistemas PC-based  
    - **Konami Concerto/KX** - Tecnología avanzada
    - **Problemas de red y touch screens** - Soluciones validadas
    - **Mantenimiento preventivo** - Basado en procedimientos técnicos
    """)
    
    # Accesos rápidos - ACTUALIZADO
    st.subheader("🚀 Accesos Rápidos")
    cols = st.columns(3)
    with cols[0]:
        if st.button("🤖 Diagnóstico IA", use_container_width=True, key="btn_diagnostico"):
            set_menu("🤖 DIAGNÓSTICO INTELIGENTE MEJORADO")
    with cols[1]:
        if st.button("👨‍🔧 Conocimiento Técnico", use_container_width=True, key="btn_conocimiento"):
            set_menu("👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO")
    with cols[2]:
        if st.button("🔧 Info Técnica", use_container_width=True, key="btn_tecnica"):
            set_menu("🔧 INFORMACIÓN TÉCNICA ESPECÍFICA")

# ==================== NUEVA SECCIÓN: INFORMACIÓN TÉCNICA ESPECÍFICA ====================
elif st.session_state.current_menu == "🔧 INFORMACIÓN TÉCNICA ESPECÍFICA":
    st.header("🔧 Información Técnica Específica")
    st.success("**📚 Base de datos técnica con herramientas integradas**")
    
    # PESTAÑAS PARA ORGANIZAR MEJOR
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Información Técnica", 
        "🔍 Búsqueda Inteligente", 
        "🧮 Calculadoras",
        "📊 Checklists",
        "📝 Notas Técnicas"
    ])
    
    with tab1:
        st.subheader("📋 Información Técnica Detallada")
        
        categoria = st.selectbox(
            "📂 **Seleccioná categoría técnica:**",
            ["RS-232 IGT", "F/O DAUG Board"],
            key="tech_category"
        )
        
        tech_ref = st.session_state.tech_reference
        
        if categoria == "RS-232 IGT":
            st.subheader("🔌 COMUNICACIÓN RS-232 IGT")
            
            # Sub-secciones para RS-232
            subseccion = st.radio(
                "**Seleccioná información específica:**",
                ["Pinout Estándar", "Configuración", "Cableado PC", "Comandos SAS", "Diagnóstico"],
                key="rs232_subs"
            )
            
            if subseccion == "Pinout Estándar":
                info = tech_ref.get_technical_info('rs232_igt', 'pinout_estandar')
            elif subseccion == "Configuración":
                info = tech_ref.get_technical_info('rs232_igt', 'configuracion_comun')
            elif subseccion == "Cableado PC":
                info = tech_ref.get_technical_info('rs232_igt', 'cableado_pc')
            elif subseccion == "Comandos SAS":
                info = tech_ref.get_technical_info('rs232_igt', 'comandos_sas_basicos')
            else:
                info = tech_ref.get_technical_info('rs232_igt', 'diagnostico_problemas')
            
            if info:
                st.markdown(f"### {info['title']}")
                for line in info['content']:
                    if any(line.startswith(char) for char in ["**", "┌", "│", "└"]):
                        st.markdown(line)
                    else:
                        st.write(line)
        
        elif categoria == "F/O DAUG Board":
            st.subheader("🔌 F/O DAUG BOARD IGT")
            
            # Sub-secciones para F/O DAUG
            subseccion = st.radio(
                "**Seleccioná información específica:**",
                ["Descripción", "Sistemas", "Problemas", "Componentes", "Diagnóstico"],
                key="fodaug_subs"
            )
            
            if subseccion == "Descripción":
                info = tech_ref.get_technical_info('fo_daug_board', 'descripcion_general')
            elif subseccion == "Sistemas":
                info = tech_ref.get_technical_info('fo_daug_board', 'sistemas_compatibles')
            elif subseccion == "Problemas":
                info = tech_ref.get_technical_info('fo_daug_board', 'problemas_comunes')
            elif subseccion == "Componentes":
                info = tech_ref.get_technical_info('fo_daug_board', 'componentes_criticos')
            else:
                info = tech_ref.get_technical_info('fo_daug_board', 'procedimiento_diagnostico')
            
            if info:
                st.markdown(f"### {info['title']}")
                for line in info['content']:
                    if line.startswith("**"):
                        st.markdown(line)
                    else:
                        st.write(line)
    
    with tab2:
        st.subheader("🔍 Búsqueda Inteligente")
        busqueda = st.text_input(
            "🔎 **Buscar en información técnica:**",
            placeholder="Ej: pinout rs232, problemas fo daug, comandos sas...",
            key="search_input"
        )
        
        if busqueda:
            with st.spinner("Buscando información..."):
                resultados = st.session_state.smart_search.search_technical_info(busqueda)
                
                if resultados and not resultados[0].startswith("🔍 No se encontraron"):
                    st.success(f"📖 Se encontraron {len(resultados)} resultados:")
                    for resultado in resultados:
                        if st.button(resultado, key=f"result_{resultado}", use_container_width=True):
                            st.info(f"**{resultado}** - Usá las pestañas de información para ver detalles completos")
                else:
                    st.info("💡 Probá con: pinout, comandos, diagnóstico, voltaje, problemas")
                    
                    # Sugerencias de búsqueda
                    st.write("**🎯 Términos sugeridos:**")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("• rs232 pinout")
                        st.write("• fo daug problemas")
                        st.write("• comandos sas")
                    with col2:
                        st.write("• diagnóstico rs232")
                        st.write("• voltaje reguladores")
                        st.write("• cableado serial")
    
    with tab3:
        st.subheader("🧮 Calculadoras Técnicas")
        
        calc_type = st.radio(
            "**Seleccioná calculadora:**",
            ["Caída de Voltaje", "Resistencia para LED"],
            key="calc_type"
        )
        
        if calc_type == "Caída de Voltaje":
            st.write("**🔋 Calculadora de Reguladores de Voltaje**")
            col1, col2, col3 = st.columns(3)
            with col1:
                vin = st.number_input("Voltaje Entrada (V)", value=12.0, min_value=0.0, max_value=50.0, key="vin")
            with col2:
                vout = st.number_input("Voltaje Salida (V)", value=5.0, min_value=0.0, max_value=50.0, key="vout")
            with col3:
                corriente = st.number_input("Corriente (A)", value=0.5, min_value=0.0, max_value=10.0, key="corriente")
            
            if st.button("🔄 Calcular Caída de Voltaje", key="calc_voltaje"):
                resultado = st.session_state.tech_calculator.calcular_caida_voltaje(vin, vout, corriente)
                if resultado:
                    st.info(f"""
                    **📊 RESULTADOS:**
                    - 🔋 Diferencia de voltaje: **{resultado['diferencia_voltaje']}V**
                    - 💡 Potencia disipada: **{resultado['potencia_disipada']}W**
                    - ⚡ Resistencia teórica: **{resultado['resistencia_teorica']}Ω**
                    - 💡 **{resultado['recomendacion']}**
                    """)
        
        elif calc_type == "Resistencia para LED":
            st.write("**💡 Calculadora para Circuitos LED**")
            col1, col2, col3 = st.columns(3)
            with col1:
                vfuente = st.number_input("Voltaje Fuente (V)", value=5.0, key="vfuente")
            with col2:
                vled = st.number_input("Voltaje LED (V)", value=2.1, key="vled")
            with col3:
                iled = st.number_input("Corriente LED (mA)", value=20, key="iled")
            
            if st.button("🔄 Calcular Resistencia LED", key="calc_led"):
                resultado = st.session_state.tech_calculator.calcular_resistencia_led(vfuente, vled, iled)
                if resultado:
                    st.info(f"""
                    **💡 RESULTADOS LED:**
                    - 🔌 Resistencia necesaria: **{resultado['resistencia']}Ω**
                    - 📈 Valor comercial: **{resultado['valor_comercial']}**
                    - 💡 Potencia: **{resultado['potencia']}W** (usar 1/4W o mayor)
                    """)
    
    with tab4:
        st.subheader("📊 Checklists de Diagnóstico")
        
        checklist_type = st.selectbox(
            "**Seleccioná checklist:**",
            ["RS-232 Comunicación", "F/O DAUG Board", "Fuente de Poder"],
            key="checklist_type"
        )
        
        if checklist_type == "RS-232 Comunicación":
            items = checklists_diagnostico['rs232']
        elif checklist_type == "F/O DAUG Board":
            items = checklists_diagnostico['fo_daug']
        else:
            items = checklists_diagnostico['fuente_poder']
        
        st.write("**✅ Marcá los items completados:**")
        checkboxes = []
        for i, item in enumerate(items):
            checked = st.checkbox(item, key=f"check_{checklist_type}_{i}")
            checkboxes.append(checked)
        
        completados = sum(checkboxes)
        st.progress(completados / len(items) if items else 0)
        st.write(f"**🎯 Progreso: {completados}/{len(items)} items completados**")
        
        if st.button("📝 Generar Reporte de Checklist", key="gen_report"):
            if completados == len(items):
                st.success("✅ ¡Checklist completo! Todas las verificaciones realizadas.")
            else:
                st.warning(f"⚠️ Checklist incompleto. Faltan {len(items) - completados} verificaciones.")
    
    with tab5:
        st.subheader("📝 Notas Técnicas Rápidas")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            nueva_nota = st.text_area(
                "**Agregar nueva nota técnica:**", 
                placeholder="Ej: Pin 2 del DB-9 es RXD (Receive Data)...",
                height=100,
                key="nueva_nota"
            )
        with col2:
            st.write("")  # Espacio
            st.write("")  # Espacio
            if st.button("💾 Guardar Nota", use_container_width=True, key="save_note"):
                if nueva_nota.strip():
                    st.session_state.technical_notes.append({
                        'fecha': datetime.now().strftime('%H:%M'),
                        'nota': nueva_nota.strip()
                    })
                    st.success("✅ Nota guardada")
                    st.rerun()
        
        if st.session_state.technical_notes:
            st.write("---")
            st.write("**📋 Últimas notas guardadas:**")
            for i, nota in enumerate(reversed(st.session_state.technical_notes[-10:])):  # Últimas 10 notas
                col1, col2 = st.columns([1, 20])
                with col1:
                    if st.button("🗑️", key=f"del_note_{i}"):
                        st.session_state.technical_notes.remove(nota)
                        st.rerun()
                with col2:
                    st.write(f"**[{nota['fecha']}]** {nota['nota']}")
        else:
            st.info("💡 Aún no hay notas guardadas. Agregá tu primera nota técnica arriba.")

# ==================== MANTENER TODAS LAS OTRAS SECCIONES EXISTENTES ====================
# (DIAGNÓSTICO INTELIGENTE, BASE DE CONOCIMIENTO, MANUALES, MÁQUINAS, INVENTARIO)
# ... todo el código existente de estas secciones se mantiene IGUAL

elif st.session_state.current_menu == "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO":
    # ... (todo el código existente igual)
    pass

elif st.session_state.current_menu == "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO":
    # ... (todo el código existente igual)
    pass

elif st.session_state.current_menu == "💰 MANUALES ACEPTADORES":
    # ... (todo el código existente igual)
    pass

elif st.session_state.current_menu == "🎰 MÁQUINAS REGISTRADAS":
    # ... (todo el código existente igual)
    pass

elif st.session_state.current_menu == "📦 INVENTARIO COMPLETO":
    # ... (todo el código existente igual)
    pass

# FOOTER ACTUALIZADO
st.markdown("---")
st.caption("🎰 **CasinoPro Expert v7.0** - Datos Técnicos + Diagnóstico IA + Herramientas Técnicas Integradas")
st.caption("🔧 **RS-232, F/O DAUG, Calculadoras, Checklists y más**")

# Botón para volver al inicio en todas las páginas (excepto inicio)
if st.session_state.current_menu != "🏠 INICIO":
    if st.button("🏠 Volver al Inicio", use_container_width=True):
        set_menu("🏠 INICIO")
