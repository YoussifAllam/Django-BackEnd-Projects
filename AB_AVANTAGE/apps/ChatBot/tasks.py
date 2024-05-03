from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from django.conf import settings

tone_of_voice_list = ('Excited', 'Professional', 'Encouraging', 'Funny', 'Dramatic', 'Witty', 'Sarcastic', 'Engaging', 'Creative')
models = ('Cohere ', 'GPT-3.5', 'GPT-4')
creativity_dict = {
    'Original':0.0,
    'Balanced':0.25,
    'Creative':0.5, 
    'Spirited':0.75,
    'Visionary':1.0
}

def generator( prompt:str , inputs:dict , creativity_idx = 4 ) -> str:
    creativity = list(creativity_dict.keys())[creativity_idx]
    temp = creativity_dict[creativity]

    llm = ChatGoogleGenerativeAI( model = 'gemini-pro', temperature = temp , google_api_key = settings.GOOGLE_API_KEY)

    promptTemp = ChatPromptTemplate.from_template(template=prompt)
    try:
        output_parser = JsonOutputParser()
        chain = promptTemp | llm | output_parser
        generator_output = chain.invoke(inputs)
        return generator_output
    except Exception as e:
        # print("Handling non-JSON output or error:", str(e))
        output_parser = StrOutputParser()
        chain = promptTemp | llm | output_parser
        generator_output = chain.invoke(inputs)
        return generator_output

# input_dict = {'keyword': 'hello'}
# response = generator('tell me about you', input_dict, model_name='gemini')
# print(response)
