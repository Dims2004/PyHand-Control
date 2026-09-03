# 🖐️ PyHandControl

### Computer Vision-Based Virtual Desktop Control Using Hand Gestures

PyHandControl adalah project **Computer Vision** yang memungkinkan pengguna berinteraksi dengan media digital menggunakan **gesture tangan secara real-time**.

Dengan bantuan kamera, sistem mendeteksi posisi dan gesture tangan menggunakan **MediaPipe**, kemudian menggunakan gesture tersebut untuk mengambil, memindahkan, dan melepaskan gambar pada dua virtual desktop.

Project ini juga terintegrasi dengan **Telegram Bot API**, sehingga media yang dipindahkan dari Desktop 1 ke Desktop 2 dapat dikirimkan secara otomatis ke Telegram.

---

## 🎥 Project Demo

Sistem bekerja dengan kamera sebagai sensor gesture.

Alur interaksi:

```text
Camera
   │
   ▼
Hand Detection
   │
   ▼
Hand Landmark Tracking
   │
   ▼
Gesture Recognition
   │
   ├── Open Hand → Navigasi Media
   │
   ├── Fist → Mengambil Media
   │
   └── Open Hand → Melepaskan Media
   │
   ▼
Virtual Desktop
   │
   ├── Desktop 1
   │
   └── Desktop 2
          │
          ▼
     Telegram Bot
