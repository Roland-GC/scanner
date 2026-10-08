# # Custom Web Vulnerability & OSINT Scanner

Este repositorio contiene una herramienta de línea de comandos en **Python** diseñada para automatizar las fases de reconocimiento inicial (*Recon*), técnicas de enumeración en fuentes abiertas (**OSINT**) y auditoría de seguridad superficial sobre activos web y de red.

La aplicación integra de forma modular el análisis de la infraestructura de red mediante escaneos de puertos y la validación de configuraciones HTTP defensivas.

## 🚀 Características Principales

El escáner está estructurado en tres módulos de auditoría críticos:

*   **Enumeración de Subdominios (OSINT):** Realiza un descubrimiento pasivo de subdominios comunes mediante resolución DNS asíncrona por fuerza bruta para mapear la superficie de ataque del objetivo.
*   **Análisis de Cabeceras de Seguridad HTTP:** Evalúa el nivel de protección de la aplicación web auditando la presencia o ausencia de cabeceras de seguridad fundamentales (`X-Frame-Options`, `Content-Security-Policy` y `Strict-Transport-Security`) para mitigar riesgos de Clickjacking y XSS.
*   **Escaneo de Puertos y Detección de Servicios (Nmap):** Se conecta activamente al motor local de Nmap para escanear puertos críticos (`21, 22, 80, 443, 8080`), identificando de forma automatizada el estado de los hosts, los servicios en ejecución y las versiones de software (`-sV`).

## 📋 Requisitos Previos

Antes de ejecutar el script, asegúrate de cumplir con las siguientes dependencias en tu sistema operativo:

1.  **Python 3.x** instalado.
2.  **Nmap** (Binario oficial del sistema):
    *   **Windows:** Descarga e instala Nmap desde [nmap.org](https://nmap.org) y asegúrate de marcar la opción de **Npcap**. Verifica que la ruta esté añadida a las Variables de Entorno (`PATH`).
    *   **Linux (Debian/Ubuntu):** `sudo apt install nmap`
3.  Librerías de Python requeridas:
    ```bash
    pip install requests python-nmap
    ```

## 🛠️ Instalación y Uso

Clona este repositorio en tu máquina local y accede al directorio:

```bash
git clone https://github.com
cd nombre-repositorio
```

### Ejecución Directa

Puedes pasar el dominio objetivo directamente como un argumento por consola:

```bash
python scanner.py scanme.nmap.org
```

### Ejecución Interactiva

Si lanzas el script sin parámetros, la propia consola te solicitará de forma dinámica el objetivo a auditar:

```bash
python scanner.py
# Entrada por consola: Introduce el dominio objetivo (ej: scanme.nmap.org):
```

## 🖥️ Demostración de Salida (Output)

```text
    ==================================================
    [+] PENTESTING & OSINT WEB SCANNER ACTIVADO
    [+] Perfil: Auditoría Inicial Automática
    ==================================================
    
[*] Iniciando OSINT de subdominios para: scanme.nmap.org
[+] Subdominio encontrado: www.scanme.nmap.org -> IP: 45.33.32.156

[*] Analizando cabeceras de seguridad para: scanme.nmap.org
[-] CRÍTICO: Falta la cabecera X-Frame-Options (Riesgo de Clickjacking/XSS)
[-] CRÍTICO: Falta la cabecera Content-Security-Policy (Riesgo de Clickjacking/XSS)

[*] Iniciando escaneo de puertos Nmap en: scanme.nmap.org
[*] Escaneando IP: 45.33.32.156...
[+] Host: 45.33.32.156 (scanme.nmap.org)
[+] Estado: up
    -> Puerto 22/tcp: open | Servicio: ssh (Ver: OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13)
    -> Puerto 80/tcp: open | Servicio: http (Ver: Apache httpd 2.4.7)

[+] Análisis finalizado.
```

## ⚖️ Descargo de Responsabilidad (Disclaimer)

*Este script ha sido desarrollado estrictamente con fines educativos y de auditoría interna de ciberseguridad (Hacking Ético). El uso de esta herramienta contra objetivos sin una autorización previa y por escrito es totalmente ilegal. El autor no se hace responsable del uso indebido o de los daños causados por las acciones derivadas de este código. Realiza siempre tus pruebas sobre entornos controlados o plataformas autorizadas como `scanme.nmap.org`.*
