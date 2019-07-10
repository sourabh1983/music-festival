import operator


# Record label object consists of record label name and list of bands
class RecordLabel:
    def __init__(self, name):
        self.name = name
        self.bands = []

    def add_band(self, band):
        if not self.band_exists_in_record_label(band):
            self.bands.append(band)
            self.bands = sorted(self.bands, key=operator.attrgetter('name'))

    def band_exists_in_record_label(self, band):
        if any(mf.name == band.name for mf in self.bands):
            return True
        return False

    '''
    Formats Output in below format:
    Still Bottom Records
            Wild Antelope
                    Trainerella
    XS Recordings
            Werewolf Weekday
                    LOL-palooza
    unknownLabel
            Squint-281
                    Twisted Tour
    '''
    def __str__(self):
        return self.name + '\n' + '\n'.join(
            [
                '\t' + band.name + '\n'.join(
                    [
                        '\n\t\t' + mfest.name for mfest in band.music_festivals
                    ]
                ) for band in self.bands
            ]
        )


# Band object consist of band name and list of music festivals
class Band:
    name = None
    music_festivals = []

    def __init__(self, name):
        self.name = name
        self.music_festivals = []

    def add_music_festival(self, music_festival):
        if not self.music_festival_exists_in_band(music_festival):
            self.music_festivals.append(music_festival)
            self.music_festivals = sorted(self.music_festivals, key=operator.attrgetter('name'))

    def music_festival_exists_in_band(self, music_festival):
        if any(mf.name == music_festival.name for mf in self.music_festivals):
            return True
        return False


# Music festival object consists of name
class MusicFestival:
    def __init__(self, name):
        self.name = name
