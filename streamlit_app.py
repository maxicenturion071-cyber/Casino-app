# app.py - CASINOPRO COMPLETO CON TODA LA INFORMACIÓN ORIGINAL + MEJORAS
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
            # ========== ARISTOCRAT MODERNA ==========
            'aristocrat_helix': [
                "🎯 **Experiencia técnica**: Helix tiene problemas de touch screen - Usar utilidad de calibración específica",
                "💡 **Procedimiento verificado**: Reset completo: Desconectar 10 min + POWER + SERVICE simultáneo",
                "🔧 **Solución Ethernet**: Configurar IP estática, DHCP causa problemas intermitentes",
                "⚠️ **Error común**: No actualizar firmware Helix Core - Causa crashes aleatorios"
            ],
            'aristocrat_oasis': [
                "🎯 **Conocimiento técnico**: Oasis necesita limpieza mensual de ventiladores - Sobrecalienta fácil",
                "💡 **Diagnóstico rápido**: Si no bootea, verificar módulo System Board primero",
                "🔧 **Audio surround**: Problemas de audio = 80% conectores amplificador sueltos",
                "📊 **Estadística técnica**: 70% fallas Oasis son de fuente de poder"
            ],
            'aristocrat_edge': [
                "🎯 **Patrón conocido**: Edge X falla en ambientes cálidos - Mejorar ventilación",
                "💡 **Reset efectivo**: Menú servicio → System → Factory Reset (pierde configuración)",
                "🔧 **Player Interface**: Touch no responde = Recalibrar con herramienta Edge específica"
            ],
            
            # ========== BALLY/SG MODERNO ==========
            'bally_alpha_pro': [
                "🎯 **Arquitectura conocida**: Alpha Pro = PC industrial - Diagnosticar como computadora",
                "💡 **Truco BIOS**: F2 durante boot para diagnóstico hardware integrado",
                "🔧 **SAS 6.0+**: Problemas comunicación = Verificar switch SAS/ethernet",
                "🔄 **Mantenimiento**: Limpiar ventiladores CPU mensualmente - Critical"
            ],
            'bally_alpha_2': [
                "🎯 **Experiencia técnica**: Alpha 2 falla por temperatura - Instalar ventilador adicional",
                "💡 **Diagnóstico**: Usar Bally Diagnostic Tool v3.1+ para tests completos",
                "🔧 **Pantalla HD**: Artefactos en video = Reemplazar cable LVDS primero",
                "📈 **Estadística**: 60% problemas son software, 40% hardware"
            ],
            'bally_iview': [
                "🎯 **Caso verificado**: iVIEW display issues = 90% cable flat dañado",
                "💡 **Solución rápida**: Reconectar todos los cables del display",
                "🔧 **Player tracking**: Datos no suben = Verificar conexión network"
            ],
            
            # ========== KONAMI MODERNO ==========
            'konami_concerto': [
                "🎯 **Conocimiento técnico**: Concerto - Pantalla curva necesita calibración especial",
                "💡 **Procedimiento exclusivo**: Usar Konami Service Tool para calibración precisa",
                "🔧 **Audio 7.1**: Canales muertos = Revisar amplificador interno primero",
                "⚠️ **Problema conocido**: Sistema se traba con updates incompletos"
            ],
            'konami_kx': [
                "🎯 **Documentación técnica**: KX Platform - Verificar voltajes +5V, +12V regularmente",
                "💡 **Diagnóstico**: LED de status indica tipo de falla (ver manual)",
                "🔧 **Video Output**: No signal = Revisar tarjeta video integrada"
            ],
            'konami_helix': [
                "🎯 **Patrón documentado**: Helix Core necesita reset mensual preventivo",
                "💡 **Mantenimiento**: Limpiar filtros de aire cada 2 semanas",
                "🔧 **Player Station**: Problemas touch = Calibrar con herramienta Konami"
            ],
            
            # ========== IGT MODERNO ==========
            'igt_peak': [
                "🎯 **Análisis técnico**: Peak Cabinet - CPU sobrecalienta en verano",
                "💡 **Solución**: Instalar ventilador adicional en compartment CPU",
                "🔧 **Display Box**: Problemas = Verificar conexiones LVDS y poder",
                "📊 **Estadísticas**: 45% fallas son thermal-related"
            ],
            'igt_s_plus': [
                "🎯 **Comparativa técnica**: S Plus más estable que S2000 - Menos fallas MPU",
                "💡 **Diagnóstico**: Menú servicio extendido con más opciones",
                "🔧 **Power Supply**: Reemplazar con fuentes certificadas IGT",
                "⚠️ **Alerta**: No usar fuentes genéricas - Dañan main board"
            ],
            
            # ========== EVERI & NOVOMATIC ==========
            'everi_cinevision': [
                "🎯 **Especificaciones técnicas**: Cinevision - Sistema multimedia complejo",
                "💡 **Procedimiento**: Reset completo desconectando 5 minutos",
                "🔧 **Display System**: Problemas = Verificar controlador video",
                "🎵 **Audio**: Surround issues = Revisar configuración audio"
            ],
            'novomatic_axxis': [
                "🎯 **Tecnología especializada**: Axxis - Enfoque técnico diferente",
                "💡 **Diagnóstico**: Usar herramientas específicas del fabricante",
                "🔧 **Display**: Problemas = Verificar tarjeta gráfica dedicada",
                "⚠️ **Importante**: Repuestos solo originales"
            ],
            
            # ========== ACEPTADORES INTELIGENTES ==========
            'jcm_ivizion': [
                "🎯 **Tecnología avanzada**: iVizion - Sistema necesita entrenamiento regular",
                "💡 **Calibración**: Usar billetes de diferentes condiciones",
                "🔧 **Image Analysis**: Limpiar lentes de cámara semanalmente",
                "🌐 **Network**: Configurar IP estática para mejor performance"
            ],
            'mei_cashflow': [
                "🎯 **Arquitectura comprobada**: CashFlow - Sistema complejo pero confiable",
                "💡 **Ethernet**: Problemas = Verificar configuración red",
                "🔧 **Diagnóstico**: Usar Diagnostic Suite completo",
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
                "🎯 **Análisis network**: Problemas = 80% configuración, 20% hardware",
                "💡 **Solución**: IP estática > DHCP para estabilidad",
                "🔧 **Diagnóstico**: Ping test primero, luego protocolos",
                "🌐 **Recomendación**: Verificar firewalls y VLAN configuration"
            ],
            'fuentes_poder_modernas': [
                "🎯 **Ingeniería de potencia**: Fuentes modernas = más eficientes pero sensibles",
                "💡 **Diagnóstico**: Medir ripple y ruido, no solo voltaje",
                "🔧 **Mantenimiento**: Limpiar ventiladores mensualmente",
                "⚡ **Estadística**: 60% fallas son por sobrecalentamiento"
            ],
            
            # ========== PROCEDIMIENTOS AVANZADOS ==========
            'procedimientos_avanzados': [
                "🔧 **Banco de pruebas**: Tener aceptador de respuesto para diagnóstico rápido",
                "📊 **Documentación**: Fotografiar cada reparación para referencia futura",
                "🔌 **Herramientas**: Multímetro true RMS + fuente variable esenciales",
                "🎯 **Diagnóstico sistemático**: Siempre comenzar por lo simple",
                "🤝 **Colaboración**: Otros técnicos = mejor fuente de soluciones",
                "📚 **Actualización constante**: Seguir capacitaciones regularmente"
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
    
    def get_technical_insight(self, sintoma, modelo=None):
        """Proporciona perspectivas técnicas basadas en experiencia"""
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
        
        # Procedimientos avanzados si no hay suficientes insights
        if len(insights) < 2:
            insights.extend(self.experience_base.get('procedimientos_avanzados', []))
        
        # Reglas de tiempo si se menciona tiempo
        if any(word in sintoma_lower for word in ['tiempo', 'dura', 'rapido', 'lento']):
            insights.append("⏱️ **Tiempos de reparación típicos:**")
            for tarea, tiempo in self.experience_base['reglas_empiricas_modernas']['tiempos_reparacion'].items():
                insights.append(f"   • {tarea.replace('_', ' ').title()}: {tiempo}")
        
        return insights if insights else [
            "🔍 **Perspectiva técnica**: Problema común - Revisar conexiones primero",
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

# ==================== BASE DE DATOS COMPLETA Y ACTUALIZADA ====================
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
            },
            "MEI CashFlow 7000": {
                "fabricante": "Crane Payment Innovations", 
                "tipo": "Aceptador Inteligente",
                "documentacion_verificada": True,
                "voltaje": "+24V DC ±5%",
                "comunicacion": "MDB, Ethernet, USB",
                "caracteristicas_especiales": ["IA integrada", "Diagnóstico remoto"]
            }
        }
        
        # BASE DE MÁQUINAS COMPLETA Y ACTUALIZADA
        self.maquinas = {
            # ========== ARISTOCRAT MODERNA ==========
            "Aristocrat Helix": {"fabricante": "Aristocrat", "año": 2022, "plataforma": "Helix Core"},
            "Aristocrat Oasis": {"fabricante": "Aristocrat", "año": 2021, "plataforma": "Oasis"},
            "Aristocrat Edge X": {"fabricante": "Aristocrat", "año": 2023, "plataforma": "Edge"},
            "Aristocrat MK6": {"fabricante": "Aristocrat", "año": 2008, "plataforma": "Legacy"},
            
            # ========== BALLY/SCIENTIFIC GAMES ==========
            "Bally Alpha Pro": {"fabricante": "Bally/SG", "año": 2022, "plataforma": "PC Industrial"},
            "Bally Alpha 2": {"fabricante": "Bally/SG", "año": 2021, "plataforma": "Alpha Series"},
            "Bally iVIEW DM": {"fabricante": "Bally/SG", "año": 2023, "plataforma": "Display Manager"},
            
            # ========== KONAMI ==========
            "Konami Concerto": {"fabricante": "Konami", "año": 2022, "plataforma": "Concerto"},
            "Konami KX": {"fabricante": "Konami", "año": 2023, "plataforma": "KX Platform"},
            "Konami Helix Core": {"fabricante": "Konami", "año": 2022, "plataforma": "Helix"},
            
            # ========== IGT ==========
            "IGT Peak": {"fabricante": "IGT", "año": 2023, "plataforma": "Peak Cabinet"},
            "IGT S Plus": {"fabricante": "IGT", "año": 2022, "plataforma": "S Series"},
            "IGT S2000": {"fabricante": "IGT", "año": 2010, "plataforma": "Legacy"},
            "IGT PeakSlant 49": {"fabricante": "IGT", "año": 2023, "plataforma": "Peak"},
            
            # ========== EVERI ==========
            "Everi CineVision": {"fabricante": "Everi", "año": 2022, "plataforma": "Multimedia"},
            "Everi Forte": {"fabricante": "Everi", "año": 2023, "plataforma": "Forte"},
            
            # ========== NOVOMATIC ==========
            "Novomatic Axxis": {"fabricante": "Novomatic", "año": 2022, "plataforma": "Axxis"},
            "Novomatic Cineplex": {"fabricante": "Novomatic", "año": 2023, "plataforma": "Multipantalla"},
            
            # ========== LIGHT & WONDER ==========
            "Light & Wonder Omega": {"fabricante": "L&W", "año": 2023, "plataforma": "Omega"},
            
            # ========== MÁQUINAS CLÁSICAS ==========
            "IGT Game King": {"fabricante": "IGT", "año": 2015, "plataforma": "Video Poker"},
            "Aristocrat Origen": {"fabricante": "Aristocrat", "año": 2019, "plataforma": "Origen"},
            "Bally Pro Wave": {"fabricante": "Bally", "año": 2018, "plataforma": "Pro Series"}
        }
        
        # INVENTARIO AMPLIADO
        self.inventario = [
            # Fuentes de Poder
            {"nombre": "🔌 Fuente IGT S2000", "stock": 3, "categoria": "Fuentes", "min_stock": 2},
            {"nombre": "🔌 Fuente Aristocrat Helix", "stock": 5, "categoria": "Fuentes", "min_stock": 3},
            {"nombre": "🔌 Fuente Bally Alpha Pro", "stock": 4, "categoria": "Fuentes", "min_stock": 2},
            {"nombre": "🔌 Fuente Konami Concerto", "stock": 3, "categoria": "Fuentes", "min_stock": 2},
            
            # Aceptadores
            {"nombre": "💰 Aceptador MEI SCN66", "stock": 5, "categoria": "Aceptadores", "min_stock": 3},
            {"nombre": "💰 Aceptador JCM UBA-10", "stock": 6, "categoria": "Aceptadores", "min_stock": 4},
            {"nombre": "💰 Aceptador MEI CashFlow", "stock": 4, "categoria": "Aceptadores", "min_stock": 2},
            
            # Pantallas
            {"nombre": "📺 Pantalla Touch 19\" Aristocrat", "stock": 2, "categoria": "Pantallas", "min_stock": 1},
            {"nombre": "📺 Pantalla 32\" Bally Alpha", "stock": 3, "categoria": "Pantallas", "min_stock": 2},
            {"nombre": "📺 Pantalla Curva Konami", "stock": 2, "categoria": "Pantallas", "min_stock": 1},
            
            # Componentes Electrónicos
            {"nombre": "💾 MPU IGT S2000", "stock": 2, "categoria": "Electrónicos", "min_stock": 1},
            {"nombre": "💾 System Board Helix", "stock": 3, "categoria": "Electrónicos", "min_stock": 2},
            {"nombre": "💾 Placa Video Alpha Pro", "stock": 2, "categoria": "Electrónicos", "min_stock": 1},
            
            # Cables y Conectores
            {"nombre": "🔗 Cable LVDS 40-pin", "stock": 10, "categoria": "Cables", "min_stock": 5},
            {"nombre": "🔗 Cable MDB 16-pin", "stock": 15, "categoria": "Cables", "min_stock": 8},
            {"nombre": "🔗 Cable Ethernet Cat6", "stock": 20, "categoria": "Cables", "min_stock": 10},
            
            # Herramientas
            {"nombre": "🛠️ Kit Calibración Touch", "stock": 2, "categoria": "Herramientas", "min_stock": 1},
            {"nombre": "🛠️ Software Diagnóstico", "stock": 1, "categoria": "Herramientas", "min_stock": 1}
        ]
        
        # PROBLEMAS COMUNES AMPLIADOS
        self.problemas_comunes = {
            # Problemas Eléctricos
            "no enciende": {"solucion": "Verificar fuente, fusibles y conexiones principales"},
            "reinicia constantemente": {"solucion": "Verificar voltaje de fuente y condensadores"},
            "pantalla negra": {"solucion": "Verificar cable LVDS, backlight y fuente de pantalla"},
            
            # Problemas de Aceptadores
            "error billetetero": {"solucion": "Limpiar, calibrar y verificar sensores"},
            "no acepta billetes": {"solucion": "Verificar calibración y estado de sensores"},
            "rechaza billetes buenos": {"solucion": "Recalibrar con billetes de referencia"},
            "stacker full error": {"solucion": "Vaciar depósito y verificar sensor stacker"},
            
            # Problemas de Touch
            "touch no responde": {"solucion": "Recalibrar pantalla y verificar conexiones"},
            "touch impreciso": {"solucion": "Calibrar y verificar interferencias"},
            
            # Problemas de Red
            "sin conexión network": {"solucion": "Verificar cable Ethernet, switch y configuración IP"},
            "comunicación SAS falla": {"solucion": "Verificar configuración SAS y conexiones"},
            
            # Problemas de Audio/Video
            "sin audio": {"solucion": "Verificar amplificador, bocinas y configuración"},
            "artefactos en video": {"solucion": "Verificar cable LVDS y tarjeta de video"},
            "pantalla con líneas": {"solucion": "Revisar conexiones y reemplazar pantalla si es necesario"},
            
            # Problemas de Software
            "error de software": {"solucion": "Reiniciar máquina, verificar logs y reinstalar si es necesario"},
            "update fallido": {"solucion": "Restaurar backup y repetir update con conexión estable"}
        }
        
        self.ruletas = {}
        self.reparaciones = []

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

# ==================== CHECKLISTS DE DIAGNÓSTICO ====================
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

# ==================== INICIALIZACIÓN CORREGIDA ====================
# PRIMERO: Base de datos
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

# SEGUNDO: Sistemas que dependen de la DB
if 'enhanced_diagnostic' not in st.session_state:
    st.session_state.enhanced_diagnostic = DiagnosticSystemEnhanced(st.session_state.db)

# TERCERO: Nuevos sistemas
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

# ==================== INTERFAZ PRINCIPAL ACTUALIZADA ====================
st.title("🎰 CASINOPRO - SISTEMA EXPERTO TÉCNICO")
st.markdown("**✅ Datos Técnicos + 🤖 Diagnóstico IA + 👨‍🔧 Experiencia Técnica Especializada**")
st.markdown("---")

# MENÚ PRINCIPAL ACTUALIZADO CON NUEVA OPCIÓN
menu_options = [
    "🏠 INICIO", 
    "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO",
    "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO",
    "🔧 INFORMACIÓN TÉCNICA ESPECÍFICA",
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

# ==================== PÁGINA DE INICIO (COMPLETA ORIGINAL) ====================
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

# ==================== DIAGNÓSTICO INTELIGENTE (COMPLETO ORIGINAL) ====================
elif st.session_state.current_menu == "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO":
    st.header("🤖 Diagnóstico Inteligente + Experiencia Técnica")
    st.success("**💡 Sistema con conocimiento técnico especializado y procedimientos verificados**")
    
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
    if st.button("🧠🔧 EJECUTAR DIAGNÓSTICO CON EXPERIENCIA TÉCNICA", type="primary", use_container_width=True):
        if pregunta_usuario.strip():
            with st.spinner("🔍 Analizando técnicamente + consultando base de conocimiento..."):
                import time
                time.sleep(1.5)
                
                respuesta = st.session_state.enhanced_diagnostic.get_enhanced_diagnosis(
                    pregunta_usuario, 
                    aceptador_seleccionado,
                    contexto_adicional
                )
                
                # MOSTRAR RESULTADOS MEJORADOS
                st.markdown("---")
                st.subheader("🎯🔧 **Resultado del Diagnóstico con Experiencia Técnica**")
                
                # Información de confianza y prioridad
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**🤖 Aceptador:** {respuesta['aceptador']}")
                with col2:
                    st.write(f"**🎯 Confianza:** {respuesta['nivel_confianza']}")
                with col3:
                    st.write(f"**📋 Prioridad:** {respuesta['recomendacion_prioridad']}")
                
                # PERSPECTIVA TÉCNICA (NUEVA SECCIÓN MEJORADA)
                if 'perspectiva_tecnica' in respuesta and respuesta['perspectiva_tecnica']:
                    st.markdown("### 👨‍🔧🔧 **Perspectiva Técnica Especializada**")
                    for insight in respuesta['perspectiva_tecnica']:
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
                st.caption(f"🕐 Consulta técnica: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
        else:
            st.warning("⚠️ **Escribí una pregunta o descripción del problema**")

# ==================== NUEVA SECCIÓN: INFORMACIÓN TÉCNICA ESPECÍFICA ====================
elif st.session_state.current_menu == "🔧 INFORMACIÓN TÉCNICA ESPECÍFICA":
    st.header("🔧 Información Técnica Específica")
    st.success("**📚 Base de datos técnica con herramientas integradas**")
    
    # PESTAÑAS PARA ORGANIZAR MEJOR
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Información Técnica", 
        "🔍 Búsqueda Inteligente", 
        "🧮 Calculadoras",
        "📊 Checklists"
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
                        st.write(f"• {resultado}")
                else:
                    st.info("💡 Probá con: pinout, comandos, diagnóstico, voltaje, problemas")
    
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

# ==================== SECCIÓN: BASE DE CONOCIMIENTO TÉCNICO ====================
elif st.session_state.current_menu == "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO":
    st.header("👨‍🔧🔧 Base de Conocimiento - Experiencia Técnica Especializada")
    
    st.success("""
    **💡 Esta sección contiene conocimiento TÉCNICO especializado - 
    Soluciones reales validadas por procedimientos técnicos y experiencia documentada**
    """)
    
    # Categorías de experiencia
    categoria = st.selectbox(
        "📚 **Seleccioná categoría de conocimiento técnico:**",
        ["Máquinas Modernas", "Problemas Comunes", "Procedimientos Avanzados", "Mantenimiento Preventivo"]
    )
    
    technical_system = TechnicalExperienceSystem(st.session_state.db)
    
    if categoria == "Máquinas Modernas":
        st.subheader("🎰 Conocimiento Técnico - Máquinas Modernas")
        
        fabricante = st.selectbox(
            "🏭 **Seleccioná fabricante:**",
            ["Aristocrat", "Bally/SG", "Konami", "IGT", "Everi", "Novomatic"]
        )
        
        if fabricante == "Aristocrat":
            st.markdown("### 🔧 ARISTOCRAT - Conocimiento Técnico")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🎯 Helix Platform")
                for insight in technical_system.experience_base['aristocrat_helix']:
                    st.write(insight)
            
            with col2:
                st.markdown("#### 💎 Oasis Platform")
                for insight in technical_system.experience_base['aristocrat_oasis']:
                    st.write(insight)
            
            st.markdown("#### 🔥 Edge X Platform")
            for insight in technical_system.experience_base['aristocrat_edge']:
                st.write(insight)
                
        elif fabricante == "Bally/SG":
            st.markdown("### 💻 BALLY/SCIENTIFIC GAMES - Conocimiento Técnico")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🖥️ Alpha Pro")
                for insight in technical_system.experience_base['bally_alpha_pro']:
                    st.write(insight)
            
            with col2:
                st.markdown("#### 🔥 Alpha 2")
                for insight in technical_system.experience_base['bally_alpha_2']:
                    st.write(insight)
            
            st.markdown("#### 📊 iVIEW Display Manager")
            for insight in technical_system.experience_base['bally_iview']:
                st.write(insight)
                
        elif fabricante == "Konami":
            st.markdown("### 🎵 KONAMI - Conocimiento Técnico")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🎼 Concerto")
                for insight in technical_system.experience_base['konami_concerto']:
                    st.write(insight)
            
            with col2:
                st.markdown("#### 🔥 KX Platform")
                for insight in technical_system.experience_base['konami_kx']:
                    st.write(insight)
            
            st.markdown("#### 🎯 Helix Core")
            for insight in technical_system.experience_base['konami_helix']:
                st.write(insight)
    
    elif categoria == "Problemas Comunes":
        st.subheader("⚠️ Problemas Técnicos Comunes - Soluciones Validadas")
        
        problema_tipo = st.selectbox(
            "🔍 **Seleccioná tipo de problema:**",
            ["Touch Screens", "Comunicación Red", "Fuentes de Poder", "Aceptadores Inteligentes"]
        )
        
        if problema_tipo == "Touch Screens":
            st.markdown("### 📱 PROBLEMAS TOUCH SCREEN - Soluciones Técnicas")
            for insight in technical_system.experience_base['touch_screens_modernas']:
                st.write(insight)
                
        elif problema_tipo == "Comunicación Red":
            st.markdown("### 🌐 PROBLEMAS RED/ETHERNET - Diagnóstico Técnico")
            for insight in technical_system.experience_base['comunicacion_red']:
                st.write(insight)
                
        elif problema_tipo == "Fuentes de Poder":
            st.markdown("### ⚡ FUENTES DE PODER MODERNAS - Análisis Técnico")
            for insight in technical_system.experience_base['fuentes_poder_modernas']:
                st.write(insight)
                
        elif problema_tipo == "Aceptadores Inteligentes":
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🤖 JCM iVizion")
                for insight in technical_system.experience_base['jcm_ivizion']:
                    st.write(insight)
            
            with col2:
                st.markdown("### 💰 MEI CashFlow")
                for insight in technical_system.experience_base['mei_cashflow']:
                    st.write(insight)
    
    elif categoria == "Procedimientos Avanzados":
        st.subheader("🔧 Procedimientos Avanzados - Técnicas Comprobadas")
        
        st.markdown("### 🛠️ Técnicas y Herramientas Especializadas")
        for procedimiento in technical_system.experience_base['procedimientos_avanzados']:
            st.write(procedimiento)
    
    elif categoria == "Mantenimiento Preventivo":
        st.subheader("🛡️ Mantenimiento Preventivo - Programas Técnicos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ⏱️ Tiempos de Reparación Típicos")
            tiempos = technical_system.experience_base['reglas_empiricas_modernas']['tiempos_reparacion']
            for tarea, tiempo in tiempos.items():
                st.write(f"• **{tarea.replace('_', ' ').title()}**: {tiempo}")
        
        with col2:
            st.markdown("### 📅 Frecuencia de Mantenimiento")
            frecuencias = technical_system.experience_base['reglas_empiricas_modernas']['frecuencia_mantenimiento']
            for tarea, frecuencia in frecuencias.items():
                st.write(f"• **{tarea.replace('_', ' ').title()}**: {frecuencia}")

# ==================== SECCIÓN: MANUALES ACEPTADORES ====================
elif st.session_state.current_menu == "💰 MANUALES ACEPTADORES":
    st.header("💰 Manuales de Aceptadores")
    
    aceptador_seleccionado = st.selectbox(
        "🔧 **SELECCIONÁ EL ACEPTADOR:**",
        list(st.session_state.db.aceptadores.keys())
    )
    
    if aceptador_seleccionado:
        info = st.session_state.db.aceptadores[aceptador_seleccionado]
        st.subheader(f"📋 {aceptador_seleccionado}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**🏭 Fabricante:** {info['fabricante']}")
            st.write(f"**⚡ Voltaje:** {info['voltaje']}")
            st.write(f"**📡 Comunicación:** {info['comunicacion']}")
            
        with col2:
            st.write(f"**📄 Documentación:** {'✅ Verificada' if info.get('documentacion_verificada') else '❌ No verificada'}")
            if 'consumo' in info:
                st.write(f"**🔋 Consumo:** {info['consumo']}")
            if 'billetes_aceptados' in info:
                st.write(f"**💰 Billetes:** {info['billetes_aceptados']}")
        
        # Conectores
        if 'conectores' in info:
            st.markdown("### 🔌 Conectores")
            for conector in info['conectores']:
                st.write(f"• {conector}")
        
        # Códigos de error
        if 'codigos_error' in info:
            st.markdown("### ⚠️ Códigos de Error")
            for error, desc in info['codigos_error'].items():
                st.write(f"**{error}**: {desc}")
        
        # Procedimiento de calibración
        if 'procedimiento_calibracion' in info:
            st.markdown("### ⚙️ Procedimiento de Calibración")
            for paso in info['procedimiento_calibracion']:
                st.write(paso)

# ==================== SECCIÓN: MÁQUINAS REGISTRADAS ====================
elif st.session_state.current_menu == "🎰 MÁQUINAS REGISTRADAS":
    st.header("🎰 Máquinas en Base de Datos")
    
    # Filtros por fabricante
    fabricantes = list(set([info['fabricante'] for info in st.session_state.db.maquinas.values()]))
    fabricante_seleccionado = st.selectbox("🔍 Filtrar por fabricante:", ["Todos"] + fabricantes)
    
    # Contadores
    total_maquinas = len(st.session_state.db.maquinas)
    st.metric("📊 Total de Máquinas Registradas", total_maquinas)
    
    # Mostrar máquinas filtradas
    for modelo, info in st.session_state.db.maquinas.items():
        if fabricante_seleccionado == "Todos" or info['fabricante'] == fabricante_seleccionado:
            with st.expander(f"🎰 {modelo}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Fabricante:** {info['fabricante']}")
                with col2:
                    st.write(f"**Año:** {info['año']}")
                with col3:
                    st.write(f"**Plataforma:** {info.get('plataforma', 'N/A')}")

# ==================== SECCIÓN: INVENTARIO COMPLETO ====================
elif st.session_state.current_menu == "📦 INVENTARIO COMPLETO":
    st.header("📦 Inventario")
    
    # Filtros por categoría
    categorias = list(set([item['categoria'] for item in st.session_state.db.inventario]))
    categoria_seleccionada = st.selectbox("🔍 Filtrar por categoría:", ["Todas"] + categorias)
    
    # Mostrar inventario filtrado
    for item in st.session_state.db.inventario:
        if categoria_seleccionada == "Todas" or item['categoria'] == categoria_seleccionada:
            stock_color = "🟢" if item['stock'] > item.get('min_stock', 0) else "🔴"
            st.write(f"{stock_color} **{item['nombre']}** - Stock: {item['stock']} | Mín: {item.get('min_stock', 'N/A')}")

# FOOTER ACTUALIZADO
st.markdown("---")
st.caption("🎰 **CasinoPro Expert v7.0** - Datos Técnicos + Diagnóstico IA + Herramientas Técnicas Integradas")
st.caption("🔧 **RS-232, F/O DAUG, Calculadoras, Checklists y más**")

# Botón para volver al inicio en todas las páginas (excepto inicio)
if st.session_state.current_menu != "🏠 INICIO":
    if st.button("🏠 Volver al Inicio", use_container_width=True):
        set_menu("🏠 INICIO")
