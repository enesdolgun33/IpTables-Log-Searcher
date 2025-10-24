import re

def get_user_input():
    """
    Kullanıcıdan IP adresi ve arama tipini alır.
    """
    ip_adresi = ""
    while not ip_adresi:
        ip_adresi = input("Lütfen aranacak IP adresini girin (örn: 192.168.2.89): ").strip()

    arama_tipi = ""
    while arama_tipi not in ["Source", "Destination", "Any"]:
        arama_tipi = input("Arama tipini seçin (Source/Destination/Any): ").strip().capitalize()
        if arama_tipi not in ["Source", "Destination", "Any"]:
            print("Hatalı seçim! Lütfen 'Source', 'Destination' veya 'Any' yazın.")
    
    return ip_adresi, arama_tipi

def find_ip_in_log(log_file, ip_to_find, search_type):
    """
    Log dosyasında IP'yi arar ve eşleşen satırları döndürür.
    """
    found_lines = []
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                
                src_match = re.search(r"SRC=([\d\.]+)", line)
                dst_match = re.search(r"DST=([\d\.]+)", line)
                
                src_ip = src_match.group(1) if src_match else None
                dst_ip = dst_match.group(1) if dst_match else None

                match_found = False
                if search_type == "Source" and src_ip == ip_to_find:
                    match_found = True
                elif search_type == "Destination" and dst_ip == ip_to_find:
                    match_found = True
                elif search_type == "Any" and (src_ip == ip_to_find or dst_ip == ip_to_find):
                    match_found = True
                
                if match_found:
                    found_lines.append(line)

    except FileNotFoundError:
        print(f"HATA: '{log_file}' dosyası bulunamadı.")
        print("Lütfen 'ipTables.log' adında bir dosyanın kodla aynı dizinde olduğundan emin olun.")
        return None 
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")
        return None 

    return found_lines

def write_to_html(output_file, lines, ip_to_highlight):
    """
    Bulunan satırları bir HTML dosyasına yazar ve IP'yi vurgular.
    """
   
    highlight_tag = f'<span style="background-color: yellow; color: red;">{ip_to_highlight}</span>'

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            
            f.write("<!DOCTYPE html>\n")
            f.write("<html lang='tr'>\n<head>\n")
            f.write("    <meta charset='UTF-8'>\n")
            f.write("    <title>ipTables Log Arama Sonuçları</title>\n")
            f.write("    <style> body { font-family: monospace; } </style>\n")
            f.write("</head>\n<body>\n")
            f.write(f"<h1>Arama Sonuçları: '{ip_to_highlight}'</h1>\n")

            if not lines:
                f.write("<p>Belirtilen IP adresi için sonuç bulunamadı.</p>\n")
            else:
                f.write("<ul>\n")
                for line in lines:
                    safe_line = line.replace("<", "&lt;").replace(">", "&gt;")
                    highlighted_line = re.sub(rf"(\b{re.escape(ip_to_highlight)}\b)", highlight_tag, safe_line)
                    f.write(f"    <li>{highlighted_line}</li>\n")
                f.write("</ul>\n")
            
            f.write("</body>\n</html>\n")
        
        print(f"İşlem tamamlandı. Sonuçlar '{output_file}' dosyasına yazıldı.")

    except IOError:
        print(f"HATA: '{output_file}' dosyası yazılamadı. İzinleri kontrol edin.")
    except Exception as e:
        print(f"HTML yazılırken bir hata oluştu: {e}")

def main():
    log_file = "ipTables.log"
    output_file = "sonuc.html"
    
    ip_adresi, arama_tipi = get_user_input()
    
    print(f"'{log_file}' dosyasında '{ip_adresi}' IP'si '{arama_tipi}' tipinde aranıyor...")
    
    eslesen_satirlar = find_ip_in_log(log_file, ip_adresi, arama_tipi)
    
    if eslesen_satirlar is not None:
        write_to_html(output_file, eslesen_satirlar, ip_adresi)

if __name__ == "__main__":
    main()