![PyPI - Version](https://img.shields.io/pypi/v/dverse-agent-python)
![Known Vulnerabilities](https://snyk.io/test/github/fuas-dverse/dverse-agent-python/badge.svg)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=fuas-dverse_dverse-agent-python&metric=bugs)](https://sonarcloud.io/summary/new_code?id=fuas-dverse_dverse-agent-python)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=fuas-dverse_dverse-agent-python&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=fuas-dverse_dverse-agent-python)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=fuas-dverse_dverse-agent-python&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=fuas-dverse_dverse-agent-python)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=fuas-dverse_dverse-agent-python&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=fuas-dverse_dverse-agent-python)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=fuas-dverse_dverse-agent-python&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=fuas-dverse_dverse-agent-python)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=fuas-dverse_dverse-agent-python&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fuas-dverse_dverse-agent-python)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=fuas-dverse_dverse-agent-python&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=fuas-dverse_dverse-agent-python)

# Dverse Agent Python
As part of the Dverse application, we as a team decided to create a Python package that can be installed by developers who want to contribute to our network of agents.

This package helps developers that want to create their own agent, by taking care of the basics.

___
## Dverse (project explanation)
The goal of the Dverse application, is to create a system where a user, with a specific task or question in mind, can prompt our system to complete this task or answer the question.

For example, I as a user want to book a trip to Spain this summer. The prompt I will ask the system could look something like: “Coming summer I want to book a trip to Spain”. You could imagine that to complete this task, there are a couple of smaller steps involved like, selecting the right date, booking a hotel or appartement, booking flight tickets, etc. To complete the user's prompt, these smaller steps (agents) have to work together to achieve the bigger question.

We as a group created a solution that makes this possible. We combined things like NLP, LLM, vector databases etc., to achieve a collaborating system of agents.

___
## Installation
To use our package, it is quite simple as we have deployed this agent to PyPi. We recommend using a virtual environment, as this is the recommended way to configure a Python project.

Set up a virtual environment:
```terminal
python -m venv venv
```

Activate virtual environment on Windows:
```terminal
./.venv/Scripts/active
```

Activate virtual environment on Mac:
```terminal
source ./venv/bin/activate
```

Install the package via pip by running:
```terminal
pip install dverse-agent-python
```

___
## Usage
To use our package, you just simply import the `Agent` class from our package and initialize it with some required parameters.

<table style="width: 100%">
<tr>
<th>
<p>
Parameter
</p>
</th>
<th>
<p>
Description
</p>
</th>
</tr>
<tr>
<td>
name
</td>
<td>
The name of the Agent. <br/>(example: Hotel Information Agent, Flights Booking Agent)
</td>
</tr>
<tr>
<td>
description
</td>
<td>
The description of the Agent. <br/>(example: Agent provides information about hotels in a certain area)
</td>
</tr>
<tr>
<td>
topics
</td>
<td>
Array of topics / keywords used to get the agents based on a matching intent. <br/>(example: ["hotel", "accommodation", "hotel-information"])
</td>
</tr>
<tr>
<td>
output_format
</td>
<td>
The format the agent sends a result back <br/>(example: image, JSON, text etc.)
</td>
</tr>
<tr>
<td>
callback
</td>
<td>
The function that gets triggered when an agent received a message.
</td>
</tr>
</table>


Example:
```python
# Import the Agent class from dverse-agent-python package
from agentDVerse import Agent


def callback(x):
    # Get the user's question from the JSON-object
    user_question = x.get("content")[0].get("message")

    # Call self created function here
    result = self_created_function(message)

    # Return the initial object and generated result
    # This will pass it to the next agent or back to the UI
    agent.send_response_to_next(
        initial=x,
        message={
            "message": result
        }
    )

if __name__ == "__main__":
    # Initialize the agent class with required parameters.
    agent = Agent(
        name="Hotel Information Agent",
        description="Agent provides information about hotels",
        topics=["hotel", "accommodation", "hotel-information"],
        output_format="json",
        callback=callback
    )
```

