SCHEMA_MAP = {
    "GENERATE_QUESTIONS": {
        "REQUEST": {
            "type": "object",
            "properties": {
                "num_questions": {"type": "integer"},
                "difficulty_level": {"type": "string"},
                "programming_language": {"type": "string"},
                "topics": {"type": "string"},
            },
            "required": ["difficulty_level", "programming_language", "topics"],
            "additionalProperties": False,
        },
        "MCQ_RESPONSE": {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "problem_description": {"type": "string"},
                "options": {"type": "array", "items": {"type": "string"}},
                "correct_answer": {"type": "string"},
                "required_time": {"type": ["string", "number"]},
            },
            "required": [
                "problem_description",
                "options",
                "correct_answer",
                "required_time",
            ],
            "additionalProperties": False,
        },
        "PSQ_RESPONSE": {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "problem_description": {"type": "string"},
                "input_format": {"type": "string"},
                "output_format": {"type": "string"},
                "constraints": {"type": "string"},
                "examples": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "input": {"type": "string"},
                            "output": {"type": "string"},
                        },
                        "required": ["input", "output"],
                    },
                },
                "edge_cases": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "input": {"type": "string"},
                            "output": {"type": "string"},
                        },
                        "required": ["input", "output"],
                    },
                },
                "required_time": {"type": ["string", "number"]},
            },
            "required": ["problem_description", "required_time"],
        },
    },
    "EVALUATE_ANSWERS": {
        "REQUEST": {
            "type": "array",  # the root is an array
            "items": {
                "type": "object",  # each item in the array is an object
                "properties": {
                    "q_id": {
                        "type": "string",  # q_id should be a string
                        # simple alphanumeric validation for q_id
                        "pattern": "^[a-zA-Z0-9]+$",
                    },
                    "problem_description": {
                        "type": "string"  # problem_description should be a string
                    },
                    "input_format": {
                        "type": "string"  # input_format should be a string
                    },
                    "output_format": {
                        "type": "string"  # output_format should be a string
                    },
                    "constraints": {"type": "string"},  # constraints should be a string
                    "examples": {
                        "type": "array",  # examples should be an array
                        "items": {
                            "type": "object",  # Each example is an object
                            "properties": {
                                "input": {
                                    "type": "string"  # input for example should be a string
                                },
                                "output": {
                                    "type": "string"  # output for example should be a string
                                },
                            },
                            # both input and output are required in examples
                            "required": ["input", "output"],
                        },
                    },
                    "edge_cases": {
                        "type": "array",  # edge_cases should be an array
                        "items": {
                            "type": "object",  # Each edge case is an object
                            "properties": {
                                "input": {
                                    "type": "string"  # input for edge case should be a string
                                },
                                "output": {
                                    "type": "string"  # output for edge case should be a string
                                },
                            },
                            # both input and output are required in edge cases
                            "required": ["input", "output"],
                        },
                    },
                    "userCode": {
                        # userCode should be a string (a Python code block)
                        "type": "string"
                    },
                },
                "required": [
                    "q_id",
                    "problem_description",
                    "input_format",
                    "output_format",
                    "constraints",
                    "examples",
                    "edge_cases",
                    "userCode",
                ],  # all fields are required
            },
        },
        "RESPONSE": {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "q_id": {"type": "string", "pattern": "^[a-zA-Z0-9]+$"},
                    "feedback": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "correctness": {"type": "string"},
                                "areas_for_improvement": {"type": "string"},
                                "strengths": {"type": "string"},
                            },
                            "additionalProperties": False,
                            "anyOf": [
                                {"required": ["correctness"]},
                                {"required": ["areas_for_improvement"]},
                                {"required": ["strengths"]},
                            ],
                        },
                    },
                    "points": {"type": "string", "pattern": "^[0-9]+$"},
                },
                "required": ["q_id", "feedback", "points"],
                "additionalProperties": False,
            },
        },
    },
    "FEEDBACK": {
        "REQUEST": {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "rating": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 10,
                    "description": "Rating from 1 to 10, where 10 is extremely good and 1 is bad",
                },
                "comments": {
                    "type": "string",
                    "description": "Feedback about KANHA",
                },
                "frequency_of_use": {
                    "type": "string",
                    "enum": [
                        "daily",
                        "several_times_a_week",
                        "once_a_week",
                        "several_times_a_month",
                        "once_a_month",
                        "less_than_once_a_month",
                        "first_time",
                    ],
                    "description": "Frequency of use",
                },
                "purpose_of_use": {
                    "type": "string",
                    "description": "The primary purpose for using the product",
                },
                "ease_of_use": {
                    "type": "string",
                    "enum": [
                        "very_easy",
                        "easy",
                        "neutral",
                        "difficult",
                        "very_difficult",
                    ],
                    "description": "Ease of use rating",
                },
                "specific_features": {
                    "type": "string",
                    "description": "Specific features the user wants to highlight",
                },
            },
            "required": ["rating"],
        },
    },
    "CONTACT": {
        "REQUEST": {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "full_name": {
                    "type": "string",
                    "description": "The full name of the user",
                },
                "email": {
                    "type": "string",
                    "format": "email",
                    "description": "The email address of the user",
                },
                "phone": {
                    "type": "string",
                    "description": "The phone number of the user",
                },
                "subject": {
                    "type": "string",
                    "description": "The subject of the message",
                },
                "message": {
                    "type": "string",
                    "description": "The content of the message",
                },
            },
            "required": ["full_name", "message"],
        },
    },
}
