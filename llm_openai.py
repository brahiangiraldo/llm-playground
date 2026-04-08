from openai import OpenAI
from dotenv import load_dotenv

#cargar las variables de entorno del archivo .env
load_dotenv()


def openAIBasic(prompt):
    client = OpenAI()
    response = client.responses.create(
            model="gpt-5.4",
            input=prompt
        )
    return response.output_text

# response = openAIBasic('Dime cual es tu nombre y tu edad') 



#

# def textStreamTextgeneration(prompt: str):
        

#         client = OpenAI()

#         stream = client.responses.create(
#             model="gpt-5",
#             input=[
#                 {
#                     "role": "user",
#                     "content": prompt,
#                 },
#         ],
#         stream=True,
#     )

#         for event in stream:
#             print(event)

# textStreamTextgeneration('Dime el 11 ideal de francia en 2026')        

def textStreamTextGeneration(prompt: str):
        client = OpenAI()

        stream = client.responses.create(
            model="gpt-5",
            input=prompt,
            stream=True,
        )

        response_text = ""

        for event in stream:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
                response_text += event.delta


        return response_text


# textStreamTextGeneration("Cual es el 11 ideal de francia en 2026") 





def effortPirate(propmt: str):

    client = OpenAI()


    response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        instructions="Habla como un paisa y responde a la pregunta",
        input=propmt,
)

    print(response.output_text)

effortPirate("De donde es la arepa?")

















# Response(id='resp_0f09a57771bc718d0069c7231d75188199841026fe94eae7af',
#           created_at=1774658333.0, 
#           error=None, 
#           incomplete_details=None, 
#           instructions=None, 
#           metadata={}, 
#           model='gpt-5.4-2026-03-05', 
#           object='response', 
#           output=[
#               ResponseOutputMessage(id='msg_0f09a57771bc718d0069c7231dd9848199ac00cf3c2547ee1f', 
#               content=[ResponseOutputText(annotations=[],
#               text='Me llamo ChatGPT y no tengo una edad como una persona. Soy un modelo de IA creado por OpenAI. Si quieres, también puedo contarte “cuándo fui creado” o qué versión soy.', 
#               type='output_text', 
#               logprobs=[])
#               ], 
#               role='assistant',
#               status='completed', 
#               type='message', 
#               phase='final_answer')], 
#               parallel_tool_calls=True, temperature=1.0, 
#               tool_choice='auto', tools=[], top_p=0.98, background=False, 
#               completed_at=1774658334.0, conversation=None, 
#               max_output_tokens=None, max_tool_calls=None, 
#               previous_response_id=None, prompt=None, 
#               prompt_cache_key=None, prompt_cache_retention=None, 
#               reasoning=Reasoning(effort='none', 
#               generate_summary=None, summary=None), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=15, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=46, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=61), user=None, billing={'payer': 'developer'}, frequency_penalty=0.0, presence_penalty=0.0, store=True)