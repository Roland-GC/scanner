import sys
import requests
import nmap
import socket

GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_banner():
    print(BLUE + """
    ==================================================
    [+] PENTESTING & OSINT WEB SCANNER ACTIVADO
    [+] Perfil: Auditoría Inicial Automática
    ==================================================
    """ + RESET)

def check_security_headers(url):
    print(BLUE + f"\n[*] Analizando cabeceras de seguridad para: {url}" + RESET)
    if not url.startswith("http"):
        url = "https://" + url
    
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        # Cabeceras críticas a verificar
        critical_headers = ["X-Frame-Options", "Content-Security-Policy", "Strict-Transport-Security"]
        
        for header in critical_headers:
            if header in headers:
                print(GREEN + f"[+] {header}: Configurada correctamente ({headers[header][:30]}...)" + RESET)
            else:
                print(RED + f"[-] CRÍTICO: Falta la cabecera {header} (Riesgo de Clickjacking/XSS)" + RESET)
    except requests.exceptions.RequestException as e:
        print(RED + f"[-] Error al conectar con la URL: {e}" + RESET)

def scan_ports(target):
    print(BLUE + f"\n[*] Iniciando escaneo de puertos Nmap en: {target}" + RESET)
    try:
        # Traducir dominio a IP si es necesario
        ip = socket.gethostbyname(target)
        nm = nmap.PortScanner()
        
        # Escaneamos los puertos más comunes: 21, 22, 80, 443, 8080
        print(f"[*] Escaneando IP: {ip}...")
        nm.scan(ip, '21,22,80,443,8080', arguments='-sV')
        
        for host in nm.all_hosts():
            print(f"[+] Host: {host} ({nm[host].hostname()})")
            print(f"[+] Estado: {nm[host].state()}")
            
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in ports:
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port]['version']
                    print(GREEN + f"    -> Puerto {port}/{proto}: {state} | Servicio: {service} (Ver: {version})" + RESET)
    except Exception as e:
        print(RED + f"[-] Error en el escaneo de puertos: {e}" + RESET)

def brute_force_subdomains(domain):
    print(BLUE + f"\n[*] Iniciando OSINT de subdominios para: {domain}" + RESET)
    
    # Lista corta de prueba (puedes expandirla con un diccionario .txt)
    subdomains_to_test = ["www", "mail", "dev", "staging", "admin", "api", "vpn", "blog"]
    
    for sub in subdomains_to_test:
        subdomain = f"{sub}.{domain}"
        try:
            # Intentamos resolver la IP del subdominio
            ip = socket.gethostbyname(subdomain)
            print(GREEN + f"[+] Subdominio encontrado: {subdomain} -> IP: {ip}" + RESET)
        except socket.gaierror:
            # Si no resuelve, pasamos de largo
            continue

if __name__ == "__main__":
    print_banner()
    
    # Solicitar objetivo por consola si no se pasa por argumento
    if len(sys.argv) > 1:
        target_domain = sys.argv[1]
    else:
        target_domain = input("Introduce el dominio objetivo (ej: scanme.nmap.org): ")
    
    # Ejecución de los módulos
    brute_force_subdomains(target_domain)
    check_security_headers(target_domain)
    scan_ports(target_domain)
    
    print(BLUE + "\n[+] Análisis finalizado." + RESET)
