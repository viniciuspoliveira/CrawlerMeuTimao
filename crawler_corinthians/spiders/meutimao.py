import scrapy


class MeutimaoSpider(scrapy.Spider):
    name = 'meutimao'
    allowed_domains = ['meutimao.com.br']
    start_urls = ['https://www.meutimao.com.br']

    def parse(self, response):
        for noticias, y in enumerate(response.css('h2')):
            yield {
                'titulo': response.css('.veja_mais::text')[noticias].get(),
                'href': 'https://www.meutimao.com.br' + response.css('.veja_mais').xpath(
                    '@href')[noticias].get(),
                'data': response.css('.horario::text')[noticias].get(),
                'portal': "meutimao"
            }
