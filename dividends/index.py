# index.py

import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Dividend


@register(Dividend)
class DividendIndex(AlgoliaIndex):
    fields = ('company', 'symbol', 'sector', 'industry', 'cons_years', 'ranking', 'drip_fees', 'spp_fees', 'spp_fees',
              'price', 'div_yield', 'current_dividend', 'num_payouts', 'annual_dividend', 'schedule', 'previous_dividend',
              'ex_dividend_date', 'payable_date', 'mr_increase', 'dgr_1', 'dgr_3', 'dgr_5', 'dgr_10', 'ad_5_10', 'deg_5',
              'eps', 'ttm_pe', 'fye')

    settings = {'searchableAttributes': ["company", "sector", "industry",
                                         "symbol"],
                'attributesForFaceting': ['sector', 'industry', 'price', 'cons_years', 'div_yield']
                }
    index_name = 'Dividend'