import discord
from discord.ext import commands 

import asyncio
import time
from datetime import datetime, timedelta

import aiohttp
import discord
import discord.ext.commands as commands








class fetch():


    async def fetch_anilist(title, method):
        def monthintext(number):
            idn = ["January", "February", "March", "April",
                    "May", "June", "July", "August",
                    "September", "October", "November", "December"]
            if number is None:
                return "Unknown"
            x = number - 1
            if x < 0:
                return "Unknown"
            return idn[number - 1]


        def create_time_format(secs):
            months = int(secs // 2592000) # 30 days format
            secs -= months * 2592000
            days = int(secs // 86400)
            secs -= days * 86400
            hours = int(secs // 3600)
            secs -= hours * 3600
            minutes = int(secs // 60)
            secs -= minutes * 60

            return_text = ''
            if months != 0:
                return_text += '{} months '.format(months)

            return return_text + '{} days {} hours {} minutes {} seconds left'.format(days, hours, minutes, secs)
       
        anilist_query = '''
        query ($page: Int, $perPage: Int, $search: String) {
            Page (page: $page, perPage: $perPage) {
                pageInfo {
                    total
                    currentPage
                    lastPage
                    hasNextPage
                    perPage
                }
                media(search: $search, type: %s) {
                    id
                    idMal
                    title {
                        romaji
                        english
                        native
                    }
                    coverImage {
                        large
                    }
                    averageScore
                    chapters
                    volumes
                    episodes
                    format
                    status
                    source
                    
                    genres
                    popularity
                    description(asHtml:false)
                    startDate {
                        year
                        month
                        day
                    }
                    endDate {
                        year
                        month
                        day
                    }
                    nextAiringEpisode {
                        airingAt
                        timeUntilAiring
                        episode
                    }
                }
            }
        }
        '''
        def html2markdown(text):
            re_list = {
                '<br>': '\n',
                '</br>': '\n',
                '<i>': '*',
                '</i>': '*',
                '<b>': '**',
                '</b>': '**',
                '\n\n': '\n'
            }
            for k, v in re_list.items():
                text = text.replace(k, v)
            return text
        variables = {
            'search': title,
            'page': 1,
            'perPage': 50
        }
        async with aiohttp.ClientSession() as sesi:
            try:
                async with sesi.post('https://graphql.anilist.co', json={'query': anilist_query % method.upper(), 'variables': variables}) as r:
                    try:
                        data = await r.json()
                    except IndexError:
                        return 'ERROR: An internal error occurred'
                    if r.status != 200:
                        if r.status == 404:
                            return "No Page on that name"
                        elif r.status == 500:
                            return "ERROR: Internal Error :/"
                    try:
                        query = data['data']['Page']['media']
                    except IndexError:
                        return "No result."
            except aiohttp.ClientError:
                return 'ERROR: Connection lost'
            await sesi.close()
       
        status_tl = {
            'finished': 'Finished',
            'releasing': 'Releasing',
            'not_yet_released': 'Not_Yet_released',
            'cancelled': 'Cancelled'
        }
        format_tl = {
            "TV": "Anime",
            "TV_SHORT": "Short_anime",
            "MOVIE": "Film",
            "SPECIAL": "Special",
            "OVA": "OVA",
            "ONA": "ONA",
            "MUSIC": "MV",
            "NOVEL": "Novel",
            "MANGA": "Manga",
            "ONE_SHOT": "One-Shot",
            None: "None"
        }
        source_tl = {
            "ORIGINAL": "Original",
            "MANGA": "Manga",
            "VISUAL_NOVEL": "Visual Novel",
            "LIGHT_NOVEL": "Novel ",
            "VIDEO_GAME": "Game",
            "OTHER": "Idk",
            None: "Idk"
        }

        if not query:
            return "Please add a name for your anime or manga."

        full_query_result = []
        for entry in query:
            start_y = entry['startDate']['year']
            end_y = entry['endDate']['year']
            if not start_y:
                start = 'Not yet released'
            else:
                start = '{}'.format(start_y)
                start_m = entry['startDate']['month']
                if start_m:
                    start = '{}/{}'.format(start, start_m)
                    start_d = entry['startDate']['day']
                    if start_d:
                        start = '{}/{}'.format(start, start_d)
            
            if not end_y:
                end = 'Not yet over'
            else:
                end = '{}'.format(end_y)
                end_m = entry['endDate']['month']
                if end_m:
                    end = '{}/{}'.format(end, end_m)
                    end_d = entry['endDate']['day']
                    if end_d:
                        end = '{}/{}'.format(end, end_d)

            title = entry['title']['romaji']
            popularity = int(entry['popularity'])
            
            ani_id = str(entry['id'])
            try:
                mal_id = int(entry['idMal'])
            except:
                mal_id = None

            other_title = entry['title']['native']
            english_title = entry['title']['english']
            if english_title:
                if other_title:
                    other_title += '\n' + english_title
                else:
                    other_title = english_title

            score_rate = None
            score_rate_anilist = entry['averageScore']
            if score_rate:
                score_rate = '{}/10'.format(score_rate_anilist/10)
     
            description = entry['description']
            if description is not None:
                description = html2markdown(description)
                if len(description) > 1023:
                    description = description[:1020] + '...'

            genres = ', '.join(entry['genres']).lower()
            
           
            status = entry['status'].lower()
            img = entry['coverImage']['large']
            ani_link = 'https://anilist.co/{m}/{id}'.format(m=method, id=ani_id)
            if entry['source'] != None:
                source = entry['source'].capitalize()
            else:
                source = "Original"

            dataset = {
                'title': title,
                'title_other': other_title,
                'start_date': start,
                'end_date': end,
                'poster_img': img,
                'synopsis': description,
                'status': status.capitalize(),
                'format': entry['format'].capitalize(),
                'source_fmt': source,
                'link': ani_link,
                'score': score_rate,
                'ani_id': int(ani_id),
                'MALID': mal_id,
                'genres': genres,
                'popularity': int(popularity),
                
            }

            if method == 'manga':
                vol = entry['volumes']
                ch = entry['chapters']
                ch_vol = '{c} chapterXXC/{v} volumeXXV'.format(c=ch, v=vol).replace('None', '??')
                if ch:
                    if ch > 1:
                        ch_vol = ch_vol.replace('XXC', 's')
                ch_vol = ch_vol.replace('XXC', '')
                if vol:
                    if vol > 1:
                        ch_vol = ch_vol.replace('XXV', 's')
                ch_vol = ch_vol.replace('XXV', '')
                dataset['ch_vol'] = ch_vol
            if method == 'anime':
                dataset['episodes'] = entry["episodes"]
                if status in ['releasing', 'not_yet_released']:
                    ne_data = entry['nextAiringEpisode']
                    if ne_data:
                        airing_time = ne_data['airingAt']
                        d_airing_time = timedelta(seconds=abs(airing_time))
                        time_tuple = datetime(1,1,1) + d_airing_time

                        dataset['airing_date'] = '{d} {m} {y}'.format(d=time_tuple.day, m=monthintext(time_tuple.month), y=time.strftime('%Y'))
                        dataset['next_episode'] = ne_data['episode']
                        dataset['time_remain'] = create_time_format(ne_data['timeUntilAiring'])

            for k, v in dataset.items():
                if not v:
                    dataset[k] = 'No Data'

            full_query_result.append(dataset)
        return {'result': full_query_result, 'data_total': len(full_query_result)}