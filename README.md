This is my second project for my internship at the company Qpick
This is a Django mysite and polls project developed in Pychram Pro

To clone this project you will need to click on the green button Code and copy the HTTPS link 
after that you will open Pycharm and in the terminal you will write 
git clone HTTTP link
or you can downlad it and open it in Pycharm;




To start the mysite.py django projects you need to check in your terminal if you have instaled 
django ( py -m django --version ); 

After that you need to type in your terminal < django-admin startproject mysite > ;
And after that you will see the mysite project in you directory 
and check if is it working by writing in your terminal < py manage.py runserver > 
and you should see a message in you terminal somethilike this
After clicking on the link you should be directed on a django website that the server and the app is working ; 
{
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

October 23, 2020 - 15:50:53
Django version 3.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

}

You will need to go to the outside directory of mysite and in TOOLS you will need to click the 

 Run manage.py Task... ( CTRL + ALT + R  )
in the terminal you will need to write < py manage.py startapp polls > and this will create the app polls ;
After writing some codes you will need to run the server again < py manage.py runserver >
after clicking on the link in the url you will need to add < /polls >
