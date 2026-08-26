# Analisis-de-Signals-Seriales-UART-RS232-con-Analizador-Logico

**Universidad Militar Nueva Granada — Asignatura: Comunicaciones Digitales**

**Autores:** Riveros Sierra Harol Felipe (1401660), Bohorquez Blanco Salome (1401654)
**Docente:** Ing. José de Jesús Rugeles Uribe

## Descripción

Este repositorio contiene el desarrollo de la práctica de laboratorio sobre análisis de señales seriales UART/RS232 mediante un analizador lógico digital de 8 canales (24 MHz máx.). Se utiliza una **Raspberry Pi Pico 2W** programada en **MicroPython** como fuente de la trama UART, y se estudia experimentalmente la relación entre la frecuencia de muestreo del instrumento, el número de muestras por bit y la tasa de baudios configurada.

## Objetivos

- Comprobar la relación entre el tiempo de bit y la tasa de transmisión de datos.
- Analizar los niveles y características de una comunicación serial UART/RS232.
- Analizar la estructura del protocolo (bit de inicio, bits de datos, paridad y bit(s) de parada).
- Comprender el funcionamiento y las limitaciones de los analizadores lógicos.
- Desarrollar habilidades de programación en MicroPython.

## Estructura del repositorio

```
4 laboratorio comunicacion digital/
└── 4.2/
    ├── ANALIZADOR_LOGICO.docx                                                    # Informe completo del laboratorio
    ├── Análisis de muestras por bit según la tasa de transmisión...xlsx          # Tabla de análisis baudrate vs. frecuencia de muestreo
    ├── Codigo para la letra u.py                                                 # Script MicroPython: envío del carácter 'U' (9600 baudios)
    ├── Codigo para el mensaje.py                                                 # Script MicroPython: envío de la trama completa (57600 baudios)
    ├── Captura para la leetra U.sal                                              # Captura del analizador lógico (letra U)
    ├── Captura para la letra s.sal                                               # Captura del analizador lógico (mensaje completo)
    ├── csv de la letra U.txt                                                     # Exportación CSV de la captura (letra U)
    ├── envio de varios caracteres u.png                                          # Evidencia: captura decodificada, carácter U
    └── envio de la frase umng 2026 lider en telecomunicaciones.png               # Evidencia: captura decodificada, trama completa
```

## Hardware y software utilizados

| Elemento | Detalle |
|---|---|
| Microcontrolador | Raspberry Pi Pico 2W (RP2350) |
| Firmware | MicroPython |
| Pines usados | GPIO0 (TX), GPIO1 (RX), GND |
| Instrumento de medida | Analizador lógico USB, 8 canales, hasta 24 MS/s |
| Software de captura | Analizador de protocolo Async Serial (decodificación UART) |

## Configuración UART empleada

| Script | Baudrate | Bits de datos | Paridad | Bits de parada |
|---|---|---|---|---|
| `Codigo para la letra u.py` | 9600 | 8 | None | 1 |
| `Codigo para el mensaje.py` | numeros de baudios | 8 | 1 (Odd) | 1 |

## Cómo reproducir la práctica

1. Cargar el script MicroPython deseado en la Raspberry Pi Pico 2W (usando Thonny u otro IDE compatible).
2. Conectar el pin TX (GPIO0) y GND de la Pico al canal correspondiente del analizador lógico.
3. Configurar el software de captura con la frecuencia de muestreo deseada y añadir el decodificador Async Serial con los parámetros de la tabla anterior.
4. Ejecutar el script en la Pico y capturar la señal.
5. Exportar la captura (`.sal` / `.csv`) y verificar la decodificación contra el mensaje enviado.

## Contenido del informe

El informe (`ANALIZADOR_LOGICO.docx`) desarrolla el marco teórico (trama UART, tasa de baudios, bit de paridad, criterio de Nyquist, muestras por bit, RS232 vs. UART de nivel lógico, error de cuantización temporal) y presenta los resultados experimentales obtenidos con el montaje descrito.
