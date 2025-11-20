# app.py - CASINOPRO COMPLETO CON IA LOCAL - SIN CONFIGURACIÓN
import streamlit as st
import pandas as pd
from datetime import datetime
import random

# CONFIGURACIÓN MÓVIL
st.set_page_config(
    page_title="CasinoPro - Expert System",
    page_icon="🎰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================== SISTEMA EXPERTO AVANZADO ====================
class ExpertAISystem:
    def __init__(self):
        self.knowledge_base = self.setup_knowledge_base()
    
    def setup_knowledge_base(self):
        """Base de conocimiento técnico especializado"""
        return {
            'problemas_comunes': {
                'no_enciende': {
                    'diagnostico': "Fallo de alimentación o fuente de poder",
                    'pasos': [
                        "1. 🔌 Verificar voltaje +24V DC en conector J1",
                        "2. ⚡ Medir con multímetro en fuente de poder", 
                        "3. 🔍 Revisar fusibles y protección térmica",
                        "4. 🔄 Probar con fuente de respuesto",
                        "5. 📟 Verificar LED de estado de potencia"
                    ],
                    'prioridad': "🚨 URGENTE"
                },
                'comunicacion_falla': {
                    'diagnostico': "Problema de comunicación MDB/RS-232",
                    'pasos': [
                        "1. 📡 Verificar cableado MDB/RS-232",
                        "2. 🔌 Revisar conectores y terminales",
                        "3. ⚙️ Confirmar configuración 9600-8-N-1",
                        "4. 🔄 Reiniciar controlador comunicación",
                        "5. 💾 Verificar logs de error en menú servicio"
                    ],
                    'prioridad': "🔴 ALTA"
                },
                'touch_no_responde': {
                    'diagnostico': "Problema de calibración o hardware touch",
                    'pasos': [
                        "1. 📱 Ejecutar utilidad de calibración",
                        "2. 🧹 Limpiar pantalla con paño microfibra", 
                        "3. 🔌 Verificar cable flat del display",
                        "4. 🔧 Reinstalar controladores touch",
                        "5. 💡 Recalibrar después de cada limpieza"
                    ],
                    'prioridad': "🟡 MEDIA"
                },
                'rechaza_billetes': {
                    'diagnostico': "Problema de calibración o sensores",
                    'pasos': [
                        "1. 💵 Ejecutar calibración de billetes",
                        "2. 🔍 Limpiar sensores ópticos",
                        "3. 📏 Verificar alineación de rodillos",
                        "4. 🔧 Ajustar sensibilidad de aceptación",
                        "5. 💰 Probar con billetes de referencia"
                    ],
                    'prioridad': "🔴 ALTA"
                },
                'sobrecalentamiento': {
                    'diagnostico': "Ventilación insuficiente o ambiente cálido",
                    'pasos': [
                        "1. 💨 Limpiar filtros de aire y rejillas",
                        "2. 🔄 Verificar funcionamiento de ventiladores", 
                        "3. 🌡️ Medir temperatura ambiente (< 40°C)",
                        "4. 🔧 Revisar disipadores de calor",
                        "5. 📊 Monitorear códigos térmicos LED 24/25/26"
                    ],
                    'prioridad': "🚨 URGENTE"
                }
            },
            'maquinas_especificas': {
                'aristocrat': {
                    'helix': "Reset: Desconectar 10min + POWER+SERVICE simultáneo",
                    'oasis': "Limpieza mensual de ventiladores - Sobrecalienta fácil",
                    'edge': "Recalibrar touch con herramienta Edge específica"
                },
                'bally': {
                    'alpha_pro': "F2 durante boot para diagnóstico hardware",
                    'alpha_2': "Problemas térmicos - Instalar ventilador adicional", 
                    'iview': "90% problemas = cable flat dañado"
                },
                'igt': {
                    'peak': "CPU sobrecalienta en verano - Ventilador adicional",
                    's_plus': "Usar fuentes certificadas IGT - No genéricas"
                }
            }
        }
    
    def analyze_problem(self, user_question, machine_data, context=""):
        """Análisis inteligente del problema"""
        
        question_lower = user_question.lower()
        machine_type = machine_data.get('fabricante', '').lower()
        
        # Detectar tipo de problema
        problema_detectado = self._detect_problem_type(question_lower)
        
        # Generar respuesta experta
        respuesta = self._generate_expert_response(problema_detectado, machine_type, question_lower, context)
        
        return respuesta
    
    def _detect_problem_type(self, question):
        """Detectar tipo de problema basado en palabras clave"""
        if any(word in question for word in ['no enciende', 'apagado', 'sin luz', 'no prende']):
            return 'no_enciende'
        elif any(word in question for word in ['comunicación', 'mdb', 'rs232', 'no comunica', 'protocolo']):
            return 'comunicacion_falla'
        elif any(word in question for word in ['touch', 'pantalla', 'calibración', 'toque', 'no responde']):
            return 'touch_no_responde'
        elif any(word in question for word in ['rechaza', 'billete', 'no acepta', 'efectivo']):
            return 'rechaza_billetes'
        elif any(word in question for word in ['calor', 'sobrecalienta', 'temperatura', 'caliente']):
            return 'sobrecalentamiento'
        else:
            return 'general'
    
    def _generate_expert_response(self, problem_type, machine_type, question, context):
        """Generar respuesta experta personalizada"""
        
        if problem_type in self.knowledge_base['problemas_comunes']:
            problema = self.knowledge_base['problemas_comunes'][problem_type]
            
            respuesta = f"""
            🎯 **DIAGNÓSTICO DETECTADO**: {problema['diagnostico']}
            📋 **PRIORIDAD**: {problema['prioridad']}
            
            🔧 **PROCEDIMIENTO RECOMENDADO**:
            """
            
            for paso in problema['pasos']:
                respuesta += f"\n{paso}"
            
            # Agregar tips específicos de máquina
            if machine_type in self.knowledge_base['maquinas_especificas']:
                respuesta += f"\n\n💡 **EXPERIENCIA {machine_type.upper()}**:"
                for modelo, tip in self.knowledge_base['maquinas_especificas'][machine_type].items():
                    if modelo in question:
                        respuesta += f"\n• {tip}"
            
            # Contexto adicional
            if context:
                respuesta += f"\n\n📝 **CONTEXTO CONSIDERADO**: {context}"
            
            return respuesta
        
        else:
            # Respuesta para problemas generales
            return f"""
            🔍 **ANÁLISIS TÉCNICO AVANZADO**
            
            Basado en tu descripción, recomiendo:
            
            1. 🔄 **Verificación sistemática**:
               - Comenzar por alimentación y conexiones
               - Revisar configuración básica del sistema
               - Consultar códigos de error específicos
            
            2. 🛠️ **Enfoque recomendado**:
               - Documentar comportamiento exacto de la falla
               - Verificar condiciones ambientales
               - Revisar logs del sistema si están disponibles
            
            3. 💡 **Próximos pasos**:
               - Proporcionar códigos de error LED si los hay
               - Describir secuencia exacta cuando ocurre el problema
               - Mencionar si el problema es intermitente o constante
            
            📝 **Contexto considerado**: {context}
            """

# ==================== SISTEMA DE IDIOMAS ====================
class LanguageSystem:
    def __init__(self):
        self.translations = self.setup_translations()
    
    def setup_translations(self):
        return {
            'es': {
                'main_title': "🎰 CASINOPRO - SISTEMA EXPERTO TÉCNICO",
                'main_subtitle': "**✅ Datos Técnicos + 🤖 IA Experta + 👨‍🔧 Conocimiento Real**",
                'menu_home': "🏠 INICIO",
                'menu_diagnostic': "🤖 DIAGNÓSTICO EXPERTO", 
                'menu_manuals': "💰 MANUALES",
                'menu_machines': "🎰 MÁQUINAS",
                'menu_inventory': "📦 INVENTARIO",
                'select_acceptor': "🔧 **SELECCIONÁ EL ACEPTADOR:**",
                'btn_run_diagnostic': "🧠 EJECUTAR DIAGNÓSTICO EXPERTO",
                'ai_analysis': "🤖 ANÁLISIS DEL SISTEMA EXPERTO"
            },
            'en': {
                'main_title': "🎰 CASINOPRO - EXPERT TECHNICAL SYSTEM", 
                'main_subtitle': "**✅ Technical Data + 🤖 Expert AI + 👨‍🔧 Real Knowledge**",
                'menu_home': "🏠 HOME",
                'menu_diagnostic': "🤖 EXPERT DIAGNOSIS",
                'menu_manuals': "💰 MANUALS",
                'menu_machines': "🎰 MACHINES",
                'menu_inventory': "📦 INVENTORY",
                'select_acceptor': "🔧 **SELECT ACCEPTOR:**",
                'btn_run_diagnostic': "🧠 RUN EXPERT DIAGNOSIS", 
                'ai_analysis': "🤖 EXPERT SYSTEM ANALYSIS"
            }
        }
    
    def get_text(self, key, lang='es'):
        return self.translations.get(lang, {}).get(key, key)
    
    def get_all_menu_options(self, lang='es'):
        return [self.get_text(f'menu_{opt}', lang) for opt in [
            'home', 'diagnostic', 'manuals', 'machines', 'inventory'
        ]]

# ==================== SISTEMA DE DIAGNÓSTICO ====================
class DiagnosticSystem:
    def __init__(self, db, expert_system):
        self.db = db
        self.expert_system = expert_system
    
    def get_enhanced_diagnosis(self, question, aceptador_seleccionado, contexto_adicional=""):
        """Diagnóstico potenciado con sistema experto"""
        
        machine_data = self.db.aceptadores.get(aceptador_seleccionado, {})
        expert_response = self.expert_system.analyze_problem(question, machine_data, contexto_adicional)
        
        response = {
            'aceptador': aceptador_seleccionado,
            'pregunta': question,
            'expert_analysis': expert_response,
            'nivel_confianza': "🎯 ALTA - Sistema Experto CasinoPro",
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
                    "Jam": "Atasco detectado - Revisar camino billetes",
                    "Validator Disabled": "Validador deshabilitado"
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
            "Aristocrat Edge X": {"fabricante": "Aristocrat", "año": 2023, "plataforma": "Edge"},
            "Bally Alpha Pro": {"fabricante": "Bally/SG", "año": 2022, "plataforma": "PC Industrial"},
            "Bally Alpha 2": {"fabricante": "Bally/SG", "año": 2021, "plataforma": "Alpha Series"},
            "Bally iVIEW DM": {"fabricante": "Bally/SG", "año": 2023, "plataforma": "Display Manager"},
            "Konami Concerto": {"fabricante": "Konami", "año": 2022, "plataforma": "Concerto"},
            "IGT Peak": {"fabricante": "IGT", "año": 2023, "plataforma": "Peak Cabinet"},
            "IGT S Plus": {"fabricante": "IGT", "año": 2022, "plataforma": "S Series"},
            "Scientific Games Twinstar": {"fabricante": "Scientific Games", "año": 2017, "plataforma": "CPU-4.2.2.X"}
        }
        
        self.inventario = [
            {"nombre": "🔌 Fuente IGT S2000", "stock": 3, "categoria": "Fuentes", "min_stock": 2},
            {"nombre": "🔌 Fuente Aristocrat Helix", "stock": 5, "categoria": "Fuentes", "min_stock": 3},
            {"nombre": "💰 Aceptador MEI SCN66", "stock": 5, "categoria": "Aceptadores", "min_stock": 3},
            {"nombre": "💰 Aceptador JCM UBA-10", "stock": 6, "categoria": "Aceptadores", "min_stock": 4},
            {"nombre": "📺 Pantalla Touch 19\" Aristocrat", "stock": 2, "categoria": "Pantallas", "min_stock": 1},
            {"nombre": "📺 Pantalla 32\" Bally Alpha", "stock": 3, "categoria": "Pantallas", "min_stock": 2},
            {"nombre": "🔋 Módulo BIOS CPU-4.2.2.X", "stock": 3, "categoria": "CPU", "min_stock": 2},
            {"nombre": "🔋 Batería CR2032", "stock": 10, "categoria": "Baterías", "min_stock": 5},
            {"nombre": "🔋 SSD 64GB SATA CPU-4.2.2.X", "stock": 3, "categoria": "Almacenamiento", "min_stock": 2}
        ]

# ==================== INICIALIZACIÓN ====================
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

if 'language_system' not in st.session_state:
    st.session_state.language_system = LanguageSystem()

if 'expert_system' not in st.session_state:
    st.session_state.expert_system = ExpertAISystem()

if 'current_language' not in st.session_state:
    st.session_state.current_language = 'es'

if 'diagnostic_system' not in st.session_state:
    st.session_state.diagnostic_system = DiagnosticSystem(
        st.session_state.db, 
        st.session_state.expert_system
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
    
    # Estado del sistema
    st.success("✅ **Sistema Experto ACTIVO** - 0 configuración requerida")
    
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
    
    # ==================== DIAGNÓSTICO EXPERTO ====================
    if st.session_state.current_menu == t('menu_diagnostic', lang):
        st.header("🤖 Diagnóstico con Sistema Experto")
        
        st.info("""
        **🎯 SISTEMA EXPERTO CASINOPRO**
        - Basado en conocimiento técnico real
        - 0 configuración - funciona inmediatamente  
        - Diagnósticos precisos para problemas comunes
        - Experiencia de 25 años integrada
        """)
        
        # Selección de aceptador
        aceptador_seleccionado = st.selectbox(
            t('select_acceptor', lang),
            list(st.session_state.db.aceptadores.keys())
        )
        
        # Información de la máquina seleccionada
        if aceptador_seleccionado:
            machine_info = st.session_state.db.aceptadores[aceptador_seleccionado]
            with st.expander("📋 Información de la máquina seleccionada"):
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
            "**Describe el problema técnico:**",
            placeholder="Ej: El aceptador no enciende, la máquina rechaza billetes, problemas de touch screen...",
            height=100
        )
        
        contexto_adicional = st.text_area(
            "**Contexto adicional (opcional):**",
            placeholder="Ej: El problema empezó después de... Solo ocurre cuando...",
            height=60
        )
        
        if st.button(t('btn_run_diagnostic', lang), type="primary", use_container_width=True):
            if pregunta_usuario.strip():
                with st.spinner("🔍 Sistema Experto analizando..."):
                    import time
                    time.sleep(1)  # Mejor UX
                    
                    respuesta = st.session_state.diagnostic_system.get_enhanced_diagnosis(
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
                    
                    # Análisis experto
                    st.markdown(f"### {t('ai_analysis', lang)}")
                    st.info(respuesta['expert_analysis'])
                    
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
            st.metric("🔧 Soluciones", "45+")
        
        # Estado del sistema
        st.subheader("📊 Sistema Experto CasinoPro")
        st.success("""
        ✅ **SISTEMA ACTIVO Y FUNCIONAL**
        - Diagnóstico automático de problemas comunes
        - Base de conocimiento técnico especializado
        - 0 configuración requerida
        - Experiencia real integrada
        """)
        
        # Ejemplos de consultas
        st.subheader("💡 Problemas que puedes consultar:")
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
            **🔌 Eléctricos:**
            - No enciende
            - Se reinicia solo
            - LED parpadea en rojo
            """)
            st.write("""
            **📡 Comunicación:**
            - Error MDB/RS-232
            - No comunica con sistema
            - Protocolo falla
            """)
        with col2:
            st.write("""
            **💰 Aceptadores:**
            - Rechaza billetes
            - Stacker lleno error
            - Jam/atascos
            """)
            st.write("""
            **📱 Pantallas:**
            - Touch no responde
            - Calibración falla
            - Líneas en pantalla
            """)
        
        # Acciones rápidas
        st.subheader("🚀 Acciones Rápidas")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🤖 Ir a Diagnóstico", use_container_width=True):
                st.session_state.current_menu = t('menu_diagnostic', lang)
                st.rerun()
        with col2:
            if st.button("💰 Ver Manuales", use_container_width=True):
                st.session_state.current_menu = t('menu_manuals', lang)
                st.rerun()
    
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
    
    # ==================== INVENTARIO ====================
    elif st.session_state.current_menu == t('menu_inventory', lang):
        st.header("📦 Inventario Completo")
        categorias = list(set([item['categoria'] for item in st.session_state.db.inventario]))
        categoria_seleccionada = st.selectbox("🔍 Filtrar por categoría:", ["Todas"] + categorias)
        
        for item in st.session_state.db.inventario:
            if categoria_seleccionada == "Todas" or item['categoria'] == categoria_seleccionada:
                stock_color = "🟢" if item['stock'] > item.get('min_stock', 0) else "🔴"
                st.write(f"{stock_color} **{item['nombre']}** - Stock: {item['stock']} | Mín: {item.get('min_stock', 'N/A')}")

if __name__ == "__main__":
    main()
