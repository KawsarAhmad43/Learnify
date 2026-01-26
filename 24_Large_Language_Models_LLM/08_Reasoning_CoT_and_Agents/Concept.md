# Reasoning and Agents

## 1. Chain of Thought (CoT)
Ask an LLM: "What is 123 * 456?".
*   **Direct Answer**: "random number" (It guesses, because it has to output the last digit before calculating the carry).
*   **CoT**: "Let's think step by step. 3*6=18, carry the 1..." (It uses the context window as scratchpad memory).
*   **DeepSeek R1 / OpenAI o1**: Models trained specifically to generate long CoT traces before determining the final answer. "System 2 Thinking".

## 2. ReAct (Reason + Act)
LLMs are stuck in a text box. Agents give them hands.
*   **Loop**:
    1.  **Thought**: "I need to check the weather."
    2.  **Action**: `call_tool("get_weather", "New York")`
    3.  **Observation**: "It is raining."
    4.  **Thought**: "I should suggest an umbrella."
    5.  **Answer**: "Take an umbrella."

## 3. Tool Use (Function Calling)
The model is fine-tuned to output JSON structures like `{ "function": "get_weather" }` instead of plain text when it detects a need for external data.
