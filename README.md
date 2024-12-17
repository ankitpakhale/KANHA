## **KANHA** – **Kustomized Assessment & NLP-based Hyperpersonalized Audit**

### **Project Structure**

```
KANHA
├── cookbook
│   └── version1
│       └── index.md
├── infra
│   ├── environments
│   │   ├── dev
│   │   │   ├── docker-compose.yml
│   │   │   └── Dockerfile
│   │   ├── prod
│   │   │   ├── docker-compose.yml
│   │   │   └── Dockerfile
│   │   ├── qa
│   │   │   ├── docker-compose.yml
│   │   │   └── Dockerfile
│   │   └── stage
│   │       ├── docker-compose.yml
│   │       └── Dockerfile
│   └── terraform
│       ├── lambda_code
│       │   ├── app.py
│       │   ├── main.tf
│       │   ├── outputs.tf
│       │   ├── provider.tf
│       │   ├── requirements.txt
│       │   ├── terraform.tfstate
│       │   └── variables.tf
│       ├── main.tf
│       ├── outputs.tf
│       ├── provider.tf
│       ├── terraform.tfstate
│       └── variables.tf
├── LICENSE
├── Makefile
├── poetry.lock
├── pyproject.toml
├── README.md
├── release
├── requirements.txt
├── setup.py
├── src
│   ├── clients
│   │   ├── base.py
│   │   ├── client_types
│   │   │   ├── bedrock_client.py
│   │   │   ├── __init__.py
│   │   │   └── openai_client.py
│   │   ├── docs
│   │   │   ├── ClientPackageArchitectureDiagram.png
│   │   │   └── docs.md
│   │   ├── factory.py
│   │   ├── __init__.py
│   │   ├── payload
│   │   │   ├── request_examples
│   │   │   │   ├── evaluate_answers.json
│   │   │   │   └── generate_questions.json
│   │   │   └── response_examples
│   │   │       ├── evaluate_answers.json
│   │   │       └── generate_questions.json
│   │   ├── tests
│   │   │   ├── test_evaluate_answers.py
│   │   │   └── test_generate_questions.py
│   │   └── utils.py
│   ├── config
│   │   ├── aws_config.py
│   │   ├── base_config.py
│   │   ├── env_config.py
│   │   ├── general_config.py
│   │   ├── __init__.py
│   │   └── openai_config.py
│   ├── framework
│   │   ├── bottle_app.py
│   │   └── __init__.py
│   ├── main.py
│   ├── prompts
│   │   ├── answer_evaluation
│   │   │   ├── __init__.py
│   │   │   ├── system_prompts.py
│   │   │   └── user_prompts.py
│   │   ├── factory
│   │   │   ├── answer_evaluation_prompt.py
│   │   │   ├── base_prompt.py
│   │   │   ├── __init__.py
│   │   │   ├── prompt_factory.py
│   │   │   └── question_generation_prompt.py
│   │   ├── __init__.py
│   │   ├── question_generation
│   │   │   ├── __init__.py
│   │   │   ├── system_prompts.py
│   │   │   └── user_prompts.py
│   │   └── tests
│   │       ├── test_answer_evaluation_prompt.py
│   │       └── test_question_generation_prompt.py
│   ├── repository
│   │   ├── evaluation_repo.py
│   │   ├── __init__.py
│   │   └── question_repo.py
│   ├── routes
│   │   ├── cache_route.py
│   │   ├── constants.py
│   │   ├── evaluation_route.py
│   │   ├── healthcheck_route.py
│   │   ├── __init__.py
│   │   └── question_route.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── service_types
│   │   │   ├── evaluation_service.py
│   │   │   ├── __init__.py
│   │   │   └── question_service.py
│   │   ├── tests
│   │   │   ├── test_evaluation_service.py
│   │   │   └── test_question_service.py
│   │   └── validation_manager
│   │       ├── __init__.py
│   │       ├── schema_map.py
│   │       ├── strategy
│   │       │   ├── base.py
│   │       │   ├── evaluate_answers_request_payload.py
│   │       │   ├── evaluate_answers_response_payload.py
│   │       │   ├── generate_questions_request_payload.py
│   │       │   ├── generate_questions_response_payload.py
│   │       │   └── __init__.py
│   │       ├── tests.py
│   │       └── validation_manager.py
│   └── utils
│       ├── cache
│       │   ├── __init__.py
│       │   └── manager.py
│       ├── __init__.py
│       ├── logging
│       │   ├── base.py
│       │   ├── filters.py
│       │   ├── formatters.py
│       │   ├── handlers.py
│       │   └── __init__.py
│       └── response_manager
│           ├── __init__.py
│           └── response_manager.py
└── entrypoint.sh

```

### **Project Overview**

**KANHA** is a cutting-edge, AI-driven platform designed to provide highly personalized programming assessments and evaluate user submissions with precision. By leveraging NLP (Natural Language Processing) and AI, KANHA delivers customized question sets tailored to individual user requirements, ensuring a unique and efficient learning or assessment experience. The system focuses on two key processes: generating questions based on user inputs and evaluating answers with meaningful feedback. The platform awards points for programming questions based on initial code quality and provides optimized solutions for improvement.

---

### **Core Features**

1.  **User-Driven Customization**
    - **Inputs:**
      - Level of Difficulty: Easy, Medium, High.
      - Programming Language: Python, Java, C++, etc.
      - Topics: Specific topics or "All" for a comprehensive assessment.
2.  **Question Generation**

    - AI-powered generation of question sets tailored to user inputs:
      - **Easy Level**: 20 multiple-choice questions (MCQs).
      - **Medium Level**: 12 MCQs + 8 programming questions.
      - **High Level**: 20 programming questions.

3.  **Answer Evaluation**
    - Programming questions are evaluated based on initial code quality, awarding points for correctness, efficiency, and adherence to best practices. Optimized solutions are provided for improvement.
    - MCQ responses are marked as correct or incorrect.
4.  **Streamlined Two-Step Process**

    - **Step 1:** Question Generation: Generates a personalized set of questions.
    - **Step 2:** Answer Evaluation: Reviews submissions, awards points, and provides suggestions for programming questions.

---

### **Technology Stack**

1.  **Libraries**

    - **OpenAI API**: For generating NLP-based personalized questions and optimized solutions.
    - **Langchain**: For managing AI interactions and automating workflows.

2.  **APIs**

    - **RESTful API**: Facilitates communication between the frontend and backend services.

3.  **Infrastructure**

    - **Docker**: Used for containerization to ensure consistent deployment across environments.
    - **AWS Lambda**: Deploys the two services (Question Generation and Answer Evaluation) in a serverless, scalable architecture.

4.  **Database**

    - **Amazon RDS (PostgreSQL)**: Manages structured data such as user information, question sets, and evaluation results.
    - **Amazon S3**: Stores large unstructured data like question banks and evaluation logs.

5.  **Message Queues**

    - **Kafka**: Ensures asynchronous communication between services, supporting a distributed architecture.

6.  **CI/CD**

    - **GitHub Actions**: Automates the build, test, and deployment pipelines.

7.  **Hosting**

    - **AWS**: Provides cloud infrastructure for hosting backend services, APIs, and storage.

---

### **System Workflow**

1.  **User Journey**

    - The user logs in and specifies assessment requirements: difficulty level, topics, and programming language.
    - The frontend communicates with the backend via RESTful API to request a personalized question set.
    - The Question Generation Service (AWS Lambda) generates the questions and returns them to the user.
    - The user submits answers.
    - The Answer Evaluation Service (AWS Lambda) evaluates the submissions, providing scores and optimized solutions for programming questions.

2.  **Backend Architecture**

    - **Question Generation Service:** Generates customized questions based on user inputs and integrates with OpenAI and Langchain for NLP-driven question creation.
    - **Answer Evaluation Service:** Evaluates answers, provides feedback, awards points, and generates optimized programming solutions.

---

### **Scalability and Performance**

1.  **AWS Lambda**

    - A serverless architecture ensures automatic scaling and cost efficiency. Each request is processed independently, allowing the system to handle varying workloads seamlessly.

2.  **Kafka**

    - Kafka enables decoupled communication between the two services (Question Generation and Answer Evaluation), ensuring asynchronous processing and system resilience.

3.  **Amazon RDS and S3**

    - RDS handles structured data efficiently, while S3 provides scalable storage for unstructured data like logs and question sets.

---

### **Security and Privacy**

1.  **Data Encryption**

    - All data, including user submissions and question sets, is encrypted in transit (HTTPS) and at rest (RDS and S3).

2.  **Access Control**

    - Role-based access control (RBAC) restricts access to sensitive data and APIs.

3.  **User Privacy**

    - Compliant with GDPR and other privacy regulations, ensuring data protection and anonymity.

---

### **Future Enhancements**

1.  **Dynamic Difficulty Adjustment**

    - The system can dynamically adjust question difficulty based on user performance.

2.  **Multi-Language Support**

    - Expanding the platform to support additional programming languages and natural languages.

3.  **Plagiarism Detection**

    - Adding a feature to detect plagiarized programming submissions.

4.  **Gamification Features**

    - Incorporating leaderboards, badges, and achievements to enhance user engagement.

---

### **Conclusion**

**KANHA** is a powerful, AI-driven assessment platform designed to deliver tailored evaluation experiences. It offers two key services:

- **Question Generation**
- **Answer Evaluation**

Both services are hosted on **AWS Lambda** for optimal scalability and efficiency. By integrating advanced **Natural Language Processing (NLP)** capabilities with a distributed architecture, **KANHA** ensures personalized and meaningful assessments that foster skill improvement and engagement.

The platform’s robust technology stack, coupled with its scalable design, makes it a versatile solution for various industries:

- **Education**
- **Training**
- **Recruitment**
- **Other**

---

I hope **KANHA** helps you achieve your evaluation goals! For more information or to provide feedback, visit at [https://ankitpakhale.netlify.app](https://ankitpakhale.netlify.app). I’d love to hear from you!
