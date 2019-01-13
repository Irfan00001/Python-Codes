#Song Program
#Ed Sheeran
SongDicSets={}
print("--------------Song Album Details-----------------")
Artist="Ed Sheeran"
Album="Shape of You"
print("SingerName : "+Artist)
print("Album : "+Album)
print("-------------------------------------------------")
SongDicSets[Artist]=Album
#Louis Fonsi
Artist="Luis Fonsi"
Album="Despacito"
print("SingerName : "+Artist)
print("Album : "+Album)
print("--------------------------------------------------")
SongDicSets[Artist]=Album
#Micheal Jackson
Artist="Michael Jackson"
Album="They Don't Care About Us"
print("SingerName : "+Artist)
print("Album : "+Album)
print("--------------------------------------------------")
SongDicSets[Artist]=Album
print(SongDicSets)


while(True):
    ArtistName=input("Enter the Artist Name :")
    if ArtistName in SongDicSets:
        AlbumName=input("Guess the "+ArtistName+" Album :")
        if SongDicSets[ArtistName]==AlbumName:
            print("True")
            break
        else:
            print("False")
            break

    else:
        print("No Artist in the Record, Wrong Guess")
        continue
