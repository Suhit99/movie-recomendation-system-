import bs4
import urllib.request as req

def gener():
    genre_pageurl="https://www.imdb.com/feature/genre/?ref_=nv_ch_gr"
    genre_pageresponse=req.urlopen(genre_pageurl)
    genre_page=bs4.BeautifulSoup(genre_pageresponse,'html.parser')


    list2=genre_page.find_all('div',class_="table-cell primary")
    len(list2)

    glist=[]
    for i in range(0,24):
        glist.append(list2[i].find('a').text)
        print(i+1,list2[i].find('a').text)
    gchoice = input("Enter Genre:- ")
    #if gchoice>24 or gchoice<=0:
     #   print("Invalid choice")
    #else:
    glist1=[]
    for i in range(24):
        glist1.append(glist[i].replace(" ",""))
    gurl="https://www.imdb.com/search/title/?genres="+gchoice+"&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=313MPAMJSD4KFMETM137&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_1"
    greq=req.urlopen(gurl)
    gpage=bs4.BeautifulSoup(greq,'html.parser')
    list5 = gpage.find_all('h3',class_='lister-item-header')
    for i in range(len(list5)):
        print(list5[i].text)
def actor():
    actor =input("Enter Actor:- ")
    actor = actor.replace(" ",'+')
    htp = req.urlopen('https://www.imdb.com/find?ref_=nv_sr_fn&q='+actor+'&s=all')
    page = bs4.BeautifulSoup(htp,'html.parser')
    actor_content = page.find_all('td',class_='result_text')
    for i in range(len(actor_content)):
        print(i+1,actor_content[i].text)
    act_option = int(input("Enter choice:- "))-1
    if act_option<0 or act_option>i:
        print("Invalid choice")
    else:
        act_name = actor_content[act_option].find('a')['href']
    htp1 = req.urlopen('https://www.imdb.com'+act_name+'?ref_=fn_al_nm_1')
    page2 = bs4.BeautifulSoup(htp1,'html.parser')
    detail = page2.find_all('div',class_='filmo-row')
    for i in range(len(detail)):
        print((detail[i].text.replace('\n'," ")))


def topmov():
    print('''
1.Top Rated Movies
2.Top Rated Indian Movies
3.Most Popular Movies
4.Box Office(US)
                 ''')
    
    top_rated_choices={1:'https://www.imdb.com/chart/top/?ref_=nv_mv_250',
                  2:'https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=8a7876cd-2844-4017-846a-2c0876945b7b&pf_rd_r=Y6JX5KTNM1JKB5G51560&pf_rd_s=right-5&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_india_tr_rhs_1',
                  3:'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm',
                  4:'https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht'
                 }   
    top_rated_choice=int(input("Enter Choice:-"))
    if(top_rated_choice in top_rated_choices):
        home_pageurl=top_rated_choices[top_rated_choice]
        home_pageresponse=req.urlopen(home_pageurl)


        home_page=bs4.BeautifulSoup(home_pageresponse,'html.parser')


        movies_content=home_page.find_all('td',class_="titleColumn")
        #movies_content[0].text
        for i in range(len(movies_content)):
         #   print(i+1,movies_content[i].text)
            print(i+1,movies_content[i].find('a').text)

    else:
        print("Invalid choice")

#main
n=True
while(n):
    print('''
        1. Top rated movies
        2. Movies done by Actors
        3. Genre
        ''')
    userinput = int(input("Enter Choice:- "))
   # if userinput>3 or userinput<=0:
    #    print("Invalid choice")
    #else:    
    if(userinput == 1):
           topmov()
    elif(userinput == 2):
          actor()
    elif(userinput == 3):
         gener()
    else:
        print("Invalid choice!!!")
    cont=str(input("DO YOU WISH TO CONTINUE(Y/N): "))
    if cont=='y' or cont=='Y':
        n=True
    else:
        n=False
