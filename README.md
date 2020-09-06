# News Article Scrapping
Python Code to scrape the Newspaper or News Website source for the News Article in to JSON format Output
A Flask Based API is too available to working using CURL request [NEWS FETCH API](https://github.com/imakashsahu/News-Articles-Scrapping-API)

## Required Python Libraries
```
- newspaper3k
- news-fetch
```

# Fields Fetched
```
'headline': news.headline, 
'author': news.authors, 
'publish_date': news.date_publish, 
'modify_date': news.date_modify,
'download_date': news.date_download,
'image_url': news.image_url,
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
```

## Files Included
There are two python file to server two type of purpose.
1. ***get_one_article.py*** this file can is designed to fetch the details from a single news articles using the articles URL link.
2. ***get_all_article.py*** this file can fetch the all the news articles from a given newspaper/news website source url


## Tweak to made fulfill your needs
1. The Code is developed fetch the news article from the source for the past 24 hrs by default but can be changed in ***get_all_article.py***
   - **difference_day == 0:**
   - 0 - If you want to fetch all article from Today
   - 1 - If you want to fetch all article from yesterday
   - Increase number accordingly to fetch the respective date

2. The code uses the memoize feature in order to fetch only the new fetch when run rather than unnecessarily fetching all articles on every run
   - **news_paper = newspaper3k.build('http://www.cnn.com/', memoize_articles=True)**
   - *memoize_articles=TRUE* turns memoize ON
   - *memoize_articles=FALSE* turns memoize OFF
