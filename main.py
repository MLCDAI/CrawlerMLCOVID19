import logging
import argparse
from pathlib import Path 
import yaml
import logging
from src.fact_checker import FactChecker
from src.translator import GoogleTranslator
import pandas as pd 
logger = logging.getLogger(__name__)
cwd_dir = Path.cwd()

from datetime import datetime


parser = argparse.ArgumentParser(description='COVID19 News Crawler Initialized')


parser.add_argument('-q','--query', nargs='+', dest='query',type=str,help="Examples: -q item1 item2, -q item3")
parser.add_argument('-trans','--translate',type=str, help="python main.py -trans 'hello world' -lang zh")
parser.add_argument('-lang','--language_code',  type=str, metavar="", default='en',help = '''restrict language for returned news''')
parser.add_argument('-num','--number_of_result',  type=int, metavar="",default=10 , help = '''The maximum number of news to return''')

#you can customize fact-checker and query refer to file of src.fetch_facts 
#parser.add_argument('-checker','--fact_checker',  nargs='+', dest='checker',type=str, default= None,help="Examples: -q item1 item2, -q item3")

def main():
    args = parser.parse_args()
    if args.query:
        reviewer_dir = cwd_dir /'data'/ 'checkers.yaml'

        #add reviewer to restrict fact-checking
        all_reviewer = yaml.safe_load(reviewer_dir.read_text())


        crawler = FactChecker()
        try:
            all_data = pd.concat([crawler(query =q, num_results=args.number_of_result, language_code=args.language_code) for q in args.query])
            df = all_data.drop_duplicates(subset='claim').reset_index(drop=True)
            print(f'Successfully collected {len(df)} news ')
        except:
            df = pd.DataFrame()
        file_name = "_".join(str(datetime.now()).split(' '))

        if type(args.query) == list:
            front_name = "_".join(args.query)
        else:
            front_name =  args.query

        # Set up reviewer directory
        download_folder = cwd_dir / 'data' / 'news'
        if not reviewer_dir.exists():
            download_folder.mkdir()
            
        download_file_path = f'{cwd_dir}/data/news/{front_name}_{file_name}.csv'
        df.to_csv(download_file_path, index=False)
        print(f"data have been downloaded in {download_file_path} successfully")
        
    elif args.translate:
        text = args.translate
        print(f'Input text: {text}')
        translator = GoogleTranslator()
        if args.language_code:
            trans_result =translator.trans(text, lang=args.language_code)
        else:
            trans_result =translator.trans(text)
        print(trans_result)
        
    else:
        print('please input text to search') 

if __name__ == '__main__':
    main()            

        