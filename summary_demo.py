import requests
import streamlit as st

from enum import Enum
from pydantic import BaseModel, Field
from nlpretext import Preprocessor
from nlpretext.basic.preprocess import normalize_whitespace, fix_bad_unicode
from utils import *


preprocessor = Preprocessor()
preprocessor.pipe(normalize_whitespace)
preprocessor.pipe(fix_bad_unicode)


class DocumentType(str, Enum):
    NEWLISTING = 'new_listing'
    NEWPARTNERSHIP = 'new_partnership'
    MILESTONE_ACHIEVEMENT = 'milestone_achievement'
    MAJORUSECASE = 'major_use_case'
    IREVENT = 'ir_event'
    GOVERNANCE_PROPOSAL = 'governance_proposal'
    PRODUCT_SERVICE_ROADMAP = 'product_service_roadmap'
    FUNDRAISING = 'fundraising'
    ROADMAP_RELEASE = 'roadmap_release'
    GOVERNANCE_DECISION = 'governance_decision'
    TOKEN_SWAP = 'token_swap'
    EXCHANGE_WARNING_ISSUED = 'exchange_warning_issued'
    FORK = 'fork'
    DELISTING = 'delisting'
    WARNING_WITHDRAWN = 'warning_withdrawn'


class TextGenerationInput(BaseModel):
    doc_type: DocumentType = Field(
        DocumentType.NEWLISTING, 
        title="Type of Document of public notice"
    )

    context: str = Field(
        title="Input Context",
        description="Context to summary public notice.",
    )


class TextGenerationOutput(BaseModel):
    output: str


def process(context: str, doc_type: DocumentType) -> str:
    query_param = st.experimental_get_query_params()
    
    if 'api' in query_param:
        api_url = query_param['api'][0]
        try:
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            response = requests.post(url=api_url, headers=headers, json={"context": preprocessor.run(context), "docType": doc_type})

            output = response.json()

            results = FORMAT_FUNC[doc_type](output)
        except:
            results = 'Endpoint API Internal error occurs.'

    else:
        results = 'There is no endpoint API in Query String.'

    return results


def xangle_context_summary(input: TextGenerationInput) -> TextGenerationOutput:
    """Select type of Document on sidebar."""
    context = input.context
    doc_type = input.doc_type

    results = process(context, doc_type)

    return TextGenerationOutput(output=results)
