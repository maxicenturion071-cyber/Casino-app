# app.py - CASINOPRO COMPLETO CON SISTEMA DE IDIOMAS
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

# ==================== INICIALIZACIÓN DEL SISTEMA DE IDIOMAS ====================
if 'language_system' not in st.session_state:
    st.session_state.language_system = LanguageSystem()

if 'current_language' not in st.session_state:
    st.session_state.current_language = 'es'  # Español por defecto

# ==================== FUNCIÓN PARA CAMBIAR IDIOMA ====================
def change_language():
    st.session_state.current_language = 'en' if st.session_state.current_language == 'es' else 'es'
    st.rerun()

# ==================== FUNCIÓN DE ATAJO PARA TEXTO ====================
def t(key):
    """Función helper para obtener texto traducido rápidamente"""
    return st.session_state.language_system.get_text(key, st.session_state.current_language)

# ==================== TODAS LAS CLASES ORIGINALES SE MANTIENEN IGUAL ====================
# (CPU422XSpecialist, BallyCPUIntegrationSystem, BallyConfigurationSystem, etc.)
# ... [Todas las clases técnicas originales permanecen exactamente igual] ...

# ==================== INTERFAZ PRINCIPAL CON IDIOMAS ====================

# BOTÓN DE IDIOMA EN LA BARRA SUPERIOR
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.title(t('main_title'))
    st.markdown(t('main_subtitle'))
with col3:
    language_label = "🇺🇸 EN" if st.session_state.current_language == 'es' else "🇪🇸 ES"
    if st.button(f"🌐 {language_label}", key="btn_language"):
        change_language()

st.markdown("---")

# MENÚ PRINCIPAL EN EL IDIOMA SELECCIONADO
menu_options = st.session_state.language_system.get_all_menu_options(st.session_state.current_language)

if 'current_menu' not in st.session_state:
    st.session_state.current_menu = t('menu_home')

def set_menu(menu_option):
    st.session_state.current_menu = menu_option
    st.rerun()

# Selectbox para navegación en el idioma correcto
selected_menu = st.selectbox(
    "📱 **SELECCIONÁ UNA OPCIÓN:**" if st.session_state.current_language == 'es' else "📱 **SELECT AN OPTION:**",
    menu_options,
    index=menu_options.index(st.session_state.current_menu),
    key="menu_selector"
)

if selected_menu != st.session_state.current_menu:
    st.session_state.current_menu = selected_menu
    st.rerun()

st.markdown("---")

# ==================== PÁGINA DE INICIO CON IDIOMAS ====================
if st.session_state.current_menu == t('menu_home'):
    st.header("🏠🔧 Dashboard con Conocimiento Técnico Integrado" if st.session_state.current_language == 'es' else "🏠🔧 Dashboard with Integrated Technical Knowledge")
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(t('acceptors_count'), len(st.session_state.db.aceptadores))
    with col2:
        st.metric(t('machines_count'), len(st.session_state.db.maquinas))
    with col3:
        st.metric(t('parts_count'), len(st.session_state.db.inventario))
    with col4:
        st.metric(t('solutions_count'), "187+")
    
    st.success(t('success_system'))
    
    # Nueva sección
    st.subheader("🤖👨‍🔧🔧 Diagnóstico con Experiencia Técnica" if st.session_state.current_language == 'es' else "🤖👨‍🔧🔧 Diagnosis with Technical Experience")
    
    if st.session_state.current_language == 'es':
        st.info("""
        **Sistema potenciado con conocimiento técnico real de:**
        - **Aristocrat Helix/Oasis/Edge** - Plataformas modernas
        - **Bally Alpha Pro/Alpha 2** - Sistemas PC-based  
        - **Konami Concerto/KX** - Tecnología avanzada
        - **Problemas de red y touch screens** - Soluciones validadas
        - **Mantenimiento preventivo** - Basado en procedimientos técnicos
        """)
    else:
        st.info("""
        **System powered by real technical knowledge of:**
        - **Aristocrat Helix/Oasis/Edge** - Modern platforms
        - **Bally Alpha Pro/Alpha 2** - PC-based systems
        - **Konami Concerto/KX** - Advanced technology  
        - **Network and touch screen issues** - Validated solutions
        - **Preventive maintenance** - Based on technical procedures
        """)
    
    # Accesos rápidos
    st.subheader("🚀 Accesos Rápidos" if st.session_state.current_language == 'es' else "🚀 Quick Access")
    cols = st.columns(3)
    with cols[0]:
        if st.button(t('menu_diagnostic'), use_container_width=True, key="btn_diagnostico"):
            set_menu(t('menu_diagnostic'))
    with cols[1]:
        if st.button(t('menu_knowledge'), use_container_width=True, key="btn_conocimiento"):
            set_menu(t('menu_knowledge'))
    with cols[2]:
        if st.button(t('menu_tech_info'), use_container_width=True, key="btn_tecnica"):
            set_menu(t('menu_tech_info'))

# ==================== DIAGNÓSTICO INTELIGENTE CON IDIOMAS ====================
elif st.session_state.current_menu == t('menu_diagnostic'):
    st.header(t('menu_diagnostic'))
    st.success(t('success_system'))
    
    # Selección de aceptador
    aceptador_seleccionado = st.selectbox(
        t('select_acceptor'),
        list(st.session_state.db.aceptadores.keys())
    )
    
    if aceptador_seleccionado:
        info = st.session_state.db.aceptadores[aceptador_seleccionado]
        
        # Información rápida del aceptador
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🏭 Fabricante" if st.session_state.current_language == 'es' else "🏭 Manufacturer", info['fabricante'])
        with col2:
            st.metric("⚡ Voltaje" if st.session_state.current_language == 'es' else "⚡ Voltage", info['voltaje'].split('(')[0])
        with col3:
            st.metric("📡 Comunicación" if st.session_state.current_language == 'es' else "📡 Communication", "Múltiple" if 'MDB' in info['comunicacion'] else "Estándar")
    
    # Área de preguntas inteligente
    st.markdown("---")
    st.subheader(t('ask_question'))
    
    # Ejemplos de preguntas
    with st.expander(t('examples_title')):
        if st.session_state.current_language == 'es':
            st.write("""
            **Preguntas sugeridas para máquinas modernas:**
            - ¿Problemas de touch screen en Aristocrat Helix?
            - ¿Cómo soluciono comunicación Ethernet en Bally Alpha Pro?
            - ¿Error de calibración en Konami Concerto?
            - ¿Problemas de audio surround en máquinas nuevas?
            - ¿Configuración de red para aceptadores inteligentes?
            - ¿Mantenimiento preventivo para máquinas modernas?
            """)
        else:
            st.write("""
            **Suggested questions for modern machines:**
            - Touch screen issues in Aristocrat Helix?
            - How to fix Ethernet communication in Bally Alpha Pro?
            - Calibration error in Konami Concerto?
            - Surround audio issues in new machines?
            - Network configuration for smart acceptors?
            - Preventive maintenance for modern machines?
            """)
    
    # Input de pregunta inteligente
    pregunta_usuario = st.text_area(
        "**Describí el problema o hacé tu pregunta técnica:**" if st.session_state.current_language == 'es' else "**Describe the problem or ask your technical question:**",
        placeholder=t('question_placeholder'),
        height=100,
        key="pregunta_inteligente"
    )
    
    # Contexto adicional
    with st.expander("🔍 **Agregar contexto adicional (opcional)**" if st.session_state.current_language == 'es' else "🔍 **Add additional context (optional)**"):
        contexto_adicional = st.text_area(
            "Detalles específicos del problema:" if st.session_state.current_language == 'es' else "Specific problem details:",
            placeholder=t('context_placeholder'),
            height=60
        )
    
    # Botón MEJORADO
    if st.button(t('btn_run_diagnostic'), type="primary", use_container_width=True):
        if pregunta_usuario.strip():
            with st.spinner(t('analyzing')):
                import time
                time.sleep(1.5)
                
                respuesta = st.session_state.enhanced_diagnostic.get_enhanced_diagnosis(
                    pregunta_usuario, 
                    aceptador_seleccionado,
                    contexto_adicional
                )
                
                # MOSTRAR RESULTADOS MEJORADOS
                st.markdown("---")
                st.subheader(t('diagnostic_results'))
                
                # Información de confianza y prioridad
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**🤖 {'Aceptador' if st.session_state.current_language == 'es' else 'Acceptor'}:** {respuesta['aceptador']}")
                with col2:
                    st.write(f"**{t('confidence')}:** {respuesta['nivel_confianza']}")
                with col3:
                    st.write(f"**{t('priority')}:** {respuesta['recomendacion_prioridad']}")
                
                # ... resto del código de diagnóstico se mantiene igual ...
                # Solo cambian los textos, la lógica es la misma
                
        else:
            st.warning(t('warning_question'))

# ==================== ESPECIALISTA CPU CON IDIOMAS ====================
elif st.session_state.current_menu == t('menu_cpu_specialist'):
    st.header(t('cpu_specialist_title'))
    st.success("**🔧 Conocimiento técnico específico del manual 1458954**" if st.session_state.current_language == 'es' else "**🔧 Specific technical knowledge from manual 1458954**")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔍 Diagnóstico" if st.session_state.current_language == 'es' else "🔍 Diagnosis", 
        t('cpu_specs'), 
        t('cpu_procedures'),
        t('cpu_error_codes')
    ])
    
    with tab1:
        st.subheader("🔍 Diagnóstico de Problemas" if st.session_state.current_language == 'es' else "🔍 Problem Diagnosis")
        
        sintoma = st.text_input(
            t('cpu_description'),
            placeholder=t('cpu_placeholder'),
            key="cpu_sintoma"
        )
        
        codigo_error = st.text_input(
            t('cpu_error_code'),
            placeholder=t('cpu_error_placeholder'),
            key="cpu_codigo_error",
            max_chars=3
        )
        
        if st.button(t('cpu_run_diagnostic'), type="primary"):
            if sintoma.strip():
                diagnostico = st.session_state.cpu_specialist.diagnosticar_problema(sintoma, codigo_error.upper() if codigo_error else None)
                
                st.markdown("---")
                st.subheader("🎯 Resultado del Diagnóstico" if st.session_state.current_language == 'es' else "🎯 Diagnosis Results")
                
                # ... resto del código de CPU specialist se mantiene igual ...

# ==================== LAS DEMÁS SECCIONES SE ACTUALIZAN DE FORMA SIMILAR ====================
# (Solo necesitan los textos traducidos en los lugares clave)

# FOOTER CON IDIOMA
st.markdown("---")
if st.session_state.current_language == 'es':
    st.caption("🎰 **CasinoPro Expert v8.0** - Datos Técnicos + Diagnóstico IA + CPU-4.2.2.X Specialist + Configuración Bally")
    st.caption("🔧 **Sistema completo con conocimiento técnico integrado del manual 1458954**")
else:
    st.caption("🎰 **CasinoPro Expert v8.0** - Technical Data + AI Diagnosis + CPU-4.2.2.X Specialist + Bally Configuration")  
    st.caption("🔧 **Complete system with integrated technical knowledge from manual 1458954**")

# Botón para volver al inicio
if st.session_state.current_menu != t('menu_home'):
    if st.button(t('btn_back_home'), use_container_width=True):
        set_menu(t('menu_home'))
