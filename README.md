
## Fake News Crawler 
![Build Status](https://img.shields.io/github/workflow/status/damnever/pigar/PyCI?style=flat-square)
![Python](https://img.shields.io/pypi/pyversions/weibo-spider)

 
**Project**: [**Multi-Lingual COVID19 Fake News Detection and Intervention**](https:counterinfodemic/) <br>

- Generating fact-checking COVID19 News for COVID-19 Misinformation Detection and any other possible research tasks
  - Supporting restrict result by language code, such as "`zh` for `Chinese`, "`pt` for `Portuguese`" 
- Search all the fact-checked news which warping in [Google Fact Check API](https://developers.google.com/fact-check/tools/api)
- Translating text  and detecting news whose language used 

---
### API KEY
To used the scripts, several API keys need to be set up and stored in the file named `.env`. The `GOOGLE_API_KEY` can be generated from [here](https://cloud.google.com/docs/authentication/api-keys).Toturial of how to upload the JSON file into variable `GOOGLE_TRANSLATION_API_PATH` can be found [here](https://docs.zeet.co/cloud/gcp/)

```
GOOGLE_API_KEY=XXXX
GOOGLE_TRANSLATION_API_PATH=XXXX

```



### Installation
Fork or download this repo and then
```
pip3 install -r requirements.txt
```

### Usage
- We make it as easy as possible, all you need to is inputting query and news will automatically download in folder of `./data/news`
```
COVID19 News Crawler Initialized

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY [QUERY ...], --query QUERY [QUERY ...]
                        Examples: -q item1 item2, -q item3
  -lang , --language_code 
                        restrict language for returned news
  -num , --number_of_result 
```

- Example: search news by keyword of "COVID-19, Omicron" (separate by space)
  ```
  python crawler.py -q COVID-19, Omicron

  ```

  If you would like to restrict search result by [language code](https://cloud.google.com/translate/docs/languages)
  ```
  python crawler.py -q COVID-19, Omicron -lang zh
  ```

  If you would like to return number of results for each query:
  ```
  python crawler.py -q COVID-19, Omicron -num 20
  ```
- Put it all together:
  ```
  python crawler.py -q COVID19A Omicron -num 20
  ```
  The output will be like:
  ```
  GET request returned 20 news for COVID19.
  GET request returned 20 news for Omicron.
  Successfully collected 40 news 
  data have been downloaded in ..API/data/news/COVID19_Omicron_2022-10-20_04:21:58.559290.csv successfully
  ```


### Language Code (ISO639)
- `am`     # Amharic
- `ar`     # Arabic
- `hy`     # Armenian
- `eu`     # Basque
- `bn`     # Bengali
- `bs`     # Bosnian
- `bg`     # Bulgarian
- `my`     # Burmese
- `hr`     # Croatian
- `ca`     # Catalan
- `cs`     # Czech
- `da`     # Danish
- `nl`     # Dutch
- `en`     # English
- `et`     # Estonian
- `fi`     # Finnish
- `fr`     # French
- `ka`     # Georgian
- `de`     # German
- `el`     # Greek
- `gu`     # Gujarati
- `ht`     # Haitian Creole
- `iw`     # Hebrew
- `hi`     # Hindi
- `hu`     # Hungarian
- `is`     # Icelandic
- `in`     # Indonesian
- `it`     # Italian
- `ja`     # Japanese
- `kn`     # Kannada
- `km`     # Khmer
- `ko`     # Korean
- `lo`     # Lao
- `lv`     # Latvian
- `lt`     # Lithuanian
- `ml`     # Malayalam
- `mr`     # Marathi
- `ne`     # Nepali
- `no`     # Norwegian
- `or`     # Oriya
- `pa`     # Panjabi
- `ps`     # Pashto
- `fa`     # Persian
- `pl`     # Polish
- `pt`     # Portuguese
- `ro`     # Romanian
- `ru`     # Russian
- `sr`     # Serbian
- `zh-CN`  # Simplified Chinese
- `sd`     # Sindhi
- `si`     # Sinhala
- `sk`     # Slovak
- `sl`     # Slovenian
- `es`     # Spanish
- `sv`     # Swedish
- `tl`     # Tagalog
- `ta`     # Tamil
- `te`     # Telugu
- `th`     # Thai
- `zh-TW`  # Traditional Chinese
- `tr`     # Turkish
- `uk`     # Ukranian
- `ur`     # Urdu
- `ug`     # Uyghur
- `vi`     # Vietnamese
- `cy`     # Welsh
- `id`     # Indonesian
