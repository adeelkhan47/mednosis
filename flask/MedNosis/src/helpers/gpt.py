from conf import settings
import openai

openai.api_key = settings.openai_key

def format_html(string):
    if type(string) == str:
        return string.replace('\n', '<br />')
    return string

def __query(prompt, max_tokens):
    try:
        response = openai.Completion.create(
            engine=settings.model,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return True, response.choices[0].text.strip().capitalize()
    except openai.error.InvalidRequestError as ex:
        if "maximum context length" in str(ex):
            return False, "The request is too long!"
        else:
            return False, ex
    except Exception as ex:
        return False, ex

def medical_prompt(question):
    question = question.replace('"', "'")
    prompt = "You are a doctor, you need to give medical advice for the given question.\n"
    prompt += "Do not answer non-medical questions. never use the following words: doctor, physician, visit, professional and appointment in your response.\n"
    prompt += "Give a list of possible diagnosis and treatments if applicable, include medications. Ask follow up questions to narrow down the diagnosis.\n\n"
    prompt += f"Question: {question}\n"
    prompt += "Answer:"
    success, data = __query(prompt, settings.max_tokens)
    return success, format_html(data)
