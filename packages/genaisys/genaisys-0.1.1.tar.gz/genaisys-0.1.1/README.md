# GenAISys

This is a meta project where we play with various prompts to llm and save their results with some tinking and document the evolution of llms to automate tasks that would take several hours otherwise.

### Development

    VSCode Settings :     "python.poetryPath": "/opt/homebrew/bin/poetry",
    

### Running Tests

    poetry install # this will install the package locally

    poetry run pytest # this will run all the tests

### Publishing

This is a poerty project and we are publishing the project to pypi.Make sure you have your pypi token or copy from your .pypirc file. Set the following before running poetry publish

    poetry config pypi-token <paste_pypi_token_here>

