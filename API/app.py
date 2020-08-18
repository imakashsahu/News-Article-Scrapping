from flask import Flask, jsonify, request
import newspaper as newspaper3k
# from newsfetch.news import newspaper as newsfetch # Use After Fix 
from news import newspaper as newsfetch # Use Local File until the Image URl and Language is fixed by Developer
from datetime import date

app = Flask(__name__)

@app.route("/")
def online_news_api():
    # http://localhost:5000/?source_url=
    source_url = request.args.get("source_url")
    
    try:
        # Memoize gets the cache to be cleared and show all the recent articles :- "memoize_articles=False"
        news_paper = newspaper3k.build(source_url)

        if news_paper.size() == 0:
            return news_paper.brand + " has no new NEWS"
        else:
            # Fetch using newsfetch Library
            Article_Data=[]
            for article in news_paper.articles:
                article_url = article.url
                news = newsfetch(article_url)

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
                    Article_Data.append({'headline': news.headline, 
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
                                        'url': news.uri})
                else:
                    Article_Data.append({'Error': 'Article is OLDER than 24 Hrs'})
                    
            return jsonify(Article_Data = Article_Data)
    
    except:
        return "Source is not a valid URL or Use the format 'https://www.site.com'"

if __name__ == "__main__":
    app.run(debug=True)