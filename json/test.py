import json

data = {
    "president" : {
        "name": "jacques chirac",
        "species": "reptilian(lol)",
    }
}

with open("president.json", "w") as write_file:
    json.dump(data, write_file)


tentation_links = [
    "https://drive.google.com/file/d/1TvudkrQDQDgHsKpqXb1iBcsemARNV9WK/preview",
    "https://drive.google.com/file/d/1Bs2F9RMgnxIEJFosbGPstNa9_bWgMrd-/preview",
    "https://drive.google.com/file/d/1iJ9yTRQy7o7hyf3od6ZC3J4KTks_J09Q/preview",
    "https://drive.google.com/file/d/1WaYpTU-Y7AK12FhmP30l8nM5SbwFVHwr/preview"]

ex_revanche_links = [
    "https://drive.google.com/file/d/1ubDa9I_SALwkPmLikEmBKc-asdrWV1Oi/preview",
]


with open("bc.json", "w") as file:
    json.dump(tentation_links, file, indent=4)