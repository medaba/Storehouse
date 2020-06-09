# -*- coding: utf-8 -*-

# Пример работы с модулем для постинга в telegra.ph

from telegraph import Telegraph


telegraph = Telegraph()

telegraph.create_account(short_name='377')

response = telegraph.create_page(
    title='Main Headling',
    html_content=f'''<h4>SubHeadling</h4>
                    <figure>
                      <img src="https://images.pexels.com/photos/3985158/pexels-photo-3985158.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260"/>
                      <figcaption>Подпись к картинке</figcaption>
                    </figure>
                    <p>{"большая статья " * 50}</p>
                    <br>
                    <p>{"продолжение большой статьи " * 50}</p>''',
    author_name='MS-Bot'
)

telegraph_url = response['url']
mirror_url = f'https://tgraph.io/{response["path"]}'

print(telegraph_url)
print(mirror_url)