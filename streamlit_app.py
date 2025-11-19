import json
import os
from difflib import SequenceMatcher

print("=" * 70)
print("IA ASISTENTE COMPLETO - CON TODO INTEGRADO")
print("=" * 70)

# ==================== MÓDULO DE RULETAS BCM ====================
class BCMRouletteRecommendations:
    def __init__(self):
        self.roulettes = self.load_bcm_roulettes()
    
    def load_bcm_roulettes(self):
        return {
            # ========== RULETAS ELECTRÓNICAS BCM ==========
            "BCM ARISTOCRAT RW-2000": {
                "tipo": "Ruleta Electrónica Profesional",
                "fabricante": "BCM (Bally Manufacturing)",
                "mercado": "Argentina - Casinos Establecidos",
                "caracteristicas": [
                    "Rueda mecánica de precisión suiza",
                    "Sistema de apuestas digital integrado",
                    "Display LCD táctil de 42 pulgadas",
                    "Software de gestión en español",
                    "Conectividad para jackpot progresivo"
                ],
                "ventajas_argentina": [
                    "Alta confiabilidad en ambiente casino",
                    "Fácil mantenimiento y repuestos disponibles",
                    "Acepta múltiples denominaciones en pesos",
                    "Certificado por entidades regulatorias argentinas"
                ],
                "especificaciones_tecnicas": {
                    "voltaje": "220V AC 50Hz",
                    "comunicacion": "TCP/IP, RS-485, USB",
                    "fichas_aceptadas": "Pesos ARS: $0.50, $1, $5, $10, $25, $100",
                    "dimensiones": "180cm x 120cm x 90cm",
                    "peso": "250 kg",
                    "certificaciones": "INTI, Lotería de Santa Fe"
                },
                "conectores_principales": {
                    "J1": "Alimentación principal 220V",
                    "J2": "Comunicación datos casino",
                    "J3": "Sensores de bola y rueda", 
                    "J4": "Sistema de apuestas",
                    "J5": "Display y interface"
                },
                "sensores_incluidos": [
                    "Sensores ópticos de posición de bola",
                    "Encoders de posición de rueda",
                    "Sensores de fichas en mesa",
                    "Detectores de movimiento"
                ],
                "codigos_error_comunes": {
                    "BCM-001": "Error sensor de bola - Limpiar sensores ópticos",
                    "BCM-002": "Fallo encoder rueda - Recalibrar encoder",
                    "BCM-003": "Comunicación display - Verificar cable LVDS",
                    "BCM-004": "Sistema apuestas offline - Reiniciar módulo APM"
                },
                "mantenimiento_recomendado": [
                    "Diario: Limpieza de sensores ópticos",
                    "Semanal: Verificación de calibración",
                    "Mensual: Lubricación de mecanismos",
                    "Trimestral: Calibración completa"
                ],
                "problemas_comunes": [
                    "BCM-001 Error: Limpiar sensores de bola con alcohol isopropílico",
                    "Deriva calibración: Ejecutar utilidad de calibración BCM",
                    "Fichas no detectadas: Ajustar sensores de mesa",
                    "Display parpadea: Verificar fuente de poder +12V"
                ],
                "precio_estimado": "USD 18,000 - 30,000",
                "disponibilidad_argentina": "4-6 semanas - Importación directa"
            },

            "BCM iDECK ROULETTE": {
                "tipo": "Ruleta con Sistema de Apuestas Avanzado",
                "fabricante": "BCM (Bally Manufacturing)",
                "mercado": "Argentina - High Limit",
                "caracteristicas": [
                    "Sistema iDeck con reconocimiento táctil",
                    "Pantalla multi-touch de 55 pulgadas",
                    "Gestión inteligente de límites de apuesta",
                    "Análisis de comportamiento de jugadores",
                    "Integración con sistema de vigilancia"
                ],
                "ventajas_argentina": [
                    "Ideal para salones VIP argentinos",
                    "Sistema de seguridad reforzado",
                    "Reportes automáticos para AFIP",
                    "Compatibilidad con moneda local"
                ],
                "especificaciones_tecnicas": {
                    "voltaje": "220V AC ±10%",
                    "comunicacion": "Ethernet Gigabit, Fibra óptica",
                    "apuestas_minimas": "$10 ARS",
                    "apuestas_maximas": "$10,000 ARS", 
                    "capacidad_jugadores": "8 posiciones"
                },
                "configuracion_argentina": [
                    "Denominaciones en pesos argentinos",
                    "Impuestos locales configurados",
                    "Idioma: Español argentino",
                    "Horarios según regulación local"
                ],
                "mantenimiento_especializado": [
                    "Calibración diaria de sensores táctiles",
                    "Backup nocturno de datos de juego",
                    "Actualización semanal de software",
                    "Auditoría mensual de seguridad"
                ]
            },

            "BCM COMPACT ROULETTE": {
                "tipo": "Ruleta Compacta para Espacios Reducidos",
                "fabricante": "BCM (Bally Manufacturing)", 
                "mercado": "Argentina - Casinos Medianos",
                "caracteristicas": [
                    "Diseño compacto para espacios limitados",
                    "Sistema de apuestas simplificado",
                    "Bajo consumo energético",
                    "Fácil transporte e instalación"
                ],
                "ventajas_argentina": [
                    "Ideal para casinos provinciales",
                    "Bajo costo de operación",
                    "Fácil mantenimiento local",
                    "Certificación nacional rápida"
                ],
                "especificaciones_tecnicas": {
                    "voltaje": "220V AC",
                    "dimensiones": "150cm x 100cm x 80cm",
                    "peso": "180 kg",
                    "consumo": "450W máximo"
                }
            }
        }
    
    def get_roulette(self, model):
        return self.roulettes.get(model, None)
    
    def list_models(self):
        return list(self.roulettes.keys())
    
    def get_roulettes_by_market(self, market):
        return {model: data for model, data in self.roulettes.items() 
                if data.get('mercado', '').lower() == market.lower()}

# ==================== MÓDULO DE MANUALES DE ACEPTADORES ====================
class BillAcceptorManuals:
    def __init__(self):
        self.manuals = self.load_manuals()
    
    def load_manuals(self):
        return {
            # ========== MEI SCN66 ADVANCE SERIES ==========
            "MEI SCN66 Advance": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador de Billetes de Alta Seguridad",
                "voltaje": "+24V DC ±5% (regulado crítico)",
                "consumo": "3.5A máximo durante validación intensiva",
                "comunicacion": "RS-232, MDB v4.0, USB 3.0, Ethernet 1Gbps, RS-485",
                "billetes_aceptados": "MXN: Todas denominaciones + USD: $1-$100 + EUR: €5-€500 + Billetes de alta seguridad",
                "conectores": [
                    "CN1: 20-pin - Principal de alta densidad",
                    "CN2: 8-pin - Comunicaciones avanzadas",
                    "CN3: 6-pin - Alimentación con supervisión",
                    "CN4: 4-pin - Sensores de seguridad",
                    "CN5: 2-pin - Tierra de blindaje"
                ],
                "pines_principal": {
                    "1": "+24V DC Regulado",
                    "2": "GND Power",
                    "3": "MDB Data+ (Diferencial)",
                    "4": "MDB Data- (Diferencial)", 
                    "5": "MDB Clock+",
                    "6": "MDB Clock-",
                    "7": "RS-232 TX",
                    "8": "RS-232 RX",
                    "9": "RS-232 RTS",
                    "10": "RS-232 CTS",
                    "11": "USB 3.0 D+",
                    "12": "USB 3.0 D-",
                    "13": "Ethernet TX+",
                    "14": "Ethernet TX-", 
                    "15": "Ethernet RX+",
                    "16": "Ethernet RX-",
                    "17": "RS-485 A",
                    "18": "RS-485 B",
                    "19": "Security Sensor In",
                    "20": "Security Sensor Out"
                },
                "sensores_avanzados": [
                    "Espectrómetro UV/Visible de alta resolución",
                    "Sensores magnéticos de 16 canales",
                    "Cámara CMOS de 5MP para análisis de imagen",
                    "Sensores IR multiespectral (4 longitudes de onda)",
                    "Detectores de metalización y hologramas",
                    "Sensores de grosor y densidad con precisión micrométrica",
                    "Sistema de detección de billetes superpuestos"
                ],
                "codigos_error_avanzados": {
                    "SCN-001": "Spectrometer Calibration Lost - Calibración espectrómetro perdida",
                    "SCN-002": "Magnetic Sensor Array Failure - Fallo array sensores magnéticos",
                    "SCN-003": "CMOS Camera Module Fault - Fallo módulo cámara CMOS",
                    "SCN-004": "IR Multi-Spectral Error - Error IR multiespectral", 
                    "SCN-005": "Security Feature Mismatch - Discrepancia características seguridad",
                    "SCN-006": "Thickness Sensor Drift - Deriva sensor grosor",
                    "SCN-007": "Superposition Detection Fault - Fallo detección superposición",
                    "SCN-008": "Advanced Encryption Failure - Fallo encriptación avanzada",
                    "SCN-009": "Real-time Clock Battery - Batería RTC baja",
                    "SCN-010": "Environmental Sensor Error - Error sensores ambientales"
                },
                "calibracion_avanzada": [
                    "1. Ejecutar MEI SCN66 Advanced Diagnostic Suite",
                    "2. Conectar patrón de calibración NIST-traceable",
                    "3. Calibrar espectrómetro con fuentes de referencia UV/Vis",
                    "4. Ajustar sensores magnéticos con billetes de calibración certificados",
                    "5. Alinear cámara CMOS usando patrón de alineación óptica",
                    "6. Configurar thresholds de seguridad por denominación y divisa",
                    "7. Realizar test de estrés con billetes límite",
                    "8. Generar certificado de calibración digital firmado"
                ],
                "mantenimiento_especializado": [
                    "Cada 8 horas: Auto-calibración espectrómetro",
                    "Diario: Limpieza óptica con kit MEI profesional",
                    "Semanal: Verificación sensores magnéticos",
                    "Quincenal: Actualización base datos seguridad global",
                    "Mensual: Calibración completa con equipos certificados",
                    "Trimestral: Reemplazo filtros ópticos y revisión completa"
                ],
                "caracteristicas_seguridad": [
                    "Detección de falsificaciones avanzadas (superdólares)",
                    "Análisis de tintas magnéticas de alta frecuencia",
                    "Verificación de hologramas 3D y elementos cambiantes",
                    "Detección de billetes lavados químicamente",
                    "Análisis de fibras de seguridad y marcas de agua",
                    "Protección contra ataques de emulación"
                ],
                "problemas_comunes_avanzados": [
                    "SCN-001 Error: Ejecutar recalibración espectrómetro completa",
                    "SCN-005 Error: Actualizar base datos características seguridad",
                    "Falsos rechazos: Ajustar thresholds de confianza por divisa",
                    "Comunicación Ethernet: Verificar configuración VLAN segura",
                    "Deriva calibración: Verificar condiciones ambientales (temp/hum)"
                ]
            },

            "MEI SCN66 Standard": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador de Billetes de Seguridad Estándar", 
                "voltaje": "+24V DC ±10%",
                "consumo": "3.0A máximo",
                "comunicacion": "RS-232, MDB v3.0, USB 2.0",
                "billetes_aceptados": "MXN: $20-$1000 + USD: $1-$50 + EUR: €5-€200",
                "conectores": [
                    "J1: 16-pin - Principal estándar",
                    "J2: 4-pin - Alimentación",
                    "J3: 6-pin - Opciones avanzadas"
                ],
                "pines_principal": {
                    "1": "+24V DC",
                    "2": "GND",
                    "3": "MDB Data",
                    "4": "MDB Clock", 
                    "5": "RS-232 TX",
                    "6": "RS-232 RX",
                    "7": "USB D+",
                    "8": "USB D-",
                    "9": "Accept Signal",
                    "10": "Reject Signal",
                    "11": "Stacker Full",
                    "12": "Validator Enable", 
                    "13": "Bill Present",
                    "14": "Security Status",
                    "15": "Diagnostic",
                    "16": "Auxiliary Power"
                },
                "sensores_estandar": [
                    "Sensores UV estándar",
                    "Sensores magnéticos de 8 canales", 
                    "Sensores IR duales",
                    "Sensores ópticos de alta resolución",
                    "Detección de grosor básica"
                ],
                "codigos_error_estandar": {
                    "SCN-101": "Standard Sensor Calibration - Calibración sensores estándar",
                    "SCN-102": "Magnetic Head Basic Fault - Fallo cabezal magnético básico",
                    "SCN-103": "UV Sensor Standard Error - Error sensor UV estándar",
                    "SCN-104": "IR Sensor Pair Mismatch - Discrepancia par sensores IR",
                    "SCN-105": "Basic Security Check Fail - Fallo chequeo seguridad básico"
                },
                "calibracion_estandar": [
                    "1. Usar MEI SCN66 Configuration Tool",
                    "2. Insertar billetes de calibración MEI oficiales",
                    "3. Ajustar sensores UV, magnéticos e IR",
                    "4. Configurar parámetros de seguridad básicos",
                    "5. Validar con billetes de prueba"
                ],
                "problemas_comunes_estandar": [
                    "SCN-101 Error: Ejecutar calibración estándar",
                    "SCN-104 Error: Re-alinear sensores IR",
                    "Rechazo constante: Verificar condiciones ambientales"
                ]
            },

            # ========== MEI CASHFLOW SERIES ==========
            "MEI CashFlow 7000": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador de Billetes CashFlow Series",
                "voltaje": "+24V DC ±10%",
                "consumo": "2.8A máximo durante aceptación",
                "comunicacion": "RS-232, MDB, USB, Ethernet",
                "billetes_aceptados": "MXN: $20, $50, $100, $200, $500, $1000 | USD: $1, $5, $10, $20, $50, $100",
                "conectores": [
                    "J1: 16-pin - Alimentación y datos principales",
                    "J2: 8-pin - Ethernet y opciones avanzadas", 
                    "J3: 4-pin - Entrada +24V con protección"
                ],
                "pines_principal": {
                    "1": "+24V DC",
                    "2": "GND",
                    "3": "MDB Data",
                    "4": "MDB Clock",
                    "5": "RS-232 TX",
                    "6": "RS-232 RX",
                    "7": "Ethernet TX+",
                    "8": "Ethernet TX-",
                    "9": "Ethernet RX+", 
                    "10": "Ethernet RX-",
                    "11": "USB D+",
                    "12": "USB D-",
                    "13": "Bill Accept",
                    "14": "Stacker Full",
                    "15": "Validator Enable",
                    "16": "Diagnostic LED"
                },
                "codigos_error": {
                    "CF-01": "CashFlow Sensor Error - Error sensores principales",
                    "CF-02": "Transport Mechanism Fault - Fallo mecanismo transporte",
                    "CF-03": "Magnetic Sensor Error - Error sensor magnético",
                    "CF-04": "Optical Path Blocked - Ruta óptica bloqueada",
                    "CF-05": "Flash Memory Error - Error memoria flash"
                },
                "calibracion": [
                    "1. Acceder al modo CashFlow (botón diagnóstico + power)",
                    "2. Seleccionar 'Auto Calibration' en menú LCD",
                    "3. Insertar billetes de referencia en orden denominación",
                    "4. Sistema auto-ajusta sensores magnéticos y ópticos",
                    "5. Validar con billetes de diferentes condiciones"
                ],
                "mantenimiento": [
                    "Diario: Limpieza sensores ópticos con kit MEI oficial",
                    "Semanal: Verificación rodillos transporte",
                    "Mensual: Actualización firmware via Ethernet"
                ],
                "problemas_comunes": [
                    "CF-01 Error: Limpiar cabezal de validación completo",
                    "CF-04 Error: Verificar obstrucciones en ruta óptica",
                    "Rechazo alto USD: Configurar sensibilidad para divisa"
                ]
            },

            "MEI CashFlow 6000": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador de Billetes Mid-Range", 
                "voltaje": "+24V DC ±10%",
                "consumo": "2.5A máximo",
                "comunicacion": "RS-232, MDB, USB",
                "billetes_aceptados": "MXN: $20, $50, $100, $200, $500 | USD: $1, $5, $10, $20",
                "conectores": [
                    "J1: 14-pin - Principal power y data",
                    "J2: 4-pin - Stacker y funciones",
                    "J3: 3-pin - Alimentación protegida"
                ],
                "pines_principal": {
                    "1": "+24V DC",
                    "2": "GND", 
                    "3": "MDB Data",
                    "4": "MDB Clock",
                    "5": "RS-232 TX",
                    "6": "RS-232 RX",
                    "7": "USB D+",
                    "8": "USB D-",
                    "9": "Accept Pulse",
                    "10": "Reject Signal", 
                    "11": "Stacker Status",
                    "12": "Enable/Disable",
                    "13": "Bill Present",
                    "14": "Security Sensor"
                },
                "codigos_error": {
                    "E20": "Magnetic Head Error - Cabezal magnético",
                    "E21": "UV Sensor Failure - Sensor UV",
                    "E22": "IR Sensor Array Error - Array sensores IR",
                    "E23": "Transport Timeout - Timeout transporte"
                },
                "calibracion": [
                    "1. Entrar modo servicio (botón lateral 5 segundos)",
                    "2. Usar utilidad MEI CF-6000 Calibration Tool",
                    "3. Seguir calibration wizard paso a paso",
                    "4. Ajustar thresholds por denominación"
                ],
                "mantenimiento": [
                    "Cada 10,000 billetes: Limpieza completa",
                    "Mensual: Verificación sensores UV/IR",
                    "Bimestral: Lubricación guías (solo lubricante MEI)"
                ],
                "problemas_comunes": [
                    "E20 Error: Recalibrar cabezal magnético",
                    "E21 Error: Limpiar sensores UV con alcohol especial",
                    "Atascos frecuentes: Revisar tensión rodillos"
                ]
            },

            # ========== JCM MODERN SERIES ==========
            "JCM iVizion": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador Inteligente con Visión Artificial",
                "voltaje": "+24V DC ±10%",
                "consumo": "3.2A máximo (picos durante análisis)",
                "comunicacion": "RS-232, MDB, Ethernet, WiFi, Bluetooth",
                "billetes_aceptados": "Múltiples divisas + Billetes dañados/arrugados + Detección falsificaciones avanzada",
                "conectores": [
                    "CN1: 18-pin - Principal inteligente",
                    "CN2: 8-pin - Red y comunicaciones",
                    "CN3: 4-pin - Alimentación con filtro",
                    "CN4: 6-pin - Cámara y sensores avanzados"
                ],
                "pines_principal": {
                    "1": "+24V DC",
                    "2": "GND",
                    "3": "MDB Data",
                    "4": "MDB Clock",
                    "5": "RS-232 TX",
                    "6": "RS-232 RX", 
                    "7": "Ethernet TX+",
                    "8": "Ethernet TX-",
                    "9": "Ethernet RX+",
                    "10": "Ethernet RX-",
                    "11": "WiFi Antenna",
                    "12": "Bluetooth Data",
                    "13": "Camera Data+",
                    "14": "Camera Data-", 
                    "15": "AI Processor Sync",
                    "16": "Validation Result",
                    "17": "Security Encryption",
                    "18": "Diagnostic Bus"
                },
                "codigos_error": {
                    "IV-100": "AI Vision System Failure - Fallo sistema visión",
                    "IV-101": "Neural Network Error - Error red neuronal",
                    "IV-102": "Camera Module Fault - Fallo módulo cámara",
                    "IV-103": "Pattern Recognition Error - Error reconocimiento",
                    "IV-104": "Database Corruption - Corrupción base datos"
                },
                "calibracion": [
                    "1. Conectar a red y acceder vía IP web interface",
                    "2. Ejecutar 'Intelligent Calibration Wizard'",
                    "3. Sistema auto-aprende con billetes de entrenamiento",
                    "4. Subir imágenes para entrenamiento IA",
                    "5. Configurar thresholds de confianza por denominación"
                ],
                "mantenimiento": [
                    "Automático: Auto-limpieza sensores programada",
                    "Diario: Verificación cámara y lentes",
                    "Semanal: Actualización base datos falsificaciones"
                ],
                "problemas_comunes": [
                    "IV-100 Error: Reiniciar sistema IA completo",
                    "IV-102 Error: Limpiar lente cámara con kit especial",
                    "Falsos positivos: Re-entrenar modelo IA"
                ]
            },

            "JCM UNA-10": {
                "fabricante": "JCM Global", 
                "tipo": "Aceptador Universal Nueva Arquitectura",
                "voltaje": "+24V DC ±10%",
                "consumo": "2.8A máximo",
                "comunicacion": "RS-232, MDB, USB-C, Ethernet",
                "billetes_aceptados": "Compatibilidad global: 150+ divisas + Billetes polymer + Billetes verticales",
                "conectores": [
                    "U1: 16-pin - Universal main connector",
                    "U2: 6-pin - USB-C y datos rápidos", 
                    "U3: 4-pin - Ethernet gigabit",
                    "U4: 3-pin - Power management"
                ],
                "pines_principal": {
                    "1": "+24V DC",
                    "2": "GND",
                    "3": "MDB Data+",
                    "4": "MDB Data-", 
                    "5": "RS-232 TX",
                    "6": "RS-232 RX",
                    "7": "USB-C TX+",
                    "8": "USB-C TX-",
                    "9": "USB-C RX+",
                    "10": "USB-C RX-",
                    "11": "Ethernet 1000T",
                    "12": "Universal Accept",
                    "13": "Currency Detect",
                    "14": "Security Level",
                    "15": "Diagnostic Advanced", 
                    "16": "Configuration Mode"
                },
                "codigos_error": {
                    "U10": "Universal Transport Error - Error transporte universal",
                    "U11": "Multi-Currency Sensor Fault - Fallo sensor multi-divisa",
                    "U12": "Polymer Detection Error - Error detección polymer",
                    "U13": "Vertical Bill Mechanism - Mecanismo billetes verticales"
                },
                "calibracion": [
                    "1. Usar JCM Universal Configuration Tool (software)",
                    "2. Seleccionar región y divisas a aceptar",
                    "3. Auto-detección de características de billetes",
                    "4. Ajustar sensibilidad por tipo de papel/polymer"
                ],
                "mantenimiento": [
                    "Diario: Limpieza sensores multi-espectrales",
                    "Semanal: Verificación mecanismo universal",
                    "Mensual: Actualización base datos divisas"
                ],
                "problemas_comunes": [
                    "U10 Error: Revisar mecanismo transporte universal",
                    "U12 Error: Recalibrar para billetes polymer",
                    "No detecta divisas: Actualizar base datos"
                ]
            },

            # ========== MODELOS CLÁSICOS ==========
            "MEI AE-2600": {
                "fabricante": "MEI (Crane Payment Innovations)",
                "tipo": "Aceptador de Billetes Estándar",
                "voltaje": "+24V DC ±10%",
                "consumo": "2.5A máximo durante aceptación",
                "comunicacion": "RS-232, MDB, Pulse",
                "billetes_aceptados": "Pesos Mexicanos: $20, $50, $100, $200, $500, $1000",
                "conectores": [
                    "J1: 12-pin - Alimentación y datos",
                    "J2: 4-pin - Opcional para stacker",
                    "J3: 2-pin - Entrada +24V"
                ],
                "pines_principal": {
                    "1": "+24V DC",
                    "2": "GND", 
                    "3": "GND",
                    "4": "MDB Data",
                    "5": "MDB Clock",
                    "6": "RS-232 TX",
                    "7": "RS-232 RX",
                    "8": "Pulse Output",
                    "9": "Reject Output",
                    "10": "Stacker Full",
                    "11": "Enable/Disable",
                    "12": "Sensor de billete presente"
                },
                "codigos_error": {
                    "E01": "Bill Jam - Billete atascado",
                    "E02": "Bill Removed - Billete removido",
                    "E03": "Stacker Full - Contenedor lleno",
                    "E04": "Bill Rejected - Billete rechazado",
                    "E05": "Sensor Error - Error de sensores"
                },
                "calibracion": [
                    "1. Ingresar al modo servicio de la máquina",
                    "2. Seleccionar 'Calibrar Aceptador'",
                    "3. Insertar billetes de prueba en orden",
                    "4. Seguir instrucciones en pantalla",
                    "5. Guardar configuración y reiniciar"
                ],
                "mantenimiento": [
                    "Limpieza diaria: Aire comprimido en sensores",
                    "Limpieza semanal: Alcohol isopropílico en rodillos",
                    "Mensual: Revisión de rodillos y mecanismos"
                ],
                "problemas_comunes": [
                    "No acepta billetes: Verificar enable/disable",
                    "Rechaza billetes buenos: Limpiar sensores ópticos",
                    "Atasca billetes: Revisar rodillos y guías",
                    "No comunica: Verificar cableado MDB/RS-232"
                ]
            },

            "JCM WBA-100": {
                "fabricante": "JCM Global",
                "tipo": "Aceptador de Billetes Universal",
                "voltaje": "+24V DC ±10%", 
                "consumo": "2.0A máximo",
                "comunicacion": "RS-232, MDB, Weighing",
                "billetes_aceptados": "Pesos Mexicanos: $20, $50, $100, $200, $500, $1000",
                "conectores": [
                    "P1: 10-pin - Alimentación y control",
                    "P2: 8-pin - Datos y comunicación", 
                    "P3: 2-pin - Entrada +24V"
                ],
                "pines_principal": {
                    "1": "+24V DC",
                    "2": "GND",
                    "3": "MDB Data",
                    "4": "MDB Clock",
                    "5": "RS-232 TX",
                    "6": "RS-232 RX", 
                    "7": "Bill Accept Pulse",
                    "8": "Stacker Full Signal",
                    "9": "Validator Enable",
                    "10": "Bill Present"
                },
                "codigos_error": {
                    "F1": "Bill Jam in Validator",
                    "F2": "Bill Jam in Stacker",
                    "F3": "Cheated Bill", 
                    "F4": "Bill Removal",
                    "F5": "Stacker Full",
                    "F6": "Bill Rejected",
                    "F7": "Validator ROM Error"
                },
                "calibracion": [
                    "1. Presionar botón de calibración 3 segundos",
                    "2. Insertar billetes de referencia",
                    "3. Ajustar threshold de aceptación",
                    "4. Configurar denominaciones",
                    "5. Probar funcionamiento"
                ],
                "mantenimiento": [
                    "Diario: Limpieza con aire comprimido",
                    "Semanal: Limpieza de rodillos con alcohol",
                    "Mensual: Verificación de sensores",
                    "Trimestral: Calibración completa"
                ],
                "problemas_comunes": [
                    "F1 Error: Desatascar mecanismo",
                    "F3 Error: Billete sospechoso - revisar sensores",
                    "No enciende: Verificar fusible interno",
                    "Comunicación MDB: Revisar reloj y datos"
                ]
            }
        }
    
    def get_manual(self, model):
        return self.manuals.get(model, None)
    
    def list_models(self):
        return list(self.manuals.keys())

# ==================== MÓDULO DE DIAGRAMAS DE FLUJO ====================
class DiagnosticFlowcharts:
    def __init__(self):
        self.flowcharts = self.load_flowcharts()
    
    def load_flowcharts(self):
        return {
            "no_enciende": {
                "titulo": "DIAGNÓSTICO - NO ENCIENDE",
                "pasos": [
                    {"pregunta": "¿La máquina tiene LED de standby encendido?", "si": 1, "no": 2},
                    {"pregunta": "¿Al presionar power hay algún sonido o LED que cambie?", "si": 3, "no": 4},
                    {"pregunta": "¿El cable de alimentación está firmemente conectado?", "si": 5, "no": 6},
                    {"pregunta": "¿Los ventiladores giran aunque sea un instante?", "si": 7, "no": 8},
                    {"pregunta": "Verificar fusibles de entrada en fuente de poder", "accion": "revisar_fusibles"},
                    {"pregunta": "Conectar cable de alimentación correctamente", "accion": "conectar_cable"},
                    {"pregunta": "Problema en main board o CPU. Verificar señales de power", "accion": "revisar_mainboard"},
                    {"pregunta": "Fuente de poder defectuosa. Medir voltajes de salida", "accion": "medir_fuente"}
                ]
            },
            "error_billetetero": {
                "titulo": "DIAGNÓSTICO - ERROR BILLETETERO",
                "pasos": [
                    {"pregunta": "¿El billetetero hace algún sonido al insertar billete?", "si": 1, "no": 2},
                    {"pregunta": "¿Los billetes pasan pero son rechazados?", "si": 3, "no": 4},
                    {"pregunta": "¿El billetetero no agarra los billetes?", "si": 5, "no": 6},
                    {"pregunta": "Verificar conexiones de cableado del billetetero", "accion": "revisar_conexiones"},
                    {"pregunta": "Limpiar sensores ópticos con alcohol isopropílico", "accion": "limpiar_sensores"},
                    {"pregunta": "Ajustar rodillos de alimentación", "accion": "ajustar_rodillos"},
                    {"pregunta": "Calibrar billetetero desde menú de servicio", "accion": "calibrar_billetetero"}
                ]
            },
            "pantalla_negra": {
                "titulo": "DIAGNÓSTICO - PANTALLA NEGRA",
                "pasos": [
                    {"pregunta": "¿La máquina suena normal pero no muestra imagen?", "si": 1, "no": 2},
                    {"pregunta": "¿El backlight de la pantalla está encendido?", "si": 3, "no": 4},
                    {"pregunta": "Problema de tarjeta de video o cable LVDS", "accion": "revisar_video"},
                    {"pregunta": "Verificar si la máquina está en modo suspendido", "accion": "verificar_suspension"},
                    {"pregunta": "Revisar inversor de backlight o LED strips", "accion": "revisar_backlight"},
                    {"pregunta": "Problema de main board. Verificar señal de video", "accion": "revisar_mainboard"}
                ]
            }
        }
    
    def get_flowchart(self, problem_type):
        return self.flowcharts.get(problem_type, None)
    
    def list_flowchart_types(self):
        return list(self.flowcharts.keys())

# ==================== MÓDULO DE DIAGRAMAS DE FUENTES ====================
class PowerSupplyDiagrams:
    def __init__(self):
        self.diagrams = self.load_diagrams()
    
    def load_diagrams(self):
        return {
            "IGT S2000": {
                "modelo_fuente": "IGT PS-2450-1",
                "voltaje_entrada": "100-240V AC, 50/60Hz",
                "voltajes_salida": ["+5V DC @ 15A", "+12V DC @ 8A", "+24V DC @ 6A", "-12V DC @ 1A"],
                "fusibles": ["F1: 5A 250V", "F2: 10A 250V", "F3: 3A 250V"],
                "conectores": ["J1: 20-pin MPU", "J2: 6-pin +24V", "J3: 4-pin +12V", "J4: 2-pin AC"],
                "puntos_medicion": {"TP1": "+5V DC", "TP2": "+12V DC", "TP3": "+24V DC", "TP4": "PG +5V"},
                "problemas_comunes": [
                    "Fusible F1 quemado: revisar cortocircuitos",
                    "Sin +5V: revisar regulador U1",
                    "Sin +24V: revisar transformador T1",
                    "Voltajes inestables: revisar capacitores"
                ]
            },
            "Aristocrat MK6": {
                "modelo_fuente": "Aristocrat PS-MK6-200W",
                "voltaje_entrada": "100-240V AC, 50/60Hz", 
                "voltajes_salida": ["+5V DC @ 18A", "+12V DC @ 10A", "+28V DC @ 5A", "+50V DC @ 2A"],
                "fusibles": ["F1: 4A 250V", "F2: 8A 250V", "F3: 5A 250V", "F4: 2A 250V"],
                "conectores": ["P1: 16-pin main", "P2: 4-pin +28V", "P3: 3-pin +50V", "P4: 2-pin AC"],
                "puntos_medicion": {"TP1": "+5V STBY", "TP2": "+5V MAIN", "TP3": "+12V", "TP4": "+28V", "TP5": "+50V"},
                "problemas_comunes": [
                    "No enciende: revisar F1 y relay K1",
                    "Sin +28V: revisar circuito de switching",
                    "Backlight parpadea: revisar inversor +50V",
                    "Fuente hace click: revisar protección"
                ]
            }
        }
    
    def get_diagram(self, model):
        return self.diagrams.get(model, None)
    
    def list_models(self):
        return list(self.diagrams.keys())

# ==================== BASE DE DATOS PRINCIPAL ====================
class TechnicalDatabase:
    def __init__(self, data_file="technical_data.json"):
        self.data_file = data_file
        if os.path.exists(self.data_file):
            os.remove(self.data_file)
        self.data = self.load_data()
        self.power_diagrams = PowerSupplyDiagrams()
        self.flowcharts = DiagnosticFlowcharts()
        self.bill_acceptors = BillAcceptorManuals()
        self.roulettes = BCMRouletteRecommendations()  # NUEVO: Módulo de ruletas
    
    def load_data(self):
        default_data = {
            "common_problems": [
                {
                    "symptoms": ["no enciende", "sin power", "no prende", "apagada"],
                    "model_patterns": ["*"],
                    "solutions": [
                        {
                            "description": "Verificar fuente de poder y fusibles",
                            "estimated_time": "15 min",
                            "difficulty": "Baja",
                            "tools": ["multimetro", "destornilladores"]
                        }
                    ]
                },
                {
                    "symptoms": ["error billetetero", "no acepta billetes", "billetetero falla"],
                    "model_patterns": ["*"],
                    "solutions": [
                        {
                            "description": "Limpiar sensores opticos del aceptador",
                            "estimated_time": "30 min",
                            "difficulty": "Media",
                            "tools": ["aire comprimido", "hisopos alcohol"]
                        }
                    ]
                }
            ],
            "manuals": [
                # ========== IGT (INTERNATIONAL GAME TECHNOLOGY) ==========
                {"model": "IGT S2000", "manufacturer": "International Game Technology", "pages": 245, "available": True, "sections": ["MPU", "Power Supply", "Bill Acceptor"]},
                {"model": "IGT S Plus", "manufacturer": "International Game Technology", "pages": 267, "available": True, "sections": ["Main Board", "Power Supply", "Bill Validator"]},
                {"model": "IGT Game King", "manufacturer": "International Game Technology", "pages": 312, "available": True, "sections": ["CPU Board", "Video Board", "Power Supply"]},
                {"model": "IGT Advantage", "manufacturer": "International Game Technology", "pages": 289, "available": True, "sections": ["Main Logic", "Power Distribution", "Monitor"]},
                {"model": "IGT Peak", "manufacturer": "International Game Technology", "pages": 334, "available": True, "sections": ["CPU Cabinet", "Display Box", "Player Panel"]},
                {"model": "IGT AVP", "manufacturer": "International Game Technology", "pages": 276, "available": True, "sections": ["Advanced Video Platform", "Power System"]},

                # ========== ARISTOCRAT TECHNOLOGIES ==========
                {"model": "Aristocrat MK6", "manufacturer": "Aristocrat Technologies", "pages": 189, "available": True, "sections": ["Main Board", "Display", "Power Supply"]},
                {"model": "Aristocrat MK5", "manufacturer": "Aristocrat Technologies", "pages": 175, "available": True, "sections": ["CPU Board", "Power Supply", "Monitor"]},
                {"model": "Aristocrat Helix", "manufacturer": "Aristocrat Technologies", "pages": 298, "available": True, "sections": ["Helix Core", "Display Module"]},
                {"model": "Aristocrat Oasis", "manufacturer": "Aristocrat Technologies", "pages": 321, "available": True, "sections": ["System Board", "Cash System"]},
                {"model": "Aristocrat Edge", "manufacturer": "Aristocrat Technologies", "pages": 267, "available": True, "sections": ["Edge X", "Player Interface"]},
                {"model": "Aristocrat Cobalt", "manufacturer": "Aristocrat Technologies", "pages": 289, "available": True, "sections": ["Cobalt Cabinet", "Video System"]},

                # ========== BALLY TECHNOLOGIES ==========
                {"model": "Bally Alpha 2", "manufacturer": "Bally Technologies", "pages": 312, "available": True, "sections": ["CPU Board", "Power Supply", "Touch Screen"]},
                {"model": "Bally Alpha Pro", "manufacturer": "Bally Technologies", "pages": 345, "available": True, "sections": ["Pro Cabinet", "Display System"]},
                {"model": "Bally iVIEW", "manufacturer": "Bally Technologies", "pages": 234, "available": True, "sections": ["Display Module", "Player Interface"]},
                {"model": "Bally SDS", "manufacturer": "Bally Technologies", "pages": 278, "available": True, "sections": ["Server System", "Network Module"]},

                # ========== KONAMI GAMING ==========
                {"model": "Konami Concerto", "manufacturer": "Konami Gaming", "pages": 301, "available": True, "sections": ["Concerto Cabinet", "Display Panel"]},
                {"model": "Konami KX", "manufacturer": "Konami Gaming", "pages": 267, "available": True, "sections": ["KX Platform", "Video Output"]},
                {"model": "Konami Helix", "manufacturer": "Konami Gaming", "pages": 289, "available": True, "sections": ["Helix Core", "Player Station"]},

                # ========== SCIENTIFIC GAMES ==========
                {"model": "SG Oasis 360", "manufacturer": "Scientific Games", "pages": 334, "available": True, "sections": ["360 Cabinet", "Display System"]},
                {"model": "SG TwinStar", "manufacturer": "Scientific Games", "pages": 312, "available": True, "sections": ["Dual Screen", "CPU System"]},
                {"model": "SG Vision", "manufacturer": "Scientific Games", "pages": 276, "available": True, "sections": ["Vision Cabinet", "Video Board"]},

                # ========== EVERI HOLDINGS ==========
                {"model": "Everi Cinevision", "manufacturer": "Everi Holdings", "pages": 298, "available": True, "sections": ["Cinevision Cabinet", "Display System"]},
                {"model": "Everi Edge X", "manufacturer": "Everi Holdings", "pages": 267, "available": True, "sections": ["Edge X Platform", "Player Station"]},
                {"model": "Everi Forte", "manufacturer": "Everi Holdings", "pages": 289, "available": True, "sections": ["Forte Cabinet", "Game System"]},

                # ========== APOLLO GAMES ==========
                {"model": "Apollo G40", "manufacturer": "Apollo Games", "pages": 245, "available": True, "sections": ["G40 Chassis", "Display", "Power Unit"]},
                {"model": "Apollo V20", "manufacturer": "Apollo Games", "pages": 223, "available": True, "sections": ["V20 Platform", "Video System"]},

                # ========== NOVOMATIC ==========
                {"model": "Novomatic Axxis", "manufacturer": "Novomatic", "pages": 301, "available": True, "sections": ["Axxis Cabinet", "Display System"]},
                {"model": "Novomatic V.I.P.", "manufacturer": "Novomatic", "pages": 278, "available": True, "sections": ["VIP Platform", "Player Interface"]},

                # ========== ATRONIC INTERNATIONAL ==========
                {"model": "Atronic 8300", "manufacturer": "Atronic International", "pages": 256, "available": True, "sections": ["8300 Series", "Main Board"]},
                {"model": "Atronic 7300", "manufacturer": "Atronic International", "pages": 234, "available": True, "sections": ["7300 Platform", "Display"]},

                # ========== WMS INDUSTRIES ==========
                {"model": "WMS Bluebird 2", "manufacturer": "WMS Industries", "pages": 289, "available": True, "sections": ["Bluebird Cabinet", "CPU System"]},
                {"model": "WMS Gamefield XD", "manufacturer": "WMS Industries", "pages": 312, "available": True, "sections": ["Gamefield Platform", "Video System"]},

                # ========== SPIELO INTERNATIONAL ==========
                {"model": "Spielo G3", "manufacturer": "Spielo International", "pages": 267, "available": True, "sections": ["G3 Cabinet", "Main Logic"]},
                {"model": "Spielo Odissey", "manufacturer": "Spielo International", "pages": 245, "available": True, "sections": ["Odissey Platform", "Display Module"]},

                # ========== MÁQUINAS MEXICANAS/LOCALES ==========
                {"model": "Bingomania Clasico", "manufacturer": "Bingomania", "pages": 178, "available": True, "sections": ["Main Board", "Display", "Power Supply"]},
                {"model": "Caliente Slots Pro", "manufacturer": "Grupo Caliente", "pages": 234, "available": True, "sections": ["Pro Cabinet", "Video System"]},
                {"model": "Playdo Grande", "manufacturer": "Playdo Gaming", "pages": 201, "available": True, "sections": ["Grande Cabinet", "Display"]}
            ],
            "inventory": [
                {
                    "name": "Fuente Poder IGT S2000",
                    "compatible_models": ["IGT S2000", "IGT S Plus", "IGT Game King"],
                    "quantity": 3,
                    "supplier": "IGT Parts"
                },
                {
                    "name": "Display Touch IGT S2000",
                    "compatible_models": ["IGT S2000", "IGT S Plus"],
                    "quantity": 2,
                    "supplier": "IGT Parts"
                },
                {
                    "name": "Aceptador MEI SCN66 Advance",
                    "compatible_models": ["IGT S2000", "Aristocrat MK6", "Bally Alpha Pro"],
                    "quantity": 2,
                    "supplier": "MEI Professional"
                },
                {
                    "name": "Aceptador MEI CashFlow 7000",
                    "compatible_models": ["IGT Game King", "Aristocrat Oasis", "Bally Alpha 2"],
                    "quantity": 4,
                    "supplier": "MEI Parts"
                },
                {
                    "name": "Aceptador JCM iVizion",
                    "compatible_models": ["Konami Concerto", "SG Oasis 360", "Everi Cinevision"],
                    "quantity": 3,
                    "supplier": "JCM Global"
                },
                {
                    "name": "Aceptador JCM UNA-10", 
                    "compatible_models": ["Novomatic Axxis", "WMS Gamefield XD", "Spielo G3"],
                    "quantity": 2,
                    "supplier": "JCM Global"
                },
                {
                    "name": "MPU Board IGT S2000",
                    "compatible_models": ["IGT S2000"],
                    "quantity": 1,
                    "supplier": "IGT Parts"
                },
                # NUEVO: Repuestos para ruletas BCM
                {
                    "name": "Sensores de Bola BCM RW-2000",
                    "compatible_models": ["BCM ARISTOCRAT RW-2000"],
                    "quantity": 5,
                    "supplier": "BCM Argentina"
                },
                {
                    "name": "Display LCD BCM 42\"",
                    "compatible_models": ["BCM ARISTOCRAT RW-2000", "BCM iDECK ROULETTE"],
                    "quantity": 2,
                    "supplier": "BCM Argentina"
                },
                {
                    "name": "Encoder Rueda BCM",
                    "compatible_models": ["BCM ARISTOCRAT RW-2000", "BCM COMPACT ROULETTE"],
                    "quantity": 3,
                    "supplier": "BCM Argentina"
                }
            ],
            "repair_history": [
                {
                    "date": "2024-01-15",
                    "model": "IGT S2000",
                    "problem": "No enciende",
                    "solution": "Reemplazada fuente de poder",
                    "technician": "Juan Perez"
                },
                {
                    "date": "2024-01-10", 
                    "model": "Aristocrat MK6",
                    "problem": "Error billetetero",
                    "solution": "Limpieza de sensores opticos",
                    "technician": "Maria Garcia"
                },
                {
                    "date": "2024-01-08",
                    "model": "Bally Alpha 2",
                    "problem": "Pantalla negra",
                    "solution": "Reemplazado cable de video",
                    "technician": "Carlos Rodriguez"
                },
                # NUEVO: Reparaciones de ruletas
                {
                    "date": "2024-01-18",
                    "model": "BCM ARISTOCRAT RW-2000", 
                    "problem": "Error sensor de bola BCM-001",
                    "solution": "Limpieza de sensores ópticos y recalibración",
                    "technician": "Luis Fernandez"
                }
            ]
        }
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(default_data, f, indent=2, ensure_ascii=False)
            return default_data
    
    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def get_common_problems(self):
        return self.data.get("common_problems", [])
    
    def get_manuals(self):
        return self.data.get("manuals", [])
    
    def get_inventory(self):
        return self.data.get("inventory", [])
    
    def get_repair_history(self):
        return self.data.get("repair_history", [])
    
    def get_manual(self, model):
        for manual in self.get_manuals():
            if manual['model'].lower() == model.lower():
                return manual
        return None
    
    def add_repair_record(self, record):
        self.data["repair_history"].append(record)
        self.save_data()
    
    def get_models_count(self):
        return len(self.get_manuals())

# ==================== MOTOR DE DIAGNOSTICO ====================
class DiagnosticEngine:
    def __init__(self, database):
        self.db = database
    
    def analyze_symptoms(self, model, symptoms):
        symptoms_lower = symptoms.lower()
        problems = self.db.get_common_problems()
        
        matches = []
        
        for problem in problems:
            model_match = self._check_model_match(model, problem['model_patterns'])
            
            if model_match:
                symptom_match_score = self._calculate_symptom_match(symptoms_lower, problem['symptoms'])
                
                if symptom_match_score > 0.3:
                    matches.append({
                        'problem': problem,
                        'score': symptom_match_score,
                        'solutions': problem['solutions']
                    })
        
        matches.sort(key=lambda x: x['score'], reverse=True)
        
        if matches:
            best_match = matches[0]
            confidence = min(int(best_match['score'] * 100), 95)
            
            return {
                'confidence': confidence,
                'solutions': best_match['solutions'],
                'matched_problems': len(matches)
            }
        else:
            return {
                'confidence': 0,
                'solutions': [{
                    'description': 'Problema no identificado. Verificar manual tecnico.',
                    'estimated_time': 'Desconocido',
                    'difficulty': 'Alta',
                    'tools': ['Manual tecnico', 'Equipo de diagnostico']
                }],
                'matched_problems': 0
            }
    
    def _check_model_match(self, model, patterns):
        model_lower = model.lower()
        
        for pattern in patterns:
            if pattern.endswith('*'):
                base_pattern = pattern[:-1].lower()
                if model_lower.startswith(base_pattern):
                    return True
            elif model_lower == pattern.lower():
                return True
        
        return False
    
    def _calculate_symptom_match(self, symptoms, symptom_list):
        max_score = 0
        
        for known_symptom in symptom_list:
            score = SequenceMatcher(None, symptoms, known_symptom).ratio()
            max_score = max(max_score, score)
        
        return max_score

# ==================== GESTOR DE INVENTARIO ====================
class InventoryManager:
    def __init__(self, database):
        self.db = database
    
    def search_part(self, part_name):
        inventory = self.db.get_inventory()
        results = []
        
        for item in inventory:
            if part_name.lower() in item['name'].lower():
                results.append(item)
        
        return results
    
    def show_inventory(self):
        inventory = self.db.get_inventory()
        
        if not inventory:
            print("El inventario esta vacio")
            return
        
        print("\n" + "=" * 50)
        print("INVENTARIO ACTUAL")
        print("=" * 50)
        
        for item in inventory:
            print(f"REPUESTO: {item['name']}")
            print(f"Compatible: {', '.join(item['compatible_models'])}")
            print(f"Stock: {item['quantity']} unidades")
            print(f"Proveedor: {item['supplier']}")
            print("-" * 40)

# ==================== IA PRINCIPAL COMPLETA ====================
class CompleteSlotTechnicianAI:
    def __init__(self):
        self.db = TechnicalDatabase()
        self.diagnostic = DiagnosticEngine(self.db)
        self.inventory = InventoryManager(self.db)
        
    def start(self):
        total_models = self.db.get_models_count()
        total_parts = len(self.db.get_inventory())
        total_repairs = len(self.db.get_repair_history())
        total_roulettes = len(self.db.roulettes.list_models())  # NUEVO: Contador de ruletas
        
        print(f"\n=== SISTEMA COMPLETO CARGADO ===")
        print(f"📊 Modelos de maquinas: {total_models}")
        print(f"🔧 Repuestos en inventario: {total_parts}")
        print(f"📝 Reparaciones registradas: {total_repairs}")
        print(f"⚡ Diagramas de fuentes: {len(self.db.power_diagrams.list_models())}")
        print(f"📋 Diagramas de flujo: {len(self.db.flowcharts.list_flowchart_types())}")
        print(f"💰 Manuales aceptadores: {len(self.db.bill_acceptors.list_models())}")
        print(f"🎰 Ruletas BCM: {total_roulettes}")  # NUEVO: Mostrar ruletas
        
        while True:
            print("\n" + "=" * 50)
            print("MENU PRINCIPAL COMPLETO")
            print("=" * 50)
            print("1. 🔍 Diagnostico de Fallas")
            print("2. 📋 Diagramas de Flujo Interactivos")
            print("3. 📚 Manuales Tecnicos")
            print("4. 🧮 Gestion de Inventario")
            print("5. 📊 Historial de Reparaciones")
            print("6. ➕ Agregar Reparacion")
            print("7. ⚡ Diagramas de Fuentes")
            print("8. 💰 Manuales Aceptadores MEI/JCM")
            print("9. 🎰 Manuales Ruletas BCM")  # NUEVO: Opción de ruletas
            print("10. 📋 Listar Todos los Modelos")
            print("11. 🚪 Salir")
            
            choice = input("\nSelecciona una opcion (1-11): ").strip()
            
            if choice == "1":
                self.diagnostic_flow()
            elif choice == "2":
                self.flowchart_diagnostic_flow()
            elif choice == "3":
                self.manuals_flow()
            elif choice == "4":
                self.inventory_flow()
            elif choice == "5":
                self.history_flow()
            elif choice == "6":
                self.add_repair_flow()
            elif choice == "7":
                self.power_supply_flow()
            elif choice == "8":
                self.bill_acceptor_flow()
            elif choice == "9":  # NUEVO: Ruletas BCM
                self.roulettes_flow()
            elif choice == "10":
                self.list_all_models_flow()
            elif choice == "11":
                print("¡Hasta pronto! Que tengas buenas reparaciones.")
                break
            else:
                print("Opcion invalida. Intenta nuevamente.")
    
    def diagnostic_flow(self):
        print("\n" + "=" * 50)
        print("DIAGNOSTICO AUTOMATICO POR SINTOMAS")
        print("=" * 50)
        
        model = input("Modelo de la maquina (ej: IGT S2000): ").strip()
        symptoms = input("Describe los sintomas: ").strip()
        
        if not model or not symptoms:
            print("Error: Debes ingresar modelo y sintomas.")
            return
        
        print("\nAnalizando el problema...")
        
        results = self.diagnostic.analyze_symptoms(model, symptoms)
        
        print(f"\nRESULTADOS DEL DIAGNOSTICO:")
        print(f"Maquina: {model.upper()}")
        print(f"Sintomas: {symptoms}")
        print(f"Confianza: {results['confidence']}%")
        
        print("\nSOLUCIONES RECOMENDADAS:")
        for i, solution in enumerate(results['solutions'], 1):
            print(f"\n{i}. {solution['description']}")
            print(f"   Tiempo estimado: {solution['estimated_time']}")
            print(f"   Dificultad: {solution['difficulty']}")
            print(f"   Herramientas: {', '.join(solution['tools'])}")
    
    def flowchart_diagnostic_flow(self):
        """Diagnóstico por diagramas de flujo interactivos"""
        print("\n" + "=" * 60)
        print("DIAGRAMAS DE FLUJO INTERACTIVOS")
        print("=" * 60)
        
        print("\nSelecciona el tipo de problema:")
        flowchart_types = self.db.flowcharts.list_flowchart_types()
        for i, problem_type in enumerate(flowchart_types, 1):
            problem_name = problem_type.replace('_', ' ').title()
            print(f"{i}. {problem_name}")
        
        try:
            choice = int(input("\nSelecciona el problema (1-{}): ".format(len(flowchart_types))))
            if 1 <= choice <= len(flowchart_types):
                problem_type = flowchart_types[choice - 1]
                self.run_flowchart(problem_type)
            else:
                print("Selección inválida")
        except ValueError:
            print("Por favor ingresa un número válido")
    
    def run_flowchart(self, problem_type):
        """Ejecuta un diagrama de flujo interactivo"""
        flowchart = self.db.flowcharts.get_flowchart(problem_type)
        if not flowchart:
            print("Diagrama de flujo no encontrado")
            return
        
        print(f"\n" + "=" * 60)
        print(flowchart["titulo"])
        print("=" * 60)
        
        current_step = 0
        steps = flowchart["pasos"]
        
        while current_step < len(steps):
            step = steps[current_step]
            
            if "pregunta" in step:
                print(f"\n{step['pregunta']}")
                respuesta = input("(s/n): ").strip().lower()
                
                if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                    if "si" in step:
                        current_step = step["si"]
                    else:
                        break
                else:
                    if "no" in step:
                        current_step = step["no"]
                    else:
                        break
            elif "accion" in step:
                print(f"\n🎯 ACCIÓN RECOMENDADA: {step['pregunta']}")
                print(f"   💡 Procedimiento: {self.get_action_procedure(step['accion'])}")
                
                resolvio = input("\n¿Se resolvió el problema? (s/n): ").strip().lower()
                if resolvio in ['s', 'si', 'sí', 'y', 'yes']:
                    print("✅ ¡Problema resuelto!")
                    self.quick_repair_record(problem_type, step['accion'])
                    break
                else:
                    print("➡️ Continuando con el diagnóstico...")
                    current_step += 1
        
        print(f"\n🔚 Fin del diagrama de flujo para: {problem_type.replace('_', ' ').title()}")
    
    def get_action_procedure(self, action):
        """Devuelve el procedimiento detallado para una acción"""
        procedures = {
            "revisar_fusibles": "1. Desconectar alimentación\n2. Revisar fusibles visualmente\n3. Medir continuidad con multímetro\n4. Reemplazar si es necesario",
            "medir_fuente": "1. Conectar multímetro\n2. Medir +5V, +12V, +24V en TP1, TP2, TP3\n3. Verificar que estén dentro de ±5%\n4. Revisar señal PG (Power Good)",
            "limpiar_sensores": "1. Desconectar billetetero\n2. Limpiar con alcohol isopropílico\n3. Usar hisopos de calidad\n4. Secar completamente antes de conectar",
            "calibrar_billetetero": "1. Entrar en modo servicio\n2. Seleccionar calibración billetetero\n3. Seguir instrucciones en pantalla\n4. Probar con billetes de prueba",
        }
        return procedures.get(action, "Procedimiento no especificado. Consultar manual técnico.")
    
    def quick_repair_record(self, problem_type, solution):
        """Registro rápido de reparación desde diagrama de flujo"""
        confirmar = input("¿Deseas registrar esta reparación en el historial? (s/n): ").strip().lower()
        if confirmar in ['s', 'si', 'sí']:
            model = input("Modelo de la máquina: ").strip()
            technician = input("Nombre del técnico: ").strip()
            
            record = {
                "date": "2024-01-20",
                "model": model,
                "problem": problem_type.replace('_', ' ').title(),
                "solution": solution,
                "technician": technician
            }
            
            self.db.add_repair_record(record)
            print("✅ Reparación registrada en historial")
    
    def manuals_flow(self):
        print("\n" + "=" * 50)
        print("MANUALES TECNICOS")
        print("=" * 50)
        
        model = input("Modelo a consultar: ").strip()
        manual = self.db.get_manual(model)
        
        if manual:
            print(f"\nINFORMACION DEL MANUAL:")
            print(f"Modelo: {manual['model']}")
            print(f"Fabricante: {manual['manufacturer']}")
            print(f"Paginas: {manual['pages']}")
            print(f"Disponible: {'SI' if manual['available'] else 'NO'}")
            
            if manual['sections']:
                print("\nSECCIONES DISPONIBLES:")
                for section in manual['sections']:
                    print(f"  - {section}")
        else:
            print(f"No se encontro manual para: {model}")
    
    def inventory_flow(self):
        print("\n" + "=" * 50)
        print("GESTION DE INVENTARIO")
        print("=" * 50)
        
        print("1. Buscar repuesto")
        print("2. Ver inventario completo")
        print("3. Volver al menu principal")
        
        choice = input("Selecciona opcion (1-3): ").strip()
        
        if choice == "1":
            part_name = input("Nombre del repuesto: ").strip()
            results = self.inventory.search_part(part_name)
            
            if results:
                print(f"\nSe encontraron {len(results)} repuestos:")
                for part in results:
                    print(f"\nREPUESTO: {part['name']}")
                    print(f"  Compatible: {', '.join(part['compatible_models'])}")
                    print(f"  Stock: {part['quantity']} unidades")
                    print(f"  Proveedor: {part['supplier']}")
            else:
                print("No se encontraron repuestos.")
                
        elif choice == "2":
            self.inventory.show_inventory()
    
    def history_flow(self):
        print("\n" + "=" * 50)
        print("HISTORIAL DE REPARACIONES")
        print("=" * 50)
        
        history = self.db.get_repair_history()
        if history:
            print(f"Total de reparaciones: {len(history)}")
            print("\nULTIMAS REPARACIONES:")
            for repair in history:
                print(f"\nFECHA: {repair['date']}")
                print(f"MAQUINA: {repair['model']}")
                print(f"PROBLEMA: {repair['problem']}")
                print(f"SOLUCION: {repair['solution']}")
                print(f"TECNICO: {repair['technician']}")
                print("-" * 40)
        else:
            print("No hay historial de reparaciones.")
    
    def add_repair_flow(self):
        print("\n" + "=" * 50)
        print("REGISTRAR REPARACION")
        print("=" * 50)
        
        date = input("Fecha (YYYY-MM-DD): ").strip()
        model = input("Modelo de la maquina: ").strip()
        problem = input("Problema encontrado: ").strip()
        solution = input("Solucion aplicada: ").strip()
        technician = input("Nombre del tecnico: ").strip()
        
        if not all([date, model, problem, solution, technician]):
            print("Error: Todos los campos son obligatorios.")
            return
        
        new_record = {
            "date": date,
            "model": model,
            "problem": problem,
            "solution": solution,
            "technician": technician
        }
        
        self.db.add_repair_record(new_record)
        print("¡Reparacion registrada exitosamente!")
    
    def power_supply_flow(self):
        print("\n" + "=" * 60)
        print("DIAGRAMAS DE FUENTES DE ALIMENTACIÓN")
        print("=" * 60)
        
        print("1. Ver diagrama de fuente específica")
        print("2. Listar modelos con diagramas disponibles")
        print("3. Volver al menú principal")
        
        choice = input("\nSelecciona opción (1-3): ").strip()
        
        if choice == "1":
            models = self.db.power_diagrams.list_models()
            print("\nModelos con diagramas disponibles:")
            for i, model in enumerate(models, 1):
                print(f"{i}. {model}")
            
            try:
                choice = int(input("\nSelecciona modelo: "))
                if 1 <= choice <= len(models):
                    model = models[choice - 1]
                    diagram = self.db.power_diagrams.get_diagram(model)
                    
                    if diagram:
                        print(f"\n" + "=" * 50)
                        print(f"DIAGRAMA - {model}")
                        print("=" * 50)
                        
                        print(f"\n📊 ESPECIFICACIONES:")
                        print(f"   Modelo de fuente: {diagram['modelo_fuente']}")
                        print(f"   Voltaje entrada: {diagram['voltaje_entrada']}")
                        
                        print(f"\n⚡ VOLTAJES DE SALIDA:")
                        for voltage in diagram['voltajes_salida']:
                            print(f"   • {voltage}")
                        
                        print(f"\n🔌 FUSIBLES:")
                        for fuse in diagram['fusibles']:
                            print(f"   • {fuse}")
                    else:
                        print("No se encontró diagrama para este modelo")
                else:
                    print("Selección inválida")
            except ValueError:
                print("Ingresa un número válido")
        elif choice == "2":
            models = self.db.power_diagrams.list_models()
            print(f"\nModelos con diagramas de fuentes:")
            for model in models:
                print(f"  • {model}")
    
    def bill_acceptor_flow(self):
        """Manuales de aceptadores MEI y JCM"""
        print("\n" + "=" * 60)
        print("MANUALES DE ACEPTADORES MEI Y JCM")
        print("=" * 60)
        
        print("1. Ver manual de aceptador específico")
        print("2. Listar todos los aceptadores disponibles")
        print("3. Búsqueda por problema común")
        print("4. Volver al menú principal")
        
        choice = input("\nSelecciona opción (1-4): ").strip()
        
        if choice == "1":
            self.show_bill_acceptor_manual()
        elif choice == "2":
            self.list_bill_acceptors()
        elif choice == "3":
            self.bill_acceptor_troubleshooting()
        elif choice == "4":
            return
        else:
            print("Opción inválida")
    
    def show_bill_acceptor_manual(self):
        """Muestra manual completo de un aceptador específico"""
        models = self.db.bill_acceptors.list_models()
        print("\nModelos de aceptadores disponibles:")
        for i, model in enumerate(models, 1):
            print(f"{i}. {model}")
        
        try:
            choice = int(input("\nSelecciona el modelo (1-{}): ".format(len(models))))
            if 1 <= choice <= len(models):
                model = models[choice - 1]
                manual = self.db.bill_acceptors.get_manual(model)
                
                if manual:
                    print(f"\n" + "=" * 60)
                    print(f"MANUAL TÉCNICO - {model}")
                    print("=" * 60)
                    
                    print(f"\n🏭 FABRICANTE: {manual['fabricante']}")
                    print(f"🔧 TIPO: {manual['tipo']}")
                    print(f"⚡ VOLTAJE: {manual['voltaje']}")
                    print(f"🔋 CONSUMO: {manual['consumo']}")
                    print(f"📡 COMUNICACIÓN: {manual['comunicacion']}")
                    
                    print(f"\n💵 BILLETES ACEPTADOS:")
                    print(f"   {manual['billetes_aceptados']}")
                    
                    print(f"\n🔌 CONECTORES:")
                    for connector in manual['conectores']:
                        print(f"   • {connector}")
                    
                    if 'pines_principal' in manual:
                        print(f"\n📍 PINOUT CONECTOR PRINCIPAL:")
                        for pin, funcion in manual['pines_principal'].items():
                            print(f"   Pin {pin}: {funcion}")
                    
                    # Mostrar códigos de error según el tipo de aceptador
                    if 'codigos_error_avanzados' in manual:
                        print(f"\n❌ CÓDIGOS DE ERROR AVANZADOS:")
                        for codigo, descripcion in manual['codigos_error_avanzados'].items():
                            print(f"   {codigo}: {descripcion}")
                    elif 'codigos_error' in manual:
                        print(f"\n❌ CÓDIGOS DE ERROR:")
                        for codigo, descripcion in manual['codigos_error'].items():
                            print(f"   {codigo}: {descripcion}")
                    
                    # Mostrar sensores avanzados para SCN66
                    if 'sensores_avanzados' in manual:
                        print(f"\n🔬 SENSORES AVANZADOS:")
                        for sensor in manual['sensores_avanzados']:
                            print(f"   • {sensor}")
                    
                    # Mostrar calibración según el tipo
                    if 'calibracion_avanzada' in manual:
                        print(f"\n🛠️  PROCEDIMIENTO DE CALIBRACIÓN AVANZADA:")
                        for paso in manual['calibracion_avanzada']:
                            print(f"   • {paso}")
                    elif 'calibracion' in manual:
                        print(f"\n🛠️  PROCEDIMIENTO DE CALIBRACIÓN:")
                        for paso in manual['calibracion']:
                            print(f"   • {paso}")
                    
                    # Mostrar mantenimiento
                    if 'mantenimiento_especializado' in manual:
                        print(f"\n📅 MANTENIMIENTO ESPECIALIZADO:")
                        for tarea in manual['mantenimiento_especializado']:
                            print(f"   • {tarea}")
                    elif 'mantenimiento' in manual:
                        print(f"\n📅 MANTENIMIENTO PREVENTIVO:")
                        for tarea in manual['mantenimiento']:
                            print(f"   • {tarea}")
                    
                    # Mostrar características de seguridad para SCN66
                    if 'caracteristicas_seguridad' in manual:
                        print(f"\n🛡️  CARACTERÍSTICAS DE SEGURIDAD:")
                        for caracteristica in manual['caracteristicas_seguridad']:
                            print(f"   • {caracteristica}")
                    
                    # Mostrar problemas comunes
                    if 'problemas_comunes_avanzados' in manual:
                        print(f"\n⚠️  PROBLEMAS COMUNES AVANZADOS:")
                        for problema in manual['problemas_comunes_avanzados']:
                            print(f"   • {problema}")
                    elif 'problemas_comunes' in manual:
                        print(f"\n⚠️  PROBLEMAS COMUNES:")
                        for problema in manual['problemas_comunes']:
                            print(f"   • {problema}")
                        
                else:
                    print("No se encontró manual para este modelo")
            else:
                print("Selección inválida")
        except ValueError:
            print("Por favor ingresa un número válido")
    
    def list_bill_acceptors(self):
        """Lista todos los aceptadores disponibles"""
        models = self.db.bill_acceptors.list_models()
        manuals = self.db.bill_acceptors.manuals
        
        print(f"\n" + "=" * 60)
        print("LISTA COMPLETA DE ACEPTADORES")
        print("=" * 60)
        
        print(f"\n🎯 TOTAL DE MODELOS: {len(models)}")
        
        print(f"\n🔬 MEI SCN66 ADVANCE SERIES:")
        for model in models:
            if "SCN66" in model:
                info = manuals[model]
                print(f"   • {model} - {info['tipo']}")
        
        print(f"\n💰 MEI CASHFLOW SERIES:")
        for model in models:
            if "CashFlow" in model:
                info = manuals[model]
                print(f"   • {model} - {info['tipo']}")
        
        print(f"\n🤖 JCM MODERN SERIES:")
        for model in models:
            if "JCM" in model and "iVizion" in model:
                info = manuals[model]
                print(f"   • {model} - {info['tipo']}")
        
        print(f"\n🌍 JCM UNIVERSAL SERIES:")
        for model in models:
            if "JCM" in model and "UNA" in model:
                info = manuals[model]
                print(f"   • {model} - {info['tipo']}")
        
        print(f"\n🎰 MODELOS CLÁSICOS:")
        for model in models:
            if "AE-2600" in model or "WBA-100" in model:
                info = manuals[model]
                print(f"   • {model} - {info['tipo']}")
    
    def bill_acceptor_troubleshooting(self):
        """Diagnóstico rápido de problemas comunes"""
        print(f"\n" + "=" * 60)
        print("DIAGNÓSTICO RÁPIDO - ACEPTADORES")
        print("=" * 60)
        
        problemas = [
            "No acepta billetes",
            "Rechaza billetes buenos",
            "Atasca billetes frecuentemente",
            "Error de comunicación",
            "No enciende el aceptador",
            "Código de error específico"
        ]
        
        print("\nSelecciona el problema:")
        for i, problema in enumerate(problemas, 1):
            print(f"{i}. {problema}")
        
        try:
            choice = int(input("\nSelecciona el problema (1-6): "))
            if choice == 1:
                self._diagnosticar_no_acepta()
            elif choice == 2:
                self._diagnosticar_rechaza_buenos()
            elif choice == 3:
                self._diagnosticar_atascos()
            elif choice == 4:
                self._diagnosticar_comunicacion()
            elif choice == 5:
                self._diagnosticar_no_enciende()
            elif choice == 6:
                self._diagnosticar_codigo_error()
            else:
                print("Selección inválida")
        except ValueError:
            print("Por favor ingresa un número válido")

    def _diagnosticar_no_acepta(self):
        print(f"\n" + "=" * 50)
        print("DIAGNÓSTICO - NO ACEPTA BILLETES")
        print("=" * 50)
        
        print("\n1. ✅ Verificar alimentación +24V DC")
        print("2. ✅ Revisar señal ENABLE del aceptador")
        print("3. ✅ Limpiar sensores de entrada")
        print("4. ✅ Verificar rodillos de alimentación")
        print("5. ✅ Comprobar configuración de denominaciones")
        
        modelo = input("\n¿Qué modelo de aceptador es? ").strip()
        manual = self.db.bill_acceptors.get_manual(modelo)
        
        if manual:
            print(f"\n🔧 PROCEDIMIENTOS ESPECÍFICOS PARA {modelo}:")
            if 'problemas_comunes_avanzados' in manual:
                for problema in manual['problemas_comunes_avanzados']:
                    if "rechazo" in problema.lower() or "acepta" in problema.lower():
                        print(f"   • {problema}")
            elif 'problemas_comunes' in manual:
                for problema in manual['problemas_comunes']:
                    if "rechazo" in problema.lower() or "acepta" in problema.lower():
                        print(f"   • {problema}")

    def _diagnosticar_rechaza_buenos(self):
        print(f"\n" + "=" * 50)
        print("DIAGNÓSTICO - RECHAZA BILLETES BUENOS")
        print("=" * 50)
        
        print("\n1. 🧹 Limpieza completa de sensores ópticos")
        print("2. 🔧 Ejecutar calibración completa")
        print("3. ⚙️  Ajustar thresholds de sensibilidad")
        print("4. 🔄 Actualizar base de datos de seguridad")
        print("5. 🌡️  Verificar condiciones ambientales")
        
        modelo = input("\n¿Qué modelo de aceptador es? ").strip()
        manual = self.db.bill_acceptors.get_manual(modelo)
        
        if manual:
            print(f"\n🔧 PROCEDIMIENTOS ESPECÍFICOS PARA {modelo}:")
            if 'calibracion_avanzada' in manual:
                print("   CALIBRACIÓN AVANZADA REQUERIDA:")
                for paso in manual['calibracion_avanzada'][:3]:
                    print(f"   • {paso}")
            elif 'calibracion' in manual:
                print("   PROCEDIMIENTO DE CALIBRACIÓN:")
                for paso in manual['calibracion'][:3]:
                    print(f"   • {paso}")

    def _diagnosticar_atascos(self):
        print(f"\n" + "=" * 50)
        print("DIAGNÓSTICO - ATASCOS FRECUENTES")
        print("=" * 50)
        
        print("\n1. 🔧 Revisar rodillos y mecanismo de transporte")
        print("2. 🧹 Limpiar guías y camino del billete")
        print("3. ⚙️  Verificar tensión de rodillos")
        print("4. 🔄 Lubricar mecanismo (solo lubricante especificado)")
        print("5. 📏 Verificar alineación de componentes")
        
        modelo = input("\n¿Qué modelo de aceptador es? ").strip()
        print(f"\n🔧 PARA {modelo}:")
        print("   • Usar solo lubricantes autorizados por el fabricante")
        print("   • Verificar especificaciones de torque en manual")
        print("   • Revisar desgaste de rodillos cada 50,000 ciclos")

    def _diagnosticar_comunicacion(self):
        print(f"\n" + "=" * 50)
        print("DIAGNÓSTICO - ERROR DE COMUNICACIÓN")
        print("=" * 50)
        
        print("\n1. 🔌 Verificar cableado y conectores")
        print("2. ⚡ Comprobar voltajes de alimentación")
        print("3. 📡 Revisar configuración protocolo (MDB/RS-232)")
        print("4. 🔄 Reiniciar aceptador y controlador")
        print("5. 💾 Actualizar firmware si es necesario")
        
        modelo = input("\n¿Qué modelo de aceptador es? ").strip()
        manual = self.db.bill_acceptors.get_manual(modelo)
        
        if manual and 'pines_principal' in manual:
            print(f"\n🔌 PINOUT DE COMUNICACIÓN PARA {modelo}:")
            for pin, funcion in manual['pines_principal'].items():
                if any(com in funcion for com in ['MDB', 'RS-232', 'USB', 'Ethernet']):
                    print(f"   Pin {pin}: {funcion}")

    def _diagnosticar_no_enciende(self):
        print(f"\n" + "=" * 50)
        print("DIAGNÓSTICO - NO ENCIENDE ACEPTADOR")
        print("=" * 50)
        
        print("\n1. 🔌 Verificar alimentación +24V DC")
        print("2. ⚡ Medir voltaje en conector de alimentación")
        print("3. 🔥 Revisar fusibles internos")
        print("4. 🔧 Comprobar cableado de potencia")
        print("5. 💡 Verificar LEDs de estado")
        
        print(f"\n🔧 PROCEDIMIENTO GENERAL:")
        print("   • Desconectar alimentación")
        print("   • Medir continuidad de cables")
        print("   • Verificar fusibles con multímetro")
        print("   • Revisar reguladores de voltaje")

    def _diagnosticar_codigo_error(self):
        print(f"\n" + "=" * 50)
        print("DIAGNÓSTICO - CÓDIGO DE ERROR ESPECÍFICO")
        print("=" * 50)
        
        codigo = input("Ingresa el código de error (ej: SCN-001, CF-01): ").strip()
        modelo = input("Modelo del aceptador: ").strip()
        
        manual = self.db.bill_acceptors.get_manual(modelo)
        
        if manual:
            encontrado = False
            
            # Buscar en códigos avanzados
            if 'codigos_error_avanzados' in manual:
                for error_codigo, descripcion in manual['codigos_error_avanzados'].items():
                    if error_codigo.upper() == codigo.upper():
                        print(f"\n✅ CÓDIGO ENCONTRADO: {error_codigo}")
                        print(f"📝 DESCRIPCIÓN: {descripcion}")
                        encontrado = True
                        
                        # Buscar solución en problemas comunes
                        if 'problemas_comunes_avanzados' in manual:
                            for problema in manual['problemas_comunes_avanzados']:
                                if codigo in problema:
                                    print(f"🔧 SOLUCIÓN SUGERIDA: {problema}")
                                    break
            
            # Buscar en códigos estándar
            if not encontrado and 'codigos_error' in manual:
                for error_codigo, descripcion in manual['codigos_error'].items():
                    if error_codigo.upper() == codigo.upper():
                        print(f"\n✅ CÓDIGO ENCONTRADO: {error_codigo}")
                        print(f"📝 DESCRIPCIÓN: {descripcion}")
                        encontrado = True
            
            if not encontrado:
                print(f"\n❌ Código de error '{codigo}' no encontrado para {modelo}")
                print("💡 Verifica el código o consulta el manual completo")
        else:
            print(f"❌ No se encontró manual para {modelo}")

    def roulettes_flow(self):
        """NUEVO: Manuales de ruletas BCM"""
        print("\n" + "=" * 60)
        print("MANUALES DE RULETAS BCM")
        print("=" * 60)
        
        print("1. Ver manual de ruleta específica")
        print("2. Listar todas las ruletas disponibles")
        print("3. Búsqueda por mercado argentino")
        print("4. Volver al menú principal")
        
        choice = input("\nSelecciona opción (1-4): ").strip()
        
        if choice == "1":
            self.show_roulette_manual()
        elif choice == "2":
            self.list_roulettes()
        elif choice == "3":
            self.show_argentina_roulettes()
        elif choice == "4":
            return
        else:
            print("Opción inválida")

    def show_roulette_manual(self):
        """Muestra manual completo de una ruleta BCM específica"""
        models = self.db.roulettes.list_models()
        print("\nModelos de ruletas BCM disponibles:")
        for i, model in enumerate(models, 1):
            print(f"{i}. {model}")
        
        try:
            choice = int(input("\nSelecciona el modelo (1-{}): ".format(len(models))))
            if 1 <= choice <= len(models):
                model = models[choice - 1]
                roulette = self.db.roulettes.get_roulette(model)
                
                if roulette:
                    print(f"\n" + "=" * 60)
                    print(f"MANUAL TÉCNICO - {model}")
                    print("=" * 60)
                    
                    print(f"\n🏭 FABRICANTE: {roulette['fabricante']}")
                    print(f"🔧 TIPO: {roulette['tipo']}")
                    print(f"🌎 MERCADO: {roulette['mercado']}")
                    
                    print(f"\n⭐ CARACTERÍSTICAS:")
                    for caracteristica in roulette['caracteristicas']:
                        print(f"   • {caracteristica}")
                    
                    print(f"\n✅ VENTAJAS PARA ARGENTINA:")
                    for ventaja in roulette['ventajas_argentina']:
                        print(f"   • {ventaja}")
                    
                    print(f"\n⚙️  ESPECIFICACIONES TÉCNICAS:")
                    for espec, valor in roulette['especificaciones_tecnicas'].items():
                        print(f"   {espec}: {valor}")
                    
                    if 'conectores_principales' in roulette:
                        print(f"\n🔌 CONECTORES PRINCIPALES:")
                        for conector, descripcion in roulette['conectores_principales'].items():
                            print(f"   {conector}: {descripcion}")
                    
                    if 'sensores_incluidos' in roulette:
                        print(f"\n🔬 SENSORES INCLUIDOS:")
                        for sensor in roulette['sensores_incluidos']:
                            print(f"   • {sensor}")
                    
                    if 'codigos_error_comunes' in roulette:
                        print(f"\n❌ CÓDIGOS DE ERROR COMUNES:")
                        for codigo, solucion in roulette['codigos_error_comunes'].items():
                            print(f"   {codigo}: {solucion}")
                    
                    print(f"\n🔧 MANTENIMIENTO RECOMENDADO:")
                    for tarea in roulette['mantenimiento_recomendado']:
                        print(f"   • {tarea}")
                    
                    if 'problemas_comunes' in roulette:
                        print(f"\n⚠️  PROBLEMAS COMUNES:")
                        for problema in roulette['problemas_comunes']:
                            print(f"   • {problema}")
                    
                    if 'precio_estimado' in roulette:
                        print(f"\n💰 PRECIO ESTIMADO: {roulette['precio_estimado']}")
                    
                    if 'disponibilidad_argentina' in roulette:
                        print(f"\n📦 DISPONIBILIDAD ARGENTINA: {roulette['disponibilidad_argentina']}")
                        
                else:
                    print("No se encontró manual para este modelo")
            else:
                print("Selección inválida")
        except ValueError:
            print("Por favor ingresa un número válido")

    def list_roulettes(self):
        """Lista todas las ruletas BCM disponibles"""
        models = self.db.roulettes.list_models()
        roulettes_data = self.db.roulettes.roulettes
        
        print(f"\n" + "=" * 60)
        print("LISTA COMPLETA DE RULETAS BCM")
        print("=" * 60)
        
        print(f"\n🎯 TOTAL DE MODELOS: {len(models)}")
        
        for model in models:
            info = roulettes_data[model]
            print(f"\n🎰 {model}")
            print(f"   Tipo: {info['tipo']}")
            print(f"   Mercado: {info['mercado']}")
            print(f"   Especificaciones: {info['especificaciones_tecnicas'].get('dimensiones', 'N/A')}")

    def show_argentina_roulettes(self):
        """Muestra ruletas específicas para el mercado argentino"""
        argentina_roulettes = self.db.roulettes.get_roulettes_by_market("Argentina")
        
        print(f"\n" + "=" * 60)
        print("RULETAS BCM RECOMENDADAS PARA ARGENTINA")
        print("=" * 60)
        
        if argentina_roulettes:
            for model, info in argentina_roulettes.items():
                print(f"\n🎰 {model}")
                print(f"   💡 {info['tipo']}")
                print(f"   ⚙️  Voltaje: {info['especificaciones_tecnicas']['voltaje']}")
                print(f"   💰 Precio: {info.get('precio_estimado', 'Consultar')}")
                print(f"   📦 Disponibilidad: {info.get('disponibilidad_argentina', 'Inmediata')}")
        else:
            print("No se encontraron ruletas específicas para Argentina")

    def list_all_models_flow(self):
        """Lista todos los modelos disponibles en el sistema"""
        print(f"\n" + "=" * 60)
        print("LISTA COMPLETA DE MODELOS DISPONIBLES")
        print("=" * 60)
        
        # Modelos de máquinas
        manuals = self.db.get_manuals()
        print(f"\n🎰 MÁQUINAS TRAGAMONEDAS ({len(manuals)} modelos):")
        manufacturers = {}
        for manual in manuals:
            manufacturer = manual['manufacturer']
            if manufacturer not in manufacturers:
                manufacturers[manufacturer] = []
            manufacturers[manufacturer].append(manual['model'])
        
        for manufacturer, models in manufacturers.items():
            print(f"\n  🏭 {manufacturer}:")
            for model in models:
                print(f"     • {model}")
        
        # Aceptadores de billetes
        bill_models = self.db.bill_acceptors.list_models()
        print(f"\n💰 ACEPTADORES DE BILLETES ({len(bill_models)} modelos):")
        bill_manufacturers = {}
        for model in bill_models:
            manual = self.db.bill_acceptors.get_manual(model)
            if manual:
                manufacturer = manual['fabricante']
                if manufacturer not in bill_manufacturers:
                    bill_manufacturers[manufacturer] = []
                bill_manufacturers[manufacturer].append(model)
        
        for manufacturer, models in bill_manufacturers.items():
            print(f"\n  🏭 {manufacturer}:")
            for model in models:
                print(f"     • {model}")
        
        # Ruletas BCM
        roulette_models = self.db.roulettes.list_models()
        print(f"\n🎰 RULETAS BCM ({len(roulette_models)} modelos):")
        for model in roulette_models:
            roulette = self.db.roulettes.get_roulette(model)
            if roulette:
                print(f"  • {model} - {roulette['tipo']}")
        
        # Fuentes de poder
        power_models = self.db.power_diagrams.list_models()
        print(f"\n⚡ FUENTES DE PODER ({len(power_models)} modelos):")
        for model in power_models:
            print(f"  • {model}")
        
        print(f"\n📊 RESUMEN TOTAL:")
        print(f"   🎰 Máquinas: {len(manuals)} modelos")
        print(f"   💰 Aceptadores: {len(bill_models)} modelos") 
        print(f"   🎰 Ruletas BCM: {len(roulette_models)} modelos")
        print(f"   ⚡ Fuentes: {len(power_models)} modelos")
        print(f"   📚 TOTAL: {len(manuals) + len(bill_models) + len(roulette_models) + len(power_models)} modelos en sistema")

# ==================== EJECUCIÓN PRINCIPAL ====================
if __name__ == "__main__":
    ai = CompleteSlotTechnicianAI()
    ai.start()
