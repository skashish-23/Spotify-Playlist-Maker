# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# #all_anchor_tags = soup.find(name = "span", class_ = "titleline")
# #article_score = soup.find(name = "span", class_ = "score")
# #article_link = all_anchor_tags.find("a")["href"]
# #print(f" {all_anchor_tags.getText()} \n { article_score.getText()}\n{article_link}")
# article_text = []
# article_link = []
# articles = soup.find_all("span", class_="titleline")
# for article_tag in articles:
#     text = article_tag.getText()
#     article_text.append(text)
#     link = article_tag.find("a")["href"]
#     article_link.append(link)
# upvote = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_ = "score")]
# max_votes = max(upvote)
# max_vote_index = upvote.index(max_votes)
#
# print(article_text[max_vote_index])
# print(article_link[max_vote_index])
# print(max_votes  )