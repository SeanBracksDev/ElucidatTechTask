Feature: Voting Kevin's case
    Background: User navigates to the voting page
        Given a user is on the voting page for kevin's case

    Scenario: Vote Kevin is "Guilty"
        When a user votes that kevin is Guilty
        Then the prompt should reflect that the user voted Guilty

    Scenario: Vote Kevin is "Not guilty"
        When a user votes that kevin is Not guilty
        Then the prompt should reflect that the user voted Not guilty