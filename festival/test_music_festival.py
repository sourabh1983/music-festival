from .music_festival import Band, MusicFestival, RecordLabel


def test_record_label_should_not_add_duplicate_band():
    record_label = RecordLabel('record label 1')
    band1 = Band('band 1')
    band2 = Band('band 1')
    record_label.add_band(band1)
    record_label.add_band(band2)
    assert record_label.bands == [band1]


def test_band_should_not_add_duplicate_music_festival():
    band = Band('band 1')
    mfest1 = MusicFestival('mfest1')
    mfest2 = MusicFestival('mfest1')
    band.add_music_festival(mfest1)
    band.add_music_festival(mfest2)
    assert band.music_festivals == [mfest1]


def test_bands_are_sorted_in_record_label():
    record_label = RecordLabel('record label 1')
    band1 = Band('B1')
    band2 = Band('A2')
    record_label.add_band(band1)
    record_label.add_band(band2)
    assert record_label.bands == [band2, band1]


def test_music_festivals_are_sorted_in_bands():
    band = Band('Band 1')
    mfest1 = MusicFestival('B1')
    mfest2 = MusicFestival('A2')
    band.add_music_festival(mfest1)
    band.add_music_festival(mfest2)
    assert band.music_festivals == [mfest2, mfest1]
