def position(x, y):

    # This function finds position of each shot found in the csv file

    if y <= 7.8 and x > 22 or y <= 7.8 and x < -22:
        return 'C3'
    if x + y > 23.5 and y > 7.8:
        return 'NC3'
    if x + y < 23.5 and y >= 7.8 or y <= 7.8 and x < 22 or x + (y) > -23.5 and y >= 7.8 or y <= 7.8 and x > -22:
        return '2PT'

def main(csvfile):

    # This opens the given csv file

    fp = open(csvfile)
    fp.readline()
    file_in = fp.read().split('\n')

    # This prints a dictionary containing shot distribution and effective field goal %
    print('Team A:')
    print(stats_getter(file_in,'Team A'))
    print('Team B:')
    print(stats_getter(file_in,'Team B'))


def stats_getter(file_in, name):
    fgm = 0
    two_made = 0
    c3_made = 0
    nc3_made = 0
    threes_made = 0
    shot_attempts = 0
    efg2pt = 0
    efgc3 = 0
    efgnc3 = 0
    sd = {'C3': 0, 'NC3': 0, '2PT': 0, 'efg2PT': 0, 'efgC3': 0, 'efgNC3': 0}

    # This loops through each line in the csv file

    for row in file_in:
        if row != '':

            # Determines stats based off each line in the given csv file

            stats = row.split(',')
            team = stats[0]
            x = float(stats[1])
            y = float(stats[2])
            make = stats[3]
            pos = position(x,y)
            if team == name:
                if pos == '2PT':
                    sd['2PT'] += 1
                    if make == '1':
                        fgm += 1
                        two_made += 1
                if pos == 'NC3':
                    sd['NC3'] += 1
                    if make == '1':
                        threes_made += 1
                        nc3_made += 1
                if pos == 'C3':
                    sd['C3'] += 1
                    if make == '1':
                        threes_made += 1
                        c3_made += 1
                shot_attempts += 1
    for key in sd.keys():
        sd[key] /= shot_attempts
    sd['efg2PT'] = (fgm + (0.5 * 0))/(shot_attempts)
    sd['efgC3'] = (fgm + (0.5 * c3_made))/(shot_attempts)
    sd['efgNC3'] = (fgm + (0.5 * nc3_made))/(shot_attempts)
    return sd
