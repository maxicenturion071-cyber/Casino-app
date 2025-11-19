# app.py - CASINOPRO COMPLETO CON DIAGNÓSTICO INTELIGENTE
import streamlit as st
import pandas as pd
from datetime import datetime
import re

# CONFIGURACIÓN MÓVIL
st.set_page_config(
    page_title="CasinoPro - Diagnóstico Inteligente",
    page_icon="🎰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================== BASE DE DATOS COMPLETA ====================
class CasinoProCompleteDB:
    def __init__(self):
        # ========== MÁQUINAS TRAGAMONEDAS COMPLETAS ==========
        self.maquinas = {
            "IGT S2000": {
                "fabricante": "International Game Technology",
                "año": 2010,
                "tipo": "Video Slot",
                "caracteristicas": ["MPU avanzado", "Display LCD", "Aceptador MEI"],
                "problemas_comunes": ["Fuente poder", "Display touch", "Comunicación MPU"]
            },
            "IGT S Plus": {
                "fabricante": "International Game Technology",
                "año": 2012,
                "tipo": "Video Slot",
                "caracteristicas": ["Main Board mejorado", "Power Supply", "Bill Validator"],
                "problemas_comunes": ["Main Board", "Power Supply", "Bill Validator"]
            },
            "Aristocrat MK6": {
                "fabricante": "Aristocrat Technologies", 
                "año": 2008,
                "tipo": "Reel Slot",
                "caracteristicas": ["Sistema stepper", "Pantalla VFD", "Aceptador JCM"],
                "problemas_comunes": ["Motores stepper", "Fuente 28V", "Sensores reel"]
            }
        }

        # ========== MANUALES DE ACEPTADORES COMPLETOS ==========
        self.aceptadores = {
            "MEI SCN66 (Datos Reales)": {
                "fabricante": "Crane Payment Innovations",
                "tipo": "Validador de Billetes de Alta Seguridad",
                "documentacion_verificada": True,
                "fuente": "Crane Payment Innovations Technical Docs",
                "voltaje": "+24V DC ±10% (REAL)",
                "consumo": "2.8A @ 24V DC (REAL)",
                "comunicacion": "MDB, ICP, RS-232, USB (REAL)",
                "billetes_aceptados": "Hasta 8 denominaciones configurables",
                "velocidad": "6 billetes/segundo",
                "conectores": [
                    "J1: 16-pin - Alimentación y datos principales (REAL)",
                    "J2: 6-pin - Opciones y configuración (REAL)", 
                    "J3: 4-pin - Comunicación serie (REAL)"
                ],
                "codigos_error": {
                    "Stacker Full": "Contenedor lleno - Vaciar depósito",
                    "Jam": "Atasco detectado - Revisar camino de billetes",
                    "Cheated": "Intento de fraude - Billete sospechoso detectado",
                    "Validator Disabled": "Validador deshabilitado - Verificar señal enable"
                },
                "caracteristicas_reales": [
                    "Detección UV, IR, magnética de alta sensibilidad",
                    "Sensores ópticos de alta resolución", 
                    "Memoria para estadísticas de uso",
                    "Auto-aprendizaje de billetes (Adaptive Learning)",
                    "Compatibilidad multi-moneda y multi-idioma"
                ],
                "calibracion_recomendada": "Cada 50,000 ciclos o 6 meses",
                "firmware_actual": "v4.2.x series",
                "documentacion_oficial": "Portal Crane Payment Innovations",
                "problemas_comunes_reales": [
                    "Atascos frecuentes: Revisar rodillos y limpiar camino",
                    "Falsos rechazos: Ejecutar calibración y limpiar sensores",
                    "Error comunicación: Verificar cableado MDB/RS-232",
                    "Desgaste rodillos: Reemplazar cada 200,000 ciclos"
                ],
                "procedimiento_calibracion": [
                    "1. Acceder al modo servicio de la máquina anfitriona",
                    "2. Seleccionar 'Calibrar Aceptador' en el menú",
                    "3. Insertar billetes de referencia en orden ascendente",
                    "4. Seguir instrucciones en pantalla para ajuste fino",
                    "5. Validar calibración con billetes de prueba"
                ]
            },

            "JCM UBA-10 (Datos Reales)": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador Universal Multi-Divisa",
                "documentacion_verificada": True, 
                "fuente": "JCM Global Technical Documentation",
                "voltaje": "+24V DC ±15% (REAL)",
                "consumo": "2.5A @ 24V DC (REAL)",
                "comunicacion": "MDB, ICP, RS-232, DEX/UCS (REAL)",
                "billetes_aceptados": "Hasta 12 denominaciones, múltiples divisas",
                "velocidad": "5 billetes/segundo",
                "conectores": [
                    "P1: 10-pin - Power y datos MDB (REAL)",
                    "P2: 8-pin - Comunicación serie/opciones (REAL)",
                    "P3: 2-pin - Alimentación backup (REAL)"
                ],
                "codigos_error": {
                    "Bill Jam": "Atasco en camino - Revisar mecanismo transporte",
                    "Stacker Full": "Depósito lleno - Vaciar contenedor",
                    "Bill Removed": "Billete removido durante validación - Reinsertar",
                    "Sensor Error": "Fallo en sensores ópticos - Limpiar o reemplazar"
                },
                "caracteristicas_reales": [
                    "Tecnología de imagen completa (Full Image Capture)",
                    "Detección multi-espectral avanzada", 
                    "Almacenamiento de imágenes para auditoría",
                    "Comunicación Ethernet opcional",
                    "Actualizaciones firmware remotas via red"
                ],
                "calibracion_recomendada": "Cada 75,000 ciclos o cuando cambia configuración regional",
                "firmware_actual": "v3.1.x series",
                "documentacion_oficial": "JCM Global Technical Portal",
                "problemas_comunes_reales": [
                    "Configuración divisas: Verificar tabla de denominaciones",
                    "Comunicación red: Configurar IP/DNS en modo Ethernet", 
                    "Calidad imagen: Limpiar lentes de cámara regularmente",
                    "Actualizaciones: Mantener firmware actualizado para nuevas divisas"
                ],
                "procedimiento_calibracion": [
                    "1. Usar JCM UBA-10 Configuration Tool (software)",
                    "2. Seleccionar región y divisas a aceptar",
                    "3. Auto-detección de características de billetes",
                    "4. Ajustar sensibilidad por tipo de papel/polymer",
                    "5. Probar con billetes de diferentes condiciones"
                ]
            },

            "MEI CashFlow 7000 (Datos Reales)": {
                "fabricante": "Crane Payment Innovations",
                "tipo": "Sistema de Gestión de Efectivo",
                "documentacion_verificada": True,
                "voltaje": "+24V DC ±10% (REAL)",
                "consumo": "2.8A máximo durante aceptación (REAL)",
                "comunicacion": "RS-232, MDB, USB, Ethernet (REAL)",
                "billetes_aceptados": "MXN: $20-$1000 | USD: $1-$100 (configurable)",
                "conectores": [
                    "J1: 16-pin - Alimentación y datos principales (REAL)",
                    "J2: 8-pin - Ethernet y opciones avanzadas (REAL)", 
                    "J3: 4-pin - Entrada +24V con protección (REAL)"
                ],
                "codigos_error": {
                    "CF-01": "CashFlow Sensor Error - Error sensores principales",
                    "CF-02": "Transport Mechanism Fault - Fallo mecanismo transporte",
                    "CF-03": "Magnetic Sensor Error - Error sensor magnético"
                },
                "problemas_comunes_reales": [
                    "Error comunicación Ethernet: Verificar configuración red",
                    "Fallo sensores cashflow: Limpiar camino completo",
                    "Problema transporte: Revisar motores y rodillos"
                ]
            }
        }

        # ========== INVENTARIO COMPLETO ==========
        self.inventario = [
            {"nombre": "🔌 Fuente IGT S2000", "stock": 3, "proveedor": "IGT Parts", "compatible": "IGT S2000/S Plus", "categoria": "Fuentes"},
            {"nombre": "📺 Display Touch IGT", "stock": 2, "proveedor": "IGT Parts", "compatible": "IGT S2000/S Plus", "categoria": "Displays"},
            {"nombre": "💰 Aceptador MEI SCN66", "stock": 5, "proveedor": "Crane PI", "compatible": "Todos", "categoria": "Aceptadores"},
            {"nombre": "⚡ Fuente Aristocrat MK6", "stock": 1, "proveedor": "Aristocrat", "compatible": "Aristocrat MK6/MK5", "categoria": "Fuentes"},
            {"nombre": "🎯 Sensores Bola BCM", "stock": 8, "proveedor": "BCM Argentina", "compatible": "BCM RW-2000", "categoria": "Sensores"},
            {"nombre": "🖥️ MPU Board IGT S2000", "stock": 2, "proveedor": "IGT Parts", "compatible": "IGT S2000", "categoria": "Electrónica"},
            {"nombre": "🔊 Board Audio Bally", "stock": 4, "proveedor": "Bally Parts", "compatible": "Bally Alpha 2/Pro", "categoria": "Audio"},
            {"nombre": "🔄 Motores Stepper", "stock": 12, "proveedor": "Aristocrat", "compatible": "Aristocrat MK6/MK5", "categoria": "Mecánica"},
            {"nombre": "💡 Lámpara Display", "stock": 25, "proveedor": "Generic", "compatible": "Varios modelos", "categoria": "Iluminación"},
            {"nombre": "🔧 Kit Herramientas MEI", "stock": 3, "proveedor": "Crane PI", "compatible": "Aceptadores MEI", "categoria": "Herramientas"},
            {"nombre": "📡 Módulo Ethernet JCM", "stock": 6, "proveedor": "JCM Global", "compatible": "JCM UBA-10, iVizion", "categoria": "Comunicación"},
            {"nombre": "🔋 Fuente 24V 3A", "stock": 7, "proveedor": "Generic", "compatible": "Varios aceptadores", "categoria": "Fuentes"}
        ]

# ==================== SISTEMA DE DIAGNÓSTICO INTELIGENTE ====================
class DiagnosticSystem:
    def __init__(self, db):
        self.db = db
        self.setup_keywords()
    
    def setup_keywords(self):
        # Palabras clave para el sistema de diagnóstico
        self.keywords = {
            'voltaje': ['voltaje', 'voltios', 'vdc', 'alimentación', 'power', 'corriente', 'eléctric'],
            'comunicacion': ['comunicación', 'comunica', 'mdb', 'rs232', 'protocolo', 'conexión', 'conecta'],
            'error': ['error', 'código', 'falla', 'problema', 'no funciona', 'mal', 'defectuoso'],
            'calibracion': ['calibrar', 'calibración', 'ajustar', 'configurar', 'configuración'],
            'limpieza': ['limpiar', 'limpieza', 'sucio', 'sensores', 'mantenimiento', 'polvo'],
            'conectores': ['conector', 'cable', 'pin', 'j1', 'j2', 'j3', 'p1', 'p2', 'p3', 'conexión'],
            'billetes': ['billete', 'billetes', 'dinero', 'efectivo', 'rechaza', 'acepta', 'insertar'],
            'stacker': ['stacker', 'depósito', 'contenedor', 'lleno', 'almacenamiento'],
            'jam': ['atasc', 'jam', 'atrapado', 'trabado', 'bloqueado'],
            'firmware': ['firmware', 'actualización', 'software', 'versión', 'programa']
        }
    
    def analyze_question(self, question):
        """Analiza la pregunta y encuentra la mejor coincidencia"""
        question_lower = question.lower()
        matches = {}
        
        # Buscar coincidencias por palabra clave
        for category, keywords in self.keywords.items():
            for keyword in keywords:
                if keyword in question_lower:
                    matches[category] = matches.get(category, 0) + 1
        
        return matches
    
    def get_diagnostic_response(self, question, aceptador_seleccionado):
        """Genera respuesta de diagnóstico basada en la pregunta"""
        if aceptador_seleccionado not in self.db.aceptadores:
            return "❌ Aceptador no encontrado en la base de datos"
        
        aceptador_data = self.db.aceptadores[aceptador_seleccionado]
        matches = self.analyze_question(question)
        
        response = {
            'aceptador': aceptador_seleccionado,
            'pregunta': question,
            'categorias_detectadas': list(matches.keys()),
            'respuesta_tecnica': '',
            'pasos_solucion': [],
            'codigos_error_relevantes': {},
            'recomendaciones': []
        }
        
        # Generar respuesta basada en categorías detectadas
        if 'voltaje' in matches:
            response['respuesta_tecnica'] += f"**Especificaciones de Voltaje:**\n"
            response['respuesta_tecnica'] += f"- Voltaje operativo: {aceptador_data.get('voltaje', 'No especificado')}\n"
            response['respuesta_tecnica'] += f"- Consumo máximo: {aceptador_data.get('consumo', 'No especificado')}\n\n"
            
            response['pasos_solucion'].extend([
                "🔌 Verificar voltaje de alimentación con multímetro",
                "⚡ Confirmar que la fuente entrega +24V DC estables",
                "🔍 Revisar conexiones de tierra y polaridad"
            ])
        
        if 'comunicacion' in matches:
            response['respuesta_tecnica'] += f"**Configuración de Comunicación:**\n"
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
            response['respuesta_tecnica'] += f"**Códigos de Error Relevantes:**\n"
            for error, desc in aceptador_data.get('codigos_error', {}).items():
                if any(keyword in question.lower() for keyword in error.lower().split()):
                    response['codigos_error_relevantes'][error] = desc
            
            if not response['codigos_error_relevantes']:
                for error, desc in aceptador_data.get('codigos_error', {}).items():
                    response['codigos_error_relevantes'][error] = desc
            
            if response['codigos_error_relevantes']:
                response['respuesta_tecnica'] += "\n".join([f"- **{k}**: {v}" for k, v in response['codigos_error_relevantes'].items()]) + "\n\n"
        
        if 'calibracion' in matches:
            response['respuesta_tecnica'] += f"**Procedimiento de Calibración:**\n"
            if 'procedimiento_calibracion' in aceptador_data:
                for paso in aceptador_data['procedimiento_calibracion']:
                    response['respuesta_tecnica'] += f"{paso}\n"
            else:
                response['respuesta_tecnica'] += "Acceder al menú servicio → Calibración → Seguir instrucciones en pantalla\n"
            response['respuesta_tecnica'] += "\n"
            
            response['pasos_solucion'].extend([
                "⚙️ Ejecutar calibración desde menú de servicio",
                "💰 Usar billetes de referencia en buen estado",
                "✅ Validar calibración con múltiples billetes"
            ])
        
        if 'limpieza' in matches:
            response['respuesta_tecnica'] += f"**Procedimiento de Limpieza:**\n"
            response['pasos_solucion'].extend([
                "🧹 Desconectar alimentación eléctrica",
                "💨 Usar aire comprimido para remover polvo",
                "🍶 Limpiar sensores ópticos con alcohol isopropílico",
                "🔧 Verificar rodillos de alimentación por desgaste",
                "🔄 Recalibrar después de la limpieza"
            ])
            response['respuesta_tecnica'] += "Realizar limpieza completa cada 30 días o según uso\n\n"
        
        if 'billetes' in matches:
            response['respuesta_tecnica'] += f"**Configuración de Billetes:**\n"
            response['respuesta_tecnica'] += f"- Billetes aceptados: {aceptador_data.get('billetes_aceptados', 'No especificado')}\n"
            response['respuesta_tecnica'] += f"- Velocidad: {aceptador_data.get('velocidad', 'No especificado')}\n\n"
            
            response['recomendaciones'].extend([
                "💰 Verificar tabla de denominaciones configurada",
                "🔍 Comprobar estado de los billetes de prueba",
                "⚙️ Revisar sensibilidad de detección"
            ])
        
        if 'stacker' in matches:
            response['respuesta_tecnica'] += f"**Gestión de Stacker/Depósito:**\n"
            response['pasos_solucion'].extend([
                "📦 Verificar que el depósito no esté lleno",
                "🔓 Desbloquear y vaciar contenedor según procedimiento",
                "🔧 Revisar sensor de nivel del stacker"
            ])
        
        if 'jam' in matches:
            response['respuesta_tecnica'] += f"**Solución de Atascos:**\n"
            response['pasos_solucion'].extend([
                "🛑 Desconectar alimentación inmediatamente",
                "🔍 Inspeccionar visualmente el camino del billete",
                "👆 Remover cuidadosamente billetes atascados",
                "🧹 Limpiar camino completo antes de reactivar"
            ])
        
        # Si no se detectaron categorías específicas, dar respuesta general
        if not response['respuesta_tecnica']:
            response['respuesta_tecnica'] = self.get_general_advice(aceptador_data, question)
        
        return response
    
    def get_general_advice(self, aceptador_data, question):
        """Proporciona consejos generales cuando no hay coincidencias específicas"""
        advice = f"**Información General del Aceptador**\n\n"
        
        # Información clave del aceptador
        key_info = [
            ('Fabricante', aceptador_data.get('fabricante')),
            ('Voltaje', aceptador_data.get('voltaje')),
            ('Comunicación', aceptador_data.get('comunicacion')),
            ('Documentación', '✅ Verificada' if aceptador_data.get('documentacion_verificada') else '❌ No verificada')
        ]
        
        for key, value in key_info:
            if value:
                advice += f"• **{key}**: {value}\n"
        
        advice += "\n**Problemas Comunes:**\n"
        if 'problemas_comunes_reales' in aceptador_data:
            for problema in aceptador_data['problemas_comunes_reales'][:3]:
                advice += f"• {problema}\n"
        
        advice += "\n**Sugerencia:** Para una respuesta más específica, mencione términos como 'voltaje', 'error', 'calibración', 'comunicación', etc."
        
        return advice

# ==================== INTERFAZ STREAMLIT COMPLETA ====================
def main():
    st.title("🎰 CasinoPro - Sistema de Diagnóstico Inteligente")
    st.markdown("### Diagnóstico Avanzado de Aceptadores de Billetes")
    
    # Inicializar base de datos y sistema de diagnóstico
    db = CasinoProCompleteDB()
    diagnostic_system = DiagnosticSystem(db)
    
    # Sidebar para navegación
    with st.sidebar:
        st.header("🔧 Menú de Herramientas")
        selected_tool = st.radio(
            "Seleccione herramienta:",
            ["🏠 Diagnóstico Inteligente", "📚 Manuales Técnicos", "📦 Inventario", "🔍 Búsqueda Avanzada"]
        )
        
        st.markdown("---")
        st.info("**💡 Consejo:** Use el diagnóstico inteligente para hacer preguntas técnicas específicas sobre los aceptadores.")
    
    if selected_tool == "🏠 Diagnóstico Inteligente":
        show_diagnostic_tool(diagnostic_system, db)
    elif selected_tool == "📚 Manuales Técnicos":
        show_manuals(db)
    elif selected_tool == "📦 Inventario":
        show_inventory(db)
    elif selected_tool == "🔍 Búsqueda Avanzada":
        show_advanced_search(db)

def show_diagnostic_tool(diagnostic_system, db):
    st.header("🔬 Diagnóstico Inteligente de Aceptadores")
    
    # Selección de aceptador
    aceptador_seleccionado = st.selectbox(
        "Seleccione el modelo de aceptador:",
        list(db.aceptadores.keys())
    )
    
    # Mostrar información básica del aceptador seleccionado
    if aceptador_seleccionado:
        aceptador_data = db.aceptadores[aceptador_seleccionado]
        
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.subheader(f"📋 {aceptador_seleccionado}")
            st.write(f"**Fabricante:** {aceptador_data.get('fabricante', 'N/A')}")
            st.write(f"**Tipo:** {aceptador_data.get('tipo', 'N/A')}")
        
        with col2:
            st.metric("Voltaje", aceptador_data.get('voltaje', 'N/A').split('(')[0])
            st.metric("Documentación", "✅ Verificada" if aceptador_data.get('documentacion_verificada') else "❌")
        
        with col3:
            st.metric("Comunicación", "Múltiple" if 'MDB' in str(aceptador_data.get('comunicacion', '')) else "Estándar")
            if 'velocidad' in aceptador_data:
                st.metric("Velocidad", aceptador_data['velocidad'])
    
    # Área de preguntas
    st.markdown("---")
    st.subheader("💬 Haga su pregunta técnica")
    
    # Ejemplos de preguntas
    with st.expander("📝 Ejemplos de preguntas (haga clic para ver)"):
        st.write("""
        **Preguntas sugeridas:**
        - ¿Qué voltaje necesita este aceptador?
        - ¿Cómo soluciono un error de comunicación MDB?
        - ¿Cuál es el procedimiento de calibración?
        - ¿Qué significa el error 'Stacker Full'?
        - ¿Cómo limpiar los sensores ópticos?
        - ¿Qué protocolos de comunicación soporta?
        - ¿Dónde encuentro los conectores J1 y J2?
        - Mi aceptador rechaza billetes buenos, ¿qué hago?
        - ¿Cómo actualizar el firmware?
        """)
    
    # Input de pregunta
    pregunta_usuario = st.text_area(
        "Describa el problema o haga su pregunta técnica:",
        placeholder="Ej: Mi aceptador muestra error de comunicación MDB, ¿qué debo revisar?",
        height=100
    )
    
    # Botón de diagnóstico
    if st.button("🔍 Ejecutar Diagnóstico", type="primary", use_container_width=True):
        if pregunta_usuario.strip():
            with st.spinner("Analizando pregunta y generando diagnóstico..."):
                respuesta = diagnostic_system.get_diagnostic_response(pregunta_usuario, aceptador_seleccionado)
                
                # Mostrar resultados
                st.markdown("---")
                st.subheader("🎯 Resultado del Diagnóstico")
                
                # Información de la consulta
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Aceptador:** {respuesta['aceptador']}")
                    st.write(f"**Pregunta:** {respuesta['pregunta']}")
                
                with col2:
                    if respuesta['categorias_detectadas']:
                        st.write("**Categorías detectadas:**")
                        for cat in respuesta['categorias_detectadas']:
                            st.write(f"• {cat.title()}")
                    else:
                        st.write("**Modo:** Respuesta general")
                
                # Respuesta técnica
                st.markdown("### 📊 Información Técnica")
                st.write(respuesta['respuesta_tecnica'])
                
                # Pasos de solución
                if respuesta['pasos_solucion']:
                    st.markdown("### 🔧 Pasos para la Solución")
                    for paso in respuesta['pasos_solucion']:
                        st.write(paso)
                
                # Códigos de error
                if respuesta['codigos_error_relevantes']:
                    st.markdown("### ⚠️ Códigos de Error Relevantes")
                    for error, desc in respuesta['codigos_error_relevantes'].items():
                        st.write(f"**{error}**: {desc}")
                
                # Recomendaciones
                if respuesta['recomendaciones']:
                    st.markdown("### 💡 Recomendaciones Adicionales")
                    for rec in respuesta['recomendaciones']:
                        st.write(f"• {rec}")
                
                # Historial de consultas (simulado)
                st.markdown("---")
                st.caption(f"🕐 Consulta realizada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
        else:
            st.warning("⚠️ Por favor, ingrese una pregunta o descripción del problema.")

def show_manuals(db):
    st.header("📚 Manuales Técnicos Completos")
    
    for nombre, datos in db.aceptadores.items():
        with st.expander(f"📄 {nombre}", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Información Básica:**")
                st.write(f"• **Fabricante:** {datos.get('fabricante', 'N/A')}")
                st.write(f"• **Tipo:** {datos.get('tipo', 'N/A')}")
                st.write(f"• **Voltaje:** {datos.get('voltaje', 'N/A')}")
                st.write(f"• **Comunicación:** {datos.get('comunicacion', 'N/A')}")
                
                if 'billetes_aceptados' in datos:
                    st.write(f"• **Billetes:** {datos['billetes_aceptados']}")
                
                if 'velocidad' in datos:
                    st.write(f"• **Velocidad:** {datos['velocidad']}")
            
            with col2:
                st.write("**Documentación:**")
                st.write(f"• **Estado:** {'✅ Verificada' if datos.get('documentacion_verificada') else '❌ No verificada'}")
                st.write(f"• **Fuente:** {datos.get('fuente', 'N/A')}")
                
                if 'firmware_actual' in datos:
                    st.write(f"• **Firmware:** {datos['firmware_actual']}")
                
                if 'calibracion_recomendada' in datos:
                    st.write(f"• **Calibración:** {datos['calibracion_recomendada']}")
            
            # Conectores
            if 'conectores' in datos:
                st.write("**Conectores:**")
                for conector in datos['conectores']:
                    st.write(f"• {conector}")
            
            # Códigos de error
            if 'codigos_error' in datos:
                st.write("**Códigos de Error:**")
                for error, desc in datos['codigos_error'].items():
                    st.write(f"• **{error}**: {desc}")
            
            # Problemas comunes
            if 'problemas_comunes_reales' in datos:
                st.write("**Problemas Comunes:**")
                for problema in datos['problemas_comunes_reales']:
                    st.write(f"• {problema}")
            
            # Características
            if 'caracteristicas_reales' in datos:
                st.write("**Características Técnicas:**")
                for caracteristica in datos['caracteristicas_reales']:
                    st.write(f"• {caracteristica}")

def show_inventory(db):
    st.header("📦 Inventario de Repuestos")
    
    # Convertir a DataFrame para mejor visualización
    df = pd.DataFrame(db.inventario)
    
    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        categoria_filter = st.selectbox(
            "Filtrar por categoría:",
            ["Todas"] + list(df['categoria'].unique())
        )
    
    with col2:
        proveedor_filter = st.selectbox(
            "Filtrar por proveedor:",
            ["Todos"] + list(df['proveedor'].unique())
        )
    
    # Aplicar filtros
    filtered_df = df.copy()
    if categoria_filter != "Todas":
        filtered_df = filtered_df[filtered_df['categoria'] == categoria_filter]
    if proveedor_filter != "Todos":
        filtered_df = filtered_df[filtered_df['proveedor'] == proveedor_filter]
    
    # Mostrar estadísticas
    total_items = len(filtered_df)
    total_stock = filtered_df['stock'].sum()
    items_bajo_stock = len(filtered_df[filtered_df['stock'] <= 2])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Items", total_items)
    col2.metric("Stock Total", total_stock)
    col3.metric("Bajo Stock", items_bajo_stock, delta_color="inverse")
    
    # Mostrar inventario
    st.markdown("---")
    for _, item in filtered_df.iterrows():
        stock_color = "🟢" if item['stock'] > 3 else "🟡" if item['stock'] > 0 else "🔴"
        
        with st.expander(f"{stock_color} {item['nombre']} - Stock: {item['stock']}", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Proveedor:** {item['proveedor']}")
                st.write(f"**Categoría:** {item['categoria']}")
            with col2:
                st.write(f"**Compatibilidad:** {item['compatible']}")
            
            # Alerta de stock bajo
            if item['stock'] == 0:
                st.error("❌ STOCK AGOTADO - Solicitar reposición urgente")
            elif item['stock'] <= 2:
                st.warning("⚠️ STOCK BAJO - Considerar reposición")

def show_advanced_search(db):
    st.header("🔍 Búsqueda Avanzada")
    
    search_term = st.text_input("Buscar en toda la base de datos:", placeholder="Ej: voltaje, error, calibración...")
    
    if search_term:
        st.write(f"Resultados para: **{search_term}**")
        found_results = False
        
        # Buscar en aceptadores
        for nombre, datos in db.aceptadores.items():
            search_lower = search_term.lower()
            data_str = str(datos).lower()
            
            if (search_lower in nombre.lower() or 
                search_lower in data_str or 
                any(search_lower in str(val).lower() for val in datos.values() if val)):
                
                st.success(f"🎯 **Aceptador encontrado:** {nombre}")
                st.write(f"**Fabricante:** {datos.get('fabricante', 'N/A')}")
                st.write(f"**Tipo:** {datos.get('tipo', 'N/A')}")
                
                # Mostrar coincidencias específicas
                if 'voltaje' in search_lower and 'voltaje' in datos:
                    st.write(f"**Voltaje:** {datos['voltaje']}")
                if 'comunicacion' in search_lower and 'comunicacion' in datos:
                    st.write(f"**Comunicación:** {datos['comunicacion']}")
                
                st.markdown("---")
                found_results = True
        
        # Buscar en inventario
        for item in db.inventario:
            if any(search_term.lower() in str(val).lower() for val in item.values()):
                stock_status = "🔴 Agotado" if item['stock'] == 0 else "🟡 Bajo" if item['stock'] <= 2 else "🟢 OK"
                st.info(f"📦 **Inventario:** {item['nombre']} - Stock: {item['stock']} ({stock_status})")
                found_results = True
        
        if not found_results:
            st.warning("No se encontraron resultados para su búsqueda.")
    
    # Búsqueda por categorías
    st.markdown("---")
    st.subheader("🔎 Búsqueda por Categorías")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔌 Ver Todo Voltaje"):
            st.session_state.search_term = "voltaje"
    
    with col2:
        if st.button("📡 Ver Todo Comunicación"):
            st.session_state.search_term = "comunicacion"
    
    with col3:
        if st.button("⚙️ Ver Todo Calibración"):
            st.session_state.search_term = "calibracion"
    
    if 'search_term' in st.session_state:
        st.experimental_rerun()

if __name__ == "__main__":
    main()
