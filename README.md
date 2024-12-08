## **KANHA** – **Kustomized Assessment & NLP-based Hyperpersonalized Assessments**

### **Project Structure**

```
KANHA
	src/
	├── prompts/
	│   ├── __init__.py                           # Initializes the prompts package
	│   ├── question_generation/                  # Subpackage for question generation prompts
	│   │   ├── __init__.py                       # Initializes the subpackage
	│   │   ├── user_prompts.py                   # User input prompts for question generation
	│   │   ├── system_prompts.py                 # System prompts for question generation
	│   ├── answer_evaluation/                    # Subpackage for answer evaluation prompts
	│   │   ├── __init__.py                       # Initializes the subpackage
	│   │   ├── user_prompts.py                   # User input prompts for answer evaluation
	│   │   ├── system_prompts.py                 # System prompts for answer evaluation
	│   └── prompt_manager.py                     # Centralized logic for managing prompts (Factory and logic)
	│
	├── clients/                                  # Clients for external APIs
	│   ├── bedrock_client/                       # Bedrock package (question generation + evaluation)
	│   │	├── __init__.py                       # Bedrock constructor
	│   │	├── base.py                   		  # Bedrock base clients
	│	│   └── bedrock_client.py                 # Bedrock client for question generation + evaluation
	│   │
	│   ├── openai_client/                        # OpenAI package (question generation + evaluation)
	│   │	├── __init__.py                       # OpenAI constructor
	│   │	├── base.py                           # OpenAI base clients
	│	│   └── openai_client.py                  # OpenAI client for question generation + evaluation
	│   │
	├── clients/                                  # Clients for external APIs
	│   ├── openai_client.py                      # Handles OpenAI API calls (question generation + evaluation)
	│   ├── bedrock_client.py                     # Handles Bedrock API calls (question generation + evaluation)
	│   └── __init__.py                           # Makes clients a Python package
	│
	├── config/                                   # Configuration files
	│   ├── aws_config.py                         # AWS configurations (Bedrock, RDS, S3, etc.)
	│   ├── base_config.py                        # Base configurations
	│   ├── env_config.py                         # Environments configurations
	│   ├── general_config.py                     # General configurations
	│   ├── openai_config.py                      # OpenAI API configurations
	│   └── __init__.py                           # Makes config a Python package
	│
	├── framework/                                # Web framework files
	│   ├── __init__.py                           # Initializes the framework package
	│   └── bottle_app.py                         # Encapsulates Bottle-specific components
	│
	├── repository/                               # Database interaction layer
	│   ├── question_repo.py                      # Handles CRUD operations for questions
	│   ├── evaluation_repo.py                    # Handles CRUD operations for evaluation results
	│   └── __init__.py                           # Makes repository a Python package
	│
	├── routes/                                   # API endpoints (controllers)
	│   ├── question_routes.py                    # Routes for question generation
	│   ├── evaluation_routes.py                  # Routes for answer evaluation
	│   └── __init__.py                           # Makes routes a Python package
	│
	├── services/                                 # Business logic layer
	│   ├── question_service/                     # Core logic for question generation
	│   │   ├── __init__.py                       # Main service logic
	│   ├── evaluation_service/                   # Core logic for answer evaluation
	│   │   ├── __init__.py                       # Main service logic
	│   ├── validation_manager/                   # Payload validation logic
	│   │   ├── __init__.py                       # Main validation logic
	│   └── __init__.py                           # Makes services a Python package
	│
	├── utils/                                    # Utilities for reusable logic
	│   ├── logging_manager/                      # Handles logging for the project
	│   │   ├── __init__.py                       # Main logging logic
	│   ├── cache_manager/                        # Handles caching for the project
	│   │   ├── __init__.py                       # Main cache logic
	│   ├── __init__.py                           # Makes utils a Python package
	│   │
	├── main.py                                   # Application entry point
	│
	└── start_application.sh                      # Bash file to run main entry point

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

**KANHA** is a powerful, AI-driven assessment platform designed to provide tailored learning and evaluation experiences. Its two key services—question generation and answer evaluation—are hosted on AWS Lambda for scalability and efficiency. By integrating advanced NLP capabilities with a distributed architecture, KANHA ensures personalized, meaningful assessments that promote skill improvement and engagement. Its robust technology stack and scalable design make it a versatile solution for education, training, and recruitment.
