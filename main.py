import bs4
from bs4 import BeautifulSoup
import requests
import re
from tqdm import tqdm

is_first = True
strain = bs4.SoupStrainer("p")
page_count = 0

def get_re(url) :
    while True :
        try :
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml",parse_only=bs4.SoupStrainer("p"))
            return soup
        except KeyboardInterrupt :
            raise KeyboardInterrupt
        except :
            continue


page_url = "https://en.wikipedia.org/wiki/Special:AllPages/0"
while page_url != "https://en.wikipedia.org/wiki/Special:AllPages/0" or is_first:
    page_count += 1
    is_first = False
    page_response = requests.get(page_url)
    page_soup = BeautifulSoup(page_response.text, "lxml")

    sub_url_l = page_soup.select('div .mw-allpages-body li>a')
    raw_text = ""
    with open("wiki_cxk_point.txt","w+", encoding="utf-8") as p :
        with open(f"Wikitext\\wiki{page_count}.txt", 'w+', encoding="utf-8") as f :
            p.write(str(page_count)+"\n")
            for prgraph_url in tqdm(sub_url_l) :
                main_url ="https://en.wikipedia.org/" + prgraph_url["href"]
                p.write(main_url+"\n")
                main_soup = get_re(main_url)

                #find paragraph of main page
                for del_tag in main_soup.find_all("sup", class_="reference") :
                    del_tag.decompose()
                for del_tag in main_soup.find_all("math") :
                    del_tag.decompose()
                prgraph = main_soup.select("p", role="paragraph")
                for txt in prgraph :
                    f.write(txt.get_text())
            page_url = "https://en.wikipedia.org" + page_soup.find_all('a', title="Special:AllPages")[1]["href"]
f.close()  
p.close()
