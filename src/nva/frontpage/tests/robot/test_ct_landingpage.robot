# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s nva.frontpage -t test_landingpage.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src nva.frontpage.testing.NVA_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/nva/frontpage/tests/robot/test_landingpage.robot
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

Scenario: As a site administrator I can add a Landingpage
  Given a logged-in site administrator
    and an add Landingpage form
   When I type 'My Landingpage' into the title field
    and I submit the form
   Then a Landingpage with the title 'My Landingpage' has been created

Scenario: As a site administrator I can view a Landingpage
  Given a logged-in site administrator
    and a Landingpage 'My Landingpage'
   When I go to the Landingpage view
   Then I can see the Landingpage title 'My Landingpage'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Landingpage form
  Go To  ${PLONE_URL}/++add++Landingpage

a Landingpage 'My Landingpage'
  Create content  type=Landingpage  id=my-landingpage  title=My Landingpage

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Landingpage view
  Go To  ${PLONE_URL}/my-landingpage
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Landingpage with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Landingpage title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
