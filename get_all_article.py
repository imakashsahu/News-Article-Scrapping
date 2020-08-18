# Refer below Link for Multi Threading
# https://github.com/codelucas/newspaper/blob/master/docs/user_guide/advanced.rst

import newspaper as newspaper3k
# from newsfetch.news import newspaper as newsfetch # Use After Fix 
from news import newspaper as newsfetch # Use Local File until the Image URl and Language is fixed by Developer
from datetime import date
import json

# Memoize gets the cache to be cleared and show all the recent articles :- "memoize_articles=False"
news_paper = newspaper3k.build('http://www.cnn.com/', memoize_articles=True)

# Prints the total number of Articles in Given Newspaper Build
print(news_paper.brand + " has total " + str(news_paper.size()) + " News ")

# Fetch using newsfetch Library
for article in news_paper.articles:
    article_url = article.url
    news = newsfetch(article_url)
    try:
        print('News-Fetch-URL : ' + news.uri)
        # print('News-Fetch : '+ str(news.date_publish))            
        # Convert Fetched date from Str to Datetime to void with base 10 Error
        publish_date = news.date_publish
        publish_year = int(publish_date[0:4])
        publish_month = int(publish_date[5:7])
        publish_day = int(publish_date[8:10])
        # someday = date(2020, int('08'), int('03'))
        article_date = date(publish_year, publish_month, publish_day)
        # Check if the article is Older than 24 Hrs ?
        today = date.today()
        diff =  today - article_date
        difference_day = diff.days
        
        # 1 - If you want to fetch all article from yesterday
        # 0 - If you want to fetch all article from Today
        if difference_day == 0:
            try:
                #GET RESULT IN JSON
                data = {'Article_Data': 
                            [{
                                'headline': news.headline, 
                                'author': news.authors, 
                                'publish_date': news.date_publish, 
                                'modify_date': news.date_modify,
                                'download_date': news.date_download,
                                'image_url': news.image_url,
                                'language': news.language,
                                'filename': news.filename,
                                'description': news.description,
                                'publication': news.publication,
                                'category': news.category,
                                'source_domain': news.source_domain,
                                'article': news.article,
                                'summary': news.summary,
                                'keyword': news.keywords,
                                'title_page': news.title_page,
                                'title_rss': news.title_rss,
                                'url': news.uri
                            }]
                        }
                print(json.dumps(data, indent=2))
            except:
                print("Data for this Article can't be fetched")
        else:
            print("Article is OLDER than 24 Hrs")
    except:
        print("Data for this Article can't be fetched")
