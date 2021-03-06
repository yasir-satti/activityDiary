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

[Risk assessment](#risk)

[User Cases](#userC)
   * [Login](#login)
   * [Logout](#logout)
   * [Add](#add)
   * [Modify](#modify)
   * [Display](#display)
   * [Delete](#delete)

[Entiry Relationship Diagram](#ERD)

[Application Wireframe](#appUI)

[Deployment](#Deploy)

[Tests](#Tests)

[Technology stack used](#TechStack)



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

* [Kanban board](https://trello.com/b/PsqraGjP/daily-activities)

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

<a name="risk"></a>
# Risk assessment

## MVP development steps

Ensure producing incremental working app with each sprint. Broken down app developmwnt to steps:

1. App pages and navigation
2. Creating and writing to database
2. Reading from database and display
3. updating/modifying data
4. Delete data

## Time constraint

Limited time to produce the app require making progress in specific time frame for each development step. If progress is not made as planned then need to seek support to overcome issues and be able to deliver.

## Infrastructure technology setup being stable and available

Technology stack used relied mainly on cloud solutions. If it becomes not available or not reilable then need to prepare local development setup and backup

## Programming knowledge and support to produce CRUD application

1. Understanding software programming principles and their relations
2. Understanding programming language and ability to translate app behaviour logic using programming language into working app




<a name="useC"></a>
# Use cases

These are a list of actions or event steps typically defining the interactions between a role represented by an actor and a system to achieve a goal. The actor can be a human or other external system.

For detailed content on the each use case refer to 
* [Use cases](https://github.com/yasir-satti/activityDiary/blob/master/docs/proj_use_cases.pdf)

<a name="login"></a>
## 1. Login - UC001
This use case starts when the user decides to logon to the application and it ends the logon is successful or being terminated.

<a name="Logout"></a>
## 2. Logout - UC002
This use case starts when the user decides to logout from the application and ends when the user is logged out.

<a name="add"></a>
## 3. Add - UC003
This use case starts when the user decides to add an activity, then enter activity details and select to add them.

<a name="modify"></a>
## 4. Modify - UC004
This use case starts when the user decides to update or change details of an activity, then it ends when the user selects to save the new changes.

<a name="display"></a>
## Display - UC005
This use case starts when the user decides to display the list of activities, then it ends when the user selects close.

<a name="delete"></a>
## Delete - UC006
This use case starts when the user decides to display the list of activities, then it ends when the user selects close.

<a name="ERD"></a>
# Entity Relationship Diagram

An entity relationship diagram (ERD) shows the relationships of entity sets stored in a database. An entity in this context is an object, a component of data. An entity set is a collection of similar entities. These entities can have attributes that define its properties. An ER diagram illustrates the logical structure of databases. 

We have 2 tables:

1. Users: this table stores each application user's details

2. Activities: here each user's activities are stored with its details


![ERD](/images/ERD.jpg)

<a name="appUI"></a>
# Application wireframe

## Login

![login_wf](/images/wire_frame_002_login.jpg)

## Landing page

![landing_wf](/images/wire_frame_001_landing_page.jpg)

## Create activity list

![activity_list_wf](/images/wire_frame_005_add_create_activity_list_items.jpg)

## Add activity item rating

![activity_rating_wf](/images/wire_frame_003_add_activity_rating.jpg)

## Add activity item rating

![activity_display_wf](/images/wire_frame_004_add_display_activity_rating.jpg)

<a name="tests"></a>
# Tests

<a name="deploy"></a>
# Deployment

Jenkins was used during development to deploy working app

1. After each app increment working code was pushed to git hub repository and Jenkins received a webhook trigger to deploy it

2. Deployed app was working as systemd service where after succssful deployment just required app web page refresh to access new features


<a name="techstack"></a>
# Technology stack used

1. Python
2. Flask framework
3. Linux VM on Google Cloud Platform (GCP)
4. MySQL DB on Google Cloud Platform (GCP)
5. Jenkins
6. Github
7. Linux
8. Draw.io
9. Wireframe draw
10 Visual Studio Code (VSCODE) IDE




