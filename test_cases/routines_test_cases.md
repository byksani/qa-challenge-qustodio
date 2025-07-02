# Routines test cases
This document contains manual test cases for the Routines feature from the parent web experience in Qustodio.

## Test Case Overview
1. [Positive test cases](#positive-test-cases)
2. [Negative test cases](#negative-test-cases)

### Priority classification:
- **High** – critical scenarios that cover the core functionality of the Routines feature; 
without them, the feature does not work as intended
- **Medium** – important scenarios that affect user experience or behavior but are not blocking; 
there is a workaround or partial functionality still works
- **Low** – optional scenarios mostly related to UI or visual elements; 
they do not affect the main functionality

## Preconditions (apply to all test cases)
- User is logged in as a parent using valid credentials
- User has at least one family member added to the account
- The family member has a connected device 
- User is viewing the **Routines** page for that family member

---

## Positive test cases 

### TC-01: Create routine from preset
**Priority**: High  
**Test steps**:
1. Click the **Add routine** button
2. Select routine from list of presets
3. Set an available time slot
4. Click the **Save routine** button

**Expected results**: 
- Created routine appears in the list of routines
- Created routine appears in the calendar

### TC-02: Create a custom App & website routine (Ignore daily time limits)
**Priority**: High  
**Test steps**:
1. Click the **Add routine** button
2. Click the **Custom** button
3. Select **App & website rules** as routine type
4. Set up any combination of App and Website rules
5. On the "Choose a time limit option" screen, select **Recommended** (Ignore daily time limits) 
6. Enter a name of the routine
7. Set an available time slot
8. Click the **Save routine** button

**Expected results**:
- Routine is created with selected rule configuration 
- Created routine appears in the list of routines
- Created routine appears in the calendar
- Routine editor shows: **This routine ignores daily time limits**

### TC-03: Create a custom App & website routine (Apply daily time limits)
**Priority**: High  
**Test steps**:
1. Click the **Add routine** button
2. Click the **Custom** button
3. Select **App & website rules** as routine type
4. Set up any combination of App and Website rules
5. On the "Choose a time limit option" screen, select **Apply daily time limits**
6. Enter a name of the routine
7. Set an available time slot
8. Click the **Save routine** button

**Expected results**:
- Routine is created with selected rule configuration
- Created routine appears in the list of routines
- Created routine appears in the calendar
- Routine displays a **blue hourglass icon** next to the routine's icon 
- Routine editor shows: **Daily time limits apply to this routine**

### TC-04: Create a custom Device blocks routine
**Priority**: High  
**Test steps**:
1. Click the **Add routine** button
2. Click the **Custom** button
3. Select **Device blocks** as routine type
4. Choose either **Disconnect internet** or **Lock devices**
5. Enter a name of the routine
6. Set an available time slot
7. Click the **Save routine** button

**Expected results**:
- Routine is created with selected block rule configuration
- Created routine appears in the list of routines
- Created routine appears in the calendar

### TC-05: Exit routine editor without saving — show confirmation popup
**Priority**: Medium  
**Test steps**:
1. Click the **Add routine** button
2. Make any changes in the routine editor
3. Click the **X** icon or try to close the editor without saving

**Expected results**:
- A confirmation popup appears with a message that unsaved changes will be lost
- Popup contains **Leave** and **Cancel** buttons

### TC-06: Confirm exit without saving in routine editor
**Priority**: Medium  
**Precondition**: Routine editor is open with unsaved changes  
**Test steps**:
1. Click the **X** icon to close the editor
2. In the confirmation popup, click **Leave**

**Expected results**:
- Editor closes
- No changes are saved
- Routine is not created

### TC-07: Cancel exit without saving in routine editor
**Priority**: Medium  
**Precondition**: Routine editor is open with unsaved changes  
**Test steps**:
1. Click the **X** icon to close the editor
2. In the confirmation popup, click **Cancel**

**Expected results**:
- Popup closes
- User stays in the routine editor
- Changes remain visible and editable

### TC-08: Open and close routine from the list
**Priority**: Low  
**Precondition**: Family member has at least one routine in the list  
**Test steps**:
1. Click on a routine from the list
2. Routine editor opens
3. Click the **Done** button or the **Close** (X) icon

**Expected results**:
- Routine editor opens successfully
- Routine editor closes without saving any changes
- No data is modified
- User returns to the previous view

### TC-09: Disable a routine
**Priority**: High  
**Precondition**: Family member has at least one active routine  
**Test steps**:
1. Select an active routine from the list
2. Click the **Enable time slots** toggle to turn it off
3. Click the **Done** button

**Expected results**: 
- Routine is marked as **disabled** in the routine list
- The routine no longer appears in the calendar 

### TC-10: Enable a routine
**Priority**: High  
**Precondition**: Family member has at least one inactive routine  
**Test steps**:
1. Select an inactive routine from the list
2. Click the **Enable time slots** toggle to turn it on
3. Click the **Done** button

**Expected results**: 
- Routine is marked as **enabled** in the routine list
- The routine appears in the calendar 

### TC-11: Change style for a routine
**Priority**: Medium  
**Precondition**: Family member has at least one routine  
**Test steps**:
1. Select a routine from the list
2. Click the **Change style** button
3. Change the routine name
4. Change the color
5. Change the icon
6. Add/remove description: if it's filled, clear it; if it's empty, enter a description
7. Click the **Save and go back** button

**Expected results**: 
- Routine name, color, icon, and description (if changed) are updated in the routine list
- The calendar reflects the updated routine name and color

### TC-12: Update time slot for a routine
**Priority**: High  
**Precondition**: Family member has at least one active routine with a configured time slot  
**Test steps**:
1. Select an active routine from the list
2. Click the **Edit** icon on the existing time slot
3. Change the **From** and **To** fields to a new available time
4. Select a different day of the week (that does not overlap with other routines)
5. Click the **Save** button

**Expected results**:
- Routine is updated with the new time and day
- The calendar reflects the updated day and time for the routine

### TC-13: Add an additional time slot to a routine
**Priority**: Medium  
**Precondition**: Family member has at least one active routine with a configured time slot  
**Test steps**:
1. Select an active routine from the list
2. Click the **Add** button in the time slots section
3. Select an available time period and day that does not overlap with other routines
4. Click the **Save** button

**Expected results**:
- A new time slot is added to the routine
- The calendar displays the new time slot for the routine

### TC-14: Save overnight time slot (cross-day)
**Priority**: Medium  
**Precondition**: Family member has at least one active routine with a configured time slot  
**Test steps**:
1. Select an active routine from the list
2. Create a time slot that starts in the evening and ends the next morning (e.g., 21:00 to 07:00)
3. Click the **Save** button

**Expected results**:
- Time slot is saved correctly as overnight 
- Calendar displays the slot as spanning two calendar days 

### TC-15: Remove a time slot from an active routine
**Priority**: Medium  
**Precondition**: Family member has an active routine with at least two configured time slot  
**Test steps**:
1. Select an active routine from the list 
2. Click the **Edit** icon on the existing time slot 
3. In the time slots section, click the **Delete time slot** icon on a time slot
4. In the confirmation popup, click the **Delete** button

**Expected results**:
- The selected time slot is removed from the routine
- The calendar no longer displays the removed slot

### TC-16: Remove all time slots from an active routine
**Priority**: Medium  
**Precondition**: Family member has an active routine with configured time slot   
**Test steps**:
1. Select the active routine from the list
2. Click the **Edit** icon for time slot
3. Click the **Delete time slot** icon to delete a time slot
4. In the confirmation popup, click the **Delete** button

**Expected results**:
- The time slot is removed from the routine
- Routine remains **enabled** in the list
- Routine no longer appear in the calendar

### TC-17: Remove a time slot from an inactive routine
**Priority**: Medium  
**Precondition**: Family member has at least one inactive routine with a configured time slot  
**Test steps**:
1. Select an inactive routine from the list
2. In the time slots section, click the **Delete time slot** icon on a time slot
3. In the confirmation popup, click the **Delete** button

**Expected results**:
- The selected time slot is removed from the routine
- The calendar does not display the removed slot

### TC-18: Create routine from Study preset (App/Web rules)
**Priority**: Medium  
**Note**: The same behavior applies also to **Entertainment** preset  
**Test steps**:
1. Click the **Add routine** button
2. Select the **Study** preset
3. Click the **Save routine** button
4. Open the created routine

**Expected results**: 
- Routine is created with **App and websites rules** configuration
- App/Web rules section is visible in the routine editor

### TC-19: Create routine from Bedtime preset (Device block)
**Priority**: Medium  
**Note**: The same behavior applies also to **Focus** preset  
**Test steps**:
1. Click the **Add routine** button
2. Select the **Bedtime** preset
3. Click the **Save routine** button
4. Open the created routine

**Expected results**:
- Routine is created with **Device block** configuration
- Block rules section is visible in the routine editor

### TC-20: Change App rules — allow all apps with blocked exceptions
**Priority**: Medium  
**Precondition**: Family member has an active App/Web-based routine with **Block all apps** setting  
**Note**: This test also applies to the case when no exceptions are added  
**Test steps**:
1. Select the routine from the list
2. Click the **Edit app rules** button
3. Select **Allow all apps**
4. Add at least one app to the **App exceptions** list
5. Click the **Done** button

**Expected results**:
- Routine is saved with the **Allow all apps** setting
- Blocked exceptions list is preserved (if any)

### TC-21: Change App rules — block all apps with allowed exceptions
**Priority**: Medium  
**Precondition**: Family member has an active App/Web-based routine with **Allow all apps** setting  
**Note**: This test also applies to the case when no exceptions are added  
**Test steps**:
1. Select the routine from the list
2. Click the **Edit app rules** button
3. Select **Block all apps**
4. Add at least one app to the **App exceptions** list
5. Click the **Done** button

**Expected results**:
- Routine is saved with the **Block all apps** setting
- Allowed exceptions list is preserved (if any)

### TC-22: Change Website rules — allow all categories
**Priority**: Medium  
**Precondition**: Family member has an active App/Web-based routine with **Block all website categories** setting  
**Note**: The confirmation popup appears only if category exceptions have already been selected.  
**Test steps**:
1. Select the routine from the list 
2. Click the **Edit website rules** button
3. Select **Allow all website categories**
4. Click the **Change** button in the confirmation popup (if it does)
5. Click the **Done** button

**Expected results**:
- Routine is saved with the **Allow all website categories** setting 
- Default category exceptions are automatically added

### TC-23: Change Website rules — block all categories with allowed exceptions
**Priority**: Medium  
**Precondition**: Family member has an active App/Web-based routine with **Allow all website categories** setting  
**Note**: The confirmation popup appears only if category exceptions have already been selected.  
**Test steps**:
1. Select the routine from the list
2. Click the **Edit website rules** button
3. Switch to **Block all website categories** 
4. Click the **Change** button in the confirmation popup (if it does)
5. Click the **Add** button in the exceptions section
6. Add one or more website categories to the exception list
7. Click the **Save and go back** button
8. Click the **Done** button

**Expected results**:
- Routine is saved with the **Block all website categories** setting
- Allowed category exceptions are preserved

### TC-24: Remove all selected website categories
**Priority**: Medium  
**Precondition**: Family member has an active App/Web-based routine with categories exceptions already selected  
**Test steps**:
1. Select the routine from the list
2. Click the **Edit website rules** button
3. Click the **Remove all** button
4. In the confirmation popup, click the **Remove** button
5. Click the **Done** button

**Expected results**:
- All website category exceptions are cleared
- Routine is saved with an empty exceptions list

### TC-25: Change rules for routine with Device block type
**Priority**: Medium  
**Precondition**: Family member has an active routine with **Device block** configuration  
**Test steps**:
1. Select the routine from the list
2. Click the **Edit rules** button
3. Choose a different rule type (e.g., Disconnect the internet or Lock devices)
4. Click the **Save** button

**Expected results**:
- Routine is saved with selected rule type 

### TC-26: View rule description popup for Device block type routine
**Priority**: Low  
**Precondition**: Family member has an active routine with **Device block** configuration  
**Test steps**:
1. Select the routine from the list
2. Click the **Edit rules** button
3. Click the More info icon next to each block rule mode

**Expected results**:
- A popup appears showing a description for the selected block rule mode
- The popup can be closed

### TC-27: Open routine by clicking on calendar slot
**Priority**: Medium  
**Precondition**: At least one routine is visible in the calendar  
**Test steps**:
1. Hover over any routine in the calendar view
2. Observe the tooltip
3. Click the routine block

**Expected results**:
- Tooltip displays the name of the routine
- Routine settings page opens after click 

### TC-28: Create routine via calendar view
**Priority**: Medium  
**Test steps**:
1. Click the **Add routine** button in the calendar view
2. Select a preset or create a custom routine
3. Configure the time slot
4. Click the **Save routine** button

**Expected results**:
- Routine is created with the selected configuration
- User remains in the calendar view after saving 
- Calendar automatically updates to show the new routine 

### TC-29: Display of current time in calendar
**Priority**: Low    
**Test steps**:  
1. Open the calendar view  
2. Observe the horizontal line representing current time  

**Expected results**:  
- A horizontal line is shown at the current time  
- Time is displayed according to the parent account's time zone settings  
- The line updates dynamically as time progresses

### TC-30: Delete a routine
**Priority**: Medium  
**Precondition**: Family member has at least one routine  
**Test steps**:
1. Open the routine settings 
2. Click the **Delete routine** button
3. In the confirmation popup, click the **Delete** button

**Expected results**:
- Routine is removed from the routine list
- All associated time slots are removed from the calendar

### TC-31: Cancel routine deletion from routine settings
**Priority**: Medium  
**Precondition**: Family member has at least one routine  
**Test steps**:
1. Open the routine settings
2. Click the **Delete routine** button
3. In the confirmation popup, click the **Cancel** button

**Expected results**:
- Confirmation popup is closed
- User is returned to the routine settings view
- Routine is not deleted

---

## Negative test cases

### TC-32: Time slot overlaps with another routine
**Priority**: Medium  
**Precondition**: Family member has at least two active routine  
**Test steps**:
1. Select an active routine from the list
2. Edit an existing time slot or add a new one
3. Change a time and day that overlaps with another routine 

**Expected results**:
- Save button is disabled 
- Warning message is displayed: *"{Routine name} is already scheduled at this time."*

### TC-33: Enable routine with conflicting time slot
**Priority**: Medium  
**Precondition**: Family member has an inactive routine with a time slot that overlaps with another active routine  
**Test steps**:
1. Select the inactive routine
2. Toggle the **Enable time slots** option to ON 

**Expected results**:
- Error popup appears: *"Can't enable this slots. Some time slots overlap with other routines so they can't be enabled."*
- User must click **OK** or **X** icon to dismiss the popup
- Routine remains disabled

### TC-34: Create custom routine without selecting day or valid time
**Priority**: Medium  
**Test steps**:
1. Click **Add routine**
2. Choose **Custom**
3. Set up any combination of App/website and Blocks rules
4. Set a name
5. Do one of the following:
   a. Don’t select any day
   b. Enter an invalid time manually (e.g., "99:99")
6. Attempt to click **Save routine**

**Expected results**:
- Save button is disabled
- Error message appears: *"Please enter a time slot and select at least one day."*

### TC-35: Save routine with empty name
**Priority**: Medium  
**Precondition**: Routine editor is open  
**Test steps**:
1. Clear the routine name input
2. Click the **Save and go back** button 

**Expected results**:
- Save button is disabled
- Error message is shown: *"Please choose a name for this routine."*

### TC-36: Enter routine name longer than 28 characters
**Priority**: Low  
**Test steps**:
1. In the routine editor, enter a name with more than 28 characters
2. Observe behavior at the 29th character

**Expected results**:
- Save button is disabled
- Error message appears: *"Name should not be longer than 28 characters."*

### TC-37: Create routine with duplicate name
**Priority**: Medium  
**Precondition**: Family member already has a routine named "Study"  
**Test steps**:
1. Create a new routine 
2. Enter "Study" as the routine name
3. Click **Save routine**

**Expected results**:
- Save button is disabled
- Error message appears: *"A routine with this name already exists for {Family member name}."*

### TC-38: Save routine with lost internet connection
**Priority**: Medium  
**Test steps**:
1. Fill out the routine creation form correctly
2. Disconnect internet connection (or enable **Offline** mode in DevTools)
3. Click **Save routine**

**Expected results**:
- A popup appears with error: *"Whoops! Something's gone wrong. Please check your connection and try again."*
- Routine is not saved
