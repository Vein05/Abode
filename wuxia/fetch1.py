from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from cogs.utils import string_
from lxml import etree
from lxml.html import fromstring, HTMLParser


def fetchNovel(name):
    def response(name):
        my_url = "https://www.novelupdates.com/series/{}/".format(name)
        req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

        client = urlopen(req)
        html = client.read()
        client.close()

        page = soup(html, "html.parser")

        novel_data = {
            "image": fetchImage(page),
            "genres": fetchGenres(page),
            "description": fetchDescription(page),
            "type": fetchType(page),
            "tags": fetchTags(page),
            "votes": fetchVotes(page),
            "language": fetchLanguage(page),
            "authors": fetchAuthors(page),
            "artists": fetchArtists(page),
            "year": fetchYear(page),
            "status": fetchStatus(page),
            "licensed": fetchLicensed(page),
            "completelyTranslated": fetchCompletelyTranslated(page),
            "publisher": fetchPublisher(page),
            "englishPublisher": fetchEnglishPublisher(page),
            "releaseFrequency": fetchReleaseFrequency(page),
            "activityStats": fetchActivityStats(page),
            "aliases": fetchAliases(page),
            # "asd": fetchAssociatedName(page)
        }

        return novel_data
    
    def fetchImage(page):
        return page.find("div", {"class": "seriesimg"}).img["src"]
    
    def fetchDescription(page):
        def decodeQuotes(string):
            return string.replace(u"\u2018", "'").replace(u"\u2019", "'")
        return decodeQuotes(page.find("div", {"id": "editdescription"}).p.text)
    def fetchAliases(page):
        def decodeQuotes(string):
            return string.replace(u"\u2018", "'").replace(u"\u2019", "'")
        return decodeQuotes(page.find("div", {"id": "editassociated"}).text)


    def fetchType(page):
        return page.find("a", {"class", "genre type"}).text
    
    def fetchGenres(page):
        genres = []
        genres_html = page.find("div", {"id": "seriesgenre"}).find_all("a")

        for genre_html in genres_html:
            genres.append(genre_html.text)

        return genres

    def fetchTags(page):
        tags = []
        tags_html = page.find("div", {"id": "showtags"}).find_all("a")

        for tag_html in tags_html:
            tags.append(tag_html.text)

        return tags

    def fetchVotes(page):
        votes = {}
        votes_html = page.find_all("span", {"class": "votetext"})
        score = 5

        for vote_html in votes_html:
            texts = vote_html.text.split()
            votes[score] = int(texts[1][1:])
            score -= 1
        
        return votes

    def fetchLanguage(page):
        return page.find("div", {"id": "showlang"}).a.text
    
    def fetchAuthors(page):
        authors = []
        authors_html = page.find("div", {"id": "showauthors"}).find_all("a")

        for author_html in authors_html:
            authors.append(author_html.text)
        
        return authors
    
    def fetchArtists(page):
        artists = []
        artists_html = page.find("div", {"id": "showartists"}).find_all("a")

        for artist_html in artists_html:
            artists.append(artist_html.text)
        
        return artists
    
    def fetchYear(page):
        return page.find("div", {"id": "edityear"}).text.strip()
    
    def fetchStatus(page):
        return page.find("div", {"id": "editstatus"}).text.strip()

    def fetchLicensed(page):
        return page.find("div", {"id": "showlicensed"}).text.strip()
    
    def fetchCompletelyTranslated(page):
        return page.find("div", {"id": "showtranslated"}).text.strip()
    
    def fetchPublisher(page):
        return page.find("div", {"id": "showopublisher"}).find("a").text.strip()

    def fetchEnglishPublisher(page):
        try:
            return page.find("div", {"id": "showepublisher"}).text.strip()
        except:
            return "Error"
    def fetchReleaseFrequency(page):
        page_str = str(page)
        start_index = page_str.find("Release Frequency")
        words = page_str[start_index:start_index+100].split()
        return float(words[3])



    def fetchActivityStats(page):
        time = ["week", "month", "allTime"]
        stats = {}

        activity_ranks_html = page.find_all("span", {"class": "userrate rank"}) 

        for i in range(3):
            stats[time[i]] = int(activity_ranks_html[i].text[1:])

        return stats

    return response(name)