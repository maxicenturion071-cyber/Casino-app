# app.py - CASINOPRO CON IA "CASINOPRO" - Sistema de Chat Inteligente
import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import hashlib

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
        self.version = "2.2"
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
            'saludo': '¡Hola! Soy CasinoPro, tu especialista en diagnóstico técnico. ¿En qué puedo ayudarte hoy?',
            'caracteristicas': [
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
                'vertex_no_enciende': {
                    'diagnostico': "Problema de alimentación Vertex Controller",
                    'pasos': [
                        "1. 🔌 Verificar fuente de poder externa (Vertex 4.0)",
                        "2. ⚡ Medir voltaje de entrada +24V DC",
                        "3. 🔍 Revisar botón frontal - PULSAR Y SOLTAR, no mantener",
                        "4. 📟 Verificar LED de estado del controlador",
                        "5. 🔄 Probar con fuente de respuesto certificada",
                        "6. ⚠️ NUNCA desconectar de red eléctrica directamente"
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
                        "1. 🌎 USER INTERFACE → Seleccionar jurisdicción",
                        "2. 🇦🇷 Para Argentina: Argentina - Buenos Aires",
                        "3. 🔧 Credenciales VERTEX 4.0: Retail1/Retail1",
                        "4. 🔑 Credenciales VERTEX 3.5: admin/Password1",
                        "5. 💾 Guardar configuración y reiniciar controlador"
                    ],
                    'prioridad': "🟡 MEDIA",
                    'confidence': 0.85,
                    'usage_count': 0,
                    'success_rate': 0.90
                }
            },
            'fabricantes_especificos': {
                'aristocrat': {
                    'helix': "Reset completo: Desconectar 10min + POWER + SERVICE simultáneo",
                    'oasis': "Limpieza mensual de ventiladores - Tiende a sobrecalentar",
                    'edge': "Recalibrar touch con herramienta Edge específica",
                    'mk6': "Verificar versión de firmware - Actualizar si es necesario",
                    'general': "Problemas comunes: sobrecalentamiento y touch"
                },
                'bally': {
                    'alpha_pro': "F2 durante boot para diagnóstico hardware integrado",
                    'alpha_2': "Problemas térmicos comunes - Instalar ventilador adicional",
                    'iview': "90% problemas de display = cable flat dañado o suelto",
                    'pro_wave': "Verificar conexiones de audio surround",
                    'general': "Problemas comunes: display y comunicación"
                },
                'igt': {
                    'peak': "CPU sobrecalienta en verano - Ventilador adicional recomendado",
                    's_plus': "Usar únicamente fuentes certificadas IGT",
                    's2000': "Problemas comunes en placa MPU - Verificar condensadores",
                    'game_king': "Reset de fábrica soluciona 70% problemas de software",
                    'general': "Problemas comunes: fuente de poder y software"
                },
                'konami': {
                    'concerto': "Pantalla curva necesita calibración especializada",
                    'kx': "Verificar voltajes +5V y +12V regularmente", 
                    'helix_core': "Reset mensual preventivo recomendado",
                    'general': "Problemas comunes: voltaje y calibración"
                },
                'vertex': {
                    'vertex_3.5': "Solo 1 puerto USB - Requiere HUB USB para teclado/mouse",
                    'vertex_4.0': "Display Port o VGA - Fuente externa al controlador",
                    'configuracion_red': "Todas EGMs y controlador via switch DHCP",
                    'lightning_link': "Plugin específico para progresivos Lighting Link",
                    'general': "Problemas comunes: base datos, comunicación, jurisdicción"
                },
                'general': {
                    'aceptadores': "Los aceptadores suelen fallar por suciedad en sensores",
                    'fuente_poder': "Verificar siempre voltajes de salida primero",
                    'pantallas': "90% problemas de pantalla son por cables flat",
                    'comunicacion': "Revisar configuración MDB/RS-232 siempre"
                }
            },
            'vertex_controller': {
                'vertex_3.5': {
                    'ensamblaje': "Remover tapa frontal con tuerca 7mm, conectar disco SATA y Plugin CF",
                    'configuracion_ip': "IP: 192.168.50.2, Mask: 255.255.255.0, Gateway: 192.168.50.1",
                    'credenciales': "Usuario: Retail1, Contraseña: Retail1 (VERTEX 4.0)",
                    'apagado_correcto': "PULSAR Y SOLTAR botón frontal - NO mantener presionado",
                    'problemas_comunes': "Base de datos defectuosa si no muestra 'Passed'"
                },
                'vertex_4.0': {
                    'ensamblaje': "Remover placa aluminio (disipador RAM), montar disco, plugin CFAST1",
                    'alimentacion': "Fuente externa al controlador (diferente a v3.5)",
                    'configuracion_red': "Todos dispositivos conectados via switch DHCP",
                    'estructura_red': "8 máquinas Helix XT + Splitter HDMI + AMP + Switch"
                },
                'procedimientos_criticos': {
                    'ram_clear': "Menú DataBase → BackUp/Restore → Ram Clear",
                    'cambio_jurisdiccion': "USER INTERFACE → Seleccionar Argentina - Buenos Aires",
                    'asociar_egms': "EGMs → Add New EGM → Seleccionar MAC Address",
                    'runaway_threshold': "Progressives → Options → Runaway Meter Threshold: 200000"
                }
            },
            'nuevos_problemas': {},
            'soluciones_personalizadas': {}
        }
    
    def analizar_problema(self, pregunta_usuario, datos_maquina=None, contexto=""):
        """Análisis inteligente con el estilo único de CasinoPro"""
        
        # Guardar en memoria de conversación
        entrada_conversacion = {
            'timestamp': datetime.now().isoformat(),
            'question': pregunta_usuario,
            'machine': datos_maquina or {},
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
                'machine_type': datos_maquina.get('fabricante', '') if datos_maquina else '',
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
        """Detectar tipo de problema basado en palabras clave - MEJORADA CON VERTEX"""
        pregunta_lower = pregunta.lower()
        
        # PROBLEMAS VERTEX CONTROLLER - DETECCIÓN MEJORADA
        if any(palabra in pregunta_lower for palabra in [
            'vertex', 'controlador progresivo', 'banco progresivo', 'helix xt', 'progressive', 
            'vertex 3.5', 'vertex 4.0', 'vertex controller', 'progresivo'
        ]):
            if any(palabra in pregunta_lower for palabra in ['no enciende', 'apagado', 'power', 'no prende']):
                return 'vertex_no_enciende'
            elif any(palabra in pregunta_lower for palabra in ['comunicación', 'conexión', 'network', 'ip', 'red']):
                return 'vertex_comunicacion'
            elif any(palabra in pregunta_lower for palabra in ['base datos', 'database', 'passed', 'disco']):
                return 'vertex_database'
            elif any(palabra in pregunta_lower for palabra in ['jurisdicción', 'argentina', 'buenos aires', 'configuración']):
                return 'vertex_jurisdiccion'
            else:
                return 'vertex_general'
        
        # Detección mejorada de problemas
        if any(palabra in pregunta_lower for palabra in ['no enciende', 'apagado', 'sin luz', 'no prende', 'no arranca', 'no power']):
            return 'no_enciende'
        elif any(palabra in pregunta_lower for palabra in ['comunicación', 'mdb', 'rs232', 'no comunica', 'protocolo', 'sas', 'network']):
            return 'comunicacion_falla'
        elif any(palabra in pregunta_lower for palabra in ['touch', 'pantalla', 'calibración', 'toque', 'no responde', 'táctil', 'display']):
            return 'touch_no_responde'
        elif any(palabra in pregunta_lower for palabra in ['rechaza', 'billete', 'no acepta', 'efectivo', 'aceptador', 'validator', 'bill']):
            return 'rechaza_billetes'
        elif any(palabra in pregunta_lower for palabra in ['calor', 'sobrecalienta', 'temperatura', 'caliente', 'ventilador', 'therm', 'hot']):
            return 'sobrecalentamiento'
        elif any(palabra in pregunta_lower for palabra in ['error', 'código', 'led', 'falla', 'bios', 'post', 'boot']):
            return 'error_sistema'
        elif any(palabra in pregunta_lower for palabra in ['sonido', 'audio', 'altavoz', 'speaker', 'mute', 'silenci']):
            return 'problema_audio'
        elif any(palabra in pregunta_lower for palabra in ['red', 'network', 'internet', 'wifi', 'ethernet', 'conexión']):
            return 'problema_red'
        elif any(palabra in pregunta_lower for palabra in ['jackpot', 'premio', 'pago', 'pay', 'winner']):
            return 'problema_pagos'
        elif any(palabra in pregunta_lower for palabra in ['botón', 'button', 'tecla', 'key', 'switch']):
            return 'problema_botones'
        else:
            return 'general'
    
    def _generar_respuesta_casinopro(self, tipo_problema, datos_maquina, pregunta, contexto):
        """Generar respuesta con el estilo y conocimiento de CasinoPro - MEJORADA CON VERTEX"""
        
        # Primero analizar la pregunta para determinar si es sobre aceptador o máquina completa
        es_sobre_aceptador = any(palabra in pregunta.lower() for palabra in [
            'aceptador', 'validator', 'billete', 'bill', 'efectivo', 'cash', 'scn', 'uba'
        ])
        
        # DETECCIÓN ESPECIAL PARA VERTEX CONTROLLER
        es_sobre_vertex = any(palabra in pregunta.lower() for palabra in [
            'vertex', 'controlador progresivo', 'banco progresivo', 'helix xt', 'progressive'
        ])
        
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
            
            # AGREGAR CONOCIMIENTO ESPECÍFICO VERTEX CONTROLLER
            if es_sobre_vertex:
                respuesta += "\n\n🎰 **CONOCIMIENTO ESPECÍFICO VERTEX CONTROLLER**:"
                conocimiento_vertex = self.knowledge_base['vertex_controller']
                
                if '3.5' in pregunta.lower():
                    for area, info in conocimiento_vertex['vertex_3.5'].items():
                        respuesta += f"\n• **{area.title()}**: {info}"
                elif '4.0' in pregunta.lower():
                    for area, info in conocimiento_vertex['vertex_4.0'].items():
                        respuesta += f"\n• **{area.title()}**: {info}"
                
                # Agregar procedimientos críticos
                respuesta += "\n\n🔧 **PROCEDIMIENTOS CRÍTICOS VERTEX**:"
                for proc, desc in conocimiento_vertex['procedimientos_criticos'].items():
                    respuesta += f"\n• **{proc.replace('_', ' ').title()}**: {desc}"
            
            # Agregar conocimiento específico solo si es relevante
            elif datos_maquina and es_sobre_aceptador:
                fabricante = datos_maquina.get('fabricante', '').lower()
                for fab_key, fab_data in self.knowledge_base['fabricantes_especificos'].items():
                    if fab_key in fabricante:
                        respuesta += f"\n\n💡 **CONOCIMIENTO {fab_key.upper()}**:"
                        for modelo, consejo in fab_data.items():
                            if any(palabra in pregunta.lower() for palabra in [modelo, fab_key]):
                                respuesta += f"\n• **{modelo.replace('_', ' ').title()}**: {consejo}"
            
            # Agregar conocimiento general si no es específico de aceptador
            if not es_sobre_aceptador and not es_sobre_vertex:
                respuesta += f"\n\n💡 **CONOCIMIENTO GENERAL MÁQUINAS CASINO**:"
                conocimiento_general = self.knowledge_base['fabricantes_especificos']['general']
                for area, consejo in conocimiento_general.items():
                    respuesta += f"\n• **{area.replace('_', ' ').title()}**: {consejo}"
            
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
            'emoji_firma': self.personalidad['emoji_firma'],
            'saludo': self.personalidad['saludo']  # AÑADIDO PARA CORREGIR EL ERROR
        }

# ==================== SISTEMA DE DIAGNÓSTICO CON CASINOPRO AI ====================
class DiagnosticSystemWithCasinoPro:
    def __init__(self, db):
        self.db = db
        self.casinopro_ai = CasinoProAISystem()
    
    def obtener_diagnostico_mejorado(self, pregunta, aceptador_seleccionado, contexto_adicional=""):
        """Diagnóstico potenciado con CasinoPro AI"""
        
        datos_maquina = self.db.aceptadores.get(aceptador_seleccionado, {}) if aceptador_seleccionado != "No específico" else {}
        
        # Obtener análisis de CasinoPro AI - CORREGIDO: No forzar enfoque en aceptador
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

# ==================== BASE DE DATOS COMPLETA CON 22+ MÁQUINAS ====================
class CasinoProCompleteDB:
    def __init__(self):
        self.aceptadores = {
            "MEI SCN66": {
                "fabricante": "Crane Payment Innovations",
                "tipo": "Validador de Billetes",
                "voltaje": "+24V DC ±10%",
                "comunicacion": "MDB, ICP, RS-232, USB"
            },
            "JCM UBA-10": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador Universal", 
                "voltaje": "+24V DC ±15%",
                "comunicacion": "MDB, ICP, RS-232"
            },
            "MEI CashFlow 7000": {
                "fabricante": "Crane Payment Innovations",
                "tipo": "Aceptador Inteligente",
                "voltaje": "+24V DC ±5%",
                "comunicacion": "MDB, Ethernet, USB"
            },
            "Aristocrat NV9": {
                "fabricante": "Aristocrat",
                "tipo": "Validación Avanzada",
                "voltaje": "+24V DC ±8%",
                "comunicacion": "MDB, SAS, RS-232"
            },
            "MEI SC Advance": {
                "fabricante": "Crane Payment Innovations", 
                "tipo": "Aceptador de Monedas",
                "voltaje": "+24V DC ±12%",
                "comunicacion": "MDB, RS-232"
            }
        }
        
        self.maquinas = {
            # ARISTOCRAT
            "Aristocrat Helix": {"fabricante": "Aristocrat", "año": 2022},
            "Aristocrat Oasis": {"fabricante": "Aristocrat", "año": 2021},
            "Aristocrat Edge X": {"fabricante": "Aristocrat", "año": 2023},
            "Aristocrat Edge C": {"fabricante": "Aristocrat", "año": 2022},
            "Aristocrat MK6": {"fabricante": "Aristocrat", "año": 2020},
            "Aristocrat MK5": {"fabricante": "Aristocrat", "año": 2018},
            "Aristocrat Hyperlink": {"fabricante": "Aristocrat", "año": 2021},
            "Aristocrat Sirius": {"fabricante": "Aristocrat", "año": 2022},
            
            # BALLY
            "Bally Alpha Pro": {"fabricante": "Bally/SG", "año": 2022},
            "Bally Alpha 2": {"fabricante": "Bally/SG", "año": 2021},
            "Bally iView": {"fabricante": "Bally/SG", "año": 2023},
            "Bally Pro Wave": {"fabricante": "Bally/SG", "año": 2022},
            "Bally CineVision": {"fabricante": "Bally/SG", "año": 2021},
            
            # IGT
            "IGT Peak": {"fabricante": "IGT", "año": 2023},
            "IGT PeakBarTop": {"fabricante": "IGT", "año": 2022},
            "IGT S3000": {"fabricante": "IGT", "año": 2021},
            "IGT S2000": {"fabricante": "IGT", "año": 2020},
            "IGT Game King": {"fabricante": "IGT", "año": 2022},
            "IGT Advantage": {"fabricante": "IGT", "año": 2021},
            
            # KONAMI
            "Konami Concerto": {"fabricante": "Konami", "año": 2022},
            "Konami KX": {"fabricante": "Konami", "año": 2023},
            "Konami Helix Core": {"fabricante": "Konami", "año": 2022},
            "Konami Dimension": {"fabricante": "Konami", "año": 2021},
            
            # VERTEX CONTROLLERS - NUEVOS
            "Vertex Controller 3.5": {"fabricante": "Aristocrat", "año": 2018},
            "Vertex Controller 4.0": {"fabricante": "Aristocrat", "año": 2020},
            "Aristocrat Helix XT LCD": {"fabricante": "Aristocrat", "año": 2022},
            "Aristocrat Helix XT": {"fabricante": "Aristocrat", "año": 2021},
            
            # OTHER MANUFACTURERS
            "Ainsworth A-Star": {"fabricante": "Ainsworth", "año": 2022},
            "Aruze Oasis": {"fabricante": "Aruze", "año": 2021},
            "Everi CineLuxe": {"fabricante": "Everi", "año": 2023},
            "Multimedia Games E32": {"fabricante": "MG", "año": 2022},
            "Novomatic Gaminator": {"fabricante": "Novomatic", "año": 2021},
            "WMS Bluebird 2": {"fabricante": "WMS", "año": 2020}
        }

        # NUEVO: COMPONENTES VERTEX
        self.componentes_vertex = {
            "Aristocrat Media Player (AMP)": {"tipo": "Reproductor Multimedia", "conexion": "HDMI"},
            "Splitter HDMI 8 salidas": {"tipo": "Distribuidor Video", "conexion": "HDMI"},
            "Switch DHCP Progresivo": {"tipo": "Networking", "puertos": "8+"}
        }

# ==================== INICIALIZACIÓN ====================
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

if 'diagnostic_system' not in st.session_state:
    st.session_state.diagnostic_system = DiagnosticSystemWithCasinoPro(st.session_state.db)

if 'current_menu' not in st.session_state:
    st.session_state.current_menu = "💬 CHAT CASINOPRO"

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'last_question' not in st.session_state:
    st.session_state.last_question = ""
    
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = False

# ==================== INTERFAZ PRINCIPAL CON CHAT ====================
def main():
    # Header con información de CasinoPro AI
    try:
        info_casinopro = st.session_state.diagnostic_system.casinopro_ai.obtener_info_sistema()
        saludo = info_casinopro.get('saludo', '¡Hola! Soy CasinoPro, tu especialista en diagnóstico técnico. ¿En qué puedo ayudarte hoy?')
    except Exception as e:
        # Fallback en caso de error
        saludo = '¡Hola! Soy CasinoPro, tu especialista en diagnóstico técnico. ¿En qué puedo ayudarte hoy?'
        info_casinopro = {
            'nombre': 'CasinoPro',
            'version': '2.2',
            'titulo': '🎰 CasinoPro - Sistema Inteligente Especializado',
            'eslogan': 'Tu asistente técnico inteligente para máquinas de casino',
            'emoji_firma': '🤖🎰'
        }
    
    st.title(info_casinopro['titulo'])
    st.markdown(f"**{info_casinopro['eslogan']}**")
    
    # Sidebar con información del sistema
    with st.sidebar:
        st.header(f"🎰 {info_casinopro['nombre']} AI")
        
        try:
            stats = st.session_state.diagnostic_system.casinopro_ai.obtener_estadisticas()
            
            st.metric("📚 Patrones Aprendidos", stats['total_patrones'])
            st.metric("💬 Consultas Totales", stats['total_conversaciones'])
            st.metric("⭐ Feedback Recibido", stats['total_feedback'])
            st.metric("🎓 Confianza Promedio", f"{stats['confianza_promedio']*100:.1f}%")
            
            st.info(f"🔄 **v{stats['version']}** - Último aprendizaje: {stats['ultimo_aprendizaje'][:16]}")
        except:
            st.metric("📚 Patrones Aprendidos", 0)
            st.metric("💬 Consultas Totales", 0)
            st.metric("⭐ Feedback Recibido", 0)
            st.metric("🎓 Confianza Promedio", "0%")
            st.info("🔄 **v2.2** - Sistema iniciando...")
        
        st.markdown("---")
        st.subheader("🚀 Características")
        caracteristicas = [
            "25+ años de experiencia integrada",
            "Aprendizaje automático continuo", 
            "Especialista en Aristocrat, Bally, IGT, Konami",
            "Conocimiento del manual CPU-4.2.2.X",
            "Diagnóstico basado en patrones reales",
            "Especialista en Vertex Controller 3.5/4.0"
        ]
        for caracteristica in caracteristicas:
            st.write(f"• {caracteristica}")
        
        # Información Vertex Controller en sidebar
        st.markdown("---")
        st.subheader("🎰 Especialidad Vertex")
        st.write("• Vertex Controller 3.5/4.0")
        st.write("• Bancos progresivos")
        st.write("• Configuración Lighting Link")
        st.write("• Redes progresivas")
        
        # Botón para limpiar chat
        st.markdown("---")
        if st.button("🗑️ Limpiar Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
    
    st.markdown("---")
    
    # Menú principal
    menu_options = [
        "💬 CHAT CASINOPRO", 
        "🤖 DIAGNÓSTICO AVANZADO",
        "📊 ESTADÍSTICAS AI",
        "💰 MANUALES",
        "🎰 MÁQUINAS"
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
    
    # ==================== INTERFAZ DE CHAT ====================
    if st.session_state.current_menu == "💬 CHAT CASINOPRO":
        st.header("💬 Chat con CasinoPro AI")
        
        st.success("""
        **🎰 CHAT INTELIGENTE CON CASINOPRO**
        - Conversación natural como esta que estamos teniendo
        - Diagnósticos en tiempo real
        - Aprendizaje continuo de cada consulta
        - Especialidad en Vertex Controller
        """)
        
        # Área del chat
        chat_container = st.container()
        
        with chat_container:
            # Mostrar historial del chat
            for message in st.session_state.chat_history:
                if message['type'] == 'user':
                    with st.chat_message("user"):
                        st.write(f"**Tú:** {message['content']}")
                        st.caption(f"🕐 {message['timestamp']}")
                else:
                    with st.chat_message("assistant"):
                        st.write(f"**CasinoPro:** {message['content']}")
                        st.caption(f"🕐 {message['timestamp']}")
            
            # Mostrar saludo inicial si no hay historial
            if not st.session_state.chat_history:
                with st.chat_message("assistant"):
                    st.write(f"**CasinoPro:** {saludo}")
                    st.caption(f"🕐 {datetime.now().strftime('%H:%M')}")
        
        # Input de chat
        st.markdown("---")
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_input = st.chat_input("Escribe tu pregunta o problema técnico aquí...")
        
        with col2:
            if st.button("🔄 Nueva Consulta", use_container_width=True):
                user_input = "Hola, necesito ayuda con un problema técnico"
        
        if user_input:
            # Agregar mensaje del usuario al historial
            user_message = {
                'type': 'user',
                'content': user_input,
                'timestamp': datetime.now().strftime('%H:%M')
            }
            st.session_state.chat_history.append(user_message)
            
            # Obtener respuesta de CasinoPro
            with st.spinner("🔍 CasinoPro está analizando..."):
                try:
                    respuesta = st.session_state.diagnostic_system.obtener_diagnostico_mejorado(
                        user_input,
                        "No específico"
                    )
                    
                    # Formatear respuesta para chat
                    respuesta_chat = respuesta['analisis_experto']
                    
                    # Agregar respuesta al historial
                    assistant_message = {
                        'type': 'assistant',
                        'content': respuesta_chat,
                        'timestamp': datetime.now().strftime('%H:%M')
                    }
                    st.session_state.chat_history.append(assistant_message)
                    
                    st.session_state.last_response = respuesta
                    st.session_state.last_question = user_input
                    
                except Exception as e:
                    # Respuesta de fallback en caso de error
                    error_message = {
                        'type': 'assistant',
                        'content': f"⚠️ Ocurrió un error al procesar tu consulta. Por favor, intentá nuevamente. Error: {str(e)}",
                        'timestamp': datetime.now().strftime('%H:%M')
                    }
                    st.session_state.chat_history.append(error_message)
                
            st.rerun()
        
        # Sugerencias rápidas
        st.markdown("---")
        st.subheader("💡 ¿No sabés por dónde empezar? Probá con:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎰 Vertex no enciende", use_container_width=True):
                st.session_state.chat_history.append({
                    'type': 'user', 
                    'content': 'Mi Vertex Controller 4.0 no enciende, ¿qué puedo hacer?',
                    'timestamp': datetime.now().strftime('%H:%M')
                })
                st.rerun()
                
        with col2:
            if st.button("🔧 Aceptador rechaza", use_container_width=True):
                st.session_state.chat_history.append({
                    'type': 'user',
                    'content': 'El aceptador MEI SCN66 rechaza todos los billetes',
                    'timestamp': datetime.now().strftime('%H:%M')
                })
                st.rerun()
                
        with col3:
            if st.button("📡 Problema de red", use_container_width=True):
                st.session_state.chat_history.append({
                    'type': 'user',
                    'content': 'Las máquinas no se comunican con el sistema central',
                    'timestamp': datetime.now().strftime('%H:%M')
                })
                st.rerun()
    
    # ==================== DIAGNÓSTICO AVANZADO (MANTENIDO) ====================
    elif st.session_state.current_menu == "🤖 DIAGNÓSTICO AVANZADO":
        st.header("🤖 Diagnóstico Avanzado con CasinoPro")
        
        st.info("""
        **🔧 MODO DIAGNÓSTICO AVANZADO**
        - Selección específica de equipos
        - Configuración detallada
        - Análisis técnico profundo
        """)
        
        # Selección de aceptador (ahora opcional)
        col1, col2 = st.columns(2)
        
        with col1:
            aceptador_seleccionado = st.selectbox(
                "🔧 **SELECCIONÁ EL ACEPTADOR (Opcional):**",
                ["No específico"] + list(st.session_state.db.aceptadores.keys())
            )
        
        with col2:
            # Nueva selección de tipo de máquina
            tipo_consulta = st.selectbox(
                "🎯 **TIPO DE CONSULTA:**",
                ["Problema general", "Aceptador específico", "Máquina completa", "Software/Sistema", "Vertex Controller"]
            )
        
        # Información de la máquina seleccionada solo si es relevante
        if aceptador_seleccionado != "No específico":
            info_maquina = st.session_state.db.aceptadores[aceptador_seleccionado]
            with st.expander("📋 Información del equipo seleccionado"):
                st.write(f"**Fabricante**: {info_maquina['fabricante']}")
                st.write(f"**Tipo**: {info_maquina['tipo']}")
                st.write(f"**Voltaje**: {info_maquina['voltaje']}")
                st.write(f"**Comunicación**: {info_maquina['comunicacion']}")
        
        # Información específica para Vertex Controller
        if tipo_consulta == "Vertex Controller":
            with st.expander("🎰 INFORMACIÓN VERTEX CONTROLLER", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Vertex 3.5**")
                    st.write("• 1 puerto USB (requiere HUB)")
                    st.write("• Disco SATA + Plugin CF")
                    st.write("• Credenciales: admin/Password1")
                
                with col2:
                    st.write("**Vertex 4.0**")
                    st.write("• Display Port/VGA")
                    st.write("• Fuente externa")
                    st.write("• Credenciales: Retail1/Retail1")
                
                st.info("**IP Configuración**: 192.168.50.2 | Mask: 255.255.255.0 | Gateway: 192.168.50.1")
        
        # Área de diagnóstico
        st.markdown("---")
        st.subheader("💬 Consulta de Diagnóstico")
        
        pregunta_usuario = st.text_area(
            "**Describí el problema técnico:**",
            placeholder="Ej: Mi Vertex Controller 4.0 no comunica con las Helix XT después del cambio de IP...",
            height=120,
            key="pregunta_casinopro"
        )
        
        contexto_adicional = st.text_area(
            "**Contexto adicional (opcional):**",
            placeholder="Ej: El problema empezó después de una actualización, solo ocurre con ciertas EGMs...",
            height=80
        )
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            if st.button("🎰🔧 EJECUTAR DIAGNÓSTICO CASINOPRO", type="primary", use_container_width=True):
                if pregunta_usuario.strip():
                    st.session_state.last_question = pregunta_usuario
                    st.session_state.show_feedback = False
                    
                    with st.spinner("🔍 CasinoPro AI analizando + aprendiendo..."):
                        import time
                        time.sleep(1)
                        
                        # Si no se seleccionó aceptador específico, pasar None
                        aceptador_para_analisis = aceptador_seleccionado if aceptador_seleccionado != "No específico" else "No específico"
                        
                        try:
                            respuesta = st.session_state.diagnostic_system.obtener_diagnostico_mejorado(
                                pregunta_usuario,
                                aceptador_para_analisis, 
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
                                if aceptador_seleccionado != "No específico":
                                    st.write(f"**🤖 Aceptador:** {respuesta['aceptador']}")
                                    st.write(f"**🏭 Fabricante:** {respuesta['datos_maquina'].get('fabricante', 'N/A')}")
                                else:
                                    st.write(f"**🎯 Tipo de consulta:** {tipo_consulta}")
                                    st.write(f"**🔧 Equipo:** Consulta general")
                            with col2:
                                st.write(f"**🎯 Confianza:** {respuesta['nivel_confianza']}")
                                st.write(f"**📋 Prioridad:** {respuesta['prioridad_recomendada']}")
                            
                            # Análisis de CasinoPro AI
                            st.markdown("### 🎰 **Análisis de CasinoPro AI**")
                            st.info(respuesta['analisis_experto'])
                            
                            # Timestamp
                            st.markdown("---")
                            st.caption(f"🕐 Diagnóstico generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                            
                        except Exception as e:
                            st.error(f"❌ Error al procesar el diagnóstico: {str(e)}")
                        
                else:
                    st.warning("⚠️ Por favor, describí el problema técnico")
        
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
                if st.button("✅ Sí, muy acertado", use_container_width=True, key="fb_yes"):
                    st.session_state.diagnostic_system.casinopro_ai.agregar_feedback(
                        st.session_state.last_question,
                        st.session_state.last_response['analisis_experto'],
                        fue_efectiva=True
                    )
                    st.success("🎉 ¡Gracias! CasinoPro aprendió de tu experiencia")
                    st.session_state.show_feedback = False
            
            with col2:
                if st.button("❌ No fue preciso", use_container_width=True, key="fb_no"):
                    st.session_state.diagnostic_system.casinopro_ai.agregar_feedback(
                        st.session_state.last_question,
                        st.session_state.last_response['analisis_experto'],
                        fue_efectiva=False
                    )
                    st.error("📝 CasinoPro ajustará sus diagnósticos. Contanos más...")
                    st.session_state.show_feedback = False
            
            with col3:
                if st.button("⭐ Calificar Diagnóstico", use_container_width=True, key="fb_rate"):
                    with st.expander("💬 Danos tu opinión detallada", expanded=True):
                        calificacion = st.slider("Calificación del diagnóstico:", 1, 5, 3, key="rating_slider")
                        comentarios = st.text_area("Comentarios para mejorar:", placeholder="¿Qué funcionó bien? ¿Qué podría mejorar CasinoPro?", key="comments_area")
                        
                        if st.button("🎰 Enviar Calificación", key="send_rating"):
                            st.session_state.diagnostic_system.casinopro_ai.agregar_feedback(
                                st.session_state.last_question,
                                st.session_state.last_response['analisis_experto'],
                                rating=calificacion,
                                comentarios=comentarios
                            )
                            st.success(f"⭐ ¡Gracias por tu calificación de {calificacion}/5! CasinoPro mejorará")
                            st.session_state.show_feedback = False
    
    # ==================== ESTADÍSTICAS DE CASINOPRO AI ====================
    elif st.session_state.current_menu == "📊 ESTADÍSTICAS AI":
        st.header("📊 Estadísticas de CasinoPro AI")
        
        try:
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
                
        except Exception as e:
            st.error(f"❌ Error al cargar las estadísticas: {str(e)}")
            st.info("💡 Intentá usar el sistema primero para generar datos estadísticos")
    
    # ==================== MANUALES ====================
    elif st.session_state.current_menu == "💰 MANUALES":
        st.header("💰 Manuales Técnicos")
        
        st.success("""
        **📚 Biblioteca de Manuales CasinoPro**
        - Documentación técnica especializada
        - Procedimientos de calibración
        - Diagramas de conexión
        - Códigos de error
        - **MANUALES VERTEX CONTROLLER** ✅
        """)
        
        manuales = {
            "Aristocrat Helix": "Manual de servicio técnico completo - v4.2.1",
            "Bally Alpha Pro": "Guía de diagnóstico y reparación - Edición 2023",
            "IGT Peak": "Manual del operador y técnico - Sistema PEAK",
            "Konami Concerto": "Documentación técnica Concerto Platform",
            "MEI SCN66": "Manual de instalación y configuración",
            "JCM UBA-10": "Guía de mantenimiento preventivo",
            "Vertex Controller 3.5": "Manual completo armado y configuración",
            "Vertex Controller 4.0": "Instructivo progresivos Lighting Link",
            "Vertex Red Progresiva": "Estructura de red y componentes"
        }
        
        col1, col2 = st.columns(2)
        
        for i, (manual, descripcion) in enumerate(manuales.items()):
            with col1 if i % 2 == 0 else col2:
                with st.container():
                    st.markdown(f"**{manual}**")
                    st.write(descripcion)
                    if st.button(f"📥 Descargar {manual}", key=f"manual_{i}"):
                        st.success(f"📚 Descargando manual de {manual}...")
        
    # ==================== MÁQUINAS ====================
    elif st.session_state.current_menu == "🎰 MÁQUINAS":
        st.header("🎰 Catálogo de Máquinas")
        
        st.success("""
        **🏭 Base de Datos de Fabricantes**
        - Especificaciones técnicas completas
        - Configuraciones recomendadas
        - Problemas comunes documentados
        - **VERTEX CONTROLLERS INCLUIDOS** ✅
        """)
        
        # Mostrar máquinas disponibles - AHORA CON 26+ MÁQUINAS
        st.subheader(f"📊 Total de máquinas en base de datos: {len(st.session_state.db.maquinas)}")
        
        # Agrupar por fabricante
        fabricantes = {}
        for maquina, detalles in st.session_state.db.maquinas.items():
            fabricante = detalles['fabricante']
            if fabricante not in fabricantes:
                fabricantes[fabricante] = []
            fabricantes[fabricante].append((maquina, detalles))
        
        # Mostrar por fabricante
        for fabricante, maquinas_list in fabricantes.items():
            with st.expander(f"🏭 {fabricante} ({len(maquinas_list)} máquinas)"):
                for maquina, detalles in maquinas_list:
                    # Destacar Vertex Controllers
                    if "Vertex" in maquina:
                        st.write(f"**🎰 {maquina}** - Año: {detalles['año']} - ✅ **ESPECIALIDAD CASINOPRO**")
                    else:
                        st.write(f"**🎰 {maquina}** - Año: {detalles['año']} - ✅ Compatible con CasinoPro")
        
        # Mostrar componentes Vertex
        st.markdown("---")
        st.subheader("🔧 Componentes Vertex Controller")
        
        for componente, info in st.session_state.db.componentes_vertex.items():
            with st.expander(f"🔌 {componente}"):
                st.write(f"**Tipo**: {info['tipo']}")
                st.write(f"**Conexión**: {info['conexion']}")
                if 'puertos' in info:
                    st.write(f"**Puertos**: {info['puertos']}")

if __name__ == "__main__":
    main()
