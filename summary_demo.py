import requests
from enum import Enum
from pydantic import BaseModel, Field
from nlpretext import Preprocessor
from nlpretext.basic.preprocess import normalize_whitespace, fix_bad_unicode


preprocessor = Preprocessor()
preprocessor.pipe(normalize_whitespace)
preprocessor.pipe(fix_bad_unicode)

# TODO: 필요한 카테고리 더 추가하기
class Categories(str, Enum):
    NEWLISTING = 'New Listing'
    NEWPARTNERSHIP = 'New Partnership'

# TODO: Categories 클래스에 있는 각 카테고리에 대해서 필요한 sub 카테고리 추가하기
SUB_CATEGORIES = {
    'New Listing': [
        "Exchange Name", 
        "Date (Estimated Date)", 
        "Name", 
        "Symbol / Ticker", 
        "Wallet creation and deposit requests opening date", 
        "Trading opening date", "Withdrawal opening date", 
        "Withdrawal fee", 
        "Announced listing pairs", 
        "Listing price", 
        "Minimum Trade/Purchase Amount", 
        "Minimum Price Movement", 
        "Minimum Order Size", 
        "Exchange promoted listing/airdrop event",
    ],
    'New Partnership': [
        "Applicable Date(s)", 
        "Partnership Details", 
        "Partner's Name", 
        "Counterparty Website", 
        "Counterparty Details", 
        "Does this partnership generate any kind of revenue?"
    ],
}


class TextGenerationInput(BaseModel):
    context: str = Field(
        ...,
        title="Input Context",
        description="Context to summary public notice.",
    )
    category: Categories = Field(
        Categories.NEWLISTING, 
        title="Category of public notice"
    )


class TextGenerationOutput(BaseModel):
    output: str


def process(context, category):
    summary = ''
    for i, sub_category in enumerate(SUB_CATEGORIES[category]):
        '''
        TODO
        - API 연동하기
        - DUMMY 데이터 삭제(Lorem ipsum...)
        '''

        model_url = 'https://train-mw86iwjxfypsj60gvh84-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/xangle-summary'
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url=model_url, headers=headers, json={"context": preprocessor.run(context), "category": sub_category})
        output = response.json()

        print(f'{i} => category : {sub_category}, output : {output}')

        summary += f'{i+1}. {sub_category}' + '\n' + f'{output}' + '\n\n'

    return summary


def xangle_context_summary(input: TextGenerationInput) -> TextGenerationOutput:
    """Select category of public notice on sidebar."""
    context = input.context
    category = input.category

    summary = process(context, category)

    return TextGenerationOutput(output=summary)
