def format_new_listing(output):
    summary = f"""
1. Exchange Name
{output["Exchange Name"]}

2. Date (Estimated Date)
{output["Date (Estimated Date)"]}

3. Details
Name: {output["Details"]["Name"]}
Symbol / Ticker: {output["Details"]["Symbol / Ticker"]}

Key Dates
Wallet creation and deposit requests opening date: {output["Details"]["Key Dates"]["Wallet creation and deposit requests opening date"]}
Trading opening date: {output["Details"]["Key Dates"]["Trading opening date"]}
Withdrawal opening date: {output["Details"]["Key Dates"]["Withdrawal opening date"]}

Initial Fees and Pricing
Withdrawal fee: {output["Details"]["Initial Fees and Pricing"]["Withdrawal fee"]}
Announced listing pairs: {output["Details"]["Initial Fees and Pricing"]["Announced listing pairs"]}
Listing price: {output["Details"]["Initial Fees and Pricing"]["Listing price"]}

Trading
Minimum Trade/Purchase Amount: {output["Details"]["Trading"]["Minimum Trade/Purchase Amount"]}
Minimum Price Movement: {output["Details"]["Trading"]["Minimum Price Movement"]}
Minimum Order Size: {output["Details"]["Trading"]["Minimum Order Size"]}

Other info
Exchange promoted listing/airdrop event: {output["Details"]["Other info"]["Exchange promoted listing/airdrop event"]}
"""
    return summary


def format_new_partnership(output):
    output["Logo"] = '-'

    summary = f"""
1. Partner's Name
{output["Partner's Name"]}

2. Counterparty Website
{output["Counterparty Website"]}

3. Counterparty Details
{output["Counterparty Details"]}

4. Does this partnership generate any kind of revenue?
{output["Does this partnership generate any kind of revenue?"]}

5. Logo
{output["Logo"]}

6. Applicable Date(s)
{output["Applicable Date(s)"]}

7. Partnership Details
{output["Partnership Details"]}
"""
    return summary


def format_milestone_achievement(output):
    summary = f"""
1. Name 
{output["Name"]}

2. Date 
{output["Date"]}

3. Accomplished 
{output["Accomplished"]}

4. Details 
{output["Details"]}
"""
    return summary


def format_major_use_case(output):
    summary = f"""
1. Title 
{output["Title"]}

2. Applicable Date(s) 
{output["Applicable Date(s)"]}

3. Type 
{output["Type"]}

4. Category 
{output["Category"]}

5. Main Participant 
Name: {output["Main Participant"]["Main Participant's Name"]}
Company Website: {output["Main Participant"]["Main Participant's Website"]}
Sector: {output["Main Participant"]["Main Participant's Sector"]}
Company Details: 
    {output["Main Participant"]["Main Participant's Details"]}

6. List of others involved 
Name: {output["List of others involved"]["Involved Entity's Name"]}
Company Website: {output["List of others involved"]["Involved Entity's Website"]}

7. Details 
{output["Details"]}
"""
    return summary


def format_ir_event(output):
    summary = f"""
1. IR Activity Type 
{output["IR Activity Type"]}

2. Applicable Date(s) 
{output["Applicable Date(s)"]}

3. Events 
Online: {output["Event"]["Online event"]}
Offline:
    Location: {output["Event"]["Offline event Location"]}
    Address: {output["Event"]["Offline event Address"]}

4. Purpose
{output["Purpose"]}

5. Details
{output["Details"]}

6. Sponsorships
Name: {output["Sponsorships"]["Sponsorships Name"]}
Details: {output["Sponsorships"]["Sponsorships Details"]}

7. Other relevant information
Related disclosure: 
{output["Related disclosure"]}
"""
    return summary


def format_governance_proposal(output):
    summary = f"""
1. Category 
{output["Category"]}

2. Subject 
{output["Subject"]}

3. Proposal Date 
{output["Proposal Date"]}

4. Proposer 
    Name: {output["Proposer Name"]}
    Category: {output["Proposer Category"]}

5. Details
{output["Details"]}
"""
    return summary


def format_product_service_roadmap(output):
    summary = f"""
1. Title 
{output["Title"]}

2. Date to be Accomplished 
{output["Date to be Accomplished"]}

3. Details 
{output["Details"]}

4. Project roadmap disclosure URL 
{output["Project Roadmap Disclosure URL"]}
"""
    return summary


def format_fundraising(output):
    summary = f"""
1. Subject 
{output["Subject"]}

2. Applicable Date(s) 
{output["Applicable Date(s)"]}

3. Details 
{output["Details"]}
"""
    return summary
    

def format_roadmap_release(output):
    summary = f"""
1. Title 
{output["Title"]}

2. Timeline 
{output["Timeline"]}

3. Date of announcement 
{output["Date of Announcement"]}

4. Details 
{output["Details"]}
"""
    return summary
    

def format_governance_decision(output):
    summary = f"""
1. Subject 
{output["Subject"]}

2. Applicable Date 
{output["Applicable Date"]}

3. Details 
{output["Details"]}

4. Block Number 
{output["Block Number"]}

5. Transaction Hash 
{output["Transaction Hash"]}

6. Protocol Proposal Disclosure URL 
{output["Protocol Proposal Disclosure URL"]}
"""
    return summary


def format_token_swap(output):
    summary = f"""
1. Applicable Date(s)
{output["Applicable Date(s)"]}

2. Announcement Type 
{output["Announcement Type"]}

3. Purpose of token swap 
{output["Purpose of token swap"]}

4. Details 
Token Name: {output["Details"]["Token Name"]}
Swap Amount (Tokens): {output["Details"]["Swap Amount (Tokens)"]}
Exchanges officially supporting token swap(Exchange Name: URL): 
    {output["Details"]["Supporting Exchange's Name"]}:{output["Details"]["Supporting Exchange's URL"]}
    
5. Other relevant information 
{output["Other relevant information"]}
"""
    return summary


def format_exchange_warning_issued(output):
    summary = f"""
1. Exchange Name 
{output["Relevant Exchange"]}

2. Date (Applicable Date) 
{output["Date (Applicable Date)"]}

3. Details 
{output["Details"]}
"""
    return summary


def format_fork(output):
    summary = f"""
1. Applicable Date(s) 
{output["Applicable Date(s)"]}

2. Announcement Type 
{output["Announcement Type"]}

3. Fork Type 
{output["Fork Type"]}

4. Purpose of token fork 
{output["Purpose of token fork"]}

5. Details 
{output["Details"]}

6. Other relevant information 
{output["Other relevant information"]}
"""
    return summary


def format_delisting(output):
    summary = f"""
1. Exchange Name 
{output["Exchange Name"]}

2. Date (Estimated Date) 
{output["Date (Estimated Date)"]}

3. Details 
Name: {output["Details"]["Name"]}
Symbol: {output["Details"]["Symbol"]}

Key Dates 
Deposit deadline: {output["Details"]["Key Dates"]["Deposit deadline"]}
Trading deadline: {output["Details"]["Key Dates"]["Trading deadline"]}
Withdrawal deadline: {output["Details"]["Key Dates"]["Withdrawal deadline"]}

{output["Details"]["Reason"]}
"""
    return summary


def format_warning_withdrawn(output):
    summary = f"""
1. Relevant Exchange 
{output["Relevant Exchange"]}

2. Date (Applicable Date) 
{output["Date (Applicable Date)"]}

3. Details 
{output["Reason"]}

Date of Termination: {output["Date of Termination"]}
Time of Deposit Service Resumption: {output["Time of Deposit Service Resumption"]}
"""
    return summary


FORMAT_FUNC = {
    'new_listing': format_new_listing,
    'new_partnership': format_new_partnership,
    'milestone_achievement': format_milestone_achievement,
    'major_use_case': format_major_use_case,
    'ir_event': format_ir_event,
    'governance_proposal': format_governance_proposal,
    'product_service_roadmap': format_product_service_roadmap,
    'fundraising': format_fundraising,
    'roadmap_release': format_roadmap_release,
    'governance_decision': format_governance_decision,
    'token_swap': format_token_swap,
    'exchange_warning_issued': format_exchange_warning_issued,
    'fork': format_fork,
    'delisting': format_delisting,
    'warning_withdrawn': format_warning_withdrawn,
}
