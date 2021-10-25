# Django social app
Basically it is something like discord.

What we have now:
1) Authorization. Standard.
2) Room creating. Room represents separate page for discussing a theme provided by room's host.
3) Topics. Depends on room theme you can choose the topic or create new one. Just to sort things.
4) Activity feed - shows last actions on the site. Is going to be more specific depending on the topic you choose.
5) User profile. Shows user avatar, bio, rooms you created.
6) Small REST API. Is going to be developed.

Right now it is deployed on AWS. Server part = Elastic Beanstalk, database = RDS PostgreSQL, static files = S3 Bucket.
Praise the su... Amazon!
Why AWS? Because I never done this before and my Heroku free tier is no more.


Plans for this app:
1) Check security issues. There are a lot of them
2) Make it possible for app to add files to S3 Bucket
3) Discover what is wrong with registartion button
4) Work on site style a little. May be set some background.
5) Email verification?
6) Password reset?
7) More Noticable edit and delete buttons for rooms, messages etc.

___
Notes for myself:

Some note about project itself (it may duplicate notes from code):

..........................WRITE ME.......................................
___
** How deploy to AWS:

Follow this guide https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
Keep in mind:
	1) Make sure you get requirements.txt from project env and not global env. Command: project_env/bin/python3 -m pip freeze > requirements.txt
	2) When initializing your EB CLI repository with "eb init" better specify the region you want to use. Command: eb init -p python-3.8 ..._cli_name --region eu-central-1
	3) VERY IMPORTANT: make sure your default (eb configure) AWS_ACCESS_KEY_ID, AWS_SECERET_ACCESS_KEY are active. You may check it in your AWS profile.
	4) Add '127.0.0.1' to ALLOWED_HOSTS, if you want to test your app locally.
	5) Configure Permissions for your AWS Beanstalk enviroment, so you can access it.

Connect PostgreSQL to AWS RDS guide: https://www.youtube.com/watch?v=3HPq12w-dww&list=LL&index=2
But also:
	1) Make sure to add rule to RDS PostgreSQL instance security group where you specify EC2 Private IP, so the database could be accessible. "Edit inbound rules"
	2) The same thing is about your local IP. It also should be in this inbound rules, so you can access database to edit it.

Connect to S3 Bucket: https://www.youtube.com/watch?v=inQyZ7zFMHM&t=496s
Also:
	1) Same thing about rules. Check every permission.
	2) Check if your files/folders are publicly accessible. This is simpliest way to open them. You may check it by simply opening them with link in files descrition.
