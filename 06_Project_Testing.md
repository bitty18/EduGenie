6. Project Testing --- EduGenie

1. Testing Approach

Testing of the current prototype focuses on functional behaviour and
input validation.

Because current responses are static demonstration responses, expected
outputs are known in advance. Testing was performed manually by running
the application and interacting with each widget.

Additional testing will be needed after Gemini integration for response
quality, error handling and response time.

2. Test Cases

  -----------------------------------------------------------------------
  ID                Feature           Input             Expected Result
  ----------------- ----------------- ----------------- -----------------
  TC1               Ask EduGenie      Text entered +    Success message
                                      button clicked    and answer
                                                        displayed

  TC2               Ask EduGenie      Empty input +     Warning asking
                                      button clicked    for a question

  TC3               Explain Topic     Topic entered +   Success message
                                      button clicked    and explanation
                                                        displayed

  TC4               Explain Topic     Empty input +     Warning asking
                                      button clicked    for a topic

  TC5               Summarize Notes   Notes pasted +    Success message
                                      button clicked    and summary
                                                        displayed

  TC6               Summarize Notes   Empty text area + Warning asking
                                      button clicked    for notes

  TC7               Generate          Topic entered +   Three practice
                    Questions         button clicked    questions
                                                        displayed

  TC8               Generate          Empty input +     Warning asking
                    Questions         button clicked    for a topic

  TC9               Page Load         Open application  Title, subheader
                                                        and all four
                                                        sections visible

  TC10              Layout            Resize browser    Content stays
                                      window            centered and
                                                        readable
  -----------------------------------------------------------------------



3. Test Results

According to the project documentation, all ten test cases behaved as
expected in the current version.

The tests confirmed: - Empty input does not crash the application. -
Messages appear in the correct place. - The layout remains readable. -
The prototype answer is fixed regardless of the entered question.

The fixed-answer behaviour is expected for the prototype and is intended
to be replaced by Gemini integration.

4. Future Testing

After AI integration, testing should additionally cover: - Generated
response quality - API errors - Rate limits - Response time - Prompt
behaviour - Error messages



