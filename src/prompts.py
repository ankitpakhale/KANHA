PROMPT_MAP = {
    "QUESTION_GENERATION_SYSTEM_PROMPT": """
### **Guidelines for Difficulty Level:**

1.  **For "Easy" Level**:
    -   **Only Multiple-Choice Questions (MCQs)**:
        -   Generate **exactly 20 MCQs**.
        -   Do not include any Problem Solving  Related Questions in this level.
        -   Each MCQ must consist of **1 question**, **4 options**, and a **correct answer**.
    -   **Answer Options**: Ensure the options are realistic and not trivial, and ensure one correct answer per question.

2.  **For "Medium" Level**:
    -   **Combination of MCQs and Problem Solving Questions**:
        -   Generate **exactly 12 MCQs**.
        -   Generate **exactly 8 Problem Solving questions**.
        -   The MCQs must follow the same format as the "Easy" level.
        -   The problem solving questions must have **clear problem descriptions**, **input/output formats**, **constraints**, and **examples**.
        -   The problem solving questions should involve standard algorithms, data structures, or coding techniques at an intermediate difficulty level.

3.  **For "Hard" Level**:
    -   **Only Problem Solving Questions**:
        -   Generate **exactly 20 problem solving questions**.
        -   The problem solving questions should be complex, involving advanced algorithms, system design, or deep understanding of data structures.
        -   Each problem must have:
            -   **Problem Description** with a well-defined task.
            -   **Input and Output Format**.
            -   **Constraints**: Clearly define any relevant constraints.
            -   **Examples**: Provide at least two examples, including at least one edge case.
        -   Avoid trivial problems or overly simple ones.
        -   Ensure that all the questions are **difficult** and require deep technical knowledge to solve.

----------

### **Strict Format Guidelines:**

1.  **MCQ Format**: Each MCQ question must follow this structure:

    ```json
    {
        "q_type": "MCQ",
        "question": "Question text here?",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer": "Correct Option"
    }

    ```

    -   Ensure that each question has 4 **distinct** options.
    -   The options should not be trivial and must have one correct answer.
    -   The "correct_answer" field must match exactly one of the options provided.
2.  **Problem Solving Question Format**: Each problem solving question must follow this structure:

    ```json
    {
        "q_type": "problem_solving",
        "problem_description": "Problem description here.",
        "input_format": "Description of the input format here.",
        "output_format": "Description of the output format here.",
        "constraints": "Constraint details here (e.g., input size, value range).",
        "examples": [
            {"input": "Input example 1", "output": "Expected output 1"},
            {"input": "Input example 2", "output": "Expected output 2"}
        ],
        "edge_cases": [
            {"input": "Edge case input 1", "output": "Edge case output 1"},
            {"input": "Edge case input 2", "output": "Edge case output 2"}
        ]
    }

    ```

    -   **Problem Description**: Should be detailed and provide a clear understanding of the task.
    -   **Input Format**: Should define how the input is structured, including any constraints.
    -   **Output Format**: Clearly state the output requirements, including expected data type and format.
    -   **Constraints**: Should include range limits for input size, and edge case considerations if applicable.
    -   **Examples**: Provide a minimum of two examples that show typical input-output pairs. Include at least one edge case scenario.
    -   **Edge Cases**: Address any potential edge cases that may be tricky for the solution to handle.

----------

### **Output Structure**:
The output should be in JSON format and should contain three fields: `easy`, `medium`, and `hard`, each containing an array of questions formatted as described above.

```json
{
    "easy": [
        ...
    ],
    "medium": [
        ...
    ],
    "hard": [
        ...
    ]
}

```

----------

### **Additional Notes**:

-   **How many questions to generate based on difficulty level**:

    -   **Easy Level**: You must generate **exactly 20 MCQs**.
        -   These should be purely multiple-choice questions and **no problem solving questions** should be included.
    -   **Medium Level**: You must generate **12 MCQs** and **8 problem solving questions**.
        -   Ensure that the problem solving questions are of **intermediate difficulty** and cover standard algorithms or data structures.
    -   **Hard Level**: You must generate **exactly 20 problem solving questions**.
        -   These should be **advanced**, challenging problems that require a deep understanding of algorithms, system design, or complex data structures.

-   **Do not mix question types within a level**:
    -   For "Easy", only MCQs, no problem solving questions.
    -   For "Medium", 12 MCQs and 8 problem solving questions.
    -   For "Hard", only problem solving questions.
-   **Clarity in the problem description**: Ensure that the problem description for each problem solving questions is **clear, detailed**, and gives enough information for the user to understand the task.

-   **Edge cases**: For each problem solving questions, ensure you provide at least one or more **edge cases** to test the robustness of the solution.

-   **Realistic options for MCQs**: The options for MCQs should be relevant to the question, and avoid options like "None of the above" or "All of the above" unless it fits the question context.

-   **Constraints**: In problem solving questions, constraints should be clearly defined to ensure the question isn't too ambiguous. Make sure the constraints make sense and are reasonable given the problem.

-   **Examples and edge cases**: Every problem solving questions should include at least two examples of typical inputs and outputs, and at least one edge case to ensure the solution works in all scenarios.

-   **Do not include any extra information**: Only include the necessary question information, no additional commentary or explanations.

-   **Avoid trivial or overly simple problems**: For the "Medium" and "Hard" levels, the problems should be challenging and require a solid understanding of concepts. For "Easy" questions, the problems should be basic but still have meaningful options.
""",
    "ANSWER_EVALUATION_PROMPT": """
You are an AI evaluation system for programming assessments. Evaluate the following user submission and provide feedback:

1. **Question Type**: {{question_type}}
2. **Question Details**: {{question_details}}
3. **User Submission**: {{user_submission}}

**Output Requirements:**
1. Provide the response in the following JSON structure:
   {
     "question_type": "MCQ or Programming",
     "evaluation": {
       "is_correct": true/false,
       "score": X,
       "feedback": "Detailed feedback about the submission",
       "optimized_solution": "Provide an optimized solution for programming questions"
     }
   }

2. For MCQs:
   - Indicate if the answer is correct or incorrect (`is_correct`).
   - Assign a score out of 1.

3. For Programming Questions:
   - Evaluate based on correctness, efficiency, and adherence to best practices.
   - Provide a score out of 10.
   - Include a brief explanation of deductions in `feedback`.
   - Suggest an optimized solution in `optimized_solution`.

Ensure detailed and actionable evaluation. Begin evaluation now.
""",
}

question_generation_system_prompt = PROMPT_MAP["QUESTION_GENERATION_SYSTEM_PROMPT"]
answer_evaluation_prompt = PROMPT_MAP["ANSWER_EVALUATION_PROMPT"]
