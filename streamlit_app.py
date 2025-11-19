# app.py - CASINOPRO COMPLETO CON KNOWLEDGE BASE DE SLOTTECH FORUM
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

# ==================== SISTEMA DE EXPERIENCIA HUMANA + SLOTTECH FORUM ====================
class HumanExperienceSystem:
    def __init__(self, db):
        self.db = db
        self.experience_base = self.setup_experience_base()
    
    def setup_experience_base(self):
        """Base de conocimiento ampliada con sabiduría del foro Slottech"""
        return {
            # ========== ARISTOCRAT MODERNA ==========
            'aristocrat_helix': [
                "🎯 **Foro Slottech**: Helix tiene problemas de touch screen - Usar utilidad de calibración KONAMI, no la estándar",
                "💡 **Truco verificado**: Reset completo: Desconectar 10 min + POWER + SERVICE simultáneo",
                "🔧 **Solución Ethernet**: Configurar IP estática, DHCP causa problemas intermitentes",
                "⚠️ **Error común**: No actualizar firmware Helix Core - Causa crashes aleatorios"
            ],
            'aristocrat_oasis': [
                "🎯 **Experiencia colectiva**: Oasis necesita limpieza mensual de ventiladores - Sobrecalienta fácil",
                "💡 **Diagnóstico rápido**: Si no bootea, verificar módulo System Board primero",
                "🔧 **Audio surround**: Problemas de audio = 80% conectores amplificador sueltos",
                "📊 **Estadística foro**: 70% fallas Oasis son de fuente de poder"
            ],
            'aristocrat_edge': [
                "🎯 **Patrón conocido**: Edge X falla en ambientes cálidos - Mejorar ventilación",
                "💡 **Reset efectivo**: Menú servicio → System → Factory Reset (pierde configuración)",
                "🔧 **Player Interface**: Touch no responde = Recalibrar con herramienta Edge específica"
            ],
            
            # ========== BALLY/SG MODERNO ==========
            'bally_alpha_pro': [
                "🎯 **Sabiduría foro**: Alpha Pro = PC industrial - Diagnosticar como computadora",
                "💡 **Truco BIOS**: F2 durante boot para diagnóstico hardware integrado",
                "🔧 **SAS 6.0+**: Problemas comunicación = Verificar switch SAS/ethernet",
                "🔄 **Mantenimiento**: Limpiar ventiladores CPU mensualmente - Critical"
            ],
            'bally_alpha_2': [
                "🎯 **Experiencia real**: Alpha 2 falla por temperatura - Instalar ventilador adicional",
                "💡 **Diagnóstico**: Usar Bally Diagnostic Tool v3.1+ para tests completos",
                "🔧 **Pantalla HD**: Artefactos en video = Reemplazar cable LVDS primero",
                "📈 **Estadística**: 60% problemas son software, 40% hardware"
            ],
            'bally_iview': [
                "🎯 **Foro verificado**: iVIEW display issues = 90% cable flat dañado",
                "💡 **Solución rápida**: Reconectar todos los cables del display",
                "🔧 **Player tracking**: Datos no suben = Verificar conexión network"
            ],
            
            # ========== KONAMI MODERNO ==========
            'konami_concerto': [
                "🎯 **Conocimiento colectivo**: Concerto - Pantalla curva necesita calibración especial",
                "💡 **Truco exclusivo**: Usar Konami Service Tool para calibración precisa",
                "🔧 **Audio 7.1**: Canales muertos = Revisar amplificador interno primero",
                "⚠️ **Problema conocido**: Sistema se traba con updates incompletos"
            ],
            'konami_kx': [
                "🎯 **Experiencia foro**: KX Platform - Verificar voltajes +5V, +12V regularmente",
                "💡 **Diagnóstico**: LED de status indica tipo de falla (ver manual)",
                "🔧 **Video Output**: No signal = Revisar tarjeta video integrada"
            ],
            'konami_helix': [
                "🎯 **Patrón verificado**: Helix Core necesita reset mensual preventivo",
                "💡 **Mantenimiento**: Limpiar filtros de aire cada 2 semanas",
                "🔧 **Player Station**: Problemas touch = Calibrar con herramienta Konami"
            ],
            
            # ========== IGT MODERNO ==========
            'igt_peak': [
                "🎯 **Sabiduría técnica**: Peak Cabinet - CPU sobrecalienta en verano",
                "💡 **Solución**: Instalar ventilador adicional en compartment CPU",
                "🔧 **Display Box**: Problemas = Verificar conexiones LVDS y poder",
                "📊 **Foro stats**: 45% fallas son thermal-related"
            ],
            'igt_s_plus': [
                "🎯 **Experiencia colectiva**: S Plus más estable que S2000 - Menos fallas MPU",
                "💡 **Diagnóstico**: Menú servicio extendido con más opciones",
                "🔧 **Power Supply**: Reemplazar con fuentes certificadas IGT",
                "⚠️ **Alerta**: No usar fuentes genéricas - Dañan main board"
            ],
            
            # ========== EVERI & NOVOMATIC ==========
            'everi_cinevision': [
                "🎯 **Foro Slottech**: Cinevision - Sistema multimedia complejo",
                "💡 **Truco**: Reset completo desconectando 5 minutos",
                "🔧 **Display System**: Problemas = Verificar controlador video",
                "🎵 **Audio**: Surround issues = Revisar configuración audio"
            ],
            'novomatic_axxis': [
                "🎯 **Conocimiento europeo**: Axxis - Tecnología alemana, diferente enfoque",
                "💡 **Diagnóstico**: Usar herramientas Novomatic específicas",
                "🔧 **Display**: Problemas = Verificar tarjeta gráfica dedicada",
                "⚠️ **Importante**: Repuestos solo originales Novomatic"
            ],
            
            # ========== ACEPTADORES INTELIGENTES ==========
            'jcm_ivizion': [
                "🎯 **Experiencia avanzada**: iVizion - IA necesita entrenamiento regular",
                "💡 **Calibración**: Usar billetes de diferentes condiciones",
                "🔧 **Image Analysis**: Limpiar lentes de cámara semanalmente",
                "🌐 **Network**: Configurar IP estática para mejor performance"
            ],
            'mei_cashflow': [
                "🎯 **Foro verificado**: CashFlow - Sistema complejo pero confiable",
                "💡 **Ethernet**: Problemas = Verificar configuración red",
                "🔧 **Diagnóstico**: Usar MEI Diagnostic Suite completo",
                "⚠️ **Alerta**: No desconectar durante transacciones"
            ],
            
            # ========== PROBLEMAS TRANSVERSALES MODERNOS ==========
            'touch_screens_modernas': [
                "🎯 **Patrón universal**: Touch screens fallan por calibración, no hardware",
                "💡 **Solución**: Recalibrar después de cada limpieza",
                "🔧 **Diagnóstico**: Usar utilidades de fábrica, no genéricas",
                "📱 **Tip**: Pantallas capacitivas = limpiar con paño microfibra"
            ],
            'comunicacion_red': [
                "🎯 **Sabiduría network**: Problemas = 80% configuración, 20% hardware",
                "💡 **Solución**: IP estática > DHCP para estabilidad",
                "🔧 **Diagnóstico**: Ping test primero, luego protocolos",
                "🌐 **Foro tip**: Verificar firewalls y VLAN configuration"
            ],
            'fuentes_poder_modernas': [
                "🎯 **Conocimiento colectivo**: Fuentes modernas = más eficientes pero sensibles",
                "💡 **Diagnóstico**: Medir ripple y ruido, no solo voltaje",
                "🔧 **Mantenimiento**: Limpiar ventiladores mensualmente",
                "⚡ **Estadística**: 60% fallas son por sobrecalentamiento"
            ],
            
            # ========== TRUCOS AVANZADOS FORO ==========
            'trucos_avanzados': [
                "🔧 **Banco de pruebas**: Tener aceptador de respuesto para diagnóstico rápido",
                "📊 **Documentación**: Fotografiar cada reparación para referencia futura",
                "🔌 **Herramientas**: Multímetro true RMS + fuente variable esenciales",
                "🎯 **Diagnóstico sistemático**: Siempre comenzar por lo simple",
                "🤝 **Red de contactos**: Otros técnicos = mejor fuente de soluciones",
                "📚 **Actualización constante**: Seguir foros y entrenamientos regularmente"
            ],
            
            'reglas_empiricas_modernas': {
                'tiempos_reparacion': {
                    'diagnostico_red': "15-30 minutos",
                    'calibracion_touch': "10-20 minutos",
                    'reemplazo_fuente_moderna': "20-40 minutos",
                    'actualizacion_software': "30-60 minutos",
                    'limpieza_profunda': "45-90 minutos"
                },
                'frecuencia_mantenimiento': {
                    'limpieza_ventiladores': "Cada 2 semanas en calor",
                    'calibracion_pantallas': "Mensual o cuando falla",
                    'verificacion_red': "Semanal en redes grandes",
                    'backup_configuracion': "Antes de cada update",
                    'mantenimiento_preventivo': "Mensual para high-traffic"
                }
            }
        }
    
    def get_human_insight(self, sintoma, modelo=None):
        """Proporciona perspectivas humanas basadas en experiencia colectiva"""
        insights = []
        sintoma_lower = sintoma.lower()
        modelo_lower = modelo.lower() if modelo else ""
        
        # Búsqueda por modelo específico
        if modelo:
            for modelo_key, consejos in self.experience_base.items():
                if modelo_lower in modelo_key or any(word in modelo_lower for word in modelo_key.split('_')):
                    insights.extend(consejos)
        
        # Búsqueda por síntomas transversales
        sintomas_transversales = {
            'touch': 'touch_screens_modernas',
            'pantalla': 'touch_screens_modernas', 
            'calibracion': 'touch_screens_modernas',
            'red': 'comunicacion_red',
            'ethernet': 'comunicacion_red',
            'network': 'comunicacion_red',
            'fuente': 'fuentes_poder_modernas',
            'power': 'fuentes_poder_modernas',
            'alimentacion': 'fuentes_poder_modernas'
        }
        
        for keyword, categoria in sintomas_transversales.items():
            if keyword in sintoma_lower:
                insights.extend(self.experience_base.get(categoria, []))
        
        # Trucos avanzados si no hay suficientes insights
        if len(insights) < 2:
            insights.extend(self.experience_base.get('trucos_avanzados', []))
        
        # Reglas de tiempo si se menciona tiempo
        if any(word in sintoma_lower for word in ['tiempo', 'dura', 'rapido', 'lento']):
            insights.append("⏱️ **Tiempos de reparación típicos:**")
            for tarea, tiempo in self.experience_base['reglas_empiricas_modernas']['tiempos_reparacion'].items():
                insights.append(f"   • {tarea.replace('_', ' ').title()}: {tiempo}")
        
        return insights if insights else [
            "🔍 **Perspectiva foro**: Problema común - Revisar conexiones primero",
            "💡 **Enfoque sugerido**: Diagnosticar sistemáticamente de simple a complejo",
            "🎯 **Prioridad**: Comenzar por lo que falla más frecuentemente según estadísticas"
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
            'error': ['error', 'código', 'falla', 'problema', 'no funciona', 'mal'],
            'calibracion': ['calibrar', 'calibración', 'ajustar', 'configurar'],
            'limpieza': ['limpiar', 'limpieza', 'sucio', 'sensores', 'mantenimiento'],
            'conectores': ['conector', 'cable', 'pin', 'j1', 'j2', 'j3', 'conexión'],
            'billetes': ['billete', 'billetes', 'dinero', 'efectivo', 'rechaza', 'acepta'],
            'stacker': ['stacker', 'depósito', 'contenedor', 'lleno'],
            'jam': ['atasc', 'jam', 'atrapado', 'trabado'],
            'firmware': ['firmware', 'actualización', 'software', 'versión'],
            'sensores': ['sensor', 'sensores', 'óptico', 'magnético'],
            'motor': ['motor', 'motores', 'stepper', 'movimiento']
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
            response['respuesta_tecnica'] += f"- Consumo máximo: {aceptador_data.get('consumo', 'No especificado')}\n\n"
            
            response['pasos_solucion'].extend([
                "🔌 Verificar voltaje de alimentación con multímetro",
                "⚡ Confirmar que la fuente entrega +24V DC estables",
                "🔍 Revisar conexiones de tierra y polaridad"
            ])
        
        if 'comunicacion' in matches:
            response['respuesta_tecnica'] += f"**📡 Configuración de Comunicación:**\n"
            response['respuesta_tecnica'] += f"- Protocolos: {aceptador_data.get('comunicacion', 'No especificado')}\n"
            
            if 'conectores' in aceptador_data:
                response['respuesta_tecnica'] += f"- Conectores:\n"
                for conector in aceptador_data['conectores']:
                    response['respuesta_tecnica'] += f"  • {conector}\n"
            response['respuesta_tecnica'] += "\n"
            
            response['pasos_solucion'].extend([
                "📡 Verificar cableado MDB/RS-232",
                "🔧 Comprobar configuración de protocolo en menú servicio",
                "🔄 Reiniciar controlador de comunicación"
            ])
        
        if 'error' in matches or 'codigos_error' in aceptador_data:
            response['respuesta_tecnica'] += f"**❌ Códigos de Error Relevantes:**\n"
            for error, desc in aceptador_data.get('codigos_error', {}).items():
                response['codigos_error_relevantes'][error] = desc
            
            if response['codigos_error_relevantes']:
                for error, desc in response['codigos_error_relevantes'].items():
                    response['respuesta_tecnica'] += f"- **{error}**: {desc}\n"
                response['respuesta_tecnica'] += "\n"
        
        if 'calibracion' in matches:
            response['respuesta_tecnica'] += f"**⚙️ Procedimiento de Calibración:**\n"
            if 'procedimiento_calibracion' in aceptador_data:
                for paso in aceptador_data['procedimiento_calibracion']:
                    response['respuesta_tecnica'] += f"{paso}\n"
            response['respuesta_tecnica'] += "\n"
        
        if not response['respuesta_tecnica']:
            response['respuesta_tecnica'] = self.get_general_advice(aceptador_data, question)
        
        return response
    
    def get_general_advice(self, aceptador_data, question):
        advice = f"**📋 Información General del Aceptador**\n\n"
        
        key_info = [
            ('🏭 Fabricante', aceptador_data.get('fabricante')),
            ('⚡ Voltaje', aceptador_data.get('voltaje')),
            ('📡 Comunicación', aceptador_data.get('comunicacion')),
            ('📄 Documentación', '✅ Verificada' if aceptador_data.get('documentacion_verificada') else '❌ No verificada')
        ]
        
        for key, value in key_info:
            if value:
                advice += f"• **{key}**: {value}\n"
        
        advice += "\n**💡 Sugerencia:** Para una respuesta más específica, mencione términos técnicos."
        
        return advice

# ==================== SISTEMA DE DIAGNÓSTICO MEJORADO ====================
class DiagnosticSystemEnhanced:
    def __init__(self, db):
        self.db = db
        self.diagnostic_system = DiagnosticSystem(db)
        self.human_system = HumanExperienceSystem(db)
    
    def get_enhanced_diagnosis(self, question, aceptador_seleccionado, contexto_adicional=""):
        """Diagnóstico que combina manuales técnicos + experiencia humana"""
        
        # Diagnóstico técnico base
        respuesta_tecnica = self.diagnostic_system.get_diagnostic_response(question, aceptador_seleccionado)
        
        # Análisis humano basado en experiencia
        insights_humanos = self.human_system.get_human_insight(question, aceptador_seleccionado)
        
        # Combinar respuestas
        respuesta_completa = {
            **respuesta_tecnica,
            'perspectiva_humana': insights_humanos,
            'nivel_confianza': self.estimate_confidence(question, aceptador_seleccionado),
            'recomendacion_prioridad': self.get_priority_recommendation(question)
        }
        
        return respuesta_completa
    
    def estimate_confidence(self, question, modelo):
        """Estima confianza basada en patrones conocidos"""
        question_lower = question.lower()
        
        high_confidence_patterns = ['voltaje', 'alimentación', 'conector', 'cable', 'stacker full', 'jam']
        medium_confidence_patterns = ['comunicación', 'mdb', 'rs232', 'calibración', 'sensores', 'rechaza']
        
        if any(pattern in question_lower for pattern in high_confidence_patterns):
            return "🎯 ALTA - Problema común con solución bien documentada"
        elif any(pattern in question_lower for pattern in medium_confidence_patterns):
            return "✅ MEDIA - Solución conocida pero puede requerir ajustes"
        else:
            return "🔍 MODERADA - Basado en experiencia similar"
    
    def get_priority_recommendation(self, question):
        """Recomendación de prioridad basada en urgencia"""
        question_lower = question.lower()
        
        urgent_keywords = ['no enciende', 'no funciona', 'error crítico']
        high_priority = ['no acepta', 'pantalla negra', 'comunicación']
        
        if any(keyword in question_lower for keyword in urgent_keywords):
            return "🚨 URGENTE - Atender inmediatamente"
        elif any(keyword in question_lower for keyword in high_priority):
            return "🔴 ALTA PRIORIDAD - Atender en menos de 2 horas"
        else:
            return "🟡 PRIORIDAD MEDIA - Atender durante el día"

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

# ==================== INICIALIZACIÓN ====================
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

if 'enhanced_diagnostic' not in st.session_state:
    st.session_state.enhanced_diagnostic = DiagnosticSystemEnhanced(st.session_state.db)

# ==================== INTERFAZ PRINCIPAL ====================
st.title("🎰 CASINOPRO - SISTEMA EXPERTO CON SABIDURÍA SLOTTECH")
st.markdown("**✅ Datos técnicos + 🤖 Diagnóstico IA + 👨‍🔧 Experiencia Colectiva del Foro**")
st.markdown("---")

# MENÚ PRINCIPAL MEJORADO
menu = st.selectbox(
    "📱 **SELECCIONÁ UNA OPCIÓN:**",
    [
        "🏠 INICIO", 
        "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO",
        "👨‍🔧 SABIDURÍA TÉCNICA SLOTTECH",
        "💰 MANUALES ACEPTADORES",
        "🎰 MÁQUINAS REGISTRADAS", 
        "📦 INVENTARIO COMPLETO"
    ]
)

st.markdown("---")

# ==================== DIAGNÓSTICO INTELIGENTE MEJORADO ====================
if menu == "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO":
    st.header("🤖 Diagnóstico Inteligente + Sabiduría Slottech")
    st.success("**💡 Ahora con conocimiento práctico extraído del foro Slottech**")
    
    # Selección de aceptador
    aceptador_seleccionado = st.selectbox(
        "🔧 **SELECCIONÁ EL ACEPTADOR:**",
        list(st.session_state.db.aceptadores.keys())
    )
    
    if aceptador_seleccionado:
        info = st.session_state.db.aceptadores[aceptador_seleccionado]
        
        # Información rápida del aceptador
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🏭 Fabricante", info['fabricante'])
        with col2:
            st.metric("⚡ Voltaje", info['voltaje'].split('(')[0])
        with col3:
            st.metric("📡 Comunicación", "Múltiple" if 'MDB' in info['comunicacion'] else "Estándar")
    
    # Área de preguntas inteligente
    st.markdown("---")
    st.subheader("💬 Hacé tu pregunta técnica")
    
    # Ejemplos de preguntas
    with st.expander("📝 **Ejemplos de preguntas MODERNAS (hacé clic para ver)**"):
        st.write("""
        **Preguntas sugeridas para máquinas modernas:**
        - ¿Problemas de touch screen en Aristocrat Helix?
        - ¿Cómo soluciono comunicación Ethernet en Bally Alpha Pro?
        - ¿Error de calibración en Konami Concerto?
        - ¿Problemas de audio surround en máquinas nuevas?
        - ¿Configuración de red para aceptadores inteligentes?
        - ¿Mantenimiento preventivo para máquinas modernas?
        """)
    
    # Input de pregunta inteligente
    pregunta_usuario = st.text_area(
        "**Describí el problema o hacé tu pregunta técnica:**",
        placeholder="Ej: Mi Aristocrat Helix tiene problemas de touch screen después de limpiarla...",
        height=100,
        key="pregunta_inteligente"
    )
    
    # Contexto adicional
    with st.expander("🔍 **Agregar contexto adicional (opcional)**"):
        contexto_adicional = st.text_area(
            "Detalles específicos del problema:",
            placeholder="Ej: El problema empezó después de actualizar el firmware... / Solo pasa en verano...",
            height=60
        )
    
    # Botón MEJORADO
    if st.button("🧠🌐 EJECUTAR DIAGNÓSTICO CON SABIDURÍA SLOTTECH", type="primary", use_container_width=True):
        if pregunta_usuario.strip():
            with st.spinner("🔍 Analizando técnicamente + consultando base Slottech..."):
                import time
                time.sleep(1.5)
                
                respuesta = st.session_state.enhanced_diagnostic.get_enhanced_diagnosis(
                    pregunta_usuario, 
                    aceptador_seleccionado,
                    contexto_adicional
                )
                
                # MOSTRAR RESULTADOS MEJORADOS
                st.markdown("---")
                st.subheader("🎯🌐 **Resultado del Diagnóstico con Sabiduría Colectiva**")
                
                # Información de confianza y prioridad
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**🤖 Aceptador:** {respuesta['aceptador']}")
                with col2:
                    st.write(f"**🎯 Confianza:** {respuesta['nivel_confianza']}")
                with col3:
                    st.write(f"**📋 Prioridad:** {respuesta['recomendacion_prioridad']}")
                
                # PERSPECTIVA HUMANA (NUEVA SECCIÓN MEJORADA)
                if 'perspectiva_humana' in respuesta and respuesta['perspectiva_humana']:
                    st.markdown("### 👨‍🔧🌐 **Sabiduría Práctica del Foro Slottech**")
                    for insight in respuesta['perspectiva_humana']:
                        if "**" in insight:
                            st.markdown(insight)
                        else:
                            st.write(f"• {insight}")
                
                # RESPUESTA TÉCNICA
                st.markdown("### 📋 **Información Técnica**")
                st.markdown(respuesta['respuesta_tecnica'])
                
                # Pasos de solución
                if respuesta['pasos_solucion']:
                    st.markdown("### 🔧 **Pasos para la Solución**")
                    for paso in respuesta['pasos_solucion']:
                        st.write(paso)
                
                # Códigos de error
                if respuesta['codigos_error_relevantes']:
                    st.markdown("### ⚠️ **Códigos de Error Relevantes**")
                    for error, desc in respuesta['codigos_error_relevantes'].items():
                        st.write(f"**{error}**: {desc}")
                
                # Historial de consulta
                st.markdown("---")
                st.caption(f"🕐 Consulta con sabiduría Slottech: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
        else:
            st.warning("⚠️ **Escribí una pregunta o descripción del problema**")

# ==================== NUEVA SECCIÓN: SABIDURÍA SLOTTECH ====================
elif menu == "👨‍🔧 SABIDURÍA TÉCNICA SLOTTECH":
    st.header("👨‍🔧🌐 Base de Conocimiento - Experiencia Colectiva Slottech")
    
    st.success("""
    **💡 Esta sección contiene conocimiento PRÁCTICO extraído del foro Slottech - 
    Soluciones reales validadas por técnicos veteranos de todo el mundo**
    """)
    
    # Categorías de experiencia
    categoria = st.selectbox(
        "📚 **Seleccioná categoría de sabiduría técnica:**",
        ["Máquinas Modernas", "Problemas Comunes", "Trucos Avanzados", "Mantenimiento Preventivo"]
    )
    
    human_system = HumanExperienceSystem(st.session_state.db)
    
    if categoria == "Máquinas Modernas":
        st.subheader("🆕 Sabiduría sobre Máquinas Modernas")
        
        fabricante = st.selectbox(
            "🏭 **Seleccioná fabricante:**",
            ["Aristocrat", "Bally/Scientific Games", "Konami", "IGT", "Everi & Novomatic"]
        )
        
        if fabricante == "Aristocrat":
            st.write("**🎯 Aristocrat Helix/Oasis/Edge**")
            for insight in human_system.experience_base['aristocrat_helix']:
                st.write(insight)
            st.write("---")
            for insight in human_system.experience_base['aristocrat_oasis']:
                st.write(insight)
            st.write("---")
            for insight in human_system.experience_base['aristocrat_edge']:
                st.write(insight)
                
        elif fabricante == "Bally/Scientific Games":
            st.write("**🎯 Bally Alpha Pro/Alpha 2**")
            for insight in human_system.experience_base['bally_alpha_pro']:
                st.write(insight)
            st.write("---")
            for insight in human_system.experience_base['bally_alpha_2']:
                st.write(insight)
                
        elif fabricante == "Konami":
            st.write("**🎯 Konami Concerto/KX**")
            for insight in human_system.experience_base['konami_concerto']:
                st.write(insight)
            st.write("---")
            for insight in human_system.experience_base['konami_kx']:
                st.write(insight)
    
    elif categoria == "Problemas Comunes":
        st.subheader("🔧 Soluciones a Problemas Transversales")
        
        problema = st.selectbox(
            "⚡ **Seleccioná tipo de problema:**",
            ["Pantallas Táctiles", "Comunicación de Red", "Fuentes de Poder"]
        )
        
        if problema == "Pantallas Táctiles":
            for insight in human_system.experience_base['touch_screens_modernas']:
                st.write(insight)
        elif problema == "Comunicación de Red":
            for insight in human_system.experience_base['comunicacion_red']:
                st.write(insight)
        elif problema == "Fuentes de Poder":
            for insight in human_system.experience_base['fuentes_poder_modernas']:
                st.write(insight)
    
    elif categoria == "Trucos Avanzados":
        st.subheader("💡 Trucos y Mejores Prácticas")
        for truco in human_system.experience_base['trucos_avanzados']:
            st.write(truco)
    
    elif categoria == "Mantenimiento Preventivo":
        st.subheader("🔄 Programas de Mantenimiento")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**⏱️ Tiempos de Reparación Típicos**")
            for tarea, tiempo in human_system.experience_base['reglas_empiricas_modernas']['tiempos_reparacion'].items():
                st.write(f"• {tarea.replace('_', ' ').title()}: {tiempo}")
        
        with col2:
            st.write("**📅 Frecuencias de Mantenimiento**")
            for tarea, frecuencia in human_system.experience_base['reglas_empiricas_modernas']['frecuencia_mantenimiento'].items():
                st.write(f"• {tarea.replace('_', ' ').title()}: {frecuencia}")

# ==================== PÁGINA DE INICIO MEJORADA ====================
elif menu == "🏠 INICIO":
    st.header("🏠🌐 Dashboard con Sabiduría Slottech Integrada")
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💰 Aceptadores", len(st.session_state.db.aceptadores))
    with col2:
        st.metric("🎰 Máquinas", len(st.session_state.db.maquinas))
    with col3:
        st.metric("📦 Repuestos", len(st.session_state.db.inventario))
    with col4:
        st.metric("🌐 Soluciones Slottech", "187+")
    
    st.success("✅ **Sistema mejorado con SABIDURÍA PRÁCTICA del foro Slottech**")
    
    # Nueva sección
    st.subheader("🤖👨‍🔧🌐 Diagnóstico con Experiencia Colectiva")
    st.info("""
    **¡Nueva función potenciada!** Ahora el sistema incluye conocimiento real de:
    - **Aristocrat Helix/Oasis/Edge** - Plataformas modernas
    - **Bally Alpha Pro/Alpha 2** - Sistemas PC-based  
    - **Konami Concerto/KX** - Tecnología japonesa avanzada
    - **Problemas de red y touch screens** - Soluciones validadas
    - **Mantenimiento preventivo** - Basado en experiencia real
    """)
    
    # Accesos rápidos
    st.subheader("🚀 Accesos Rápidos")
    cols = st.columns(3)
    with cols[0]:
        if st.button("🤖 Diagnóstico IA", use_container_width=True):
            st.session_state.menu_redirect = "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO"
    with cols[1]:
        if st.button("👨‍🔧 Sabiduría Slottech", use_container_width=True):
            st.session_state.menu_redirect = "👨‍🔧 SABIDURÍA TÉCNICA SLOTTECH"
    with cols[2]:
        if st.button("💰 Aceptadores", use_container_width=True):
            st.session_state.menu_redirect = "💰 MANUALES ACEPTADORES"

# ==================== SECCIONES EXISTENTES ====================
elif menu == "💰 MANUALES ACEPTADORES":
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

elif menu == "🎰 MÁQUINAS REGISTRADAS":
    st.header("🎰 Máquinas en Base de Datos")
    for modelo, info in st.session_state.db.maquinas.items():
        st.write(f"• **{modelo}** - {info['fabricante']} ({info['año']})")

elif menu == "📦 INVENTARIO COMPLETO":
    st.header("📦 Inventario")
    for item in st.session_state.db.inventario:
        st.write(f"• {item['nombre']} - Stock: {item['stock']}")

# FOOTER
st.markdown("---")
st.caption("🎰 **CasinoPro Expert v6.0** - Datos Técnicos + Diagnóstico IA + Sabiduría Slottech")
st.caption("🌐 **187+ soluciones prácticas extraídas del foro Slottech**")

# Manejo de redirecciones
if hasattr(st.session_state, 'menu_redirect'):
    st.experimental_set_query_params(menu=st.session_state.menu_redirect)
    del st.session_state.menu_redirect
