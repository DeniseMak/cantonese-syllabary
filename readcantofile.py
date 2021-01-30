'''
Reads canto-phones-raw.csv to generate rimes.csv and phones.csv

canto-phones-raw.csv is extracted from files included in the Jyutping IME by Dominic Yu,
which is based on LSHK table and downloadable from http://blyt.net/domingo2/Chinese.html

The columns currently in phonemes.csv (intented for consumption by Tableau) are:
jyutping_with_tone, count_homophones, jyutping_without_tone, initial letter of the jyutping,
first homophone character, full list of homophone characters.

Example:
aat3, 13, aat, 3, a, 壓, 壓歹押遏揠戛頞堨齃恝餲猒閼
'''


def has_tone(sound_string):
    tones = ['1','2','3','4','5','6']
    if len(sound_string) > 0:
        if sound_string[len(sound_string)-1] in tones:
            return True
        else:
            return False

file1 = open('canto-phones-raw.csv', 'r', encoding='utf-8')
Lines = file1.readlines()

file_len = len(Lines)
print("The file has {} lines.".format(file_len))

vocab_counts = {}
toneless_counts = {}
charlist_lists = {}
tone_counts = {}

num_sounds = 0
begun = False
for line in Lines:
    sound_list = line.split()

    # skip preamble
    if not begun and len(sound_list) > 0 and sound_list[0] == 'BEGINCHARACTER':
        begun = True

    if begun and len(sound_list) > 1:
        num_sounds += 1
        sound = sound_list[0]
        chars = sound_list[1]
        char_string = ''.join(chars.split(','))
        charlist_lists[sound] = char_string

        if has_tone(sound):
            if sound not in tone_counts:
                tone_counts[sound] = len(char_string)
            else:
                print('Warning: sound {} appeared more than once'.format(sound))
        else:
            if sound not in toneless_counts:
                toneless_counts[sound] = len(char_string)

        char_list = sound_list[1].split(',')
        for c in char_list:
            if c in vocab_counts:
                vocab_counts[c] +=1
            else:
                vocab_counts[c] = 1
        # print("sound={}, chars={}".format(sound_list[0], sound_list[1]))

print("# entries={}, #phonemes={}, # chars={}, #rimes(without tone distinctions)={}".format(
    num_sounds, len(tone_counts), len(vocab_counts), len(toneless_counts)))


# rimes

with open('rimes.csv', 'w', encoding='utf-8') as rimefile:
    for key, value in toneless_counts.items():
        rimefile.write(key + ', ' + str(value)) # the sound, the count of tone-agnostic homophones
        char_list = charlist_lists[key]
        first_ch = char_list[0]
        rimefile.write(', '+ char_list[0]) # first char, for the visualization
        rimefile.write(', '+ char_list)    # char list
        rimefile.write('\n')

with open('phonemes.csv', 'w', encoding='utf-8') as phonefile:
    for key, value in tone_counts.items():
        phonefile.write(key + ', ' + str(value)) # the sound, the count of homophones
        char_list = charlist_lists[key]
        first_ch = char_list[0]
        # tone is last char of key
        tone = key[len(key)-1]
        rime = key[:(len(key)-1)]
        phonefile.write(', ' + rime)
        phonefile.write(', ' + tone)  # tone number from 1-6
        initial = rime[0]
        if rime[0] == 'g' or rime[0]== 'k':
            if rime[1] == 'w':
                initial += rime[1]
        if rime[0] == 'n' :
            if rime[1] == 'g':
                initial += rime[1]
        phonefile.write(', ' + initial)
        phonefile.write(', ' + char_list[0])  # first char, for the visualization
        phonefile.write(', ' + char_list)     # list of chararcters
        phonefile.write('\n')


