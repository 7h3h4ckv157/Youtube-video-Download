import pytube; source = input("enter the link:")
src = pytube.YouTube(source)
hack=src.streams.first()
hack.download()
