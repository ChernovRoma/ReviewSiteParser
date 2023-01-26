from pprint import pprint

from functions import *
import pandas as pd


# pd.DataFrame(parse_softwareadvise()).to_excel('output.xlsx', header=False, index=False)
# pd.DataFrame(parse_sourceforge()).to_excel('Sourceforge_Marketing_Apps.xlsx', header=False, index=False)

p = parse_trustpilot()
pprint(len(p))
pprint(p)
# pd.DataFrame(p).to_excel('Trustpilot_Agencies.xlsx', header=False, index=False)