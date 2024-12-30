## **KANHA** – **Kustomized Assessment & NLP-based Hyperpersonalized Audit**

### **Project Structure**

```
KANHA                                  # Root directory of the project
├── cookbook                           # Contains documentation and guides
│   └── version1                       # Version 1 of the cookbook
│       └── index.md                   # Main index file of the cookbook
├── infra                              # Infrastructure related files
│   ├── environments                   # Different environment configurations
│   │   ├── dev                        # Development environment
│   │   │   ├── docker-compose.yml     # Docker Compose file for dev environment
│   │   │   └── Dockerfile             # Dockerfile for dev environment
│   │   ├── prod                       # Production environment
│   │   │   ├── docker-compose.yml     # Docker Compose file for prod environment
│   │   │   └── Dockerfile             # Dockerfile for prod environment
│   │   ├── qa                         # QA environment
│   │   │   ├── docker-compose.yml     # Docker Compose file for QA environment
│   │   │   └── Dockerfile             # Dockerfile for QA environment
│   │   └── stage                      # Staging environment
│   │       ├── docker-compose.yml     # Docker Compose file for stage environment
│   │       └── Dockerfile             # Dockerfile for stage environment
│   └── terraform                      # Terraform configuration files
│       ├── lambda_code                # Lambda-related code and Terraform files
│       │   ├── app.py                 # Lambda function code
│       │   ├── main.tf                # Terraform main configuration for lambda
│       │   ├── outputs.tf             # Terraform outputs for lambda
│       │   ├── provider.tf            # Terraform provider configuration for lambda
│       │   ├── requirements.txt       # Python requirements for lambda
│       │   ├── terraform.tfstate      # Terraform state file for lambda
│       │   └── variables.tf           # Terraform variables for lambda
│       ├── main.tf                    # Terraform main configuration
│       ├── outputs.tf                 # Terraform outputs
│       ├── provider.tf                # Terraform provider configuration
│       ├── terraform.tfstate          # Terraform state file
│       └── variables.tf               # Terraform variables
├── LICENSE                            # License file for the project
├── Makefile                           # Makefile for build automation
├── poetry.lock                        # Poetry lock file for package dependencies
├── pyproject.toml                     # Poetry project configuration
├── README.md                          # Main README file of the project
├── release                            # Folder for release-related assets
├── requirements.txt                   # Python dependencies
├── setup.py                           # Setup script for the project
├── app                                # Application code of the project
│   ├── dao                            # Data Access Object, to handle database operations
│   │   ├── base
│   │   │   ├── base_dao.py
│   │   │   └── __init__.py
│   │   ├── feedback
│   │   │   ├── feedback_dao.py
│   │   │   └── __init__.py
│   │   ├── helpers
│   │   │   ├── db_helpers.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── test_base_dao.py
│   │   │   ├── test_feedback_dao.py
│   │   │   └── test_user_dao.py
│   │   └── user
│   │       ├── __init__.py
│   │       └── user_dao.py
│   ├── clients                        # Client-related code
│   │   ├── base.py                    # Base class for clients
│   │   ├── client_types               # Different types of clients
│   │   │   ├── bedrock_client.py      # Bedrock client implementation
│   │   │   ├── __init__.py            # Initialization of client_types
│   │   │   └── openai_client.py       # OpenAI client implementation
│   │   ├── docs                       # Documentation for clients
│   │   │   ├── ClientPackageArchitectureDiagram.png  # Client architecture diagram
│   │   │   └── docs.md                # Documentation file
│   │   ├── factory.py                 # Factory to instantiate clients
│   │   ├── __init__.py                # Initialization of the clients package
│   │   ├── payload                    # Payloads for requests and responses
│   │   │   ├── request_examples       # Example request payloads
│   │   │   │   ├── evaluate_answers.json  # Example for evaluate_answers
│   │   │   │   └── generate_questions.json  # Example for generate_questions
│   │   │   └── response_examples      # Example response payloads
│   │   │       ├── evaluate_answers.json  # Example response for evaluate_answers
│   │   │       └── generate_questions.json  # Example response for generate_questions
│   │   ├── tests                      # Unit tests for clients
│   │   │   ├── test_evaluate_answers.py  # Test for evaluate_answers
│   │   │   └── test_generate_questions.py  # Test for generate_questions
│   │   └── utils.py                   # Utility functions for clients
│   ├── config                         # Configuration files
│   │   ├── aws_config.py              # AWS-specific configurations
│   │   ├── base_config.py             # Base configuration for the project
│   │   ├── env_config.py              # Environment-specific configurations
│   │   ├── general_config.py          # General project configuration
│   │   ├── __init__.py                # Initialization of config package
│   │   └── openai_config.py           # OpenAI-specific configurations
│   ├── framework                      # Core framework code
│   │   ├── bottle_app.py              # Bottle framework app
│   │   └── __init__.py                # Initialization of framework package
│   ├── main.py                        # Main entry point of the application
│   ├── prompts                        # Prompt-related files
│   │   ├── answer_evaluation          # Prompts for answer evaluation
│   │   │   ├── __init__.py            # Initialization of answer_evaluation
│   │   │   ├── system_prompts.py      # System prompts for evaluation
│   │   │   └── user_prompts.py        # User prompts for evaluation
│   │   ├── factory                    # Factory for creating prompts
│   │   │   ├── answer_evaluation_prompt.py  # Prompt for answer evaluation
│   │   │   ├── base_prompt.py         # Base class for prompts
│   │   │   ├── __init__.py            # Initialization of factory package
│   │   │   ├── prompt_factory.py      # Prompt factory logic
│   │   │   └── question_generation_prompt.py  # Prompt for question generation
│   │   ├── __init__.py                # Initialization of prompts package
│   │   ├── question_generation        # Prompts for question generation
│   │   │   ├── __init__.py            # Initialization of question_generation
│   │   │   ├── system_prompts.py      # System prompts for question generation
│   │   │   └── user_prompts.py        # User prompts for question generation
│   │   └── tests                      # Unit tests for prompts
│   │       ├── test_answer_evaluation_prompt.py  # Test for answer evaluation prompts
│   │       └── test_question_generation_prompt.py  # Test for question generation prompts
│   ├── repository                     # Data repositories for questions and evaluations
│   │   ├── evaluation_repo.py         # Repository for evaluations
│   │   ├── __init__.py                # Initialization of repository package
│   │   └── question_repo.py           # Repository for questions
│   ├── routes                         # Routes for the API
│   │   ├── cache_route.py             # Route for cache management
│   │   ├── constants.py               # Constants used across the routes
│   │   ├── evaluation_route.py        # Route for evaluations
│   │   ├── healthcheck_route.py       # Route for health checks
│   │   ├── __init__.py                # Initialization of routes package
│   │   └── question_route.py          # Route for questions
│   ├── services                       # Core services of the platform
│   │   ├── __init__.py                # Initialization of services package
│   │   ├── service_types              # Types of services (e.g., evaluation, question)
│   │   │   ├── evaluation_service.py  # Evaluation service logic
│   │   │   ├── __init__.py            # Initialization of service_types
│   │   │   └── question_service.py    # Question service logic
│   │   ├── tests                      # Unit tests for services
│   │   │   ├── test_evaluation_service.py  # Test for evaluation service
│   │   │   └── test_question_service.py    # Test for question service
│   │   └── validation_manager         # Validation logic for request/response
│   │       ├── __init__.py            # Initialization of validation_manager
│   │       ├── schema_map.py          # Schema mapping for validation
│   │       ├── strategy               # Validation strategies for payloads
│   │       │   ├── base.py            # Base strategy for validation
│   │       │   ├── evaluate_answers_request_payload.py  # Validation for evaluate_answers request
│   │       │   ├── evaluate_answers_response_payload.py  # Validation for evaluate_answers response
│   │       │   ├── generate_questions_request_payload.py  # Validation for generate_questions request
│   │       │   ├── generate_questions_response_payload.py  # Validation for generate_questions response
│   │       │   └── __init__.py        # Initialization of strategy package
│   │       ├── tests.py               # Tests for validation manager
│   │       └── validation_manager.py  # Main validation logic
│   └── utils                          # Utility functions
│       ├── cache                      # Cache management utilities
│       │   ├── __init__.py            # Initialization of cache utilities
│       │   └── manager.py             # Cache manager logic
│       ├── __init__.py                # Initialization of utils package
│       ├── logging                    # Logging utilities
│       │   ├── base.py                # Base logging utilities
│       │   ├── filters.py             # Log filters
│       │   ├── formatters.py          # Log formatters
│       │   ├── handlers.py            # Log handlers
│       │   └── __init__.py            # Initialization of logging utilities
│       └── response_manager           # Response management utilities
│           ├── __init__.py            # Initialization of response manager
│           └── response_manager.py    # Main response manager logic
└── entrypoint.sh                      # Shell script for entry point of the application

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

### Setup Database

#### Step 1: Configure Database Connection

1.  Open the `alembic.ini` file in the project directory and set the **SQLAlchemy database URL**:

    ```ini
    sqlalchemy.url = postgresql://postgres:pgpass@localhost:5432/kanha

    ```

    Replace the following values:

    - **postgres**: Your PostgreSQL username.
    - **pgpass**: Your PostgreSQL password.
    - **localhost**: The host where PostgreSQL is running (use `localhost` if it's on your local machine).
    - **5432**: The default PostgreSQL port (use another port if applicable).
    - **kanha**: Your PostgreSQL database name.

---

#### Step 2: Set Up Alembic and Migrations

1.  **Initialize Alembic** (if you haven’t initialized Alembic already):

    ```bash
    alembic init alembic

    ```

    This will create the necessary `alembic.ini` file and the `alembic/` directory structure for managing migrations.

2.  **Ensure All Models Are Registered**:  
    Alembic uses SQLAlchemy’s metadata to detect table changes. Make sure all models (like `Feedback`, `MultipleChoiceQuestion`, `ProblemSolvingQuestion`) are imported in the `env.py` file inside the `alembic/` folder.

    - Open `alembic/env.py` and import your models at the top:

      ```python
      from app.dao.models import BaseModel, Feedback, MultipleChoiceQuestion, ProblemSolvingQuestion

      ```

    - Ensure `target_metadata` is set to the base metadata:

      ```python
      target_metadata = BaseModel.metadata  # or Base.metadata if using a different base class

      ```

---

#### Step 3: Create and Apply Migrations

1.  **Generate Migration Script**:

    Run the following command to generate a new migration script. This will detect changes in your models and create the corresponding migration:

    ```bash
    alembic revision --autogenerate -m "Initial migration to create tables"

    ```

    - Alembic will compare your models to the current state of the database and generate the necessary SQL to create the tables.
    - The migration script will be saved in the `alembic/versions/` directory.

2.  **Review the Migration Script**:

    - Navigate to `alembic/versions/` and open the generated migration script.
    - Make sure that all the tables (`feedback`, `multiple_choice_question`, `problem_solving_questions`) are being created as per your models.
    - If everything looks correct, you can apply the migration.

3.  **Apply the Migration**:

    Run the following command to apply the migration and create the tables in your database:

    ```bash
    alembic upgrade head

    ```

    - This command will apply the migration and create the necessary tables in your PostgreSQL database.

---

#### Step 4: Verify the Database

Once the migration has been applied, you can verify the database schema using PostgreSQL commands:

1.  Connect to your PostgreSQL database:

    ```bash
    psql -U postgres -d kanha

    ```

2.  Check the tables in the database:

    ```sql
    \d feedback;
    \d multiple_choice_question;
    \d problem_solving_questions;

    ```

    - The above commands will show the details of the `feedback`, `multiple_choice_question`, and `problem_solving_questions` tables.

---

#### Step 5: Adding Future Migrations

If you modify your models (e.g., adding new fields or tables), you can regenerate a new migration file by running:

```bash
alembic revision --autogenerate -m "Added new fields to feedback model"

```

Then, apply the new migration using:

```bash
alembic upgrade head

```

This will update the database schema to reflect the new changes.

---

## Troubleshooting

- **Error: Can't load plugin: sqlalchemy.dialects:driver**  
  This error occurs if the database URL is incorrectly configured in the `alembic.ini` file. Make sure your connection URL is correct (e.g., `postgresql://postgres:pgpass@localhost:5432/kanha`).
- **Error: Missing Target Metadata in `env.py`**  
  Ensure that you’ve imported all models in `env.py` and that the `target_metadata` points to your `Base.metadata`:

  ```python
  target_metadata = BaseModel.metadata  # or Base.metadata

  ```

- **Error: Type Annotation for "id" can't be correctly interpreted**  
  This occurs if you're using a type annotation format incompatible with SQLAlchemy's ORM. In such cases, use `Mapped[]` instead of regular type annotations for mapped fields. For example:

  ```python
  id: Mapped[UUID] = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

  ```

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
