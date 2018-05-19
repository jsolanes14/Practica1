Feature: Registrar Pronostic
  In order to guardar els pronostics que fan els usuaris
  As a user
  I want registrar el pronostic d’un partit no jugat

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just Pronostic pronosticPartit
    Given I login as user "user" with password "password"
    When I register Pronostic
      | pronosticPartit | comment |
      | 1 | Sera un bon partit |
    Then I'm viewing the details page for Match by "user"
      | pronosticPartit | comment |
      | 1 | Sera un bon partit |
    And There are 1 pronostic
