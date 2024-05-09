Feature: Initial Score
    Background: User navigates to home page
        Given a user is on home page

    Scenario: Visit site and verify initial score is 0
        When a user visits the course and clicks the START button
        Then the users score should be 0