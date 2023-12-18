import ffmpeg

# pip3 install ffmpeg-python
# test link http://playertest.longtailvideo.com/adaptive/bipbop/gear4/prog_index.m3u8
stream = ffmpeg.input('http://playertest.longtailvideo.com/adaptive/bipbop/gear4/prog_index.m3u8')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)
