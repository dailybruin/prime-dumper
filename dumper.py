# This script generates Markdown and JSON files from the old prime SQL dump
import sys
import os
import csv

def main():
    article_list = dict({})
    author_list = dict({})
    print('Hello')
    with open('./' + 'prime_article.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            article_list.update({row['id']: article(row['title'], row['slug'], '', '', row['teaser'], row['lead_photo'], '', '', row['body'])})
            # at this point we haven't initialized the following values: author, issue, lead_photo_photographer and category
    with open('./' + 'prime_author.csv') as csv_author:
        csv_reader = csv.DictReader(csv_author)
        for row in csv_reader:
            author_list.update({row['id']: row['first_name'] + row['last_name']})
    
    with open('./' + 'prime_article_author.csv') as csv_author_relation:
        csv_reader = csv.DictReader(csv_author_relation)
        for row in csv_reader:
            article_list[row['article_id']].author = author_list[row['author_id']]
    
    # open something for writing markdown files
    for key, value in article_list.items():
        with open('./' + value.slug + '.md', 'w') as md_file:
            md_file.write('---\n')
            md_file.write('title: ' + '\'' + value.author + '\'\n')
            md_file.write('category: ' + '\'' + value.category +'\'\n')
            md_file.write('issue: ' + '\'' + value.issue + '\'\n')
            md_file.write('---\n')
            md_file.write(value.body)
class article:
    def __init__(self, title, slug, author, issue, excerpt, lead_photo_url, lead_photo_photographer, category, body):
        self.title = title
        self.slug = slug
        self.author = author
        self.issue = issue
        self.excerpt = excerpt
        self.lead_photo_url = lead_photo_url
        self.lead_photo_photographer = lead_photo_photographer
        self.category = category
        self.body = body

main()