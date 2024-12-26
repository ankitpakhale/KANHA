### TODO

- #### Tasklist 5
- [x] Save feedback in postgres.
- [ ] [HOLD] Save feedback in AWS RDS.
- [ ] [HOLD] Save feedback in AWS S3.

- #### Tasklist 6
- [ ] Fix Scheduled GH Workflow, fix psycopg2 library issue.
- [ ] Adjust frontend code to send user answers.
- [ ] Adjust frontend code to send user answers.
- [ ] Make Answer Evaluation code FINALIZE.

### BACKLOG

- #### Tasklist 1
- [ ] [HOLD] Add core logic of question generation in Bedrock client.

- #### Tasklist 4
- [ ] [HOLD] Add core logic of answer evaluation in AWS Bedrock client.
- [ ] [HOLD] Add core logic of question generation in AWS Bedrock client.

- #### Tasklist 7
- [ ] Update docs like, maintaining release version, cookbook & README file.
- [ ] Integrate OpenAI client with Frontend.
- [ ] Change Difficulty Level to Position like (junior, senior, technical specialist).

- #### Tasklist 7.5
- [ ] Implement slash command to register new route.
- [ ] Implement slash command to check all registered routes.
- [ ] Implement slash command to delete any route.
- [ ] Implement slash command to create new service_type in service_types directory.

- #### Tasklist 8
- [ ] Take programming_language input in the form of List like topic in QuestionGenerationService.
- [ ] Add adapter layer in src.
- [ ] Replace existing caching with RADIS.
- [ ] Fix all type hinting is all the methods like QuestionService.
- [ ] Implement Pydentic library for validations.
- [ ] Automate the process of registering the routes (check all the files in routes directory that starts with route\_, register those routes).
- [ ] Add retry mechanism if client fails the data generation or evaluation.

- #### Tasklist 9
- [ ] Decide deployment stratefy.
- [ ] Prototype of Terrafrom with GH actions on AWS Lambda deployment.

- #### Tasklist 10
- [ ] Implement time bound functionality, adjust FE and BE accordingly.
- [ ] Implement sharable URL for performing interview.

- #### Tasklist 11
- [ ] Make Requests Async.
- [ ] Add RAG model in the next stable version.
- [ ] Integrate users feedback with RAG model.

- #### Tasklist 12
- [ ] Check all the todo notes in BE & FE.

### COMPLETED

- #### Tasklist 1
- [x] Make a base client layer then actual client layer and then service layer.
- [x] Design evaluate answer schema.
- [x] Adjust the evaluate answer prompt as per the above task.

- #### Tasklist 2
- [x] Make Question Generation code FINALIZE.
- [x] Fix logger issue.
- [x] Add caching layer.
- [x] Add logs in .kanha_logs/logs_0.log file.
- [x] Fix validation manager issue / Json Schema.

- #### Tasklist 3
- [x] Add base layer logic of OpenAI client.
- [x] Add core logic of answer evaluation in OpenAI client.
- [x] Add core logic of question generation in OpenAI client.

- #### Tasklist 4
- [x] Add base layer logic of AWS Bedrock client.

- #### Tasklist 5
- [x] Add base layer for feedback route.
- [x] Design feedback schema, what questions to ask.
- [x] Implement Validation logic in feedback route.
- [ ] [HOLD] Save feedback in DB (RDS, postgres or any). (depend on Tasklist 5.1)

- #### Tasklist 5.1
- [x] Implement dao (data access object package) in source.
- [x] Create basic files and structure of dao.
- [x] Create base layer of dao package.
- [x] Create models and layer of integration with specific database (postgres, RDS, S3, etc).

- #### Tasklist 5.2
- [x] Make centralized test package in source directory.
- [x] Fix all the constants file, there should be single contants file and everything will be class based implemented.
