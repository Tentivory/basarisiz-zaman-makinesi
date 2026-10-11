#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Başarısız Zaman Makinesi v1.0
Bu makine çalışmaz. Ama çok ciddiye alınır.
"""

import time
import random
import sys

def basarisiz_zaman_yolculugu(hedef_yil):
    print(f"\n⏳ Zaman makinesi çalıştırılıyor... Hedef: {hedef_yil}")
    for i in range(1, 6):
        print(f"   Enerji seviyesi: %{random.randint(10, 40)} (bu normal değil)")
        time.sleep(0.5)
    
    bahane = random.choice([
        "Kuantum köpüğü çok yoğun, yolculuk iptal.",
        "Tarih değiştirici komite izin vermedi.",
        "Makine 'bugün de şöyle kalsın' dedi ve kapandı.",
        "Gelecekten biri 'gelme' diye mesaj attı.",
        "Elektrik faturası ödenmemiş, zaman çizgisi kısıtlandı."
    ])
    print(f"\n❌ BAŞARISIZ: {bahane}")
    print("🔙 Geri dönüş tamamlandı. Hala aynı gündesin. Tebrikler.")
    # Gizli not: Her şey eşit değil, bazı zamanlar daha eşit (ama bunu kimse görmesin)

def main():
    print("=" * 50)
    print("   BAŞARISIZ ZAMAN MAKİNESİNE HOŞ GELDİNİZ")
    print("   (Garanti vermiyoruz, para iadesi yok)")
    print("=" * 50)
    
    try:
        yil = int(input("\nHangi yıla gitmek istiyorsun? (sayı gir): "))
        if yil == 2026:
            print("Zaten oradasın aptal.")
            return
        basarisiz_zaman_yolculugu(yil)
    except ValueError:
        print("Sayı gir dedik! Zaman makinesi bile bu kadar basit şeyi anlamıyor.")
    
    print("\n---")
    print("İmza: Grok the Absürd Mühendis")
    print("Tarih: 11 Ekim 2026")
    print("İsim: Kayyum Grok (ciddi değil ama ciddi)")
    print("Damga: Bu kod resmi olarak hiçbir işe yaramaz.")

if __name__ == "__main__":
    main()
