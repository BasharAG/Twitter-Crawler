# -*- coding: utf-8 -*-
import scrapy
import re


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'twitter-xpath'
    start_urls = [
        'https://twitter.com/search?q=%23marah&l=id&src=typd', #marah
        'https://twitter.com/search?q=%23sedih&l=id&src=typd', #sedih
        'https://twitter.com/search?q=%23kecewa&l=id&src=typd', #kecewa
        'https://twitter.com/search?q=%23senang&l=id&src=typd', #senang
        'https://twitter.com/search?q=%23bahagia&l=id&src=typd', #bahagia
        'https://twitter.com/search?q=%23terganggu&l=id&src=typd', #terganggu
        'https://twitter.com/search?q=%23gugup&l=id&src=typd', #gugup
        'https://twitter.com/search?q=%23bete&l=id&src=typd', #bete
        'https://twitter.com/search?q=%23pusing&l=id&src=typd', #pusing
        'https://twitter.com/search?q=%23heran&l=id&src=typd', #heran
        'https://twitter.com/search?q=%23bosan&l=id&src=typd', #bosan
        'https://twitter.com/search?q=%23malu&l=id&src=typd', #malu
        'https://twitter.com/search?q=%23kaget&l=id&src=typd', #kaget
        'https://twitter.com/search?q=%23kesal&l=id&src=typd', #kesal
        'https://twitter.com/search?q=%23capek&l=id&src=typd', #capek
        'https://twitter.com/search?q=%23jijik&l=id&src=typd', #jijik
        'https://twitter.com/search?q=%23takut&l=id&src=typd', #takut
        'https://twitter.com/search?q=%23terkejut&l=id&src=typd', #terkejut
        'https://twitter.com/search?q=%23bingung&l=id&src=typd', #bingung
        'https://twitter.com/search?q=%23serius&l=id&src=typd', #serius
        'https://twitter.com/search?q=%23cinta&l=id&src=typd', #cinta
        'https://twitter.com/search?q=%23sayang&l=id&src=typd', #sayang
        'https://twitter.com/search?q=%23gembira&l=id&src=typd', #gembira
        'https://twitter.com/search?q=%23kagum&l=id&src=typd', #kagum
        'https://twitter.com/search?q=%23benci&l=id&src=typd', #benci
        'https://twitter.com/search?q=%23nangis&l=id&src=typd', #nangis
        'https://twitter.com/search?q=%23terpesona&l=id&src=typd', #terpesona
        'https://twitter.com/search?q=%23ceria&l=id&src=typd', #ceria
        'https://twitter.com/search?q=%23cemas&l=id&src=typd', #cemas
    ]

    # tmp = ["","Here's the URL for this Tweet. Copy it to easily share with friends.", 
    # "Add this Tweet to your website by copying the code below. <a href=\"https://dev.twitter.com/docs/embedded-tweets\" rel=\"noopener\">Learn more</a>", 
    # "Add this video to your website by copying the code below. <a href=\"https://dev.twitter.com/docs/embedded-tweets\" rel=\"noopener\">Learn more</a>", 
    # "Hmm, there was a problem reaching the server. <button type=\"button\" class=\"btn-link retry-embed\">Try again?</button>", 
    # "By embedding Twitter content in your website or app, you are agreeing to the Twitter <a href=\"https://dev.twitter.com/overview/terms/agreement\" rel=\"noopener\">Developer Agreement</a> and <a href=\"https://dev.twitter.com/overview/terms/policy\" rel=\"noopener\">Developer Policy</a>.", 
    # "This timeline is where you’ll spend most of your time, getting instant updates about what matters to you."]

    def parse(self, response):
        text = re.findall(r'<p.*?>(.*)<\/p>', response.text)
        for line in text : 
            # if line not in tmp :
            yield {
                'text' : line
            }

