## This Python code lets you fetch the News Article Details using the Article Link URL
from newsfetch.news import newspaper
import json

news = newspaper('https://edition.cnn.com/travel/article/disney-world-trip-planning-2020/index.html')

#GET RESULT IN JSON
data = {'Article': 
            [{
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
            }]
        }

print(json.dumps(data, indent=2))
