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
sub_categories = {
    'New Listing': ['Coin Name', 'Exchange Name'],
    'New Partnership': ['Coin Name2', 'Exchange Name2'],
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
    data = {
        'context': preprocessor.run(context),
        'category': category,
    }

    summary = ''

    for i, sub_category in enumerate(sub_categories[category]):
        '''
        TODO
        - API 연동하기
        - DUMMY 데이터 삭제(Lorem ipsum...)
        '''
        res = {
            'summary': 'Lorem ipsum dolor sit amet'
        }

        summary += f'{i+1}. {sub_category}' + '\n' + f'{res["summary"]}' + '\n\n'

    return summary


def xangle_context_summary(input: TextGenerationInput) -> TextGenerationOutput:
    """Select category of public notice on sidebar."""
    context = input.context
    category = input.category

    summary = process(context, category)

    return TextGenerationOutput(output=summary)
