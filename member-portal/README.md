# ASRG Member Portal

The objective of the ASRG member portal is to provide a central place for members, chapter leads, region leads, and others to access information. Namely:
- Create an ASRG account.
- Login to ASRG account, view "main dashboard", displaying relevant information.
- Meetup-like functionality to facilitate local events around the world, and global events. Ideally, we will utilize "Chapter" by FreeCodeCamp (https://github.com/freeCodeCamp/chapter) as the mechanism to schedule/remind/organize/etc. At minimum, we need the following functionalities:
  - View local events (and see what else is going on at ASRG chapters globally!)
  - Register for a local event.
  - Register for a global event.
  - Post events.
- Access to ASRG threat intelligence information (ThreatQ embedded dashboard)
- Access to job postings.
- Access to "wiki" (embed or redirect to docs.asrg.io, which is powered by Gitbook).
- & MORE.



To start, this app is intended to be _least effort possible_ because we don't have the resources to support it. If you're interested in helping with this project (we need it), reach out to hello@asrg.io.

The core of the application will be built on the Django version of CoreUI. (https://github.com/app-generator/django-dashboard-coreui). They give a nice template for standard use cases in a basic UI (i.e. handles authentication/authorization/roles well). We'll take this template, and we will modify it to create a basic application that we can host as our member portal.

We're using Docker to launch the app. Clone the repo, run:

sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d

Then visit:

http://localhost:5005/

To modify the application, check out CoreUI's docs (https://coreui.io/docs/getting-started/introduction/). Mostly, it is tearing out the boiler plate stuff and inserting static ASRG relevant information. 
