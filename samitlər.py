def samitleri_al(metn):
    samitler = set()
    for herf in metn:
        if herf.lower() not in ['a', 'ə', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü' , ' ']:
            samitler.add(herf.lower())
    return samitler
