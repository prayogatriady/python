def loop_bs(x: int, y: int):
    
    import requests
    from bs4 import BeautifulSoup

    job_list = []
    comp_list = []
    loc_list = []
    sal_list = []
    exp_list = []

    for i in range(x,y):
        print(i)
        URL = f'https://glints.com/id/opportunities/jobs/explore?country=ID&locationName=Indonesia&page={i}'

        html_text = requests.get(URL).content
        soup = BeautifulSoup(html_text, 'lxml')

        cards = soup.find_all('div', class_ = 'JobCardsc__JobcardContainer-sc-1f9hdu8-0 hvpJwO CompactOpportunityCardsc__CompactJobCardWrapper-sc-1y4v110-0 dLzoMG compact_job_card')
        for item in cards:
            try:
                job = item.find('h2', class_ = 'CompactOpportunityCardsc__JobTitle-sc-1y4v110-7 cYZbCX').text.strip()
                comp = item.find('a', class_ = 'CompactOpportunityCardsc__CompanyLink-sc-1y4v110-8 kCzMph').text.strip()

                inner_card = item.find('div', class_ = 'CompactOpportunityCardsc__OpportunityInfoContainer-sc-1y4v110-12 xjRgE')
                loc = inner_card.select('div div')[0].text.strip()
                sal = inner_card.select('div div')[1].text.strip()
                exp = inner_card.select('div div')[2].text.strip()
                
            except:
                pass
            
            job_list.append(job)
            comp_list.append(comp)
            loc_list.append(loc)
            sal_list.append(sal)
            exp_list.append(exp)
        
    return job_list, comp_list, loc_list, sal_list, exp_list

def generate_csv(job_list, comp_list, loc_list, sal_list, exp_list):

    import pandas as pd

    df = pd.DataFrame({'job':job_list,'company':comp_list,'location':loc_list,'salary':sal_list,'exp':exp_list})
    df.to_csv('output.csv', index=False)

def append_csv(job_list, comp_list, loc_list, sal_list, exp_list):

    import pandas as pd

    df = pd.DataFrame({'job':job_list,'company':comp_list,'location':loc_list,'salary':sal_list,'exp':exp_list})
    df.to_csv('output.csv',  mode='a', index=False, header=False)


if __name__ == '__main__':
    job_list, comp_list, loc_list, sal_list, exp_list = loop_bs(1,101)
    generate_csv(job_list, comp_list, loc_list, sal_list, exp_list)
    # append_csv(job_list, comp_list, loc_list, sal_list, exp_list)