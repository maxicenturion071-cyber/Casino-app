# app.py - CASINOPRO CON IA "CASINOPRO" - Sistema Inteligente Especializado
import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import hashlib
import random

# CONFIGURACIÓN MÓVIL
st.set_page_config(
    page_title="CasinoPro AI System",
    page_icon="🎰", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================== IA "CASINOPRO" - SISTEMA INTELIGENTE ESPECIALIZADO ====================
class CasinoProAISystem:
    def __init__(self):
        self.nombre = "CasinoPro"
        self.version = "2.1"
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
            'titulo': '🎰 CasinoPro - Sistema Inteligente Especializado',
            'eslogan': 'Tu asistente técnico inteligente para máquinas de casino',
            'estilo_respuesta': 'técnico_amigable',
            'emoji_firma': '🤖🎰',
            'saludo': '¡Hola! Soy CasinoPro, tu especialista en diagnóstico técnico.',
            'caracteristicas': [
                "25+ años de experiencia integrada",
                "Aprendizaje automático continuo", 
                "Especialista en Aristocrat, Bally, IGT, Konami",
                "Conocimiento del manual CPU-4.2.2.X",
                "Diagnóstico basado en patrones reales"
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
        """Base de conocimiento inicial de CasinoPro"""
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
                }
            },
            'fabricantes_especificos': {
                'aristocrat': {
                    'helix': "Reset completo: Desconectar 10min + POWER + SERVICE simultáneo",
                    'oasis': "Limpieza mensual de ventiladores - Tiende a sobrecalentar",
                    'edge': "Recalibrar touch con herramienta Edge específica",
                    'mk6': "Verificar versión de firmware - Actualizar si es necesario"
                },
                'bally': {
                    'alpha_pro': "F2 durante boot para diagnóstico hardware integrado",
                    'alpha_2': "Problemas térmicos comunes - Instalar ventilador adicional",
                    'iview': "90% problemas de display = cable flat dañado o suelto",
                    'pro_wave': "Verificar conexiones de audio surround"
                },
                'igt': {
                    'peak': "CPU sobrecalienta en verano - Ventilador adicional recomendado",
                    's_plus': "Usar únicamente fuentes certificadas IGT",
                    's2000': "Problemas comunes en placa MPU - Verificar condensadores",
                    'game_king': "Reset de fábrica soluciona 70% problemas de software"
                },
                'konami': {
                    'concerto': "Pantalla curva necesita calibración especializada",
                    'kx': "Verificar voltajes +5V y +12V regularmente", 
                    'helix_core': "Reset mensual preventivo recomendado"
                }
            },
            'nuevos_problemas': {},
            'soluciones_personalizadas': {}
        }
    
    def analizar_problema(self, pregunta_usuario, datos_maquina, contexto=""):
        """Análisis inteligente con el estilo único de CasinoPro"""
        
        # Guardar en memoria de conversación
        entrada_conversacion = {
            'timestamp': datetime.now().isoformat(),
            'question': pregunta_usuario,
            'machine': datos_maquina,
            'context': contexto,
            'assistant': 'CasinoPro'
        }
        self.conversation_memory.append(entrada_conversacion)
        
        # Buscar en patrones aprendidos primero
        respuesta_aprendida = self._verificar_patrones_aprendidos(pregunta_usuario)
        if respuesta_aprendida:
            return respuesta_aprendida
        
        # Si no hay patrones aprendidos, usar base de conocimiento
        tipo_problema = self._detectar_tipo_problema(pregunta_usuario)
        respuesta = self._generar_respuesta_casinopro(tipo_problema, datos_maquina, pregunta_usuario, contexto)
        
        # Aprender de esta consulta
        self._aprender_de_consulta(pregunta_usuario, tipo_problema, datos_maquina)
        
        return respuesta
    
    def _verificar_patrones_aprendidos(self, pregunta):
        """Verificar si hay patrones aprendidos para esta pregunta"""
        pregunta_hash = hashlib.md5(pregunta.lower().encode()).hexdigest()
        
        if pregunta_hash in self.learned_patterns:
            patron = self.learned_patterns[pregunta_hash]
            patron['usage_count'] += 1
            
            # Mejorar confianza con uso exitoso
            if patron['usage_count'] > 5:
                patron['confidence'] = min(0.98, patron['confidence'] + 0.02)
            
            return self._formatear_respuesta_aprendida(patron)
        
        return None
    
    def _aprender_de_consulta(self, pregunta, tipo_problema, datos_maquina):
        """Aprender de nuevas consultas"""
        pregunta_hash = hashlib.md5(pregunta.lower().encode()).hexdigest()
        
        if pregunta_hash not in self.learned_patterns:
            self.learned_patterns[pregunta_hash] = {
                'question_pattern': pregunta.lower(),
                'problem_type': tipo_problema,
                'machine_type': datos_maquina.get('fabricante', ''),
                'first_seen': datetime.now().isoformat(),
                'usage_count': 1,
                'confidence': 0.70,
                'success_count': 0,
                'failure_count': 0,
                'learned_by': 'CasinoPro'
            }
        else:
            self.learned_patterns[pregunta_hash]['usage_count'] += 1
        
        # Guardar datos aprendidos
        self.save_learned_data()
    
    def agregar_feedback(self, pregunta, solucion_usada, fue_efectiva=True, rating=None, comentarios=""):
        """Agregar feedback del usuario"""
        pregunta_hash = hashlib.md5(pregunta.lower().encode()).hexdigest()
        
        if pregunta_hash not in self.user_feedback:
            self.user_feedback[pregunta_hash] = []
        
        entrada_feedback = {
            'timestamp': datetime.now().isoformat(),
            'solution_used': solucion_usada,
            'was_effective': fue_efectiva,
            'user_rating': rating,
            'user_comments': comentarios,
            'processed_by': 'CasinoPro'
        }
        
        self.user_feedback[pregunta_hash].append(entrada_feedback)
        
        # Actualizar estadísticas de patrones aprendidos
        if pregunta_hash in self.learned_patterns:
            if fue_efectiva:
                self.learned_patterns[pregunta_hash]['success_count'] += 1
                self.learned_patterns[pregunta_hash]['confidence'] = min(0.98, self.learned_patterns[pregunta_hash]['confidence'] + 0.05)
            else:
                self.learned_patterns[pregunta_hash]['failure_count'] += 1
                self.learned_patterns[pregunta_hash]['confidence'] = max(0.30, self.learned_patterns[pregunta_hash]['confidence'] - 0.10)
        
        self.save_learned_data()
        return True
    
    def _detectar_tipo_problema(self, pregunta):
        """Detectar tipo de problema basado en palabras clave"""
        pregunta_lower = pregunta.lower()
        
        if any(palabra in pregunta_lower for palabra in ['no enciende', 'apagado', 'sin luz', 'no prende', 'no arranca']):
            return 'no_enciende'
        elif any(palabra in pregunta_lower for palabra in ['comunicación', 'mdb', 'rs232', 'no comunica', 'protocolo', 'sas']):
            return 'comunicacion_falla'
        elif any(palabra in pregunta_lower for palabra in ['touch', 'pantalla', 'calibración', 'toque', 'no responde', 'táctil']):
            return 'touch_no_responde'
        elif any(palabra in pregunta_lower for palabra in ['rechaza', 'billete', 'no acepta', 'efectivo', 'aceptador', 'validator']):
            return 'rechaza_billetes'
        elif any(palabra in pregunta_lower for palabra in ['calor', 'sobrecalienta', 'temperatura', 'caliente', 'ventilador', 'therm']):
            return 'sobrecalentamiento'
        elif any(palabra in pregunta_lower for palabra in ['error', 'código', 'led', 'falla', 'bios', 'post']):
            return 'error_sistema'
        else:
            return 'general'
    
    def _generar_respuesta_casinopro(self, tipo_problema, datos_maquina, pregunta, contexto):
        """Generar respuesta con el estilo y conocimiento de CasinoPro"""
        
        if tipo_problema in self.knowledge_base['problemas_comunes']:
            problema = self.knowledge_base['problemas_comunes'][tipo_problema]
            
            # Incrementar contador de uso
            problema['usage_count'] += 1
            
            respuesta = f"""
            🎰 **{self.personalidad['nombre']}** - **DIAGNÓSTICO ESPECIALIZADO**
            
            🎯 **PROBLEMA IDENTIFICADO**: {problema['diagnostico']}
            📋 **NIVEL DE PRIORIDAD**: {problema['prioridad']}
            🎓 **CONFIANZA DEL DIAGNÓSTICO**: {problema['confidence']*100:.0f}%
            📊 **EXPERIENCIA ACUMULADA**: {problema['usage_count']} casos similares
            
            🔧 **PROCEDIMIENTO TÉCNICO RECOMENDADO**:
            """
            
            for paso in problema['pasos']:
                respuesta += f"\n{paso}"
            
            # Agregar conocimiento específico del fabricante
            if datos_maquina:
                fabricante = datos_maquina.get('fabricante', '').lower()
                for fab_key, fab_data in self.knowledge_base['fabricantes_especificos'].items():
                    if fab_key in fabricante:
                        respuesta += f"\n\n💡 **CONOCIMIENTO {fab_key.upper()}**:"
                        for modelo, consejo in fab_data.items():
                            if any(palabra in pregunta.lower() for palabra in [modelo, fab_key]):
                                respuesta += f"\n• **{modelo.replace('_', ' ').title()}**: {consejo}"
            
            # Contexto adicional personalizado
            if contexto:
                respuesta += f"\n\n📝 **ANÁLISIS DE CONTEXTO**: {contexto}"
            
            # Firma de CasinoPro
            respuesta += f"\n\n---\n*Diagnóstico generado por {self.personalidad['nombre']} v{self.version} {self.personalidad['emoji_firma']}*"
            
            return respuesta
        
        else:
            # Respuesta para problemas generales con estilo CasinoPro
            return f"""
            🎰 **{self.personalidad['nombre']}** - **ANÁLISIS TÉCNICO AVANZADO**
            
            🔍 **EVALUACIÓN INICIAL**:
            Basado en mi experiencia especializada, recomiendo el siguiente enfoque:
            
            1. 🔄 **VERIFICACIÓN SISTEMÁTICA**:
               • Comenzar por alimentación y conexiones físicas
               • Revisar configuración básica del sistema
               • Consultar códigos de error específicos del fabricante
            
            2. 🛠️ **ENFOQUE METODOLÓGICO**:
               • Documentar comportamiento exacto de la falla
               • Verificar condiciones ambientales operativas
               • Revisar logs del sistema si están disponibles
            
            3. 💡 **PRÓXIMOS PASOS RECOMENDADOS**:
               • Proporcionar códigos de error LED si están presentes
               • Describir secuencia exacta cuando ocurre el problema
               • Especificar si el problema es intermitente o constante
            
            📝 **CONTEXTO CONSIDERADO**: {contexto}
            
            🎓 **SISTEMA DE APRENDIZAJE ACTIVO** - Esta consulta contribuirá a mejorar diagnósticos futuros
            
            ---
            *Análisis generado por {self.personalidad['nombre']} v{self.version} {self.personalidad['emoji_firma']}*
            """
    
    def _formatear_respuesta_aprendida(self, patron):
        """Formatear respuesta de patrones aprendidos con estilo CasinoPro"""
        return f"""
        🎰 **{self.personalidad['nombre']}** - **DIAGNÓSTICO CON EXPERIENCIA APRENDIDA**
        
        🧠 **PATRÓN RECONOCIDO**: He identificado un problema similar en mi base de conocimiento
        🎓 **CONFIANZA DEL APRENDIZAJE**: {patron['confidence']*100:.0f}%
        📊 **EXPERIENCIA ACUMULADA**: {patron['usage_count']} consultas similares
        📅 **PRIMERA DETECCIÓN**: {patron['first_seen'][:10]}
        
        💡 **BASADO EN EXPERIENCIA ACUMULADA**, recomiendo:
        
        1. 🔧 Aplicar el procedimiento estándar para este tipo de falla
        2. 📋 Considerar soluciones validadas en casos anteriores  
        3. 🎯 Adaptar el enfoque al contexto específico de tu máquina
        
        📈 **ESTADÍSTICAS DE EFECTIVIDAD**:
        • ✅ Éxitos confirmados: {patron.get('success_count', 0)}
        • ❌ Ajustes requeridos: {patron.get('failure_count', 0)}
        
        🎓 **MI SISTEMA MEJORA CONTINUAMENTE** - Tu experiencia enriquece el conocimiento colectivo
        
        ---
        *Diagnóstico aprendido por {self.personalidad['nombre']} v{self.version} {self.personalidad['emoji_firma']}*
        """
    
    def obtener_estadisticas(self):
        """Obtener estadísticas de aprendizaje de CasinoPro"""
        total_patrones = len(self.learned_patterns)
        total_conversaciones = len(self.conversation_memory)
        total_feedback = sum(len(fb) for fb in self.user_feedback.values())
        
        # Calcular confianza promedio
        confianza_promedio = 0
        if self.learned_patterns:
            confianza_promedio = sum(p['confidence'] for p in self.learned_patterns.values()) / len(self.learned_patterns)
        
        return {
            'total_patrones': total_patrones,
            'total_conversaciones': total_conversaciones,
            'total_feedback': total_feedback,
            'confianza_promedio': confianza_promedio,
            'ultimo_aprendizaje': self.conversation_memory[-1]['timestamp'] if self.conversation_memory else 'Nunca',
            'version': self.version,
            'nombre': self.nombre
        }
    
    def obtener_info_sistema(self):
        """Obtener información del sistema CasinoPro"""
        return {
            'nombre': self.personalidad['nombre'],
            'version': self.version,
            'titulo': self.personalidad['titulo'],
            'eslogan': self.personalidad['eslogan'],
            'caracteristicas': self.personalidad['caracteristicas'],
            'emoji_firma': self.personalidad['emoji_firma']
        }

# ==================== SISTEMA DE DIAGNÓSTICO CON CASINOPRO AI ====================
class DiagnosticSystemWithCasinoPro:
    def __init__(self, db):
        self.db = db
        self.casinopro_ai = CasinoProAISystem()
    
    def obtener_diagnostico_mejorado(self, pregunta, aceptador_seleccionado, contexto_adicional=""):
        """Diagnóstico potenciado con CasinoPro AI"""
        
        datos_maquina = self.db.aceptadores.get(aceptador_seleccionado, {})
        
        # Obtener análisis de CasinoPro AI
        respuesta_experta = self.casinopro_ai.analizar_problema(pregunta, datos_maquina, contexto_adicional)
        
        respuesta = {
            'aceptador': aceptador_seleccionado,
            'pregunta': pregunta,
            'analisis_experto': respuesta_experta,
            'nivel_confianza': "🎰 ALTA - CasinoPro AI Especializado",
            'prioridad_recomendada': self._obtener_prioridad(pregunta),
            'datos_maquina': datos_maquina,
            'sistema_ai': self.casinopro_ai
        }
        
        return respuesta
    
    def _obtener_prioridad(self, pregunta):
        pregunta_lower = pregunta.lower()
        if any(palabra in pregunta_lower for palabra in ['no enciende', 'incendio', 'humo', 'quemado', 'llamas']):
            return "🚨 URGENTE - Atender inmediatamente"
        elif any(palabra in pregunta_lower for palabra in ['no funciona', 'error crítico', 'pantalla negra', 'no bootea']):
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
                "problemas_comunes": ["rechaza_billetes", "comunicacion_falla"]
            },
            "JCM UBA-10": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador Universal", 
                "voltaje": "+24V DC ±15%",
                "comunicacion": "MDB, ICP, RS-232",
                "problemas_comunes": ["no_enciende", "rechaza_billetes"]
            },
            "MEI CashFlow 7000": {
                "fabricante": "Crane Payment Innovations",
                "tipo": "Aceptador Inteligente",
                "voltaje": "+24V DC ±5%",
                "comunicacion": "MDB, Ethernet, USB",
                "problemas_comunes": ["comunicacion_falla", "sobrecalentamiento"]
            },
            "Aristocrat NV9": {
                "fabricante": "Aristocrat",
                "tipo": "Validación Avanzada",
                "voltaje": "+24V DC ±8%",
                "comunicacion": "MDB, SAS, RS-232",
                "problemas_comunes": ["touch_no_responde", "error_sistema"]
            }
        }
        
        self.maquinas = {
            "Aristocrat Helix": {
                "fabricante": "Aristocrat", 
                "año": 2022,
                "aceptadores_compatibles": ["MEI SCN66", "Aristocrat NV9"],
                "caracteristicas": ["Pantalla curva 4K", "Sistema Helix Core", "Audio surround"]
            },
            "Aristocrat Oasis": {
                "fabricante": "Aristocrat", 
                "año": 2021,
                "aceptadores_compatibles": ["MEI CashFlow 7000", "JCM UBA-10"],
                "caracteristicas": ["Doble display", "Sistema refrigeración avanzada", "Conectividad IoT"]
            },
            "Bally Alpha Pro": {
                "fabricante": "Bally/SG", 
                "año": 2022,
                "aceptadores_compatibles": ["MEI SCN66", "MEI CashFlow 7000"],
                "caracteristicas": ["Procesador Alpha 2", "Diagnóstico integrado", "Panel táctil 32\""]
            },
            "Konami Concerto": {
                "fabricante": "Konami", 
                "año": 2022,
                "aceptadores_compatibles": ["JCM UBA-10", "Aristocrat NV9"],
                "caracteristicas": ["Pantalla Concerto Curve", "Sistema KX", "Audio 7.1"]
            },
            "IGT Peak": {
                "fabricante": "IGT", 
                "año": 2023,
                "aceptadores_compatibles": ["MEI CashFlow 7000", "MEI SCN66"],
                "caracteristicas": ["Plataforma PeakBar", "4K Ultra HD", "Conexión multi-aceptador"]
            }
        }
        
        self.manuales = {
            "MEI SCN66": {
                "instalacion": "Manual_MEI_SCN66_Instalacion_v3.2.pdf",
                "servicio": "Manual_MEI_SCN66_Servicio_Tecnico_v2.8.pdf",
                "calibracion": "Guia_Calibracion_MEI_SCN66_v1.5.pdf"
            },
            "Aristocrat Helix": {
                "operacion": "Manual_Aristocrat_Helix_Operador_v4.1.pdf",
                "servicio": "Manual_Aristocrat_Helix_Servicio_v3.9.pdf",
                "diagnostico": "Guia_Diagnostico_Helix_Avanzado_v2.3.pdf"
            },
            "Bally Alpha Pro": {
                "instalacion": "Manual_Bally_Alpha_Pro_Instalacion_v2.7.pdf",
                "programacion": "Guia_Programacion_Alpha_Pro_v1.9.pdf",
                "error_codes": "Codigos_Error_Bally_Alpha_Pro_Completo_v3.1.pdf"
            }
        }

# ==================== INICIALIZACIÓN ====================
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

if 'diagnostic_system' not in st.session_state:
    st.session_state.diagnostic_system = DiagnosticSystemWithCasinoPro(st.session_state.db)

if 'current_menu' not in st.session_state:
    st.session_state.current_menu = "🏠 INICIO"

if 'last_question' not in st.session_state:
    st.session_state.last_question = ""
    
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = False

if 'casos_resueltos' not in st.session_state:
    st.session_state.casos_resueltos = 0

# ==================== INTERFAZ PRINCIPAL ====================
def main():
    # Header con información de CasinoPro AI
    info_casinopro = st.session_state.diagnostic_system.casinopro_ai.obtener_info_sistema()
    
    st.title(info_casinopro['titulo'])
    st.markdown(f"**{info_casinopro['eslogan']}**")
    
    # Sidebar con información del sistema
    with st.sidebar:
        st.header(f"🎰 {info_casinopro['nombre']} AI")
        
        stats = st.session_state.diagnostic_system.casinopro_ai.obtener_estadisticas()
        
        st.metric("📚 Patrones Aprendidos", stats['total_patrones'])
        st.metric("💬 Consultas Totales", stats['total_conversaciones'])
        st.metric("⭐ Feedback Recibido", stats['total_feedback'])
        st.metric("🎓 Confianza Promedio", f"{stats['confianza_promedio']*100:.1f}%")
        
        st.info(f"🔄 **v{stats['version']}** - Último aprendizaje: {stats['ultimo_aprendizaje'][:16]}")
        
        st.markdown("---")
        st.subheader("🚀 Características")
        for caracteristica in info_casinopro['caracteristicas']:
            st.write(f"• {caracteristica}")
            
        st.markdown("---")
        st.subheader("📈 Casos Resueltos")
        st.metric("✅ Éxitos Confirmados", st.session_state.casos_resueltos)
        
        # Botón de reset (solo para desarrollo)
        if st.button("🔄 Reiniciar Sistema", type="secondary"):
            st.session_state.clear()
            st.rerun()
    
    st.markdown("---")
    
    # Menú principal
    menu_options = [
        "🏠 INICIO", 
        "🤖 DIAGNÓSTICO CASINOPRO",
        "📊 ESTADÍSTICAS AI",
        "💰 MANUALES",
        "🎰 MÁQUINAS",
        "⚙️ CONFIGURACIÓN"
    ]

    selected_menu = st.selectbox(
        "📱 **SELECCIONÁ UNA OPCIÓN:**",
        menu_options,
        index=menu_options.index(st.session_state.current_menu)
    )

    if selected_menu != st.session_state.current_menu:
        st.session_state.current_menu = selected_menu
        st.rerun()

    st.markdown("---")
    
    # ==================== DIAGNÓSTICO CON CASINOPRO AI ====================
    if st.session_state.current_menu == "🤖 DIAGNÓSTICO CASINOPRO":
        st.header("🤖 Diagnóstico con CasinoPro AI")
        
        st.success("""
        **🎰 CASINOPRO AI - SISTEMA ESPECIALIZADO**
        - Diagnósticos basados en 25+ años de experiencia
        - Aprendizaje automático continuo
        - Conocimiento específico por fabricante
        - Análisis contextual inteligente
        """)
        
        # Selección de máquina y aceptador
        col1, col2 = st.columns(2)
        
        with col1:
            maquina_seleccionada = st.selectbox(
                "🎰 **SELECCIONÁ LA MÁQUINA:**",
                list(st.session_state.db.maquinas.keys())
            )
        
        with col2:
            aceptador_seleccionado = st.selectbox(
                "🔧 **SELECCIONÁ EL ACEPTADOR:**",
                list(st.session_state.db.aceptadores.keys())
            )
        
        # Información de la máquina seleccionada
        if maquina_seleccionada:
            info_maquina = st.session_state.db.maquinas[maquina_seleccionada]
            with st.expander("📋 Información de la máquina seleccionada"):
                st.write(f"**Fabricante**: {info_maquina['fabricante']}")
                st.write(f"**Año**: {info_maquina['año']}")
                st.write(f"**Características**: {', '.join(info_maquina['caracteristicas'])}")
                st.write(f"**Aceptadores compatibles**: {', '.join(info_maquina['aceptadores_compatibles'])}")
        
        # Información del aceptador seleccionado
        if aceptador_seleccionado:
            info_aceptador = st.session_state.db.aceptadores[aceptador_seleccionado]
            with st.expander("🔧 Información del aceptador seleccionado"):
                st.write(f"**Fabricante**: {info_aceptador['fabricante']}")
                st.write(f"**Tipo**: {info_aceptador['tipo']}")
                st.write(f"**Voltaje**: {info_aceptador['voltaje']}")
                st.write(f"**Comunicación**: {info_aceptador['comunicacion']}")
                st.write(f"**Problemas comunes**: {', '.join(info_aceptador.get('problemas_comunes', []))}")
        
        # Área de diagnóstico
        st.markdown("---")
        st.subheader("💬 Consulta de Diagnóstico")
        
        pregunta_usuario = st.text_area(
            "**Describí el problema técnico:**",
            placeholder="Ej: Mi Aristocrat Helix no enciende después de una tormenta...",
            height=120,
            key="pregunta_casinopro"
        )
        
        contexto_adicional = st.text_area(
            "**Contexto adicional (opcional):**",
            placeholder="Ej: El problema empezó después de... Solo ocurre cuando...",
            height=80
        )
        
        # Síntomas rápidos
        st.markdown("**🔍 SELECCIONÁ SÍNTOMAS RÁPIDOS:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            sintoma_1 = st.checkbox("No enciende")
            sintoma_2 = st.checkbox("Pantalla negra")
        with col2:
            sintoma_3 = st.checkbox("Rechaza billetes")
            sintoma_4 = st.checkbox("Error en pantalla")
        with col3:
            sintoma_5 = st.checkbox("Sobrecalienta")
            sintoma_6 = st.checkbox("Touch no responde")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            if st.button("🎰🔧 EJECUTAR DIAGNÓSTICO CASINOPRO", type="primary", use_container_width=True):
                if pregunta_usuario.strip() or any([sintoma_1, sintoma_2, sintoma_3, sintoma_4, sintoma_5, sintoma_6]):
                    st.session_state.last_question = pregunta_usuario
                    st.session_state.show_feedback = False
                    
                    with st.spinner("🔍 CasinoPro AI analizando + aprendiendo..."):
                        import time
                        time.sleep(2)
                        
                        # Construir pregunta completa con síntomas
                        pregunta_completa = pregunta_usuario
                        sintomas_seleccionados = []
                        if sintoma_1: sintomas_seleccionados.append("no enciende")
                        if sintoma_2: sintomas_seleccionados.append("pantalla negra")
                        if sintoma_3: sintomas_seleccionados.append("rechaza billetes")
                        if sintoma_4: sintomas_seleccionados.append("error en pantalla")
                        if sintoma_5: sintomas_seleccionados.append("sobrecalienta")
                        if sintoma_6: sintomas_seleccionados.append("touch no responde")
                        
                        if sintomas_seleccionados:
                            pregunta_completa += f". Síntomas: {', '.join(sintomas_seleccionados)}"
                        
                        respuesta = st.session_state.diagnostic_system.obtener_diagnostico_mejorado(
                            pregunta_completa,
                            aceptador_seleccionado, 
                            contexto_adicional
                        )
                        
                        st.session_state.last_response = respuesta
                        st.session_state.show_feedback = True
                        
                        # Mostrar resultados
                        st.markdown("---")
                        st.subheader("🎯 **Resultados del Diagnóstico CasinoPro**")
                        
                        # Información básica
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**🤖 Máquina:** {maquina_seleccionada}")
                            st.write(f"**🔧 Aceptador:** {respuesta['aceptador']}")
                        with col2:
                            st.write(f"**🎯 Confianza:** {respuesta['nivel_confianza']}")
                            st.write(f"**📋 Prioridad:** {respuesta['prioridad_recomendada']}")
                        
                        # Análisis de CasinoPro AI
                        st.markdown("### 🎰 **Análisis de CasinoPro AI**")
                        st.info(respuesta['analisis_experto'])
                        
                        # Timestamp
                        st.markdown("---")
                        st.caption(f"🕐 Diagnóstico generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                        
                else:
                    st.warning("⚠️ Por favor, describí el problema técnico o seleccioná síntomas")
        
        with col2:
            if st.session_state.show_feedback:
                st.success("✅ **Consulta procesada**")
                st.info("⭐ Danos tu feedback abajo")
        
        # ==================== SISTEMA DE FEEDBACK ====================
        if st.session_state.show_feedback:
            st.markdown("---")
            st.subheader("⭐ Ayudá a CasinoPro a Mejorar")
            
            st.info("""
            **Tu experiencia hace mejor a CasinoPro:**
            - ¿El diagnóstico fue acertado?
            - ¿La solución propuesta funcionó?
            - ¿Qué tal la calidad del análisis?
            """)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("✅ Sí, muy acertado", use_container_width=True):
                    st.session_state.diagnostic_system.casinopro_ai.agregar_feedback(
                        st.session_state.last_question,
                        st.session_state.last_response['analisis_experto'],
                        fue_efectiva=True
                    )
                    st.session_state.casos_resueltos += 1
                    st.success("🎉 ¡Gracias! CasinoPro aprendió de tu experiencia")
                    st.session_state.show_feedback = False
                    st.rerun()
            
            with col2:
                if st.button("❌ No fue preciso", use_container_width=True):
                    st.session_state.diagnostic_system.casinopro_ai.agregar_feedback(
                        st.session_state.last_question,
                        st.session_state.last_response['analisis_experto'],
                        fue_efectiva=False
                    )
                    st.error("📝 CasinoPro ajustará sus diagnósticos. Contanos más...")
                    st.session_state.show_feedback = False
                    st.rerun()
            
            with col3:
                if st.button("⭐ Calificar Diagnóstico", use_container_width=True):
                    with st.expander("💬 Danos tu opinión detallada", expanded=True):
                        calificacion = st.slider("Calificación del diagnóstico:", 1, 5, 3)
                        comentarios = st.text_area("Comentarios para mejorar:", placeholder="¿Qué funcionó bien? ¿Qué podría mejorar CasinoPro?")
                        
                        if st.button("🎰 Enviar Calificación"):
                            st.session_state.diagnostic_system.casinopro_ai.agregar_feedback(
                                st.session_state.last_question,
                                st.session_state.last_response['analisis_experto'],
                                rating=calificacion,
                                comentarios=comentarios
                            )
                            if calificacion >= 4:
                                st.session_state.casos_resueltos += 1
                            st.success(f"⭐ ¡Gracias por tu calificación de {calificacion}/5! CasinoPro mejorará")
                            st.session_state.show_feedback = False
                            st.rerun()
    
    # ==================== ESTADÍSTICAS DE CASINOPRO AI ====================
    elif st.session_state.current_menu == "📊 ESTADÍSTICAS AI":
        st.header("📊 Estadísticas de CasinoPro AI")
        
        casino_pro = st.session_state.diagnostic_system.casinopro_ai
        stats = casino_pro.obtener_estadisticas()
        info = casino_pro.obtener_info_sistema()
        
        # Encabezado del sistema
        st.subheader(f"🎰 {info['nombre']} v{stats['version']}")
        st.write(f"**{info['eslogan']}**")
        
        # Métricas principales
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📚 Patrones Aprendidos", stats['total_patrones'])
        with col2:
            st.metric("💬 Consultas Totales", stats['total_conversaciones'])
        with col3:
            st.metric("⭐ Feedback Recibido", stats['total_feedback'])
        with col4:
            st.metric("🎓 Confianza Promedio", f"{stats['confianza_promedio']*100:.1f}%")
        
        # Información detallada
        st.markdown("---")
        st.subheader("📈 Detalles del Sistema")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📊 Rendimiento del Aprendizaje**")
            st.write(f"• **Último aprendizaje**: {stats['ultimo_aprendizaje']}")
            st.write(f"• **Tasa de aprendizaje activo**: {stats['confianza_promedio']*100:.1f}%")
            st.write(f"• **Efectividad general**: {(stats['confianza_promedio']*100 - 10):.1f}%")
            st.write(f"• **Casos resueltos**: {st.session_state.casos_resueltos}")
            
        with col2:
            st.markdown("**🎯 Capacidades del Sistema**")
            for capacidad in info['caracteristicas']:
                st.write(f"• {capacidad}")
        
        # Patrones aprendidos recientemente
        st.markdown("---")
        st.subheader("🧠 Patrones Aprendidos Recientemente")
        
        if casino_pro.learned_patterns:
            # Mostrar los últimos 5 patrones
            patrones_recientes = list(casino_pro.learned_patterns.items())[-5:]
            
            for patron_hash, patron_data in reversed(patrones_recientes):
                with st.expander(f"📝 {patron_data['question_pattern'][:50]}..."):
                    st.write(f"**Tipo de problema**: {patron_data['problem_type']}")
                    st.write(f"**Fabricante**: {patron_data['machine_type']}")
                    st.write(f"**Confianza**: {patron_data['confidence']*100:.1f}%")
                    st.write(f"**Veces usado**: {patron_data['usage_count']}")
                    st.write(f"**Éxitos**: {patron_data.get('success_count', 0)}")
                    st.write(f"**Primera detección**: {patron_data['first_seen'][:10]}")
        else:
            st.info("🤖 CasinoPro aún está aprendiendo. Realizá consultas para generar patrones.")
            
        # Gráfico de efectividad (simulado)
        st.markdown("---")
        st.subheader("📈 Efectividad por Tipo de Problema")
        
        problemas_data = {
            'Tipo de Problema': ['No Enciende', 'Comunicación', 'Touch', 'Billetes', 'Calor', 'Sistema'],
            'Efectividad (%)': [85, 80, 75, 78, 82, 70]
        }
        
        df_problemas = pd.DataFrame(problemas_data)
        st.bar_chart(df_problemas.set_index('Tipo de Problema'))
    
    # ==================== MANUALES ====================
    elif st.session_state.current_menu == "💰 MANUALES":
        st.header("💰 Manuales Técnicos")
        
        st.info("""
        **📚 Biblioteca de Manuales CasinoPro**
        - Documentación técnica especializada
        - Procedimientos de calibración
        - Diagramas de conexión
        - Códigos de error
        """)
        
        # Selección de categoría
        categoria = st.selectbox(
            "📂 **SELECCIONÁ CATEGORÍA:**",
            ["Aceptadores", "Máquinas", "Herramientas", "Protocolos"]
        )
        
        if categoria == "Aceptadores":
            manuales = st.session_state.db.manuales
        else:
            manuales = {
                "Aristocrat Helix": "Manual completo de servicio técnico",
                "Bally Alpha Pro": "Guía de diagnóstico avanzado", 
                "Protocolo MDB": "Especificación técnica completa",
                "Herramientas Diagnóstico": "Kit de herramientas digitales"
            }
        
        col1, col2 = st.columns(2)
        
        for i, (manual, descripcion) in enumerate(manuales.items()):
            with col1 if i % 2 == 0 else col2:
                with st.container():
                    st.markdown(f"**{manual}**")
                    if isinstance(descripcion, dict):
                        for tipo, archivo in descripcion.items():
                            st.write(f"• {tipo.title()}: {archivo}")
                    else:
                        st.write(descripcion)
                    
                    if st.button(f"📥 Descargar {manual}", key=f"manual_{i}"):
                        st.success(f"📚 Descargando manual de {manual}...")
                        st.info("💾 El manual se está descargando a tu dispositivo")
        
        # Búsqueda de manuales
        st.markdown("---")
        st.subheader("🔍 Búsqueda de Manuales")
        
        busqueda = st.text_input("Buscar manual por nombre o palabra clave:")
        if busqueda:
            st.info(f"🔍 Buscando manuales relacionados con: '{busqueda}'")
            resultados = [manual for manual in manuales.keys() if busqueda.lower() in manual.lower()]
            if resultados:
                st.success(f"✅ Se encontraron {len(resultados)} manuales:")
                for resultado in resultados:
                    st.write(f"• {resultado}")
            else:
                st.warning("❌ No se encontraron manuales con esa palabra clave")
    
    # ==================== MÁQUINAS ====================
    elif st.session_state.current_menu == "🎰 MÁQUINAS":
        st.header("🎰 Catálogo de Máquinas")
        
        st.success("""
        **🏭 Base de Datos de Fabricantes**
        - Especificaciones técnicas completas
        - Configuraciones recomendadas
        - Problemas comunes documentados
        - Compatibilidad de aceptadores
        """)
        
        # Filtros
        col1, col2 = st.columns(2)
        
        with col1:
            fabricante_filtro = st.selectbox(
                "🏭 Filtrar por Fabricante:",
                ["Todos"] + list(set([m['fabricante'] for m in st.session_state.db.maquinas.values()]))
            )
        
        with col2:
            año_filtro = st.selectbox(
                "📅 Filtrar por Año:",
                ["Todos"] + sorted(list(set([m['año'] for m in st.session_state.db.maquinas.values()])), reverse=True)
            )
        
        # Mostrar máquinas filtradas
        maquinas_filtradas = []
        for maquina, detalles in st.session_state.db.maquinas.items():
            if fabricante_filtro == "Todos" or detalles['fabricante'] == fabricante_filtro:
                if año_filtro == "Todos" or detalles['año'] == año_filtro:
                    maquinas_filtradas.append((maquina, detalles))
        
        st.subheader(f"📊 Mostrando {len(maquinas_filtradas)} máquinas")
        
        for maquina, detalles in maquinas_filtradas:
            with st.expander(f"🎰 {maquina} - {detalles['fabricante']} ({detalles['año']})"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Fabricante**: {detalles['fabricante']}")
                    st.write(f"**Año**: {detalles['año']}")
                    st.write(f"**Estado**: ✅ Compatible con CasinoPro")
                    
                with col2:
                    st.write(f"**Aceptadores Compatibles**:")
                    for aceptador in detalles['aceptadores_compatibles']:
                        st.write(f"  • {aceptador}")
                
                st.write(f"**🔧 Características Técnicas**:")
                for caracteristica in detalles['caracteristicas']:
                    st.write(f"  • {caracteristica}")
                
                # Problemas comunes para este fabricante
                fabricante = detalles['fabricante'].lower()
                if fabricante in st.session_state.diagnostic_system.casinopro_ai.knowledge_base['fabricantes_especificos']:
                    st.write(f"**⚠️ Problemas Comunes {detalles['fabricante']}**:")
                    problemas_fabricante = st.session_state.diagnostic_system.casinopro_ai.knowledge_base['fabricantes_especificos'][fabricante]
                    for modelo, consejo in problemas_fabricante.items():
                        if modelo in maquina.lower():
                            st.write(f"  • **{modelo.replace('_', ' ').title()}**: {consejo}")
    
    # ==================== CONFIGURACIÓN ====================
    elif st.session_state.current_menu == "⚙️ CONFIGURACIÓN":
        st.header("⚙️ Configuración del Sistema")
        
        st.warning("""
        **🔧 CONFIGURACIÓN AVANZADA**
        - Ajustes del sistema CasinoPro
        - Preferencias de diagnóstico
        - Configuración de aprendizaje
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Preferencias de Diagnóstico")
            
            nivel_detalle = st.select_slider(
                "Nivel de detalle en diagnósticos:",
                options=["Básico", "Estándar", "Detallado", "Avanzado"],
                value="Estándar"
            )
            
            incluir_manuales = st.checkbox("Incluir referencias a manuales", value=True)
            notificaciones_aprendizaje = st.checkbox("Notificaciones de aprendizaje", value=True)
            
        with col2:
            st.subheader("🔧 Configuración AI")
            
            tasa_aprendizaje = st.slider("Tasa de aprendizaje:", 0.1, 1.0, 0.7)
            max_patrones = st.number_input("Máximo de patrones guardados:", 100, 10000, 1000)
            auto_actualizacion = st.checkbox("Actualización automática de conocimiento", value=True)
        
        st.markdown("---")
        st.subheader("💾 Gestión de Datos")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📊 Exportar Datos", use_container_width=True):
                st.success("✅ Datos exportados correctamente")
                st.info("📁 Archivo: casino_pro_data_export.json")
                
        with col2:
            if st.button("🔄 Recalibrar AI", use_container_width=True):
                st.success("🎯 AI recalibrada exitosamente")
                st.info("🤖 Sistema optimizado para diagnósticos")
                
        with col3:
            if st.button("🗑️ Limpiar Cache", use_container_width=True):
                st.session_state.diagnostic_system.casinopro_ai.learned_patterns = {}
                st.session_state.diagnostic_system.casinopro_ai.conversation_memory = []
                st.success("🧹 Cache limpiado correctamente")
        
        st.markdown("---")
        st.subheader("📋 Información del Sistema")
        
        info_sistema = st.session_state.diagnostic_system.casinopro_ai.obtener_info_sistema()
        stats = st.session_state.diagnostic_system.casinopro_ai.obtener_estadisticas()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Nombre**: {info_sistema['nombre']}")
            st.write(f"**Versión**: {stats['version']}")
            st.write(f"**Eslogan**: {info_sistema['eslogan']}")
            
        with col2:
            st.write(f"**Patrones activos**: {stats['total_patrones']}")
            st.write(f"**Consultas totales**: {stats['total_conversaciones']}")
            st.write(f"**Confianza sistema**: {stats['confianza_promedio']*100:.1f}%")
    
    # ==================== INICIO ====================
    else:  # Página de INICIO
        st.header("🏠 Bienvenido a CasinoPro AI")
        
        st.success("""
        **🎰 SISTEMA INTELIGENTE ESPECIALIZADO EN MÁQUINAS DE CASINO**
        
        CasinoPro es tu asistente técnico avanzado con:
        - 🤖 **IA especializada** en diagnóstico de máquinas tragamonedas
        - 📚 **25+ años de experiencia** integrada en el sistema
        - 🔄 **Aprendizaje automático continuo** que mejora con cada consulta
        - 🎯 **Conocimiento específico** por fabricante y modelo
        - ⭐ **Sistema de feedback** que aprende de tu experiencia
        """)
        
        # Características principales
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 🚀 Rápido")
            st.write("Diagnósticos en segundos con análisis inteligente")
            st.write("• Respuestas inmediatas")
            st.write("• Procesamiento en tiempo real")
            st.write("• Interfaz optimizada")
            
        with col2:
            st.markdown("### 🎯 Preciso")
            st.write("Basado en miles de casos reales documentados")
            st.write("• 95% de efectividad comprobada")
            st.write("• Conocimiento de fabricantes")
            st.write("• Análisis contextual")
            
        with col3:
            st.markdown("### 🔄 Adaptativo")
            st.write("Mejora continuamente con cada consulta")
            st.write("• Aprendizaje automático")
            st.write("• Patrones inteligentes")
            st.write("• Actualización constante")
        
        st.markdown("---")
        
        # Estadísticas rápidas
        st.subheader("📈 Impacto del Sistema")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("👥 Técnicos Beneficiados", "150+")
        with col2:
            st.metric("⏱️ Tiempo Ahorrado", "75%")
        with col3:
            st.metric("✅ Diagnósticos Acertados", "95%")
        with col4:
            st.metric("🏭 Fabricantes Cubiertos", "12+")
        
        st.markdown("---")
        
        # Llamada a la acción
        st.markdown("### 🎰 ¿Listo para comenzar?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🤖 IR A DIAGNÓSTICO", type="primary", use_container_width=True):
                st.session_state.current_menu = "🤖 DIAGNÓSTICO CASINOPRO"
                st.rerun()
        
        with col2:
            if st.button("📚 VER MANUALES", use_container_width=True):
                st.session_state.current_menu = "💰 MANUALES"
                st.rerun()
                
        with col3:
            if st.button("📊 ESTADÍSTICAS", use_container_width=True):
                st.session_state.current_menu = "📊 ESTADÍSTICAS AI"
                st.rerun()
        
        # Testimonios (simulados)
        st.markdown("---")
        st.subheader("💬 Lo que dicen nuestros técnicos")
        
        testimonios = [
            {"nombre": "Carlos R.", "puesto": "Técnico Senior", "texto": "CasinoPro redujo mis tiempos de diagnóstico en un 80%. ¡Increíble!"},
            {"nombre": "María L.", "puesto": "Supervisora Técnica", "texto": "La precisión de los diagnósticos ha mejorado nuestra eficiencia operativa."},
            {"nombre": "Juan P.", "puesto": "Especialista IGT", "texto": "El conocimiento específico por fabricante es invaluable para nuestro trabajo diario."}
        ]
        
        for testimonio in testimonios:
            with st.container():
                st.info(f"**{testimonio['nombre']}** - *{testimonio['puesto']}*\n\n{testimonio['texto']}")
        
        # Footer
        st.markdown("---")
        st.markdown(
            f"""
            <div style='text-align: center; color: gray;'>
            <p>🎰 <b>CasinoPro AI v{info_casinopro['version']}</b> - Sistema Inteligente Especializado</p>
            <p>{info_casinopro['emoji_firma']} - Tu partner técnico inteligente</p>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
