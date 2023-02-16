import pydub

# # files                                                                         
src = r".\home\ubuntu\up1\dead.mp3"

dst = r".\home\ubuntu\up1\dead.wav"

# convert wav to mp3                                                            
sound = pydub.AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
