from tradingview_screener.query import Query, And, Or
from tradingview_screener.column import col


stock_screener = (
    Query()
    .where(
        col('type').isin(['stock', 'dr', 'fund']),
        col('subtype').isin(
            [
                'common',
                'foreign-issuer',
                '',
                'etf',
                'etf,odd',
                'etf,otc',
                'etf,cfd',
            ]
        ),
        col('exchange').isin(['AMEX', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('active_symbol') == True,
    )
    .set_property('options', {'lang': 'en'})
    .set_markets('america')
    .set_property('symbols', {'query': {'types': []}, 'tickers': []})
    .select(
        'logoid',
        'name',
        'close',
        'change',
        'change_abs',
        'Recommend.All',
        'volume',
        'Value.Traded',
        'market_cap_basic',
        'price_earnings_ttm',
        'earnings_per_share_basic_ttm',
        'number_of_employees',
        'sector',
        'description',
        'type',
        'subtype',
        'update_mode',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        'fundamental_currency_code',
    )
    .order_by('market_cap_basic', ascending=False)
    .limit(150)
)

etf_screener = (
    Query()
    .select(
        'name',
        'description',
        'logoid',
        'update_mode',
        'type',
        'typespecs',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        'change',
        'Value.Traded',
        'relative_volume_10d_calc',
        'aum',
        'fundamental_currency_code',
        'nav_total_return.5Y',
        'expense_ratio',
        'asset_class.tr',
        'focus.tr',
        'exchange',
    )
    .where2(
        And(
            Or(
                And(col('typespecs').has(['etn'])),
                And(col('typespecs').has(['etf'])),
                And(col('type') == 'structured'),
            )
        )
    )
    # NOTE that this can be rewritten as:
    # .where2(
    #     Or(col('typespecs').has(['etn', 'etf']), col('type') == 'structured'),
    # )
    # but I want to keep it exactly as in the browser
    .set_property('ignore_unknown_fields', False)
    .set_markets('america')
    .set_property('options', {'lang': 'en'})
    .limit(100)
    .order_by('aum', ascending=False)
    .set_property('symbols', {})
)

forex_screener = (
    Query()
    .where(col('sector').isin(['Major', 'Minor']))
    .set_property('options', {'lang': 'en'})
    .set_markets('forex')
    .set_property('symbols', {'query': {'types': ['forex']}, 'tickers': []})
    .select(
        'base_currency_logoid',
        'currency_logoid',
        'name',
        'close',
        'change',
        'change_abs',
        'bid',
        'ask',
        'high',
        'low',
        'Recommend.All',
        'description',
        'type',
        'subtype',
        'update_mode',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
    )
    .order_by('name', ascending=True)
    .limit(150)
)

crypto_screener = (
    Query()
    .set_property('options', {'lang': 'en'})
    .set_markets('crypto')
    .set_property('symbols', {'query': {'types': []}, 'tickers': []})
    .select(
        'base_currency_logoid',
        'currency_logoid',
        'name',
        'close',
        'change',
        'change_abs',
        'high',
        'low',
        'volume',
        '24h_vol|5',
        '24h_vol_change|5',
        'Recommend.All',
        'exchange',
        'description',
        'type',
        'subtype',
        'update_mode',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
    )
    .order_by('24h_vol|5', ascending=False)
    .set_property('price_conversion', {'to_symbol': False})
    .limit(150)
)


stock_screener2 = (
    Query()
    .select(
        'name',
        'description',
        'logoid',
        'update_mode',
        'type',
        'typespecs',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        'change',
        'volume',
        'relative_volume_10d_calc',
        'market_cap_basic',
        'fundamental_currency_code',
        'price_earnings_ttm',
        'earnings_per_share_diluted_ttm',
        'earnings_per_share_diluted_yoy_growth_ttm',
        'dividends_yield_current',
        'sector.tr',
        'market',
        'sector',
        'recommendation_mark',
        'exchange',
    )
    .where2(
        And(
            Or(
                And(col('type') == 'stock', col('typespecs').has(['common'])),
                And(col('type') == 'stock', col('typespecs').has(['preferred'])),
                And(col('type') == 'dr'),
                And(col('type') == 'fund', col('typespecs').has_none_of(['etf'])),
            )
        )
    )
    # can be rewritten as:
    # .where2(
    #     Or(
    #         And(col('type') == 'stock', col('typespecs').has(['common', 'preferred'])),
    #         col('type') == 'dr',
    #         And(col('type') == 'fund', col('typespecs').has_none_of(['etf'])),
    #     )
    # )
    .set_property('ignore_unknown_fields', False)
    .set_markets('america')
    .set_property('options', {'lang': 'en'})
    .limit(100)
    .order_by('market_cap_basic', ascending=False)
    .set_property('symbols', {})
)

dex_screener = (
    Query()
    .select(
        'original_base_currency',
        'short-description',
        'base_currency_logoid',
        'update_mode',
        'type',
        'typespecs',
        'exchange',
        'blockchain-id.tr',
        'blockchain-id',
        'exchange.tr',
        'provider-id',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        '24h_close_change|5',
        'dex_txs_count_24h',
        'dex_trading_volume_24h',
        'dex_txs_count_uniq_24h',
        'dex_total_liquidity',
        'fully_diluted_value',
        'Recommend.All',
    )
    .where2(
        And(
            col('exchange').isin(
                [
                    'UNISWAP3POLYGON',
                    'VERSEETH',
                    'UNISWAP3ETH',
                    'UNISWAP3ARBITRUM',
                    'UNISWAP3OPTIMISM',
                    'RAYDIUM',
                    'ORCA',
                    'PULSEX',
                    'THRUSTER3',
                ]
            ),
            col('currency_id') == 'USD',
        )
    )
    .set_markets('crypto')
    .set_property('options', {'lang': 'en'})
    .limit(100)
    .order_by('dex_trading_volume_24h', ascending=False)
    .set_property('symbols', {})
)
"""
https://www.tradingview.com/dex-screener/
"""

# TODO: remove columns and simplify where2()
# TODO: perhaps move this content to the website since its bound to change often.
#  along with the `dict[column_display_name, col_name]` mapping, since its also smth that needs
#  to be updated often.
#
