# app.py - CASINOPRO COMPLETO CON TODA LA INFORMACIÓN ORIGINAL + MEJORAS
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

# ==================== NUEVO: SISTEMA ESPECIALISTA CPU-4.2.2.X ====================
class CPU422XSpecialist:
    def __init__(self):
        self.cpu_data = self.setup_cpu_database()
        self.led_codes = self.setup_led_codes()
        self.troubleshooting_flows = self.setup_troubleshooting_flows()
    
    def setup_cpu_database(self):
        """Base de datos técnica específica de CPU-4.2.2.X"""
        return {
            'especificaciones_generales': {
                'modelo': 'CPU-4.2.2.X',
                'numero_parte': '1458954',
                'fabricante': 'Scientific Games',
                'manual_servicio': '1458954 SERVICE MANUAL',
                'voltaje_operativo': '+24V DC',
                'temperatura_operacion': '4-40°C (39.2-104°F)',
                'humedad_maxima': '90%',
                'maquinas_compatibles': [
                    "Twinstar Vertical (56-T14335T)",
                    "Bally Alpha Series", 
                    "Bally iVIEW DM Systems",
                    "Otras máquinas Scientific Games modernas"
                ],
                'aplicacion_primaria': "Subsistema de control para máquinas de juego Scientific Games/Bally",
                'componentes_principales': [
                    'Ensamblaje CPU-4.XXX',
                    'Placa de plano posterior', 
                    'Módulo de fuente de alimentación (PSM)',
                    'Bandeja de ventilador'
                ]
            },
            
            'leds_panel_frontal': {
                'ESTADO DE POTENCIA': {
                    'APAGADO': 'Alimentación de CA apagada o modo bajo consumo',
                    'ROJO': 'Alimentación CA encendida, SIDC - Wake On LAN',
                    'VERDE': 'Alimentación CA encendida, CPU-4K ENCENDIDA EGM APAGADA, Modo servicio',
                    'AZUL': 'Alimentación CA encendida, Operación normal'
                },
                'BOTÓN DE ENCENDIDO': {
                    'funcionalidad': 'Definida por firmware - múltiples modos según estado'
                },
                'ESTADO DE LA CPU': {
                    'descripcion': 'Dos LED de siete segmentos para diagnóstico'
                }
            },
            
            'baterias': {
                'bateria_cr2032': {
                    'tipo': 'Celda de moneda 3.2V',
                    'ubicacion': 'Placa principal',
                    'proposito': 'Backup BIOS/configuración'
                },
                'baterias_aa': {
                    'tipo': 'Litio AA 1.5V',
                    'cantidad': '4 unidades',
                    'proposito': 'Backup de sistema'
                }
            },
            
            'componentes_internos': {
                'tarjeta_video': 'Con conducto de ventilación',
                'modulo_bios': 'Receptáculo amarillo - JUR SPI',
                'ssd': 'Unidad de estado sólido 64GB SATA',
                'memoria': 'Módulos DRAM',
                'guia_modulo_bios': 'Sistema de guía amarillo'
            }
        }
    
    def setup_led_codes(self):
        """Códigos de error de LED de estado"""
        return {
            '1C': {'nombre': 'ALL_SYS_PWRGD_FAIL', 'descripcion': 'Fallo en circuito de alimentación interno', 'solucion': 'Reemplazar CPU'},
            '24': {'nombre': 'APU_THERMTRIP', 'descripcion': 'Protección térmica activada', 'solucion': 'Verificar ventilación y disipadores'},
            '25': {'nombre': 'APU_OVERTEMP', 'descripcion': 'Temperatura APU excede umbral', 'solucion': 'Limpiar ventiladores y verificar flujo de aire'},
            '26': {'nombre': 'RAM_OVERTEMP', 'descripcion': 'Temperatura RAM excede umbral', 'solucion': 'Verificar módulos RAM y ventilación'},
            '40': {'nombre': 'GIO_PG_TIMEOUT', 'descripcion': 'Timeout señal de poder GIO', 'solucion': 'Reemplazar placa GIO'},
            '49': {'nombre': 'MXM_THERMTRIP', 'descripcion': 'Protección térmica tarjeta video', 'solucion': 'Verificar ventilador tarjeta video'},
            '68': {'nombre': 'SYS_OUT_PS_OVERTEMP', 'descripcion': 'Temperatura aire de salida alta', 'solucion': 'Limpiar filtros y verificar ventilación ambiente'}
        }
    
    def setup_troubleshooting_flows(self):
        """Flujos de solución de problemas específicos"""
        return {
            'no_enciende': [
                "1. Verificar alimentación +24V DC en conector J1",
                "2. Comprobar LED de estado de potencia",
                "3. Verificar módulo BIOS instalado correctamente",
                "4. Revisar baterías de backup",
                "5. Comprobar fuente de alimentación PSM"
            ],
            'sobrecalentamiento': [
                "1. Limpiar filtros de aire y rejillas de ventilación",
                "2. Verificar funcionamiento de todos los ventiladores",
                "3. Comprobar que la bandeja de ventilador esté instalada",
                "4. Verificar ambiente operativo (no exceder 40°C)",
                "5. Revisar disipadores de CPU y tarjeta video"
            ],
            'problemas_video': [
                "1. Verificar tarjeta de video y conducto instalados",
                "2. Comprobar conexiones LVDS a pantalla",
                "3. Reinstalar tarjeta de video en ranura PCIe",
                "4. Verificar módulo BIOS y LED de diagnóstico",
                "5. Probar con tarjeta de video de respuesto"
            ],
            'error_bios': [
                "1. Verificar módulo BIOS en receptáculo amarillo",
                "2. Comprobar batería CR2032",
                "3. Reinstalar módulo BIOS",
                "4. Verificar LED del módulo BIOS (Power, POST, Validation)",
                "5. Reemplazar módulo BIOS si es necesario"
            ]
        }
    
    def diagnosticar_problema(self, sintoma, codigo_error=None):
        """Diagnóstico especializado para CPU-4.2.2.X"""
        diagnostico = {
            'sintoma': sintoma,
            'codigo_error': codigo_error,
            'posibles_causas': [],
            'pasos_solucion': [],
            'componentes_afectados': [],
            'prioridad': 'MEDIA'
        }
        
        sintoma_lower = sintoma.lower()
        
        # Diagnóstico por código de error
        if codigo_error and codigo_error in self.led_codes:
            error_info = self.led_codes[codigo_error]
            diagnostico['posibles_causas'].append(f"Error {codigo_error}: {error_info['descripcion']}")
            diagnostico['pasos_solucion'].append(f"Solución: {error_info['solucion']}")
            diagnostico['prioridad'] = 'ALTA'
        
        # Diagnóstico por síntomas
        if 'no enciende' in sintoma_lower:
            diagnostico['posibles_causas'].extend([
                "Falta de alimentación +24V DC",
                "Fuente de alimentación PSM defectuosa", 
                "Problema en placa de plano posterior",
                "Módulo BIOS no detectado"
            ])
            diagnostico['pasos_solucion'] = self.troubleshooting_flows['no_enciende']
            diagnostico['componentes_afectados'] = ['PSM', 'Placa posterior', 'Módulo BIOS']
            
        elif 'calienta' in sintoma_lower or 'sobrecalienta' in sintoma_lower:
            diagnostico['posibles_causas'].extend([
                "Ventiladores obstruidos o fallados",
                "Filtros de aire sucios",
                "Ambiente operativo muy cálido",
                "Disipadores de calor mal contactados"
            ])
            diagnostico['pasos_solucion'] = self.troubleshooting_flows['sobrecalentamiento']
            diagnostico['componentes_afectados'] = ['Bandeja ventilador', 'Ventiladores', 'Disipadores']
            diagnostico['prioridad'] = 'ALTA'
            
        elif 'pantalla' in sintoma_lower or 'video' in sintoma_lower:
            diagnostico['posibles_causas'].extend([
                "Tarjeta de video mal asentada",
                "Conducto de video obstruido",
                "Problema en conexiones LVDS",
                "Módulo BIOS corrupto"
            ])
            diagnostico['pasos_solucion'] = self.troubleshooting_flows['problemas_video']
            diagnostico['componentes_afectados'] = ['Tarjeta video', 'Conducto video', 'Módulo BIOS']
            
        elif 'bios' in sintoma_lower or 'post' in sintoma_lower:
            diagnostico['posibles_causas'].extend([
                "Módulo BIOS no instalado correctamente",
                "Batería CR2032 agotada",
                "Corrupción de firmware",
                "Problema en guía del módulo BIOS"
            ])
            diagnostico['pasos_solucion'] = self.troubleshooting_flows['error_bios']
            diagnostico['componentes_afectados'] = ['Módulo BIOS', 'Batería CR2032', 'Guía módulo']
            
        return diagnostico
    
    def get_procedimiento_reemplazo(self, componente):
        """Procedimientos de reemplazo específicos"""
        procedimientos = {
            'bateria_cr2032': [
                "1. Usar alicates de punta de aguja aislados",
                "2. Retirar batería vieja del zócalo",
                "3. Insertar nueva batería CR2032 con polaridad correcta (+ hacia frente)",
                "4. Asegurar que quede firmemente asentada"
            ],
            'baterias_aa': [
                "1. Usar destornillador plano pequeño para liberar clips",
                "2. Retirar baterías viejas con cuidado",
                "3. Insertar 4 nuevas baterías de litio AA",
                "4. Reinstalar clips asegurando que encajen en ranuras"
            ],
            'modulo_bios': [
                "1. Localizar guía del módulo BIOS (amarillo)",
                "2. Retirar módulo existente sujetando por el asa",
                "3. Insertar nuevo módulo en receptáculo amarillo",
                "4. Presionar suavemente hasta asentar completamente"
            ],
            'ssd': [
                "1. Retirar CPU del backplane",
                "2. Quitar 3 tornillos del soporte SSD (Torx T10 o Phillips #2)",
                "3. Extraer SSD vieja del conector",
                "4. Insertar nueva SSD en mismo conector",
                "5. Asegurar con tornillos del soporte"
            ],
            'tarjeta_video': [
                "1. Retirar 2 tornillos de sujeción (Phillips #1)",
                "2. Levantar tarjeta en ángulo de 45° y extraer",
                "3. Para conducto: desenganchar plástico del disipador",
                "4. Reinstalar en orden inverso asegurando buen contacto"
            ]
        }
        return procedimientos.get(componente, ["Procedimiento no documentado para este componente"])

# ==================== NUEVO: SISTEMA DE INTEGRACIÓN BALLY ====================
class BallyCPUIntegrationSystem:
    def __init__(self, cpu_specialist):
        self.cpu_specialist = cpu_specialist
        self.bally_mappings = self.setup_bally_mappings()
        self.common_problems = self.setup_common_problems()
    
    def setup_bally_mappings(self):
        """Mapea problemas de máquinas Bally a soluciones de CPU-4.2.2.X"""
        return {
            # MÁQUINAS BALLY QUE USAN CPU-4.2.2.X
            'bally_alpha_pro': {
                'cpu_compatible': True,
                'cpu_model': 'CPU-4.2.2.X',
                'symptoms_mapping': {
                    'no enciende': 'no_enciende',
                    'reinicia solo': 'sobrecalentamiento', 
                    'pantalla negra': 'problemas_video',
                    'error bios': 'error_bios',
                    'sobrecalienta': 'sobrecalentamiento',
                    'no bootea': 'error_bios'
                },
                'specific_issues': [
                    "Problemas de ventilación en gabinete Alpha",
                    "Configuración BIOS específica para Alpha Pro",
                    "Comunicación con periféricos Bally"
                ]
            },
            
            'bally_alpha_2': {
                'cpu_compatible': True,
                'cpu_model': 'CPU-4.2.2.X',
                'symptoms_mapping': {
                    'no enciende': 'no_enciende',
                    'problemas video': 'problemas_video',
                    'error térmico': 'sobrecalentamiento',
                    'comunicación red': 'error_bios'
                }
            },
            
            'bally_iview': {
                'cpu_compatible': True, 
                'cpu_model': 'CPU-4.2.2.X',
                'symptoms_mapping': {
                    'display no funciona': 'problemas_video',
                    'touch no responde': 'problemas_video',
                    'comunicación falla': 'error_bios'
                }
            },
            
            # MÁQUINAS BALLY ANTIGUAS (conocimiento general)
            'bally_s9000': {
                'cpu_compatible': False,
                'platform': 'S9000 Legacy',
                'knowledge_base': 'Problemas específicos de plataforma S9000'
            }
        }
    
    def setup_common_problems(self):
        """Problemas comunes de Bally con soluciones del manual CPU"""
        return {
            'bally_alpha_pro_thermal': {
                'symptom': 'Sobrecalentamiento en Bally Alpha Pro',
                'cpu_relation': 'Códigos LED 24, 25, 26 del manual',
                'solution_steps': [
                    "1. Verificar bandeja de ventilador de CPU-4.2.2.X",
                    "2. Limpiar filtros de aire del gabinete Alpha", 
                    "3. Comprobar ventiladores adicionales del sistema",
                    "4. Verificar ambiente operativo (< 40°C)",
                    "5. Revisar disipadores de CPU y tarjeta video"
                ],
                'led_codes': ['24', '25', '26']
            },
            
            'bally_alpha_video_issues': {
                'symptom': 'Problemas de video/artefactos en Alpha',
                'cpu_relation': 'Tarjeta de video y conducto de CPU-4.2.2.X',
                'solution_steps': [
                    "1. Reinstalar tarjeta de video en CPU-4.2.2.X",
                    "2. Verificar conducto de ventilación de video",
                    "3. Comprobar cable LVDS a pantalla Bally",
                    "4. Verificar módulo BIOS de CPU",
                    "5. Probar con tarjeta de video de respuesto"
                ],
                'manual_reference': 'Páginas 31-33 manual CPU'
            },
            
            'bally_boot_issues': {
                'symptom': 'Bally no bootea o se traba en POST',
                'cpu_relation': 'Módulo BIOS y baterías de CPU-4.2.2.X', 
                'solution_steps': [
                    "1. Verificar módulo BIOS en receptáculo amarillo",
                    "2. Comprobar batería CR2032 de CPU",
                    "3. Verificar baterías AA de backup",
                    "4. Reinstalar módulo BIOS",
                    "5. Verificar LED del módulo BIOS"
                ],
                'manual_reference': 'Páginas 26, 34-35 manual CPU'
            }
        }
    
    def diagnose_bally_problem(self, maquina_bally, sintoma, contexto=""):
        """Diagnóstico especializado para máquinas Bally usando conocimiento CPU"""
        
        maquina_lower = maquina_bally.lower()
        sintoma_lower = sintoma.lower()
        
        # Buscar mapeo para esta máquina Bally
        maquina_info = None
        for bally_key, info in self.bally_mappings.items():
            if bally_key in maquina_lower or maquina_lower in bally_key:
                maquina_info = info
                break
        
        diagnostico = {
            'maquina_bally': maquina_bally,
            'sintoma': sintoma,
            'compatible_cpu': maquina_info.get('cpu_compatible', False) if maquina_info else False,
            'soluciones_cpu': [],
            'soluciones_especificas': [],
            'led_codes_relevantes': [],
            'referencias_manual': []
        }
        
        if not maquina_info:
            diagnostico['soluciones_especificas'] = [
                "⚠️ Máquina Bally no específicamente mapeada",
                "💡 Consultar documentación específica del modelo",
                "🔧 Verificar problemas comunes de plataforma Bally"
            ]
            return diagnostico
        
        # SI ES COMPATIBLE CON CPU-4.2.2.X
        if maquina_info.get('cpu_compatible'):
            # Usar el diagnóstico del especialista CPU
            cpu_diagnosis = self.cpu_specialist.diagnosticar_problema(sintoma)
            
            diagnostico['soluciones_cpu'] = cpu_diagnosis['pasos_solucion']
            diagnostico['componentes_cpu'] = cpu_diagnosis['componentes_afectados']
            
            # Agregar soluciones específicas Bally
            diagnostico['soluciones_especificas'].extend([
                f"🔧 Esta {maquina_bally} usa {maquina_info['cpu_model']}",
                "💡 Aplicar procedimientos del manual CPU-4.2.2.X",
                "🎯 Verificar integración con periféricos Bally específicos"
            ])
            
            # Buscar problemas comunes mapeados
            for problem_key, problem_info in self.common_problems.items():
                if any(keyword in sintoma_lower for keyword in problem_key.split('_')):  # Simple keyword matching
                    diagnostico['soluciones_especificas'].extend(problem_info['solution_steps'])
                    if 'led_codes' in problem_info:
                        diagnostico['led_codes_relevantes'].extend(problem_info['led_codes'])
                    if 'manual_reference' in problem_info:
                        diagnostico['referencias_manual'].append(problem_info['manual_reference'])
        
        return diagnostico

# ==================== NUEVO: SISTEMA DE CONFIGURACIÓN BALLY ====================
class BallyConfigurationSystem:
    def __init__(self):
        self.config_profiles = self.setup_config_profiles()
        self.network_guides = self.setup_network_guides()
        self.bios_settings = self.setup_bios_settings()
    
    def setup_config_profiles(self):
        """Perfiles de configuración basados en experiencia con máquinas Bally"""
        return {
            'bally_alpha_pro_network': {
                'description': 'Configuración Red Alpha Pro con CPU-4.2.2.X',
                'network_settings': {
                    'ip_mode': 'STATIC (Recomendado)',
                    'typical_ip': '192.168.1.100-200',
                    'subnet_mask': '255.255.255.0',
                    'gateway': '192.168.1.1',
                    'dns': '8.8.8.8, 8.8.4.4'
                },
                'config_steps': [
                    "1. Acceder al menú servicio (llave de técnico)",
                    "2. Navegar a: System → Network Settings", 
                    "3. Configurar IP estática fuera del rango DHCP",
                    "4. Guardar configuración y reiniciar",
                    "5. Verificar conectividad con ping"
                ],
                'troubleshooting': [
                    "🔍 Si no hay comunicación: Verificar cable Ethernet en CPU-4.2.2.X",
                    "🌐 Si IP conflict: Cambiar a IP única en la red",
                    "🔧 Si no guarda: Verificar batería CR2032 en CPU"
                ]
            },
            
            'bally_alpha_2_bios': {
                'description': 'Configuración BIOS Alpha 2',
                'bios_settings': {
                    'boot_order': 'SSD SATA0 → Network → USB',
                    'power_management': 'ACPI S3 (Suspend to RAM)',
                    'usb_legacy': 'Enabled',
                    'network_boot': 'Disabled (normal operation)'
                },
                'access_method': [
                    "Método 1: F2 durante boot (algunos modelos)",
                    "Método 2: Menú servicio → Advanced → BIOS Setup",
                    "Método 3: Comandos específicos del modelo"
                ]
            },
            
            'cpu_4_2_2_x_general': {
                'description': 'Configuración general CPU-4.2.2.X',
                'typical_settings': {
                    'operating_system': 'ArgOS 2.X (Scientific Games)',
                    'storage': '64GB SSD SATA (ubicación predeterminada SATA4)',
                    'memory': '8GB DDR3 (verificar compatibilidad)',
                    'video_output': 'Depende de tarjeta instalada'
                },
                'boot_sequence': [
                    "1. POWER ON → LED rojo (standby)",
                    "2. Botón encendido → LED azul (operación)", 
                    "3. BIOS POST → LED verde POST listo",
                    "4. Validación medios → LED azul validation",
                    "5. Carga SO → Operación normal"
                ]
            }
        }
    
    def setup_network_guides(self):
        """Guías de configuración de red basadas en experiencia"""
        return {
            'static_ip_setup': {
                'title': '📡 Configurar IP Estática',
                'steps': [
                    "**VENTAJA:** Mayor estabilidad que DHCP",
                    "**PROCEDIMIENTO:**",
                    "1. Menú Servicio → Configuración Red",
                    "2. Seleccionar 'IP Estática' vs 'DHCP'", 
                    "3. Ingresar: IP, Mascara, Gateway, DNS",
                    "4. **IP TÍPICA:** 192.168.1.150 (ajustar según red)",
                    "5. **MÁSCARA:** 255.255.255.0",
                    "6. **GATEWAY:** 192.168.1.1 (usar router local)",
                    "7. Guardar y reiniciar"
                ],
                'verification': [
                    "✅ Ping desde PC: ping 192.168.1.150",
                    "✅ Acceso remoto si está habilitado",
                    "✅ Comunicación con sistema central"
                ]
            },
            
            'dhcp_troubleshooting': {
                'title': '🔧 Problemas con DHCP',
                'issues': [
                    "**PROBLEMA:** IP cambia frecuentemente",
                    "**SOLUCIÓN:** Usar IP estática o reserva DHCP",
                    "",
                    "**PROBLEMA:** No obtiene IP",
                    "**SOLUCIÓN:** Verificar servidor DHCP en red",
                    "",
                    "**PROBLEMA:** Conflictos IP", 
                    "**SOLUCIÓN:** Reservar IP en router o cambiar a estática"
                ]
            },
            
            'sas_communication': {
                'title': '🎰 Comunicación SAS',
                'configuration': [
                    "**PROTOCOLO:** SAS 6.0x (estándar industria)",
                    "**CONFIGURACIÓN:**",
                    "- SAS Address: 01 (común para standalone)",
                    "- Game ID: Configurar según instalación", 
                    "- Communication Rate: Auto (normalmente)",
                    "",
                    "**VERIFICACIÓN:**",
                    "- Menú servicio → SAS Status",
                    "- Debería mostrar 'Connected' o similar",
                    "- Meter readings deberían transmitirse"
                ]
            }
        }
    
    def setup_bios_settings(self):
        """Configuración BIOS basada en experiencia"""
        return {
            'standard_settings': {
                'boot': {
                    'boot_order': ['SSD', 'USB', 'Network'],
                    'fast_boot': 'Disabled (para diagnóstico)',
                    'boot_delay': '0 seconds'
                },
                'power': {
                    'ac_power_recovery': 'Last State',
                    'wake_on_lan': 'Enabled (para operación remota)',
                    'suspend_mode': 'S3 (STR)'
                },
                'security': {
                    'admin_password': 'Según políticas del casino', 
                    'user_password': 'Opcional',
                    'secure_boot': 'Disabled (normalmente)'
                }
            },
            
            'recovery_procedures': {
                'bios_reset': [
                    "**RESET BIOS COMPLETO:**",
                    "1. Apagar máquina completamente",
                    "2. Desconectar alimentación 5 minutos", 
                    "3. Quitar batería CR2032 30 segundos",
                    "4. Reinstalar batería y reconectar",
                    "5. Encender - BIOS volverá a defaults"
                ],
                'boot_failure': [
                    "**SI NO BOOTEA:**",
                    "1. Verificar módulo BIOS instalado",
                    "2. Comprobar SSD en SATA4 (ubicación default)",
                    "3. Verificar LED del módulo BIOS",
                    "4. Probar con medios de recuperación"
                ]
            }
        }
    
    def get_configuration_help(self, config_type, machine_model=""):
        """Obtiene ayuda de configuración específica"""
        config_type_lower = config_type.lower()
        
        if 'red' in config_type_lower or 'network' in config_type_lower or 'ip' in config_type_lower:
            return self.network_guides['static_ip_setup']
        
        elif 'bios' in config_type_lower:
            return {
                'title': '⚙️ Configuración BIOS',
                'standard_settings': self.bios_settings['standard_settings'],
                'recovery': self.bios_settings['recovery_procedures']
            }
        
        elif 'sas' in config_type_lower:
            return self.network_guides['sas_communication']
        
        else:
            return {
                'title': '🔧 Configuración General',
                'profiles': self.config_profiles,
                'note': 'Selecciona un tipo específico de configuración'
            }

# ==================== SISTEMA DE EXPERIENCIA TÉCNICA (ORIGINAL) ====================
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

# ==================== SISTEMA DE DIAGNÓSTICO INTELIGENTE (ORIGINAL) ====================
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

# ==================== SISTEMA DE DIAGNÓSTICO MEJORADO (ORIGINAL + MEJORAS) ====================
class DiagnosticSystemEnhanced:
    def __init__(self, db):
        self.db = db
        self.diagnostic_system = DiagnosticSystem(db)
        self.technical_system = TechnicalExperienceSystem(db)
        # QUITAR LA INICIALIZACIÓN DE BALLY_INTEGRATION DEL __INIT__
    
    def get_enhanced_diagnosis(self, question, aceptador_seleccionado, contexto_adicional=""):
        """Diagnóstico que combina manuales técnicos + experiencia técnica"""
        
        # Diagnóstico técnico base (original)
        respuesta_tecnica = self.diagnostic_system.get_diagnostic_response(question, aceptador_seleccionado)
        
        # Análisis técnico basado en experiencia (original)
        insights_tecnicos = self.technical_system.get_technical_insight(question, aceptador_seleccionado)
        
        # 🆕 DETECCIÓN DE MÁQUINAS BALLY (USAR EL SISTEMA DE SESSION_STATE)
        question_lower = question.lower()
        bally_machines = ['bally alpha', 'bally alpha pro', 'bally alpha 2', 'bally iview', 'bally s9000']
        
        for bally_machine in bally_machines:
            if bally_machine in question_lower:
                # Usar el sistema de integración Bally desde session_state
                if 'bally_integration' in st.session_state:
                    bally_diagnosis = st.session_state.bally_integration.diagnose_bally_problem(
                        bally_machine, 
                        question,
                        contexto_adicional
                    )
                    
                    respuesta_tecnica['diagnostico_bally'] = bally_diagnosis
                    respuesta_tecnica['nivel_confianza'] = "🎯 ALTA - Diagnóstico Bally con conocimiento CPU-4.2.2.X"
                break
        
        # 🆕 DETECCIÓN DE CONFIGURACIÓN
        if any(keyword in question_lower for keyword in ['configurar', 'ip', 'red', 'bios', 'setup', 'configuración']):
            if 'config_system' in st.session_state:
                config_help = st.session_state.config_system.get_configuration_help(question)
                respuesta_tecnica['configuracion_ayuda'] = config_help
        
        # Combinar respuestas (original)
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

# ==================== BASE DE DATOS COMPLETA Y ACTUALIZADA (ORIGINAL + MEJORAS) ====================
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
            "Bally Pro Wave": {"fabricante": "Bally", "año": 2018, "plataforma": "Pro Series"},
            
            # 🆕 AGREGAR MÁQUINAS CON CPU-4.2.2.X
            "Scientific Games Twinstar Vertical": {
                "fabricante": "Scientific Games", 
                "año": 2017,
                "plataforma": "CPU-4.2.2.X",
                "cpu_especifica": True,
                "numero_parte": "56-T14335T",
                "modelo_cpu": "CPU-4.2.2.X (1458954)",
                "manual_servicio": "1489211 [A]"
            },
            
            "Scientific Games CPU-4.2.2.X Standalone": {
                "fabricante": "Scientific Games", 
                "año": 2017,
                "plataforma": "CPU-4.2.2.X", 
                "cpu_especifica": True,
                "numero_parte": "1458954",
                "descripcion": "Subsistema de control genérico para múltiples máquinas"
            },
            
            "Bally Alpha Pro con CPU-4.2.2.X": {
                "fabricante": "Bally/Scientific Games",
                "año": 2017,
                "plataforma": "CPU-4.2.2.X",
                "cpu_especifica": True,
                "compatible": True
            },
            
            "Bally iVIEW DM con CPU-4.2.2.X": {
                "fabricante": "Bally/Scientific Games", 
                "año": 2017,
                "plataforma": "CPU-4.2.2.X",
                "cpu_especifica": True,
                "compatible": True
            }
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
            {"nombre": "🛠️ Software Diagnóstico", "stock": 1, "categoria": "Herramientas", "min_stock": 1},
            
            # 🆕 AGREGAR NUEVOS COMPONENTES CPU-4.2.2.X
            {"nombre": "🔋 CPU-4.2.2.X Assembly", "stock": 2, "categoria": "CPU", "min_stock": 1},
            {"nombre": "🔋 Módulo BIOS CPU-4.2.2.X", "stock": 3, "categoria": "CPU", "min_stock": 2},
            {"nombre": "🔋 Batería CR2032", "stock": 10, "categoria": "Baterías", "min_stock": 5},
            {"nombre": "🔋 Baterías Litio AA", "stock": 8, "categoria": "Baterías", "min_stock": 4},
            {"nombre": "🔋 SSD 64GB SATA CPU-4.2.2.X", "stock": 3, "categoria": "Almacenamiento", "min_stock": 2},
            {"nombre": "🔋 Placa Posterior CPU-4.2.2.X", "stock": 2, "categoria": "CPU", "min_stock": 1}
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
            "update fallido": {"solucion": "Restaurar backup y repetir update con conexión estable"},
            
            # 🆕 AGREGAR PROBLEMAS ESPECÍFICOS CPU-4.2.2.X
            "error led 1c cpu": {"solucion": "Reemplazar CPU - fallo circuito alimentación"},
            "error led 24 cpu": {"solucion": "Verificar ventilación y disipadores térmicos"},
            "error led 25 cpu": {"solucion": "Limpiar ventiladores y verificar temperatura ambiente"},
            "cpu no bootea": {"solucion": "Verificar módulo BIOS y batería CR2032"},
            "sobrecalentamiento cpu": {"solucion": "Limpiar bandeja ventilador y verificar flujo de aire"}
        }
        
        self.ruletas = {}
        self.reparaciones = []

# ==================== NUEVO: SISTEMA DE REFERENCIA TÉCNICA (ORIGINAL) ====================
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

# ==================== NUEVO: SISTEMA DE BÚSQUEDA INTELIGENTE (ORIGINAL) ====================
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

# ==================== NUEVO: CALCULADORA TÉCNICA (ORIGINAL) ====================
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

# ==================== CHECKLISTS DE DIAGNÓSTICO (ORIGINAL) ====================
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

# ==================== INICIALIZACIÓN CORREGIDA (ORDEN CORREGIDO) ====================
# PRIMERO: Base de datos
if 'db' not in st.session_state:
    st.session_state.db = CasinoProCompleteDB()

# SEGUNDO: NUEVOS SISTEMAS CPU-4.2.2.X (DEBEN IR PRIMERO)
if 'cpu_specialist' not in st.session_state:
    st.session_state.cpu_specialist = CPU422XSpecialist()

if 'bally_integration' not in st.session_state:
    st.session_state.bally_integration = BallyCPUIntegrationSystem(st.session_state.cpu_specialist)

if 'config_system' not in st.session_state:
    st.session_state.config_system = BallyConfigurationSystem()

# TERCERO: Sistemas que dependen de la DB (AHORA PUEDEN USAR LOS NUEVOS SISTEMAS)
if 'enhanced_diagnostic' not in st.session_state:
    st.session_state.enhanced_diagnostic = DiagnosticSystemEnhanced(st.session_state.db)

# CUARTO: Nuevos sistemas ORIGINALES
if 'tech_reference' not in st.session_state:
    st.session_state.tech_reference = TechnicalReferenceSystem()

if 'smart_search' not in st.session_state:
    st.session_state.smart_search = SmartSearchSystem(st.session_state.tech_reference)

if 'tech_calculator' not in st.session_state:
    st.session_state.tech_calculator = TechCalculator()

if 'technical_notes' not in st.session_state:
    st.session_state.technical_notes = []

# ==================== SISTEMA DE NAVEGACIÓN (ORIGINAL + NUEVAS OPCIONES) ====================
if 'current_menu' not in st.session_state:
    st.session_state.current_menu = "🏠 INICIO"

def set_menu(menu_option):
    st.session_state.current_menu = menu_option
    st.rerun()

# ==================== INTERFAZ PRINCIPAL ACTUALIZADA ====================
st.title("🎰 CASINOPRO - SISTEMA EXPERTO TÉCNICO")
st.markdown("**✅ Datos Técnicos + 🤖 Diagnóstico IA + 👨‍🔧 Experiencia Técnica Especializada**")
st.markdown("---")

# MENÚ PRINCIPAL ACTUALIZADO CON NUEVAS OPCIONES
menu_options = [
    "🏠 INICIO", 
    "🤖 DIAGNÓSTICO INTELIGENTE MEJORADO",
    "👨‍🔧 BASE DE CONOCIMIENTO TÉCNICO",
    "🔧 INFORMACIÓN TÉCNICA ESPECÍFICA",
    "💻 ESPECIALISTA CPU-4.2.2.X",  # 🆕 NUEVA OPCIÓN
    "⚙️ CONFIGURACIÓN BALLY/CPU",   # 🆕 NUEVA OPCIÓN
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

# ==================== DIAGNÓSTICO INTELIGENTE (COMPLETO ORIGINAL + MEJORAS) ====================
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
                
                # 🆕 DETECCIÓN DE MÁQUINAS BALLY
                if 'diagnostico_bally' in respuesta and respuesta['diagnostico_bally']:
                    bally_diag = respuesta['diagnostico_bally']
                    
                    st.markdown("### 🎰 **Diagnóstico Específico Bally**")
                    
                    if bally_diag['compatible_cpu']:
                        st.success("✅ **Compatibilidad confirmada:** Esta máquina Bally usa CPU-4.2.2.X")
                        
                        if bally_diag['soluciones_cpu']:
                            st.markdown("#### 🔧 Soluciones desde Manual CPU-4.2.2.X")
                            for solucion in bally_diag['soluciones_cpu']:
                                st.write(solucion)
                        
                        if bally_diag['soluciones_especificas']:
                            st.markdown("#### 🎯 Soluciones Específicas Bally")
                            for solucion in bally_diag['soluciones_especificas']:
                                st.write(solucion)
                    
                    else:
                        st.warning("⚠️ Máquina Bally no específicamente mapeada - usar conocimiento general")
                        for solucion in bally_diag['soluciones_especificas']:
                            st.write(solucion)
                
                # 🆕 DETECCIÓN DE CONFIGURACIÓN
                if 'configuracion_ayuda' in respuesta and respuesta['configuracion_ayuda']:
                    config_help = respuesta['configuracion_ayuda']
                    
                    st.markdown("### ⚙️ **Ayuda de Configuración**")
                    st.markdown(f"#### {config_help['title']}")
                    
                    if 'steps' in config_help:
                        for step in config_help['steps']:
                            if step.startswith("**"):
                                st.markdown(step)
                            else:
                                st.write(step)
                    
                    if 'verification' in config_help:
                        st.markdown("#### ✅ Verificación")
                        for item in config_help['verification']:
                            st.write(item)
                
                # PERSPECTIVA TÉCNICA (ORIGINAL)
                if 'perspectiva_tecnica' in respuesta and respuesta['perspectiva_tecnica']:
                    st.markdown("### 👨‍🔧🔧 **Perspectiva Técnica Especializada**")
                    for insight in respuesta['perspectiva_tecnica']:
                        if "**" in insight:
                            st.markdown(insight)
                        else:
                            st.write(f"• {insight}")
                
                # RESPUESTA TÉCNICA (ORIGINAL)
                st.markdown("### 📋 **Información Técnica**")
                st.markdown(respuesta['respuesta_tecnica'])
                
                # Pasos de solución (ORIGINAL)
                if respuesta['pasos_solucion']:
                    st.markdown("### 🔧 **Pasos para la Solución**")
                    for paso in respuesta['pasos_solucion']:
                        st.write(paso)
                
                # Códigos de error (ORIGINAL)
                if respuesta['codigos_error_relevantes']:
                    st.markdown("### ⚠️ **Códigos de Error Relevantes**")
                    for error, desc in respuesta['codigos_error_relevantes'].items():
                        st.write(f"**{error}**: {desc}")
                
                # Historial de consulta
                st.markdown("---")
                st.caption(f"🕐 Consulta técnica: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
        else:
            st.warning("⚠️ **Escribí una pregunta o descripción del problema**")

# ==================== 🆕 NUEVA SECCIÓN: ESPECIALISTA CPU-4.2.2.X ====================
elif st.session_state.current_menu == "💻 ESPECIALISTA CPU-4.2.2.X":
    st.header("💻 ESPECIALISTA CPU-4.2.2.X - Scientific Games")
    st.success("**🔧 Conocimiento técnico específico del manual 1458954**")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔍 Diagnóstico", 
        "📊 Especificaciones", 
        "⚙️ Procedimientos",
        "⚠️ Códigos Error"
    ])
    
    with tab1:
        st.subheader("🔍 Diagnóstico de Problemas")
        
        sintoma = st.text_input(
            "Describí el problema:",
            placeholder="Ej: CPU no enciende, sobrecalienta, error de video...",
            key="cpu_sintoma"
        )
        
        codigo_error = st.text_input(
            "Código de error LED (opcional):",
            placeholder="Ej: 1C, 24, 25, 40...",
            key="cpu_codigo_error",
            max_chars=3
        )
        
        if st.button("🔧 EJECUTAR DIAGNÓSTICO CPU", type="primary"):
            if sintoma.strip():
                diagnostico = st.session_state.cpu_specialist.diagnosticar_problema(sintoma, codigo_error.upper() if codigo_error else None)
                
                st.markdown("---")
                st.subheader("🎯 Resultado del Diagnóstico")
                
                # Mostrar prioridad
                color_prioridad = "🔴" if diagnostico['prioridad'] == 'ALTA' else "🟡"
                st.write(f"{color_prioridad} **Prioridad:** {diagnostico['prioridad']}")
                
                # Posibles causas
                if diagnostico['posibles_causas']:
                    st.markdown("### 📋 Posibles Causas")
                    for causa in diagnostico['posibles_causas']:
                        st.write(f"• {causa}")
                
                # Pasos de solución
                if diagnostico['pasos_solucion']:
                    st.markdown("### 🔧 Pasos para Solución")
                    for paso in diagnostico['pasos_solucion']:
                        st.write(paso)
                
                # Componentes afectados
                if diagnostico['componentes_afectados']:
                    st.markdown("### 🔩 Componentes Involucrados")
                    for componente in diagnostico['componentes_afectados']:
                        st.write(f"• {componente}")
            else:
                st.warning("⚠️ Por favor, describí el problema")
    
    with tab2:
        st.subheader("📊 Especificaciones Técnicas")
        especificaciones = st.session_state.cpu_specialist.cpu_data['especificaciones_generales']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📋 Información General")
            st.write(f"**Modelo:** {especificaciones['modelo']}")
            st.write(f"**Número Parte:** {especificaciones['numero_parte']}")
            st.write(f"**Fabricante:** {especificaciones['fabricante']}")
            st.write(f"**Voltaje:** {especificaciones['voltaje_operativo']}")
            
        with col2:
            st.markdown("### 🌡️ Condiciones Operativas")
            st.write(f"**Temperatura:** {especificaciones['temperatura_operacion']}")
            st.write(f"**Humedad Máx:** {especificaciones['humedad_maxima']}")
        
        st.markdown("### 🧩 Componentes Principales")
        for componente in especificaciones['componentes_principales']:
            st.write(f"• {componente}")
            
        st.markdown("### 🎰 Máquinas Compatibles")
        for maquina in especificaciones['maquinas_compatibles']:
            st.write(f"• {maquina}")
    
    with tab3:
        st.subheader("⚙️ Procedimientos de Reemplazo")
        
        componente = st.selectbox(
            "Seleccioná componente a reemplazar:",
            ["bateria_cr2032", "baterias_aa", "modulo_bios", "ssd", "tarjeta_video"],
            format_func=lambda x: x.replace('_', ' ').title()
        )
        
        if componente:
            procedimiento = st.session_state.cpu_specialist.get_procedimiento_reemplazo(componente)
            
            st.markdown(f"### 🔧 Procedimiento: {componente.replace('_', ' ').title()}")
            for i, paso in enumerate(procedimiento, 1):
                st.write(f"{i}. {paso}")
    
    with tab4:
        st.subheader("⚠️ Códigos de Error LED")
        
        for codigo, info in st.session_state.cpu_specialist.led_codes.items():
            with st.expander(f"🚨 Código {codigo}: {info['nombre']}"):
                st.write(f"**Descripción:** {info['descripcion']}")
                st.write(f"**Solución:** {info['solucion']}")

# ==================== 🆕 NUEVA SECCIÓN: CONFIGURACIÓN BALLY/CPU ====================
elif st.session_state.current_menu == "⚙️ CONFIGURACIÓN BALLY/CPU":
    st.header("⚙️ Configuración Bally/CPU-4.2.2.X")
    st.info("**💡 Guías de configuración basadas en experiencia técnica**")
    
    tab1, tab2, tab3 = st.tabs(["📡 Red", "⚙️ BIOS", "🎰 SAS"])
    
    with tab1:
        st.subheader("📡 Configuración de Red")
        
        config_type = st.radio(
            "Seleccioná tipo de configuración:",
            ["IP Estática", "Problemas DHCP", "Verificación Conectividad"],
            key="network_config"
        )
        
        if st.button("🔄 Obtener Guía Configuración", key="btn_network_guide"):
            guide = st.session_state.config_system.get_configuration_help(config_type)
            
            st.markdown(f"### {guide['title']}")
            
            if 'steps' in guide:
                for step in guide['steps']:
                    if step.startswith("**"):
                        st.markdown(step)
                    else:
                        st.write(step)
            
            if 'verification' in guide:
                st.markdown("### ✅ Verificación")
                for item in guide['verification']:
                    st.write(item)
    
    with tab2:
        st.subheader("⚙️ Configuración BIOS")
        
        if st.button("📋 Mostrar Configuración BIOS Estándar", key="btn_bios"):
            bios_info = st.session_state.config_system.get_configuration_help("bios")
            
            st.markdown("### 🏗️ Configuración Estándar")
            for category, settings in bios_info['standard_settings'].items():
                st.markdown(f"#### {category.upper()}")
                for key, value in settings.items():
                    st.write(f"**{key}:** {value}")
            
            st.markdown("### 🔄 Procedimientos de Recovery")
            for procedure, steps in bios_info['recovery'].items():
                st.markdown(f"#### {procedure}")
                for step in steps:
                    if step.startswith("**"):
                        st.markdown(step)
                    else:
                        st.write(step)
    
    with tab3:
        st.subheader("🎰 Comunicación SAS")
        
        if st.button("📡 Mostrar Configuración SAS", key="btn_sas"):
            sas_info = st.session_state.config_system.get_configuration_help("sas")
            
            st.markdown(f"### {sas_info['title']}")
            for item in sas_info['configuration']:
                if item.startswith("**"):
                    st.markdown(item)
                else:
                    st.write(item)

# ==================== SECCIÓN: INFORMACIÓN TÉCNICA ESPECÍFICA (ORIGINAL) ====================
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

# ==================== SECCIÓN: BASE DE CONOCIMIENTO TÉCNICO (ORIGINAL) ====================
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

# ==================== SECCIÓN: MANUALES ACEPTADORES (ORIGINAL) ====================
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

# ==================== SECCIÓN: MÁQUINAS REGISTRADAS (ORIGINAL) ====================
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

# ==================== SECCIÓN: INVENTARIO COMPLETO (ORIGINAL) ====================
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
st.caption("🎰 **CasinoPro Expert v8.0** - Datos Técnicos + Diagnóstico IA + CPU-4.2.2.X Specialist + Configuración Bally")
st.caption("🔧 **Sistema completo con conocimiento técnico integrado del manual 1458954**")

# Botón para volver al inicio en todas las páginas (excepto inicio)
if st.session_state.current_menu != "🏠 INICIO":
    if st.button("🏠 Volver al Inicio", use_container_width=True):
        set_menu("🏠 INICIO")
