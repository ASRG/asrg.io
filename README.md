# Welcome to the asrg.io github account.  

Join the discussion in our Slack channel: [Link](https://join.slack.com/t/asrg/shared_invite/enQtNTYzMjE5NDcyMzUyLWZmMzBhYTRmMzIzZDMyODA5NDkwZDc0Y2EwMDc5NjM2ODhlYWM5NjVlZjY3OWQyMGZhMDljNWI5ZDI1OWUzMDc)

## Why does this exist?

ASRG.io is constantly being developed to bring new benefits to the ASRG's membership around the world. As a non-profit, we need help. We believe that providing a platform for members to use will *fundamentally* impact vehicle safety by creating a place to share *knowledge*, facilitate *networking*, and foster *collaboration*.

ASRG.io is the main member portal that we are seeking to centralize our member's user experience around. It will be the single point of contact with all of our members and leads. In the same place, we imagine our regional/local leads and academic leads to *schedule* events and members to *view events/attend events*. We imagine a tab where members can access the "Automotive Security Intelligence Project (ASIP)", effectively allowing the member to get an update on the latest intelligence in the space. We imagine job postings by companies that our members can access. We imagine an education platform in the member portal that allows our members to learn about topics in automotive security.

To date, this portal has been developed by volunteers. Check out the latest release at https://asrg.io. If you want to participate in developing this platform to serve the industry and ultimately make vehicles more safe, reach out to us at hello@asrg.io (or message in github - really, just get in contact any way :) ).

For more information on contributing (e.g. writing code), visit {INSERT LINK TO CONTRIBUTING} to learn how to pull the member portal locally and start pushing changes.

## Project Technical Background

Because we're all volunteers with limited time, we chose the path of least resistance to build this portal. Thus, we chose *Django* to build this web app. The core of the application was built on the Django+Gunicorn version of CoreUI. (https://github.com/app-generator/django-dashboard-coreui). They gave a nice template for standard use cases in a basic UI (i.e. handles authentication/authorization/roles well). They also gave us a nicely bundled database (Postgres) and proxy (nginx) all bundled neatly in a docker container that makes it easy to develop on AND deploy to our server.

Link to CoreUI: https://coreui.io/?ref=appseed

###Running the Django app [TODO]

##Management
Tasks for feature development on this project are managed in Github Projects via sprints.

##Using the Member Portal.
