### TODO

- #### Tasklist 10
- [ ] Remove total number of questions to generate from system prompt & adjust this same thing in user prompt.
- [ ] Prompts must be compatible with Pricing Page of KanhaUI.

- #### Tasklist 10.1
- [ ] Simplify routes package ex server healthcheck & db healthcheck.
- [ ] Implement changes in DAO package to save mcq type of questions.
- [ ] Implement changes in DAO package to save psq type of questions.
- [ ] Get at least 1000 MCQ questions using GPT and save it in csv and then DB.
- [ ] Get at least 500 PSQ Medium level questions using GPT and save it in csv and then DB.
- [ ] Get at least 500 PSQ Hard level questions using GPT and save it in csv and then DB.

### BACKLOG

- #### Tasklist 5
- [ ] [HOLD] Save feedback in DB (RDS, postgres or any). (depend on Tasklist 5.1)

- #### Tasklist 9
- [ ] [HOLD] Save feedback in AWS RDS.
- [ ] [HOLD] Save feedback in AWS S3.

- #### Tasklist 11
- [ ] [HOLD] Add core logic of question generation in Bedrock client.

- #### Tasklist 12
- [ ] [HOLD] Add core logic of answer evaluation in AWS Bedrock client.
- [ ] [HOLD] Add core logic of question generation in AWS Bedrock client.

- #### Tasklist 13
- [ ] Save valid question obj in DB regardless of question type, received from User Query.
- [ ] If any request comes, don't call OpenAI instead fetch data from DB randomly and return it to user.
- [ ] Find a fix for malformed/broken json, extract proper json objects from received questions list from GPT and save it in DB and return it.

- #### Tasklist 14
- [ ] Fix Scheduled GH Workflow, fix psycopg2 library issue.
- [ ] Adjust frontend code to send user answers.
- [ ] Adjust frontend code to send user answers.
- [ ] Test caching properly in all the routes.
- [ ] Make Answer Evaluation code FINALIZE.

- #### Tasklist 15
- [ ] Update docs like, maintaining release version, cookbook & README file.
- [ ] Integrate OpenAI client with Frontend.
- [ ] Change Difficulty Level to Position like (junior, senior, technical specialist).

### Tasklist 16:

- [ ] Investigate the issue causing the system to crash due to framework-related errors.
- [ ] If the Bottle framework goes down, automatically switch to the Flask framework.
- [ ] If Flask fails, switch to the FastAPI framework.
- [ ] If FastAPI fails, verify that the system returns to Flask or Bottle
- [ ] Set up monitoring for all three frameworks (Bottle, Flask, and FastAPI) to detect failures in real-time.
- [ ] Implement automated alerts to notify the team if any framework goes down and failover occurs.
- [ ] Perform load testing to ensure all three frameworks can handle traffic appropriately and failover works seamlessly under heavy load. (Use a load testing tool e.g., Apache JMeter, Locust)
- [ ] Document the failover procedures and system architecture to ensure clear understanding for future maintenance and troubleshooting.
- [ ] Schedule regular system health checks to proactively identify potential issues with the frameworks.
- [ ] Test the failover mechanism in various scenarios to ensure the system remains stable and functional during failures. (e.g., kill the process or cause an error that leads to a crash).

- #### Tasklist 17
- [ ] Implement slash command to register new route.
- [ ] Implement slash command to check all registered routes.
- [ ] Implement slash command to delete any route.
- [ ] Implement slash command to create new service_type in service_types directory.

- #### Tasklist 18
- [ ] Take programming_language input in the form of List like topic in QuestionGenerationService.
- [ ] Add adapter layer in app.
- [ ] Replace existing caching with RADIS.
- [ ] Fix all type hinting is all the methods like QuestionService.
- [ ] Implement Pydentic library for validations.
- [ ] Automate the process of registering the routes (check all the files in routes directory that starts with route\_, register those routes).
- [ ] Add retry mechanism if client fails the data generation or evaluation.

- #### Tasklist 19
- [ ] Decide deployment stratefy.
- [ ] Prototype of Terrafrom with GH actions on AWS Lambda deployment.

- #### Tasklist 20
- [ ] Implement time bound functionality, adjust FE and BE accordingly.
- [ ] Implement sharable URL for performing interview.

- #### Tasklist 21
- [ ] Make Requests Async.
- [ ] Add RAG model in the next stable version.
- [ ] Integrate users feedback with RAG model.

- #### Tasklist 22
- [ ] Check all the todo notes in BE & FE.

- #### Tasklist 23
- [ ] Implement voice assistance system to take introductory round of interview and preparation.
- [ ] Calculate score of Introductory round based on facial expresion (confidance), body language, speech, level of articulation.

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

- #### Tasklist 6
- [x] Implement dao (data access object package) in source.
- [x] Create basic files and structure of dao.
- [x] Create base layer of dao package.
- [x] Create models and layer of integration with specific database (postgres, RDS, S3, etc).

- #### Tasklist 7
- [x] Make centralized test package in source directory.
- [x] Fix all the constants file, there should be single contants file and everything will be class based implemented.

- #### Tasklist 8
- [x] Design DB schema for MCQ type questions.
- [x] Design DB schema for PSQ type questions and add question level field.
- [x] Rename app to app.

- #### Tasklist 9
- [x] Save feedback in postgres.

- #### Tasklist 9.1
- [x] Design contact model.
- [x] Save contact in postgres.
- [x] Write testcases for contact.
- [x] Implement contact route.
- [x] Implement contact service.

- #### Tasklist 9.2
- [x] Add required_time field in MCQ & PSQ models.
- [x] Apply SOLID Principles in Question Service.
- [x] Make changes in MCQ & PSQ test files to implement required_time field.
