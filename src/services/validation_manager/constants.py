SCHEMA_MAP = {
    "GENERATE_QUESTIONS": {
        "REQUEST_SCHEMA": {
            "type": "object",
            "properties": {
                "difficulty_level": {"type": "string"},
                "programming_language": {"type": "string"},
                "topics": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["difficulty_level", "programming_language", "topics"],
            "additionalProperties": False,
        },
        "RESPONSE_SCHEMA": {
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
        "REQUEST_SCHEMA": {
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
        "RESPONSE_SCHEMA": {
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
}
