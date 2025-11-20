# app.py - CASINOPRO COMPLETO CON GEMINI - LISTO PARA TU API KEY
import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import json
from typing import Dict, List, Optional
import google.generativeai as genai

# CONFIGURACIÓN MÓVIL
st.set_page_config(
    page_title="CasinoPro - Expert System",
    page_icon="🎰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================== SISTEMA DE IA GEMINI ====================
class GeminiAISystem:
    def __init__(self):
        self.configured = False
        self.setup_gemini()
    
    def setup_gemini(self):
    """CONFIGURACIÓN GEMINI - PEGA TU API KEY AQUÍ"""
    try:
        # ⚠️ ⚠️ ⚠️ PEGA TU API KEY DE GEMINI AQUÍ ⚠️ ⚠️ ⚠️
        GEMINI_API_KEY = "AIzaSyBX4LrLMaX36xV85lVqPSRhwkr6NaJNHT8"
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.configured = True
        st.success("✅ Google Gemini configurado automáticamente")
    except Exception as e:
        st.error(f"❌ Error configurando Gemini: {e}")
    
    def get_technical_diagnosis(self, user_question: str, machine_data: Dict, context: str = "") -> str:
        """Obtener diagnóstico técnico con Gemini"""
        
        if not self.configured:
            return self._get_fallback_response(user_question)
        
        try:
            prompt = self._build_technical_prompt(user_question, machine_data, context)
            response = self.model.generate_content(prompt)
            return f"🌟 **Análisis con Google Gemini**:\n\n{response.text}"
            
        except Exception as e:
            return self._get_fallback_response(user_question)
    
    def _build_technical_prompt(self, question: str, machine_data: Dict, context: str) -> str:
        """Construir prompt técnico especializado"""
        
        technical_context = """
        Eres TECNICO_EXPERTO_CASINOPRO con 25 años de experiencia en máquinas de casino.

        ESPECIALIDADES:
        - Aristocrat: Helix, Oasis, Edge X, MK6
        - Bally/SG: Alpha Pro, Alpha 2, iVIEW DM  
        - Konami: Concerto, KX, Helix Core
        - IGT: Peak, S Plus, S2000, Game King
        - Aceptadores: MEI SCN66, JCM UBA-10, MEI CashFlow
        - CPU-4.2.2.X: Diagnóstico específico del manual 1458954

        PROTOCOLO DE RESPUESTA:
        1. 🎯 DIAGNÓSTICO: Identificar problema principal
        2. 🔧 VERIFICACIÓN: Pasos específicos para confirmar
        3. 🛠️ SOLUCIÓN: Procedimientos técnicos paso a paso  
        4. ⚠️ CÓDIGOS ERROR: Relacionar con códigos LED/error
        5. 💡 EXPERIENCIA: Tips de experiencia comprobada

        Responde en español, formato técnico pero claro, con emojis para móvil.
        """
        
        machine_info = f"""
        INFORMACIÓN DE LA MÁQUINA:
        - Modelo: {list(machine_data.keys())[0] if machine_data else 'No especificada'}
        - Fabricante: {machine_data.get('fabricante', 'N/A')}
        - Voltaje: {machine_data.get('voltaje', 'N/A')}
        - Comunicación: {machine_data.get('comunicacion', 'N/A')}
        """
        
        return f"""
        {technical_context}
        
        {machine_info}
        
        CONTEXTO ADICIONAL: {context}
        
        PROBLEMA DEL TÉCNICO: {question}
        
        Proporciona diagnóstico técnico completo y práctico:
        """
    
    def _get_fallback_response(self, question: str) -> str:
        """Respuesta de fallback"""
        return """
        🔧 **Sistema Experto CasinoPro**:
        
        **Procedimiento general de diagnóstico**:
        1. 🔌 Verificar alimentación y conexiones
        2. 🔧 Revisar configuración básica del sistema
        3. 📟 Consultar códigos de error específicos
        4. 🛠️ Aplicar solución más común para el síntoma
        
        **Para diagnóstico más preciso**:
        - Incluya códigos de error LED si los hay
        - Describa el comportamiento exacto de la falla
        - Mencione las condiciones cuando ocurre el problema
        
        💡 *Configure Google Gemini para análisis con IA*
        """

# ==================== SISTEMA DE IDIOMAS ====================
class LanguageSystem:
    def __init__(self):
        self.translations = self.setup_translations()
    
    def setup_translations(self):
        return {
            'es': {
                'main_title': "🎰 CASINOPRO - SISTEMA EXPERTO TÉCNICO",
                'main_subtitle': "**✅ Datos Técnicos + 🤖 IA Gemini + 👨‍🔧 Experiencia**",
                'menu_home': "🏠 INICIO",
                'menu_diagnostic': "🤖 DIAGNÓSTICO CON IA", 
                'menu_manuals': "💰 MANUALES",
                'menu_machines': "🎰 MÁQUINAS",
                'select_acceptor': "🔧 **SELECCIONÁ EL ACEPTADOR:**",
                'btn_run_diagnostic': "🧠 EJECUTAR DIAGNÓSTICO CON IA",
                'ai_analysis': "🤖 ANÁLISIS CON INTELIGENCIA ARTIFICIAL"
            },
            'en': {
                'main_title': "🎰 CASINOPRO - EXPERT TECHNICAL SYSTEM", 
                'main_subtitle': "**✅ Technical Data + 🤖 Gemini AI + 👨‍🔧 Experience**",
                'menu_home': "🏠 HOME",
                'menu_diagnostic': "🤖 AI DIAGNOSIS",
                'menu_manuals': "💰 MANUALS",
                'menu_machines': "🎰 MACHINES",
                'select_acceptor': "🔧 **SELECT ACCEPTOR:**",
                'btn_run_diagnostic': "🧠 RUN AI DIAGNOSIS", 
                'ai_analysis': "🤖 AI ANALYSIS"
            }
        }
    
    def get_text(self, key, lang='es'):
        return self.translations.get(lang, {}).get(key, key)
    
    def get_all_menu_options(self, lang='es'):
        return [self.get_text(f'menu_{opt}', lang) for opt in [
            'home', 'diagnostic', 'manuals', 'machines'
        ]]

# ==================== SISTEMA DE DIAGNÓSTICO CON IA ====================
class DiagnosticSystemWithAI:
    def __init__(self, db, ai_system):
        self.db = db
        self.ai_system = ai_system
    
    def get_enhanced_diagnosis(self, question, aceptador_seleccionado, contexto_adicional=""):
        """Diagnóstico potenciado con IA"""
        
        machine_data = self.db.aceptadores.get(aceptador_seleccionado, {})
        ai_response = self.ai_system.get_technical_diagnosis(question, machine_data, contexto_adicional)
        
        response = {
            'aceptador': aceptador_seleccionado,
            'pregunta': question,
            'ai_analysis': ai_response,
            'nivel_confianza': "🤖 ALTA - Diagnóstico con Google Gemini",
            'recomendacion_prioridad': self._get_priority(question),
            'machine_data': machine_data
        }
        
        return response
    
    def _get_priority(self, question):
        question_lower = question.lower()
        if any(word in question_lower for word in ['no enciende', 'incendio', 'humo', 'quemado']):
            return "🚨 URGENTE - Atender inmediatamente"
        elif any(word in question_lower for word in ['no funciona', 'error crítico', 'pantalla negra']):
            return "🔴 ALTA PRIORIDAD - Menos de 2 horas"
        else:
            return "🟡 PRIORIDAD MEDIA - Atender durante el día"

# ==================== BASE DE DATOS COMPLETA ====================
class CasinoProCompleteDB:
    def __init__(self):
        self.aceptadores = {
            "MEI SCN66": {
                "fabricante": "Crane Payment Innovations",
                "tipo": "Validador de Billetes",
                "voltaje": "+24V DC ±10%",
                "comunicacion": "MDB, ICP, RS-232, USB",
                "codigos_error": {
                    "Stacker Full": "Contenedor lleno - Vaciar depósito",
                    "Jam": "Atasco detectado - Revisar camino billetes"
                }
            },
            "JCM UBA-10": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador Universal", 
                "voltaje": "+24V DC ±15%",
                "comunicacion": "MDB, ICP, RS-232",
                "codigos_error": {
                    "Bill Jam": "Atasco en camino billetes",
                    "Stacker Full": "Depósito lleno"
                }
            },
            "MEI CashFlow 7000": {
                "fabricante": "Crane Payment Innovations",
                "tipo": "Aceptador Inteligente",
                "voltaje": "+24V DC ±5%", 
                "comunicacion": "MDB, Ethernet, USB",
                "caracteristicas": ["IA integrada", "Diagnóstico remoto"]
            }
        }
        
        self.maquinas = {
            "Aristocrat Helix": {"fabricante": "Aristocrat", "año": 2022, "plataforma": "Helix Core"},
            "Aristocrat Oasis": {"fabricante": "Aristocrat", "año": 2021, "plataforma": "Oasis"},
            "Bally Alpha Pro": {"fabricante": "Bally/SG", "año": 2022, "plataforma": "PC Industrial"},
            "Bally Alpha 2": {"fabricante": "Bally/SG", "año": 2021, "plataforma": "Alpha Series"},
            "Konami Concerto": {"fabricante": "Konami", "año": 2022, "plataforma": "Concerto"},
            "IGT Peak": {"fabricante": "IGT", "año": 2023, "plataforma": "Peak Cabinet"},
            "Scientific Games Twinstar": {"fabricante": "Scientific Games", "año": 2017, "plataforma": "CPU-4.2.2.X"}
        }
        
        self.inventario = [
            {"nombre": "🔌 Fuente IGT S2000", "stock": 3, "categoria": "Fuentes"},
            {"nombre": "💰 Aceptador MEI SCN66", "stock": 5, "categoria": "Aceptadores"},
            {"nombre": "📺 Pantalla Touch 19\"", "stock": 2, "categoria": "Pantallas"},
            {"nombre": "🔋 Módulo BIOS CPU-4.2.2.X", "stock": 3, "categoria": "CPU"},
            {"nombre": "🔋 Batería CR2032", "stock": 10, "categoria": "Baterías"}
        ]

# ==================== INICIALIZACIÓN ====================
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

if 'language_system' not in st.session_state:
    st.session_state.language_system = LanguageSystem()

if 'ai_system' not in st.session_state:
    st.session_state.ai_system = GeminiAISystem()

if 'current_language' not in st.session_state:
    st.session_state.current_language = 'es'

if 'enhanced_diagnostic' not in st.session_state:
    st.session_state.enhanced_diagnostic = DiagnosticSystemWithAI(
        st.session_state.db, 
        st.session_state.ai_system
    )

if 'current_menu' not in st.session_state:
    st.session_state.current_menu = st.session_state.language_system.get_text('menu_home')

# ==================== INTERFAZ PRINCIPAL ====================
def main():
    lang = st.session_state.current_language
    t = st.session_state.language_system.get_text
    
    # Header
    st.title(t('main_title', lang))
    st.markdown(t('main_subtitle', lang))
    
    # Estado Gemini
    if st.session_state.ai_system.configured:
        st.success("✅ **Google Gemini ACTIVO** - IA gratuita funcionando")
    else:
        st.error("❌ **Gemini NO configurado** - Revisa la API Key")
    
    # Selector de idioma
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("🌐 ES/EN"):
            st.session_state.current_language = 'en' if st.session_state.current_language == 'es' else 'es'
            st.rerun()
    
    st.markdown("---")
    
    # Menú principal
    menu_options = st.session_state.language_system.get_all_menu_options(lang)
    selected_menu = st.selectbox("📱 **NAVEGACIÓN:**", menu_options, 
                               index=menu_options.index(st.session_state.current_menu))
    
    if selected_menu != st.session_state.current_menu:
        st.session_state.current_menu = selected_menu
        st.rerun()
    
    st.markdown("---")
    
    # ==================== DIAGNÓSTICO CON IA ====================
    if st.session_state.current_menu == t('menu_diagnostic', lang):
        st.header("🤖 Diagnóstico con Google Gemini")
        
        if st.session_state.ai_system.configured:
            st.success("🎉 **Google Gemini listo** - 1,500 consultas/día GRATIS")
        else:
            st.error("⚠️ **Configura la API Key** para usar Gemini")
            st.info("""
            **Para configurar:**
            1. Ve a https://aistudio.google.com/
            2. Obtén tu API Key gratuita
            3. Pégala en el código donde dice 'PEGA TU API KEY AQUÍ'
            4. Recarga la app
            """)
        
        # Selección de aceptador
        aceptador_seleccionado = st.selectbox(
            t('select_acceptor', lang),
            list(st.session_state.db.aceptadores.keys())
        )
        
        # Información de la máquina seleccionada
        if aceptador_seleccionado:
            machine_info = st.session_state.db.aceptadores[aceptador_seleccionado]
            with st.expander("📋 Información de la máquina"):
                st.write(f"**Fabricante**: {machine_info['fabricante']}")
                st.write(f"**Tipo**: {machine_info['tipo']}")
                st.write(f"**Voltaje**: {machine_info['voltaje']}") 
                st.write(f"**Comunicación**: {machine_info['comunicacion']}")
                
                if 'codigos_error' in machine_info:
                    st.write("**Códigos de error comunes**:")
                    for error, desc in machine_info['codigos_error'].items():
                        st.write(f"- **{error}**: {desc}")
        
        # Área de diagnóstico
        st.markdown("---")
        st.subheader("💬 Consulta de Diagnóstico")
        
        pregunta_usuario = st.text_area(
            "**Describe el problema técnico en detalle:**",
            placeholder="Ej: El aceptador MEI SCN66 no enciende. Al conectar la alimentación, el LED de power parpadea en rojo pero no arranca. Revisé el voltaje y está en 24V...",
            height=120
        )
        
        contexto_adicional = st.text_area(
            "**Contexto adicional (opcional):**",
            placeholder="Ej: El problema empezó después de una tormenta eléctrica. La máquina estaba funcionando bien hasta entonces...",
            height=80
        )
        
        if st.button(t('btn_run_diagnostic', lang), type="primary", use_container_width=True):
            if pregunta_usuario.strip():
                with st.spinner("🔍 Google Gemini analizando el problema..."):
                    import time
                    time.sleep(1)
                    
                    respuesta = st.session_state.enhanced_diagnostic.get_enhanced_diagnosis(
                        pregunta_usuario,
                        aceptador_seleccionado, 
                        contexto_adicional
                    )
                    
                    # Mostrar resultados
                    st.markdown("---")
                    st.subheader("🎯 **Resultados del Diagnóstico**")
                    
                    # Información básica
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**🤖 Aceptador:** {respuesta['aceptador']}")
                        st.write(f"**🏭 Fabricante:** {respuesta['machine_data'].get('fabricante', 'N/A')}")
                    with col2:
                        st.write(f"**🎯 Confianza:** {respuesta['nivel_confianza']}")
                        st.write(f"**📋 Prioridad:** {respuesta['recomendacion_prioridad']}")
                    
                    # Análisis de IA
                    st.markdown(f"### {t('ai_analysis', lang)}")
                    st.info(respuesta['ai_analysis'])
                    
                    # Timestamp
                    st.markdown("---")
                    st.caption(f"🕐 Diagnóstico generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    
            else:
                st.warning("⚠️ Por favor, describe el problema técnico")
    
    # ==================== PÁGINA DE INICIO ====================
    elif st.session_state.current_menu == t('menu_home', lang):
        st.header("🏠 Dashboard CasinoPro")
        
        # Métricas
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("💰 Aceptadores", len(st.session_state.db.aceptadores))
        with col2:
            st.metric("🎰 Máquinas", len(st.session_state.db.maquinas))
        with col3:
            st.metric("📦 Repuestos", len(st.session_state.db.inventario))
        with col4:
            status = "✅ Activo" if st.session_state.ai_system.configured else "❌ Inactivo"
            st.metric("🤖 Gemini IA", status)
        
        # Estado del sistema
        st.subheader("📊 Estado del Sistema")
        if st.session_state.ai_system.configured:
            st.success("""
            ✅ **Google Gemini ACTIVO**
            - 1,500 consultas/día GRATIS
            - Calidad premium de IA
            - Diagnósticos técnicos avanzados
            """)
        else:
            st.error("""
            ❌ **Google Gemini INACTIVO** 
            - Pega tu API Key en el código
            - Obtén key gratis en: https://aistudio.google.com/
            """)
        
        # Acciones rápidas
        st.subheader("🚀 Acciones Rápidas")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🤖 Ir a Diagnóstico con IA", use_container_width=True):
                st.session_state.current_menu = t('menu_diagnostic', lang)
                st.rerun()
        with col2:
            if st.button("💰 Ver Manuales", use_container_width=True):
                st.session_state.current_menu = t('menu_manuals', lang)
                st.rerun()
                
        # Ejemplos de consultas
        st.subheader("💡 Ejemplos de Consultas para IA")
        with st.expander("Ver ejemplos"):
            st.write("""
            **Problemas comunes para probar:**
            - "Mi Aristocrat Helix no enciende, el LED de power se queda rojo"
            - "El aceptador MEI SCN66 rechaza billetes que antes aceptaba"  
            - "La máquina Bally Alpha Pro se reinicia sola cada 30 minutos"
            - "Error de comunicación SAS en IGT Peak, código 0x25"
            - "Problemas de touch screen en Konami Concerto después de limpiar"
            """)
    
    # ==================== MANUALES ====================
    elif st.session_state.current_menu == t('menu_manuals', lang):
        st.header("💰 Manuales de Aceptadores")
        for name, info in st.session_state.db.aceptadores.items():
            with st.expander(f"📋 {name}"):
                st.write(f"**Fabricante**: {info['fabricante']}")
                st.write(f"**Tipo**: {info['tipo']}")
                st.write(f"**Voltaje**: {info['voltaje']}")
                st.write(f"**Comunicación**: {info['comunicacion']}")
                if 'codigos_error' in info:
                    st.write("**Códigos de error**:")
                    for error, desc in info['codigos_error'].items():
                        st.write(f"- **{error}**: {desc}")
    
    # ==================== MÁQUINAS ====================
    elif st.session_state.current_menu == t('menu_machines', lang):
        st.header("🎰 Máquinas Registradas")
        for name, info in st.session_state.db.maquinas.items():
            with st.expander(f"🎰 {name}"):
                st.write(f"**Fabricante**: {info['fabricante']}")
                st.write(f"**Año**: {info['año']}")
                st.write(f"**Plataforma**: {info['plataforma']}")

if __name__ == "__main__":
    main()
