env_vars = {
  # Get From my.telegram.org
  "API_HASH": "f1ff78d3d0b3eaa825294af918318ac7",
  # Get From my.telegram.org
  "API_ID": "21531216",
  #Get For @BotFather
  "BOT_TOKEN": "7182062183:AAF3UFIS-uVADSY_jxUMHmnykhrUhHmHWdI",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://olwyjhgv:3366YUQaIZoBVNYdcp4ViwxLmrVzwoZK@bubble.db.elephantsql.com/olwyjhgv",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "-1002198221587",
  # Force Subs Channel username without @
  "CHANNEL": "Manga_Blast",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "Chapter - {chap_num} {chap_name} @Manga_Blast",
  # Put Thumb Link 
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
