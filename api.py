import pydub

# # files                                                                         
src = r".\audio\16_02_2023\ulatroi.mp3"

dst = r".\audio\16_02_2023\ulatroi1.wav"
# dst = r"E:\04-02-2023\folder1\ulatroi.wav"

# convert wav to mp3                                                            
sound = pydub.AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
