# cantonese-syllabary
Data preparation for visualizing the Cantonese syllabary in Tableau or other tools

# Data format
The script `readcantofile.py` generates the data in `phonemes.csv`. Currently, the columns currently in `phonemes.csv` (intented for consumption by Tableau) are:
1. jyutping with tone
2. count homophones
3. jyutping without tone
4. initial letter of the jyutping,
5. first homophone character
6. full list of homophone characterss.

Example of a row:
`aat3, 13, aat, 3, a, 壓, 壓歹押遏揠戛頞堨齃恝餲猒閼`

# Original data source
The raw data in `canto-phones-raw.csv` is extracted from files included in the Jyutping IME by Dominic Yu,
which is based on LSHK table and downloadable from [http://blyt.net/domingo2/Chinese.html](http://blyt.net/domingo2/Chinese.html)

# Data visualization
An early prototype of the visualization can be found at [https://public.tableau.com/profile/denise.mak#!/vizhome/CantonesePhonemesv0_1/canto-tone-dash](https://public.tableau.com/profile/denise.mak#!/vizhome/CantonesePhonemesv0_1/canto-tone-dash)
