from datetime import datetime
import time,sys
import datetime
try:
    import pyglet
except:
    print("Plz install pyglet")

def musik(vid_path):
    # vid_path='vid.mp4' # Nama Video
    window=pyglet.window.Window()
    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    MediaLoad = pyglet.media.load(vid_path)

    player.queue(MediaLoad)
    player.play()

    label = pyglet.text.Label('Happy Birthday',
                              font_name='Times New Roman',
                              font_size=36,
                              x=window.width // 2, y=window.height // 2,
                              anchor_x='center', anchor_y='center')

    @window.event
    def on_draw():
        window.clear()
        label.draw()
        if player.source and player.source.video_format:
            label.draw()
            player.get_texture().blit(50,50)


    pyglet.app.run()
    sys.exit()

def waktu(thn, bln, tgl, jam, menit):
    while True:
        future = datetime.datetime(thn, bln, tgl, jam, menit)
        a = datetime.datetime.now()
        print ('\r{}'.format(a), end='')
        time.sleep(1)
        if a > future:
            print ("\rHAPPY BIRTHDAY, Semoga Sehat Selalu dan Semua Keinginan Mu Dapat Terwujud ^__^v")
            break
if __name__ == "__main__":
    while True:
        print("Happy Birthday !!! \nAuthor : github.com/Anasg4\n")
        try:
            #Eng >> Year, month, date, hour, minute
            thn, bln, tgl, jam, menit = [int(x) for x in input("Masukan Rincian Ultah\nMasukan seperti ini dalam bentuk angka dan spasi >>  Tahun Bulan Tanggal Jam Menit \nKetik disini >> ").split()]
            video = input("Nama video contoh (ultah.mp4) = ")
            break
        except:
            print("Masukan Format dengan benar seperti ini dalam bentuk angka\n>>> Tahun Bulan Tanggal Jam Menit <<<<\nBerikan Spasi sebagai pemisah\n================================================================")
            continue
    waktu(thn, bln, tgl, jam, menit)
    musik(video)