### BACKLOG

- #### Tasklist 1
- [ ] [HOLD] Add core logic of question generation in Bedrock client

- #### Tasklist 4
- [ ] [HOLD] Add core logic of answer evaluation in AWS Bedrock client
- [ ] [HOLD] Add core logic of question generation in AWS Bedrock client

- #### Tasklist 6
- [ ] Update docs like, maintaining release version, cookbook & README file
- [ ] Integrate OpenAI client with Frontend

- #### Tasklist 7
- [ ] Adjust frontend code to send user answers
- [ ] Adjust frontend code to send user answers
- [ ] Make Answer Evaluation code FINALIZE

- #### Tasklist 8
- [ ] Add adapter layer in src.
- [ ] Automate the process of registering the routes (check all the files in routes directory that starts with route\_, register those routes).
- [ ] Add retry mechanism if client fails the data generation or evaluation.

- #### Tasklist 9
- [ ] Decide deployment stratefy.
- [ ] Prototype of Terrafrom with GH actions on AWS Lambda deployment.

- #### Tasklist 10
- [ ] Implement time bound functionality, adjust FE and BE accordingly
- [ ] Implement sharable URL for performing interview

- #### Tasklist 11
- [ ] Make Requests Async
- [ ] Add RAG models in the next stable version

- #### Tasklist 12
- [ ] Check all the todo notes in BE & FE

### TODO:

- #### Tasklist 5
- [ ] Add feedback route
- [ ] Design feedback schema, what questions to ask
- [ ] Save feedback in DB (RDS, postgres or any)
- [ ] Integrate feedback questions with RAG models

### COMPLETED

- #### Tasklist 1
- [x] Make a base client layer then actual client layer and then service layer
- [x] Design evaluate answer schema
- [x] Adjust the evaluate answer prompt as per the above task

- #### Tasklist 2
- [x] Make Question Generation code FINALIZE
- [x] Fix logger issue
- [x] Add caching layer
- [x] Add logs in .kanha_logs/logs_0.log file
- [x] Fix validation manager issue / Json Schema

- #### Tasklist 3
- [x] Add base layer logic of OpenAI client
- [x] Add core logic of answer evaluation in OpenAI client
- [x] Add core logic of question generation in OpenAI client

- #### Tasklist 4
- [x] Add base layer logic of AWS Bedrock client