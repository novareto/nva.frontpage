# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s nva.frontpage -t test_vorschau.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src nva.frontpage.testing.NVA_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/nva/frontpage/tests/robot/test_vorschau.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Vorschau
  Given a logged-in site administrator
    and an add Landingpage form
   When I type 'My Vorschau' into the title field
    and I submit the form
   Then a Vorschau with the title 'My Vorschau' has been created

Scenario: As a site administrator I can view a Vorschau
  Given a logged-in site administrator
    and a Vorschau 'My Vorschau'
   When I go to the Vorschau view
   Then I can see the Vorschau title 'My Vorschau'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Landingpage form
  Go To  ${PLONE_URL}/++add++Landingpage

a Vorschau 'My Vorschau'
  Create content  type=Landingpage  id=my-vorschau  title=My Vorschau

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Vorschau view
  Go To  ${PLONE_URL}/my-vorschau
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Vorschau with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Vorschau title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
