# Task: Schema Ambiguity

## Objective
Debugging SQL generation.

## Setup
*   Table `Sales` has column `amount` (in USD) and `quantity` (units sold).
*   User asks: \"What were the sales last week?\"
*   Model might generate: `SUM(quantity)` (Units) OR `SUM(amount)` (Revenue).

## Task
1.  This is ambiguous.
2.  If the model guesses wrong, the CEO gets the wrong number.
3.  **Solution**: Few-Shot Prompting. Use an example in the prompt: \"User: Sales. SQL: SUM(amount)\". Or, add `COMMENT` to the SQL schema: `amount COMMENT 'Revenue in USD', quantity COMMENT 'Number of units sold'`.

## Question
Why is `SELECT *` dangerous in RAG?
*   Answer: Context Window overflow. If `Users` has 1 Million rows, `SELECT *` will crash the LLM. Always enforce `LIMIT` in the system prompt.
