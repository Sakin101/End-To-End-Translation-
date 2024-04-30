from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
import os
import openai


os.environ['OPENAI_API_KEY'] = API_KEY  #  insert your opeanai api key
openai.api_key = os.environ["OPENAI_API_KEY"]


# function to call OpenAI APIs
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

prompt_template_str = """
Provide the code for the following pseudocode.

<<<PSEUDOCODE>>>
```
{pseudocode}
```

Use the following example as a context
<<<EXAMPLE>>>
```
<<<PSEUDOCODE>>>
```
{ex_pseudocode}
```
<<<CODE>>>
```
{ex_code}
```
```
"""
 
prompt_template = PromptTemplate.from_template(template=prompt_template_str)



prompt = (
    prompt_template.format(
        pseudocode = 'create map iterator it from string to integer\n\ncreate integer n\nread n\nread character\nfor i = 0 to n exclusive\ncreate sting str\nread line from cin to str\nset m[str] to 1\n\ncreate integer ans with ans = 0\nfor it = beginning of m to it is not end of m_._ incrementing it_._ increment ans\nprint ans print newline\n\n',
        ex_pseudocode = 'let a and b be strings\nn = integer\nst = set of strings\nread n\nfor integer i = 0 to n exclusive\nread a and b\ninsert a + " " + b into st\n\nprint size of st and a new line\n\n\n',
        ex_code = '#include <iostream>\nusing namespace std;\n int main(){ \nstring a_._ b;\nint n;\nset<string> st;\ncin >> n;\nfor (int i = 0; i < n; i++) {\ncin >> a >> b;\nst.insert(a + " " + b);\n}\ncout << st.size() << endl;\nreturn 0;\n}\n'
    )
)

result = get_completion(prompt)
print(result)
