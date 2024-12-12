## **KANHA** – **Kustomized Assessment & NLP-based Hyperpersonalized Audit**

### **Project Structure**

```
KANHA
	src/
	├── prompts/
	│   ├── __init__.py                               # initializes the prompts package
	│   ├── question_generation/                      # subpackage for question generation prompts
	│   │   ├── __init__.py                           # initializes the subpackage
	│   │   ├── user_prompts.py                       # user input prompts for question generation
	│   │   ├── system_prompts.py                     # system prompts for question generation
	│   ├── answer_evaluation/                        # subpackage for answer evaluation prompts
	│   │   ├── __init__.py                           # initializes the subpackage
	│   │   ├── user_prompts.py                       # user input prompts for answer evaluation
	│   │   ├── system_prompts.py                     # system prompts for answer evaluation
	│   └── prompt_manager.py                         # centralized logic for managing prompts (Factory and logic)
	│
	├── clients/  									  # all client-related modules and subpackages
	│   ├── __init__.py  							  # constructor for the clients package
	│   │
	│   ├── base/  									  # base subpackage under clients
	│   │   ├── __init__.py
	│   │   └── base.py  							  # shared logic for clients like prompt generation
	│   │
	│   ├── bedrock_client/  						  # subpackage for AWS Bedrock-specific client
	│   │   ├── __init__.py
	│   │   ├── bedrock_client.py  					  # main client logic for interacting with Bedrock
	│   │   ├── base/  								  # Bedrock-specific base functionality
	│   │   │   ├── __init__.py
	│   │   │
	│   │   └── strategy/  							  # Bedrock-specific strategies
	│   │       ├── __init__.py
	│   │
	│   ├── openai_client/  						  # OpenAI-specific client
	│   │   ├── __init__.py
	│   │   ├── openai_base/  						  # base OpenAI-related functionality
	│   │   │   ├── __init__.py
	│   │   │   ├── openai_base_client.py  			  # base OpenAI client
	│   │   │   └── openai_strategy.py  			  # strategy implementation for OpenAI
	│   │   │
	│   │   └── strategy/  							  # subpackage for OpenAI-specific strategies
	│   │       ├── __init__.py
	│   │       ├── evaluate_answers_strategy.py      # strategy for evaluating answers
	│   │       └── generate_questions_strategy.py    # strategy for generating questions
	│   │
	│   ├── docs/  									  # documentation for the clients package
	│   │   ├── ClientPackageArchitectureDiagram.png  # architecture diagram
	│   │   └── docs.md  							  # documentation for the client package structure and usage
	│   │
	│   ├── response_examples/   					  # sample response directory
	│   │   ├── evaluate_answers.json   			  # sample response for answer evaluation
	│   │   └── generate_questions.json 			  # sample response for question generation
	│   │
	│   └── tests/  								  # tests for all clients functionality
	│       ├── test_evaluate_answers.py    		  # tests for answer evaluation functionality
	│       └── test_generate_questions.py  		  # tests for question generation functionality
	│
	├── config/                                       # configuration files
	│   ├── aws_config.py                             # AWS configurations (Bedrock, RDS, S3, etc.)
	│   ├── base_config.py                            # base configurations
	│   ├── env_config.py                             # environments configurations
	│   ├── general_config.py                         # general configurations
	│   ├── openai_config.py                          # OpenAI API configurations
	│   └── __init__.py                               # makes config a Python package
	│
	├── framework/                                    # web framework files
	│   ├── __init__.py                               # initializes the framework package
	│   └── bottle_app.py                             # encapsulates Bottle-specific components
	│
	├── repository/                                   # database interaction layer
	│   ├── question_repo.py                          # handles CRUD operations for questions
	│   ├── evaluation_repo.py                        # handles CRUD operations for evaluation results
	│   └── __init__.py                               # makes repository a Python package
	│
	├── routes/                                       # API endpoints (controllers)
	│   ├── question_routes.py                        # routes for question generation
	│   ├── evaluation_routes.py                      # routes for answer evaluation
	│   └── __init__.py                               # makes routes a Python package
	│
	├── services/                                     # business logic layer
	│   ├── question_service/                         # core logic for question generation
	│   │   ├── __init__.py                           # main service logic
	│   ├── evaluation_service/                       # core logic for answer evaluation
	│   │   ├── __init__.py                           # main service logic
	│   ├── validation_manager/                       # Payload validation logic
	│   │   ├── __init__.py                           # main validation logic
	│   └── __init__.py                               # makes services a Python package
	│
	├── utils/                                        # utilities for reusable logic
	│   ├── logging_manager/                          # handles logging for the project
	│   │   ├── __init__.py                           # main logging logic
	│   ├── cache_manager/                            # handles caching for the project
	│   │   ├── __init__.py                           # main cache logic
	│   ├── __init__.py                               # makes utils a Python package
	│   │
	├── main.py                                       # application entry point
	│
	└── start_application.sh                          # bash file to run main entry point

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
