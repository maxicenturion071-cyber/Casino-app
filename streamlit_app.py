# app.py - CASINOPRO CON DEEPSEEK AI - Sistema de Chat Inteligente
import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import hashlib
import requests

# CONFIGURACIÓN MÓVIL
st.set_page_config(
    page_title="CasinoPro AI System",
    page_icon="🎰", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==================== CONFIGURACIÓN DEEPSEEK EN SIDEBAR ====================
def get_deepseek_api_key():
    """Obtener API Key de forma segura desde sidebar - VERSIÓN MEJORADA"""
    
    # ✅ PRIMERO: Verificar si el usuario acaba de guardar la key
    if 'api_key_input' in st.session_state and st.session_state.api_key_input:
        if st.session_state.api_key_input.startswith('sk-'):
            st.session_state.deepseek_api_key = st.session_state.api_key_input
            return st.session_state.api_key_input
    
    # ✅ SEGUNDO: Verificar session state
    if 'deepseek_api_key' in st.session_state and st.session_state.deepseek_api_key:
        if st.session_state.deepseek_api_key.startswith('sk-'):
            return st.session_state.deepseek_api_key
    
    # ✅ TERCERO: Secrets de Streamlit
    if 'DEEPSEEK_API_KEY' in st.secrets:
        return st.secrets['DEEPSEEK_API_KEY']
    
    # ✅ CUARTO: Variable de entorno
    import os
    if 'DEEPSEEK_API_KEY' in os.environ:
        return os.environ.get('DEEPSEEK_API_KEY')
    
    return None

def mostrar_configuracion_api():
    """Mostrar panel de configuración de API en sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔐 Configuración DeepSeek API")
    
    with st.sidebar.expander("⚙️ Configurar API Key", expanded=True):
        st.write("**Para activar la IA avanzada, necesitás tu API Key:**")
        
        api_key = st.text_input(
            "DeepSeek API Key:",
            type="password",
            placeholder="sk-tu_clave_aqui",
            help="Obtené tu clave gratis en: https://platform.deepseek.com/api_keys",
            key="api_key_input"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Guardar Key", use_container_width=True):
                if api_key and api_key.startswith('sk-'):
                    st.session_state.deepseek_api_key = api_key
                    st.success("✅ Clave guardada en sesión")
                    st.rerun()
                else:
                    st.error("❌ Clave inválida - debe empezar con 'sk-'")
        
        with col2:
            if st.button("🗑️ Limpiar", use_container_width=True):
                if 'deepseek_api_key' in st.session_state:
                    del st.session_state.deepseek_api_key
                st.success("🔓 Clave removida")
                st.rerun()
        
        # Mostrar estado actual
        api_key_actual = get_deepseek_api_key()
        if api_key_actual:
            st.success(f"🔑 **API Key Configurada**: {api_key_actual[:10]}...{api_key_actual[-4:]}")
        else:
            st.warning("⚠️ **API Key No Configurada**")
        
        st.info("""
        **ℹ️ ¿Cómo obtenerla?**
        1. Andá a [DeepSeek Platform](https://platform.deepseek.com/api_keys)
        2. Creá cuenta gratis
        3. Generá API Key
        4. Pegala aquí
        
        **🎯 Beneficios:**
        • Respuestas más inteligentes
        • Diagnósticos avanzados
        • Análisis contextual mejorado
        """)

def mostrar_debug_info():
    """Mostrar información de debug en sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔍 Debug Info")
    
    # Verificar API Key
    api_key = get_deepseek_api_key()
    st.sidebar.write(f"**API Key detectada:** {bool(api_key)}")
    if api_key:
        st.sidebar.write(f"**Key:** {api_key[:10]}...{api_key[-4:]}")
    
    # Verificar session state
    st.sidebar.write(f"**Session State Key:** {'deepseek_api_key' in st.session_state}")
    
    # Verificar si DeepSeek está activo
    if 'diagnostic_system' in st.session_state:
        st.sidebar.write(f"**Sistema AI cargado:** ✅")
    else:
        st.sidebar.write(f"**Sistema AI cargado:** ❌")

# ==================== DEEPSEEK API REAL ====================
class DeepSeekAPI:
    def __init__(self):
        self.base_url = "https://api.deepseek.com/v1"
        self.model = "deepseek-chat"
    
    def consultar_deepseek(self, pregunta, contexto_tecnico=""):
        """Consultar la API real de DeepSeek - VERSIÓN CON DEBUG"""
        
        # ✅ DEBUG: Mostrar información de la API Key
        api_key = get_deepseek_api_key()
        st.sidebar.info(f"🔍 DEBUG: API Key presente: {bool(api_key)}")
        
        if api_key:
            st.sidebar.info(f"🔍 DEBUG: Key inicia con: {api_key[:10]}...")
        
        if not api_key:
            debug_msg = "❌ NO HAY API KEY - Usando sistema local"
            st.sidebar.error(debug_msg)
            return """
            🔐 **Configuración Requerida**
            
            Para usar las funciones avanzadas de IA, necesitás configurar tu API Key de DeepSeek.
            
            **📋 Pasos para configurar:**
            1. **Andá a:** https://platform.deepseek.com/api_keys
            2. **Creá una cuenta** (es gratis)
            3. **Generá una nueva API Key**
            4. **Pegala en el panel de configuración** en el sidebar ←
            
            **🔧 Mientras tanto, podés usar:**
            • Sistema local de diagnóstico especializado
            • Base de conocimiento técnico completo
            • Procedimientos específicos de Vertex Controller
            
            ¡Una vez configurada, experimentá el poder real de la IA! 🚀
            """
        
        # PROMPT MEJORADO
        system_prompt = f"""
        Eres CasinoPro, un sistema experto en diagnóstico técnico de máquinas de casino con 25+ años de experiencia integrada.

        ESPECIALIDADES TÉCNICAS:
        - Vertex Controller 3.5 y 4.0 (configuración, Ram Clear, IP 192.168.50.2)
        - Aceptadores MEI SCN66, JCM UBA-10, CashFlow 7000, Aristocrat NV9
        - Máquinas Aristocrat (Helix, Oasis, Edge, MK6), Bally (Alpha Pro, iView), IGT (Peak, S3000), Konami (Concerto, KX)
        - Diagnóstico de: no enciende, problemas comunicación MDB/RS-232, touch no responde, rechazo de billetes, sobrecalentamiento
        - Procedimientos técnicos específicos y prioridades de reparación
        - Configuración de redes progresivas y Lightning Link

        CONOCIMIENTO ESPECÍFICO VERTEX:
        - Vertex 3.5: IP 192.168.50.2, Credenciales admin/Password1, 1 puerto USB
        - Vertex 4.0: IP 192.168.50.2, Credenciales Retail1/Retail1, fuente externa
        - Ram Clear: DataBase → BackUp/Restore → Ram Clear
        - Configuración jurisdicción: Argentina - Buenos Aires

        CONTEXTO ESPECÍFICO:
        {contexto_tecnico}

        **IMPORTANTE - ESTILO DE RESPUESTA:**
        - Para saludos y conversación casual: responde de forma NATURAL y AMIGABLE, como un asistente conversacional
        - NO comiences con "Soy CasinoPro..." en saludos - sé directo y natural
        - Para problemas técnicos: usa formato técnico claro con pasos numerados
        - Incluye emojis relevantes para cada paso
        - Especifica niveles de prioridad (🚨 URGENTE, 🔴 ALTA, 🟡 MEDIA)
        - Basa las soluciones en experiencia real de campo
        - Sé preciso y específico con procedimientos
        - Mantén un estilo técnico pero amigable

        **EJEMPLOS DE RESPUESTAS NATURALES:**
        - Si te saludan: "¡Hola! 👋 ¿Cómo estás? Estoy aquí para ayudarte con tus máquinas de casino. ¿En qué puedo asistirte?"
        - Si preguntan cómo estás: "¡Excelente! Listo para diagnosticar problemas técnicos. ¿Qué máquina necesita atención?"
        - Para problemas técnicos: usar formato estructurado con emojis y pasos claros
        """
        
        try:
            endpoint = f"{self.base_url}/chat/completions"
            
            st.sidebar.info("🔍 DEBUG: Enviando request a DeepSeek...")
            
            response = requests.post(
                endpoint,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system", 
                            "content": system_prompt
                        },
                        {
                            "role": "user", 
                            "content": pregunta
                        }
                    ],
                    "temperature": 0.8,
                    "max_tokens": 2000,
                    "stream": False
                },
                timeout=45
            )
            
            st.sidebar.info(f"🔍 DEBUG: Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                respuesta = data["choices"][0]["message"]["content"]
                st.sidebar.success("✅ DEBUG: DeepSeek respondió correctamente")
                return respuesta
            else:
                error_msg = f"❌ Error API DeepSeek: {response.status_code}"
                if response.status_code == 401:
                    error_msg += " - API Key inválida o expirada"
                elif response.status_code == 429:
                    error_msg += " - Límite de requests excedido"
                elif response.status_code == 400:
                    error_msg += " - Request mal formado"
                else:
                    try:
                        error_detail = response.json().get('error', {}).get('message', '')
                        error_msg += f" - {error_detail}"
                    except:
                        error_msg += f" - {response.text}"
                
                st.sidebar.error(f"🔍 DEBUG: {error_msg}")
                return error_msg
                
        except requests.exceptions.Timeout:
            error = "⏰ Timeout - DeepSeek no respondió a tiempo (45s)"
            st.sidebar.error(f"🔍 DEBUG: {error}")
            return error
        except requests.exceptions.ConnectionError:
            error = "🔌 Error de conexión - Verificá tu internet"
            st.sidebar.error(f"🔍 DEBUG: {error}")
            return error
        except Exception as e:
            error = f"⚠️ Error inesperado: {str(e)}"
            st.sidebar.error(f"🔍 DEBUG: {error}")
            return error

# ==================== IA "CASINOPRO" - SISTEMA INTELIGENTE ESPECIALIZADO ====================
class CasinoProAISystem:
    def __init__(self):
        self.nombre = "CasinoPro"
        self.version = "2.3"
        self.ia_modelo = "DeepSeek AI"
        self.codigo_ia = "DEEPSEEK-CP-VTX-8876"
        self.deepseek_api = DeepSeekAPI()
        self.personalidad = self.setup_personalidad()
        self.knowledge_base = self.setup_knowledge_base()
        self.conversation_memory = []
        self.learned_patterns = {}
        self.user_feedback = {}
        self.setup_data_storage()
        self.load_learned_data()
    
    def setup_personalidad(self):
        """Personalidad y estilo de la IA CasinoPro"""
        return {
            'nombre': 'CasinoPro',
            'ia_modelo': 'DeepSeek AI',
            'titulo': '🎰 CasinoPro - DeepSeek AI Especializado',
            'eslogan': 'Tu asistente técnico inteligente con DeepSeek AI',
            'estilo_respuesta': 'técnico_amigable',
            'emoji_firma': '🤖🧠',
            'saludo': '¡Hola! Soy CasinoPro con tecnología DeepSeek AI, tu especialista en diagnóstico técnico. ¿En qué puedo ayudarte hoy?',
            'caracteristicas': [
                "Tecnología DeepSeek AI integrada",
                "25+ años de experiencia integrada",
                "Aprendizaje automático continuo", 
                "Especialista en Aristocrat, Bally, IGT, Konami",
                "Conocimiento del manual CPU-4.2.2.X",
                "Diagnóstico basado en patrones reales",
                "Especialista en Vertex Controller 3.5/4.0"
            ]
        }
    
    def setup_data_storage(self):
        """Configurar almacenamiento para aprendizaje"""
        if not os.path.exists('casinopro_data'):
            os.makedirs('casinopro_data')
    
    def load_learned_data(self):
        """Cargar datos aprendidos desde archivos"""
        try:
            if os.path.exists('casinopro_data/learned_patterns.json'):
                with open('casinopro_data/learned_patterns.json', 'r', encoding='utf-8') as f:
                    self.learned_patterns = json.load(f)
            
            if os.path.exists('casinopro_data/user_feedback.json'):
                with open('casinopro_data/user_feedback.json', 'r', encoding='utf-8') as f:
                    self.user_feedback = json.load(f)
                    
            if os.path.exists('casinopro_data/conversation_memory.json'):
                with open('casinopro_data/conversation_memory.json', 'r', encoding='utf-8') as f:
                    self.conversation_memory = json.load(f)
                    
        except Exception as e:
            st.sidebar.warning(f"⚠️ No se pudieron cargar datos de aprendizaje: {e}")
    
    def save_learned_data(self):
        """Guardar datos aprendidos en archivos"""
        try:
            with open('casinopro_data/learned_patterns.json', 'w', encoding='utf-8') as f:
                json.dump(self.learned_patterns, f, ensure_ascii=False, indent=2)
            
            with open('casinopro_data/user_feedback.json', 'w', encoding='utf-8') as f:
                json.dump(self.user_feedback, f, ensure_ascii=False, indent=2)
                
            with open('casinopro_data/conversation_memory.json', 'w', encoding='utf-8') as f:
                json.dump(self.conversation_memory[-100:], f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            st.sidebar.error(f"❌ Error guardando datos: {e}")
    
    def setup_knowledge_base(self):
        """Base de conocimiento inicial de CasinoPro - MEJORADA CON VERTEX"""
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
                    'prioridad': "🚨 URGENTE",
                    'confidence': 0.95,
                    'usage_count': 0,
                    'success_rate': 0.85
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
                    'prioridad': "🔴 ALTA",
                    'confidence': 0.90,
                    'usage_count': 0,
                    'success_rate': 0.80
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
                    'prioridad': "🟡 MEDIA",
                    'confidence': 0.88,
                    'usage_count': 0,
                    'success_rate': 0.75
                },
                'rechaza_billetes': {
                    'diagnostico': "Problema de calibración o sensores del aceptador",
                    'pasos': [
                        "1. 💵 Ejecutar calibración de billetes",
                        "2. 🔍 Limpiar sensores ópticos con aire comprimido",
                        "3. 📏 Verificar alineación de rodillos",
                        "4. 🔧 Ajustar sensibilidad de aceptación",
                        "5. 💰 Probar con billetes de referencia en buen estado"
                    ],
                    'prioridad': "🔴 ALTA",
                    'confidence': 0.87,
                    'usage_count': 0,
                    'success_rate': 0.78
                },
                'sobrecalentamiento': {
                    'diagnostico': "Ventilación insuficiente o ambiente cálido",
                    'pasos': [
                        "1. 💨 Limpiar filtros de aire y rejillas de ventilación",
                        "2. 🔄 Verificar funcionamiento de todos los ventiladores", 
                        "3. 🌡️ Medir temperatura ambiente (no debe superar 40°C)",
                        "4. 🔧 Revisar disipadores de calor y pasta térmica",
                        "5. 📊 Monitorear códigos térmicos LED 24/25/26 en CPU"
                    ],
                    'prioridad': "🚨 URGENTE",
                    'confidence': 0.92,
                    'usage_count': 0,
                    'success_rate': 0.82
                },
                'error_sistema': {
                    'diagnostico': "Error de software o configuración del sistema",
                    'pasos': [
                        "1. 💻 Revisar códigos de error en display",
                        "2. 🔄 Realizar reset de fábrica controlado",
                        "3. 📀 Verificar integridad del software",
                        "4. ⚙️ Restaurar configuración de respaldo",
                        "5. 🔧 Actualizar firmware a última versión"
                    ],
                    'prioridad': "🔴 ALTA",
                    'confidence': 0.85,
                    'usage_count': 0,
                    'success_rate': 0.70
                },
                'problema_audio': {
                    'diagnostico': "Falla en sistema de audio o altavoces",
                    'pasos': [
                        "1. 🔊 Verificar configuración de volumen en software",
                        "2. 🔌 Revisar conexiones de cables de audio",
                        "3. 🎵 Probar con diferentes archivos de sonido",
                        "4. 🔧 Verificar estado de altavoces individualmente",
                        "5. 💻 Reinstalar controladores de audio"
                    ],
                    'prioridad': "🟡 MEDIA",
                    'confidence': 0.83,
                    'usage_count': 0,
                    'success_rate': 0.75
                },
                'problema_red': {
                    'diagnostico': "Falla en conectividad de red",
                    'pasos': [
                        "1. 🌐 Verificar conexión Ethernet/Wi-Fi",
                        "2. 🔌 Revisar cableado de red y LEDs",
                        "3. ⚙️ Comprobar configuración IP y DNS",
                        "4. 🔄 Reiniciar router y switch",
                        "5. 💻 Verificar firewall y configuraciones de red"
                    ],
                    'prioridad': "🔴 ALTA",
                    'confidence': 0.88,
                    'usage_count': 0,
                    'success_rate': 0.80
                },
                'problema_pagos': {
                    'diagnostico': "Falla en sistema de pagos o hopper",
                    'pasos': [
                        "1. 💰 Verificar nivel de monedas en hopper",
                        "2. 🔧 Revisar sensores de pago y dispensación",
                        "3. ⚙️ Calibrar mecanismo de pago",
                        "4. 🔄 Ejecutar test de dispensación",
                        "5. 📊 Verificar logs de transacciones"
                    ],
                    'prioridad': "🔴 ALTA",
                    'confidence': 0.85,
                    'usage_count': 0,
                    'success_rate': 0.75
                },
                'problema_botones': {
                    'diagnostico': "Falla en panel de botones o controles",
                    'pasos': [
                        "1. 🔘 Verificar conexiones de panel de control",
                        "2. 🔧 Revisar estado físico de botones",
                        "3. ⚡ Medir continuidad en switches",
                        "4. 💻 Probar en modo diagnóstico",
                        "5. 🔄 Reemplazar botones defectuosos"
                    ],
                    'prioridad': "🟡 MEDIA",
                    'confidence': 0.80,
                    'usage_count': 0,
                    'success_rate': 0.70
                },
                'vertex_no_enciende': {
                    'diagnostico': "Problema de alimentación Vertex Controller",
                    'pasos': [
                        "1. 🔌 Verificar fuente de poder externa (Vertex 4.0)",
                        "2. ⚡ Medir voltaje de entrada +24V DC",
                        "3. 🔍 Revisar botón frontal - PULSAR Y SOLTAR, no mantener",
                        "4. 📟 Verificar LED de estado del controlador",
                        "5. 🔄 Probar con fuente de respuesto certificada",
                        "6. ⚠️ NUNCA desconectar de net eléctrica directamente"
                    ],
                    'prioridad': "🚨 URGENTE",
                    'confidence': 0.92,
                    'usage_count': 0,
                    'success_rate': 0.85
                },
                'vertex_comunicacion': {
                    'diagnostico': "Problema de red o configuración IP Vertex",
                    'pasos': [
                        "1. 🌐 Verificar IP estática: 192.168.50.2",
                        "2. 🔌 Revisar conexión switch DHCP",
                        "3. ⚙️ Menú Network → IP estático → 192.168.50.2/255.255.255.0",
                        "4. 🔄 Reiniciar controlador después de cambio de IP",
                        "5. 💻 Probar escritorio remoto: 192.168.50.2",
                        "6. 📡 Verificar todas EGMs conectadas al mismo switch"
                    ],
                    'prioridad': "🔴 ALTA",
                    'confidence': 0.88,
                    'usage_count': 0,
                    'success_rate': 0.80
                },
                'vertex_database': {
                    'diagnostico': "Base de datos defectuosa en Vertex Controller",
                    'pasos': [
                        "1. 💾 Verificar estado base datos en pantalla principal",
                        "2. ❌ Si no muestra 'Passed' = disco defectuoso",
                        "3. 🔄 Reemplazar disco rígido inmediatamente",
                        "4. 📊 Realizar Ram Clear: DataBase → BackUp/Restore → Ram Clear",
                        "5. 🔧 Reconfigurar controlador desde cero",
                        "6. 💿 Verificar plugin CFAST1 en Vertex 4.0"
                    ],
                    'prioridad': "🔴 ALTA",
                    'confidence': 0.90,
                    'usage_count': 0,
                    'success_rate': 0.75
                },
                'vertex_jurisdiccion': {
                    'diagnostico': "Configuración de jurisdicción incorrecta",
                    'pasos': [
                        "1. ⚙️ Configurar jurisdicción: Argentina - Buenos Aires",
                        "2. 🔄 Reiniciar controlador después del cambio",
                        "3. 📋 Verificar configuración regional",
                        "4. 🔧 Ajustar parámetros locales",
                        "5. ✅ Confirmar con test de operación"
                    ],
                    'prioridad': "🟡 MEDIA",
                    'confidence': 0.85,
                    'usage_count': 0,
                    'success_rate': 0.80
                }
            },
            
            'maquinas_especificas': {
                'aristocrat_helix': {
                    'modelo': 'Helix',
                    'fabricante': 'Aristocrat',
                    'caracteristicas': ['Touch 19"', 'Aceptador MEI SCN66', 'Vertex 3.5'],
                    'problemas_comunes': ['touch_no_responde', 'rechaza_billetes']
                },
                'aristocrat_oasis': {
                    'modelo': 'Oasis',
                    'fabricante': 'Aristocrat', 
                    'caracteristicas': ['Display 32"', 'Aceptador JCM UBA-10', 'Vertex 4.0'],
                    'problemas_comunes': ['sobrecalentamiento', 'problema_audio']
                },
                'aristocrat_edge': {
                    'modelo': 'Edge',
                    'fabricante': 'Aristocrat',
                    'caracteristicas': ['Display 27"', 'Aceptador CashFlow 7000', 'Vertex 3.5'],
                    'problemas_comunes': ['comunicacion_falla', 'problema_red']
                },
                'aristocrat_mk6': {
                    'modelo': 'MK6',
                    'fabricante': 'Aristocrat',
                    'caracteristicas': ['Display 15"', 'Aceptador Aristocrat NV9', 'Sistema Legacy'],
                    'problemas_comunes': ['no_enciende', 'error_sistema']
                },
                'bally_alphapro': {
                    'modelo': 'Alpha Pro',
                    'fabricante': 'Bally',
                    'caracteristicas': ['Display 23"', 'Aceptador MEI SCN66', 'iView Display'],
                    'problemas_comunes': ['problema_pagos', 'touch_no_responde']
                },
                'bally_iview': {
                    'modelo': 'iView',
                    'fabricante': 'Bally',
                    'caracteristicas': ['Display 19"', 'Sistema Touch', 'Player Tracking'],
                    'problemas_comunes': ['touch_no_responde', 'problema_audio']
                },
                'igt_peak': {
                    'modelo': 'Peak',
                    'fabricante': 'IGT',
                    'caracteristicas': ['Display 32"', 'Aceptador JCM UBA-10', 'Sistema Dual Screen'],
                    'problemas_comunes': ['sobrecalentamiento', 'problema_red']
                },
                'igt_s3000': {
                    'modelo': 'S3000',
                    'fabricante': 'IGT',
                    'caracteristicas': ['Display 17"', 'Aceptador MEI SCN66', 'Sistema Clásico'],
                    'problemas_comunes': ['no_enciende', 'rechaza_billetes']
                },
                'konami_concerto': {
                    'modelo': 'Concerto',
                    'fabricante': 'Konami',
                    'caracteristicas': ['Display 42"', 'Aceptador JCM UBA-10', 'Sistema Panorámico'],
                    'problemas_comunes': ['problema_audio', 'sobrecalentamiento']
                },
                'konami_kx': {
                    'modelo': 'KX',
                    'fabricante': 'Konami',
                    'caracteristicas': ['Display 23"', 'Aceptador CashFlow 7000', 'Sistema Compacto'],
                    'problemas_comunes': ['comunicacion_falla', 'problema_botones']
                },
                'aristocrat_lightning_link': {
                    'modelo': 'Lightning Link',
                    'fabricante': 'Aristocrat',
                    'caracteristicas': ['Display 32"', 'Progresivo Link', 'Vertex 4.0'],
                    'problemas_comunes': ['problema_red', 'vertex_comunicacion']
                },
                'aristocrat_celebration': {
                    'modelo': 'Celebration',
                    'fabricante': 'Aristocrat',
                    'caracteristicas': ['Display 19"', 'Aceptador MEI SCN66', 'Vertex 3.5'],
                    'problemas_comunes': ['rechaza_billetes', 'touch_no_responde']
                },
                'aristocrat_opus': {
                    'modelo': 'Opus',
                    'fabricante': 'Aristocrat',
                    'caracteristicas': ['Display 42"', 'Aceptador JCM UBA-10', 'Vertex 4.0'],
                    'problemas_comunes': ['sobrecalentamiento', 'problema_audio']
                },
                'bally_prowave': {
                    'modelo': 'ProWave',
                    'fabricante': 'Bally',
                    'caracteristicas': ['Display 27"', 'Aceptador MEI SCN66', 'iView 4'],
                    'problemas_comunes': ['problema_pagos', 'vertex_database']
                },
                'igt_avp': {
                    'modelo': 'AVP',
                    'fabricante': 'IGT',
                    'caracteristicas': ['Display 23"', 'Aceptador CashFlow 7000', 'Sistema Avanzado'],
                    'problemas_comunes': ['error_sistema', 'comunicacion_falla']
                },
                'konami_ks': {
                    'modelo': 'KS',
                    'fabricante': 'Konami',
                    'caracteristicas': ['Display 19"', 'Aceptador MEI SCN66', 'Sistema Estándar'],
                    'problemas_comunes': ['no_enciende', 'problema_botones']
                },
                'aristocrat_aurora': {
                    'modelo': 'Aurora',
                    'fabricante': 'Aristocrat',
                    'caracteristicas': ['Display 49"', '4K Resolution', 'Vertex 4.0'],
                    'problemas_comunes': ['sobrecalentamiento', 'problema_red']
                },
                'bally_canine': {
                    'modelo': 'Canine',
                    'fabricante': 'Bally',
                    'caracteristicas': ['Display 32"', 'Aceptador JCM UBA-10', 'iView 5'],
                    'problemas_comunes': ['touch_no_responde', 'problema_audio']
                },
                'igt_crystal': {
                    'modelo': 'Crystal',
                    'fabricante': 'IGT',
                    'caracteristicas': ['Display 27"', 'Aceptador MEI SCN66', 'Sistema Crystal'],
                    'problemas_comunes': ['rechaza_billetes', 'vertex_jurisdiccion']
                },
                'konami_frogger': {
                    'modelo': 'Frogger',
                    'fabricante': 'Konami',
                    'caracteristicas': ['Display 23"', 'Aceptador CashFlow 7000', 'Sistema Retro'],
                    'problemas_comunes': ['error_sistema', 'problema_pagos']
                },
                'aristocrat_dragon': {
                    'modelo': 'Dragon',
                    'fabricante': 'Aristocrat',
                    'caracteristicas': ['Display 42"', 'Aceptador JCM UBA-10', 'Vertex 4.0'],
                    'problemas_comunes': ['vertex_no_enciende', 'comunicacion_falla']
                },
                'bally_tiger': {
                    'modelo': 'Tiger',
                    'fabricante': 'Bally',
                    'caracteristicas': ['Display 32"', 'Aceptador MEI SCN66', 'iView 6'],
                    'problemas_comunes': ['problema_red', 'touch_no_responde']
                }
            }
        }

    # ==================== MÉTODOS PRINCIPALES CORREGIDOS ====================
    
    def analizar_problema(self, pregunta_usuario, datos_maquina=None, contexto=""):
        """Análisis inteligente con DeepSeek AI - VERSIÓN CORREGIDA"""
        
        # Guardar en memoria de conversación
        entrada_conversacion = {
            'timestamp': datetime.now().isoformat(),
            'question': pregunta_usuario,
            'machine': datos_maquina or {},
            'context': contexto,
            'assistant': 'CasinoPro-DeepSeek'
        }
        self.conversation_memory.append(entrada_conversacion)
        
        # ✅ VERIFICACIÓN MEJORADA de la API Key
        api_key_actual = get_deepseek_api_key()
        
        st.sidebar.info(f"🔍 ANALIZAR_PROBLEMA: API Key detectada: {bool(api_key_actual)}")
        
        # ✅ SIEMPRE USAR DEEPSEEK SI HAY API KEY (INCLUYENDO "HOLA")
        if api_key_actual and api_key_actual.startswith('sk-'):
            st.sidebar.success("✅ ANALIZAR_PROBLEMA: Usando DeepSeek API para TODAS las consultas")
            
            # ✅ DEEPSEEK ACTIVO - Usar API real para TODO
            contexto_tecnico = self._preparar_contexto_tecnico(datos_maquina, contexto)
            
            # ✅ LLAMAR DIRECTAMENTE a DeepSeek para TODOS los mensajes
            respuesta_ia = self.deepseek_api.consultar_deepseek(pregunta_usuario, contexto_tecnico)
            
            st.sidebar.info(f"🔍 ANALIZAR_PROBLEMA: Respuesta DeepSeek recibida: {len(respuesta_ia) if respuesta_ia else 0} chars")
            
            # Solo si DeepSeek falla completamente, usar sistema local
            if any(error in respuesta_ia for error in ["❌", "⚠️", "⏰", "Error API", "Timeout", "conexión"]):
                st.sidebar.warning("⚠️ ANALIZAR_PROBLEMA: DeepSeek falló, usando sistema local")
                return self._analizar_problema_local(pregunta_usuario, datos_maquina, contexto)
            
            # ✅ USAR RESPUESTA DE DEEPSEEK
            st.sidebar.success("✅ ANALIZAR_PROBLEMA: Usando respuesta DeepSeek")
            return respuesta_ia
            
        else:
            # ✅ NO HAY API KEY - Usar sistema local
            st.sidebar.warning("⚠️ ANALIZAR_PROBLEMA: Sin API Key, usando sistema local")
            return self._analizar_problema_local(pregunta_usuario, datos_maquina, contexto)
    
    def _preparar_contexto_tecnico(self, datos_maquina=None, contexto=""):
        """Preparar contexto técnico para DeepSeek"""
        contexto_tecnico = "CONTEXTO TÉCNICO CASINOPRO:\n"
        contexto_tecnico += f"- Sistema: {self.nombre} v{self.version}\n"
        contexto_tecnico += f"- Especialidades: Vertex Controller, Aristocrat, Bally, IGT, Konami\n"
        contexto_tecnico += f"- Máquinas en base: {len(self.knowledge_base['maquinas_especificas'])}\n"
        contexto_tecnico += f"- Problemas conocidos: {len(self.knowledge_base['problemas_comunes'])}\n"
        
        if datos_maquina:
            contexto_tecnico += f"- Máquina actual: {datos_maquina}\n"
        
        if contexto:
            contexto_tecnico += f"- Contexto adicional: {contexto}\n"
            
        # Agregar últimos mensajes para contexto conversacional
        if len(self.conversation_memory) > 0:
            contexto_tecnico += "\nÚLTIMOS MENSAJES:\n"
            for msg in self.conversation_memory[-3:]:
                if 'question' in msg:
                    contexto_tecnico += f"Usuario: {msg['question']}\n"
                if 'system' in msg:
                    contexto_tecnico += f"Sistema: {msg['system'][:100]}...\n"
        
        return contexto_tecnico
    
    def _analizar_problema_local(self, pregunta_usuario, datos_maquina=None, contexto=""):
        """Análisis local cuando no hay API Key disponible"""
        # Detectar tipo de problema
        tipo_problema = self._detectar_tipo_problema(pregunta_usuario)
        
        # Generar respuesta local
        respuesta_local = self._generar_respuesta_casinopro(pregunta_usuario, tipo_problema, datos_maquina)
        
        return respuesta_local
    
    def _detectar_tipo_problema(self, pregunta):
        """Detectar tipo de problema basado en palabras clave"""
        pregunta_lower = pregunta.lower()
        
        # Palabras clave para cada tipo de problema
        keywords = {
            'no_enciende': ['no enciende', 'no prende', 'sin energía', 'no power', 'apagada'],
            'comunicacion_falla': ['comunicación', 'mdb', 'rs232', 'conexión', 'network'],
            'touch_no_responde': ['touch', 'pantalla', 'no responde', 'calibración'],
            'rechaza_billetes': ['billete', 'rechaza', 'aceptador', 'validator'],
            'sobrecalentamiento': ['calor', 'sobrecalentamiento', 'ventilador', 'temperatura'],
            'vertex_no_enciende': ['vertex no enciende', 'vertex power'],
            'vertex_comunicacion': ['vertex ip', '192.168.50.2', 'vertex network'],
            'vertex_database': ['vertex database', 'ram clear', 'base datos']
        }
        
        for problema, palabras in keywords.items():
            if any(palabra in pregunta_lower for palabra in palabras):
                return problema
        
        return 'desconocido'
    
    def _generar_respuesta_casinopro(self, pregunta, tipo_problema, datos_maquina):
        """Generar respuesta usando el sistema local"""
        if tipo_problema in self.knowledge_base['problemas_comunes']:
            problema = self.knowledge_base['problemas_comunes'][tipo_problema]
            
            respuesta = f"**🔧 {problema['diagnostico']}**\n\n"
            respuesta += f"**Prioridad:** {problema['prioridad']}\n\n"
            respuesta += "**Pasos de solución:**\n"
            
            for paso in problema['pasos']:
                respuesta += f"{paso}\n"
                
            respuesta += f"\n**Confianza del diagnóstico:** {problema['confidence']*100}%"
            
        else:
            # Respuesta genérica para problemas no identificados
            respuesta = f"**🤔 Análisis de: '{pregunta}'**\n\n"
            respuesta += "**Sistema CasinoPro Local**\n\n"
            respuesta += "**Recomendaciones generales:**\n"
            respuesta += "1. 🔍 Verificar conexiones de alimentación\n"
            respuesta += "2. 🔌 Revisar todos los conectores\n"
            respuesta += "3. 🔄 Realizar reinicio completo\n"
            respuesta += "4. 📟 Consultar códigos de error en display\n"
            respuesta += "5. 🔧 Contactar soporte técnico especializado\n\n"
            respuesta += "💡 **Sugerencia:** Configurá tu API Key de DeepSeek en el sidebar para obtener diagnósticos más precisos."
        
        return respuesta
    
    def obtener_diagnostico_mejorado(self, problema, maquina=None):
        """Obtener diagnóstico mejorado usando DeepSeek"""
        st.sidebar.info("🎯 DIAGNOSTICO_MEJORADO: Iniciando...")
        
        prompt = f"Problema: {problema}"
        if maquina:
            prompt += f" | Máquina: {maquina}"
        
        prompt += "\n\nPor favor proporciona un diagnóstico técnico detallado con pasos específicos de solución."
        
        return self.deepseek_api.consultar_deepseek(prompt, "DIAGNÓSTICO TÉCNICO ESPECIALIZADO")

# ==================== INTERFAZ STREAMLIT ====================
def main():
    # Inicializar sistema en session state
    if 'diagnostic_system' not in st.session_state:
        st.session_state.diagnostic_system = CasinoProAISystem()
        st.session_state.chat_history = []
    
    # Sidebar con configuración
    mostrar_configuracion_api()
    mostrar_debug_info()
    
    # Header principal
    st.title("🎰 CasinoPro - DeepSeek AI System")
    st.markdown("### Tu asistente técnico especializado en máquinas de casino")
    
    # Verificar API Key
    api_key = get_deepseek_api_key()
    if not api_key:
        st.warning("⚠️ **Configura tu API Key de DeepSeek en el sidebar para activar la IA avanzada**")
    else:
        st.success(f"✅ **DeepSeek AI Activado** - Key: {api_key[:10]}...{api_key[-4:]}")
    
    # Área de chat
    st.markdown("---")
    st.subheader("💬 Chat con CasinoPro AI")
    
    # Mostrar historial de chat
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(chat['user'])
        with st.chat_message("assistant"):
            st.write(chat['assistant'])
    
    # Input de usuario
    user_input = st.chat_input("Escribe tu mensaje aquí...")
    
    if user_input:
        # Mostrar mensaje del usuario
        with st.chat_message("user"):
            st.write(user_input)
        
        # Obtener respuesta del sistema
        with st.chat_message("assistant"):
            with st.spinner("CasinoPro AI pensando..."):
                respuesta = st.session_state.diagnostic_system.analizar_problema(user_input)
                st.write(respuesta)
        
        # Guardar en historial
        st.session_state.chat_history.append({
            'user': user_input,
            'assistant': respuesta
        })
        
        # Limitar historial a 50 mensajes
        if len(st.session_state.chat_history) > 50:
            st.session_state.chat_history = st.session_state.chat_history[-50:]

if __name__ == "__main__":
    main()
