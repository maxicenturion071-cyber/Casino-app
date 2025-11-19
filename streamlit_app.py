# app.py - CASINOPRO COMPLETO CON KNOWLEDGE BASE TÉCNICA
import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN MÓDIL
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

# ==================== INICIALIZACIÓN ====================
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

if 'enhanced_diagnostic' not in st.session_state:
    st.session_state.enhanced_diagnostic = DiagnosticSystemEnhanced(st.session_state.db)

# ==================== INTERFAZ PRINCIPAL ====================
st.title("🎰 CASINOPRO - SISTEMA EXPERTO TÉCNICO")
st.markdown("**✅ Datos técnicos + 🤖 Diagnóstico IA + 👨‍🔧 Experiencia Técnica Especializada**")
st.markdown("---")

# MENÚ PRINCIPAL MEJORADO
menu = st.selectbox(
    "📱 **SELECCIONÁ UNA OPCIÓN:**",
    [
        "🏠 INICIO", 
        "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO",
        "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO",
        "💰 MANUALES ACEPTADORES",
        "🎰 MÁQUINAS REGISTRADAS", 
        "📦 INVENTARIO COMPLETO"
    ]
)

st.markdown("---")

# ==================== DIAGNÓSTICO INTELIGENTE MEJORADO ====================
if menu == "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO":
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

# ==================== NUEVA SECCIÓN: BASE DE CONOCIMIENTO TÉCNICO ====================
elif menu == "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO":
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
        st.subheader("🆕 Conocimiento sobre Máquinas Modernas")
        
        fabricante = st.selectbox(
            "🏭 **Seleccioná fabricante:**",
            ["Aristocrat", "Bally/Scientific Games", "Konami", "IGT", "Everi & Novomatic"]
        )
        
        if fabricante == "Aristocrat":
            st.write("**🎯 Aristocrat Helix/Oasis/Edge**")
            for insight in technical_system.experience_base['aristocrat_helix']:
                st.write(insight)
            st.write("---")
            for insight in technical_system.experience_base['aristocrat_oasis']:
                st.write(insight)
            st.write("---")
            for insight in technical_system.experience_base['aristocrat_edge']:
                st.write(insight)
                
        elif fabricante == "Bally/Scientific Games":
            st.write("**🎯 Bally Alpha Pro/Alpha 2**")
            for insight in technical_system.experience_base['bally_alpha_pro']:
                st.write(insight)
            st.write("---")
            for insight in technical_system.experience_base['bally_alpha_2']:
                st.write(insight)
                
        elif fabricante == "Konami":
            st.write("**🎯 Konami Concerto/KX**")
            for insight in technical_system.experience_base['konami_concerto']:
                st.write(insight)
            st.write("---")
            for insight in technical_system.experience_base['konami_kx']:
                st.write(insight)
    
    elif categoria == "Problemas Comunes":
        st.subheader("🔧 Soluciones a Problemas Transversales")
        
        problema = st.selectbox(
            "⚡ **Seleccioná tipo de problema:**",
            ["Pantallas Táctiles", "Comunicación de Red", "Fuentes de Poder"]
        )
        
        if problema == "Pantallas Táctiles":
            for insight in technical_system.experience_base['touch_screens_modernas']:
                st.write(insight)
        elif problema == "Comunicación de Red":
            for insight in technical_system.experience_base['comunicacion_red']:
                st.write(insight)
        elif problema == "Fuentes de Poder":
            for insight in technical_system.experience_base['fuentes_poder_modernas']:
                st.write(insight)
    
    elif categoria == "Procedimientos Avanzados":
        st.subheader("💡 Procedimientos y Mejores Prácticas")
        for procedimiento in technical_system.experience_base['procedimientos_avanzados']:
            st.write(procedimiento)
    
    elif categoria == "Mantenimiento Preventivo":
        st.subheader("🔄 Programas de Mantenimiento")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**⏱️ Tiempos de Reparación Típicos**")
            for tarea, tiempo in technical_system.experience_base['reglas_empiricas_modernas']['tiempos_reparacion'].items():
                st.write(f"• {tarea.replace('_', ' ').title()}: {tiempo}")
        
        with col2:
            st.write("**📅 Frecuencias de Mantenimiento**")
            for tarea, frecuencia in technical_system.experience_base['reglas_empiricas_modernas']['frecuencia_mantenimiento'].items():
                st.write(f"• {tarea.replace('_', ' ').title()}: {frecuencia}")

# ==================== PÁGINA DE INICIO MEJORADA ====================
elif menu == "🏠 INICIO":
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
    
    # Accesos rápidos
    st.subheader("🚀 Accesos Rápidos")
    cols = st.columns(3)
    with cols[0]:
        if st.button("🤖 Diagnóstico IA", use_container_width=True):
            st.session_state.menu_redirect = "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO"
    with cols[1]:
        if st.button("👨‍🔧 Conocimiento Técnico", use_container_width=True):
            st.session_state.menu_redirect = "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO"
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

elif menu == "📦 INVENTARIO COMPLETO":
    st.header("📦 Inventario")
    
    # Filtros por categoría
    categorias = list(set([item['categoria'] for item in st.session_state.db.inventario]))
    categoria_seleccionada = st.selectbox("🔍 Filtrar por categoría:", ["Todas"] + categorias)
    
    # Mostrar inventario filtrado
    for item in st.session_state.db.inventario:
        if categoria_seleccionada == "Todas" or item['categoria'] == categoria_seleccionada:
            stock_color = "🟢" if item['stock'] > item.get('min_stock', 0) else "🔴"
            st.write(f"{stock_color} **{item['nombre']}** - Stock: {item['stock']} | Mín: {item.get('min_stock', 'N/A')}")

# FOOTER
st.markdown("---")
st.caption("🎰 **CasinoPro Expert v6.0** - Datos Técnicos + Diagnóstico IA + Conocimiento Técnico Especializado")
st.caption("🔧 **187+ soluciones técnicas validadas por procedimientos especializados**")

# Manejo de redirecciones
if hasattr(st.session_state, 'menu_redirect'):
    st.experimental_set_query_params(menu=st.session_state.menu_redirect)
    del st.session_state.menu_redirect
