# Text2SQL

## 1. Unstructured vs Structured
*   **Unstructured**: PDF, Email, Slack. (Use Vector DB).
*   **Structured**: SQL Database, Excel, CSV. (Use Code Generation).

## 2. The Text2SQL Pipeline
1.  **User**: "Show me the top 3 customers by revenue."
2.  **Prompt**: "You are a SQL expert. Here is the schema: `Customers(id, name)`, `Orders(id, customer_id, amount)`. Write the query."
3.  **LLM**: `SELECT name, SUM(amount) FROM Customers JOIN Orders...`
4.  **Execute**: Run Python `cursor.execute()`.
5.  **Response**: "The top customers are..."

## 3. Schema Linking
If you have 100 tables, you can't paste the whole schema into the prompt.
You need a "Retriever" just to find the relevant tables (e.g., retrieving `Orders` table but ignoring `HR_Employee` table).
