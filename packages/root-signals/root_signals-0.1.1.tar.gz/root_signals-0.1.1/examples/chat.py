from root import RootSignals

# Connect to the Root Signals API
client = RootSignals()

skill = client.skills.create(
    name="My chatbot",
    intent="Simple Q&A chatbot",
    prompt="Answer me questions in markdown format. {{question}}",
    input_variables=[{"name": "question"}],
    model="gpt-4",
)

# Start chatting with the skill
chat = client.skills.create_chat(skill_id=skill.id)

first_response = chat.run(variables={"question": "List the states in the US"})
print(first_response.llm_output)
# Sure, here it is:
#
# 1. Alabama
# 2. Alaska
# ...
# 50. Wyoming

question = "Which of those states have a population of more than 2 million?"

second_response = chat.run(variables={"question": question})
print(second_response.llm_output)
# According to the U.S. Census Bureau's estimates as of 2020,
# these are the U.S. states with a population of more than 2 million:
#
# 1. Alabama
# 2. Arizona
# ..
# 35. Wisconsin
