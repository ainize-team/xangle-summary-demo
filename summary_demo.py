import requests
from enum import Enum
from pydantic import BaseModel, Field
from nlpretext import Preprocessor
from nlpretext.basic.preprocess import normalize_whitespace, fix_bad_unicode


preprocessor = Preprocessor()
preprocessor.pipe(normalize_whitespace)
preprocessor.pipe(fix_bad_unicode)

class Categories(str, Enum):
    new_listing = 'New Listing'
    new_partnership = 'New Partnership'


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
        Categories.new_listing, 
        title="Category of public notice"
    )


class TextGenerationOutput(BaseModel):
    output: str


# max_length is not used
def process(context, category):
    data = {
        'context': preprocessor.run(context),
        'category': category,
    }

    summary = ''

    for i, sub_category in enumerate(sub_categories[category]):
        # res = requests.post(f'http://localhost/api/{category}/{sub_category}', data=json.dumps(data), headers={"Content-Type": "application/json"})
        
        res = {
            'summary': 'Lorem ipsum dolor sit amet'
        }

        summary += f'{i+1}. {sub_category}' + '\n' + f'{res["summary"]}' + '\n\n'

    return summary


def xangle_context_summary(input: TextGenerationInput) -> TextGenerationOutput:
    """Select category of public notice on sidebar."""
    context = input.context  # base_text
    category = input.category

    summary = process(context, category)

    return TextGenerationOutput(output=summary)
