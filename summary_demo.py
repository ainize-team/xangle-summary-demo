import requests
import streamlit as st

from enum import Enum
from pydantic import BaseModel, Field, HttpUrl
from nlpretext import Preprocessor
from nlpretext.basic.preprocess import normalize_whitespace, fix_bad_unicode
from utils import format_new_listing, format_new_partnership, FORMAT_FUNC


preprocessor = Preprocessor()
preprocessor.pipe(normalize_whitespace)
preprocessor.pipe(fix_bad_unicode)


class Categories(str, Enum):
    NEWLISTING = 'New Listing'
    NEWPARTNERSHIP = 'New Partnership'


SUB_CATEGORIES = {
    'New Listing': [
        "Exchange Name", 
        "Date (Estimated Date)", 
        "Name", 
        "Symbol / Ticker", 
        "Wallet creation and deposit requests opening date", 
        "Trading opening date", 
        "Withdrawal opening date", 
        "Withdrawal fee", 
        "Announced listing pairs", 
        "Listing price", 
        "Minimum Trade/Purchase Amount", 
        "Minimum Price Movement", 
        "Minimum Order Size", 
        "Exchange promoted listing/airdrop event",
    ],
    'New Partnership': [
        "Partner's Name", 
        "Counterparty Website", 
        "Counterparty Details", 
        "Does this partnership generate any kind of revenue?", 
        "Applicable Date(s)", 
        "Partnership Details"
    ]
}

class OtherData(BaseModel):
    text: str


class TextGenerationInput(BaseModel):
    model_url: HttpUrl = Field(
        '',
        title="Model URL",
        description="URL to request API.",
    )

    category: Categories = Field(
        Categories.NEWLISTING, 
        title="Category of public notice"
    )

    context: str = Field(
        title="Input Context",
        description="Context to summary public notice.",
    )


class TextGenerationOutput(BaseModel):
    output: str


def process(model_url, context, category):
    summary = ''
    outputs = {}
    for i, sub_category in enumerate(SUB_CATEGORIES[category]):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url=model_url, headers=headers, json={"context": preprocessor.run(context), "category": sub_category})
        output = response.json()

        outputs.update({sub_category: output})

    summary = FORMAT_FUNC[category](outputs)

    return summary


def xangle_context_summary(input: TextGenerationInput) -> TextGenerationOutput:
    """Select category of public notice on sidebar."""
    context = input.context
    category = input.category
    model_url = input.model_url

    summary = process(model_url, context, category)

    return TextGenerationOutput(output=summary)
