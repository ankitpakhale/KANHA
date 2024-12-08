### Expected Client Packages Structure

- Client packages will follow encapsulation logic

```bash
- Base Client
  - Prompt -> Prompt class to generate system & user prompt, based on type like question generation and answer evaluation

- Bedrock Client
  - Base Bedrock Client
    - BedrockClient -> BedrockClient class
    - BedrockStrategy -> BedrockStrategy class
  - generate_questions.py -> GenerateQuestionStrategy class Inheriting Base Bedrock classes
  - evaluate_answers.py -> EvaluateAnswerStrategy class Inheriting Base Bedrock classes

- OpenAI Client
  - Base OpenAI Client: Should Include core logic of calling OpenAI API "openai.ChatCompletion.create()"
    - OpenAIClient -> OpenAIClient class
    - OpenAIStrategy -> OpenAIStrategy class
  - generate_questions.py -> GenerateQuestionStrategy class Inheriting Base Bedrock classes
  - evaluate_answers.py -> EvaluateAnswerStrategy class Inheriting Base Bedrock classes

- tests
  - test_generate_questions.py
  - test_evaluate_answers.py
```

### Evaluate Answer Schema

```json
[
  {
    "question": "",
    "user_code": "<USER_CODE>"
  },
  {
    "question": "",
    "user_code": "<USER_CODE>"
  }
]
```
