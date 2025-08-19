import tkinter as tk
from tkinter import filedialog
from PIL import Image

def resmi_siyah_beyaz_yap():
    
    
    root = tk.Tk()
    root.withdraw()

    
    print("Lütfen siyah beyaza dönüştürmek istediğiniz resmi seçin...")
    dosya_yolu = filedialog.askopenfilename(
        title="Dönüştürülecek Resmi Seçin",
        filetypes=[("Resim Dosyaları", "*.jpg *.jpeg *.png *.bmp *.gif"), 
                   ("Tüm Dosyalar", "*.*")]
    )

    
    if not dosya_yolu:
        print("İşlem iptal edildi. Hiçbir dosya seçilmedi.")
        return

    
    try:
        
        renkli_resim = Image.open(dosya_yolu)

        
        siyah_beyaz_resim = renkli_resim.convert('L')
        
        print(f"'{dosya_yolu}' başarıyla yüklendi ve dönüştürmeye hazır.")

    except Exception as e:
        print(f"Resim açılırken veya dönüştürülürken bir hata oluştu: {e}")
        return

    
    print("Lütfen dönüştürülen resmi nereye kaydedeceğinizi seçin...")
    kayit_yolu = filedialog.asksaveasfilename(
        title="Siyah Beyaz Resmi Kaydet",
        defaultextension=".png", 
        filetypes=[("PNG Dosyası", "*.png"),
                   ("JPEG Dosyası", "*.jpg"),
                   ("BMP Dosyası", "*.bmp"),
                   ("Tüm Dosyalar", "*.*")]
    )

    
    if not kayit_yolu:
        print("Kayıt işlemi iptal edildi.")
        return

   
    try:
        siyah_beyaz_resim.save(kayit_yolu)
        print(f"Resim başarıyla '{kayit_yolu}' konumuna kaydedildi!")
         
    except Exception as e:
        print(f"Resim kaydedilirken bir hata oluştu: {e}")



if __name__ == "__main__":
    resmi_siyah_beyaz_yap()
