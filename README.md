# Activity Rating Diary

Rate your frequent activities on how much you enjoy them and whether you achieved what you want from them

## Contents
[Scope](#scope)

[Organizing things](#organize)
   * [Requirements](#req)
   * [Agile](#agile)

[User Stories](#userS)
   * [Must Have](#mustH)
   * [Could Have](#couldH)


<a name="scope"></a>
# Scope

I do many activities every day. I would like to evaluate how much I achieved in terms of objectives. Also I would like to evaluate my level of ‘joy’ I experienced while doing the activities. I should be able to record an activity and do a rating for achievement and one for joy. Then I can get an average for achievement and joy.

<a name="organize"></a>
# Organizing things

<a name="req"></a>
## Requirements
I used a trello board to capture the requiremments visually and set delivery contraints


![Requirements](/images/trello_req.jpg)

<a name="agile"></a>
## Kanban board

I used a trello board to demonstrate agile way of working. Kanban board showed my working pipeline and its progress

![Agile](/images/trello_kanban.jpg)

<a name="userS"></a>
# User Stories

These are short, simple descriptions of the features desired and capabilities of the system

<a name="mustH"></a>
## Must have

These are the minimum features that must be in the first working application

1.	AS a professional 
I want to rate my daily activities
So that for each activity I can know how much I achieved and how much I enjoyed

2.	As a user
I want to add activity to the diary with description, date, time, its achievement and joy ratings
So that I know what my updated activity list look like

3.	As a user
I want to update an activity
So that I can track its new status

4.	As a user
I want to show my diary activities for a specified period with their ratings and the average for achievement and joy for the specified period
So that I know how I am performing 

5.	As a user
I want to delete an activity when it is done
So that I know what my updated activity list look like

<a name="couldH"></a>
## Could have

These features can be added at later application development sprints

1.	As a user
I want to logon on to my application
So that I can access my daily activities diary

2.	As a user
I want to logout of my application
So that I quit my activities diary

3.	As a user
I want to add activity with more details like start time, end time, involved partners, colleagues ...etc
So that I know what my updated activity list look like

# Use cases

These are a list of actions or event steps typically defining the interactions between a role represented by an actor and a system to achieve a goal. The actor can be a human or other external system.

## 1. logon - UC001
This use case starts when the user decides to logon to the application and it ends the logon is successful or being terminated.

## 2. Logout - UC002
This use case starts when the user decides to logout from the application and ends when the user is logged out.

## 3. Add - UC003
This use case starts when the user decides to add an activity, then enter activity details and select to add them.

## 4. Modify - UC004
This use case starts when the user decides to update or change details of an activity, then it ends when the user selects to save the new changes.

## Dsiaply - UC005
This use case starts when the user decides to display the list of activities, then it ends when the user selects close.

## Delete - UC006
This use case starts when the user decides to display the list of activities, then it ends when the user selects close.


