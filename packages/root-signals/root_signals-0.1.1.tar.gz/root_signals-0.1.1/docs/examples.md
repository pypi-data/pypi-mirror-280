# SDK features using concrete examples #

These examples walk through some features of the platform in a bit more detail.

## Minimal skill

This is the same as the quickstart one, except on multiple lines for readability. The APIs typically respond with Python objects, which can be used to chain requests or alternatively reuse previous calls' results.

```{literalinclude} ../examples/minimal.py
```

## Simple skill

The simple skill example adds some more metadata to the skill, but is otherwise similar to minimal one. It specifies explicitly the model to use, as well as descriptive intent and input variables that are referred to in the prompt.

```{literalinclude} ../examples/simple.py
```

## Skill with a data loader

In this example, we add a data loader which loads the contents of a reference variable called kimchi_ingredients from Wikipedia, and then uses that to populate the prompt.

```{literalinclude} ../examples/data_loader.py
```

## Skill with a validator

If we want to validate results of skill execution, we can add a validator. In this example, we add validator which scores the results by relevance of the answer to the input prompt, and if it is less than threshold of 0.9, fails the skill execution.

```{literalinclude} ../examples/validator.py
```

The validation results can be retrieved from the execution logs for analysis and audit.

```{literalinclude} ../examples/execution_logs.py
```

## Evaluator skill and minimal version of it

We can also create an evaluator skill. Evaluator skills return only floating point values between 0 and 1, based on how well the received output (of a skill) matches what the evaluator is described to look for.

```{literalinclude} ../examples/evaluator_skill.py
```

The evaluator skill can be also created implicitly by supplying evaluator_name and a prompt:

```{literalinclude} ../examples/evaluator_skill_minimal.py
```


## Chat with a skill

Beyond single request-response model, it is also possible to start a chat session with a skill, with the Root Signals system taking care of remembering the history of the conversation.

```{literalinclude} ../examples/chat.py
```

## Use Retrieval Augmented Generation (RAG) evaluator

It is also possible to use RAG evaluators, which have extra data for evaluating the input.

```{literalinclude} ../examples/run_rag.py
```

## Use OpenAI client for chat completions

It is also possible to retrieve `base_url` from Root Signals SDK Skill, and then use the normal `openai` API client with it. There are two ways to do it:

Without streaming, the API returns whole response to the call:

```{literalinclude} ../examples/chat_openai.py
```

Do note that only models specified as either `model` or
`fallback_models` to the created Skill are accepted by the API. Trying
to use other model names will result in an error.

When streaming (`stream=True`), the API response will be provided as a generator which will provide a set of chunks over time:chunks :

```{literalinclude} ../examples/chat_openai_2.py
```

Do note that if validators are in use, it is not possible to stream the response as the response must be validated before returning it to the caller. In that case (and possibly for other reasons too), the platform will just return the final full response after validators are done evaluating it as a single chunk.
