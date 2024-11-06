# nb default colors for plots and excel
default_color1 = '#179297'
default_color2 = '#BFCE28'

sidebar_indicators = ("Fear & Greed Index", "VIX", "Warren Buffett indicator - Marketcap to GDP", "Benchmark Indexs",
 "Yield Bonds 5Y - Spain, Germany, Portugal, Euro Area", "Yield CDS 5Y - Spain, Germany, USA", "Euribor rates - 1M, 3M, 6M, 12M",
 "Commercial Property prices", "Residential Property prices", "Inflation - Portugal", "Currency exchange rates",
 "Euro short-term rate (€STR)", "Key ECB interest rates", "SOFR")

dashboard_main_title = "TRAVEL - Market Risk Dashboard"

path_bonds = 'https://raw.githubusercontent.com/ricardoandreom/TRAVEL_MARKET_RISK/refs/heads/main/TRAVEL_Market_Risk/bonds_data/'
path_cds = 'C:/Users/Admin/Desktop/Market_Risk_dashboard/cds_data/'

travel_logo_url = "https://raw.githubusercontent.com/ricardoandreom/TRAVEL_MARKET_RISK/refs/heads/main/TRAVEL_Market_Risk/travel_logo.webp"

# Alphavantage API Key
alpha_api_key = 'EW4A338V8YGLZI3G'
# FRED API KEY
fred_api_key = 'eff3c719d275248bf5cdcfc836400e53'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
}

key_ecb_str = """
    <p>The Governing Council of the ECB sets the key interest rates for the euro area. These are as follows:</p>

    <h3>Deposit facility</h3>
    <p>The rate on the deposit facility, which banks may use to make overnight deposits with the Eurosystem at a pre-set interest rate. 
    The Governing Council decided in March 2024 to continue to steer the monetary policy stance through this rate.</p>

    <h3>Main refinancing operations</h3>
    <p>The interest rate on the main refinancing operations. In these operations banks can borrow funds from the ECB against broad collateral 
    on a weekly basis at a pre-determined interest rate. The rate is set above the deposit facility rate.</p>

    <h3>Marginal lending facility</h3>
    <p>The rate on the marginal lending facility, which offers overnight credit to banks against broad collateral at a pre-set interest rate. 
    The rate is set above the main refinancing operations rate.</p>
    """

sofr_str = """
    **SOFR - Secured Overnight Financing Rate**

    A **SOFR** (Secured Overnight Financing Rate) é uma taxa de referência para empréstimos de curto prazo no mercado financeiro dos Estados Unidos. Ela reflete o custo do crédito garantido por ativos de alta qualidade, como títulos do governo dos EUA, em transações realizadas durante a noite. A SOFR foi introduzida pelo **Federal Reserve** (o banco central dos EUA) como alternativa à **LIBOR** (London Interbank Offered Rate), após a LIBOR ter sido afetada por escândalos de manipulação e perda de confiança no processo de definição.

    A SOFR é calculada com base em transações reais de financiamento garantido, o que a torna uma taxa mais transparente e representativa do mercado. A SOFR é utilizada como taxa de referência para uma variedade de produtos financeiros, incluindo empréstimos, derivados e títulos. Ela reflete os custos de financiamento em um mercado de alta liquidez e com baixo risco, proporcionando uma taxa mais estável e confiável para os participantes do mercado.
    """

ir_str_str = """
**€STR - Taxa de juro de curto prazo do euro**

<p>A €STR é baseada em transações diárias de obtenção de fundos no mercado monetário sem garantia do euro, no prazo overnight.</p>
"""
