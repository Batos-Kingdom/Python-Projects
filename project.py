import yt_dlp

def video_indir(link):
    try:
        ydl_opts = {
            'format': 'best',  # en iyi kalite
            'outtmpl': '%(title)s.%(ext)s',  # dosya adını video başlığı yapar
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        print("İndirme tamamlandı.")
    except Exception as e:
        print("Hata oluştu:", e)

link = input("YouTube video linkini girin: ")
video_indir(link)
