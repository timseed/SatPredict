fake_tle = """OSCAR 7 (AO-7)
1 07530U 74089B   20201.87118354 -.00000042  00000-0  19725-4 0  9990
2 07530 101.8016 171.4337 0011910 303.3629  84.8626 12.53644246 90053
UOSAT 2 (UO-11)
1 14781U 84021B   20202.00960294  .00000058  00000-0  13214-4 0  9990
2 14781  97.5893 212.3639 0010048  93.7853 266.4511 14.83178810957656
SAUDISAT 1C (SO-50)
1 27607U 02058C   20201.62679157 -.00000040  00000-0  14827-4 0  9996
2 27607  64.5554 276.0014 0043919 167.5041 192.7161 14.75646851945476
FOX-1D (AO-92)
1 43137U 18004AC  20202.17900275  .00000591  00000-0  27210-4 0  9999
2 43137  97.4444 273.1171 0007703 307.2392  52.8142 15.24173144140028
ISS (ZARYA)
1 25544U 98067A   20202.20401620 -.00000117  00000-0  59461-5 0  9991
2 25544  51.6421 185.0514 0001366 134.5482  43.1038 15.49516517237137
SAUDISAT 1C (SO-50)
1 27607U 02058C   20201.62679157 -.00000040  00000-0  14827-4 0  9996
2 27607  64.5554 276.0014 0043919 167.5041 192.7161 14.75646851945476
"""

cfg_dir = '/user/.mysat/'

cfg = \
        """[Location]
lat = 15.3
lon = 120.2
alt = 50
name = "Arayat"

[Track]
sats = AO-92,SO-50,ISS,

[Pass]
minalt = 20.0

[Tle]
files = 'https://www.celestrak.com/NORAD/elements/amateur.txt,'
"""

cfg_as_dict = {'Location': {'alt': '50', 'lat': '15.3', 'lon': '120.2', 'name': '"Arayat"'},
 'Pass': {'minalt': '20.0'},
 'Tle': {'files': "'https://www.celestrak.com/NORAD/elements/amateur.txt,'"},
 'Track': {'sats': ['AO-92', 'SO-50', 'ISS']}}