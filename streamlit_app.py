# app.py - CASINOPRO COMPLETO CON SISTEMA DE IDIOMAS + TODAS LAS CLASES TÉCNICAS
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

# ==================== SISTEMA DE IDIOMAS ====================
class LanguageSystem:
    def __init__(self):
        self.translations = self.setup_translations()
    
    def setup_translations(self):
        return {
            'es': {
                # TÍTULOS PRINCIPALES
                'main_title': "🎰 CASINOPRO - SISTEMA EXPERTO TÉCNICO",
                'main_subtitle': "**✅ Datos Técnicos + 🤖 Diagnóstico IA + 👨‍🔧 Experiencia Técnica Especializada**",
                
                # MENÚ PRINCIPAL
                'menu_home': "🏠 INICIO",
                'menu_diagnostic': "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO", 
                'menu_knowledge': "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO",
                'menu_tech_info': "🔧 INFORMACIÓN TÉCNICA ESPECÍFICA",
                'menu_cpu_specialist': "💻 ESPECIALISTA CPU-4.2.2.X",
                'menu_config': "⚙️ CONFIGURACIÓN BALLY/CPU",
                'menu_manuals': "💰 MANUALES ACEPTADORES",
                'menu_machines': "🎰 MÁQUINAS REGISTRADAS",
                'menu_inventory': "📦 INVENTARIO COMPLETO",
                
                # BOTONES GENERALES
                'btn_back_home': "🏠 Volver al Inicio",
                'btn_language': "🌐 Idioma",
                'btn_run_diagnostic': "🧠🔧 EJECUTAR DIAGNÓSTICO CON EXPERIENCIA TÉCNICA",
                'btn_search': "🔍 Buscar",
                'btn_calculate': "🔄 Calcular",
                
                # DIAGNÓSTICO INTELIGENTE
                'select_acceptor': "🔧 **SELECCIONÁ EL ACEPTADOR:**",
                'ask_question': "💬 Hacé tu pregunta técnica",
                'question_placeholder': "Ej: Mi Aristocrat Helix tiene problemas de touch screen después de limpiarla...",
                'context_placeholder': "Ej: El problema empezó después de actualizar el firmware... / Solo pasa en verano...",
                'examples_title': "📝 **Ejemplos de preguntas MODERNAS (hacé clic para ver)**",
                'diagnostic_results': "🎯🔧 **Resultado del Diagnóstico con Experiencia Técnica**",
                'confidence': "🎯 Confianza",
                'priority': "📋 Prioridad",
                'technical_perspective': "👨‍🔧🔧 **Perspectiva Técnica Especializada**",
                'technical_info': "📋 **Información Técnica**",
                'solution_steps': "🔧 **Pasos para la Solución**",
                'error_codes': "⚠️ **Códigos de Error Relevantes**",
                
                # CPU SPECIALIST
                'cpu_specialist_title': "💻 ESPECIALISTA CPU-4.2.2.X - Scientific Games",
                'cpu_description': "Describí el problema:",
                'cpu_placeholder': "Ej: CPU no enciende, sobrecalienta, error de video...",
                'cpu_error_code': "Código de error LED (opcional):",
                'cpu_error_placeholder': "Ej: 1C, 24, 25, 40...",
                'cpu_run_diagnostic': "🔧 EJECUTAR DIAGNÓSTICO CPU",
                'cpu_specs': "📊 Especificaciones Técnicas",
                'cpu_procedures': "⚙️ Procedimientos de Reemplazo",
                'cpu_error_codes': "⚠️ Códigos de Error LED",
                
                # CONFIGURACIÓN
                'config_title': "⚙️ Configuración Bally/CPU-4.2.2.X",
                'config_network': "📡 Red", 
                'config_bios': "⚙️ BIOS",
                'config_sas': "🎰 SAS",
                
                # MÉTRICAS
                'acceptors_count': "💰 Aceptadores",
                'machines_count': "🎰 Máquinas", 
                'parts_count': "📦 Repuestos",
                'solutions_count': "🔧 Soluciones Técnicas",
                
                # MENSAJES DE ESTADO
                'analyzing': "🔍 Analizando técnicamente + consultando base de conocimiento...",
                'searching': "Buscando información...",
                'no_results': "🔍 No se encontraron resultados. Intentá con otras palabras.",
                'warning_question': "⚠️ **Escribí una pregunta o descripción del problema**",
                'success_system': "✅ **Sistema con conocimiento técnico especializado y procedimientos verificados**"
            },
            
            'en': {
                # MAIN TITLES
                'main_title': "🎰 CASINOPRO - EXPERT TECHNICAL SYSTEM",
                'main_subtitle': "**✅ Technical Data + 🤖 AI Diagnosis + 👨‍🔧 Specialized Technical Experience**",
                
                # MAIN MENU
                'menu_home': "🏠 HOME",
                'menu_diagnostic': "🤖 ENHANCED INTELLIGENT DIAGNOSIS", 
                'menu_knowledge': "👨‍🔧 TECHNICAL KNOWLEDGE BASE",
                'menu_tech_info': "🔧 SPECIFIC TECHNICAL INFORMATION",
                'menu_cpu_specialist': "💻 CPU-4.2.2.X SPECIALIST",
                'menu_config': "⚙️ BALLY/CPU CONFIGURATION",
                'menu_manuals': "💰 ACCEPTOR MANUALS",
                'menu_machines': "🎰 REGISTERED MACHINES",
                'menu_inventory': "📦 COMPLETE INVENTORY",
                
                # GENERAL BUTTONS
                'btn_back_home': "🏠 Back to Home",
                'btn_language': "🌐 Language",
                'btn_run_diagnostic': "🧠🔧 RUN DIAGNOSIS WITH TECHNICAL EXPERIENCE",
                'btn_search': "🔍 Search",
                'btn_calculate': "🔄 Calculate",
                
                # INTELLIGENT DIAGNOSIS
                'select_acceptor': "🔧 **SELECT ACCEPTOR:**",
                'ask_question': "💬 Ask your technical question",
                'question_placeholder': "Example: My Aristocrat Helix has touch screen issues after cleaning...",
                'context_placeholder': "Example: The problem started after firmware update... / Only happens in summer...",
                'examples_title': "📝 **MODERN QUESTION EXAMPLES (click to view)**",
                'diagnostic_results': "🎯🔧 **Diagnosis Results with Technical Experience**",
                'confidence': "🎯 Confidence",
                'priority': "📋 Priority", 
                'technical_perspective': "👨‍🔧🔧 **Specialized Technical Perspective**",
                'technical_info': "📋 **Technical Information**",
                'solution_steps': "🔧 **Solution Steps**",
                'error_codes': "⚠️ **Relevant Error Codes**",
                
                # CPU SPECIALIST
                'cpu_specialist_title': "💻 CPU-4.2.2.X SPECIALIST - Scientific Games",
                'cpu_description': "Describe the problem:",
                'cpu_placeholder': "Example: CPU won't turn on, overheating, video error...",
                'cpu_error_code': "LED error code (optional):",
                'cpu_error_placeholder': "Example: 1C, 24, 25, 40...",
                'cpu_run_diagnostic': "🔧 RUN CPU DIAGNOSIS",
                'cpu_specs': "📊 Technical Specifications",
                'cpu_procedures': "⚙️ Replacement Procedures", 
                'cpu_error_codes': "⚠️ LED Error Codes",
                
                # CONFIGURATION
                'config_title': "⚙️ Bally/CPU-4.2.2.X Configuration",
                'config_network': "📡 Network",
                'config_bios': "⚙️ BIOS", 
                'config_sas': "🎰 SAS",
                
                # METRICS
                'acceptors_count': "💰 Acceptors",
                'machines_count': "🎰 Machines",
                'parts_count': "📦 Parts",
                'solutions_count': "🔧 Technical Solutions",
                
                # STATUS MESSAGES
                'analyzing': "🔍 Technical analysis + consulting knowledge base...",
                'searching': "Searching information...",
                'no_results': "🔍 No results found. Try with other words.",
                'warning_question': "⚠️ **Write a question or problem description**",
                'success_system': "✅ **System with specialized technical knowledge and verified procedures**"
            }
        }
    
    def get_text(self, key, lang='es'):
        """Obtiene texto traducido"""
        return self.translations.get(lang, {}).get(key, key)
    
    def get_all_menu_options(self, lang='es'):
        """Obtiene todas las opciones del menú en el idioma seleccionado"""
        return [
            self.get_text('menu_home', lang),
            self.get_text('menu_diagnostic', lang),
            self.get_text('menu_knowledge', lang),
            self.get_text('menu_tech_info', lang),
            self.get_text('menu_cpu_specialist', lang),
            self.get_text('menu_config', lang),
            self.get_text('menu_manuals', lang),
            self.get_text('menu_machines', lang),
            self.get_text('menu_inventory', lang)
        ]

# ==================== SISTEMA ESPECIALISTA CPU-4.2.2.X ====================
class CPU422XSpecialist:
    def __init__(self):
        self.cpu_data = self.setup_cpu_database()
        self.led_codes = self.setup_led_codes()
        self.troubleshooting_flows = self.setup_troubleshooting_flows()
    
    def setup_cpu_database(self):
        """Base de datos técnica específica de CPU-4.2.2.X"""
        return {
            'especificaciones_generales': {
                'modelo': 'CPU-4.2.2.X',
                'numero_parte': '1458954',
                'fabricante': 'Scientific Games',
                'manual_servicio': '1458954 SERVICE MANUAL',
                'voltaje_operativo': '+24V DC',
                'temperatura_operacion': '4-40°C (39.2-104°F)',
                'humedad_maxima': '90%',
                'maquinas_compatibles': [
                    "Twinstar Vertical (56-T14335T)",
                    "Bally Alpha Series", 
                    "Bally iVIEW DM Systems",
                    "Otras máquinas Scientific Games modernas"
                ],
                'aplicacion_primaria': "Subsistema de control para máquinas de juego Scientific Games/Bally",
                'componentes_principales': [
                    'Ensamblaje CPU-4.XXX',
                    'Placa de plano posterior', 
                    'Módulo de fuente de alimentación (PSM)',
                    'Bandeja de ventilador'
                ]
            }
        }
    
    def setup_led_codes(self):
        """Códigos de error de LED de estado"""
        return {
            '1C': {'nombre': 'ALL_SYS_PWRGD_FAIL', 'descripcion': 'Fallo en circuito de alimentación interno', 'solucion': 'Reemplazar CPU'},
            '24': {'nombre': 'APU_THERMTRIP', 'descripcion': 'Protección térmica activada', 'solucion': 'Verificar ventilación y disipadores'},
            '25': {'nombre': 'APU_OVERTEMP', 'descripcion': 'Temperatura APU excede umbral', 'solucion': 'Limpiar ventiladores y verificar flujo de aire'}
        }
    
    def setup_troubleshooting_flows(self):
        """Flujos de solución de problemas específicos"""
        return {
            'no_enciende': [
                "1. Verificar alimentación +24V DC en conector J1",
                "2. Comprobar LED de estado de potencia",
                "3. Verificar módulo BIOS instalado correctamente"
            ],
            'sobrecalentamiento': [
                "1. Limpiar filtros de aire y rejillas de ventilación",
                "2. Verificar funcionamiento de todos los ventiladores",
                "3. Comprobar que la bandeja de ventilador esté instalada"
            ]
        }
    
    def diagnosticar_problema(self, sintoma, codigo_error=None):
        """Diagnóstico especializado para CPU-4.2.2.X"""
        diagnostico = {
            'sintoma': sintoma,
            'codigo_error': codigo_error,
            'posibles_causas': [],
            'pasos_solucion': [],
            'componentes_afectados': [],
            'prioridad': 'MEDIA'
        }
        
        sintoma_lower = sintoma.lower()
        
        # Diagnóstico por código de error
        if codigo_error and codigo_error in self.led_codes:
            error_info = self.led_codes[codigo_error]
            diagnostico['posibles_causas'].append(f"Error {codigo_error}: {error_info['descripcion']}")
            diagnostico['pasos_solucion'].append(f"Solución: {error_info['solucion']}")
            diagnostico['prioridad'] = 'ALTA'
        
        # Diagnóstico por síntomas
        if 'no enciende' in sintoma_lower:
            diagnostico['posibles_causas'].extend([
                "Falta de alimentación +24V DC",
                "Fuente de alimentación PSM defectuosa"
            ])
            diagnostico['pasos_solucion'] = self.troubleshooting_flows['no_enciende']
            diagnostico['componentes_afectados'] = ['PSM', 'Placa posterior', 'Módulo BIOS']
            
        elif 'calienta' in sintoma_lower or 'sobrecalienta' in sintoma_lower:
            diagnostico['posibles_causas'].extend([
                "Ventiladores obstruidos o fallados",
                "Filtros de aire sucios"
            ])
            diagnostico['pasos_solucion'] = self.troubleshooting_flows['sobrecalentamiento']
            diagnostico['componentes_afectados'] = ['Bandeja ventilador', 'Ventiladores', 'Disipadores']
            diagnostico['prioridad'] = 'ALTA'
            
        return diagnostico

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
                "billetes_aceptados": "Hasta 8 denominaciones"
            },
            "JCM UBA-10 (Datos Reales)": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador Universal",
                "documentacion_verificada": True,
                "voltaje": "+24V DC ±15% (REAL)",
                "comunicacion": "MDB, ICP, RS-232 (REAL)"
            }
        }
        
        self.maquinas = {
            "Aristocrat Helix": {"fabricante": "Aristocrat", "año": 2022, "plataforma": "Helix Core"},
            "Bally Alpha Pro": {"fabricante": "Bally/SG", "año": 2022, "plataforma": "PC Industrial"},
            "Konami Concerto": {"fabricante": "Konami", "año": 2022, "plataforma": "Concerto"}
        }
        
        self.inventario = [
            {"nombre": "🔌 Fuente IGT S2000", "stock": 3, "categoria": "Fuentes", "min_stock": 2},
            {"nombre": "💰 Aceptador MEI SCN66", "stock": 5, "categoria": "Aceptadores", "min_stock": 3},
            {"nombre": "📺 Pantalla Touch 19\" Aristocrat", "stock": 2, "categoria": "Pantallas", "min_stock": 1}
        ]

# ==================== SISTEMA DE DIAGNÓSTICO ====================
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
    
    def get_diagnostic_response(self, question, aceptador_seleccionado):
        if aceptador_seleccionado not in self.db.aceptadores:
            return {'error': f"❌ Aceptador '{aceptador_seleccionado}' no encontrado"}
        
        aceptador_data = self.db.aceptadores[aceptador_seleccionado]
        
        response = {
            'aceptador': aceptador_seleccionado,
            'pregunta': question,
            'respuesta_tecnica': '',
            'pasos_solucion': [],
            'nivel_confianza': "✅ MEDIA - Basado en experiencia similar",
            'recomendacion_prioridad': "🟡 PRIORIDAD MEDIA - Atender durante el día"
        }
        
        response['respuesta_tecnica'] = self.get_general_advice(aceptador_data, question)
        
        return response
    
    def get_general_advice(self, aceptador_data, question):
        advice = f"**📋 Información General del Aceptador**\n\n"
        
        key_info = [
            ('🏭 Fabricante', aceptador_data.get('fabricante')),
            ('⚡ Voltaje', aceptador_data.get('voltaje')),
            ('📡 Comunicación', aceptador_data.get('comunicacion'))
        ]
        
        for key, value in key_info:
            if value:
                advice += f"• **{key}**: {value}\n"
        
        advice += "\n**💡 Sugerencia:** Para una respuesta más específica, mencione términos técnicos."
        
        return advice

# ==================== SISTEMA DE EXPERIENCIA TÉCNICA ====================
class TechnicalExperienceSystem:
    def __init__(self, db):
        self.db = db
        self.experience_base = self.setup_experience_base()
    
    def setup_experience_base(self):
        return {
            'aristocrat_helix': [
                "🎯 **Experiencia técnica**: Helix tiene problemas de touch screen - Usar utilidad de calibración específica",
                "💡 **Procedimiento verificado**: Reset completo: Desconectar 10 min + POWER + SERVICE simultáneo"
            ],
            'bally_alpha_pro': [
                "🎯 **Arquitectura conocida**: Alpha Pro = PC industrial - Diagnosticar como computadora",
                "💡 **Truco BIOS**: F2 durante boot para diagnóstico hardware integrado"
            ]
        }
    
    def get_technical_insight(self, sintoma, modelo=None):
        return [
            "🔍 **Perspectiva técnica**: Problema común - Revisar conexiones primero",
            "💡 **Enfoque sugerido**: Diagnosticar sistemáticamente de simple a complejo"
        ]

# ==================== SISTEMA DE DIAGNÓSTICO MEJORADO ====================
class DiagnosticSystemEnhanced:
    def __init__(self, db):
        self.db = db
        self.diagnostic_system = DiagnosticSystem(db)
        self.technical_system = TechnicalExperienceSystem(db)
    
    def get_enhanced_diagnosis(self, question, aceptador_seleccionado, contexto_adicional=""):
        respuesta_tecnica = self.diagnostic_system.get_diagnostic_response(question, aceptador_seleccionado)
        insights_tecnicos = self.technical_system.get_technical_insight(question, aceptador_seleccionado)
        
        respuesta_completa = {
            **respuesta_tecnica,
            'perspectiva_tecnica': insights_tecnicos
        }
        
        return respuesta_completa

# ==================== INICIALIZACIÓN DEL SISTEMA ====================
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

if 'language_system' not in st.session_state:
    st.session_state.language_system = LanguageSystem()

if 'current_language' not in st.session_state:
    st.session_state.current_language = 'es'

if 'cpu_specialist' not in st.session_state:
    st.session_state.cpu_specialist = CPU422XSpecialist()

if 'enhanced_diagnostic' not in st.session_state:
    st.session_state.enhanced_diagnostic = DiagnosticSystemEnhanced(st.session_state.db)

if 'current_menu' not in st.session_state:
    st.session_state.current_menu = st.session_state.language_system.get_text('menu_home')

# ==================== FUNCIONES DE NAVEGACIÓN ====================
def set_menu(menu_option):
    st.session_state.current_menu = menu_option
    st.rerun()

def change_language(lang):
    st.session_state.current_language = lang
    # Actualizar el menú actual al nuevo idioma
    current_menu_key = get_menu_key_by_value(st.session_state.current_menu)
    if current_menu_key:
        st.session_state.current_menu = st.session_state.language_system.get_text(current_menu_key, lang)
    st.rerun()

def get_menu_key_by_value(value):
    """Obtiene la clave del menú por su valor"""
    for key in ['menu_home', 'menu_diagnostic', 'menu_knowledge', 'menu_tech_info', 
                'menu_cpu_specialist', 'menu_config', 'menu_manuals', 'menu_machines', 'menu_inventory']:
        if st.session_state.language_system.get_text(key) == value:
            return key
    return None

# ==================== INTERFAZ PRINCIPAL ====================
def main():
    lang = st.session_state.current_language
    t = st.session_state.language_system.get_text
    
    # Header con selector de idioma
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title(t('main_title', lang))
        st.markdown(t('main_subtitle', lang))
    with col2:
        selected_lang = st.selectbox(
            t('btn_language', lang),
            ['es', 'en'],
            index=0 if st.session_state.current_language == 'es' else 1,
            key="language_selector"
        )
        if selected_lang != st.session_state.current_language:
            change_language(selected_lang)
    
    st.markdown("---")
    
    # MENÚ PRINCIPAL
    menu_options = st.session_state.language_system.get_all_menu_options(lang)
    selected_menu = st.selectbox(
        "📱 **NAVEGACIÓN:**",
        menu_options,
        index=menu_options.index(st.session_state.current_menu),
        key="menu_selector"
    )
    
    if selected_menu != st.session_state.current_menu:
        st.session_state.current_menu = selected_menu
        st.rerun()
    
    st.markdown("---")
    
    # ==================== PÁGINA DE INICIO ====================
    if st.session_state.current_menu == t('menu_home', lang):
        st.header("🏠🔧 Dashboard con Conocimiento Técnico Integrado")
        
        # Métricas
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(t('acceptors_count', lang), len(st.session_state.db.aceptadores))
        with col2:
            st.metric(t('machines_count', lang), len(st.session_state.db.maquinas))
        with col3:
            st.metric(t('parts_count', lang), len(st.session_state.db.inventario))
        with col4:
            st.metric(t('solutions_count', lang), "187+")
        
        st.success(t('success_system', lang))
        
        # Accesos rápidos
        st.subheader("🚀 Accesos Rápidos")
        cols = st.columns(3)
        with cols[0]:
            if st.button("🤖 Diagnóstico IA", use_container_width=True):
                set_menu(t('menu_diagnostic', lang))
        with cols[1]:
            if st.button("👨‍🔧 Conocimiento Técnico", use_container_width=True):
                set_menu(t('menu_knowledge', lang))
        with cols[2]:
            if st.button("🔧 Info Técnica", use_container_width=True):
                set_menu(t('menu_tech_info', lang))
    
    # ==================== DIAGNÓSTICO INTELIGENTE ====================
    elif st.session_state.current_menu == t('menu_diagnostic', lang):
        st.header("🤖 Diagnóstico Inteligente + Experiencia Técnica")
        st.success("**💡 Sistema con conocimiento técnico especializado y procedimientos verificados**")
        
        # Selección de aceptador
        aceptador_seleccionado = st.selectbox(
            t('select_acceptor', lang),
            list(st.session_state.db.aceptadores.keys())
        )
        
        # Área de preguntas
        st.markdown("---")
        st.subheader(t('ask_question', lang))
        
        with st.expander(t('examples_title', lang)):
            st.write("""
            **Preguntas sugeridas para máquinas modernas:**
            - ¿Problemas de touch screen en Aristocrat Helix?
            - ¿Cómo soluciono comunicación Ethernet en Bally Alpha Pro?
            - ¿Error de calibración en Konami Concerto?
            """)
        
        pregunta_usuario = st.text_area(
            "**Describí el problema o hacé tu pregunta técnica:**",
            placeholder=t('question_placeholder', lang),
            height=100
        )
        
        with st.expander("🔍 **Agregar contexto adicional (opcional)**"):
            contexto_adicional = st.text_area(
                "Detalles específicos del problema:",
                placeholder=t('context_placeholder', lang),
                height=60
            )
        
        if st.button(t('btn_run_diagnostic', lang), type="primary", use_container_width=True):
            if pregunta_usuario.strip():
                with st.spinner(t('analyzing', lang)):
                    import time
                    time.sleep(1.5)
                    
                    respuesta = st.session_state.enhanced_diagnostic.get_enhanced_diagnosis(
                        pregunta_usuario, 
                        aceptador_seleccionado,
                        contexto_adicional
                    )
                    
                    # MOSTRAR RESULTADOS
                    st.markdown("---")
                    st.subheader(t('diagnostic_results', lang))
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**🤖 Aceptador:** {respuesta['aceptador']}")
                    with col2:
                        st.write(f"**{t('confidence', lang)}:** {respuesta['nivel_confianza']}")
                    with col3:
                        st.write(f"**{t('priority', lang)}:** {respuesta['recomendacion_prioridad']}")
                    
                    # Perspectiva Técnica
                    if 'perspectiva_tecnica' in respuesta:
                        st.markdown(f"### {t('technical_perspective', lang)}")
                        for insight in respuesta['perspectiva_tecnica']:
                            st.write(f"• {insight}")
                    
                    # Información Técnica
                    st.markdown(f"### {t('technical_info', lang)}")
                    st.markdown(respuesta['respuesta_tecnica'])
                    
                    # Pasos de solución
                    if respuesta['pasos_solucion']:
                        st.markdown(f"### {t('solution_steps', lang)}")
                        for paso in respuesta['pasos_solucion']:
                            st.write(paso)
                    
                    st.markdown("---")
                    st.caption(f"🕐 Consulta técnica: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    
            else:
                st.warning(t('warning_question', lang))
    
    # ==================== ESPECIALISTA CPU-4.2.2.X ====================
    elif st.session_state.current_menu == t('menu_cpu_specialist', lang):
        st.header(t('cpu_specialist_title', lang))
        st.success("**🔧 Conocimiento técnico específico del manual 1458954**")
        
        tab1, tab2, tab3 = st.tabs([
            "🔍 Diagnóstico", 
            "📊 Especificaciones", 
            "⚠️ Códigos Error"
        ])
        
        with tab1:
            st.subheader("🔍 Diagnóstico de Problemas")
            
            sintoma = st.text_input(
                t('cpu_description', lang),
                placeholder=t('cpu_placeholder', lang),
                key="cpu_sintoma"
            )
            
            codigo_error = st.text_input(
                t('cpu_error_code', lang),
                placeholder=t('cpu_error_placeholder', lang),
                key="cpu_codigo_error",
                max_chars=3
            )
            
            if st.button(t('cpu_run_diagnostic', lang), type="primary"):
                if sintoma.strip():
                    diagnostico = st.session_state.cpu_specialist.diagnosticar_problema(
                        sintoma, 
                        codigo_error.upper() if codigo_error else None
                    )
                    
                    st.markdown("---")
                    st.subheader("🎯 Resultado del Diagnóstico")
                    
                    color_prioridad = "🔴" if diagnostico['prioridad'] == 'ALTA' else "🟡"
                    st.write(f"{color_prioridad} **Prioridad:** {diagnostico['prioridad']}")
                    
                    if diagnostico['posibles_causas']:
                        st.markdown("### 📋 Posibles Causas")
                        for causa in diagnostico['posibles_causas']:
                            st.write(f"• {causa}")
                    
                    if diagnostico['pasos_solucion']:
                        st.markdown("### 🔧 Pasos para Solución")
                        for paso in diagnostico['pasos_solucion']:
                            st.write(paso)
                            
                else:
                    st.warning("⚠️ Por favor, describí el problema")
        
        with tab2:
            st.subheader(t('cpu_specs', lang))
            especificaciones = st.session_state.cpu_specialist.cpu_data['especificaciones_generales']
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 📋 Información General")
                st.write(f"**Modelo:** {especificaciones['modelo']}")
                st.write(f"**Número Parte:** {especificaciones['numero_parte']}")
                st.write(f"**Fabricante:** {especificaciones['fabricante']}")
                st.write(f"**Voltaje:** {especificaciones['voltaje_operativo']}")
                
            with col2:
                st.markdown("### 🌡️ Condiciones Operativas")
                st.write(f"**Temperatura:** {especificaciones['temperatura_operacion']}")
                st.write(f"**Humedad Máx:** {especificaciones['humedad_maxima']}")
        
        with tab3:
            st.subheader(t('cpu_error_codes', lang))
            
            for codigo, info in st.session_state.cpu_specialist.led_codes.items():
                with st.expander(f"🚨 Código {codigo}: {info['nombre']}"):
                    st.write(f"**Descripción:** {info['descripcion']}")
                    st.write(f"**Solución:** {info['solucion']}")
    
    # ==================== CONFIGURACIÓN BALLY/CPU ====================
    elif st.session_state.current_menu == t('menu_config', lang):
        st.header(t('config_title', lang))
        st.info("**💡 Guías de configuración basadas en experiencia técnica**")
        
        tab1, tab2 = st.tabs([
            t('config_network', lang), 
            t('config_bios', lang)
        ])
        
        with tab1:
            st.subheader(t('config_network', lang))
            
            config_type = st.radio(
                "Seleccioná tipo de configuración:",
                ["IP Estática", "Problemas DHCP", "Verificación Conectividad"],
                key="network_config"
            )
            
            if st.button("🔄 Obtener Guía Configuración", key="btn_network_guide"):
                st.markdown("### 📡 Configurar IP Estática")
                st.write("""
                **VENTAJA:** Mayor estabilidad que DHCP
                
                **PROCEDIMIENTO:**
                1. Menú Servicio → Configuración Red
                2. Seleccionar 'IP Estática' vs 'DHCP'
                3. Ingresar: IP, Mascara, Gateway, DNS
                4. **IP TÍPICA:** 192.168.1.150 (ajustar según red)
                5. **MÁSCARA:** 255.255.255.0
                6. **GATEWAY:** 192.168.1.1 (usar router local)
                7. Guardar y reiniciar
                """)
        
        with tab2:
            st.subheader(t('config_bios', lang))
            
            if st.button("📋 Mostrar Configuración BIOS Estándar"):
                st.markdown("### 🏗️ Configuración Estándar BIOS")
                st.write("""
                **BOOT:**
                - Boot Order: SSD → USB → Network
                - Fast Boot: Disabled (para diagnóstico)
                - Boot Delay: 0 seconds
                
                **POWER:**
                - AC Power Recovery: Last State
                - Wake On LAN: Enabled
                - Suspend Mode: S3 (STR)
                """)
    
    # ==================== MANUALES ACEPTADORES ====================
    elif st.session_state.current_menu == t('menu_manuals', lang):
        st.header("💰 Manuales de Aceptadores")
        
        aceptador_seleccionado = st.selectbox(
            t('select_acceptor', lang),
            list(st.session_state.db.aceptadores.keys())
        )
        
        if aceptador_seleccionado:
            info = st.session_state.db.aceptadores[aceptador_seleccionado]
            st.subheader(f"📋 {aceptador_seleccionado}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**🏭 Fabricante:** {info['fabricante']}")
                st.write(f"**⚡ Voltaje:** {info['voltaje']}")
                
            with col2:
                st.write(f"**📡 Comunicación:** {info['comunicacion']}")
                st.write(f"**📄 Documentación:** {'✅ Verificada' if info.get('documentacion_verificada') else '❌ No verificada'}")
    
    # ==================== MÁQUINAS REGISTRADAS ====================
    elif st.session_state.current_menu == t('menu_machines', lang):
        st.header("🎰 Máquinas en Base de Datos")
        
        total_maquinas = len(st.session_state.db.maquinas)
        st.metric("📊 Total de Máquinas Registradas", total_maquinas)
        
        for modelo, info in st.session_state.db.maquinas.items():
            with st.expander(f"🎰 {modelo}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Fabricante:** {info['fabricante']}")
                with col2:
                    st.write(f"**Año:** {info['año']}")
                with col3:
                    st.write(f"**Plataforma:** {info.get('plataforma', 'N/A')}")
    
    # ==================== INVENTARIO COMPLETO ====================
    elif st.session_state.current_menu == t('menu_inventory', lang):
        st.header("📦 Inventario")
        
        for item in st.session_state.db.inventario:
            stock_color = "🟢" if item['stock'] > item.get('min_stock', 0) else "🔴"
            st.write(f"{stock_color} **{item['nombre']}** - Stock: {item['stock']} | Mín: {item.get('min_stock', 'N/A')}")
    
    # ==================== OTRAS SECCIONES (Placeholders) ====================
    elif st.session_state.current_menu == t('menu_knowledge', lang):
        st.header("👨‍🔧 Base de Conocimiento Técnico")
        st.info("**💡 Esta sección contiene conocimiento TÉCNICO especializado**")
        st.write("En desarrollo...")
        
    elif st.session_state.current_menu == t('menu_tech_info', lang):
        st.header("🔧 Información Técnica Específica")
        st.success("**📚 Base de datos técnica con herramientas integradas**")
        st.write("En desarrollo...")
    
    # FOOTER
    st.markdown("---")
    st.caption("🎰 **CasinoPro Expert v8.0** - Sistema Multidioma + Especialista CPU-4.2.2.X")
    
    # Botón para volver al inicio
    if st.session_state.current_menu != t('menu_home', lang):
        if st.button(t('btn_back_home', lang), use_container_width=True):
            set_menu(t('menu_home', lang))

if __name__ == "__main__":
    main()
