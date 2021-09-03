def format_new_listing(output):
    summary = f"""
1. Exchange Name
{output['Exchange Name']}

2. Date (Estimated Date)
{output['Date (Estimated Date)']}

3. Details
Name: {output['Details']['Name']}
Symbol / Ticker: {output['Details']['Symbol / Ticker']}

Key Dates
Wallet creation and deposit requests opening date: {output['Details']['Key Dates']['Wallet creation and deposit requests opening date']}
Trading opening date: {output['Details']['Key Dates']['Trading opening date']}
Withdrawal opening date: {output['Details']['Key Dates']['Withdrawal opening date']}

Initial Fees and Pricing
Withdrawal fee: {output['Details']['Initial Fees and Pricing']['Withdrawal fee']}
Announced listing pairs: {output['Details']['Initial Fees and Pricing']['Announced listing pairs']}
Listing price: {output['Details']['Initial Fees and Pricing']['Listing price']}

Trading
Minimum Trade/Purchase Amount: {output['Details']['Trading']['Minimum Trade/Purchase Amount']}
Minimum Price Movement: {output['Details']['Trading']['Minimum Price Movement']}
Minimum Order Size: {output['Details']['Trading']['Minimum Order Size']}

Other info
Exchange promoted listing/airdrop event: {output['Details']['Other info']['Exchange promoted listing/airdrop event']}
    """

    return summary


def format_new_partnership(output):
    output['Logo'] = '-'

    summary = f"""
1. Partner's Name
{output["Partner's Name"]}

2. Counterparty Website
{output['Counterparty Website']}

3. Counterparty Details
{output['Counterparty Details']}

4. Does this partnership generate any kind of revenue?
{output['Does this partnership generate any kind of revenue?']}

5. Logo
{output['Logo']}

6. Applicable Date(s)
{output['Applicable Date(s)']}

7. Partnership Details
{output['Partnership Details']}
    """

    return summary


FORMAT_FUNC = {
    'New Listing': format_new_listing,
    'New Partnership': format_new_partnership,
}
