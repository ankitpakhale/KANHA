SCHEMA_MAP = {
    "GENERATE_QUESTIONS": {
        "REQUEST": {
            "type": "object",
            "properties": {
                "difficulty_level": {"type": "string"},
                "programming_language": {"type": "string"},
                "topics": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["difficulty_level", "programming_language", "topics"],
            "additionalProperties": False,
        },
        "RESPONSE": {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "q_id": {"type": "string", "pattern": "^mcq[0-9]+$"},
                    "question": {"type": "string"},
                    "options": {
                        "type": "array",
                        "items": {"type": "string"},
                        "minItems": 2,
                        "uniqueItems": True,
                    },
                    "correct_answer": {"type": "string"},
                },
                "required": ["q_id", "question", "options", "correct_answer"],
                "additionalProperties": False,
            },
        },
    },
    "EVALUATE_ANSWERS": {
        "REQUEST": {
            "type": "object",
            "properties": {
                "user_code": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "q_id": {"type": "string"},
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
                            "user_code": {"type": "string"},
                        },
                        "required": [
                            "q_id",
                            "problem_description",
                            "input_format",
                            "output_format",
                            "constraints",
                            "examples",
                            "edge_cases",
                            "user_code",
                        ],
                    },
                }
            },
            "required": ["user_code"],
            "additionalProperties": False,
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
                    "description": "Feedback or comments about the product",
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
}
