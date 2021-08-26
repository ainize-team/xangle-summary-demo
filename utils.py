
def format_new_listing(outputs):
    summary = f"""
    1. Exchange Name
    {outputs['Exchange Name']}

    2. Date (Estimated Date)
    {outputs['Date (Estimated Date)']}

    3. Details
    Name: {outputs['Name']}
    Symbol / Ticker: {outputs['Symbol / Ticker']}

    Key Dates
    Wallet creation and deposit requests opening date: {outputs['Wallet creation and deposit requests opening date']}
    Trading opening date: {outputs['Trading opening date']}
    Withdrawal opening date: {outputs['Withdrawal opening date']}

    Initial Fees and Pricing
    Withdrawal fee: {outputs['Withdrawal fee']}
    Announced listing pairs: {outputs['Announced listing pairs']}
    Listing price: {outputs['Listing price']}

    Trading
    Minimum Trade/Purchase Amount: {outputs['Minimum Trade/Purchase Amount']}
    Minimum Price Movement: {outputs['Minimum Price Movement']}
    Minimum Order Size: {outputs['Minimum Order Size']}

    Other info
    Exchange promoted listing/airdrop event: {outputs['Exchange promoted listing/airdrop event']}
    """

    return summary


def format_new_partnership(outputs):
    outputs['Logo'] = '-'

    summary = f"""
    1. Partner's Name
    {outputs["Partner's Name"]}

    2. Counterparty Website
    {outputs['Counterparty Website']}

    3. Counterparty Details
    {outputs['Counterparty Details']}

    4. Does this partnership generate any kind of revenue?
    {outputs['Does this partnership generate any kind of revenue?']}

    5. Logo
    {outputs['Logo']}

    6. Applicable Date(s)
    {outputs['Applicable Date(s)']}

    7. Partnership Details
    {outputs['Partnership Details']}
    """

    return summary


FORMAT_FUNC = {
    'New Listing': format_new_listing,
    'New Partnership': format_new_partnership,
}
