# Documentation for KANHA

- Test all the APIs of project KANHA

```bash
bash start_application.sh
```

- Open terminal and hit below command

```bash
curl -X POST -F "difficulty_level=easy" -F "programming_language=Python" -F "topics=loops, functions" http://localhost:8080/generate-questions
```
