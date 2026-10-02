2. Requirement Analysis --- EduGenie

1. Project Scope

The current scope includes: - Four learning features - Input
validation - A centered single-page layout - Consistent visual style
using icons and headings

Planned but not yet implemented: - Live Gemini API connection -
Conversation history - User accounts - Saving summaries and questions -
PDF export

2. Functional Requirements

  -----------------------------------------------------------------------
  ID                      Requirement             Description
  -----------------------------------------------------------------------
  FR1                     Ask a question          Accept a student
                                                  question and display an
                                                  answer

  FR2                     Explain a topic         Accept a topic name and
                                                  display a simple
                                                  explanation

  FR3                     Summarize notes         Accept pasted notes and
                                                  display a short summary

  FR4                     Generate questions      Accept a topic and
                                                  display practice
                                                  questions

  FR5                     Input validation        Show a warning when a
                                                  button is clicked with
                                                  empty input

  FR6                     Feedback message        Show a success message
                                                  when valid input is
                                                  received
  -----------------------------------------------------------------------

3. Non-Functional Requirements

-   Usability: A first-time user should be able to operate the
    interface without instructions.
-   Performance: Static responses should appear instantly; planned
    AI responses should appear within a few seconds.
-   Portability: The application should run on Windows, macOS and
    Linux where Python is installed.
-   Maintainability: Code should be short, organized and easy to
    extend.
-   Reliability: Empty input should not crash the application.
-   Security: API keys must remain outside the source code and must
    not be uploaded to GitHub.




4. User Requirements

* Students should be able to enter a question, topic or notes, select the appropriate learning function and receive a formatted result.

5. Current Limitations Relevant to Requirements

* The current implementation uses demonstration/static responses. Gemini integration, history, accounts, saving and PDF export are planned rather than current features.

6. Requirement Summary

* EduGenie is designed around four simple student workflows with
consistent input, processing and output behaviour.

**Source basis:** EduGenie Project Documentation, pages 3--6.

