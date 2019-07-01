import operator

from festival.music_festival import Band, MusicFestival, RecordLabel

record_labels = []
bands = []
music_festivals = []


# function checks that if record label already exists then return record label
def record_label_exists(record_label):
    record_label = [rl for rl in record_labels if rl.name == record_label]
    if not record_label:
        return None
    return record_label[0]


'''
function will return data in below format:
[
    {
       "bands":[
          {
             "music_festivals":[
                {
                   "name":"LOL-palooza"
                }
             ],
             "name":"Frank Jupiter"
          },
          {
             "music_festivals":[
                {
                   "name": "Jill Black"
                }
             ],
             "name":"Propeller"
          }
       ],
       "name":"Pacific Records"
    },
]
'''


def restructure_data(music_festival_data):
    for data in music_festival_data:
        music_festival = MusicFestival(data.get('name', ''))
        for band in data['bands']:
            bnd = Band(band.get('name', ''))
            bnd.add_music_festival(music_festival)
            record_label = record_label_exists(band.get('recordLabel'))
            if record_label:
                record_label.add_band(bnd)
            else:
                record_label = RecordLabel(band.get('recordLabel', 'unknownLabel'))
                record_label.add_band(bnd)
                record_labels.append(record_label)
    return record_labels


def sort_data(data):
    return sorted(data, key=operator.attrgetter('name'))


def print_formatted_result(music_festival_data):
    for record_label in music_festival_data:
        print(record_label)


def run_music_festival(music_festival_data):
    if music_festival_data:
        music_festival_data = restructure_data(music_festival_data)
        music_festival_data = sort_data(music_festival_data)
        print_formatted_result(music_festival_data)
    else:
        print('Error fetching data from api')


if __name__ == "__main__":
    from service import get_festivals
    run_music_festival(get_festivals())
