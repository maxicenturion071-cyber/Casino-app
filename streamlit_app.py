# CONTINUACIÓN Y CORRECCIÓN DEL CÓDIGO ANTERIOR

# ==================== COMPLETAR SECCIÓN DE BASE DE CONOCIMIENTO TÉCNICO ====================
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
                st.write(insecto)
                
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

# ==================== NUEVO: SISTEMA DE POZOS ACUMULATIVOS ====================
class ProgressiveSystems:
    def __init__(self):
        self.progressive_data = self.setup_progressive_knowledge()
    
    def setup_progressive_knowledge(self):
        """Base de conocimiento completa sobre pozos acumulativos"""
        return {
            'mikhon_systems': {
                'title': '🔧 SISTEMAS MIKHON PROGRESSIVE',
                'sections': {
                    'arquitectura': {
                        'title': '🏗️ Arquitectura Mikhon',
                        'content': [
                            "**SISTEMA MIKHON PROGRESSIVE**",
                            "• Wide Area Progressive (WAP) - Múltiples casinos",
                            "• Standalone Progressive - Máquina individual", 
                            "• Hybrid Systems - Combinación flexible",
                            "",
                            "**COMPONENTES PRINCIPALES:**",
                            "• Servidor Central Mikhon - Control maestro",
                            "• Hubs de Comunicación - Distribución datos",
                            "• Controladores de Display - Pantallas progresivas",
                            "• Interfaces SAS Extendidas - Comunicación máquinas"
                        ]
                    },
                    'configuracion': {
                        'title': '⚙️ Configuración Básica',
                        'content': [
                            "**PARÁMETROS DE CONFIGURACIÓN:**",
                            "• Incremento: 0.5% - 2.5% de cada apuesta",
                            "• Base Amount: Valor inicial del pozo",
                            "• Reset Value: Valor al resetear",
                            "• Hit Point: Cuando se debe pagar el pozo",
                            "",
                            "**EJEMPLO PRÁCTICO:**",
                            "Base: $1,000 | Incremento: 1% | Reset: $1,000",
                            "Cada $1 apostado → $0.01 al pozo"
                        ]
                    },
                    'problemas_comunes': {
                        'title': '⚠️ Problemas Comunes',
                        'content': [
                            "**COMUNICACIÓN:**",
                            "• Hubs no sincronizados",
                            "• Latencia de red alta",
                            "• Configuración SAS incorrecta",
                            "",
                            "**CONTABILIDAD:**",
                            "• Discrepancias en valores",
                            "• Resets no registrados",
                            "• Validación de jackpots fallida",
                            "",
                            "**DISPLAYS:**",
                            "• Pantallas no actualizan",
                            "• Controladores offline",
                            "• Cableado dañado"
                        ]
                    }
                }
            },
            'igt_progressive': {
                'title': '💻 IGT PROGRESSIVE SYSTEMS',
                'sections': {
                    's2000_3000': {
                        'title': '🎰 S2000/S3000 Progressives',
                        'content': [
                            "**ARQUITECTURA LEGACY:**",
                            "• SAS 5.0x/6.0x protocol",
                            "• Progressive Controller Boards",
                            "• Display Drivers específicos",
                            "",
                            "**CONFIGURACIÓN:**",
                            "• Menú Service → Progressive Setup",
                            "• Configurar niveles: Minor/Major/Grand",
                            "• Validar comunicación SAS"
                        ]
                    },
                    'peak_systems': {
                        'title': '🔥 Peak Progressive',
                        'content': [
                            "**SISTEMA MODERNO:**",
                            "• Ethernet-based communication",
                            "• Web interface de configuración",
                            "• Multiple progressive levels",
                            "",
                            "• Validación automática",
                            "• Logs detallados",
                            "• Monitorización en tiempo real"
                        ]
                    }
                }
            },
            'configuraciones_avanzadas': {
                'title': '⚙️ CONFIGURACIONES AVANZADAS',
                'sections': {
                    'niveles_multiples': {
                        'title': '📊 Múltiples Niveles',
                        'content': [
                            "**ESTRUCTURA TÍPICA:**",
                            "• Mini: $10 - $100",
                            "• Minor: $100 - $1,000", 
                            "• Major: $1,000 - $10,000",
                            "• Grand: $10,000+",
                            "",
                            "**CONFIGURACIÓN:**",
                            "• Incrementos diferenciados",
                            "• Resets independientes",
                            "• Límites específicos"
                        ]
                    },
                    'seguimiento_contable': {
                        'title': '📈 Seguimiento Contable',
                        'content': [
                            "**VALIDACIONES:**",
                            "• Auditoría de incrementos",
                            "• Verificación de resets",
                            "• Conciliación de valores",
                            "",
                            "• Logs de transacciones",
                            "• Reportes automáticos",
                            "• Alertas de discrepancias"
                        ]
                    }
                }
            }
        }

# ==================== NUEVO: CALCULADORA DE RESISTENCIAS COMPLETA ====================
class ResistanceCalculator:
    def calcular_ley_ohm(self, voltaje=None, corriente=None, resistencia=None):
        """Calcula parámetros faltantes usando Ley de Ohm"""
        try:
            if voltaje is not None and corriente is not None:
                resistencia = voltaje / corriente
                potencia = voltaje * corriente
                return {
                    'resistencia': round(resistencia, 2),
                    'potencia': round(potencia, 2),
                    'formula': f"R = V/I = {voltaje}/{corriente}"
                }
            elif voltaje is not None and resistencia is not None:
                corriente = voltaje / resistencia
                potencia = voltaje * corriente
                return {
                    'corriente': round(corriente, 3),
                    'potencia': round(potencia, 2),
                    'formula': f"I = V/R = {voltaje}/{resistencia}"
                }
            elif corriente is not None and resistencia is not None:
                voltaje = corriente * resistencia
                potencia = voltaje * corriente
                return {
                    'voltaje': round(voltaje, 2),
                    'potencia': round(potencia, 2),
                    'formula': f"V = I×R = {corriente}×{resistencia}"
                }
        except:
            return None
    
    def calcular_divisor_voltaje(self, vin, r1, r2):
        """Calcula divisor de voltaje"""
        try:
            vout = vin * (r2 / (r1 + r2))
            corriente = vin / (r1 + r2)
            return {
                'vout': round(vout, 2),
                'corriente': round(corriente, 3),
                'formula': f"Vout = Vin × (R2/(R1+R2)) = {vin} × ({r2}/({r1}+{r2}))"
            }
        except:
            return None
    
    def calcular_resistencia_led(self, voltaje_fuente, voltaje_led, corriente_led_ma):
        """Calcula resistencia para LED"""
        try:
            corriente_led = corriente_led_ma / 1000  # Convertir mA a A
            resistencia = (voltaje_fuente - voltaje_led) / corriente_led
            potencia = (voltaje_fuente - voltaje_led) * corriente_led
            
            # Encontrar valor comercial más cercano
            valor_comercial = self.encontrar_valor_comercial(resistencia)
            
            return {
                'resistencia_calculada': round(resistencia, 1),
                'resistencia_comercial': valor_comercial,
                'potencia': round(potencia, 2),
                'corriente_real': round((voltaje_fuente - voltaje_led) / valor_comercial['valor'], 3)
            }
        except:
            return None
    
    def encontrar_valor_comercial(self, resistencia):
        """Encuentra el valor comercial más cercano"""
        serie_e12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
                    100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820,
                    1000, 1200, 1500, 1800, 2200, 2700, 3300, 3900, 4700, 5600, 6800, 8200,
                    10000, 12000, 15000, 18000, 22000, 27000, 33000, 39000, 47000, 56000, 68000, 82000,
                    100000, 120000, 150000, 180000, 220000, 270000, 330000, 390000, 470000, 560000, 680000, 820000,
                    1000000]
        
        valor_mas_cercano = min(serie_e12, key=lambda x: abs(x - resistencia))
        
        # Calcular potencia recomendada (mínimo 2x la calculada para margen)
        potencia_minima = (resistencia / 1000) * 2  # Estimación simple
        
        return {
            'valor': valor_mas_cercano,
            'potencia_recomendada': f"{max(0.125, round(potencia_minima, 3))}W"
        }
    
    def calcular_combinaciones(self, resistencias, tipo='serie'):
        """Calcula combinaciones serie/paralelo"""
        try:
            if tipo == 'serie':
                total = sum(resistencias)
                return {
                    'total': round(total, 2),
                    'formula': 'R_total = R1 + R2 + ... + Rn'
                }
            else:  # paralelo
                total = 1 / sum(1/r for r in resistencias)
                return {
                    'total': round(total, 2),
                    'formula': '1/R_total = 1/R1 + 1/R2 + ... + 1/Rn'
                }
        except:
            return None

# ==================== AGREGAR NUEVOS SISTEMAS AL SESSION STATE ====================
if 'progressive_systems' not in st.session_state:
    st.session_state.progressive_systems = ProgressiveSystems()

if 'resistance_calculator' not in st.session_state:
    st.session_state.resistance_calculator = ResistanceCalculator()

# ==================== ACTUALIZAR MENÚ PRINCIPAL ====================
# Reemplazar la definición del menú para incluir nuevas opciones
menu_options = [
    "🏠 INICIO", 
    "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO",
    "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO",
    "🔧 INFORMACIÓN TÉCNICA ESPECÍFICA",
    "💰 POZOS ACUMULATIVOS",  # NUEVA OPCIÓN
    "🧮 CALCULADORA RESISTENCIAS",  # NUEVA OPCIÓN
    "💰 MANUALES ACEPTADORES",
    "🎰 MÁQUINAS REGISTRADAS", 
    "📦 INVENTARIO COMPLETO"
]

# ==================== NUEVA SECCIÓN: POZOS ACUMULATIVOS ====================
elif st.session_state.current_menu == "💰 POZOS ACUMULATIVOS":
    st.header("💰 SISTEMAS DE POZOS ACUMULATIVOS")
    st.success("**🎯 Información técnica especializada sobre sistemas progresivos**")
    
    tab1, tab2, tab3 = st.tabs(["🔧 Mikhon Systems", "💻 IGT Systems", "⚙️ Configuraciones"])
    
    with tab1:
        st.subheader("🔧 MIKHON PROGRESSIVE SYSTEMS")
        
        subseccion = st.radio(
            "Seleccioná información:",
            ["Arquitectura", "Configuración", "Problemas Comunes"],
            key="mikhon_subs"
        )
        
        if subseccion == "Arquitectura":
            info = st.session_state.progressive_systems.progressive_data['mikhon_systems']['sections']['arquitectura']
        elif subseccion == "Configuración":
            info = st.session_state.progressive_systems.progressive_data['mikhon_systems']['sections']['configuracion']
        else:
            info = st.session_state.progressive_systems.progressive_data['mikhon_systems']['sections']['problemas_comunes']
        
        if info:
            st.markdown(f"### {info['title']}")
            for line in info['content']:
                if line.startswith("**"):
                    st.markdown(line)
                else:
                    st.write(line)
    
    with tab2:
        st.subheader("💻 IGT PROGRESSIVE SYSTEMS")
        
        subseccion = st.radio(
            "Seleccioná sistema:",
            ["S2000/S3000", "Peak Systems"],
            key="igt_subs"
        )
        
        if subseccion == "S2000/S3000":
            info = st.session_state.progressive_systems.progressive_data['igt_progressive']['sections']['s2000_3000']
        else:
            info = st.session_state.progressive_systems.progressive_data['igt_progressive']['sections']['peak_systems']
        
        if info:
            st.markdown(f"### {info['title']}")
            for line in info['content']:
                if line.startswith("**"):
                    st.markdown(line)
                else:
                    st.write(line)
    
    with tab3:
        st.subheader("⚙️ CONFIGURACIONES AVANZADAS")
        
        subseccion = st.radio(
            "Seleccioná configuración:",
            ["Niveles Múltiples", "Seguimiento Contable"],
            key="config_subs"
        )
        
        if subseccion == "Niveles Múltiples":
            info = st.session_state.progressive_systems.progressive_data['configuraciones_avanzadas']['sections']['niveles_multiples']
        else:
            info = st.session_state.progressive_systems.progressive_data['configuraciones_avanzadas']['sections']['seguimiento_contable']
        
        if info:
            st.markdown(f"### {info['title']}")
            for line in info['content']:
                if line.startswith("**"):
                    st.markdown(line)
                else:
                    st.write(line)

# ==================== NUEVA SECCIÓN: CALCULADORA DE RESISTENCIAS ====================
elif st.session_state.current_menu == "🧮 CALCULADORA RESISTENCIAS":
    st.header("🧮 CALCULADORA DE RESISTENCIAS COMPLETA")
    st.success("**🔧 Herramientas para cálculos electrónicos en reparaciones**")
    
    calc_type = st.selectbox(
        "🔧 Seleccioná calculadora:",
        ["Ley de Ohm", "Divisor de Voltaje", "Resistencia para LED", "Combinaciones Serie/Paralelo"]
    )
    
    if calc_type == "Ley de Ohm":
        st.subheader("🔋 LEY DE OHM")
        st.write("Calculá el parámetro faltante (dejá un campo vacío)")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            voltaje = st.number_input("Voltaje (V)", value=None, placeholder="Ej: 12.0")
        with col2:
            corriente = st.number_input("Corriente (A)", value=None, placeholder="Ej: 0.5")
        with col3:
            resistencia = st.number_input("Resistencia (Ω)", value=None, placeholder="Ej: 1000")
        
        if st.button("🔄 Calcular Ley de Ohm"):
            resultado = st.session_state.resistance_calculator.calcular_ley_ohm(voltaje, corriente, resistencia)
            if resultado:
                st.info(f"""
                **📊 RESULTADOS:**
                - {resultado['formula']}
                {f"- 🔌 Resistencia: **{resultado['resistencia']}Ω**" if 'resistencia' in resultado else ''}
                {f"- ⚡ Corriente: **{resultado['corriente']}A**" if 'corriente' in resultado else ''}
                {f"- 🔋 Voltaje: **{resultado['voltaje']}V**" if 'voltaje' in resultado else ''}
                - 💡 Potencia: **{resultado['potencia']}W**
                """)
            else:
                st.error("❌ Ingresá exactamente 2 valores para calcular el tercero")
    
    elif calc_type == "Divisor de Voltaje":
        st.subheader("🎚️ DIVISOR DE VOLTAJE")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            vin = st.number_input("Voltaje Entrada (V)", value=12.0)
        with col2:
            r1 = st.number_input("Resistencia R1 (Ω)", value=1000.0)
        with col3:
            r2 = st.number_input("Resistencia R2 (Ω)", value=1000.0)
        
        if st.button("🔄 Calcular Divisor"):
            resultado = st.session_state.resistance_calculator.calcular_divisor_voltaje(vin, r1, r2)
            if resultado:
                st.info(f"""
                **📊 RESULTADOS DIVISOR:**
                - {resultado['formula']}
                - 🔌 Voltaje Salida: **{resultado['vout']}V**
                - ⚡ Corriente: **{resultado['corriente']}A**
                - 💡 Potencia R1: **{round(resultado['corriente']**2 * r1, 3)}W**
                - 💡 Potencia R2: **{round(resultado['corriente']**2 * r2, 3)}W**
                """)
    
    elif calc_type == "Resistencia para LED":
        st.subheader("💡 RESISTENCIA PARA LED")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            vfuente = st.number_input("Voltaje Fuente (V)", value=5.0)
        with col2:
            vled = st.number_input("Voltaje LED (V)", value=2.1)
        with col3:
            iled = st.number_input("Corriente LED (mA)", value=20)
        
        if st.button("🔄 Calcular para LED"):
            resultado = st.session_state.resistance_calculator.calcular_resistencia_led(vfuente, vled, iled)
            if resultado:
                st.info(f"""
                **💡 RESULTADOS LED:**
                - 🔌 Resistencia calculada: **{resultado['resistencia_calculada']}Ω**
                - 🏪 Valor comercial: **{resultado['resistencia_comercial']['valor']}Ω**
                - 💡 Potencia calculada: **{resultado['potencia']}W**
                - 🔋 Potencia recomendada: **{resultado['resistencia_comercial']['potencia_recomendada']}**
                - ⚡ Corriente real: **{resultado['corriente_real']}A**
                """)
    
    elif calc_type == "Combinaciones Serie/Paralelo":
        st.subheader("🔌 COMBINACIONES DE RESISTENCIAS")
        
        tipo = st.radio("Tipo de combinación:", ["Serie", "Paralelo"])
        
        st.write("**Ingresá los valores de resistencia (Ω):**")
        col1, col2, col3 = st.columns(3)
        with col1:
            r1 = st.number_input("R1 (Ω)", value=1000.0)
        with col2:
            r2 = st.number_input("R2 (Ω)", value=1000.0)
        with col3:
            r3 = st.number_input("R3 (Ω)", value=0.0)
        
        resistencias = [r for r in [r1, r2, r3] if r > 0]
        
        if st.button("🔄 Calcular Combinación"):
            if len(resistencias) >= 2:
                resultado = st.session_state.resistance_calculator.calcular_combinaciones(
                    resistencias, 
                    'serie' if tipo == "Serie" else 'paralelo'
                )
                if resultado:
                    st.info(f"""
                    **📊 RESULTADOS {tipo.upper()}:**
                    - {resultado['formula']}
                    - 🔌 Resistencia total: **{resultado['total']}Ω**
                    - 📝 Resistencias usadas: {', '.join([f'{r}Ω' for r in resistencias])}
                    """)
            else:
                st.error("❌ Necesitás al menos 2 resistencias")

# ACTUALIZAR FOOTER FINAL
st.markdown("---")
st.caption("🎰 **CasinoPro Expert v8.0** - Sistema Completo con Pozos Acumulativos + Calculadora de Resistencias")
st.caption("🔧 **Desarrollado por [Tu Nombre] - Todos los derechos reservados**")

# Botón para volver al inicio en todas las páginas
if st.session_state.current_menu != "🏠 INICIO":
    if st.button("🏠 Volver al Inicio", use_container_width=True, key="back_home_final"):
        st.session_state.current_menu = "🏠 INICIO"
        st.rerun()
