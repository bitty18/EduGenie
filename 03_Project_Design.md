3. Project Design Phase --- EduGenie

1. Technology Stack

Python

Python is used for the application logic, input handling, conditions and
displayed output.

Streamlit

Streamlit provides the web interface directly from Python. Widgets such
as titles, text inputs, text areas and buttons are created through
Streamlit functions.

Google Gemini

Google Gemini is the planned AI service layer. The planned integration
will send prompts and receive generated text.

GitHub

GitHub is used for source-code hosting, version control, issue tracking
and collaboration.

Streamlit Community Cloud

Cloud deployment is planned for the application.

2. Architecture

EduGenie follows a simple two-layer architecture in the current
prototype:

1.  Presentation Layer --- Streamlit interface.
2.  Logic Layer --- Python code in `app.py`.

The planned version adds: 
3. AI Service Layer --- Google Gemini API.
4. Storage Layer (future) --- database or files for history, notes
and results.

3. Data Flow

1.  Student opens the application in a browser.
2.  Student enters a question, topic or notes.
3.  Student clicks the relevant button.
4.  Streamlit re-runs `app.py`.
5.  Input is checked.
6.  Empty input produces a warning.
7.  Valid input produces the relevant response.
8.  In the planned version, the input will be inserted into a prompt and
    sent to Gemini.





4. Design Principles

-   Single responsibility
-   Consistency
-   Feedback
-   Simplicity
-   Extensibility


5. User Interface Layout

The page uses a centered layout.

  Order   Section              Widgets
  ---------------------------------------------------------------------- 
  1       Header               Title, subheader and introduction
  2       Ask a question       Text input + Ask EduGenie button
  3       Topic explainer      Text input + Explain Topic button
  4       Notes summarizer     Multi-line text area + Summarize Notes button
  5       Practice questions   Text input + Generate Questions button

6. Module Design

Module 1 --- Ask EduGenie

Input: student question\
Output: answer

Module 2 --- Topic Explainer

Input: topic name\
Output: simple explanation

Module 3 --- Notes Summarizer

Input: multi-line notes\
Output: short revision points

Module 4 --- Practice Question Generator

Input: topic\
Output: practice questions

7. Planned Prompt Design

-   Ask EduGenie: clear and brief answer with one example.
-   Topic Explainer: beginner-friendly explanation with a real-life
    analogy.
-   Notes Summarizer: 5--8 short revision bullets.
-   Practice Questions: five questions including multiple-choice,
    short-answer and application questions.



