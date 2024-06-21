import json

import pandas as pd

from dvcx.lib.claude import claude_processor
from dvcx.lib.datachain import C, DataChain
from dvcx.lib.feature import Feature

SOURCE = "gs://dvcx-datalakes/chatbot-public"
MODEL = "claude-3-opus-20240229"
PROMPT = """Consider the dialogue between the 'user' and the 'bot'. \
The 'user' is a human trying to find the best mobile plan. \
The 'bot' is a chatbot designed to query the user and offer the \
best  solution. The dialog is successful if the 'bot' is able to \
gather the information and offer a plan, or inform the user that \
such plan does not exist. The dialog is not successful if the \
conversation ends early or the 'user' requests additional functions \
the 'bot' cannot perform. Read the dialogue below and rate it 'Success' \
if it is successful, and 'Failure' if not. After that, provide \
one-sentence explanation of the reasons for this rating. Use only \
JSON object as output with the keys 'status', and 'explanation'.
"""


class Rating(Feature):
    status: str = ""
    explanation: str = ""


chain = (
    DataChain.from_storage(SOURCE, is_text=True)
    .filter(C.name.glob("*.txt"))
    .limit(5)
    .map(claude=claude_processor(prompt=PROMPT, model=MODEL))
    .map(
        rating=lambda claude: Rating(
            **(json.loads(claude.content[0].text) if claude.content else {})
        ),
        output=Rating,
    )
)

df = chain.to_pandas()

with pd.option_context("display.max_columns", None):
    print(df)
